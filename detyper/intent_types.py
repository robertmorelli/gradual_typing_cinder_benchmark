"""Intent data types and JSON shape."""

from __future__ import annotations

import ast
from ast import AST
from dataclasses import dataclass
from typing import Literal, NamedTuple


class Arg(NamedTuple):
    index: int | None
    typ: ast.expr | None
    wrap_order: int = 0


IntentKind = Literal[
    'remove_annotation',
    'rewrite_param_binding',
    'preserve_argument_mutations',
    'unwrap_checked_return_value',
    'wrap',
    'unwrap_box',
]

IntentionKey = tuple[int, int, IntentKind]
NodeCollisionKey = tuple[int, int]

INTENT_EXECUTION_ORDER: list[IntentKind] = [
    'remove_annotation',
    'rewrite_param_binding',
    'preserve_argument_mutations',
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
    context_id: int
    args: list[Arg]
    func_name: str
    lineno: int = 0
    col_offset: int = 0
    node_kind: str = ''

    def key(self) -> IntentionKey:
        return (self.location_id, self.context_id, self.kind)

    def node_collision_key(self) -> NodeCollisionKey:
        return (self.location_id, self.context_id)

    @property
    def sort_key(self) -> tuple[str, int, int, str, int, int]:
        return (self.func_name, self.lineno, self.col_offset, self.node_kind, self.location_id, precedence_index(self.kind))

    def clone(self) -> 'Intent':
        return Intent(self.kind, self.location_id, self.context_id, list(self.args), self.func_name, self.lineno, self.col_offset, self.node_kind)


def make_intent(kind: IntentKind, location: AST, context: AST, args: list[Arg], func_name: str) -> Intent:
    return Intent(
        kind=kind,
        location_id=node_id(location),
        context_id=node_id(context),
        args=args,
        func_name=func_name,
        lineno=getattr(location, 'lineno', 0) or 0,
        col_offset=getattr(location, 'col_offset', 0) or 0,
        node_kind=location.__class__.__name__,
    )


def make_remove_annotation_intent(location: AST, context: AST, args: list[Arg], func_name: str) -> Intent:
    return make_intent('remove_annotation', location, context, args, func_name)


def make_rewrite_param_binding_intent(location: AST, context: AST, args: list[Arg], func_name: str) -> Intent:
    return make_intent('rewrite_param_binding', location, context, args, func_name)


def make_preserve_argument_mutations_intent(location: AST, context: AST, args: list[Arg], func_name: str) -> Intent:
    return make_intent('preserve_argument_mutations', location, context, args, func_name)


def make_unwrap_checked_return_value_intent(location: AST, context: AST, args: list[Arg], func_name: str) -> Intent:
    return make_intent('unwrap_checked_return_value', location, context, args, func_name)


def make_wrap_intent(location: AST, context: AST, args: list[Arg], func_name: str) -> Intent:
    return make_intent('wrap', location, context, args, func_name)


def make_unwrap_box_intent(location: AST, context: AST, args: list[Arg], func_name: str) -> Intent:
    return make_intent('unwrap_box', location, context, args, func_name)


def typ_to_json(typ: ast.expr | None) -> str | None:
    return ast.unparse(typ) if typ is not None else None


def typ_from_json(text: str | None) -> ast.expr | None:
    return ast.parse(text, mode='eval').body if text is not None else None


def intent_to_json(intent: Intent) -> dict:
    return {
        'kind': intent.kind,
        'location_id': intent.location_id,
        'context_id': intent.context_id,
        'args': [
            {'index': arg.index, 'typ': typ_to_json(arg.typ), 'wrap_order': arg.wrap_order}
            for arg in intent.args
        ],
        'func_name': intent.func_name,
        'lineno': intent.lineno,
        'col_offset': intent.col_offset,
        'node_kind': intent.node_kind,
    }


def intent_from_json(data: dict) -> Intent:
    return Intent(
        kind=data['kind'],
        location_id=data['location_id'],
        context_id=data['context_id'],
        args=[Arg(arg['index'], typ_from_json(arg['typ']), arg.get('wrap_order', 0)) for arg in data['args']],
        func_name=data['func_name'],
        lineno=data.get('lineno', 0),
        col_offset=data.get('col_offset', 0),
        node_kind=data.get('node_kind', ''),
    )
