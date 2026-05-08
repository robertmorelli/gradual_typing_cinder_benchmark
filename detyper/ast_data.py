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
        ids = self.indexes.get('calls_by_name', {}).get(name, []) + self.indexes.get('method_calls_by_attr', {}).get(name, [])
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
        self.calls_by_name: dict[str, list[int]] = {}
        self.method_calls_by_attr: dict[str, list[int]] = {}
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
        self.classes[str(node.detyping_id)] = {'id': node.detyping_id, 'name': node.name, 'base_names': base_names}
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
        if isinstance(node.func, ast.Name):
            self.calls_by_name.setdefault(node.func.id, []).append(node.detyping_id)
        elif isinstance(node.func, ast.Attribute):
            self.method_calls_by_attr.setdefault(node.func.attr, []).append(node.detyping_id)
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
    if ':' in text and not text.startswith(('list[', 'dict[', 'tuple[', 'Optional[', 'Union[')):
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
    if pyright_resolved in {'Unknown', 'Any'}:
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

    functions_by_name: dict[str, list[int]] = {}
    for raw_id, info in base.functions.items():
        functions_by_name.setdefault(info['name'], []).append(int(raw_id))

    classes_by_name: dict[str, int] = {info['name']: int(raw_id) for raw_id, info in base.classes.items()}
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
            if is_field:
                prefix = 'init_instance_variable' if func_name == '__init__' else 'non_init_instance_variable'
                kind = f'{prefix}_annotation_{"with_value" if has_value else "no_value"}'
            elif func_id is None and class_id is None:
                kind = f'module_global_annotation_{"with_value" if has_value else "no_value"}'
            elif func_id is None and class_id is not None:
                kind = f'class_attribute_annotation_{"with_value" if has_value else "no_value"}'
            elif class_id is None:
                kind = f'function_local_annotation_{"with_value" if has_value else "no_value"}'
            elif func_name == '__init__':
                kind = f'constructor_local_annotation_{"with_value" if has_value else "no_value"}'
            else:
                kind = f'method_local_annotation_{"with_value" if has_value else "no_value"}'
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
    self_fields_by_name: dict[str, list[int]] = {}
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
            if rec['is_self_attr']:
                self_fields_by_name.setdefault(node.attr, []).append(node.detyping_id)

    nodes_by_function_kind: dict[str, dict[str, list[int]]] = {}
    for raw_node_id, func_id in base.enclosing_function_by_node.items():
        if func_id is None:
            continue
        node = by_id[int(raw_node_id)]
        nodes_by_function_kind.setdefault(str(func_id), {}).setdefault(type(node).__name__, []).append(int(raw_node_id))

    function_uses: dict[str, dict[str, Any]] = {}
    function_uses_by_def: dict[str, list[int]] = {}
    method_uses_by_name: dict[str, list[int]] = {}
    method_uses_by_def: dict[str, list[int]] = {}
    for call_id, call_rec in calls.items():
        name = call_rec.get('name')
        if not name:
            continue
        if call_rec.get('kind') == 'name':
            def_ids = functions_by_name.get(name, [])
            function_uses[call_id] = {**call_rec, 'definition_ids': def_ids}
            for def_id in def_ids:
                function_uses_by_def.setdefault(str(def_id), []).append(int(call_id))
        elif call_rec.get('kind') == 'attribute':
            def_ids = functions_by_name.get(name, [])
            method_uses_by_name.setdefault(name, []).append(int(call_id))
            function_uses[call_id] = {**call_rec, 'definition_ids': def_ids}
            for def_id in def_ids:
                method_uses_by_def.setdefault(str(def_id), []).append(int(call_id))

    field_definitions: dict[str, dict[str, Any]] = {}
    field_uses: dict[str, dict[str, Any]] = {}
    field_uses_by_field: dict[str, list[int]] = {}
    for cls, fields in base.class_field_annotations.items():
        for field, ann_id in fields.items():
            key = f'{cls}.{field}'
            field_definitions[key] = {'class_name': cls, 'field_name': field, 'annotation_id': ann_id}
    for attr_id, attr_rec in attributes.items():
        field = attr_rec['attr']
        value_node = by_id.get(int(attr_rec['value_id']))
        value_type = _clean_pyright_type(getattr(value_node, 'pyright_type', None)) if value_node is not None else None
        value_class = None
        if value_type:
            value_class = value_type.split('|', 1)[0].strip().split('[', 1)[0].split('.')[-1]
            if value_class.startswith('Self@'):
                value_class = value_class.split('@', 1)[1]
        precise: list[str] = []
        cursor = value_class
        while cursor:
            key = f'{cursor}.{field}'
            if key in field_definitions:
                precise = [key]
                break
            cursor = base.class_bases.get(cursor)
        fallback = [key for key, info in field_definitions.items() if info['field_name'] == field]
        matches = precise or (fallback if len(fallback) == 1 else [])
        field_uses[attr_id] = {**attr_rec, 'field_keys': matches, 'receiver_type_src': value_type, 'receiver_class': value_class}
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
        ann_node = by_id[int(ann_id)]
        if not (isinstance(ann_node, ast.AnnAssign) and isinstance(ann_node.target, ast.Name)):
            continue
        binding_id = None
        for bid, binding in base.variables['bindings'].items():
            if binding.get('node_id') == ann_node.target.detyping_id:
                binding_id = bid
                break
        if binding_id is None:
            continue
        rhs_ids: list[int] = []
        for store_id in base.variables['stores_by_binding'].get(str(binding_id), []):
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

    binding_annotation_by_binding: dict[str, int] = {}
    for ann_id, ann_rec in annotations.items():
        ann_node = by_id[int(ann_id)]
        binding_node_id = None
        if isinstance(ann_node, ast.arg):
            binding_node_id = ann_node.detyping_id
        elif isinstance(ann_node, ast.AnnAssign) and isinstance(ann_node.target, ast.Name):
            binding_node_id = ann_node.target.detyping_id
        if binding_node_id is None:
            continue
        for bid, binding in base.variables['bindings'].items():
            if binding.get('node_id') == binding_node_id:
                binding_annotation_by_binding[str(bid)] = int(ann_id)
                break

    call_arg_uses: dict[str, dict[str, Any]] = {}
    call_args_by_param_annotation: dict[str, list[int]] = {}

    def _arg_binding_metadata(arg_node: ast.AST) -> dict[str, Any]:
        if not isinstance(arg_node, ast.Name):
            return {}
        use = base.variables['uses'].get(str(arg_node.detyping_id), {})
        binding_id = use.get('binding_id')
        if binding_id is None:
            return {}
        ann_id = binding_annotation_by_binding.get(str(binding_id))
        ann_rec = annotations.get(str(ann_id), {}) if ann_id is not None else {}
        return {
            'arg_binding_id': binding_id,
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
        class_id = classes_by_name.get(call_rec.get('name'))
        if class_id is None:
            continue
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
        is_unbound_class_call = (
            isinstance(call_node.func, ast.Attribute)
            and isinstance(call_node.func.value, ast.Name)
            and call_node.func.value.id in classes_by_name
        )
        param_offset = 0 if is_unbound_class_call else 1
        relation = 'call_arg_to_unbound_method_param' if is_unbound_class_call else 'call_arg_to_method_param'
        receiver_class_name = call_node.func.value.id if is_unbound_class_call and isinstance(call_node.func, ast.Attribute) and isinstance(call_node.func.value, ast.Name) else None
        for def_id in use_rec.get('definition_ids', []):
            if receiver_class_name is not None:
                def_func = base.functions.get(str(def_id), {})
                def_class = base.classes.get(str(def_func.get('class_id')), {})
                if def_class.get('name') != receiver_class_name:
                    continue
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
    functions_grouped: dict[tuple[str, int | None], list[int]] = {}
    for raw_func_id, func in base.functions.items():
        functions_grouped.setdefault((func['name'], len(func.get('arg_ids', []))), []).append(int(raw_func_id))
    for _group, func_ids in functions_grouped.items():
        if len(func_ids) < 2:
            continue
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
    for def_id, call_ids in function_uses_by_def.items():
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

    return {
        'aliases': aliases,
        'int_enum_names': sorted(int_enum_names),
        'alias_type_metadata': {alias: classification_metadata(target, aliases=set(aliases.keys()), int_enums=int_enum_names) for alias, target in aliases.items()},
        'functions': base.functions,
        'functions_by_name': functions_by_name,
        'function_uses': function_uses,
        'function_uses_by_def': function_uses_by_def,
        'method_uses_by_name': method_uses_by_name,
        'method_uses_by_def': method_uses_by_def,
        'classes': base.classes,
        'classes_by_name': classes_by_name,
        'calls': calls,
        'calls_by_name': base.calls_by_name,
        'method_calls_by_attr': base.method_calls_by_attr,
        'calls_by_function': calls_by_function,
        'call_arg_uses': call_arg_uses,
        'call_args_by_param_annotation': call_args_by_param_annotation,
        'call_args_by_param_annotation_and_arg_kind': call_args_by_param_annotation_and_arg_kind,
        'reassign_rhs_uses': reassign_rhs_uses,
        'reassign_rhs_by_annotation': reassign_rhs_by_annotation,
        'field_reassign_rhs_uses': field_reassign_rhs_uses,
        'field_reassign_rhs_by_annotation': field_reassign_rhs_by_annotation,
        'field_read_uses': field_read_uses,
        'field_reads_by_annotation': field_reads_by_annotation,
        'override_family_annotations_by_annotation': override_family_annotations_by_annotation,
        'annotation_sync_groups': annotation_sync_groups,
        'call_result_uses': call_result_uses,
        'call_results_by_return_annotation': call_results_by_return_annotation,
        'attributes': attributes,
        'self_fields_by_name': self_fields_by_name,
        'field_definitions': field_definitions,
        'field_uses': field_uses,
        'field_uses_by_field': field_uses_by_field,
        'annotations': annotations,
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
