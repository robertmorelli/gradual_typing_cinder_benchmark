"""AST query and rewrite helpers shared across the detyper pipeline."""

from __future__ import annotations

import ast
from ast import AST, Call, FunctionDef
from typing import Callable


def node_index(tree: AST) -> dict[int, AST]:
    """Map deterministic node ids to AST nodes."""
    return {node.detyping_id: node for node in ast.walk(tree) if hasattr(node, 'detyping_id')}


def label_tree(tree: AST) -> None:
    """Attach deterministic preorder ids and parent ids to every AST node."""
    next_id = 0

    def visit(node: AST, parent_id: int | None = None) -> None:
        nonlocal next_id
        node.detyping_id = next_id
        node.parent_detyping_id = parent_id
        node.detyping_span = (
            getattr(node, 'lineno', None),
            getattr(node, 'col_offset', None),
            getattr(node, 'end_lineno', None),
            getattr(node, 'end_col_offset', None),
        )
        next_id += 1
        current_id = node.detyping_id
        for child in ast.iter_child_nodes(node):
            visit(child, current_id)

    visit(tree)


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


def detypable_annotation_ids(source: str) -> list[str]:
    """Return deterministic annotation ids that participate in permutations."""
    from .annotation_sites import annotation_sites_from_source

    return [str(site.id) for site in annotation_sites_from_source(source)]


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


def _sibling_stmts_after(
    func: FunctionDef,
    after_stmt: ast.stmt,
) -> list[ast.stmt]:
    """Sibling statements that occur after after_stmt in the same statement list."""

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
    return body[index + 1:]


def find_name_uses_after(
    func: FunctionDef,
    var_name: str,
    after_stmt: ast.stmt,
) -> list[ast.Name]:
    """All Load uses of var_name in sibling statements after after_stmt."""

    results: list[ast.Name] = []

    class Visitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node: FunctionDef) -> None:
            return

        visit_AsyncFunctionDef = visit_FunctionDef
        visit_ClassDef = visit_FunctionDef

        def visit_Name(self, node: ast.Name) -> None:
            if node.id == var_name and isinstance(node.ctx, ast.Load):
                results.append(node)

    for stmt in _sibling_stmts_after(func, after_stmt):
        Visitor().visit(stmt)

    return results


def find_assigns_to_name_after(
    func: FunctionDef,
    var_name: str,
    after_stmt: ast.stmt,
) -> list[ast.Assign]:
    """Plain assignments to var_name in sibling statements after after_stmt."""
    results: list[ast.Assign] = []

    class Visitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node: FunctionDef) -> None:
            return

        visit_AsyncFunctionDef = visit_FunctionDef
        visit_ClassDef = visit_FunctionDef

        def visit_Assign(self, node: ast.Assign) -> None:
            if any(isinstance(target, ast.Name) and target.id == var_name for target in node.targets):
                results.append(node)
            self.generic_visit(node)

    for stmt in _sibling_stmts_after(func, after_stmt):
        Visitor().visit(stmt)

    return results
