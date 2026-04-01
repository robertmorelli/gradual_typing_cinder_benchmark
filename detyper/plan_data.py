"""PlanData and function-level annotation merging."""

from dataclasses import dataclass
import ast
from ast import FunctionDef

from .rules import resolve_annotation

TypeSpec = ast.expr  # alias for clarity


@dataclass(frozen=True)
class FuncInfo:
    fun_name: str
    param_types: list[TypeSpec | None]
    return_type: TypeSpec | None
    is_detyped: bool


@dataclass(frozen=True)
class PlanData:
    funcs: dict[str, FuncInfo]


def _annotations_equal(a: TypeSpec, b: TypeSpec) -> bool:
    return ast.dump(a) == ast.dump(b)


def _optional_member(typ: TypeSpec | None) -> TypeSpec | None:
    if typ is None:
        return None
    if isinstance(typ, ast.Subscript) and isinstance(typ.value, ast.Name) and typ.value.id == 'Optional':
        return typ.slice
    if (
        isinstance(typ, ast.BinOp)
        and isinstance(typ.op, ast.BitOr)
        and isinstance(typ.right, ast.Constant)
        and typ.right.value is None
    ):
        return typ.left
    if (
        isinstance(typ, ast.BinOp)
        and isinstance(typ.op, ast.BitOr)
        and isinstance(typ.left, ast.Constant)
        and typ.left.value is None
    ):
        return typ.right
    return None


def _merge_annotations(a: TypeSpec | None, b: TypeSpec | None) -> TypeSpec | None | object:
    """Tiny ad-hoc unifier for benchmark examples.

    Supported special case:
    - T with Optional[T]
    - T with T | None

    In that case we keep the optional form, since it is the less specific type.
    Returns _CONFLICT when the two annotations still do not unify.
    """
    if a is None:
        return b
    if b is None:
        return a
    if _annotations_equal(a, b):
        return a

    a_inner = _optional_member(a)
    if a_inner is not None and _annotations_equal(a_inner, b):
        return a

    b_inner = _optional_member(b)
    if b_inner is not None and _annotations_equal(a, b_inner):
        return b

    return _CONFLICT


_CONFLICT = object()


def build_plan_data(defs: list, guide: dict) -> PlanData:
    """Build PlanData from function defs and a permutation guide.

    guide: dict[str, bool] — fun_name -> is_detyped
    On arity or annotation conflict (for example, same method name in different
    classes), the conflicting annotation slots are cleared to None so wrapping
    can be skipped safely without discarding the whole function.
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
                merged_ann = _merge_annotations(merged, new_ann)
                if merged_ann is _CONFLICT:
                    param_types[i] = None
                    param_locked[i] = True
                else:
                    param_types[i] = merged_ann
            new_ret = resolve_annotation(fdef.returns)
            if return_locked:
                pass
            else:
                merged_ret = _merge_annotations(return_type, new_ret)
                if merged_ret is _CONFLICT:
                    return_type = None
                    return_locked = True
                else:
                    return_type = merged_ret

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
