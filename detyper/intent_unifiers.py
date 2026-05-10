"""Slot-based intent execution rules."""

from __future__ import annotations

from ast import AST

from .intent_impls import apply_intent
from .intent_types import Intent
from .kind_context_policy import annihilates


def _annihilation_slot(intent: Intent) -> tuple[str, str] | None:
    if not intent.smoothing or intent.affinity not in {'producer', 'consumer'}:
        return None
    return (intent.slot_key or str(intent.location_id), intent.affinity)


def _intent_debug(intent: Intent) -> str:
    return f'kind={intent.kind} loc={intent.location_id} ctx={intent.context_id} affinity={intent.affinity} place={intent.policy_place} action={intent.policy_action} slot={intent.slot_key}'


def _place_in_slots(intents: list[Intent]) -> dict[str, dict[str, Intent]]:
    slots: dict[str, dict[str, Intent]] = {}
    for intent in intents:
        slot = _annihilation_slot(intent)
        if slot is None:
            continue
        slot_key, affinity = slot
        sides = slots.setdefault(slot_key, {})
        existing = sides.get(affinity)
        if existing is not None:
            raise ValueError(
                f'duplicate intents in same node slot {(slot_key, affinity)}: '
                f'{_intent_debug(existing)}; {_intent_debug(intent)}'
            )
        sides[affinity] = intent
    return slots


def mark_symmetric_execution(intents: list[Intent]) -> list[Intent]:
    marked = [intent.clone() for intent in intents]
    for intent in marked:
        intent.should_execute = True

    slots = _place_in_slots(marked)
    for sides in slots.values():
        producer = sides.get('producer')
        consumer = sides.get('consumer')
        if producer is not None and consumer is not None and annihilates(producer.policy_place, producer.policy_action, consumer.policy_place, consumer.policy_action):
            producer.should_execute = False
            consumer.should_execute = False

    by_all: dict[str, list[Intent]] = {}
    for intent in marked:
        if intent.smoothing and intent.all_symmetric_key:
            by_all.setdefault(intent.all_symmetric_key, []).append(intent)
    for grouped in by_all.values():
        total = grouped[0].all_symmetric_total
        affinities = {intent.affinity for intent in grouped}
        if total is not None and len(grouped) >= total and {'producer', 'consumer'} <= affinities:
            for intent in grouped:
                intent.should_execute = False

    return marked


# Backcompat name for existing debug scripts.
def annihilate_smoothing_intents(intents: list[Intent]) -> list[Intent]:
    return [intent for intent in mark_symmetric_execution(intents) if intent.should_execute]


class IntentSet:
    """A bag of intents routed through explicit producer/consumer slots."""

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
        marked = mark_symmetric_execution(self._intents)
        executable = [intent for intent in marked if intent.should_execute]
        return sorted(executable, key=lambda intent: intent.sort_key)

    def execute(self, nodes: dict[int, AST]) -> None:
        for intent in self._sorted():
            apply_intent(intent, nodes)
