"""Dumb intent collection and execution ordering."""

from __future__ import annotations

from ast import AST

from .intent_impls import apply_intent
from .intent_types import Intent


def _affinity_rank(intent: Intent) -> int:
    if intent.affinity == 'consumer':
        return 0
    if intent.affinity == 'producer':
        return 2
    return 1


def _merge_wrap_intents(intents: list[Intent]) -> list[Intent]:
    grouped: dict[int, list[Intent]] = {}
    others: list[Intent] = []
    for intent in intents:
        if intent.kind == 'wrap':
            grouped.setdefault(intent.node_collision_key(), []).append(intent)
        else:
            others.append(intent)

    merged = list(others)
    for group in grouped.values():
        if len(group) == 1:
            merged.append(group[0].clone())
            continue
        base = sorted(group, key=lambda intent: intent.sort_key)[0].clone()
        # Minimal intent shape has only one type slot, so keep the outermost non-box type.
        ordered = sorted(group, key=lambda item: (_affinity_rank(item), item.sort_key))
        for intent in ordered:
            if intent.typ is not None:
                base.typ = intent.typ
            if intent.nonnull_typ is not None:
                base.nonnull_typ = intent.nonnull_typ
        base.affinity = None
        merged.append(base)
    return merged


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
        return sorted(_merge_wrap_intents(self._intents), key=lambda intent: intent.sort_key)

    def execute(self, nodes: dict[int, AST]) -> None:
        for intent in self._sorted():
            apply_intent(intent, nodes)
