"""Pure Tree-sitter detyping pipeline for the Cinder backend."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from tree_sitter import Node

from ..core.types import DetypedProgram, Permutation, perm_name
from .ast_utils import (
    FunctionDefInfo,
    all_function_defs,
    iter_named,
    node_text,
    parse_source,
    root_function_defs,
    span_key,
)
from .generators import wrap_args_for
from .plan_data import FuncInfo, PlanData, build_plan_data
from .rules import body_policy_for, classify_type, param_policy_for, return_policy_for
from .tasks import (
    Arg,
    PreserveArg,
    build_checked_list_param_binding_stmt,
    build_preserve_argument_mutations_wrapper,
    build_rewrite_param_binding_stmt,
    call_arg_index,
    make_wrap_expr,
    wrap_expr,
)
from .unparse import Edit, unparse

GuideType = dict[str, bool]


@dataclass
class RewriteState:
    source: str
    root: Node
    defs: list[FunctionDefInfo]
    plan: PlanData
    info_by_span: dict[tuple[int, int], FunctionDefInfo]
    used_top_level_names: set[str]
    generated_wrapper_names: set[str] = field(default_factory=set)
    wrapper_defs: list[str] = field(default_factory=list)
    requires_cast: bool = False
    requires_box: bool = False

    def register_wrapper(self, callee_name: str, args: list[PreserveArg], n_args: int) -> str:
        arg_suffix = '_'.join(f'arg{arg.index}' for arg in sorted(args, key=lambda item: item.index))
        base = f'_repro_{callee_name}_{arg_suffix}'
        name = base
        suffix = 2
        while name in self.used_top_level_names or name in self.generated_wrapper_names:
            name = f'{base}_{suffix}'
            suffix += 1
        self.generated_wrapper_names.add(name)
        self.wrapper_defs.append(build_preserve_argument_mutations_wrapper(name, n_args, args))
        return name


def _top_level_function_names(root: Node, source: str) -> set[str]:
    names: set[str] = set()
    for child in iter_named(root):
        if child.type == 'function_definition':
            names.add(node_text(source, child.child_by_field_name('name')))
        if child.type == 'decorated_definition':
            for inner in iter_named(child):
                if inner.type == 'function_definition':
                    names.add(node_text(source, inner.child_by_field_name('name')))
    return names


def _line_start(source: str, byte_offset: int) -> int:
    return source.rfind('\n', 0, byte_offset) + 1


def _indent_before(source: str, node: Node) -> str:
    return source[_line_start(source, node.start_byte):node.start_byte]


def _apply_local_replacements(
    source: str,
    parent: Node,
    replacements: list[tuple[int, int, str]],
) -> str:
    if not replacements:
        return node_text(source, parent)

    pieces: list[str] = []
    cursor = parent.start_byte
    for start, end, replacement in sorted(replacements, key=lambda item: item[0]):
        pieces.append(source[cursor:start])
        pieces.append(replacement)
        cursor = end
    pieces.append(source[cursor:parent.end_byte])
    return ''.join(pieces)


def _import_insert_byte(source: str, root: Node) -> int:
    insert_at = 0
    for child in iter_named(root):
        if child.type in ('import_statement', 'import_from_statement'):
            insert_at = child.end_byte
            if insert_at < len(source) and source[insert_at:insert_at + 1] == '\n':
                insert_at += 1
    return insert_at


def _imported_static_names(source: str, root: Node) -> set[str]:
    imported: set[str] = set()
    for child in iter_named(root):
        if child.type != 'import_from_statement':
            continue
        parts = iter_named(child)
        if not parts:
            continue
        if node_text(source, parts[0]) != '__static__':
            continue
        for part in parts[1:]:
            if part.type == 'aliased_import':
                alias = part.child_by_field_name('alias')
                name = part.child_by_field_name('name')
                if alias is not None:
                    imported.add(node_text(source, alias))
                elif name is not None:
                    imported.add(node_text(source, name))
                continue
            imported.add(node_text(source, part))
    return imported


def _param_text_without_annotation(source: str, param_node: Node, new_name: str | None = None) -> str:
    if param_node.type == 'identifier':
        return new_name or node_text(source, param_node)
    if param_node.type == 'default_parameter':
        name_node = param_node.child_by_field_name('name')
        value_node = param_node.child_by_field_name('value')
        if name_node is None or value_node is None:
            return node_text(source, param_node)
        return f'{new_name or node_text(source, name_node)}={node_text(source, value_node)}'
    if param_node.type == 'typed_default_parameter':
        name_node = param_node.child_by_field_name('name')
        value_node = param_node.child_by_field_name('value')
        if name_node is None or value_node is None:
            return node_text(source, param_node)
        return f'{new_name or node_text(source, name_node)}={node_text(source, value_node)}'
    if param_node.type == 'typed_parameter':
        named = iter_named(param_node)
        if not named:
            return node_text(source, param_node)
        first = named[0]
        if first.type != 'identifier':
            return node_text(source, param_node)
        return new_name or node_text(source, first)
    return node_text(source, param_node)


def _assignment_node(stmt: Node) -> Node | None:
    if stmt.type != 'expression_statement':
        return None
    named = iter_named(stmt)
    if len(named) != 1:
        return None
    if named[0].type != 'assignment':
        return None
    if named[0].child_by_field_name('type') is None:
        return None
    return named[0]


def _is_descendant_of(node: Node, ancestor: Node | None) -> bool:
    if ancestor is None:
        return False
    current: Node | None = node
    while current is not None:
        if current == ancestor:
            return True
        current = current.parent
    return False


def _is_load_identifier(node: Node) -> bool:
    if node.type != 'identifier':
        return False

    current: Node | None = node
    while current is not None:
        parent = current.parent
        if parent is None:
            return True

        if parent.type in ('import_statement', 'import_from_statement', 'aliased_import', 'dotted_name'):
            return False
        if parent.type in ('function_definition', 'class_definition') and parent.child_by_field_name('name') == current:
            return False
        if parent.type in ('typed_default_parameter', 'default_parameter') and parent.child_by_field_name('name') == current:
            return False
        if parent.type == 'keyword_argument':
            named = iter_named(parent)
            if named and named[0] == current:
                return False
        if parent.type == 'attribute':
            named = iter_named(parent)
            if named and named[-1] == current:
                return False
        if parent.type in ('assignment', 'augmented_assignment', 'for_statement'):
            if _is_descendant_of(node, parent.child_by_field_name('left')):
                return False
        current = parent

    return True


def _argument_text(state: RewriteState, node: Node, current_func: FunctionDefInfo | None, env: dict[str, str]) -> str:
    if node.type == 'keyword_argument':
        named = iter_named(node)
        if len(named) == 2 and named[0].type == 'identifier':
            return f'{node_text(state.source, named[0])}={_rewrite_node(state, named[1], current_func, env)}'
    return _rewrite_node(state, node, current_func, env)


def _first_positional_arg(node: Node) -> Node | None:
    args = node.child_by_field_name('arguments')
    if args is None:
        return None
    for child in iter_named(args):
        if child.type not in ('keyword_argument', 'dictionary_splat'):
            return child
    return None


def _call_kind_and_name(state: RewriteState, node: Node) -> tuple[str, str] | None:
    func_node = node.child_by_field_name('function')
    if func_node is None:
        return None
    if func_node.type == 'identifier':
        return ('function', node_text(state.source, func_node))
    if func_node.type == 'attribute':
        named = iter_named(func_node)
        if named and named[-1].type == 'identifier':
            return ('method', node_text(state.source, named[-1]))
    return None


def _rewrite_call(
    state: RewriteState,
    node: Node,
    current_func: FunctionDefInfo | None,
    env: dict[str, str],
) -> str:
    func_node = node.child_by_field_name('function')
    arg_list = node.child_by_field_name('arguments')
    if func_node is None or arg_list is None:
        return node_text(state.source, node)

    func_text = _rewrite_node(state, func_node, current_func, env)
    arg_children = iter_named(arg_list)
    arg_texts = {span_key(child): _argument_text(state, child, current_func, env) for child in arg_children}
    positional = [child for child in arg_children if child.type not in ('keyword_argument', 'dictionary_splat')]
    base_arg_list = _apply_local_replacements(
        state.source,
        arg_list,
        [(child.start_byte, child.end_byte, arg_texts[span_key(child)]) for child in arg_children],
    )
    base_call = _apply_local_replacements(
        state.source,
        node,
        [
            (func_node.start_byte, func_node.end_byte, func_text),
            (arg_list.start_byte, arg_list.end_byte, base_arg_list),
        ],
    )

    call_info = _call_kind_and_name(state, node)
    if call_info is None:
        return base_call

    kind, callee_name = call_info
    plan_info = state.plan.funcs.get(callee_name)
    if plan_info is None or not plan_info.is_detyped:
        return base_call

    positional_texts = [arg_texts[span_key(child)] for child in positional]
    preserve_args: list[PreserveArg] = []
    param_count = len(plan_info.param_types)

    for index, typ in enumerate(plan_info.param_types):
        if typ is None:
            continue
        policy = param_policy_for(typ)
        arg_index = call_arg_index(kind == 'method', index, param_count, len(positional_texts))
        if arg_index is None:
            continue

        if 'preserve_argument_mutations' in policy.call_edits:
            preserve_args.append(PreserveArg(arg_index, typ))
            continue

        wraps = wrap_args_for(policy.call_edits, typ)
        if wraps:
            if any(arg.typ is None for arg in wraps):
                state.requires_box = True
            if any(arg.typ is not None and classify_type(arg.typ) in ('cast', 'container') for arg in wraps):
                state.requires_cast = True
            positional_texts[arg_index] = wrap_expr(positional_texts[arg_index], wraps)

    rebuilt_args: list[str] = []
    positional_iter = iter(positional_texts)
    for child in arg_children:
        if child.type in ('keyword_argument', 'dictionary_splat'):
            rebuilt_args.append(arg_texts[span_key(child)])
        else:
            updated = next(positional_iter)
            rebuilt_args.append(updated)
            arg_texts[span_key(child)] = updated

    rewritten_arg_list = _apply_local_replacements(
        state.source,
        arg_list,
        [(child.start_byte, child.end_byte, arg_texts[span_key(child)]) for child in arg_children],
    )
    call_text = _apply_local_replacements(
        state.source,
        node,
        [
            (func_node.start_byte, func_node.end_byte, func_text),
            (arg_list.start_byte, arg_list.end_byte, rewritten_arg_list),
        ],
    )
    if preserve_args:
        helper_name = state.register_wrapper(callee_name, preserve_args, len(positional_texts))
        call_args = [func_text, *rebuilt_args]
        call_text = f"{helper_name}({', '.join(call_args)})"

    return_wraps = wrap_args_for(return_policy_for(plan_info.return_type).call_edits, plan_info.return_type)
    if return_wraps:
        if any(arg.typ is None for arg in return_wraps):
            state.requires_box = True
        if any(arg.typ is not None and classify_type(arg.typ) in ('cast', 'container') for arg in return_wraps):
            state.requires_cast = True
        call_text = wrap_expr(call_text, return_wraps)

    return call_text


def _rewrite_identifier(state: RewriteState, node: Node, env: dict[str, str]) -> str:
    text = node_text(state.source, node)
    typ = env.get(text)
    if typ is None or not _is_load_identifier(node):
        return text

    kind = classify_type(typ)
    if kind in ('cast', 'container'):
        state.requires_cast = True
    return make_wrap_expr(text, typ)


def _rewrite_class(state: RewriteState, node: Node) -> str:
    replacements: list[tuple[int, int, str]] = []
    for child in iter_named(node):
        if child.type == 'block':
            replacements.append((child.start_byte, child.end_byte, _rewrite_block(state, child, None, {})))
            continue
        replacements.append((child.start_byte, child.end_byte, _rewrite_node(state, child, None, {})))
    return _apply_local_replacements(state.source, node, replacements)


def _rewrite_node(
    state: RewriteState,
    node: Node,
    current_func: FunctionDefInfo | None,
    env: dict[str, str],
) -> str:
    if node.type == 'identifier':
        return _rewrite_identifier(state, node, env)
    if node.type == 'call':
        return _rewrite_call(state, node, current_func, env)
    if node.type == 'function_definition':
        info = state.info_by_span[span_key(node)]
        return _rewrite_function(state, info)
    if node.type == 'class_definition':
        return _rewrite_class(state, node)
    if node.type == 'decorated_definition':
        decorated_func: FunctionDefInfo | None = None
        for child in iter_named(node):
            if child.type == 'function_definition':
                decorated_func = state.info_by_span[span_key(child)]
                break
        replacements: list[tuple[int, int, str]] = []
        for child in iter_named(node):
            if child.type == 'function_definition':
                replacements.append((child.start_byte, child.end_byte, _rewrite_node(state, child, None, {})))
                continue
            if child.type == 'class_definition':
                replacements.append((child.start_byte, child.end_byte, _rewrite_class(state, child)))
                continue
            replacements.append((
                child.start_byte,
                child.end_byte,
                _rewrite_node(state, child, decorated_func, {}),
            ))
        return _apply_local_replacements(state.source, node, replacements)
    if node.type == 'block':
        return _rewrite_block(state, node, current_func, env)

    replacements: list[tuple[int, int, str]] = []
    for child in iter_named(node):
        if child.type == 'block':
            block_env = {} if node.type == 'class_definition' else env
            replacements.append((child.start_byte, child.end_byte, _rewrite_block(state, child, current_func, block_env)))
            continue
        if child.type == 'class_definition':
            replacements.append((child.start_byte, child.end_byte, _rewrite_class(state, child)))
            continue
        replacements.append((child.start_byte, child.end_byte, _rewrite_node(state, child, current_func, env)))
    return _apply_local_replacements(state.source, node, replacements)


def _rewrite_return_statement(
    state: RewriteState,
    stmt: Node,
    current_func: FunctionDefInfo,
    env: dict[str, str],
) -> str:
    named = iter_named(stmt)
    if not named:
        return 'return'

    value = named[0]
    plan_info = state.plan.funcs.get(current_func.name)
    if plan_info is None or not plan_info.is_detyped or plan_info.return_type is None:
        return f'return {_rewrite_node(state, value, current_func, env)}'

    policy = return_policy_for(plan_info.return_type)
    if 'unwrap_checked_return_value' in policy.value_edits:
        first_arg = _first_positional_arg(value) if value.type == 'call' else None
        rewritten = _rewrite_node(state, first_arg, current_func, env) if first_arg is not None else _rewrite_node(state, value, current_func, env)
    else:
        rewritten = _rewrite_node(state, value, current_func, env)

    wraps = wrap_args_for(policy.value_edits, plan_info.return_type)
    if wraps:
        if any(arg.typ is None for arg in wraps):
            state.requires_box = True
        if any(arg.typ is not None and classify_type(arg.typ) in ('cast', 'container') for arg in wraps):
            state.requires_cast = True
        rewritten = wrap_expr(rewritten, wraps)
    return f'return {rewritten}'


def _rewrite_annotated_assignment(
    state: RewriteState,
    stmt: Node,
    assignment: Node,
    current_func: FunctionDefInfo,
    env: dict[str, str],
) -> tuple[str | None, dict[str, str]]:
    target = assignment.child_by_field_name('left')
    value = assignment.child_by_field_name('right')
    typ = node_text(state.source, assignment.child_by_field_name('type')) or None
    target_text = node_text(state.source, target)
    updates: dict[str, str] = {}

    if typ is None or target is None:
        return (node_text(state.source, stmt), updates)

    actions = body_policy_for(typ).annotation_edits

    if value is None:
        if 'wrap_later_name_uses' in actions and target.type == 'identifier':
            updates[target_text] = typ
        if 'remove_annotation' in actions:
            return (None, updates)
        return (f'{target_text}: {typ}', updates)

    rewritten_value = _rewrite_node(state, value, current_func, env)
    if 'wrap_assigned_expression' in actions:
        if classify_type(typ) in ('cast', 'container'):
            state.requires_cast = True
        rewritten_value = wrap_expr(rewritten_value, [Arg(None, typ, 0)])

    if 'remove_annotation' in actions:
        return (f'{target_text} = {rewritten_value}', updates)
    return (f'{target_text}: {typ} = {rewritten_value}', updates)


def _rewrite_statement(
    state: RewriteState,
    stmt: Node,
    current_func: FunctionDefInfo | None,
    env: dict[str, str],
) -> tuple[str | None, dict[str, str]]:
    if current_func is not None:
        plan_info = state.plan.funcs.get(current_func.name)
        if plan_info is not None and plan_info.is_detyped:
            ann = _assignment_node(stmt)
            if ann is not None:
                return _rewrite_annotated_assignment(state, stmt, ann, current_func, env)
        if stmt.type == 'return_statement':
            return (_rewrite_return_statement(state, stmt, current_func, env), {})

    return (_rewrite_node(state, stmt, current_func, env), {})


def _rewrite_block(
    state: RewriteState,
    block: Node,
    current_func: FunctionDefInfo | None,
    env: dict[str, str],
) -> str:
    indent = _indent_before(state.source, block)
    active_env = dict(env)
    rewritten: list[str] = []

    for stmt in iter_named(block):
        text, updates = _rewrite_statement(state, stmt, current_func, active_env)
        active_env.update(updates)
        if text is not None:
            rewritten.append(text)

    if not rewritten:
        rewritten = ['pass']

    return ('\n' + indent).join(rewritten)


def _function_plan(plan: PlanData, info: FunctionDefInfo) -> FuncInfo | None:
    return plan.funcs.get(info.name)


def _rewrite_function(state: RewriteState, info: FunctionDefInfo) -> str:
    func_plan = _function_plan(state.plan, info)
    params_node = info.node.child_by_field_name('parameters')
    body_node = info.node.child_by_field_name('body')
    if params_node is None or body_node is None:
        return node_text(state.source, info.node)

    replacements: list[tuple[int, int, str]] = []
    prepend_stmts: list[str] = []

    if func_plan is not None and func_plan.is_detyped:
        for index, typ in enumerate(func_plan.param_types):
            if index >= len(info.regular_params):
                break
            param = info.regular_params[index]
            if typ is None:
                continue
            policy = param_policy_for(typ)
            actions = policy.definition_edits
            if 'remove_annotation' in actions:
                replacements.append((
                    param.node.start_byte,
                    param.node.end_byte,
                    _param_text_without_annotation(state.source, param.node),
                ))
                continue

            if 'rewrite_param_binding' in actions:
                kind = classify_type(typ)
                if kind == 'checked_list':
                    replacements.append((
                        param.node.start_byte,
                        param.node.end_byte,
                        _param_text_without_annotation(state.source, param.node),
                    ))
                    stmt, needs_cast = build_checked_list_param_binding_stmt(param.name, typ)
                    prepend_stmts.append(stmt)
                    state.requires_cast = state.requires_cast or needs_cast
                    continue

                temp_name = '_' + param.name
                replacements.append((
                    param.node.start_byte,
                    param.node.end_byte,
                    _param_text_without_annotation(state.source, param.node, new_name=temp_name),
                ))
                stmt, needs_cast = build_rewrite_param_binding_stmt(param.name, temp_name, typ)
                prepend_stmts.append(stmt)
                state.requires_cast = state.requires_cast or needs_cast

        return_type = info.node.child_by_field_name('return_type')
        if return_type is not None and func_plan.return_type is not None:
            if 'remove_annotation' in return_policy_for(func_plan.return_type).definition_edits:
                replacements.append((params_node.end_byte, return_type.end_byte, ''))

    body_text = _rewrite_block(state, body_node, info, {})
    if prepend_stmts:
        indent = _indent_before(state.source, body_node)
        body_text = ('\n' + indent).join([*prepend_stmts, body_text])
    replacements.append((body_node.start_byte, body_node.end_byte, body_text))

    return _apply_local_replacements(state.source, info.node, replacements)


def build_detyped_program(
    source: str,
    perm: Permutation,
    fun_names: list[str],
) -> DetypedProgram:
    root = parse_source(source)
    defs = all_function_defs(root, source)
    guide: GuideType = dict(zip(fun_names, perm))
    plan = build_plan_data(defs, guide)
    state = RewriteState(
        source=source,
        root=root,
        defs=defs,
        plan=plan,
        info_by_span={info.span: info for info in defs},
        used_top_level_names=_top_level_function_names(root, source),
    )

    edits: list[Edit] = []
    for info in root_function_defs(defs):
        target = info.node.parent if info.node.parent is not None and info.node.parent.type == 'decorated_definition' else info.node
        edits.append(Edit(
            start_byte=target.start_byte,
            end_byte=target.end_byte,
            replacement=_rewrite_node(state, target, None, {}),
        ))

    insert_at = _import_insert_byte(source, root)
    imported_static = _imported_static_names(source, root)
    import_names = [name for name in ('box', 'cast') if getattr(state, f'requires_{name}', False) and name not in imported_static]
    inserted_chunks: list[str] = []
    if import_names:
        inserted_chunks.append(f"from __static__ import {', '.join(sorted(import_names))}\n")
    if state.wrapper_defs:
        inserted_chunks.extend(wrapper + '\n' for wrapper in reversed(state.wrapper_defs))
    if inserted_chunks:
        edits.append(Edit(start_byte=insert_at, end_byte=insert_at, replacement=''.join(inserted_chunks)))

    return DetypedProgram(
        perm=perm,
        perm_hex=perm_name(perm),
        source=unparse(source, edits),
    )


def write_detyped_program(
    program: DetypedProgram,
    output_dir: Path,
    source_stem: str,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    out_file = output_dir / f'{source_stem}_{program.perm_hex}.py'
    out_file.write_text(program.source, encoding='utf-8')
    return out_file
