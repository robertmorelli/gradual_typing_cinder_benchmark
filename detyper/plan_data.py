"""PlanData, FuncInfo, type resolution, and AST visitors."""

import ast
from ast import AST, FunctionDef, Call
from typing import NamedTuple

from .policy import resolve_annotation, classify_type

TypeSpec = ast.expr  # alias for clarity


class FuncInfo(NamedTuple):
    fun_name: str
    param_types: list  # list[TypeSpec | None]
    return_type: TypeSpec | None
    is_detyped: bool


class PlanData:
    def __init__(self, funcs: dict):
        self.funcs: dict[str, FuncInfo] = funcs  # fun_name -> FuncInfo


def _annotations_equal(a: TypeSpec, b: TypeSpec) -> bool:
    return ast.dump(a) == ast.dump(b)


def build_plan_data(defs: list, guide: dict) -> PlanData:
    """Build PlanData from function defs and a permutation guide.

    guide: dict[str, bool] — fun_name -> is_detyped
    On arity or annotation conflict (e.g. same method name in different classes),
    the function is marked is_detyped=False (skip detyping rather than crash).
    """
    grouped: dict[str, list] = {}
    for fdef in defs:
        name = fdef.name
        grouped.setdefault(name, []).append(fdef)

    funcs: dict[str, FuncInfo] = {}
    for name, fdefs in grouped.items():
        base = fdefs[0]
        base_params = base.args.args
        n = len(base_params)

        param_types: list = [
            resolve_annotation(a.annotation if a.annotation else None)
            for a in base_params
        ]
        return_type: TypeSpec | None = resolve_annotation(base.returns)
        param_locked = [False] * n   # True once a conflict forces slot to None
        return_locked = False        # True once a conflict forces return_type to None

        for fdef in fdefs[1:]:
            fargs = fdef.args.args
            if len(fargs) != n:
                # Arity mismatch — clear everything; call-site wrapping is unsafe
                param_types = [None] * n
                return_type = None
                break
            for i, (merged, new_arg) in enumerate(zip(param_types, fargs)):
                if param_locked[i]:
                    continue
                new_ann = resolve_annotation(new_arg.annotation if new_arg.annotation else None)
                if merged is None:
                    param_types[i] = new_ann
                elif new_ann is not None:
                    if not _annotations_equal(merged, new_ann):
                        param_types[i] = None   # conflict — strip, skip wrapping
                        param_locked[i] = True
            new_ret = resolve_annotation(fdef.returns)
            if return_locked:
                pass
            elif return_type is None:
                return_type = new_ret
            elif new_ret is not None:
                if not _annotations_equal(return_type, new_ret):
                    return_type = None          # conflict — strip, skip wrapping
                    return_locked = True

        has_inline = any(
            (isinstance(d, ast.Name) and d.id == 'inline') or
            (isinstance(d, ast.Attribute) and d.attr == 'inline')
            for fdef in fdefs
            for d in fdef.decorator_list
        )
        is_detyped = (not has_inline) and guide.get(name, False)
        funcs[name] = FuncInfo(
            fun_name=name,
            param_types=param_types,
            return_type=return_type,
            is_detyped=is_detyped,
        )

    return PlanData(funcs)


# ── AST Visitors ────────────────────────────────────────────────────────────

class _FuncDefCollector(ast.NodeVisitor):
    def __init__(self):
        self.result: list[FunctionDef] = []

    def visit_FunctionDef(self, node: FunctionDef):
        self.result.append(node)
        self.generic_visit(node)

    visit_AsyncFunctionDef = visit_FunctionDef


def all_function_defs(tree: AST) -> list:
    v = _FuncDefCollector()
    v.visit(tree)
    return v.result


class _FuncUseCollector(ast.NodeVisitor):
    """Collect free function call sites (Call.func is Name)."""

    def __init__(self, plan_names: set):
        self.plan_names = plan_names
        self.result: list[tuple] = []
        self._current_func: FunctionDef | None = None

    def visit_FunctionDef(self, node: FunctionDef):
        old = self._current_func
        self._current_func = node
        self.generic_visit(node)
        self._current_func = old

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_Call(self, node: Call):
        if (
            isinstance(node.func, ast.Name)
            and node.func.id in self.plan_names
            and self._current_func is not None
        ):
            self.result.append((node, self._current_func))
        self.generic_visit(node)


def all_function_uses(tree: AST, plan_names: set) -> list:
    """Returns list of (call_node, containing_functiondef) for free function calls."""
    v = _FuncUseCollector(plan_names)
    v.visit(tree)
    return v.result


class _MethodUseCollector(ast.NodeVisitor):
    """Collect method call sites (Call.func is Attribute)."""

    def __init__(self, plan_names: set):
        self.plan_names = plan_names
        self.result: list[tuple] = []
        self._current_func: FunctionDef | None = None

    def visit_FunctionDef(self, node: FunctionDef):
        old = self._current_func
        self._current_func = node
        self.generic_visit(node)
        self._current_func = old

    visit_AsyncFunctionDef = visit_FunctionDef

    def visit_Call(self, node: Call):
        if (
            isinstance(node.func, ast.Attribute)
            and node.func.attr in self.plan_names
            and self._current_func is not None
        ):
            self.result.append((node, self._current_func))
        self.generic_visit(node)


def all_method_uses(tree: AST, plan_names: set) -> list:
    """Returns list of (call_node, containing_functiondef) for method calls."""
    v = _MethodUseCollector(plan_names)
    v.visit(tree)
    return v.result
