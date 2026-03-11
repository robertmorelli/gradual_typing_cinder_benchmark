"""Arg, Strat, StratType subclasses, Detyper."""

import ast
from ast import AST
from typing import NamedTuple

from .plan_data import PlanData


class Arg(NamedTuple):
    index: int | None        # param index, or None for whole-node operations
    typ: ast.expr | None     # None means 'box' (no type, just box())
    wrap_order: int = 0      # lower = inner (applied first within a Wrap strat)


# ── StratType markers ────────────────────────────────────────────────────────

class StratType:
    """Base marker for strategy types. Logic lives in runner._apply_*."""
    pass

class RemoveAnnotation(StratType): pass
class ReproParam(StratType):       pass
class AntiAlias(StratType):        pass
class StripReturn(StratType):      pass   # strips outer CheckedList ctor from Return
class Wrap(StratType):             pass

STRAT_PRECEDENCE: list[type[StratType]] = [
    RemoveAnnotation, ReproParam, AntiAlias, StripReturn, Wrap
]


# ── Strat ────────────────────────────────────────────────────────────────────

class Strat:
    def __init__(self, strat_type: type[StratType], args: list[Arg]):
        self.strat_type = strat_type
        self.args: list[Arg] = list(args)

    def __add__(self, other: 'Strat') -> 'Strat':
        assert self.strat_type is other.strat_type
        merged = list(self.args) + list(other.args)

        if self.strat_type in (RemoveAnnotation, ReproParam, AntiAlias, StripReturn):
            seen: set = set()
            deduped = []
            for a in merged:
                key = (a.index, ast.dump(a.typ) if a.typ is not None else 'None')
                if key not in seen:
                    seen.add(key)
                    deduped.append(a)
            merged = deduped
        elif self.strat_type is Wrap:
            seen = set()
            deduped = []
            for a in merged:
                key = (a.index, ast.dump(a.typ) if a.typ is not None else 'None', a.wrap_order)
                if key not in seen:
                    seen.add(key)
                    deduped.append(a)
            merged = deduped

        return Strat(self.strat_type, merged)


# ── Detyper ──────────────────────────────────────────────────────────────────

class Detyper:
    """Accumulates (location_node, context_node, Strat) entries."""

    def __init__(self):
        self._entries: list[tuple[AST, AST, Strat]] = []

    def add(self, location: AST, context: AST, strat: Strat) -> None:
        for i, (loc, ctx, s) in enumerate(self._entries):
            if (id(loc) == id(location)
                    and id(ctx) == id(context)
                    and s.strat_type is strat.strat_type):
                self._entries[i] = (loc, ctx, s + strat)
                return
        self._entries.append((location, context, strat))

    def __add__(self, other: 'Detyper') -> 'Detyper':
        result = Detyper()
        result._entries = list(self._entries)
        for loc, ctx, strat in other._entries:
            result.add(loc, ctx, strat)
        return result

    def all_tasks(self) -> list[tuple[AST, AST, Strat]]:
        return list(self._entries)
