"""Type classification and edit policies for the Cinder backend."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

TypeKind = Literal['none', 'primitive', 'checked_list', 'container', 'cast']
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
    definition_edits: tuple[EditName, ...]
    call_edits: tuple[EditName, ...]


@dataclass(frozen=True)
class BodyPolicy:
    annotation_edits: tuple[EditName, ...]


@dataclass(frozen=True)
class ReturnPolicy:
    definition_edits: tuple[EditName, ...]
    value_edits: tuple[EditName, ...]
    call_edits: tuple[EditName, ...]


PRIMITIVE_NAMES = frozenset({
    'int64', 'int32', 'int16', 'int8',
    'uint64', 'uint32', 'uint16', 'uint8',
    'float64', 'float32',
    'double', 'cbool',
})
CONTAINER_NAMES = frozenset({'Array', 'Vector'})
UNCASTABLE_NAMES = frozenset({
    'Iterator', 'Generator', 'Iterable', 'AsyncIterator', 'AsyncGenerator',
    'AsyncIterable', 'Sequence', 'MutableSequence', 'Mapping', 'MutableMapping',
    'Set', 'MutableSet', 'Callable', 'Awaitable', 'Coroutine',
})
BUILTIN_NAMES = frozenset({
    'float', 'int', 'str', 'bool', 'bytes', 'list', 'dict', 'set', 'tuple',
    'object', 'type', 'complex', 'bytearray', 'memoryview', 'range', 'slice',
    'frozenset',
})


def resolve_annotation_text(typ: str | None) -> str | None:
    if typ is None:
        return None
    stripped = typ.strip()
    if len(stripped) >= 2 and stripped[0] == stripped[-1] and stripped[0] in ("'", '"'):
        return stripped[1:-1]
    return stripped


def _base_name(typ: str) -> str:
    text = typ.strip()
    for sep in ('[', '|', '.'):
        if sep in text:
            return text.split(sep, 1)[0]
    return text


def classify_type(typ: str | None) -> TypeKind:
    text = resolve_annotation_text(typ)
    if not text or text == 'None':
        return 'none'
    if text.startswith('(') and text.endswith(')') and ',' in text:
        return 'none'

    base = _base_name(text)
    if base in PRIMITIVE_NAMES:
        return 'primitive'
    if base == 'CheckedList':
        return 'checked_list'
    if base in CONTAINER_NAMES:
        return 'container'
    if base in BUILTIN_NAMES or base in UNCASTABLE_NAMES:
        return 'none'
    return 'cast'


PARAM_POLICIES: dict[TypeKind, ParamPolicy] = {
    'none': ParamPolicy(
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


def param_policy_for(typ: str | None) -> ParamPolicy:
    return PARAM_POLICIES[classify_type(typ)]


def body_policy_for(typ: str | None) -> BodyPolicy:
    return BODY_POLICIES[classify_type(typ)]


def return_policy_for(typ: str | None) -> ReturnPolicy:
    return RETURN_POLICIES[classify_type(typ)]
