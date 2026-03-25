"""Declarative policy for type categorization and intention selection."""

from __future__ import annotations

import ast
from typing import Literal

TypeKind = Literal['none', 'primitive', 'checked_list', 'container', 'cast']


# Primitive numeric types in Static Python / Cinder.
PRIMITIVE_NAMES = frozenset({
    'int64', 'int32', 'int16', 'int8',
    'uint64', 'uint32', 'uint16', 'uint8',
    'float64', 'float32',
    'double', 'cbool',
})

# Container passthrough types (generic, treated with cast, but NOT CheckedList).
CONTAINER_NAMES = frozenset({
    'Array', 'Vector',
})

# Generic types that cannot be cast at runtime (generators, iterators, etc.)
# — strip annotation but never emit cast/wrap.
UNCASTABLE_NAMES = frozenset({
    'Iterator', 'Generator', 'Iterable', 'AsyncIterator', 'AsyncGenerator',
    'AsyncIterable', 'Sequence', 'MutableSequence', 'Mapping', 'MutableMapping',
    'Set', 'MutableSet', 'Callable', 'Awaitable', 'Coroutine',
})

# Python built-ins where cast() is not valid in Cinder — strip annotation only.
BUILTIN_NAMES = frozenset({
    'float', 'int', 'str', 'bool', 'bytes', 'list', 'dict', 'set', 'tuple', 'object', 'type',
    'complex', 'bytearray', 'memoryview', 'range', 'slice', 'frozenset',
})


def resolve_annotation(typ: ast.expr | None) -> ast.expr | None:
    """Resolve forward-reference string literals to Name nodes."""
    if isinstance(typ, ast.Constant) and isinstance(typ.value, str):
        return ast.Name(id=typ.value, ctx=ast.Load())
    return typ


def classify_type(typ: ast.expr | None) -> TypeKind:
    """Classify an annotation into a policy type-kind."""
    if typ is None:
        return 'none'
    if isinstance(typ, ast.Constant) and typ.value is None:
        return 'none'
    if isinstance(typ, ast.Constant) and isinstance(typ.value, str):
        return classify_type(ast.Name(id=typ.value, ctx=ast.Load()))
    if isinstance(typ, ast.Name):
        if typ.id == 'None':
            return 'none'
        if typ.id in PRIMITIVE_NAMES:
            return 'primitive'
        if typ.id in BUILTIN_NAMES:
            return 'none'
        return 'cast'
    if isinstance(typ, ast.Tuple):
        return 'none'
    if isinstance(typ, ast.Subscript):
        val = typ.value
        if isinstance(val, ast.Name):
            if val.id == 'CheckedList':
                return 'checked_list'
            if val.id in BUILTIN_NAMES:
                return 'none'
            if val.id in CONTAINER_NAMES:
                return 'container'
            if val.id in UNCASTABLE_NAMES:
                return 'none'
        return 'cast'
    return 'cast'


# Intention policies by scope + type-kind. This is the source of truth used by generators.
# Action names are interpreted by generator logic.
PARAM_ACTIONS_BY_KIND: dict[TypeKind, tuple[str, ...]] = {
    'none': ('remove_annotation',),
    'primitive': ('repro_param', 'wrap_arg_primitive'),
    'checked_list': ('repro_param', 'anti_alias'),
    'container': ('repro_param', 'wrap_arg_cast'),
    'cast': ('repro_param', 'wrap_arg_cast'),
}

BODY_ACTIONS_BY_KIND: dict[TypeKind, tuple[str, ...]] = {
    'none': (),
    'primitive': ('wrap_ann_assign_value',),
    'checked_list': ('remove_body_annotation', 'wrap_ann_assign_value'),
    'container': ('remove_body_annotation', 'wrap_ann_assign_value'),
    'cast': ('remove_body_annotation', 'wrap_ann_assign_value'),
}

RETURN_ACTIONS_BY_KIND: dict[TypeKind, tuple[str, ...]] = {
    'none': ('remove_return_annotation',),
    'primitive': ('remove_return_annotation', 'wrap_internal_primitive_box', 'wrap_call_primitive'),
    'checked_list': ('remove_return_annotation', 'strip_internal_checked_list', 'wrap_call_checked_list'),
    'container': ('remove_return_annotation', 'wrap_call_cast'),
    'cast': ('remove_return_annotation', 'wrap_call_cast'),
}


def param_actions(kind: TypeKind) -> tuple[str, ...]:
    return PARAM_ACTIONS_BY_KIND[kind]


def body_actions(kind: TypeKind) -> tuple[str, ...]:
    return BODY_ACTIONS_BY_KIND[kind]


def return_actions(kind: TypeKind) -> tuple[str, ...]:
    return RETURN_ACTIONS_BY_KIND[kind]
