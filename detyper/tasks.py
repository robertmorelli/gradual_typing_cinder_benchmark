"""Intent data model, canonical combination rules, and intent application."""

from __future__ import annotations

import ast
from ast import AST, FunctionDef
from dataclasses import dataclass
from typing import Literal, NamedTuple

from .rules import classify_type


def make_wrap_expr(expr: ast.expr, typ: ast.expr) -> ast.expr:
    """Return a new AST node wrapping expr for the given type."""
    kind = classify_type(typ)
    if kind == 'primitive':
        type_name = typ.id if isinstance(typ, ast.Name) else ast.unparse(typ)
        return ast.Call(
            func=ast.Name(id=type_name, ctx=ast.Load()),
            args=[expr], keywords=[],
        )
    if kind in ('cast', 'container'):
        return ast.Call(
            func=ast.Name(id='cast', ctx=ast.Load()),
            args=[typ, expr], keywords=[],
        )
    if kind == 'checked_list':
        return ast.Call(func=typ, args=[expr], keywords=[])
    return expr


def make_box_expr(expr: ast.expr) -> ast.expr:
    return ast.Call(
        func=ast.Name(id='box', ctx=ast.Load()),
        args=[expr], keywords=[],
    )


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
]

IntentionKey = tuple[int, int, IntentKind]
NodeCollisionKey = tuple[int, int]


@dataclass
class Intent:
    kind: IntentKind
    location: AST
    context: AST
    args: list[Arg]
    func_name: str

    def key(self) -> IntentionKey:
        return (id(self.location), id(self.context), self.kind)

    def node_collision_key(self) -> NodeCollisionKey:
        return (id(self.location), id(self.context))

    @property
    def sort_key(self) -> tuple[str, int, int, str, int]:
        return build_sort_key(self.func_name, self.location, self.kind)

    def clone(self) -> 'Intent':
        return Intent(self.kind, self.location, self.context, list(self.args), self.func_name)


class _SpecificNodeReplacer(ast.NodeTransformer):
    """Replace a specific AST node (by identity) with a given replacement."""

    def __init__(self, target_id: int, replacement: ast.expr):
        self.target_id = target_id
        self.replacement = replacement

    def generic_visit(self, node: AST) -> AST:
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                new_list = []
                for item in value:
                    if isinstance(item, ast.AST) and id(item) == self.target_id:
                        new_list.append(self.replacement)
                    elif isinstance(item, ast.AST):
                        new_list.append(self.visit(item))
                    else:
                        new_list.append(item)
                setattr(node, field, new_list)
            elif isinstance(value, ast.AST):
                if id(value) == self.target_id:
                    setattr(node, field, self.replacement)
                else:
                    self.visit(value)
        return node


def make_remove_annotation_intent(location: AST, context: AST, args: list[Arg], func_name: str) -> Intent:
    return Intent('remove_annotation', location, context, args, func_name)


def make_rewrite_param_binding_intent(location: AST, context: AST, args: list[Arg], func_name: str) -> Intent:
    return Intent('rewrite_param_binding', location, context, args, func_name)


def make_preserve_argument_mutations_intent(location: AST, context: AST, args: list[Arg], func_name: str) -> Intent:
    return Intent('preserve_argument_mutations', location, context, args, func_name)


def make_unwrap_checked_return_value_intent(location: AST, context: AST, args: list[Arg], func_name: str) -> Intent:
    return Intent('unwrap_checked_return_value', location, context, args, func_name)


def make_wrap_intent(location: AST, context: AST, args: list[Arg], func_name: str) -> Intent:
    return Intent('wrap', location, context, args, func_name)


def _arg_marker(intent: Intent, arg: Arg) -> tuple:
    typ_key = ast.dump(arg.typ) if arg.typ is not None else 'None'
    if intent.kind == 'wrap':
        return (arg.index, typ_key, arg.wrap_order)
    return (arg.index, typ_key)


def merge_intentions_of_same_kind(existing: Intent, incoming: Intent) -> Intent:
    """Canonical combiner for two same-kind intents on the same node."""
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


INTENTION_EXECUTION_ORDER: list[IntentKind] = [
    'remove_annotation',
    'rewrite_param_binding',
    'preserve_argument_mutations',
    'unwrap_checked_return_value',
    'wrap',
]


def _precedence_index(intent_kind: IntentKind) -> int:
    if intent_kind in INTENTION_EXECUTION_ORDER:
        return INTENTION_EXECUTION_ORDER.index(intent_kind)
    return len(INTENTION_EXECUTION_ORDER)


def build_sort_key(
    func_name: str,
    location: AST,
    intent_kind: IntentKind,
) -> tuple[str, int, int, str, int]:
    lineno = getattr(location, 'lineno', 0) or 0
    col_offset = getattr(location, 'col_offset', 0) or 0
    node_kind = location.__class__.__name__
    return (func_name, lineno, col_offset, node_kind, _precedence_index(intent_kind))


def resolve_same_node_intentions(intentions: list[Intent]) -> list[Intent]:
    """Canonical answer to: "I have A and B on the same node. What happens?"

    1. Same node/context + same intent kind => merge into one canonical intent.
    2. Same node/context + different intent kind => keep both.
    3. Execute the kept intents in sort_key order.
    """
    canonical_by_kind: dict[IntentionKey, Intent] = {}
    for intent in intentions:
        key = intent.key()
        existing = canonical_by_kind.get(key)
        if existing is None:
            canonical_by_kind[key] = intent
            continue
        canonical_by_kind[key] = merge_intentions_of_same_kind(existing, intent)
    return sorted(canonical_by_kind.values(), key=lambda intent: intent.sort_key)


def _apply_remove_annotation(intent: Intent) -> None:
    node = intent.location
    if isinstance(node, FunctionDef):
        for arg in intent.args:
            if arg.index is None:
                node.returns = None
            elif arg.index < len(node.args.args):
                node.args.args[arg.index].annotation = None
        return

    if isinstance(node, ast.AnnAssign):
        node.annotation = None
        return

    raise TypeError(f'Unsupported node for remove_annotation: {type(node).__name__}')


def _apply_rewrite_param_binding(intent: Intent) -> None:
    node = intent.location
    assert isinstance(node, FunctionDef)
    prepend: list[ast.stmt] = []

    for arg in sorted(intent.args, key=lambda item: item.index if item.index is not None else 0):
        idx = arg.index
        typ = arg.typ
        if idx is None or idx >= len(node.args.args):
            continue

        param = node.args.args[idx]
        orig_name = param.arg
        kind = classify_type(typ)

        if kind == 'checked_list':
            param.annotation = None
            stmt: ast.stmt = ast.Assign(
                targets=[ast.Name(id=orig_name, ctx=ast.Store())],
                value=ast.Call(
                    func=ast.Name(id='cast', ctx=ast.Load()),
                    args=[typ, ast.Name(id=orig_name, ctx=ast.Load())],
                    keywords=[],
                ),
                lineno=node.lineno, col_offset=node.col_offset,
            )
        else:
            new_name = '_' + orig_name
            param.arg = new_name
            param.annotation = None

            src = ast.Name(id=new_name, ctx=ast.Load())
            if kind == 'primitive':
                type_name = typ.id if isinstance(typ, ast.Name) else ast.unparse(typ)
                value: ast.expr = ast.Call(
                    func=ast.Name(id=type_name, ctx=ast.Load()),
                    args=[src], keywords=[],
                )
            else:
                value = ast.Call(
                    func=ast.Name(id='cast', ctx=ast.Load()),
                    args=[typ, src], keywords=[],
                )

            stmt = ast.AnnAssign(
                target=ast.Name(id=orig_name, ctx=ast.Store()),
                annotation=typ,
                value=value,
                simple=1,
                lineno=node.lineno, col_offset=node.col_offset,
            )

        prepend.append(stmt)

    node.body = prepend + node.body


def _apply_preserve_argument_mutations(intent: Intent) -> None:
    node = intent.location
    assert isinstance(node, ast.Call)
    assert isinstance(intent.context, ast.Module)
    mod_body = intent.context.body

    insert_idx = 0
    for i, stmt in enumerate(mod_body):
        if isinstance(stmt, (ast.Import, ast.ImportFrom)):
            insert_idx = i + 1

    existing: set[str] = {stmt.name for stmt in mod_body if isinstance(stmt, FunctionDef)}
    if isinstance(node.func, ast.Name):
        callee_name = node.func.id
    elif isinstance(node.func, ast.Attribute):
        callee_name = node.func.attr
    else:
        callee_name = 'unknown'

    sorted_args = sorted(intent.args, key=lambda item: item.index if item.index is not None else -1)
    n_args = len(node.args)
    arg_suffix = '_'.join(f'arg{arg.index}' for arg in sorted_args)
    base = f'_repro_{callee_name}_{arg_suffix}'
    repro_name = base
    suffix = 2
    while repro_name in existing:
        repro_name = f'{base}_{suffix}'
        suffix += 1

    wrapper_params = [ast.arg(arg='f')] + [ast.arg(arg=f'arg{i}') for i in range(n_args)]
    body_stmts: list[ast.stmt] = []

    for arg in sorted_args:
        idx = arg.index
        body_stmts.append(ast.Assign(
            targets=[ast.Name(id=f'_arg{idx}', ctx=ast.Store())],
            value=ast.Call(
                func=arg.typ,
                args=[ast.Name(id=f'arg{idx}', ctx=ast.Load())],
                keywords=[],
            ),
            lineno=0, col_offset=0,
        ))

    converted = {arg.index for arg in sorted_args}
    call_args = [
        ast.Name(id=(f'_arg{i}' if i in converted else f'arg{i}'), ctx=ast.Load())
        for i in range(n_args)
    ]
    body_stmts.append(ast.Assign(
        targets=[ast.Name(id='_out', ctx=ast.Store())],
        value=ast.Call(func=ast.Name(id='f', ctx=ast.Load()), args=call_args, keywords=[]),
        lineno=0, col_offset=0,
    ))

    for arg in sorted_args:
        idx = arg.index
        body_stmts.append(ast.Expr(value=ast.Call(
            func=ast.Attribute(
                value=ast.Name(id=f'arg{idx}', ctx=ast.Load()), attr='clear', ctx=ast.Load(),
            ),
            args=[], keywords=[],
        )))
        body_stmts.append(ast.Expr(value=ast.Call(
            func=ast.Attribute(
                value=ast.Name(id=f'arg{idx}', ctx=ast.Load()), attr='extend', ctx=ast.Load(),
            ),
            args=[ast.Name(id=f'_arg{idx}', ctx=ast.Load())],
            keywords=[],
        )))

    body_stmts.append(ast.Return(value=ast.Name(id='_out', ctx=ast.Load())))

    wrapper = FunctionDef(
        name=repro_name,
        args=ast.arguments(
            posonlyargs=[], args=wrapper_params, vararg=None,
            kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[],
        ),
        body=body_stmts,
        decorator_list=[], returns=None,
        lineno=0, col_offset=0,
    )
    ast.fix_missing_locations(wrapper)
    mod_body.insert(insert_idx, wrapper)

    callee_expr = node.func
    original_args = list(node.args)
    node.func = ast.Name(id=repro_name, ctx=ast.Load())
    node.args = [callee_expr] + original_args


def _apply_unwrap_checked_return_value(intent: Intent) -> None:
    node = intent.location
    assert isinstance(node, ast.Return)
    if node.value is not None:
        value = node.value
        if isinstance(value, ast.Call) and value.args:
            node.value = value.args[0]


def _wrap_expr(expr: ast.expr, args: list[Arg]) -> ast.expr:
    wrapped = expr
    for arg in args:
        assert arg.index is None
        wrapped = make_box_expr(wrapped) if arg.typ is None else make_wrap_expr(wrapped, arg.typ)
    return wrapped


def _apply_wrap(intent: Intent) -> None:
    node = intent.location
    sorted_args = sorted(intent.args, key=lambda arg: arg.wrap_order)

    if isinstance(node, ast.AnnAssign):
        if node.value is not None:
            node.value = _wrap_expr(node.value, sorted_args)
        return

    if isinstance(node, ast.Return):
        if node.value is not None:
            node.value = _wrap_expr(node.value, sorted_args)
        return

    if isinstance(node, ast.expr):
        expr: ast.expr = ast.Name(id=node.id, ctx=ast.Load()) if isinstance(node, ast.Name) else node
        expr = _wrap_expr(expr, sorted_args)
        ast.copy_location(expr, node)
        _SpecificNodeReplacer(id(node), expr).visit(intent.context)
        return

    raise TypeError(f'Unsupported node for wrap: {type(node).__name__}')


def apply_intent(intent: Intent) -> None:
    """Apply one canonical intent to the AST."""
    if intent.kind == 'remove_annotation':
        _apply_remove_annotation(intent)
        return
    if intent.kind == 'rewrite_param_binding':
        _apply_rewrite_param_binding(intent)
        return
    if intent.kind == 'preserve_argument_mutations':
        _apply_preserve_argument_mutations(intent)
        return
    if intent.kind == 'unwrap_checked_return_value':
        _apply_unwrap_checked_return_value(intent)
        return
    if intent.kind == 'wrap':
        _apply_wrap(intent)
        return
    raise ValueError(f'Unknown intent kind: {intent.kind}')


class Detyper:
    """Accumulates intents, resolves node collisions, and applies them."""

    def __init__(self, intention: Intent | None = None):
        self._intentions: list[Intent] = []
        if intention is not None:
            self.add(intention)

    def add(self, intention: Intent) -> None:
        self._intentions.append(intention)

    def __add__(self, other: 'Detyper') -> 'Detyper':
        result = Detyper()
        for intention in self._intentions:
            result.add(intention.clone())
        for intention in other._intentions:
            result.add(intention.clone())
        return result

    def _sorted_tasks(self) -> list[Intent]:
        by_node: dict[NodeCollisionKey, list[Intent]] = {}
        for intention in self._intentions:
            by_node.setdefault(intention.node_collision_key(), []).append(intention)

        canonicalized: list[Intent] = []
        for same_node_intentions in by_node.values():
            canonicalized.extend(resolve_same_node_intentions(same_node_intentions))

        return sorted(canonicalized, key=lambda intention: intention.sort_key)

    def execute(self) -> None:
        for intention in self._sorted_tasks():
            apply_intent(intention)
