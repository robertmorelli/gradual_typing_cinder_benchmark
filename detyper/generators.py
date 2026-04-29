"""Task generators."""

import ast
from ast import FunctionDef, Module

from .ast_utils import find_ann_assigns, find_name_uses_after, find_returns
from .plan_data import FuncInfo, PlanData
from .rules import EditName, body_policy_for, expand_aliases, param_policy_for, return_policy_for
from .tasks import (
    Arg,
    Detyper,
    make_preserve_argument_mutations_intent,
    make_remove_annotation_intent,
    make_rewrite_param_binding_intent,
    make_unwrap_checked_return_value_intent,
    make_wrap_intent,
)

CallSite = tuple[ast.Call, FunctionDef]


def _detyped_info(node: FunctionDef, plan: PlanData) -> FuncInfo | None:
    info = plan.funcs.get(node.name)
    if info is None or not info.is_detyped:
        return None
    return info


def _iter_call_sites(
    name: str,
    func_uses: list[CallSite],
    method_uses: list[CallSite],
) -> list[CallSite]:
    free_calls = [
        (call, caller) for call, caller in func_uses
        if isinstance(call.func, ast.Name) and call.func.id == name
    ]
    method_calls = [
        (call, caller) for call, caller in method_uses
        if isinstance(call.func, ast.Attribute) and call.func.attr == name
    ]
    return free_calls + method_calls


def _call_arg_index(call: ast.Call, param_index: int, param_count: int) -> int | None:
    if isinstance(call.func, ast.Name):
        arg_index = param_index
    else:
        arg_index = param_index if len(call.args) == param_count else param_index - 1
    if 0 <= arg_index < len(call.args):
        return arg_index
    return None


def _wrap_args_for(actions: tuple[EditName, ...], typ: ast.expr | None) -> list[Arg]:
    wrap_args: list[Arg] = []
    if 'wrap_with_runtime_type' in actions:
        wrap_args.append(Arg(None, typ, wrap_order=0))
    if 'box' in actions:
        wrap_args.append(Arg(None, None, wrap_order=1))
    return wrap_args


def generate_tasks_params_definition(
    node: FunctionDef,
    plan: PlanData,
) -> list[Detyper]:
    info = _detyped_info(node, plan)
    if info is None:
        return []

    result: list[Detyper] = []

    for idx, typ in enumerate(info.param_types):
        if typ is None:
            continue

        policy = param_policy_for(typ, plan.aliases)
        actions = policy.definition_edits

        if 'remove_annotation' in actions:
            result.append(Detyper(make_remove_annotation_intent(node, node, [Arg(idx, typ)], node.name)))
            continue

        if 'rewrite_param_binding' in actions:
            result.append(Detyper(make_rewrite_param_binding_intent(node, node, [Arg(idx, typ)], node.name)))

    return result


def generate_tasks_params_calls(
    node: FunctionDef,
    plan: PlanData,
    func_uses: list[CallSite],
    method_uses: list,
    module: Module,
) -> list[Detyper]:
    info = _detyped_info(node, plan)
    if info is None:
        return []

    call_sites = _iter_call_sites(node.name, func_uses, method_uses)
    result: list[Detyper] = []

    for idx, typ in enumerate(info.param_types):
        if typ is None:
            continue
        policy = param_policy_for(typ, plan.aliases)
        actions = policy.call_edits

        if 'preserve_argument_mutations' in actions:
            for call, caller in call_sites:
                arg_index = _call_arg_index(call, idx, len(info.param_types))
                if arg_index is None:
                    continue
                result.append(Detyper(make_preserve_argument_mutations_intent(
                    call, module, [Arg(arg_index, typ)], caller.name,
                )))
            continue

        wrap_args = _wrap_args_for(actions, typ)
        if wrap_args:
            for call, caller in call_sites:
                arg_index = _call_arg_index(call, idx, len(info.param_types))
                if arg_index is None:
                    continue
                result.append(Detyper(make_wrap_intent(call.args[arg_index], caller, wrap_args, caller.name)))

    return result


def generate_tasks_body(
    node: FunctionDef,
    plan: PlanData,
) -> list[Detyper]:
    if _detyped_info(node, plan) is None:
        return []

    result: list[Detyper] = []

    for ann in find_ann_assigns(node):
        typ = expand_aliases(ann.annotation, plan.aliases)
        policy = body_policy_for(typ, plan.aliases)
        actions = policy.annotation_edits

        if 'wrap_later_name_uses' in actions and ann.value is None and isinstance(ann.target, ast.Name):
            for use in find_name_uses_after(node, ann.target.id, ann):
                result.append(Detyper(make_wrap_intent(use, node, [Arg(None, typ, wrap_order=0)], node.name)))

        if 'remove_annotation' in actions:
            result.append(Detyper(make_remove_annotation_intent(ann, node, [Arg(None, None)], node.name)))

        if 'wrap_assigned_expression' in actions:
            result.append(Detyper(make_wrap_intent(ann, node, [Arg(None, typ, wrap_order=0)], node.name)))

    return result


def generate_tasks_return_definition(
    node: FunctionDef,
    plan: PlanData,
) -> list[Detyper]:
    info = _detyped_info(node, plan)
    if info is None:
        return []

    ret_typ = info.return_type
    policy = return_policy_for(ret_typ, plan.aliases)
    actions = policy.definition_edits
    result: list[Detyper] = []

    if 'remove_annotation' in actions:
        result.append(Detyper(make_remove_annotation_intent(node, node, [Arg(None, None)], node.name)))

    return result


def generate_tasks_return_calls(
    node: FunctionDef,
    plan: PlanData,
    func_uses: list[CallSite],
    method_uses: list,
) -> list[Detyper]:
    info = _detyped_info(node, plan)
    if info is None:
        return []

    ret_typ = info.return_type
    policy = return_policy_for(ret_typ, plan.aliases)
    value_actions = policy.value_edits
    call_actions = policy.call_edits
    result: list[Detyper] = []
    return_nodes = find_returns(node)

    if 'unwrap_checked_return_value' in value_actions:
        for ret in return_nodes:
            if ret.value is not None:
                result.append(Detyper(make_unwrap_checked_return_value_intent(
                    ret, node, [Arg(None, ret_typ)], node.name,
                )))

    return_wrap_args = _wrap_args_for(value_actions, ret_typ)
    if return_wrap_args:
        for ret in return_nodes:
            if ret.value is not None:
                result.append(Detyper(make_wrap_intent(ret, node, return_wrap_args, node.name)))

    call_wrap_args = _wrap_args_for(call_actions, ret_typ)
    if call_wrap_args:
        for call, caller in _iter_call_sites(node.name, func_uses, method_uses):
            result.append(Detyper(make_wrap_intent(call, caller, call_wrap_args, caller.name)))

    return result
