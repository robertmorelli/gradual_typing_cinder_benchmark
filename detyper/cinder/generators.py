"""Policy-to-rewrite helpers for the Cinder backend."""

from __future__ import annotations

from .rules import EditName
from .tasks import Arg


def wrap_args_for(actions: tuple[EditName, ...], typ: str | None) -> list[Arg]:
    wrap_args: list[Arg] = []
    if 'wrap_with_runtime_type' in actions:
        wrap_args.append(Arg(None, typ, wrap_order=0))
    if 'box' in actions:
        wrap_args.append(Arg(None, None, wrap_order=1))
    return wrap_args
