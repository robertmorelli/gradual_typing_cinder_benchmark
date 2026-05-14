"""Dumb intent collection and execution ordering.

Annihilation now happens in sqlite_engine. This class is a thin wrapper that
sorts intents by (location_id, affinity) and applies them.
"""

from __future__ import annotations

from ast import AST

from .intent_impls import apply_intent
from .intent_types import Intent


class IntentCollisionError(Exception):
    pass


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
        return sorted(self._intents, key=lambda intent: intent.sort_key)

    def execute(self, nodes: dict[int, AST], node_types: dict[int, str | None] | None = None) -> None:
        for intent in self._sorted():
            apply_intent(intent, nodes, node_types)
