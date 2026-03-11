"""PlanData, FuncInfo, type resolution, and AST visitors."""

import ast
from ast import AST, FunctionDef, Call
from typing import NamedTuple

TypeSpec = ast.expr  # alias for clarity

# Primitive numeric types in Static Python / Cinder
_PRIMITIVE_NAMES = frozenset({
    'int64', 'int32', 'int16', 'int8',
    'uint64', 'uint32', 'uint16', 'uint8',
    'float64', 'float32',
    'double', 'cbool',
})

# Container passthrough types (generic, treated with cast, but NOT CheckedList)
_CONTAINER_NAMES = frozenset({
    'Array', 'Vector',
})

# Python built-in types where cast() is not valid in Cinder — strip annotation only
_BUILTIN_NAMES = frozenset({
    'float', 'int', 'str', 'bool', 'bytes', 'list', 'dict', 'set', 'tuple', 'object', 'type',
    'complex', 'bytearray', 'memoryview', 'range', 'slice', 'frozenset',
})


def classify_type(typ: TypeSpec | None) -> str:
    """Return one of: 'none', 'primitive', 'checked_list', 'container', 'cast'."""
    if typ is None:
        return 'none'
    if isinstance(typ, ast.Constant) and typ.value is None:
        return 'none'
    if isinstance(typ, ast.Name):
        if typ.id == 'None':
            return 'none'
        if typ.id in _PRIMITIVE_NAMES:
            return 'primitive'
        if typ.id in _BUILTIN_NAMES:
            return 'none'  # cast() not valid for Python builtins; strip annotation only
        # User-defined class → cast
        return 'cast'
    if isinstance(typ, ast.Tuple):
        return 'none'  # tuple annotations (e.g. (int, int)) not castable in Cinder
    if isinstance(typ, ast.Subscript):
        val = typ.value
        if isinstance(val, ast.Name):
            if val.id == 'CheckedList':
                return 'checked_list'
            if val.id in _CONTAINER_NAMES:
                return 'container'
        return 'cast'
    return 'cast'


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
            a.annotation if a.annotation else None
            for a in base_params
        ]
        return_type: TypeSpec | None = base.returns

        for fdef in fdefs[1:]:
            fargs = fdef.args.args
            if len(fargs) != n:
                # Arity mismatch — clear all param types; call-site wrapping is unsafe
                param_types = [None] * n
                return_type = None
                break
            for i, (merged, new_arg) in enumerate(zip(param_types, fargs)):
                new_ann = new_arg.annotation if new_arg.annotation else None
                if merged is None:
                    param_types[i] = new_ann
                elif new_ann is not None:
                    if not _annotations_equal(merged, new_ann):
                        param_types[i] = None  # conflicting — strip annotation, skip wrapping
            new_ret = fdef.returns
            if return_type is None:
                return_type = new_ret
            elif new_ret is not None:
                if not _annotations_equal(return_type, new_ret):
                    return_type = None  # conflicting — strip annotation, skip wrapping

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
