"""Type classification and explicit annotation-site edit policies.

Each rule answers:
    "For this kind of annotation in this kind of location, what full set of
    edits should happen because of it?"

These edit names are the source of truth for generator behavior. They are
still high-level: generators turn them into concrete RewriteIntention objects.
"""

from __future__ import annotations

import ast
import copy
from dataclasses import dataclass
from typing import Literal

TypeKind = Literal['none', 'builtin', 'primitive', 'checked_list', 'container', 'cast']
EditName = Literal[
    'remove_annotation',
    'rewrite_param_binding',
    'preserve_argument_mutations',
    'wrap_with_runtime_type',
    'box',
    'wrap_later_name_uses',
    'wrap_assigned_expression',
    'unwrap_checked_return_value',
]


@dataclass(frozen=True)
class ParamPolicy:
    """All edits caused by a parameter annotation."""

    definition_edits: tuple[EditName, ...]
    call_edits: tuple[EditName, ...]


@dataclass(frozen=True)
class BodyPolicy:
    """All edits caused by a local/body annotation."""

    annotation_edits: tuple[EditName, ...]


@dataclass(frozen=True)
class ReturnPolicy:
    """All edits caused by a return annotation."""

    definition_edits: tuple[EditName, ...]
    value_edits: tuple[EditName, ...]
    call_edits: tuple[EditName, ...]


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
# Strip annotation but never emit cast/wrap.
UNCASTABLE_NAMES = frozenset({
    'Iterator', 'Generator', 'Iterable', 'AsyncIterator', 'AsyncGenerator',
    'AsyncIterable', 'Sequence', 'MutableSequence', 'Mapping', 'MutableMapping',
    'Set', 'MutableSet', 'Callable', 'Awaitable', 'Coroutine',
})

# Python built-ins where cast() is not valid in Cinder.
BUILTIN_NAMES = frozenset({
    'float', 'int', 'str', 'bool', 'bytes', 'list', 'dict', 'set', 'tuple',
    'object', 'type', 'complex', 'bytearray', 'memoryview', 'range', 'slice',
    'frozenset',
})

TYPING_BUILTIN_NAMES = frozenset({
    'List', 'Dict', 'Set', 'Tuple', 'FrozenSet', 'Type',
})


def resolve_annotation(typ: ast.expr | None) -> ast.expr | None:
    """Resolve forward-reference string literals to Name nodes."""
    if isinstance(typ, ast.Constant) and isinstance(typ.value, str):
        return ast.Name(id=typ.value, ctx=ast.Load())
    return typ


def expand_aliases(typ: ast.expr | None, aliases: dict[str, ast.expr] | None = None) -> ast.expr | None:
    """Expand simple type aliases recursively before classification."""
    if typ is None or not aliases:
        return typ

    typ = resolve_annotation(typ)
    if typ is None:
        return None

    if isinstance(typ, ast.Name) and typ.id in aliases:
        return expand_aliases(copy.deepcopy(aliases[typ.id]), aliases)

    if isinstance(typ, ast.Subscript):
        expanded_value = expand_aliases(typ.value, aliases)
        expanded_slice = expand_aliases(typ.slice, aliases)
        return ast.Subscript(
            value=expanded_value if expanded_value is not None else typ.value,
            slice=expanded_slice if expanded_slice is not None else typ.slice,
            ctx=typ.ctx,
        )

    if isinstance(typ, ast.Tuple):
        return ast.Tuple(
            elts=[expand_aliases(elt, aliases) or elt for elt in typ.elts],
            ctx=typ.ctx,
        )

    if isinstance(typ, ast.BinOp) and isinstance(typ.op, ast.BitOr):
        left = expand_aliases(typ.left, aliases) or typ.left
        right = expand_aliases(typ.right, aliases) or typ.right
        return ast.BinOp(left=left, op=typ.op, right=right)

    return typ


def classify_type(typ: ast.expr | None, aliases: dict[str, ast.expr] | None = None) -> TypeKind:
    """Classify an annotation into a rule type-kind."""
    typ = expand_aliases(typ, aliases)
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
        if typ.id in BUILTIN_NAMES or typ.id in TYPING_BUILTIN_NAMES:
            return 'builtin'
        return 'cast'
    if isinstance(typ, ast.Tuple):
        return 'builtin'
    if isinstance(typ, ast.Subscript):
        val = typ.value
        if isinstance(val, ast.Name):
            if val.id == 'CheckedList':
                return 'checked_list'
            if val.id in BUILTIN_NAMES or val.id in TYPING_BUILTIN_NAMES:
                return 'builtin'
            if val.id in CONTAINER_NAMES:
                return 'container'
            if val.id in UNCASTABLE_NAMES:
                return 'none'
        return 'cast'
    return 'cast'


PARAM_POLICIES: dict[TypeKind, ParamPolicy] = {
    'none': ParamPolicy(
        definition_edits=('remove_annotation',),
        call_edits=(),
    ),
    'builtin': ParamPolicy(
        definition_edits=('remove_annotation',),
        call_edits=(),
    ),
    'primitive': ParamPolicy(
        definition_edits=('rewrite_param_binding',),
        call_edits=('wrap_with_runtime_type', 'box'),
    ),
    'checked_list': ParamPolicy(
        definition_edits=('rewrite_param_binding',),
        call_edits=('preserve_argument_mutations',),
    ),
    'container': ParamPolicy(
        definition_edits=('rewrite_param_binding',),
        call_edits=('wrap_with_runtime_type',),
    ),
    'cast': ParamPolicy(
        definition_edits=('rewrite_param_binding',),
        call_edits=('wrap_with_runtime_type',),
    ),
}


BODY_POLICIES: dict[TypeKind, BodyPolicy] = {
    'none': BodyPolicy(annotation_edits=()),
    'builtin': BodyPolicy(annotation_edits=('remove_annotation',)),
    'primitive': BodyPolicy(annotation_edits=('wrap_assigned_expression',)),
    'checked_list': BodyPolicy(
        annotation_edits=('wrap_later_name_uses', 'remove_annotation', 'wrap_assigned_expression'),
    ),
    'container': BodyPolicy(
        annotation_edits=('wrap_later_name_uses', 'remove_annotation', 'wrap_assigned_expression'),
    ),
    'cast': BodyPolicy(
        annotation_edits=('wrap_later_name_uses', 'remove_annotation', 'wrap_assigned_expression'),
    ),
}


RETURN_POLICIES: dict[TypeKind, ReturnPolicy] = {
    'none': ReturnPolicy(
        definition_edits=('remove_annotation',),
        value_edits=(),
        call_edits=(),
    ),
    'builtin': ReturnPolicy(
        definition_edits=('remove_annotation',),
        value_edits=(),
        call_edits=(),
    ),
    'primitive': ReturnPolicy(
        definition_edits=('remove_annotation',),
        value_edits=('wrap_with_runtime_type', 'box'),
        call_edits=('wrap_with_runtime_type',),
    ),
    'checked_list': ReturnPolicy(
        definition_edits=('remove_annotation',),
        value_edits=('unwrap_checked_return_value',),
        call_edits=('wrap_with_runtime_type',),
    ),
    'container': ReturnPolicy(
        definition_edits=('remove_annotation',),
        value_edits=(),
        call_edits=('wrap_with_runtime_type',),
    ),
    'cast': ReturnPolicy(
        definition_edits=('remove_annotation',),
        value_edits=(),
        call_edits=('wrap_with_runtime_type',),
    ),
}


def param_policy_for(typ: ast.expr | None, aliases: dict[str, ast.expr] | None = None) -> ParamPolicy:
    """Return the full policy caused by a parameter annotation."""
    return PARAM_POLICIES[classify_type(typ, aliases)]


def body_policy_for(typ: ast.expr | None, aliases: dict[str, ast.expr] | None = None) -> BodyPolicy:
    """Return the full policy caused by a body annotation."""
    return BODY_POLICIES[classify_type(typ, aliases)]


def return_policy_for(typ: ast.expr | None, aliases: dict[str, ast.expr] | None = None) -> ReturnPolicy:
    """Return the full policy caused by a return annotation."""
    return RETURN_POLICIES[classify_type(typ, aliases)]
