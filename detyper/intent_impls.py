"""Concrete AST edits for intents."""

from __future__ import annotations

import ast
from ast import AST, FunctionDef

from .intent_types import Arg, Intent
from .rules import classify_type


def make_wrap_expr(expr: ast.expr, typ: ast.expr) -> ast.expr:
    kind = classify_type(typ)
    if kind == 'primitive':
        type_name = typ.id if isinstance(typ, ast.Name) else ast.unparse(typ)
        return ast.Call(func=ast.Name(id=type_name, ctx=ast.Load()), args=[expr], keywords=[])
    if kind in ('cast', 'container'):
        return ast.Call(func=ast.Name(id='cast', ctx=ast.Load()), args=[typ, expr], keywords=[])
    if kind == 'checked_list':
        return ast.Call(func=typ, args=[expr], keywords=[])
    return expr


def make_box_expr(expr: ast.expr) -> ast.expr:
    return ast.Call(func=ast.Name(id='box', ctx=ast.Load()), args=[expr], keywords=[])


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
        for arg in intent.args:
            if arg.index is None:
                node.returns = None
            elif arg.index < len(node.args.args):
                node.args.args[arg.index].annotation = None
        return
    if isinstance(node, ast.arg):
        node.annotation = None
        return
    if isinstance(node, ast.AnnAssign):
        node.annotation = None
        return
    raise TypeError(f'Unsupported node for remove_annotation: {type(node).__name__}')


def _apply_rewrite_param_binding(intent: Intent, nodes: dict[int, AST]) -> None:
    node = nodes[intent.location_id]
    assert isinstance(node, FunctionDef)
    prepend: list[ast.stmt] = []

    for arg in sorted(intent.args, key=lambda item: item.index if item.index is not None else 0):
        idx = arg.index
        typ = arg.typ
        if idx is None or idx >= len(node.args.args) or typ is None:
            continue
        param = node.args.args[idx]
        orig_name = param.arg
        kind = classify_type(typ)

        is_static_container = isinstance(typ, ast.Subscript) and isinstance(typ.value, ast.Name) and typ.value.id in {'Array', 'Vector'}
        if kind == 'checked_list' or is_static_container:
            param.annotation = None
            stmt: ast.stmt = ast.Assign(
                targets=[ast.Name(id=orig_name, ctx=ast.Store())],
                value=ast.Call(func=ast.Name(id='cast', ctx=ast.Load()), args=[typ, ast.Name(id=orig_name, ctx=ast.Load())], keywords=[]),
                lineno=node.lineno,
                col_offset=node.col_offset,
            )
        else:
            new_name = '_' + orig_name
            param.arg = new_name
            param.annotation = None
            src = ast.Name(id=new_name, ctx=ast.Load())
            if kind == 'primitive':
                type_name = typ.id if isinstance(typ, ast.Name) else ast.unparse(typ)
                value: ast.expr = ast.Call(func=ast.Name(id=type_name, ctx=ast.Load()), args=[src], keywords=[])
                if any(arg.typ is None for arg in intent.args if arg.index == idx):
                    value = ast.Call(func=ast.Name(id='box', ctx=ast.Load()), args=[value], keywords=[])
            else:
                value = ast.Call(func=ast.Name(id='cast', ctx=ast.Load()), args=[typ, src], keywords=[])
            stmt = ast.Assign(targets=[ast.Name(id=orig_name, ctx=ast.Store())], value=value, lineno=node.lineno, col_offset=node.col_offset)
        prepend.append(stmt)
    node.body = prepend + node.body


def _apply_preserve_argument_mutations(intent: Intent, nodes: dict[int, AST]) -> None:
    node = nodes[intent.location_id]
    assert isinstance(node, ast.Call)
    context = nodes[intent.context_id]
    assert isinstance(context, ast.Module)
    mod_body = context.body

    insert_idx = 0
    for i, stmt in enumerate(mod_body):
        if isinstance(stmt, (ast.Import, ast.ImportFrom)):
            insert_idx = i + 1

    existing: set[str] = {stmt.name for stmt in mod_body if isinstance(stmt, FunctionDef)}
    callee_name = node.func.id if isinstance(node.func, ast.Name) else node.func.attr if isinstance(node.func, ast.Attribute) else 'unknown'
    sorted_args = sorted(intent.args, key=lambda item: item.index if item.index is not None else -1)
    n_args = len(node.args)
    arg_suffix = '_'.join(f'arg{arg.index}' for arg in sorted_args)
    base = f'_repro_{callee_name}_{arg_suffix}'
    repro_name = base
    suffix = 2
    while repro_name in existing:
        repro_name = f'{base}_{suffix}'
        suffix += 1

    wrapper_params = [ast.arg(arg='f')] + [ast.arg(arg=f'arg{i}') for i in range(n_args)]
    body_stmts: list[ast.stmt] = []
    for arg in sorted_args:
        idx = arg.index
        body_stmts.append(ast.Assign(targets=[ast.Name(id=f'_arg{idx}', ctx=ast.Store())], value=ast.Call(func=arg.typ, args=[ast.Name(id=f'arg{idx}', ctx=ast.Load())], keywords=[]), lineno=0, col_offset=0))

    converted = {arg.index for arg in sorted_args}
    call_args = [ast.Name(id=(f'_arg{i}' if i in converted else f'arg{i}'), ctx=ast.Load()) for i in range(n_args)]
    body_stmts.append(ast.Assign(targets=[ast.Name(id='_out', ctx=ast.Store())], value=ast.Call(func=ast.Name(id='f', ctx=ast.Load()), args=call_args, keywords=[]), lineno=0, col_offset=0))

    for arg in sorted_args:
        idx = arg.index
        # CheckedList[T](arg) may return arg itself when arg is already the
        # right checked-list kind. Do not clear/extend in that case or we erase
        # the very mutations we are trying to preserve.
        body_stmts.append(ast.If(
            test=ast.Compare(
                left=ast.Name(id=f'_arg{idx}', ctx=ast.Load()),
                ops=[ast.IsNot()],
                comparators=[ast.Name(id=f'arg{idx}', ctx=ast.Load())],
            ),
            body=[
                ast.Expr(value=ast.Call(func=ast.Attribute(value=ast.Name(id=f'arg{idx}', ctx=ast.Load()), attr='clear', ctx=ast.Load()), args=[], keywords=[])),
                ast.Expr(value=ast.Call(func=ast.Attribute(value=ast.Name(id=f'arg{idx}', ctx=ast.Load()), attr='extend', ctx=ast.Load()), args=[ast.Name(id=f'_arg{idx}', ctx=ast.Load())], keywords=[])),
            ],
            orelse=[],
        ))
    body_stmts.append(ast.Return(value=ast.Name(id='_out', ctx=ast.Load())))

    wrapper = FunctionDef(
        name=repro_name,
        args=ast.arguments(posonlyargs=[], args=wrapper_params, vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
        body=body_stmts,
        decorator_list=[],
        returns=None,
        lineno=0,
        col_offset=0,
    )
    ast.fix_missing_locations(wrapper)
    mod_body.insert(insert_idx, wrapper)
    callee_expr = node.func
    original_args = list(node.args)
    node.func = ast.Name(id=repro_name, ctx=ast.Load())
    node.args = [callee_expr] + original_args


def _apply_unwrap_checked_return_value(intent: Intent, nodes: dict[int, AST]) -> None:
    node = nodes[intent.location_id]
    assert isinstance(node, ast.Return)
    if node.value is not None and isinstance(node.value, ast.Call) and node.value.args:
        node.value = node.value.args[0]


def _wrap_expr(expr: ast.expr, args: list[Arg]) -> ast.expr:
    wrapped = expr
    for arg in args:
        assert arg.index is None
        wrapped = make_box_expr(wrapped) if arg.typ is None else make_wrap_expr(wrapped, arg.typ)
    return wrapped


def _apply_unwrap_box(intent: Intent, nodes: dict[int, AST]) -> None:
    node = nodes[intent.location_id]
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'box' and len(node.args) == 1:
        _SpecificNodeReplacer(id(node), node.args[0]).visit(nodes[intent.context_id])
        return
    raise TypeError(f'Unsupported node for unwrap_box: {type(node).__name__}')


def _apply_wrap(intent: Intent, nodes: dict[int, AST]) -> None:
    node = nodes[intent.location_id]
    sorted_args = sorted(intent.args, key=lambda arg: arg.wrap_order)
    if isinstance(node, ast.AnnAssign):
        if node.value is not None:
            node.value = _wrap_expr(node.value, sorted_args)
        return
    if isinstance(node, ast.Return):
        if node.value is not None:
            node.value = _wrap_expr(node.value, sorted_args)
        return
    if isinstance(node, ast.Assign):
        node.value = _wrap_expr(node.value, sorted_args)
        return
    if isinstance(node, ast.expr):
        expr: ast.expr = ast.Name(id=node.id, ctx=ast.Load()) if isinstance(node, ast.Name) else node
        expr = _wrap_expr(expr, sorted_args)
        ast.copy_location(expr, node)
        _SpecificNodeReplacer(id(node), expr).visit(nodes[intent.context_id])
        return
    raise TypeError(f'Unsupported node for wrap: {type(node).__name__}')


def apply_intent(intent: Intent, nodes: dict[int, AST]) -> None:
    if intent.kind == 'remove_annotation':
        _apply_remove_annotation(intent, nodes)
        return
    if intent.kind == 'rewrite_param_binding':
        _apply_rewrite_param_binding(intent, nodes)
        return
    if intent.kind == 'preserve_argument_mutations':
        _apply_preserve_argument_mutations(intent, nodes)
        return
    if intent.kind == 'unwrap_checked_return_value':
        _apply_unwrap_checked_return_value(intent, nodes)
        return
    if intent.kind == 'wrap':
        _apply_wrap(intent, nodes)
        return
    if intent.kind == 'unwrap_box':
        _apply_unwrap_box(intent, nodes)
        return
    raise ValueError(f'Unknown intent kind: {intent.kind}')
