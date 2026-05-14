"""Concrete AST edits for minimal intents."""

from __future__ import annotations

import ast
from ast import AST, FunctionDef

from .intent_types import Intent
from .rules import classify_type


_VALID_CAST_KINDS = frozenset({'cast', 'container', 'checked_list'})


def _parse_typ(typ_src: str | None) -> ast.expr | None:
    if typ_src is None:
        return None
    try:
        return ast.parse(typ_src, mode='eval').body
    except SyntaxError:
        return None


def _box_expr(expr: ast.expr) -> ast.expr:
    return ast.Call(func=ast.Name(id='box', ctx=ast.Load()), args=[expr], keywords=[])


def _cast_expr(expr: ast.expr, typ: ast.expr) -> ast.expr:
    return ast.Call(func=ast.Name(id='cast', ctx=ast.Load()), args=[typ, expr], keywords=[])


def _constructor_expr(expr: ast.expr, typ: ast.expr) -> ast.expr:
    return ast.Call(func=typ, args=[expr], keywords=[])


def _primitive_expr(expr: ast.expr, typ: ast.expr) -> ast.expr:
    type_name = typ.id if isinstance(typ, ast.Name) else ast.unparse(typ)
    return ast.Call(func=ast.Name(id=type_name, ctx=ast.Load()), args=[expr], keywords=[])


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


def _apply_remove_annotation(node: AST) -> None:
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


def _apply_rewrite_param_binding(node: AST) -> None:
    if isinstance(node, ast.arg):
        node.annotation = None
        return
    if isinstance(node, FunctionDef):
        for arg in node.args.args:
            arg.annotation = None
        return
    raise TypeError(f'Unsupported node for rewrite_param_binding: {type(node).__name__}')


def _apply_unwrap_checked_return_value(node: AST) -> None:
    if isinstance(node, ast.Return) and node.value is not None and isinstance(node.value, ast.Call) and node.value.args:
        node.value = node.value.args[0]
        return
    raise TypeError(f'Unsupported node for unwrap_checked_return_value: {type(node).__name__}')


def _apply_unbox(node: AST) -> None:
    # Stub — preserved from prior behavior. Real unwrapping happens in post-processing.
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'box' and len(node.args) == 1:
        return
    raise TypeError(f'Unsupported node for unbox_wrap: {type(node).__name__}')


def _apply_wrap_like(node: AST, nodes: dict[int, AST], make_expr) -> None:
    if isinstance(node, ast.AnnAssign):
        if node.value is not None:
            node.value = make_expr(node.value)
        return
    if isinstance(node, ast.Return):
        if node.value is not None:
            node.value = make_expr(node.value)
        return
    if isinstance(node, ast.Assign):
        node.value = make_expr(node.value)
        return
    if isinstance(node, ast.expr):
        replacement = make_expr(node)
        ast.copy_location(replacement, node)
        root = nodes.get(0)
        if root is not None:
            _SpecificNodeReplacer(id(node), replacement).visit(root)
            return
        raise TypeError('wrap expression requires root node 0')
    raise TypeError(f'Unsupported node for wrap: {type(node).__name__}')


def apply_intent(intent: Intent, nodes: dict[int, AST], node_types: dict[int, str | None] | None = None) -> None:
    kind = intent.kind
    loc = intent.location_id
    node = nodes[loc]

    if kind == 'remove_annotation':
        _apply_remove_annotation(node)
        return
    if kind == 'rewrite_param_binding':
        _apply_rewrite_param_binding(node)
        return
    if kind == 'unwrap_checked_return_value':
        _apply_unwrap_checked_return_value(node)
        return
    if kind == 'unbox_wrap':
        _apply_unbox(node)
        return

    # Prefer the type carried on the intent (annotation-derived, always present
    # for typed sites). Fall back to the per-node pyright table if the intent
    # has none (e.g. when consumed from older bundles).
    typ_src = getattr(intent, 'typ_src', None)
    if typ_src is None and node_types is not None:
        typ_src = node_types.get(loc)
    typ = _parse_typ(typ_src)

    if kind == 'box_wrap':
        _apply_wrap_like(node, nodes, lambda e: _box_expr(e))
        return
    if kind == 'cast_wrap':
        if typ is None:
            _apply_wrap_like(node, nodes, lambda e: _box_expr(e))
        elif classify_type(typ) not in _VALID_CAST_KINDS:
            # typ_src like '(int, int)' from a tuple-of-types annotation -- not a valid cast target.
            # Match the pre-sqlite behavior: leave the expression unchanged.
            return
        else:
            _apply_wrap_like(node, nodes, lambda e: _cast_expr(e, typ))
        return
    if kind == 'constructor_wrap':
        if typ is None:
            _apply_wrap_like(node, nodes, lambda e: _box_expr(e))
        else:
            _apply_wrap_like(node, nodes, lambda e: _constructor_expr(e, typ))
        return
    if kind == 'primitive_wrap':
        if typ is None:
            _apply_wrap_like(node, nodes, lambda e: _box_expr(e))
        else:
            _apply_wrap_like(node, nodes, lambda e: _primitive_expr(e, typ))
        return
    if kind == 'cast_wrap_then_box':
        if typ is None:
            _apply_wrap_like(node, nodes, lambda e: _box_expr(e))
        elif classify_type(typ) not in _VALID_CAST_KINDS:
            return
        else:
            _apply_wrap_like(node, nodes, lambda e: _box_expr(_cast_expr(e, typ)))
        return
    if kind == 'constructor_wrap_then_box':
        if typ is None:
            _apply_wrap_like(node, nodes, lambda e: _box_expr(e))
        else:
            _apply_wrap_like(node, nodes, lambda e: _box_expr(_constructor_expr(e, typ)))
        return
    if kind == 'primitive_wrap_then_box':
        if typ is None:
            _apply_wrap_like(node, nodes, lambda e: _box_expr(e))
        else:
            _apply_wrap_like(node, nodes, lambda e: _box_expr(_primitive_expr(e, typ)))
        return
    raise ValueError(f'Unknown intent kind: {kind}')
