"""Tree-sitter source-rewrite helpers for the Cinder backend."""

from __future__ import annotations

from dataclasses import dataclass
from typing import NamedTuple

from .rules import classify_type


class Arg(NamedTuple):
    index: int | None
    typ: str | None
    wrap_order: int = 0


@dataclass(frozen=True)
class PreserveArg:
    index: int
    typ: str


def make_wrap_expr(expr: str, typ: str) -> str:
    kind = classify_type(typ)
    if kind == 'primitive':
        return f'{typ}({expr})'
    if kind in ('cast', 'container'):
        return f'cast({typ}, {expr})'
    if kind == 'checked_list':
        return f'{typ}({expr})'
    return expr


def make_box_expr(expr: str) -> str:
    return f'box({expr})'


def wrap_expr(expr: str, args: list[Arg]) -> str:
    wrapped = expr
    for arg in sorted(args, key=lambda item: item.wrap_order):
        wrapped = make_box_expr(wrapped) if arg.typ is None else make_wrap_expr(wrapped, arg.typ)
    return wrapped


def call_arg_index(is_method: bool, param_index: int, param_count: int, positional_arg_count: int) -> int | None:
    if not is_method:
        arg_index = param_index
    else:
        arg_index = param_index if positional_arg_count == param_count else param_index - 1
    if 0 <= arg_index < positional_arg_count:
        return arg_index
    return None


def build_rewrite_param_binding_stmt(orig_name: str, temp_name: str, typ: str) -> tuple[str, bool]:
    kind = classify_type(typ)
    if kind == 'primitive':
        return (f'{orig_name}: {typ} = {typ}({temp_name})', False)
    return (f'{orig_name}: {typ} = cast({typ}, {temp_name})', True)


def build_checked_list_param_binding_stmt(orig_name: str, typ: str) -> tuple[str, bool]:
    return (f'{orig_name} = cast({typ}, {orig_name})', True)


def build_preserve_argument_mutations_wrapper(name: str, n_args: int, args: list[PreserveArg]) -> str:
    sorted_args = sorted(args, key=lambda item: item.index)
    params = ', '.join(['f'] + [f'arg{i}' for i in range(n_args)])
    lines = [f'def {name}({params}):']

    for arg in sorted_args:
        lines.append(f'    _arg{arg.index} = {arg.typ}(arg{arg.index})')

    converted = {arg.index for arg in sorted_args}
    call_args = ', '.join(f'_arg{i}' if i in converted else f'arg{i}' for i in range(n_args))
    lines.append(f'    _out = f({call_args})')

    for arg in sorted_args:
        lines.append(f'    arg{arg.index}.clear()')
        lines.append(f'    arg{arg.index}.extend(_arg{arg.index})')

    lines.append('    return _out')
    return '\n'.join(lines)
