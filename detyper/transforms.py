"""AST manipulation helpers."""

import ast
from ast import FunctionDef, Module


def make_wrap_expr(expr: ast.expr, typ: ast.expr) -> ast.expr:
    """Return a new AST node wrapping expr for the given type."""
    from .plan_data import classify_type
    kind = classify_type(typ)
    if kind == 'primitive':
        type_name = typ.id if isinstance(typ, ast.Name) else ast.unparse(typ)
        return ast.Call(
            func=ast.Name(id=type_name, ctx=ast.Load()),
            args=[expr], keywords=[],
        )
    elif kind in ('cast', 'container'):
        return ast.Call(
            func=ast.Name(id='cast', ctx=ast.Load()),
            args=[typ, expr], keywords=[],
        )
    elif kind == 'checked_list':
        return ast.Call(func=typ, args=[expr], keywords=[])
    return expr


def make_box_expr(expr: ast.expr) -> ast.expr:
    return ast.Call(
        func=ast.Name(id='box', ctx=ast.Load()),
        args=[expr], keywords=[],
    )


def find_returns(func: FunctionDef) -> list[ast.Return]:
    """All Return nodes directly in func (not in nested functions)."""
    results: list[ast.Return] = []

    class V(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            if node is func:
                self.generic_visit(node)
        visit_AsyncFunctionDef = visit_FunctionDef

        def visit_Return(self, node):
            results.append(node)

    V().visit(func)
    return results


def find_ann_assigns(func: FunctionDef) -> list[ast.AnnAssign]:
    """All AnnAssign nodes directly in func body (not nested)."""
    results: list[ast.AnnAssign] = []

    class V(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            if node is func:
                self.generic_visit(node)
        visit_AsyncFunctionDef = visit_FunctionDef

        def visit_AnnAssign(self, node):
            results.append(node)

    V().visit(func)
    return results


def find_name_uses_after(
    func: FunctionDef,
    var_name: str,
    after_stmt: ast.stmt,
) -> list[ast.Name]:
    """All Name(id=var_name, ctx=Load) nodes in sibling statements after after_stmt,
    excluding nodes inside nested function/class defs."""

    def _stmt_lists(node: ast.AST) -> list[list[ast.stmt]]:
        out: list[list[ast.stmt]] = []
        for _field, value in ast.iter_fields(node):
            if isinstance(value, list) and value and all(isinstance(v, ast.stmt) for v in value):
                out.append(value)
        return out

    def _find_container(stmts: list[ast.stmt]) -> tuple[list[ast.stmt], int] | None:
        for i, stmt in enumerate(stmts):
            if stmt is after_stmt:
                return (stmts, i)
            if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                continue
            for child_stmts in _stmt_lists(stmt):
                found = _find_container(child_stmts)
                if found is not None:
                    return found
        return None

    found = _find_container(func.body)
    if found is None:
        return []
    body, idx = found
    start = idx + 1

    results: list[ast.Name] = []

    class V(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            pass  # don't descend into nested functions
        visit_AsyncFunctionDef = visit_FunctionDef
        visit_ClassDef = visit_FunctionDef

        def visit_Name(self, node):
            if node.id == var_name and isinstance(node.ctx, ast.Load):
                results.append(node)

    for stmt in body[start:]:
        V().visit(stmt)

    return results
