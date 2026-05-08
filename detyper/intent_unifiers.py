"""Canonical intent combine rules."""

from __future__ import annotations

import ast
from ast import AST

from .intent_impls import apply_intent
from .intent_types import Arg, Intent, IntentionKey, NodeCollisionKey


def _arg_marker(intent: Intent, arg: Arg) -> tuple:
    typ_key = ast.dump(arg.typ) if arg.typ is not None else 'None'
    if intent.kind == 'wrap':
        return (arg.index, typ_key, arg.wrap_order)
    return (arg.index, typ_key)


def merge_intents_of_same_kind(existing: Intent, incoming: Intent) -> Intent:
    assert existing.kind == incoming.kind
    assert existing.key() == incoming.key()

    merged = list(existing.args) + list(incoming.args)
    seen: set[tuple] = set()
    deduped: list[Arg] = []
    for arg in merged:
        marker = _arg_marker(existing, arg)
        if marker in seen:
            continue
        seen.add(marker)
        deduped.append(arg)
    existing.args = deduped
    return existing


def resolve_same_node_intents(intents: list[Intent]) -> list[Intent]:
    canonical_by_kind: dict[IntentionKey, Intent] = {}
    for intent in intents:
        key = intent.key()
        existing = canonical_by_kind.get(key)
        if existing is None:
            canonical_by_kind[key] = intent
        else:
            canonical_by_kind[key] = merge_intents_of_same_kind(existing, intent)
    return sorted(canonical_by_kind.values(), key=lambda intent: intent.sort_key)


class IntentSet:
    """Intent algebra keyed by location/context/kind."""

    def __init__(self, intent: Intent | None = None):
        self._by_kind: dict[IntentionKey, Intent] = {}
        if intent is not None:
            self.add(intent)

    def add(self, intent: Intent) -> None:
        key = intent.key()
        existing = self._by_kind.get(key)
        if existing is None:
            self._by_kind[key] = intent.clone()
        else:
            self._by_kind[key] = merge_intents_of_same_kind(existing, intent)

    def extend(self, intents: list[Intent]) -> None:
        for intent in intents:
            self.add(intent)

    def merge(self, other: 'IntentSet') -> None:
        for intent in other.intentions():
            self.add(intent)

    def intentions(self) -> list[Intent]:
        return [intent.clone() for intent in self._sorted()]

    def _sorted(self) -> list[Intent]:
        by_node: dict[NodeCollisionKey, list[Intent]] = {}
        for intent in self._by_kind.values():
            by_node.setdefault(intent.node_collision_key(), []).append(intent.clone())

        canonicalized: list[Intent] = []
        for same_node_intents in by_node.values():
            canonicalized.extend(resolve_same_node_intents(same_node_intents))

        return sorted(canonicalized, key=lambda intent: intent.sort_key)

    def execute(self, nodes: dict[int, AST]) -> None:
        for intent in self._sorted():
            apply_intent(intent, nodes)
