"""Dumb intent collection and execution ordering."""

from __future__ import annotations

from ast import AST

from .intent_impls import apply_intent
from .intent_types import Intent


class IntentCollisionError(Exception):
    pass


_WRAP_KINDS = {'wrap', 'wrap_then_box', 'wrap_constructor', 'wrap_cast'}


def _typ_text(intent: Intent) -> str | None:
    import ast as _ast
    return _ast.unparse(intent.typ) if intent.typ is not None else None


def _annihilate_producer_consumer(intents: list[Intent]) -> list[Intent]:
    """When producer and consumer wraps target the same node with the same type, drop one (keep the consumer)."""
    by_loc: dict[int, dict[str, Intent]] = {}
    for intent in intents:
        if intent.kind not in _WRAP_KINDS or intent.affinity not in ('producer', 'consumer'):
            continue
        slot = by_loc.setdefault(intent.location_id, {})
        slot[intent.affinity] = intent
    dropped: set[int] = set()
    for loc, slots in by_loc.items():
        if 'producer' in slots and 'consumer' in slots:
            if _typ_text(slots['producer']) == _typ_text(slots['consumer']):
                dropped.add(id(slots['producer']))
    return [intent for intent in intents if id(intent) not in dropped]


def _check_no_collisions(intents: list[Intent]) -> None:
    seen: dict[tuple[int, str, str | None], Intent] = {}
    for intent in intents:
        key = (intent.location_id, intent.kind, intent.affinity)
        if key in seen:
            raise IntentCollisionError(
                f'Intent collision: two {intent.kind} intents (affinity={intent.affinity}) '
                f'target location_id={intent.location_id}'
            )
        seen[key] = intent


class IntentSet:
    def __init__(self, intent: Intent | None = None):
        self._intents: list[Intent] = []
        if intent is not None:
            self.add(intent)

    def add(self, intent: Intent) -> None:
        self._intents.append(intent.clone())

    def extend(self, intents: list[Intent]) -> None:
        for intent in intents:
            self.add(intent)

    def merge(self, other: 'IntentSet') -> None:
        for intent in other.intentions():
            self.add(intent)

    def intentions(self) -> list[Intent]:
        return [intent.clone() for intent in self._sorted()]

    def _sorted(self) -> list[Intent]:
        _check_no_collisions(self._intents)
        return sorted(_annihilate_producer_consumer(self._intents), key=lambda intent: intent.sort_key)

    def execute(self, nodes: dict[int, AST]) -> None:
        for intent in self._sorted():
            apply_intent(intent, nodes)
