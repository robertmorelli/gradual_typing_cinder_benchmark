"""Arg, RewriteIntention subclasses, Detyper."""

from __future__ import annotations

import ast
from ast import AST, FunctionDef
from typing import NamedTuple

from .plan_data import classify_type
from .transforms import make_box_expr, make_wrap_expr


class Arg(NamedTuple):
    index: int | None        # param index, or None for whole-node operations
    typ: ast.expr | None     # None means 'box' (no type, just box())
    wrap_order: int = 0      # lower = inner (applied first within a Wrap intention)


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


class RewriteIntention:
    """Stateful rewrite intention that can merge and execute itself."""

    def __init__(self, location: AST, context: AST, args: list[Arg], func_name: str):
        self.location = location
        self.context = context
        self.args: list[Arg] = list(args)
        self.func_name = func_name
        self._key = (id(location), id(context), self.__class__)
        self._sort_key = build_sort_key(func_name, location, self.__class__)

    def key(self) -> tuple[int, int, type['RewriteIntention']]:
        return self._key

    @property
    def sort_key(self) -> tuple[str, int, int, str, int]:
        return self._sort_key

    def clone(self) -> 'RewriteIntention':
        return self.__class__(self.location, self.context, list(self.args), self.func_name)

    def merge(self, other: 'RewriteIntention') -> None:
        assert self.__class__ is other.__class__
        assert self.key() == other.key()

        merged = list(self.args) + list(other.args)
        seen: set[tuple] = set()
        deduped: list[Arg] = []
        for arg in merged:
            marker = self._arg_marker(arg)
            if marker in seen:
                continue
            seen.add(marker)
            deduped.append(arg)
        self.args = deduped

    def _arg_marker(self, arg: Arg) -> tuple:
        typ_key = ast.dump(arg.typ) if arg.typ is not None else 'None'
        return (arg.index, typ_key)

    def execute(self) -> None:
        raise NotImplementedError


class NoEditIntention(RewriteIntention):
    """No-op intention used as a neutral constructor default."""

    def __init__(self):
        sentinel = ast.Pass()
        super().__init__(sentinel, sentinel, [], '')

    def execute(self) -> None:
        return


class RemoveAnnotation(RewriteIntention):
    def execute(self) -> None:
        node = self.location
        if isinstance(node, FunctionDef):
            for arg in self.args:
                if arg.index is None:
                    node.returns = None
                elif arg.index < len(node.args.args):
                    node.args.args[arg.index].annotation = None
            return

        if isinstance(node, ast.AnnAssign):
            # Sentinel: runner._post_process converts this to a plain Assign.
            node.annotation = None
            return

        raise TypeError(f'Unsupported node for RemoveAnnotation: {type(node).__name__}')


class ReproParam(RewriteIntention):
    def execute(self) -> None:
        node = self.location
        assert isinstance(node, FunctionDef)
        prepend: list[ast.stmt] = []

        for arg in sorted(self.args, key=lambda a: a.index if a.index is not None else 0):
            idx = arg.index
            typ = arg.typ
            if idx is None or idx >= len(node.args.args):
                continue

            param = node.args.args[idx]
            orig_name = param.arg
            kind = classify_type(typ)

            if kind == 'checked_list':
                # Keep param name; prepend plain Assign: `name = cast(T, name)`.
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
                # Rename param to _name; prepend AnnAssign: `name: T = wrap(_name)`.
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
                else:  # cast / container
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


class AntiAlias(RewriteIntention):
    def execute(self) -> None:
        node = self.location
        assert isinstance(node, ast.Call)
        assert isinstance(self.context, ast.Module), "AntiAlias context must be module"
        mod_body = self.context.body

        # Insertion point: after last import.
        insert_idx = 0
        for i, stmt in enumerate(mod_body):
            if isinstance(stmt, (ast.Import, ast.ImportFrom)):
                insert_idx = i + 1

        # Collect existing top-level function names for collision avoidance.
        existing: set[str] = {
            s.name for s in mod_body if isinstance(s, FunctionDef)
        }

        # Determine callee name for wrapper naming.
        if isinstance(node.func, ast.Name):
            callee_name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            callee_name = node.func.attr
        else:
            callee_name = 'unknown'

        sorted_args = sorted(self.args, key=lambda a: a.index if a.index is not None else -1)
        n_args = len(node.args)

        # Name wrapper after callee + all converted arg indices.
        arg_suffix = '_'.join(f'arg{a.index}' for a in sorted_args)
        base = f'_repro_{callee_name}_{arg_suffix}'
        repro_name = base
        n = 2
        while repro_name in existing:
            repro_name = f'{base}_{n}'
            n += 1

        # Build a single wrapper that converts all args and calls f.
        wrapper_params = [ast.arg(arg='f')] + [ast.arg(arg=f'arg{i}') for i in range(n_args)]
        body_stmts: list[ast.stmt] = []

        # One conversion assign per arg.
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

        # Call f with converted args substituted in.
        converted = {a.index for a in sorted_args}
        call_args = [
            ast.Name(id=(f'_arg{i}' if i in converted else f'arg{i}'), ctx=ast.Load())
            for i in range(n_args)
        ]
        body_stmts.append(ast.Assign(
            targets=[ast.Name(id='_out', ctx=ast.Store())],
            value=ast.Call(func=ast.Name(id='f', ctx=ast.Load()), args=call_args, keywords=[]),
            lineno=0, col_offset=0,
        ))

        # Mutate originals in place (anti-alias).
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

        # Rewrite call site once: repro_name(callee_expr, arg0, arg1, ...).
        callee_expr = node.func
        original_args = list(node.args)
        node.func = ast.Name(id=repro_name, ctx=ast.Load())
        node.args = [callee_expr] + original_args


class StripReturn(RewriteIntention):
    def execute(self) -> None:
        node = self.location
        assert isinstance(node, ast.Return)
        if node.value is not None:
            val = node.value
            if isinstance(val, ast.Call) and val.args:
                node.value = val.args[0]


class Wrap(RewriteIntention):
    def _arg_marker(self, arg: Arg) -> tuple:
        typ_key = ast.dump(arg.typ) if arg.typ is not None else 'None'
        return (arg.index, typ_key, arg.wrap_order)

    def execute(self) -> None:
        node = self.location
        sorted_args = sorted(self.args, key=lambda a: a.wrap_order)

        if isinstance(node, ast.AnnAssign):
            # Keep AnnAssign annotation; only wrap the assigned value.
            if node.value is not None:
                node.value = _wrap_expr(node.value, sorted_args)
            return

        if isinstance(node, ast.Return):
            if node.value is not None:
                node.value = _wrap_expr(node.value, sorted_args)
            return

        if isinstance(node, ast.expr):
            # Generic expression replacement in parent context.
            if isinstance(node, ast.Name):
                expr: ast.expr = ast.Name(id=node.id, ctx=ast.Load())
            else:
                expr = node
            expr = _wrap_expr(expr, sorted_args)
            ast.copy_location(expr, node)
            _SpecificNodeReplacer(id(node), expr).visit(self.context)
            return

        raise TypeError(f'Unsupported node for Wrap: {type(node).__name__}')


def _wrap_expr(expr: ast.expr, args: list[Arg]) -> ast.expr:
    wrapped = expr
    for arg in args:
        assert arg.index is None, 'Wrap intentions should target expression nodes directly'
        wrapped = make_box_expr(wrapped) if arg.typ is None else make_wrap_expr(wrapped, arg.typ)
    return wrapped


INTENTION_PRECEDENCE: list[type[RewriteIntention]] = [
    RemoveAnnotation, ReproParam, AntiAlias, StripReturn, Wrap
]


def _precedence_index(intention_type: type[RewriteIntention]) -> int:
    if intention_type in INTENTION_PRECEDENCE:
        return INTENTION_PRECEDENCE.index(intention_type)
    return len(INTENTION_PRECEDENCE)


def build_sort_key(
    func_name: str,
    location: AST,
    intention_type: type[RewriteIntention],
) -> tuple[str, int, int, str, int]:
    lineno = getattr(location, 'lineno', 0) or 0
    col_offset = getattr(location, 'col_offset', 0) or 0
    node_kind = location.__class__.__name__
    return (func_name, lineno, col_offset, node_kind, _precedence_index(intention_type))


class Detyper:
    """Accumulates and executes canonicalized rewrite intentions."""

    def __init__(self, intention: RewriteIntention | None = None):
        self._intentions: dict[tuple[int, int, type[RewriteIntention]], RewriteIntention] = {}
        self.add(NoEditIntention() if intention is None else intention)

    def add(self, intention: RewriteIntention) -> None:
        if isinstance(intention, NoEditIntention):
            return
        key = intention.key()
        existing = self._intentions.get(key)
        if existing is None:
            self._intentions[key] = intention
            return
        existing.merge(intention)

    def __add__(self, other: 'Detyper') -> 'Detyper':
        result = Detyper()
        for intention in self._intentions.values():
            result.add(intention.clone())
        for intention in other._intentions.values():
            result.add(intention.clone())
        return result

    def _sorted_tasks(self) -> list[RewriteIntention]:
        return sorted(self._intentions.values(), key=lambda i: i.sort_key)

    def execute(self) -> None:
        for intention in self._sorted_tasks():
            intention.execute()
