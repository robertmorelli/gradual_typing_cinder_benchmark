"""Rewrite execution and source-edit application for the Cinder backend."""

from __future__ import annotations

from dataclasses import dataclass, field

from tree_sitter import Node

from .ast_utils import (
    FunctionDefInfo,
    assignment_node,
    call_kind_and_name,
    first_positional_arg,
    indent_before,
    is_load_identifier,
    iter_named,
    node_text,
    param_text_without_annotation,
    span_key,
    top_level_function_names,
)
from .generators import (
    Arg,
    PreserveArg,
    generate_body_assignment_rewrite,
    generate_call_rewrite_plan,
    generate_param_definition_rewrites,
    generate_return_rewrite_plan,
    wraps_require_box,
    wraps_require_cast,
)
from .plan_data import PlanData
from .rules import classify_type


def make_wrap_expr(expr: str, typ: str) -> str:
    kind = classify_type(typ)
    if kind == 'primitive':
        return f'{typ}({expr})'
    if kind in ('cast', 'container'):
        return f'cast({typ}, {expr})'
    if kind == 'checked_list':
        return f'{typ}({expr})'
    return expr


def make_box_expr(expr: str) -> str:
    return f'box({expr})'


def wrap_expr(expr: str, args: tuple[Arg, ...]) -> str:
    wrapped = expr
    for arg in sorted(args, key=lambda item: item.wrap_order):
        wrapped = make_box_expr(wrapped) if arg.typ is None else make_wrap_expr(wrapped, arg.typ)
    return wrapped


def build_rewrite_param_binding_stmt(orig_name: str, temp_name: str, typ: str) -> tuple[str, bool]:
    kind = classify_type(typ)
    if kind == 'primitive':
        return (f'{orig_name}: {typ} = {typ}({temp_name})', False)
    return (f'{orig_name}: {typ} = cast({typ}, {temp_name})', True)


def build_checked_list_param_binding_stmt(orig_name: str, typ: str) -> tuple[str, bool]:
    return (f'{orig_name} = cast({typ}, {orig_name})', True)


def build_preserve_argument_mutations_wrapper(name: str, n_args: int, args: tuple[PreserveArg, ...]) -> str:
    sorted_args = sorted(args, key=lambda item: item.index)
    params = ', '.join(['f'] + [f'arg{i}' for i in range(n_args)])
    lines = [f'def {name}({params}):']

    for arg in sorted_args:
        lines.append(f'    _arg{arg.index} = {arg.typ}(arg{arg.index})')

    converted = {arg.index for arg in sorted_args}
    call_args = ', '.join(f'_arg{i}' if i in converted else f'arg{i}' for i in range(n_args))
    lines.append(f'    _out = f({call_args})')

    for arg in sorted_args:
        lines.append(f'    arg{arg.index}.clear()')
        lines.append(f'    arg{arg.index}.extend(_arg{arg.index})')

    lines.append('    return _out')
    return '\n'.join(lines)


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


@dataclass
class Detyper:
    source: str
    plan: PlanData
    info_by_span: dict[tuple[int, int], FunctionDefInfo]
    used_top_level_names: set[str]
    generated_wrapper_names: set[str] = field(default_factory=set)
    wrapper_defs: list[str] = field(default_factory=list)
    requires_cast: bool = False
    requires_box: bool = False

    @classmethod
    def from_source(
        cls,
        source: str,
        root: Node,
        defs: list[FunctionDefInfo],
        plan: PlanData,
    ) -> 'Detyper':
        return cls(
            source=source,
            plan=plan,
            info_by_span={info.span: info for info in defs},
            used_top_level_names=top_level_function_names(root, source),
        )

    def _note_wraps(self, wraps: tuple[Arg, ...]) -> None:
        self.requires_box = self.requires_box or wraps_require_box(wraps)
        self.requires_cast = self.requires_cast or wraps_require_cast(wraps)

    def register_wrapper(self, callee_name: str, args: tuple[PreserveArg, ...], n_args: int) -> str:
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

    def rewrite_top_level(self, node: Node) -> str:
        return self._rewrite_node(node, None, {})

    def _argument_text(
        self,
        node: Node,
        current_func: FunctionDefInfo | None,
        env: dict[str, str],
    ) -> str:
        if node.type == 'keyword_argument':
            named = iter_named(node)
            if len(named) == 2 and named[0].type == 'identifier':
                return f'{node_text(self.source, named[0])}={self._rewrite_node(named[1], current_func, env)}'
        return self._rewrite_node(node, current_func, env)

    def _rewrite_call(
        self,
        node: Node,
        current_func: FunctionDefInfo | None,
        env: dict[str, str],
    ) -> str:
        func_node = node.child_by_field_name('function')
        arg_list = node.child_by_field_name('arguments')
        if func_node is None or arg_list is None:
            return node_text(self.source, node)

        func_text = self._rewrite_node(func_node, current_func, env)
        arg_children = iter_named(arg_list)
        arg_texts = {span_key(child): self._argument_text(child, current_func, env) for child in arg_children}
        positional = [child for child in arg_children if child.type not in ('keyword_argument', 'dictionary_splat')]
        base_arg_list = _apply_local_replacements(
            self.source,
            arg_list,
            [(child.start_byte, child.end_byte, arg_texts[span_key(child)]) for child in arg_children],
        )
        base_call = _apply_local_replacements(
            self.source,
            node,
            [
                (func_node.start_byte, func_node.end_byte, func_text),
                (arg_list.start_byte, arg_list.end_byte, base_arg_list),
            ],
        )

        call_info = call_kind_and_name(self.source, node)
        if call_info is None:
            return base_call

        kind, callee_name = call_info
        plan = generate_call_rewrite_plan(self.plan.funcs.get(callee_name), kind, len(positional))
        if plan is None:
            return base_call

        positional_texts = [arg_texts[span_key(child)] for child in positional]
        for rewrite in plan.positional_wraps:
            self._note_wraps(rewrite.wraps)
            positional_texts[rewrite.arg_index] = wrap_expr(positional_texts[rewrite.arg_index], rewrite.wraps)

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
            self.source,
            arg_list,
            [(child.start_byte, child.end_byte, arg_texts[span_key(child)]) for child in arg_children],
        )
        call_text = _apply_local_replacements(
            self.source,
            node,
            [
                (func_node.start_byte, func_node.end_byte, func_text),
                (arg_list.start_byte, arg_list.end_byte, rewritten_arg_list),
            ],
        )

        if plan.preserve_args:
            helper_name = self.register_wrapper(callee_name, plan.preserve_args, len(positional_texts))
            call_text = f"{helper_name}({', '.join([func_text, *rebuilt_args])})"

        if plan.return_wraps:
            self._note_wraps(plan.return_wraps)
            call_text = wrap_expr(call_text, plan.return_wraps)

        return call_text

    def _rewrite_identifier(self, node: Node, env: dict[str, str]) -> str:
        text = node_text(self.source, node)
        typ = env.get(text)
        if typ is None or not is_load_identifier(node):
            return text

        kind = classify_type(typ)
        if kind in ('cast', 'container'):
            self.requires_cast = True
        return make_wrap_expr(text, typ)

    def _rewrite_class(self, node: Node) -> str:
        replacements: list[tuple[int, int, str]] = []
        for child in iter_named(node):
            if child.type == 'block':
                replacements.append((child.start_byte, child.end_byte, self._rewrite_block(child, None, {})))
                continue
            replacements.append((child.start_byte, child.end_byte, self._rewrite_node(child, None, {})))
        return _apply_local_replacements(self.source, node, replacements)

    def _rewrite_node(
        self,
        node: Node,
        current_func: FunctionDefInfo | None,
        env: dict[str, str],
    ) -> str:
        if node.type == 'identifier':
            return self._rewrite_identifier(node, env)
        if node.type == 'call':
            return self._rewrite_call(node, current_func, env)
        if node.type == 'function_definition':
            return self.rewrite_function(self.info_by_span[span_key(node)])
        if node.type == 'class_definition':
            return self._rewrite_class(node)
        if node.type == 'decorated_definition':
            decorated_func: FunctionDefInfo | None = None
            for child in iter_named(node):
                if child.type == 'function_definition':
                    decorated_func = self.info_by_span[span_key(child)]
                    break
            replacements: list[tuple[int, int, str]] = []
            for child in iter_named(node):
                if child.type == 'function_definition':
                    replacements.append((child.start_byte, child.end_byte, self._rewrite_node(child, None, {})))
                    continue
                if child.type == 'class_definition':
                    replacements.append((child.start_byte, child.end_byte, self._rewrite_class(child)))
                    continue
                replacements.append((
                    child.start_byte,
                    child.end_byte,
                    self._rewrite_node(child, decorated_func, {}),
                ))
            return _apply_local_replacements(self.source, node, replacements)
        if node.type == 'block':
            return self._rewrite_block(node, current_func, env)

        replacements: list[tuple[int, int, str]] = []
        for child in iter_named(node):
            if child.type == 'block':
                block_env = {} if node.type == 'class_definition' else env
                replacements.append((child.start_byte, child.end_byte, self._rewrite_block(child, current_func, block_env)))
                continue
            if child.type == 'class_definition':
                replacements.append((child.start_byte, child.end_byte, self._rewrite_class(child)))
                continue
            replacements.append((child.start_byte, child.end_byte, self._rewrite_node(child, current_func, env)))
        return _apply_local_replacements(self.source, node, replacements)

    def _rewrite_return_statement(
        self,
        stmt: Node,
        current_func: FunctionDefInfo,
        env: dict[str, str],
    ) -> str:
        named = iter_named(stmt)
        if not named:
            return 'return'

        value = named[0]
        plan = generate_return_rewrite_plan(self.plan.funcs.get(current_func.name))
        if plan is None:
            return f'return {self._rewrite_node(value, current_func, env)}'

        if plan.unwrap_checked_return_value:
            first_arg = first_positional_arg(value) if value.type == 'call' else None
            rewritten = self._rewrite_node(first_arg, current_func, env) if first_arg is not None else self._rewrite_node(value, current_func, env)
        else:
            rewritten = self._rewrite_node(value, current_func, env)

        if plan.value_wraps:
            self._note_wraps(plan.value_wraps)
            rewritten = wrap_expr(rewritten, plan.value_wraps)
        return f'return {rewritten}'

    def _rewrite_annotated_assignment(
        self,
        stmt: Node,
        assignment: Node,
        current_func: FunctionDefInfo,
        env: dict[str, str],
    ) -> tuple[str | None, dict[str, str]]:
        target = assignment.child_by_field_name('left')
        value = assignment.child_by_field_name('right')
        typ = node_text(self.source, assignment.child_by_field_name('type')) or None
        updates: dict[str, str] = {}

        if typ is None or target is None:
            return (node_text(self.source, stmt), updates)

        plan = generate_body_assignment_rewrite(typ)
        if plan is None:
            return (node_text(self.source, stmt), updates)

        target_text = node_text(self.source, target)
        if value is None:
            if plan.wrap_later_name_uses and target.type == 'identifier':
                updates[target_text] = typ
            if plan.remove_annotation:
                return (None, updates)
            return (f'{target_text}: {typ}', updates)

        rewritten_value = self._rewrite_node(value, current_func, env)
        if plan.wrap_assigned_expression:
            wraps = (Arg(None, typ, 0),)
            self._note_wraps(wraps)
            rewritten_value = wrap_expr(rewritten_value, wraps)

        if plan.remove_annotation:
            return (f'{target_text} = {rewritten_value}', updates)
        return (f'{target_text}: {typ} = {rewritten_value}', updates)

    def _rewrite_statement(
        self,
        stmt: Node,
        current_func: FunctionDefInfo | None,
        env: dict[str, str],
    ) -> tuple[str | None, dict[str, str]]:
        if current_func is not None:
            plan = self.plan.funcs.get(current_func.name)
            if plan is not None and plan.is_detyped:
                ann = assignment_node(stmt)
                if ann is not None:
                    return self._rewrite_annotated_assignment(stmt, ann, current_func, env)
            if stmt.type == 'return_statement':
                return (self._rewrite_return_statement(stmt, current_func, env), {})

        return (self._rewrite_node(stmt, current_func, env), {})

    def _rewrite_block(
        self,
        block: Node,
        current_func: FunctionDefInfo | None,
        env: dict[str, str],
    ) -> str:
        indent = indent_before(self.source, block)
        active_env = dict(env)
        rewritten: list[str] = []

        for stmt in iter_named(block):
            text, updates = self._rewrite_statement(stmt, current_func, active_env)
            active_env.update(updates)
            if text is not None:
                rewritten.append(text)

        if not rewritten:
            rewritten = ['pass']

        return ('\n' + indent).join(rewritten)

    def rewrite_function(self, info: FunctionDefInfo) -> str:
        params_node = info.node.child_by_field_name('parameters')
        body_node = info.node.child_by_field_name('body')
        if params_node is None or body_node is None:
            return node_text(self.source, info.node)

        replacements: list[tuple[int, int, str]] = []
        prepend_stmts: list[str] = []
        func_info = self.plan.funcs.get(info.name)

        for rewrite in generate_param_definition_rewrites(func_info):
            if rewrite.index >= len(info.regular_params):
                break

            param = info.regular_params[rewrite.index]
            if rewrite.mode == 'remove_annotation':
                replacements.append((
                    param.node.start_byte,
                    param.node.end_byte,
                    param_text_without_annotation(self.source, param.node),
                ))
                continue

            kind = classify_type(rewrite.typ)
            if kind == 'checked_list':
                replacements.append((
                    param.node.start_byte,
                    param.node.end_byte,
                    param_text_without_annotation(self.source, param.node),
                ))
                stmt, needs_cast = build_checked_list_param_binding_stmt(param.name, rewrite.typ)
                prepend_stmts.append(stmt)
                self.requires_cast = self.requires_cast or needs_cast
                continue

            temp_name = '_' + param.name
            replacements.append((
                param.node.start_byte,
                param.node.end_byte,
                param_text_without_annotation(self.source, param.node, new_name=temp_name),
            ))
            stmt, needs_cast = build_rewrite_param_binding_stmt(param.name, temp_name, rewrite.typ)
            prepend_stmts.append(stmt)
            self.requires_cast = self.requires_cast or needs_cast

        return_type = info.node.child_by_field_name('return_type')
        return_plan = generate_return_rewrite_plan(func_info)
        if return_type is not None and return_plan is not None and return_plan.remove_annotation:
            replacements.append((params_node.end_byte, return_type.end_byte, ''))

        body_text = self._rewrite_block(body_node, info, {})
        if prepend_stmts:
            indent = indent_before(self.source, body_node)
            body_text = ('\n' + indent).join([*prepend_stmts, body_text])
        replacements.append((body_node.start_byte, body_node.end_byte, body_text))

        return _apply_local_replacements(self.source, info.node, replacements)
