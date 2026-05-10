"""Serializable AST data and lightweight indexes for staged detyping.

This is intentionally small: stage 1 packages the Python AST plus useful indexes
into JSON. Later stages can rehydrate the AST from this JSON and avoid source.
"""

from __future__ import annotations

import ast
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .kind_context_policy import Place, affinity_for_place
from .type_classifier import classification_metadata

_JSON_PRIMITIVE = (str, int, float, bool, type(None))
_LOCATION_ATTRS = ('lineno', 'col_offset', 'end_lineno', 'end_col_offset')
_DECORATION_ATTRS = ('detyping_id', 'parent_detyping_id', 'detyping_span')


@dataclass(frozen=True)
class AstData:
    root_id: int
    nodes: dict[str, dict[str, Any]]
    indexes: dict[str, Any]

    def to_json(self) -> dict[str, Any]:
        return {'version': 1, 'root_id': self.root_id, 'nodes': self.nodes, 'indexes': self.indexes}


class AstIndex:
    """Tiny query facade over staged indexes.

    Generators should grow toward this API instead of open-coded tree walks.
    """

    def __init__(self, tree: ast.AST):
        self.tree = tree
        self.indexes = getattr(tree, 'detyping_indexes')
        self.by_id = getattr(tree, 'detyping_node_index', None) or {
            node.detyping_id: node for node in ast.walk(tree) if hasattr(node, 'detyping_id')
        }

    def node(self, node_id: int) -> ast.AST:
        return self.by_id[int(node_id)]

    def nodes(self, node_ids: list[int]) -> list[ast.AST]:
        return [self.by_id[int(node_id)] for node_id in node_ids]

    def functions(self) -> list[ast.FunctionDef]:
        return [node for node in self.nodes(sorted(int(i) for i in self.indexes['functions'])) if isinstance(node, ast.FunctionDef)]

    def nodes_in_function(self, function_id: int, kind: str) -> list[ast.AST]:
        ids = self.indexes.get('nodes_by_function_kind', {}).get(str(function_id), {}).get(kind, [])
        return self.nodes(ids)

    def calls_named(self, name: str) -> list[ast.Call]:
        ids = [int(node_id) for node_id, rec in self.indexes.get('calls', {}).items() if rec.get('name') == name]
        return [node for node in self.nodes(ids) if isinstance(node, ast.Call)]

    def symbol_defs(self, use_id: int) -> list[ast.AST]:
        return self.nodes(self.indexes.get('symbol_links', {}).get('use_to_defs', {}).get(str(use_id), []))

    def symbol_uses(self, def_id: int) -> list[ast.AST]:
        return self.nodes(self.indexes.get('symbol_links', {}).get('def_to_uses', {}).get(str(def_id), []))

    def uses_of_function(self, function_id: int) -> list[ast.Call]:
        pyright_uses = [node for node in self.symbol_uses(function_id) if isinstance(node, ast.Call)]
        if pyright_uses:
            return pyright_uses
        return [node for node in self.nodes(self.indexes.get('function_uses_by_def', {}).get(str(function_id), [])) if isinstance(node, ast.Call)]

    def uses_of_method(self, function_id: int) -> list[ast.Call]:
        pyright_uses = [node for node in self.symbol_uses(function_id) if isinstance(node, ast.Call)]
        if pyright_uses:
            return pyright_uses
        return [node for node in self.nodes(self.indexes.get('method_uses_by_def', {}).get(str(function_id), [])) if isinstance(node, ast.Call)]

    def uses_of_field(self, class_name: str, field_name: str) -> list[ast.Attribute]:
        key = f'{class_name}.{field_name}'
        return [node for node in self.nodes(self.indexes.get('field_uses_by_field', {}).get(key, [])) if isinstance(node, ast.Attribute)]

    def calls_in_function(self, function_id: int) -> list[ast.Call]:
        return [node for node in self.nodes(self.indexes.get('calls_by_function', {}).get(str(function_id), [])) if isinstance(node, ast.Call)]

    def annotations_in_function(self, function_id: int) -> list[ast.AST]:
        return self.nodes(self.indexes.get('annotations_by_function', {}).get(str(function_id), []))

    def returns_in_function(self, function_id: int) -> list[ast.Return]:
        return [node for node in self.nodes(self.indexes.get('returns_by_function', {}).get(str(function_id), [])) if isinstance(node, ast.Return)]

    def assigns_in_function(self, function_id: int) -> list[ast.Assign]:
        return [node for node in self.nodes(self.indexes.get('assigns_by_function', {}).get(str(function_id), [])) if isinstance(node, ast.Assign)]

    def loads_for_binding(self, binding_id: int) -> list[ast.Name]:
        ids = self.indexes.get('variables', {}).get('loads_by_binding', {}).get(str(binding_id), [])
        return [node for node in self.nodes(ids) if isinstance(node, ast.Name)]


class _IndexBuilder(ast.NodeVisitor):
    def __init__(self):
        self.functions: dict[str, dict[str, Any]] = {}
        self.classes: dict[str, dict[str, Any]] = {}
        self.ann_assigns_by_function: dict[str, list[int]] = {}
        self.returns_by_function: dict[str, list[int]] = {}
        self.assigns_by_function: dict[str, list[int]] = {}
        self.nodes_by_kind: dict[str, list[int]] = {}
        self.enclosing_function_by_node: dict[str, int | None] = {}
        self.enclosing_class_by_node: dict[str, int | None] = {}
        self.function_annotation_ids: dict[str, list[int]] = {}
        self.class_bases: dict[str, str] = {}
        self.func_classes: dict[str, str] = {}
        self.class_field_annotations: dict[str, dict[str, int]] = {}
        self.class_init_param_annotation_ids: dict[str, list[int | None]] = {}
        self.variables: dict[str, Any] = {
            'bindings': {},
            'uses': {},
            'loads_by_binding': {},
            'stores_by_binding': {},
        }
        self._function_stack: list[ast.FunctionDef] = []
        self._class_stack: list[ast.ClassDef] = []
        self._scope_bindings: list[dict[str, int]] = []
        self._next_binding_id = 1

    def _node_id(self, node: ast.AST) -> int:
        return node.detyping_id

    def _current_function_id(self) -> int | None:
        return self._node_id(self._function_stack[-1]) if self._function_stack else None

    def _current_class_id(self) -> int | None:
        return self._node_id(self._class_stack[-1]) if self._class_stack else None

    def _record_common(self, node: ast.AST) -> None:
        node_id = self._node_id(node)
        self.nodes_by_kind.setdefault(type(node).__name__, []).append(node_id)
        self.enclosing_function_by_node[str(node_id)] = self._current_function_id()
        self.enclosing_class_by_node[str(node_id)] = self._current_class_id()

    def _bind(self, name: str, node: ast.AST, kind: str) -> int:
        if not self._scope_bindings:
            self._scope_bindings.append({})
        scope_id = self._current_function_id()
        if scope_id is None:
            scope_id = self._current_class_id()
        if scope_id is None:
            scope_id = 0
        existing_id = self._scope_bindings[-1].get(name)
        if existing_id is not None:
            self.variables['stores_by_binding'].setdefault(str(existing_id), []).append(self._node_id(node))
            return existing_id
        binding_id = self._next_binding_id
        self._next_binding_id += 1
        self._scope_bindings[-1][name] = binding_id
        self.variables['bindings'][str(binding_id)] = {
            'id': binding_id,
            'name': name,
            'node_id': self._node_id(node),
            'scope_id': scope_id,
            'kind': kind,
        }
        self.variables['stores_by_binding'].setdefault(str(binding_id), []).append(self._node_id(node))
        return binding_id

    def _lookup(self, name: str) -> int | None:
        for scope in reversed(self._scope_bindings):
            if name in scope:
                return scope[name]
        return None

    def _record_use(self, node: ast.Name) -> None:
        ctx = type(node.ctx).__name__.lower().replace('load', 'load').replace('store', 'store').replace('del', 'del')
        binding_id = self._lookup(node.id)
        node_id = self._node_id(node)
        self.variables['uses'][str(node_id)] = {
            'node_id': node_id,
            'name': node.id,
            'binding_id': binding_id,
            'scope_id': self._current_function_id() or self._current_class_id() or 0,
            'ctx': ctx,
        }
        if binding_id is not None:
            key = str(binding_id)
            if isinstance(node.ctx, ast.Load):
                self.variables['loads_by_binding'].setdefault(key, []).append(node_id)
            elif isinstance(node.ctx, (ast.Store, ast.Del)):
                self.variables['stores_by_binding'].setdefault(key, []).append(node_id)

    def generic_visit(self, node: ast.AST) -> None:
        if hasattr(node, 'detyping_id'):
            self._record_common(node)
        super().generic_visit(node)

    def visit_Module(self, node: ast.Module) -> None:
        self._scope_bindings.append({})
        self._record_common(node)
        for stmt in node.body:
            if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                self._bind(stmt.name, stmt, 'function' if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)) else 'class')
            elif isinstance(stmt, ast.Assign):
                for target in stmt.targets:
                    if isinstance(target, ast.Name):
                        self._bind(target.id, target, 'local')
            elif isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
                self._bind(stmt.target.id, stmt.target, 'local')
        ast.NodeVisitor.generic_visit(self, node)
        self._scope_bindings.pop()

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self._record_common(node)
        base_names = [b.id for b in node.bases if isinstance(b, ast.Name)]
        self.classes[str(node.detyping_id)] = {'id': node.detyping_id, 'name': node.name, 'base_names': base_names, 'base_ids': [b.detyping_id for b in node.bases if hasattr(b, 'detyping_id')]}
        if base_names:
            self.class_bases[node.name] = base_names[0]
        self._bind(node.name, node, 'class')
        self._class_stack.append(node)
        self._scope_bindings.append({})
        for item in node.body:
            self.visit(item)
        self._scope_bindings.pop()
        self._class_stack.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._record_common(node)
        self._bind(node.name, node, 'function')
        is_inline = any((isinstance(d, ast.Name) and d.id == 'inline') or (isinstance(d, ast.Attribute) and d.attr == 'inline') for d in node.decorator_list)
        current_class_id = self._current_class_id()
        current_class_name = self._class_stack[-1].name if self._class_stack else None
        self.functions[str(node.detyping_id)] = {
            'id': node.detyping_id,
            'name': node.name,
            'class_id': current_class_id,
            'arg_ids': [arg.detyping_id for arg in node.args.args],
            'return_annotation_id': node.detyping_id if node.returns is not None else None,
            'is_inline': is_inline,
        }
        if current_class_name is not None:
            self.func_classes[str(node.detyping_id)] = current_class_name
        ann_ids = [arg.detyping_id for arg in node.args.args if arg.annotation is not None]
        if node.returns is not None:
            ann_ids.append(node.detyping_id)
        self.function_annotation_ids[str(node.detyping_id)] = ann_ids
        if current_class_name is not None and node.name == '__init__':
            self.class_init_param_annotation_ids[current_class_name] = [
                arg.detyping_id if arg.annotation is not None else None
                for arg in node.args.args[1:]
            ]
        self._function_stack.append(node)
        self._scope_bindings.append({})
        for arg in node.args.args:
            self._bind(arg.arg, arg, 'param')
        ast.NodeVisitor.generic_visit(self, node)
        self._scope_bindings.pop()
        self._function_stack.pop()

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        self._record_common(node)
        func_id = self._current_function_id()
        if func_id is not None:
            self.ann_assigns_by_function.setdefault(str(func_id), []).append(node.detyping_id)
            if node.annotation is not None:
                self.function_annotation_ids.setdefault(str(func_id), []).append(node.detyping_id)
        if (
            node.annotation is not None
            and self._class_stack
            and isinstance(node.target, ast.Attribute)
            and isinstance(node.target.value, ast.Name)
            and node.target.value.id == 'self'
        ):
            self.class_field_annotations.setdefault(self._class_stack[-1].name, {})[node.target.attr] = node.detyping_id
        if isinstance(node.target, ast.Name):
            self._bind(node.target.id, node.target, 'local')
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Assign(self, node: ast.Assign) -> None:
        self._record_common(node)
        func_id = self._current_function_id()
        if func_id is not None:
            self.assigns_by_function.setdefault(str(func_id), []).append(node.detyping_id)
        for target in node.targets:
            if isinstance(target, ast.Name) and self._lookup(target.id) is None:
                self._bind(target.id, target, 'local')
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Return(self, node: ast.Return) -> None:
        self._record_common(node)
        func_id = self._current_function_id()
        if func_id is not None:
            self.returns_by_function.setdefault(str(func_id), []).append(node.detyping_id)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Call(self, node: ast.Call) -> None:
        self._record_common(node)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Name(self, node: ast.Name) -> None:
        self._record_common(node)
        if isinstance(node.ctx, ast.Store) and self._lookup(node.id) is None:
            self._bind(node.id, node, 'local')
        self._record_use(node)


def _value_to_json(value: Any) -> Any:
    if isinstance(value, ast.AST):
        return {'$node': value.detyping_id}
    if isinstance(value, list):
        return [_value_to_json(item) for item in value]
    if isinstance(value, tuple):
        return {'$tuple': [_value_to_json(item) for item in value]}
    if isinstance(value, _JSON_PRIMITIVE):
        return value
    return repr(value)


def _span(node: ast.AST) -> list[int | None]:
    return [
        getattr(node, 'lineno', None),
        getattr(node, 'col_offset', None),
        getattr(node, 'end_lineno', None),
        getattr(node, 'end_col_offset', None),
    ]


def _name_of_type(expr: ast.expr | None) -> str | None:
    if expr is None:
        return None
    try:
        return ast.unparse(expr)
    except Exception:
        return None


def _container_element_type_src(type_src: str | None) -> str | None:
    if not type_src:
        return None
    try:
        expr = ast.parse(type_src, mode='eval').body
    except SyntaxError:
        return None
    if isinstance(expr, ast.Subscript):
        base = _name_of_type(expr.value)
        if base in {'CheckedList', 'list', 'List'}:
            return _name_of_type(expr.slice)
        if base in {'CheckedDict', 'dict', 'Dict'}:
            sl = expr.slice
            if isinstance(sl, ast.Tuple) and len(sl.elts) == 2:
                return _name_of_type(sl.elts[1])
    return None


def _clean_pyright_type(raw: str | None) -> str | None:
    if not raw:
        return None
    text = raw.strip()
    if '```' in text:
        parts = [part.strip() for part in text.split('```') if part.strip()]
        if parts:
            text = parts[-1]
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return None
    text = lines[-1]
    for prefix in ('(variable)', '(parameter)', '(function)', '(method)', '(class)', 'type:'):
        if text.startswith(prefix):
            text = text[len(prefix):].strip()
    if text.startswith('(type)') and '=' in text:
        text = text.split('=', 1)[1].strip()
    if ':' in text and not text.startswith(('list[', 'dict[', 'tuple[', 'Tuple[', 'Optional[', 'Union[')):
        text = text.rsplit(':', 1)[-1].strip()
    if ' -> ' in text and text.startswith('('):
        return text
    return text or None


def _callee(call: ast.Call) -> dict[str, Any]:
    if isinstance(call.func, ast.Name):
        return {'kind': 'name', 'name': call.func.id, 'func_id': call.func.detyping_id}
    if isinstance(call.func, ast.Attribute):
        return {'kind': 'attribute', 'name': call.func.attr, 'func_id': call.func.detyping_id, 'value_id': call.func.value.detyping_id}
    return {'kind': 'dynamic', 'name': None, 'func_id': getattr(call.func, 'detyping_id', None)}


def _expr_type_metadata(node: ast.AST, aliases: dict[str, str] | None = None, int_enums: set[str] | None = None) -> dict[str, Any]:
    raw = _clean_pyright_type(getattr(node, 'pyright_type', None))
    if raw in {'Unknown', 'Any'}:
        raw = None
    meta = classification_metadata(raw, aliases=set((aliases or {}).keys()), int_enums=int_enums)
    return {
        'pyright_type_src': raw,
        'pyright_normalized_type_src': meta['normalized_type_src'],
        'pyright_type_kind': meta['type_kind'],
    }


def _annotation_record(node: ast.AST, *, kind: str, annotation: ast.expr, function_id: int | None, class_id: int | None = None, name: str | None = None, param_index: int | None = None, aliases: dict[str, str] | None = None, int_enums: set[str] | None = None) -> dict[str, Any]:
    annotation_src = _name_of_type(annotation)
    pyright_resolved = _clean_pyright_type(getattr(annotation, 'pyright_type', None))
    if pyright_resolved in {'Unknown', 'Any'} or (pyright_resolved or '').startswith('type[') or ' is equivalent to ' in (pyright_resolved or '') or 'There is no runtime checking' in (pyright_resolved or ''):
        pyright_resolved = None
    if annotation_src and (annotation_src.startswith(('CheckedList[', 'CheckedDict[')) or annotation_src in {'int64', 'cbool', 'clen'}):
        pyright_resolved = None
    if kind in {'function_return_annotation', 'method_return_annotation'} and annotation_src and ('|' in annotation_src or annotation_src.startswith(('Optional[', 'Union['))):
        pyright_resolved = None
    resolved = pyright_resolved or (aliases or {}).get(annotation_src or '') or annotation_src
    type_meta = classification_metadata(resolved, aliases=set((aliases or {}).keys()), int_enums=int_enums)
    return {
        'id': node.detyping_id,
        'context': kind,
        'kind': kind,
        'function_id': function_id,
        'class_id': class_id,
        'name': name,
        'param_index': param_index,
        'annotation_id': annotation.detyping_id,
        'annotation_src': annotation_src,
        'resolved_type_src': resolved,
        'resolved_by': 'pyright' if pyright_resolved else 'alias' if (aliases or {}).get(annotation_src or '') else 'source',
        **type_meta,
        'span': _span(node),
    }


def _build_rich_indexes(tree: ast.AST, base: _IndexBuilder) -> dict[str, Any]:
    by_id = {node.detyping_id: node for node in ast.walk(tree) if hasattr(node, 'detyping_id')}
    children_by_node = {str(node_id): [child.detyping_id for child in ast.iter_child_nodes(node)] for node_id, node in by_id.items()}
    subtree_by_node = {str(node_id): [child.detyping_id for child in ast.walk(node) if hasattr(child, 'detyping_id')] for node_id, node in by_id.items()}

    function_ids_by_name_line: dict[tuple[str, int], list[int]] = {}
    for raw_id, info in base.functions.items():
        fnode = by_id[int(raw_id)]
        function_ids_by_name_line.setdefault((info['name'], getattr(fnode, 'lineno', -1)), []).append(int(raw_id))
    class_ids_by_name_line: dict[tuple[str, int], int] = {
        (info['name'], getattr(by_id[int(raw_id)], 'lineno', -1)): int(raw_id)
        for raw_id, info in base.classes.items()
    }

    def _definition_start_lines(node: ast.AST) -> list[int]:
        lines: list[int] = []
        for loc in getattr(node, 'pyright_definitions', None) or []:
            start = loc.get('range', {}).get('start', {})
            if start.get('line') is not None:
                lines.append(int(start['line']) + 1)
        return sorted(set(lines))

    int_enum_names = {
        info['name'] for info in base.classes.values()
        if 'IntEnum' in info.get('base_names', []) or 'enum.IntEnum' in info.get('base_names', [])
    }

    aliases: dict[str, str] = {}
    for node in by_id.values():
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            value_src = _name_of_type(node.value) if isinstance(node.value, ast.expr) else None
            if value_src:
                aliases[node.targets[0].id] = aliases.get(value_src, value_src)
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.value is not None:
            value_src = _name_of_type(node.value) if isinstance(node.value, ast.expr) else None
            if value_src:
                aliases[node.target.id] = aliases.get(value_src, value_src)

    annotations: dict[str, dict[str, Any]] = {}
    annotations_by_function: dict[str, list[int]] = {}
    for raw_func_id, info in base.functions.items():
        func_id = int(raw_func_id)
        fdef = by_id[func_id]
        for idx, arg_id in enumerate(info['arg_ids']):
            arg = by_id[arg_id]
            if isinstance(arg, ast.arg) and arg.annotation is not None:
                if info['name'] == '__init__':
                    kind = 'constructor_self_parameter_annotation' if idx == 0 else 'constructor_parameter_annotation'
                elif info['class_id'] is not None:
                    kind = 'method_self_parameter_annotation' if idx == 0 and arg.arg == 'self' else 'method_parameter_annotation'
                else:
                    kind = 'function_parameter_annotation'
                ann_src = _name_of_type(arg.annotation)
                if kind in {'function_parameter_annotation', 'method_parameter_annotation', 'constructor_parameter_annotation'} and ann_src and ('| None' in ann_src or 'None |' in ann_src or ann_src.startswith(('Optional[', 'Union['))):
                    kind = f'{kind}_with_optional'
                rec = _annotation_record(arg, kind=kind, annotation=arg.annotation, function_id=func_id, class_id=info['class_id'], name=arg.arg, param_index=idx, aliases=aliases, int_enums=int_enum_names)
                annotations[str(arg.detyping_id)] = rec
                annotations_by_function.setdefault(str(func_id), []).append(arg.detyping_id)
        if isinstance(fdef, (ast.FunctionDef, ast.AsyncFunctionDef)) and fdef.returns is not None:
            if info['name'] == '__init__':
                kind = 'constructor_return_annotation'
            elif info['class_id'] is not None:
                kind = 'method_return_annotation'
            else:
                kind = 'function_return_annotation'
            rec = _annotation_record(fdef, kind=kind, annotation=fdef.returns, function_id=func_id, class_id=info['class_id'], name=info['name'], aliases=aliases, int_enums=int_enum_names)
            annotations[str(fdef.detyping_id)] = rec
            annotations_by_function.setdefault(str(func_id), []).append(fdef.detyping_id)
    for node in by_id.values():
        if isinstance(node, ast.AnnAssign) and node.annotation is not None:
            func_id = base.enclosing_function_by_node.get(str(node.detyping_id))
            func_info = base.functions.get(str(func_id), {}) if func_id is not None else {}
            func_name = func_info.get('name')
            class_id = base.enclosing_class_by_node.get(str(node.detyping_id))
            is_field = isinstance(node.target, ast.Attribute) and isinstance(node.target.value, ast.Name) and node.target.value.id == 'self'
            target_name = node.target.attr if isinstance(node.target, ast.Attribute) else node.target.id if isinstance(node.target, ast.Name) else None
            has_value = node.value is not None
            value_shape = 'with_none' if isinstance(node.value, ast.Constant) and node.value.value is None else 'with_value' if has_value else 'no_value'
            if is_field:
                prefix = 'init_instance_variable' if func_name == '__init__' else 'non_init_instance_variable'
                kind = f'{prefix}_annotation_{value_shape}'
            elif func_id is None and class_id is None:
                kind = f'module_global_annotation_{value_shape}'
            elif func_id is None and class_id is not None:
                kind = f'class_attribute_annotation_{value_shape}'
            elif class_id is None:
                kind = f'function_local_annotation_{value_shape}'
            elif func_name == '__init__':
                kind = f'constructor_local_annotation_{value_shape}'
            else:
                kind = f'method_local_annotation_{value_shape}'
            rec = _annotation_record(node, kind=kind, annotation=node.annotation, function_id=func_id, class_id=class_id, name=target_name, aliases=aliases, int_enums=int_enum_names)
            annotations[str(node.detyping_id)] = rec
            if func_id is not None:
                annotations_by_function.setdefault(str(func_id), []).append(node.detyping_id)

    calls: dict[str, dict[str, Any]] = {}
    calls_by_function: dict[str, list[int]] = {}
    for node in by_id.values():
        if isinstance(node, ast.Call):
            func_id = base.enclosing_function_by_node.get(str(node.detyping_id))
            rec = {'id': node.detyping_id, 'function_id': func_id, 'arg_ids': [arg.detyping_id for arg in node.args], 'span': _span(node)}
            rec.update(_callee(node))
            calls[str(node.detyping_id)] = rec
            if func_id is not None:
                calls_by_function.setdefault(str(func_id), []).append(node.detyping_id)

    attributes: dict[str, dict[str, Any]] = {}
    for node in by_id.values():
        if isinstance(node, ast.Attribute):
            rec = {
                'id': node.detyping_id,
                'attr': node.attr,
                'value_id': node.value.detyping_id,
                'ctx': type(node.ctx).__name__.lower(),
                'function_id': base.enclosing_function_by_node.get(str(node.detyping_id)),
                'class_id': base.enclosing_class_by_node.get(str(node.detyping_id)),
                'is_self_attr': isinstance(node.value, ast.Name) and node.value.id == 'self',
                'span': _span(node),
            }
            attributes[str(node.detyping_id)] = rec

    nodes_by_function_kind: dict[str, dict[str, list[int]]] = {}
    for raw_node_id, func_id in base.enclosing_function_by_node.items():
        if func_id is None:
            continue
        node = by_id[int(raw_node_id)]
        nodes_by_function_kind.setdefault(str(func_id), {}).setdefault(type(node).__name__, []).append(int(raw_node_id))

    function_uses: dict[str, dict[str, Any]] = {}
    function_uses_by_def: dict[str, list[int]] = {}
    method_uses_by_def: dict[str, list[int]] = {}
    for call_id, call_rec in calls.items():
        name = call_rec.get('name')
        if not name:
            continue
        call_node = by_id[int(call_id)]
        func_node = by_id.get(int(call_rec.get('func_id'))) if call_rec.get('func_id') is not None else None
        def_ids: list[int] = []
        if func_node is not None:
            for line in _definition_start_lines(func_node):
                def_ids.extend(function_ids_by_name_line.get((name, line), []))
        def_ids = sorted(set(def_ids))
        if call_rec.get('kind') == 'name':
            function_uses[call_id] = {**call_rec, 'definition_ids': def_ids}
            for def_id in def_ids:
                function_uses_by_def.setdefault(str(def_id), []).append(int(call_id))
        elif call_rec.get('kind') == 'attribute':
            function_uses[call_id] = {**call_rec, 'definition_ids': def_ids}
            for def_id in def_ids:
                method_uses_by_def.setdefault(str(def_id), []).append(int(call_id))

    field_definitions: dict[str, dict[str, Any]] = {}
    field_uses: dict[str, dict[str, Any]] = {}
    field_uses_by_field: dict[str, list[int]] = {}
    field_annotation_ids_by_name_line: dict[tuple[str, int], list[int]] = {}
    for cls, fields in base.class_field_annotations.items():
        for field, ann_id in fields.items():
            key = f'{cls}.{field}'
            ann_node = by_id[int(ann_id)]
            field_definitions[key] = {'class_name': cls, 'field_name': field, 'annotation_id': ann_id}
            field_annotation_ids_by_name_line.setdefault((field, getattr(ann_node, 'lineno', -1)), []).append(int(ann_id))
    annotation_to_field_keys = {str(info['annotation_id']): key for key, info in field_definitions.items()}
    for attr_id, attr_rec in attributes.items():
        attr_node = by_id[int(attr_id)]
        field = attr_rec['attr']
        matched_ann_ids: list[int] = []
        for line in _definition_start_lines(attr_node):
            matched_ann_ids.extend(field_annotation_ids_by_name_line.get((field, line), []))
        matches = sorted({annotation_to_field_keys[str(ann_id)] for ann_id in matched_ann_ids if str(ann_id) in annotation_to_field_keys})
        field_uses[attr_id] = {**attr_rec, 'field_keys': matches, 'field_resolution': 'pyright'}
        for key in matches:
            field_uses_by_field.setdefault(key, []).append(int(attr_id))

    globals_index = {
        'bindings': {
            bid: binding for bid, binding in base.variables['bindings'].items()
            if binding.get('scope_id') == 0
        },
        'uses_by_binding': {
            bid: base.variables['loads_by_binding'].get(bid, [])
            for bid, binding in base.variables['bindings'].items()
            if binding.get('scope_id') == 0
        },
    }

    def _location_node_ids(locations: list[dict[str, Any]]) -> list[int]:
        result: list[int] = []
        for loc in locations:
            rng = loc.get('range', {})
            start = rng.get('start', {})
            line = start.get('line')
            char = start.get('character')
            if line is None or char is None:
                continue
            py_line = int(line) + 1
            py_col = int(char)
            matches = [
                node_id for node_id, node in by_id.items()
                if getattr(node, 'lineno', None) == py_line and getattr(node, 'col_offset', None) == py_col
            ]
            if matches:
                result.append(min(matches, key=lambda node_id: len(subtree_by_node.get(str(node_id), []))))
        return sorted(set(result))

    symbol_links = {'use_to_defs': {}, 'def_to_uses': {}, 'use_to_type_defs': {}, 'use_to_refs': {}, 'source': {}}
    for node in by_id.values():
        defs = getattr(node, 'pyright_definitions', None)
        type_defs = getattr(node, 'pyright_type_definitions', None)
        refs = getattr(node, 'pyright_references', None)
        if defs is None and type_defs is None and refs is None:
            continue
        node_key = str(node.detyping_id)
        def_ids = _location_node_ids(defs or [])
        type_def_ids = _location_node_ids(type_defs or [])
        ref_ids = _location_node_ids(refs or [])
        if def_ids:
            symbol_links['use_to_defs'][node_key] = def_ids
            symbol_links['source'][node_key] = 'pyright'
            for def_id in def_ids:
                symbol_links['def_to_uses'].setdefault(str(def_id), []).append(node.detyping_id)
        if type_def_ids:
            symbol_links['use_to_type_defs'][node_key] = type_def_ids
        if ref_ids:
            symbol_links['use_to_refs'][node_key] = ref_ids
    for uses in symbol_links['def_to_uses'].values():
        uses.sort()

    annotation_binding_node_by_annotation: dict[str, int] = {}
    annotation_by_binding_node: dict[str, int] = {}
    for ann_id, ann_rec in annotations.items():
        ann_node = by_id[int(ann_id)]
        binding_node_id = None
        if isinstance(ann_node, ast.arg):
            binding_node_id = ann_node.detyping_id
        elif isinstance(ann_node, ast.AnnAssign) and isinstance(ann_node.target, ast.Name):
            binding_node_id = ann_node.target.detyping_id
        if binding_node_id is not None:
            annotation_binding_node_by_annotation[str(ann_id)] = binding_node_id
            annotation_by_binding_node[str(binding_node_id)] = int(ann_id)

    name_reads_by_annotation: dict[str, list[int]] = {}
    name_writes_by_annotation: dict[str, list[int]] = {}
    for ann_id, binding_node_id in annotation_binding_node_by_annotation.items():
        ref_ids = set(symbol_links['use_to_refs'].get(str(binding_node_id), []))
        ref_ids.update(symbol_links['def_to_uses'].get(str(binding_node_id), []))
        ref_ids.discard(int(binding_node_id))
        for ref_id in sorted(ref_ids):
            ref_node = by_id.get(int(ref_id))
            if isinstance(ref_node, ast.Name):
                if isinstance(ref_node.ctx, ast.Load):
                    name_reads_by_annotation.setdefault(ann_id, []).append(ref_id)
                elif isinstance(ref_node.ctx, (ast.Store, ast.Del)):
                    name_writes_by_annotation.setdefault(ann_id, []).append(ref_id)
    for ids in name_reads_by_annotation.values():
        ids[:] = sorted(set(ids))
    for ids in name_writes_by_annotation.values():
        ids[:] = sorted(set(ids))

    def _annotation_id_for_name_use(name: ast.Name) -> int | None:
        for def_id in symbol_links['use_to_defs'].get(str(name.detyping_id), []):
            ann_id = annotation_by_binding_node.get(str(def_id))
            if ann_id is not None:
                return ann_id
        return None

    def _param_annotation_id(function_id: int, param_index: int) -> int | None:
        func = base.functions.get(str(function_id))
        if not func:
            return None
        arg_ids = func.get('arg_ids', [])
        if param_index < 0 or param_index >= len(arg_ids):
            return None
        arg_id = int(arg_ids[param_index])
        return arg_id if str(arg_id) in annotations else None

    reassign_rhs_uses: dict[str, dict[str, Any]] = {}
    reassign_rhs_by_annotation: dict[str, list[int]] = {}
    for ann_id, ann_rec in annotations.items():
        rhs_ids: list[int] = []
        for store_id in name_writes_by_annotation.get(str(ann_id), []):
            store_node = by_id[int(store_id)]
            parent_ids = [pid for pid, child_ids in children_by_node.items() if int(store_id) in child_ids]
            for parent_id in parent_ids:
                parent = by_id[int(parent_id)]
                if isinstance(parent, ast.Assign) and any(target is store_node for target in parent.targets):
                    rhs_ids.append(parent.detyping_id)
                    reassign_rhs_uses[str(parent.detyping_id)] = {
                        'id': parent.detyping_id,
                        'rhs_id': parent.value.detyping_id,
                        'target_id': store_node.detyping_id,
                        'target_annotation_id': int(ann_id),
                        'target_context': ann_rec.get('context'),
                        'target_type_kind': ann_rec.get('type_kind'),
                        'target_type_src': ann_rec.get('resolved_type_src'),
                        **_expr_type_metadata(parent.value, aliases, int_enum_names),
                    }
        if rhs_ids:
            reassign_rhs_by_annotation[ann_id] = sorted(set(rhs_ids))

    field_reassign_rhs_uses: dict[str, dict[str, Any]] = {}
    field_reassign_rhs_by_annotation: dict[str, list[int]] = {}
    for field_key, field_def in field_definitions.items():
        ann_id = field_def.get('annotation_id')
        rhs_ids: list[int] = []
        for attr_id in field_uses_by_field.get(field_key, []):
            attr = by_id[int(attr_id)]
            if not isinstance(attr, ast.Attribute) or not isinstance(attr.ctx, ast.Store):
                continue
            parent_ids = [pid for pid, child_ids in children_by_node.items() if int(attr_id) in child_ids]
            for parent_id in parent_ids:
                parent = by_id[int(parent_id)]
                if isinstance(parent, ast.Assign) and any(target is attr for target in parent.targets):
                    rhs_ids.append(parent.detyping_id)
                    ann_rec = annotations.get(str(ann_id), {})
                    field_reassign_rhs_uses[str(parent.detyping_id)] = {
                        'id': parent.detyping_id,
                        'rhs_id': parent.value.detyping_id,
                        'target_id': attr.detyping_id,
                        'target_annotation_id': ann_id,
                        'target_field_key': field_key,
                        'target_context': ann_rec.get('context'),
                        'target_type_kind': ann_rec.get('type_kind'),
                        'target_type_src': ann_rec.get('resolved_type_src'),
                        **_expr_type_metadata(parent.value, aliases, int_enum_names),
                    }
        if ann_id is not None and rhs_ids:
            field_reassign_rhs_by_annotation[str(ann_id)] = sorted(set(rhs_ids))

    field_read_uses: dict[str, dict[str, Any]] = {}
    field_reads_by_annotation: dict[str, list[int]] = {}
    for field_key, field_def in field_definitions.items():
        ann_id = field_def.get('annotation_id')
        if ann_id is None:
            continue
        ann_rec = annotations.get(str(ann_id), {})
        for attr_id in field_uses_by_field.get(field_key, []):
            attr = by_id[int(attr_id)]
            if not isinstance(attr, ast.Attribute) or not isinstance(attr.ctx, ast.Load):
                continue
            field_reads_by_annotation.setdefault(str(ann_id), []).append(attr.detyping_id)
            field_read_uses[str(attr.detyping_id)] = {
                'id': attr.detyping_id,
                'field_annotation_id': ann_id,
                'field_key': field_key,
                'field_context': ann_rec.get('context'),
                'field_type_kind': ann_rec.get('type_kind'),
                'field_type_src': ann_rec.get('resolved_type_src'),
                **_expr_type_metadata(attr, aliases, int_enum_names),
            }
    for ids in field_reads_by_annotation.values():
        ids.sort()

    attribute_receiver_uses: dict[str, dict[str, Any]] = {}
    attribute_receivers_by_annotation: dict[str, list[int]] = {}
    for attr_id, attr_rec in attributes.items():
        attr = by_id[int(attr_id)]
        if not isinstance(attr, ast.Attribute):
            continue
        receiver = attr.value
        ann_id = None
        if isinstance(receiver, ast.Name):
            ann_id = _annotation_id_for_name_use(receiver)
        if ann_id is None:
            continue
        ann_rec = annotations.get(str(ann_id), {})
        attribute_receivers_by_annotation.setdefault(str(ann_id), []).append(receiver.detyping_id)
        attribute_receiver_uses[str(receiver.detyping_id)] = {
            'id': receiver.detyping_id,
            'attribute_id': attr.detyping_id,
            'attribute_attr': attr.attr,
            'attribute_ctx': type(attr.ctx).__name__.lower(),
            'receiver_annotation_id': ann_id,
            'receiver_context': ann_rec.get('context'),
            'receiver_type_kind': ann_rec.get('type_kind'),
            'receiver_type_src': ann_rec.get('resolved_type_src'),
            **_expr_type_metadata(receiver, aliases, int_enum_names),
        }
    for ids in attribute_receivers_by_annotation.values():
        ids[:] = sorted(set(ids))


    def _subscript_index_exprs(slice_node: ast.expr) -> list[ast.expr]:
        if isinstance(slice_node, ast.Slice):
            out: list[ast.expr] = []
            for part in (slice_node.lower, slice_node.upper, slice_node.step):
                if part is not None:
                    out.extend(_subscript_index_exprs(part))
            return out
        if isinstance(slice_node, ast.Tuple):
            out: list[ast.expr] = []
            for elt in slice_node.elts:
                out.extend(_subscript_index_exprs(elt))
            return out
        return [slice_node]

    primitive_index_converters = {
        'int64', 'int32', 'int16', 'int8',
        'uint64', 'uint32', 'uint16', 'uint8',
    }

    def _expr_is_cinder_scalar_index(expr: ast.expr) -> bool:
        if _expr_type_metadata(expr, aliases, int_enum_names).get('pyright_type_kind') == 'cinder_scalar':
            return True
        if isinstance(expr, ast.Call) and isinstance(expr.func, ast.Name) and expr.func.id in primitive_index_converters:
            return True
        ann_id = _annotation_id_for_name_use(expr) if isinstance(expr, ast.Name) else None
        if ann_id is not None:
            return annotations.get(str(ann_id), {}).get('type_kind') == 'cinder_scalar'
        if isinstance(expr, ast.Attribute):
            field_use = field_uses.get(str(expr.detyping_id), {})
            for field_key in field_use.get('field_keys', []):
                field_ann_id = field_definitions.get(field_key, {}).get('annotation_id')
                if field_ann_id is not None and annotations.get(str(field_ann_id), {}).get('type_kind') == 'cinder_scalar':
                    return True
        return False

    subscript_indices_by_annotation: dict[str, list[int]] = {}
    subscript_results_by_annotation: dict[str, list[int]] = {}
    subscript_result_uses: dict[str, dict[str, Any]] = {}
    for node in by_id.values():
        if not isinstance(node, ast.Subscript):
            continue
        ann_id = None
        if isinstance(node.value, ast.Name):
            ann_id = _annotation_id_for_name_use(node.value)
        if ann_id is None:
            continue
        ann_rec = annotations.get(str(ann_id), {})
        element_type_src = _container_element_type_src(ann_rec.get('annotation_src')) or _container_element_type_src(ann_rec.get('resolved_type_src'))
        for index_expr in _subscript_index_exprs(node.slice):
            if _expr_is_cinder_scalar_index(index_expr):
                subscript_indices_by_annotation.setdefault(str(ann_id), []).append(index_expr.detyping_id)
        subscript_results_by_annotation.setdefault(str(ann_id), []).append(node.detyping_id)
        subscript_result_uses[str(node.detyping_id)] = {
            'id': node.detyping_id,
            'container_annotation_id': ann_id,
            'container_type_kind': ann_rec.get('type_kind'),
            'container_type_src': ann_rec.get('resolved_type_src'),
            'element_type_src': element_type_src,
            'is_slice': isinstance(node.slice, ast.Slice),
            **_expr_type_metadata(node, aliases, int_enum_names),
        }
    for ids in subscript_indices_by_annotation.values():
        ids[:] = sorted(set(ids))
    for ids in subscript_results_by_annotation.values():
        ids[:] = sorted(set(ids))

    call_arg_uses: dict[str, dict[str, Any]] = {}
    call_args_by_param_annotation: dict[str, list[int]] = {}
    literal_call_args_by_param_annotation: dict[str, list[int]] = {}

    def _arg_binding_metadata(arg_node: ast.AST) -> dict[str, Any]:
        if not isinstance(arg_node, ast.Name):
            return {}
        ann_id = _annotation_id_for_name_use(arg_node)
        ann_rec = annotations.get(str(ann_id), {}) if ann_id is not None else {}
        return {
            'arg_binding_annotation_id': ann_id,
            'arg_binding_type_kind': ann_rec.get('type_kind'),
            'arg_binding_type_src': ann_rec.get('resolved_type_src'),
        }

    def _record_call_arg(call_id: int, call_rec: dict[str, Any], arg_index: int, param_annotation_id: int, relation: str) -> None:
        arg_ids = call_rec.get('arg_ids', [])
        if arg_index < 0 or arg_index >= len(arg_ids):
            return
        arg_id = int(arg_ids[arg_index])
        param_rec = annotations.get(str(param_annotation_id), {})
        rec = {
            'id': arg_id,
            'call_id': int(call_id),
            'arg_index': arg_index,
            'relation': relation,
            'callee_param_annotation_id': param_annotation_id,
            'callee_param_context': param_rec.get('context'),
            'callee_param_type_kind': param_rec.get('type_kind'),
            'callee_param_type_src': param_rec.get('resolved_type_src'),
            **_expr_type_metadata(by_id[arg_id], aliases, int_enum_names),
            **_arg_binding_metadata(by_id[arg_id]),
        }
        call_arg_uses[str(arg_id)] = rec
        call_args_by_param_annotation.setdefault(str(param_annotation_id), []).append(arg_id)
        if isinstance(by_id[arg_id], (ast.Constant, ast.List, ast.ListComp, ast.Tuple, ast.Set, ast.Dict)):
            literal_call_args_by_param_annotation.setdefault(str(param_annotation_id), []).append(arg_id)

    for call_id, use_rec in function_uses.items():
        call_rec = calls[str(call_id)]
        if call_rec.get('kind') != 'name':
            continue
        for def_id in use_rec.get('definition_ids', []):
            for arg_index, _arg_id in enumerate(call_rec.get('arg_ids', [])):
                ann_id = _param_annotation_id(int(def_id), arg_index)
                if ann_id is not None:
                    _record_call_arg(int(call_id), call_rec, arg_index, ann_id, 'call_arg_to_function_param')

    for call_id, call_rec in calls.items():
        if call_rec.get('kind') != 'name':
            continue
        call_node = by_id[int(call_id)]
        func_node = by_id.get(int(call_rec.get('func_id'))) if call_rec.get('func_id') is not None else None
        if func_node is None:
            continue
        class_ids: list[int] = []
        for line in _definition_start_lines(func_node):
            class_id = class_ids_by_name_line.get((call_rec.get('name'), line))
            if class_id is not None:
                class_ids.append(class_id)
        for class_id in sorted(set(class_ids)):
            class_rec = base.classes.get(str(class_id), {})
            init_ann_ids = base.class_init_param_annotation_ids.get(class_rec.get('name'), [])
            for arg_index, ann_id in enumerate(init_ann_ids[:len(call_rec.get('arg_ids', []))]):
                if str(ann_id) in annotations:
                    _record_call_arg(int(call_id), call_rec, arg_index, int(ann_id), 'call_arg_to_constructor_param')

    for call_id, use_rec in function_uses.items():
        call_rec = calls[str(call_id)]
        if call_rec.get('kind') != 'attribute':
            continue
        call_node = by_id[int(call_id)]
        assert isinstance(call_node, ast.Call)
        is_unbound_class_call = False
        if isinstance(call_node.func, ast.Attribute) and isinstance(call_node.func.value, ast.Name):
            for line in _definition_start_lines(call_node.func.value):
                if class_ids_by_name_line.get((call_node.func.value.id, line)) is not None:
                    is_unbound_class_call = True
                    break
        param_offset = 0 if is_unbound_class_call else 1
        relation = 'call_arg_to_unbound_method_param' if is_unbound_class_call else 'call_arg_to_method_param'
        for def_id in use_rec.get('definition_ids', []):
            for arg_index, _arg_id in enumerate(call_rec.get('arg_ids', [])):
                ann_id = _param_annotation_id(int(def_id), arg_index + param_offset)
                if ann_id is not None:
                    _record_call_arg(int(call_id), call_rec, arg_index, ann_id, relation)

    for ids in call_args_by_param_annotation.values():
        ids.sort()
    call_args_by_param_annotation_and_arg_kind: dict[str, dict[str, list[int]]] = {}
    for arg_id, use in call_arg_uses.items():
        ann_id = str(use['callee_param_annotation_id'])
        arg_kind = use.get('pyright_type_kind') or 'dynamic_unknown'
        call_args_by_param_annotation_and_arg_kind.setdefault(ann_id, {}).setdefault(arg_kind, []).append(int(arg_id))
    for by_kind in call_args_by_param_annotation_and_arg_kind.values():
        for ids in by_kind.values():
            ids.sort()

    override_family_annotations_by_annotation: dict[str, list[int]] = {}
    annotation_sync_groups: dict[str, list[int]] = {}
    pyright_class_bases: dict[str, list[int]] = {}
    for raw_class_id, cls in base.classes.items():
        base_class_ids: list[int] = []
        for base_id in cls.get('base_ids', []):
            base_node = by_id.get(int(base_id))
            if base_node is None:
                continue
            base_name = _name_of_type(base_node)
            for line in _definition_start_lines(base_node):
                resolved = class_ids_by_name_line.get((base_name, line))
                if resolved is not None:
                    base_class_ids.append(resolved)
        pyright_class_bases[str(raw_class_id)] = sorted(set(base_class_ids))

    def _ancestor_class_ids(class_id: int) -> set[int]:
        seen: set[int] = set()
        stack = list(pyright_class_bases.get(str(class_id), []))
        while stack:
            parent = stack.pop()
            if parent in seen:
                continue
            seen.add(parent)
            stack.extend(pyright_class_bases.get(str(parent), []))
        return seen

    methods_by_class_name: dict[tuple[int, str], int] = {}
    for raw_func_id, func in base.functions.items():
        class_id = func.get('class_id')
        if class_id is not None:
            methods_by_class_name[(int(class_id), func['name'])] = int(raw_func_id)
    override_edges: dict[int, set[int]] = {}
    method_items = list(methods_by_class_name.items())
    for (class_id, method_name), func_id in method_items:
        for (other_class_id, other_name), other_func_id in method_items:
            if func_id == other_func_id or method_name != other_name:
                continue
            if other_class_id in _ancestor_class_ids(class_id) or class_id in _ancestor_class_ids(other_class_id):
                override_edges.setdefault(func_id, set()).add(other_func_id)
                override_edges.setdefault(other_func_id, set()).add(func_id)
    override_func_groups: list[list[int]] = []
    seen_funcs: set[int] = set()
    for func_id in sorted(override_edges):
        if func_id in seen_funcs:
            continue
        stack = [func_id]
        group: set[int] = set()
        while stack:
            item = stack.pop()
            if item in group:
                continue
            group.add(item)
            stack.extend(override_edges.get(item, set()))
        seen_funcs.update(group)
        if len(group) > 1:
            override_func_groups.append(sorted(group))

    for func_ids in override_func_groups:
        return_ids = [base.functions[str(fid)].get('return_annotation_id') for fid in func_ids]
        return_ids = [int(item) for item in return_ids if item is not None and str(item) in annotations]
        for ann_id in return_ids:
            override_family_annotations_by_annotation[str(ann_id)] = sorted(item for item in return_ids if item != ann_id)
            annotation_sync_groups[str(ann_id)] = sorted(return_ids)
        max_args = max(len(base.functions[str(fid)].get('arg_ids', [])) for fid in func_ids)
        for index in range(max_args):
            param_ann_ids: list[int] = []
            for fid in func_ids:
                ann_id = _param_annotation_id(fid, index)
                if ann_id is not None:
                    param_ann_ids.append(ann_id)
            if len(param_ann_ids) > 1:
                for ann_id in param_ann_ids:
                    override_family_annotations_by_annotation[str(ann_id)] = sorted(item for item in param_ann_ids if item != ann_id)
                    annotation_sync_groups[str(ann_id)] = sorted(param_ann_ids)

    call_result_uses: dict[str, dict[str, Any]] = {}
    call_results_by_return_annotation: dict[str, list[int]] = {}
    call_ids_by_return_def: dict[str, list[int]] = {}
    for source in (function_uses_by_def, method_uses_by_def):
        for def_id, call_ids in source.items():
            call_ids_by_return_def.setdefault(str(def_id), []).extend(int(call_id) for call_id in call_ids)
    for def_id, call_ids in call_ids_by_return_def.items():
        func = base.functions.get(str(def_id), {})
        return_annotation_id = func.get('return_annotation_id')
        if return_annotation_id is not None and str(return_annotation_id) in annotations:
            call_results_by_return_annotation[str(return_annotation_id)] = sorted(set(int(call_id) for call_id in call_ids))
            ann_rec = annotations[str(return_annotation_id)]
            for call_id in call_ids:
                call_node = by_id[int(call_id)]
                call_result_uses[str(call_id)] = {
                    'id': int(call_id),
                    'return_annotation_id': return_annotation_id,
                    'return_context': ann_rec.get('context'),
                    'return_type_kind': ann_rec.get('type_kind'),
                    'return_type_src': ann_rec.get('resolved_type_src'),
                    **_expr_type_metadata(call_node, aliases, int_enum_names),
                }

    def _place_record(place: Place, node_id: int, **payload: Any) -> dict[str, Any]:
        return {
            'place': str(place),
            'node_id': int(node_id),
            'affinity': affinity_for_place(place),
            'slot_key': str(int(node_id)),
            **payload,
        }

    place_records_by_annotation: dict[str, list[dict[str, Any]]] = {}
    for raw_ann_id, rec in annotations.items():
        ann_id = int(raw_ann_id)
        records: list[dict[str, Any]] = [_place_record(Place.ANNOTATION_SITE, ann_id)]
        ann_node = by_id.get(ann_id)
        if isinstance(ann_node, ast.AnnAssign) and ann_node.value is not None:
            records.append(_place_record(Place.ANNOTATED_VALUE, ann_node.value.detyping_id))

        function_id = rec.get('function_id')
        if rec.get('context') in {'function_return_annotation', 'method_return_annotation'} and function_id is not None:
            for node_id in base.returns_by_function.get(str(function_id), []):
                records.append(_place_record(Place.RETURN_VALUES, int(node_id)))

        read_place = Place.MODULE_GLOBAL_READS if rec.get('context', '').startswith('module_global_') else Place.LOCAL_READS
        for node_id in name_reads_by_annotation.get(str(ann_id), []):
            records.append(_place_record(read_place, int(node_id)))
        for node_id in reassign_rhs_by_annotation.get(str(ann_id), []):
            records.append(_place_record(Place.REASSIGN_RHS, int(node_id)))
        for node_id in field_reassign_rhs_by_annotation.get(str(ann_id), []):
            records.append(_place_record(Place.FIELD_REASSIGN_RHS, int(node_id)))
        for node_id in field_reads_by_annotation.get(str(ann_id), []):
            records.append(_place_record(Place.FIELD_READS, int(node_id)))
        for node_id in attribute_receivers_by_annotation.get(str(ann_id), []):
            records.append(_place_record(Place.ATTRIBUTE_RECEIVERS, int(node_id)))
        for node_id in subscript_indices_by_annotation.get(str(ann_id), []):
            records.append(_place_record(Place.SUBSCRIPT_INDICES, int(node_id)))
        for node_id in subscript_results_by_annotation.get(str(ann_id), []):
            use = subscript_result_uses.get(str(node_id), {})
            records.append(_place_record(
                Place.SUBSCRIPT_RESULTS,
                int(node_id),
                is_slice=use.get('is_slice'),
                container_type_src=use.get('container_type_src'),
                element_type_src=use.get('element_type_src'),
            ))
        for node_id in override_family_annotations_by_annotation.get(str(ann_id), []):
            records.append(_place_record(Place.OVERRIDE_FAMILY_ANNOTATION_SITES, int(node_id)))
        literal_arg_ids = {int(node_id) for node_id in literal_call_args_by_param_annotation.get(str(ann_id), [])}
        scalar_arg_ids = {int(node_id) for node_id in call_args_by_param_annotation_and_arg_kind.get(str(ann_id), {}).get('cinder_scalar', [])}
        object_arg_ids = {int(node_id) for node_id in call_args_by_param_annotation_and_arg_kind.get(str(ann_id), {}).get('python_user_object', [])}
        for node_id in call_args_by_param_annotation.get(str(ann_id), []):
            node_id = int(node_id)
            if node_id in literal_arg_ids:
                records.append(_place_record(Place.CALL_ARGS_TO_PARAMETER_LITERAL, node_id))
            elif node_id in scalar_arg_ids:
                records.append(_place_record(Place.CALL_ARGS_TO_PARAMETER_FROM_CINDER_SCALAR, node_id))
            elif node_id in object_arg_ids:
                records.append(_place_record(Place.CALL_ARGS_TO_PARAMETER_FROM_PYTHON_OBJECT, node_id))
            else:
                records.append(_place_record(Place.CALL_ARGS_TO_PARAMETER_VALUE, node_id))
        for node_id in call_results_by_return_annotation.get(str(ann_id), []):
            records.append(_place_record(Place.CALL_RESULTS_FROM_RETURN, int(node_id)))
        place_records_by_annotation[str(ann_id)] = records

    return {
        'aliases': aliases,
        'int_enum_names': sorted(int_enum_names),
        'alias_type_metadata': {alias: classification_metadata(target, aliases=set(aliases.keys()), int_enums=int_enum_names) for alias, target in aliases.items()},
        'functions': base.functions,
        'function_uses': function_uses,
        'function_uses_by_def': function_uses_by_def,
        'method_uses_by_def': method_uses_by_def,
        'classes': base.classes,
        'calls': calls,
        'calls_by_function': calls_by_function,
        'call_arg_uses': call_arg_uses,
        'name_reads_by_annotation': name_reads_by_annotation,
        'name_writes_by_annotation': name_writes_by_annotation,
        'call_args_by_param_annotation': call_args_by_param_annotation,
        'literal_call_args_by_param_annotation': literal_call_args_by_param_annotation,
        'call_args_by_param_annotation_and_arg_kind': call_args_by_param_annotation_and_arg_kind,
        'reassign_rhs_uses': reassign_rhs_uses,
        'reassign_rhs_by_annotation': reassign_rhs_by_annotation,
        'field_reassign_rhs_uses': field_reassign_rhs_uses,
        'field_reassign_rhs_by_annotation': field_reassign_rhs_by_annotation,
        'field_read_uses': field_read_uses,
        'field_reads_by_annotation': field_reads_by_annotation,
        'attribute_receiver_uses': attribute_receiver_uses,
        'attribute_receivers_by_annotation': attribute_receivers_by_annotation,
        'subscript_indices_by_annotation': subscript_indices_by_annotation,
        'subscript_results_by_annotation': subscript_results_by_annotation,
        'subscript_result_uses': subscript_result_uses,
        'override_family_annotations_by_annotation': override_family_annotations_by_annotation,
        'annotation_sync_groups': annotation_sync_groups,
        'pyright_class_bases': pyright_class_bases,
        'override_function_groups': override_func_groups,
        'call_result_uses': call_result_uses,
        'call_results_by_return_annotation': call_results_by_return_annotation,
        'attributes': attributes,
        'field_definitions': field_definitions,
        'field_uses': field_uses,
        'field_uses_by_field': field_uses_by_field,
        'annotations': annotations,
        'place_records_by_annotation': place_records_by_annotation,
        'annotations_by_function': annotations_by_function,
        'ann_assigns_by_function': base.ann_assigns_by_function,
        'returns_by_function': base.returns_by_function,
        'assigns_by_function': base.assigns_by_function,
        'nodes_by_kind': base.nodes_by_kind,
        'nodes_by_function_kind': nodes_by_function_kind,
        'children_by_node': children_by_node,
        'subtree_by_node': subtree_by_node,
        'enclosing_function_by_node': base.enclosing_function_by_node,
        'enclosing_class_by_node': base.enclosing_class_by_node,
        'func_classes': base.func_classes,
        'class_bases': base.class_bases,
        'function_annotation_ids': base.function_annotation_ids,
        'class_field_annotations': base.class_field_annotations,
        'class_init_param_annotation_ids': base.class_init_param_annotation_ids,
        'variables': base.variables,
        'globals': globals_index,
        'symbol_links': symbol_links,
    }


def ast_to_data(tree: ast.AST) -> AstData:
    nodes: dict[str, dict[str, Any]] = {}
    for node in ast.walk(tree):
        fields = {name: _value_to_json(value) for name, value in ast.iter_fields(node)}
        attrs = {name: _value_to_json(getattr(node, name)) for name in _LOCATION_ATTRS + _DECORATION_ATTRS if hasattr(node, name)}
        if hasattr(node, 'pyright_type'):
            attrs['pyright_type'] = getattr(node, 'pyright_type')
        for pyright_attr in ('pyright_definitions', 'pyright_type_definitions', 'pyright_references'):
            if hasattr(node, pyright_attr):
                attrs[pyright_attr] = getattr(node, pyright_attr)
        nodes[str(node.detyping_id)] = {'id': node.detyping_id, 'kind': type(node).__name__, 'fields': fields, 'attrs': attrs}
    builder = _IndexBuilder()
    builder.visit(tree)
    indexes = _build_rich_indexes(tree, builder)
    return AstData(root_id=tree.detyping_id, nodes=nodes, indexes=indexes)


def _json_to_value(value: Any, made: dict[int, ast.AST]) -> Any:
    if isinstance(value, dict) and '$node' in value:
        return made[int(value['$node'])]
    if isinstance(value, dict) and '$tuple' in value:
        return tuple(_json_to_value(item, made) for item in value['$tuple'])
    if isinstance(value, list):
        return [_json_to_value(item, made) for item in value]
    return value


def ast_from_data(data: AstData | dict[str, Any]) -> ast.AST:
    if isinstance(data, dict):
        data = AstData(root_id=data['root_id'], nodes=data['nodes'], indexes=data.get('indexes', {}))
    made: dict[int, ast.AST] = {}
    for raw_id, node_data in data.nodes.items():
        cls = getattr(ast, node_data['kind'])
        made[int(raw_id)] = cls.__new__(cls)
    for raw_id, node_data in data.nodes.items():
        node = made[int(raw_id)]
        for name, value in node_data['fields'].items():
            setattr(node, name, _json_to_value(value, made))
        for name, value in node_data.get('attrs', {}).items():
            setattr(node, name, _json_to_value(value, made))
    root = made[data.root_id]
    by_id = {getattr(node, 'detyping_id'): node for node in ast.walk(root) if hasattr(node, 'detyping_id')}
    variables = data.indexes.get('variables', {})
    uses = variables.get('uses', {})
    annotations = data.indexes.get('annotations', {})
    calls = data.indexes.get('calls', {})
    attributes = data.indexes.get('attributes', {})
    symbol_links = data.indexes.get('symbol_links', {})
    enclosing_functions = data.indexes.get('enclosing_function_by_node', {})
    enclosing_classes = data.indexes.get('enclosing_class_by_node', {})
    subtree_by_node = data.indexes.get('subtree_by_node', {})
    children_by_node = data.indexes.get('children_by_node', {})
    for node_id, node in by_id.items():
        key = str(node_id)
        node.detyping_node_index = by_id
        node.detyping_indexes = data.indexes
        node.detyping_subtree_ids = subtree_by_node.get(key, [child.detyping_id for child in ast.walk(node) if hasattr(child, 'detyping_id')])
        node.detyping_child_ids = children_by_node.get(key, [child.detyping_id for child in ast.iter_child_nodes(node)])
        node.detyping_enclosing_function_id = enclosing_functions.get(key)
        node.detyping_enclosing_class_id = enclosing_classes.get(key)
        if key in uses:
            node.detyping_variable = uses[key]
            node.detyping_binding_id = uses[key].get('binding_id')
        if key in annotations:
            node.detyping_annotation = annotations[key]
        if key in calls:
            node.detyping_call = data.indexes.get('function_uses', {}).get(key, calls[key])
        if key in attributes:
            node.detyping_attribute = data.indexes.get('field_uses', {}).get(key, attributes[key])
        node.detyping_symbol = {
            'definition_ids': symbol_links.get('use_to_defs', {}).get(key, []),
            'type_definition_ids': symbol_links.get('use_to_type_defs', {}).get(key, []),
            'reference_ids': symbol_links.get('use_to_refs', {}).get(key, []),
            'source': symbol_links.get('source', {}).get(key),
        }
    root.detyping_indexes = data.indexes
    return root


def build_ast_data(source: str) -> AstData:
    from .ast_utils import label_tree
    from .typecheck import decorate_ast_with_pyright

    tree = ast.parse(source)
    decorate_ast_with_pyright(tree, source)
    label_tree(tree)
    return ast_to_data(tree)


def write_ast_data(source: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(build_ast_data(source).to_json(), indent=2), encoding='utf-8')
    return output_path


def read_ast_data(path: Path) -> AstData:
    raw = json.loads(path.read_text(encoding='utf-8'))
    return AstData(root_id=raw['root_id'], nodes=raw['nodes'], indexes=raw.get('indexes', {}))
