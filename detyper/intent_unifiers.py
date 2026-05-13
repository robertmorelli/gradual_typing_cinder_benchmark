"""Dumb intent collection and execution ordering."""

from __future__ import annotations

from ast import AST

from .intent_impls import apply_intent
from .intent_types import Intent


class IntentCollisionError(Exception):
    pass


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
        return sorted(self._intents, key=lambda intent: intent.sort_key)

    def execute(self, nodes: dict[int, AST]) -> None:
        for intent in self._sorted():
            apply_intent(intent, nodes)
