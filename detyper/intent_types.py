"""Minimal intent data types and JSON shape."""

from __future__ import annotations

from ast import AST
from dataclasses import dataclass
from typing import Literal


IntentKind = Literal[
    'remove_annotation',
    'rewrite_param_binding',
    'unwrap_checked_return_value',
    'cast_wrap',
    'constructor_wrap',
    'primitive_wrap',
    'box_wrap',
    'unbox_wrap',
    'cast_wrap_then_box',
    'constructor_wrap_then_box',
    'primitive_wrap_then_box',
]

Affinity = Literal['producer', 'consumer']


def node_id(node: AST) -> int:
    return getattr(node, 'detyping_id', id(node))


@dataclass
class Intent:
    kind: IntentKind
    location_id: int
    affinity: Affinity | None = None
    typ_src: str | None = None
    nonnull_typ_src: str | None = None

    def node_collision_key(self) -> int:
        return self.location_id

    @property
    def sort_key(self) -> tuple[int, str]:
        return (self.location_id, self.affinity or '')

    def clone(self) -> 'Intent':
        return Intent(self.kind, self.location_id, self.affinity, self.typ_src, self.nonnull_typ_src)


def intent_to_json(intent: Intent) -> dict:
    return {
        'kind': intent.kind,
        'location_id': intent.location_id,
        'affinity': intent.affinity,
        'typ_src': intent.typ_src,
        'nonnull_typ_src': intent.nonnull_typ_src,
    }


def intent_from_json(data: dict) -> Intent:
    return Intent(
        kind=data['kind'],
        location_id=data['location_id'],
        affinity=data.get('affinity'),
        typ_src=data.get('typ_src'),
        nonnull_typ_src=data.get('nonnull_typ_src'),
    )
