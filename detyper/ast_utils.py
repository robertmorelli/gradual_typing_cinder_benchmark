"""AST query and rewrite helpers shared across the detyper pipeline."""

from __future__ import annotations

import ast
from ast import AST, Call, FunctionDef
from typing import Callable



class _FunctionCollector(ast.NodeVisitor):
    def __init__(self):
        self.result: list[FunctionDef] = []

    def visit_FunctionDef(self, node: FunctionDef) -> None:
        self.result.append(node)
        self.generic_visit(node)

    visit_AsyncFunctionDef = visit_FunctionDef


def all_function_defs(tree: AST) -> list[FunctionDef]:
    visitor = _FunctionCollector()
    visitor.visit(tree)
    return visitor.result


def detypable_function_names(source: str) -> list[str]:
    """Return the sorted function names that participate in permutations."""
    tree = ast.parse(source)
    return sorted({
        f.name for f in all_function_defs(tree)
        if not (f.name.startswith('__') and f.name.endswith('__'))
    })


class _CallUseCollector(ast.NodeVisitor):
    """Collect call sites inside functions that match a particular predicate."""

    def __init__(self, matches_call: Callable[[Call], bool]):
        self.matches_call = matches_call
        self.result: list[tuple[ast.Call, FunctionDef]] = []
        self._current_func: FunctionDef | None = None

    def visit_FunctionDef(self, node: FunctionDef) -> None:
        old = self._current_func
        self._current_func = node
        self.generic_visit(node)
        self._current_func = old

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_Call(self, node: Call) -> None:
        if self._current_func is not None and self.matches_call(node):
            self.result.append((node, self._current_func))
        self.generic_visit(node)


def _collect_call_uses(tree: AST, matches_call: Callable[[Call], bool]) -> list[tuple[ast.Call, FunctionDef]]:
    visitor = _CallUseCollector(matches_call)
    visitor.visit(tree)
    return visitor.result


def all_function_uses(tree: AST, plan_names: set[str]) -> list[tuple[ast.Call, FunctionDef]]:
    """Collect free function calls whose callee names are in plan_names."""
    return _collect_call_uses(
        tree,
        lambda node: isinstance(node.func, ast.Name) and node.func.id in plan_names,
    )


def all_method_uses(tree: AST, plan_names: set[str]) -> list[tuple[ast.Call, FunctionDef]]:
    """Collect method calls whose attribute names are in plan_names."""
    return _collect_call_uses(
        tree,
        lambda node: isinstance(node.func, ast.Attribute) and node.func.attr in plan_names,
    )


def _find_nodes_directly_in_function(
    func: FunctionDef,
    target_type: type[AST],
) -> list[AST]:
    """Find nodes in func while skipping nested functions."""
    results: list[AST] = []

    class Visitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node: FunctionDef) -> None:
            if node is func:
                self.generic_visit(node)

        visit_AsyncFunctionDef = visit_FunctionDef

        def generic_visit(self, node: AST) -> None:
            if isinstance(node, target_type):
                results.append(node)
            super().generic_visit(node)

    Visitor().visit(func)
    return results


def find_returns(func: FunctionDef) -> list[ast.Return]:
    return [node for node in _find_nodes_directly_in_function(func, ast.Return) if isinstance(node, ast.Return)]


def find_ann_assigns(func: FunctionDef) -> list[ast.AnnAssign]:
    return [node for node in _find_nodes_directly_in_function(func, ast.AnnAssign) if isinstance(node, ast.AnnAssign)]


def find_name_uses_after(
    func: FunctionDef,
    var_name: str,
    after_stmt: ast.stmt,
) -> list[ast.Name]:
    """All Load uses of var_name in sibling statements after after_stmt."""

    def _stmt_lists(node: ast.AST) -> list[list[ast.stmt]]:
        out: list[list[ast.stmt]] = []
        for _field, value in ast.iter_fields(node):
            if isinstance(value, list) and value and all(isinstance(v, ast.stmt) for v in value):
                out.append(value)
        return out

    def _find_container(stmts: list[ast.stmt]) -> tuple[list[ast.stmt], int] | None:
        for index, stmt in enumerate(stmts):
            if stmt is after_stmt:
                return (stmts, index)
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
    body, index = found

    results: list[ast.Name] = []

    class Visitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node: FunctionDef) -> None:
            return

        visit_AsyncFunctionDef = visit_FunctionDef
        visit_ClassDef = visit_FunctionDef

        def visit_Name(self, node: ast.Name) -> None:
            if node.id == var_name and isinstance(node.ctx, ast.Load):
                results.append(node)

    for stmt in body[index + 1:]:
        Visitor().visit(stmt)

    return results
