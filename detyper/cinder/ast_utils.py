"""Tree-sitter queries and metadata helpers for the Cinder backend."""

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


def _call_kind_and_name(source: str, call_node: Node) -> tuple[str, str] | None:
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
            call_info = _call_kind_and_name(source, node)
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
