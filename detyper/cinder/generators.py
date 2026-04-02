"""Policy-to-rewrite plan generators for the Cinder backend."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, NamedTuple

from .plan_data import FuncInfo
from .rules import EditName, body_policy_for, classify_type, param_policy_for, return_policy_for


class Arg(NamedTuple):
    index: int | None
    typ: str | None
    wrap_order: int = 0


@dataclass(frozen=True)
class PreserveArg:
    index: int
    typ: str


ParamRewriteMode = Literal['remove_annotation', 'rewrite_param_binding']


@dataclass(frozen=True)
class ParamDefinitionRewrite:
    index: int
    typ: str
    mode: ParamRewriteMode


@dataclass(frozen=True)
class BodyAssignmentRewrite:
    typ: str
    remove_annotation: bool
    wrap_later_name_uses: bool
    wrap_assigned_expression: bool


@dataclass(frozen=True)
class PositionalWrap:
    arg_index: int
    wraps: tuple[Arg, ...]


@dataclass(frozen=True)
class CallRewritePlan:
    positional_wraps: tuple[PositionalWrap, ...]
    preserve_args: tuple[PreserveArg, ...]
    return_wraps: tuple[Arg, ...]


@dataclass(frozen=True)
class ReturnRewritePlan:
    remove_annotation: bool
    unwrap_checked_return_value: bool
    value_wraps: tuple[Arg, ...]
    call_wraps: tuple[Arg, ...]


def wrap_args_for(actions: tuple[EditName, ...], typ: str | None) -> tuple[Arg, ...]:
    wrap_args: list[Arg] = []
    if 'wrap_with_runtime_type' in actions:
        wrap_args.append(Arg(None, typ, wrap_order=0))
    if 'box' in actions:
        wrap_args.append(Arg(None, None, wrap_order=1))
    return tuple(wrap_args)


def wraps_require_box(wraps: tuple[Arg, ...]) -> bool:
    return any(arg.typ is None for arg in wraps)


def wraps_require_cast(wraps: tuple[Arg, ...]) -> bool:
    return any(arg.typ is not None and classify_type(arg.typ) in ('cast', 'container') for arg in wraps)


def generate_param_definition_rewrites(info: FuncInfo | None) -> tuple[ParamDefinitionRewrite, ...]:
    if info is None or not info.is_detyped:
        return ()

    rewrites: list[ParamDefinitionRewrite] = []
    for index, typ in enumerate(info.param_types):
        if typ is None:
            continue
        actions = param_policy_for(typ).definition_edits
        if 'remove_annotation' in actions:
            rewrites.append(ParamDefinitionRewrite(index=index, typ=typ, mode='remove_annotation'))
            continue
        if 'rewrite_param_binding' in actions:
            rewrites.append(ParamDefinitionRewrite(index=index, typ=typ, mode='rewrite_param_binding'))
    return tuple(rewrites)


def _call_arg_index(is_method: bool, param_index: int, param_count: int, positional_arg_count: int) -> int | None:
    if not is_method:
        arg_index = param_index
    else:
        arg_index = param_index if positional_arg_count == param_count else param_index - 1
    if 0 <= arg_index < positional_arg_count:
        return arg_index
    return None


def generate_call_rewrite_plan(
    info: FuncInfo | None,
    kind: str,
    positional_arg_count: int,
) -> CallRewritePlan | None:
    if info is None or not info.is_detyped:
        return None

    positional_wraps: list[PositionalWrap] = []
    preserve_args: list[PreserveArg] = []
    param_count = len(info.param_types)

    for index, typ in enumerate(info.param_types):
        if typ is None:
            continue
        arg_index = _call_arg_index(kind == 'method', index, param_count, positional_arg_count)
        if arg_index is None:
            continue

        policy = param_policy_for(typ)
        if 'preserve_argument_mutations' in policy.call_edits:
            preserve_args.append(PreserveArg(arg_index, typ))
            continue

        wraps = wrap_args_for(policy.call_edits, typ)
        if wraps:
            positional_wraps.append(PositionalWrap(arg_index=arg_index, wraps=wraps))

    return_plan = generate_return_rewrite_plan(info)
    return_wraps = () if return_plan is None else return_plan.call_wraps
    if not positional_wraps and not preserve_args and not return_wraps:
        return None

    return CallRewritePlan(
        positional_wraps=tuple(positional_wraps),
        preserve_args=tuple(preserve_args),
        return_wraps=return_wraps,
    )


def generate_body_assignment_rewrite(typ: str | None) -> BodyAssignmentRewrite | None:
    if typ is None:
        return None
    actions = body_policy_for(typ).annotation_edits
    return BodyAssignmentRewrite(
        typ=typ,
        remove_annotation='remove_annotation' in actions,
        wrap_later_name_uses='wrap_later_name_uses' in actions,
        wrap_assigned_expression='wrap_assigned_expression' in actions,
    )


def generate_return_rewrite_plan(info: FuncInfo | None) -> ReturnRewritePlan | None:
    if info is None or not info.is_detyped:
        return None

    policy = return_policy_for(info.return_type)
    return ReturnRewritePlan(
        remove_annotation='remove_annotation' in policy.definition_edits,
        unwrap_checked_return_value='unwrap_checked_return_value' in policy.value_edits,
        value_wraps=wrap_args_for(policy.value_edits, info.return_type),
        call_wraps=wrap_args_for(policy.call_edits, info.return_type),
    )
