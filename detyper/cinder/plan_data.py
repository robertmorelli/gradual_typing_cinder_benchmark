"""PlanData and string-based function annotation unification for Cinder."""

from __future__ import annotations

from dataclasses import dataclass

from .ast_utils import FunctionDefInfo
from .rules import resolve_annotation_text

TypeSpec = str


@dataclass(frozen=True)
class FuncInfo:
    fun_name: str
    param_types: list[TypeSpec | None]
    return_type: TypeSpec | None
    is_detyped: bool


@dataclass(frozen=True)
class PlanData:
    funcs: dict[str, FuncInfo]


def _compact(text: str) -> str:
    return ''.join(text.split())


def _annotations_equal(a: TypeSpec, b: TypeSpec) -> bool:
    return _compact(a) == _compact(b)


def _split_top_level_union(text: str) -> list[str]:
    parts: list[str] = []
    current: list[str] = []
    depth = 0
    for char in text:
        if char in '([{':
            depth += 1
        elif char in ')]}':
            depth = max(0, depth - 1)
        if char == '|' and depth == 0:
            parts.append(''.join(current).strip())
            current = []
            continue
        current.append(char)
    if current:
        parts.append(''.join(current).strip())
    return [part for part in parts if part]


def _optional_member(typ: TypeSpec | None) -> TypeSpec | None:
    if typ is None:
        return None

    compact = _compact(typ)
    if compact.startswith('Optional[') and compact.endswith(']'):
        return typ.strip()[len('Optional['):-1].strip()

    parts = _split_top_level_union(typ)
    if len(parts) == 2 and 'None' in parts:
        return next(part for part in parts if part != 'None')

    return None


def _merge_annotations(a: TypeSpec | None, b: TypeSpec | None) -> TypeSpec | None | object:
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


def build_plan_data(defs: list[FunctionDefInfo], guide: dict[str, bool]) -> PlanData:
    grouped: dict[str, list[FunctionDefInfo]] = {}
    for info in defs:
        grouped.setdefault(info.name, []).append(info)

    funcs: dict[str, FuncInfo] = {}
    for name, infos in grouped.items():
        base = infos[0]
        n = len(base.regular_params)

        param_types: list[TypeSpec | None] = [
            resolve_annotation_text(param.annotation)
            for param in base.regular_params
        ]
        return_type: TypeSpec | None = resolve_annotation_text(base.return_annotation)
        param_locked = [False] * n
        return_locked = False

        for info in infos[1:]:
            if len(info.regular_params) != n:
                param_types = [None] * n
                return_type = None
                break

            for index, (merged, param) in enumerate(zip(param_types, info.regular_params)):
                if param_locked[index]:
                    continue
                new_ann = resolve_annotation_text(param.annotation)
                merged_ann = _merge_annotations(merged, new_ann)
                if merged_ann is _CONFLICT:
                    param_types[index] = None
                    param_locked[index] = True
                else:
                    param_types[index] = merged_ann

            if not return_locked:
                merged_ret = _merge_annotations(return_type, resolve_annotation_text(info.return_annotation))
                if merged_ret is _CONFLICT:
                    return_type = None
                    return_locked = True
                else:
                    return_type = merged_ret

        funcs[name] = FuncInfo(
            fun_name=name,
            param_types=param_types,
            return_type=return_type,
            is_detyped=(not any(info.is_inline for info in infos)) and guide.get(name, False),
        )

    return PlanData(funcs)
