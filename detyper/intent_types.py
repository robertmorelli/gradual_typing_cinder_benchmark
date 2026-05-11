"""Minimal intent data types and JSON shape."""

from __future__ import annotations

import ast
from ast import AST
from dataclasses import dataclass
from typing import Literal


IntentKind = Literal[
    'remove_annotation',
    'rewrite_param_binding',
    'unwrap_checked_return_value',
    'wrap',
    'unwrap_box',
]

Affinity = Literal['producer', 'consumer']

INTENT_EXECUTION_ORDER: list[IntentKind] = [
    'remove_annotation',
    'rewrite_param_binding',
    'unwrap_checked_return_value',
    'wrap',
    'unwrap_box',
]


def node_id(node: AST) -> int:
    return getattr(node, 'detyping_id', id(node))


def precedence_index(intent_kind: IntentKind) -> int:
    if intent_kind in INTENT_EXECUTION_ORDER:
        return INTENT_EXECUTION_ORDER.index(intent_kind)
    return len(INTENT_EXECUTION_ORDER)


@dataclass
class Intent:
    kind: IntentKind
    location_id: int
    affinity: Affinity | None = None
    typ: ast.expr | None = None
    nonnull_typ: ast.expr | None = None

    def node_collision_key(self) -> int:
        return self.location_id

    @property
    def sort_key(self) -> tuple[int, int]:
        return (self.location_id, precedence_index(self.kind))

    def clone(self) -> 'Intent':
        return Intent(self.kind, self.location_id, self.affinity, self.typ, self.nonnull_typ)


def make_intent(kind: IntentKind, location: AST, typ: ast.expr | None = None, nonnull_typ: ast.expr | None = None, affinity: Affinity | None = None) -> Intent:
    return Intent(kind=kind, location_id=node_id(location), affinity=affinity, typ=typ, nonnull_typ=nonnull_typ)


def make_remove_annotation_intent(location: AST) -> Intent:
    return make_intent('remove_annotation', location)


def make_rewrite_param_binding_intent(location: AST, typ: ast.expr | None = None) -> Intent:
    return make_intent('rewrite_param_binding', location, typ=typ)


def make_unwrap_checked_return_value_intent(location: AST) -> Intent:
    return make_intent('unwrap_checked_return_value', location)


def make_wrap_intent(location: AST, typ: ast.expr | None = None, nonnull_typ: ast.expr | None = None, affinity: Affinity | None = None) -> Intent:
    return make_intent('wrap', location, typ=typ, nonnull_typ=nonnull_typ, affinity=affinity)


def make_unwrap_box_intent(location: AST) -> Intent:
    return make_intent('unwrap_box', location)


def typ_to_json(typ: ast.expr | None) -> str | None:
    return ast.unparse(typ) if typ is not None else None


def typ_from_json(text: str | None) -> ast.expr | None:
    return ast.parse(text, mode='eval').body if text is not None else None


def intent_to_json(intent: Intent) -> dict:
    return {
        'kind': intent.kind,
        'location_id': intent.location_id,
        'affinity': intent.affinity,
        'typ': typ_to_json(intent.typ),
        'nonnull_typ': typ_to_json(intent.nonnull_typ),
    }


def intent_from_json(data: dict) -> Intent:
    return Intent(
        kind=data['kind'],
        location_id=data['location_id'],
        affinity=data.get('affinity'),
        typ=typ_from_json(data.get('typ')),
        nonnull_typ=typ_from_json(data.get('nonnull_typ')),
    )
