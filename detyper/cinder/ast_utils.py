"""Tree-sitter queries and source-structure helpers for the Cinder backend."""

from __future__ import annotations

from dataclasses import dataclass

from tree_sitter import Language, Node, Parser
import tree_sitter_python as tspython


_PARSER = Parser(Language(tspython.language()))


@dataclass(frozen=True)
class ParamInfo:
    name: str
    node: Node
    annotation: str | None


@dataclass(frozen=True)
class FunctionDefInfo:
    name: str
    node: Node
    regular_params: tuple[ParamInfo, ...]
    return_annotation: str | None
    is_inline: bool

    @property
    def span(self) -> tuple[int, int]:
        return (self.node.start_byte, self.node.end_byte)


@dataclass(frozen=True)
class CallSite:
    node: Node
    caller: FunctionDefInfo
    kind: str
    name: str

    @property
    def span(self) -> tuple[int, int]:
        return (self.node.start_byte, self.node.end_byte)


def parse_source(source: str) -> Node:
    return _PARSER.parse(source.encode('utf-8')).root_node


def node_text(source: str, node: Node | None) -> str:
    if node is None:
        return ''
    return source[node.start_byte:node.end_byte]


def iter_named(node: Node) -> list[Node]:
    return [child for child in node.children if child.is_named]


def span_key(node: Node) -> tuple[int, int]:
    return (node.start_byte, node.end_byte)


def line_start(source: str, byte_offset: int) -> int:
    return source.rfind('\n', 0, byte_offset) + 1


def indent_before(source: str, node: Node) -> str:
    return source[line_start(source, node.start_byte):node.start_byte]


def top_level_function_names(root: Node, source: str) -> set[str]:
    names: set[str] = set()
    for child in iter_named(root):
        if child.type == 'function_definition':
            names.add(node_text(source, child.child_by_field_name('name')))
        if child.type == 'decorated_definition':
            for inner in iter_named(child):
                if inner.type == 'function_definition':
                    names.add(node_text(source, inner.child_by_field_name('name')))
    return names


def import_insert_byte(source: str, root: Node) -> int:
    insert_at = 0
    for child in iter_named(root):
        if child.type in ('import_statement', 'import_from_statement'):
            insert_at = child.end_byte
            if insert_at < len(source) and source[insert_at:insert_at + 1] == '\n':
                insert_at += 1
    return insert_at


def imported_static_names(source: str, root: Node) -> set[str]:
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


def param_text_without_annotation(source: str, param_node: Node, new_name: str | None = None) -> str:
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


def assignment_node(stmt: Node) -> Node | None:
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


def is_descendant_of(node: Node, ancestor: Node | None) -> bool:
    if ancestor is None:
        return False
    current: Node | None = node
    while current is not None:
        if current == ancestor:
            return True
        current = current.parent
    return False


def is_load_identifier(node: Node) -> bool:
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
            if is_descendant_of(node, parent.child_by_field_name('left')):
                return False
        current = parent

    return True


def first_positional_arg(node: Node) -> Node | None:
    args = node.child_by_field_name('arguments')
    if args is None:
        return None
    for child in iter_named(args):
        if child.type not in ('keyword_argument', 'dictionary_splat'):
            return child
    return None


def call_kind_and_name(source: str, call_node: Node) -> tuple[str, str] | None:
    func_node = call_node.child_by_field_name('function')
    if func_node is None:
        return None
    if func_node.type == 'identifier':
        return ('function', node_text(source, func_node))
    if func_node.type == 'attribute':
        named = iter_named(func_node)
        if named and named[-1].type == 'identifier':
            return ('method', node_text(source, named[-1]))
    return None


def has_function_ancestor(node: Node) -> bool:
    current = node.parent
    while current is not None:
        if current.type == 'function_definition':
            return True
        current = current.parent
    return False


def root_function_defs(defs: list[FunctionDefInfo]) -> list[FunctionDefInfo]:
    return [info for info in defs if not has_function_ancestor(info.node)]


def _regular_params(func_node: Node, source: str) -> tuple[ParamInfo, ...]:
    params = func_node.child_by_field_name('parameters')
    if params is None:
        return ()

    named = iter_named(params)
    has_positional_separator = any(child.type == 'positional_separator' for child in named)
    include_regular = not has_positional_separator
    result: list[ParamInfo] = []

    for child in named:
        if child.type == 'positional_separator':
            include_regular = True
            continue
        if child.type in ('keyword_separator', 'list_splat_pattern', 'dictionary_splat_pattern'):
            break
        if child.type in ('typed_parameter', 'typed_default_parameter'):
            first_named = next(iter(iter_named(child)), None)
            if first_named is None or first_named.type != 'identifier':
                break
            if not include_regular:
                continue
            result.append(ParamInfo(
                name=node_text(source, first_named),
                node=child,
                annotation=node_text(source, child.child_by_field_name('type')) or None,
            ))
            continue
        if child.type == 'default_parameter':
            if not include_regular:
                continue
            name_node = child.child_by_field_name('name')
            if name_node is None:
                continue
            result.append(ParamInfo(
                name=node_text(source, name_node),
                node=child,
                annotation=None,
            ))
            continue
        if child.type == 'identifier':
            if not include_regular:
                continue
            result.append(ParamInfo(
                name=node_text(source, child),
                node=child,
                annotation=None,
            ))

    return tuple(result)


def _decorators_for_function(func_node: Node) -> list[Node]:
    parent = func_node.parent
    if parent is None or parent.type != 'decorated_definition':
        return []
    return [child for child in iter_named(parent) if child.type == 'decorator']


def _decorator_endswith_inline(source: str, decorator: Node) -> bool:
    for child in iter_named(decorator):
        if child.type == 'identifier' and node_text(source, child) == 'inline':
            return True
        if child.type == 'attribute':
            named = iter_named(child)
            if named and node_text(source, named[-1]) == 'inline':
                return True
    return False


def all_function_defs(root: Node, source: str) -> list[FunctionDefInfo]:
    result: list[FunctionDefInfo] = []

    def walk(node: Node) -> None:
        if node.type == 'function_definition':
            result.append(FunctionDefInfo(
                name=node_text(source, node.child_by_field_name('name')),
                node=node,
                regular_params=_regular_params(node, source),
                return_annotation=node_text(source, node.child_by_field_name('return_type')) or None,
                is_inline=any(_decorator_endswith_inline(source, d) for d in _decorators_for_function(node)),
            ))
        for child in iter_named(node):
            walk(child)

    walk(root)
    return result


def detypable_function_names(source: str) -> list[str]:
    root = parse_source(source)
    names = {
        info.name
        for info in all_function_defs(root, source)
        if not (info.name.startswith('__') and info.name.endswith('__'))
    }
    return sorted(names)


def _function_index(defs: list[FunctionDefInfo]) -> dict[tuple[int, int], FunctionDefInfo]:
    return {info.span: info for info in defs}


def _collect_call_sites(
    root: Node,
    source: str,
    defs: list[FunctionDefInfo],
    target_kind: str,
) -> list[CallSite]:
    info_by_span = _function_index(defs)
    result: list[CallSite] = []

    def walk(node: Node, current_func: FunctionDefInfo | None) -> None:
        next_func = current_func
        if node.type == 'function_definition':
            next_func = info_by_span.get(span_key(node))

        if node.type == 'call' and next_func is not None:
            call_info = call_kind_and_name(source, node)
            if call_info is not None:
                kind, name = call_info
                if kind == target_kind:
                    result.append(CallSite(node=node, caller=next_func, kind=kind, name=name))

        for child in iter_named(node):
            walk(child, next_func)

    walk(root, None)
    return result


def all_function_uses(root: Node, source: str, defs: list[FunctionDefInfo]) -> list[CallSite]:
    return _collect_call_sites(root, source, defs, 'function')


def all_method_uses(root: Node, source: str, defs: list[FunctionDefInfo]) -> list[CallSite]:
    return _collect_call_sites(root, source, defs, 'method')
