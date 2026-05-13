"""Concrete AST edits for minimal intents."""

from __future__ import annotations

import ast
from ast import AST, FunctionDef

from .intent_types import Intent
from .rules import classify_type


def _box_expr(expr: ast.expr) -> ast.expr:
    return ast.Call(func=ast.Name(id='box', ctx=ast.Load()), args=[expr], keywords=[])


def make_wrap_expr(expr: ast.expr, typ: ast.expr | None) -> ast.expr:
    if typ is None:
        return _box_expr(expr)
    kind = classify_type(typ)
    if kind == 'primitive':
        type_name = typ.id if isinstance(typ, ast.Name) else ast.unparse(typ)
        return ast.Call(func=ast.Name(id=type_name, ctx=ast.Load()), args=[expr], keywords=[])
    if kind == 'checked_list':
        return ast.Call(func=typ, args=[expr], keywords=[])
    if kind in ('cast', 'container'):
        return ast.Call(func=ast.Name(id='cast', ctx=ast.Load()), args=[typ, expr], keywords=[])
    return expr


def make_wrap_constructor_expr(expr: ast.expr, typ: ast.expr | None) -> ast.expr:
    if typ is None:
        return _box_expr(expr)
    return ast.Call(func=typ, args=[expr], keywords=[])


def make_wrap_cast_expr(expr: ast.expr, typ: ast.expr | None) -> ast.expr:
    if typ is None:
        return _box_expr(expr)
    return ast.Call(func=ast.Name(id='cast', ctx=ast.Load()), args=[typ, expr], keywords=[])


def make_wrap_then_box_expr(expr: ast.expr, typ: ast.expr | None) -> ast.expr:
    return _box_expr(make_wrap_expr(expr, typ))


class _SpecificNodeReplacer(ast.NodeTransformer):
    def __init__(self, target_id: int, replacement: ast.expr):
        self.target_id = target_id
        self.replacement = replacement

    def generic_visit(self, node: AST) -> AST:
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                new_list = []
                for item in value:
                    if isinstance(item, ast.AST) and id(item) == self.target_id:
                        new_list.append(self.replacement)
                    elif isinstance(item, ast.AST):
                        new_list.append(self.visit(item))
                    else:
                        new_list.append(item)
                setattr(node, field, new_list)
            elif isinstance(value, ast.AST):
                if id(value) == self.target_id:
                    setattr(node, field, self.replacement)
                else:
                    self.visit(value)
        return node


def _apply_remove_annotation(intent: Intent, nodes: dict[int, AST]) -> None:
    node = nodes[intent.location_id]
    if isinstance(node, FunctionDef):
        node.returns = None
        return
    if isinstance(node, ast.arg):
        node.annotation = None
        return
    if isinstance(node, ast.AnnAssign):
        node.annotation = None
        return
    raise TypeError(f'Unsupported node for remove_annotation: {type(node).__name__}')


def _apply_rewrite_param_binding(intent: Intent, nodes: dict[int, AST]) -> None:
    # Minimal intent rows no longer carry param indexes, so this edit is intentionally inert.
    node = nodes[intent.location_id]
    if isinstance(node, ast.arg):
        node.annotation = None
        return
    if isinstance(node, FunctionDef):
        for arg in node.args.args:
            arg.annotation = None
        return
    raise TypeError(f'Unsupported node for rewrite_param_binding: {type(node).__name__}')


def _apply_unwrap_checked_return_value(intent: Intent, nodes: dict[int, AST]) -> None:
    node = nodes[intent.location_id]
    if isinstance(node, ast.Return) and node.value is not None and isinstance(node.value, ast.Call) and node.value.args:
        node.value = node.value.args[0]
        return
    raise TypeError(f'Unsupported node for unwrap_checked_return_value: {type(node).__name__}')


def _apply_unwrap_box(intent: Intent, nodes: dict[int, AST]) -> None:
    node = nodes[intent.location_id]
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'box' and len(node.args) == 1:
        # No context is carried anymore, so this only mutates directly representable calls poorly.
        return
    raise TypeError(f'Unsupported node for unwrap_box: {type(node).__name__}')


def _apply_wrap_like(intent: Intent, nodes: dict[int, AST], make_expr) -> None:
    node = nodes[intent.location_id]
    if isinstance(node, ast.AnnAssign):
        if node.value is not None:
            node.value = make_expr(node.value, intent.typ)
        return
    if isinstance(node, ast.Return):
        if node.value is not None:
            node.value = make_expr(node.value, intent.typ)
        return
    if isinstance(node, ast.Assign):
        node.value = make_expr(node.value, intent.typ)
        return
    if isinstance(node, ast.expr):
        replacement = make_expr(node, intent.typ)
        ast.copy_location(replacement, node)
        root = nodes.get(0)
        if root is not None:
            _SpecificNodeReplacer(id(node), replacement).visit(root)
            return
        raise TypeError('wrap expression requires root node 0')
    raise TypeError(f'Unsupported node for wrap: {type(node).__name__}')


def _apply_wrap(intent: Intent, nodes: dict[int, AST]) -> None:
    _apply_wrap_like(intent, nodes, make_wrap_expr)


def _apply_wrap_then_box(intent: Intent, nodes: dict[int, AST]) -> None:
    _apply_wrap_like(intent, nodes, make_wrap_then_box_expr)


def _apply_wrap_constructor(intent: Intent, nodes: dict[int, AST]) -> None:
    _apply_wrap_like(intent, nodes, make_wrap_constructor_expr)


def _apply_wrap_cast(intent: Intent, nodes: dict[int, AST]) -> None:
    _apply_wrap_like(intent, nodes, make_wrap_cast_expr)


def apply_intent(intent: Intent, nodes: dict[int, AST]) -> None:
    if intent.kind == 'remove_annotation':
        _apply_remove_annotation(intent, nodes)
        return
    if intent.kind == 'rewrite_param_binding':
        _apply_rewrite_param_binding(intent, nodes)
        return
    if intent.kind == 'unwrap_checked_return_value':
        _apply_unwrap_checked_return_value(intent, nodes)
        return
    if intent.kind == 'wrap':
        _apply_wrap(intent, nodes)
        return
    if intent.kind == 'wrap_then_box':
        _apply_wrap_then_box(intent, nodes)
        return
    if intent.kind == 'wrap_constructor':
        _apply_wrap_constructor(intent, nodes)
        return
    if intent.kind == 'wrap_cast':
        _apply_wrap_cast(intent, nodes)
        return
    if intent.kind == 'unwrap_box':
        _apply_unwrap_box(intent, nodes)
        return
    raise ValueError(f'Unknown intent kind: {intent.kind}')
