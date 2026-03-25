"""Task generators."""

import ast
from ast import FunctionDef, Module

from .plan_data import PlanData, classify_type
from .tasks import (
    Arg,
    AntiAlias,
    Detyper,
    RemoveAnnotation,
    ReproParam,
    StripReturn,
    Wrap,
)
from .transforms import find_returns, find_ann_assigns, find_name_uses_after
from .policy import param_actions, body_actions, return_actions


# ── params: definition edits ────────────────────────────────────────────────

def generate_tasks_params_definition(
    node: FunctionDef,
    plan: PlanData,
) -> list[Detyper]:
    name = node.name
    if name not in plan.funcs or not plan.funcs[name].is_detyped:
        return []

    info = plan.funcs[name]
    result: list[Detyper] = []

    for idx, typ in enumerate(info.param_types):
        if typ is None:
            continue  # unannotated param — no tasks

        kind = classify_type(typ)
        actions = param_actions(kind)

        if 'remove_annotation' in actions:
            result.append(Detyper(RemoveAnnotation(node, node, [Arg(idx, typ)], node.name)))
            continue

        if 'repro_param' in actions:
            result.append(Detyper(ReproParam(node, node, [Arg(idx, typ)], node.name)))

    return result


# ── params: call edits ───────────────────────────────────────────────────────

def generate_tasks_params_calls(
    node: FunctionDef,
    plan: PlanData,
    func_uses: list,    # list of (call_node, caller_funcdef)
    method_uses: list,
    module: Module,
) -> list[Detyper]:
    name = node.name
    if name not in plan.funcs or not plan.funcs[name].is_detyped:
        return []

    info = plan.funcs[name]
    result: list[Detyper] = []

    # Call sites: (call_node, caller_funcdef)
    free_call_sites = [
        (call, cf) for call, cf in func_uses
        if isinstance(call.func, ast.Name) and call.func.id == name
    ]
    method_call_sites = [
        (call, cf) for call, cf in method_uses
        if isinstance(call.func, ast.Attribute) and call.func.attr == name
    ]

    for idx, typ in enumerate(info.param_types):
        if typ is None:
            continue  # unannotated param — no tasks

        kind = classify_type(typ)
        actions = param_actions(kind)

        if 'anti_alias' in actions:
            # Keep param name; body gets `name = cast(T, name)`
            for call, cf in free_call_sites:
                result.append(Detyper(AntiAlias(call, module, [Arg(idx, typ)], cf.name)))
            # method call sites: for bound calls (x.f(a)) arg idx = param_idx - 1;
            # for unbound calls (C.f(self, a)) arg idx = param_idx (self is in call.args)
            for call, cf in method_call_sites:
                n_params = len(info.param_types)
                call_arg_idx = idx if len(call.args) == n_params else idx - 1
                if call_arg_idx >= 0:
                    result.append(Detyper(AntiAlias(call, module, [Arg(call_arg_idx, typ)], cf.name)))
            continue

        if 'wrap_arg_primitive' in actions or 'wrap_arg_cast' in actions:
            # Target the arg node directly so wraps don't interfere with whole-call wraps
            for call, cf in free_call_sites:
                if idx < len(call.args):
                    arg_node = call.args[idx]
                    if 'wrap_arg_primitive' in actions:
                        result.append(Detyper(Wrap(arg_node, cf, [
                            Arg(None, typ, wrap_order=0),
                            Arg(None, None, wrap_order=1),
                        ], cf.name)))
                    else:
                        result.append(Detyper(Wrap(arg_node, cf, [Arg(None, typ, wrap_order=0)], cf.name)))
            for call, cf in method_call_sites:
                n_params = len(info.param_types)
                call_arg_idx = idx if len(call.args) == n_params else idx - 1
                if call_arg_idx >= 0 and call_arg_idx < len(call.args):
                    arg_node = call.args[call_arg_idx]
                    if 'wrap_arg_primitive' in actions:
                        result.append(Detyper(Wrap(arg_node, cf, [
                            Arg(None, typ, wrap_order=0),
                            Arg(None, None, wrap_order=1),
                        ], cf.name)))
                    else:
                        result.append(Detyper(Wrap(arg_node, cf, [Arg(None, typ, wrap_order=0)], cf.name)))

    return result


# ── generate_tasks_body ──────────────────────────────────────────────────────

def generate_tasks_body(
    node: FunctionDef,
    plan: PlanData,
    module: Module,
) -> list[Detyper]:
    name = node.name
    if name not in plan.funcs or not plan.funcs[name].is_detyped:
        return []

    result: list[Detyper] = []

    for ann in find_ann_assigns(node):
        typ = ann.annotation
        kind = classify_type(typ)
        actions = body_actions(kind)

        if 'remove_body_annotation' in actions:
            # For declaration-only anchors (`x: T`), wrap all subsequent loads of x.
            # This emits use-site casts like `cast(T, x)` before annotation removal.
            if ann.value is None and isinstance(ann.target, ast.Name):
                for use in find_name_uses_after(node, ann.target.id, ann):
                    result.append(Detyper(Wrap(use, node, [Arg(None, typ, wrap_order=0)], node.name)))
            result.append(Detyper(RemoveAnnotation(ann, node, [Arg(None, None)], node.name)))

        if 'wrap_ann_assign_value' in actions:
            # Wrap only the assigned value; annotation retention/removal is policy-driven.
            result.append(Detyper(Wrap(ann, node, [Arg(None, typ, wrap_order=0)], node.name)))

    return result


# ── return: definition edits ────────────────────────────────────────────────

def generate_tasks_return_definition(
    node: FunctionDef,
    plan: PlanData,
) -> list[Detyper]:
    name = node.name
    if name not in plan.funcs or not plan.funcs[name].is_detyped:
        return []

    info = plan.funcs[name]
    ret_typ = info.return_type
    kind = classify_type(ret_typ)
    actions = return_actions(kind)
    result: list[Detyper] = []

    if 'remove_return_annotation' in actions:
        result.append(Detyper(RemoveAnnotation(node, node, [Arg(None, None)], node.name)))

    return_nodes = find_returns(node)

    if 'strip_internal_checked_list' in actions:
        # Internal: strip CheckedList[T](...) constructor from return value.
        for ret in return_nodes:
            if ret.value is not None:
                result.append(Detyper(StripReturn(ret, node, [Arg(None, ret_typ)], node.name)))

    if 'wrap_internal_primitive_box' in actions:
        # Internal: box(T(return_value)).
        for ret in return_nodes:
            if ret.value is not None:
                result.append(Detyper(Wrap(ret, node, [
                    Arg(None, ret_typ, wrap_order=0),  # T(...)
                    Arg(None, None, wrap_order=1),     # box(...)
                ], node.name)))

    return result


# ── return: call edits ───────────────────────────────────────────────────────

def generate_tasks_return_calls(
    node: FunctionDef,
    plan: PlanData,
    func_uses: list,    # list of (call_node, caller_funcdef)
    method_uses: list,
) -> list[Detyper]:
    name = node.name
    if name not in plan.funcs or not plan.funcs[name].is_detyped:
        return []

    info = plan.funcs[name]
    ret_typ = info.return_type
    kind = classify_type(ret_typ)
    actions = return_actions(kind)
    result: list[Detyper] = []

    free_calls = [
        (call, cf) for call, cf in func_uses
        if isinstance(call.func, ast.Name) and call.func.id == name
    ]
    method_calls = [
        (call, cf) for call, cf in method_uses
        if isinstance(call.func, ast.Attribute) and call.func.attr == name
    ]
    all_calls = free_calls + method_calls

    if 'wrap_call_checked_list' in actions:
        # External: CheckedList[T](call).
        for call, cf in all_calls:
            result.append(Detyper(Wrap(call, cf, [Arg(None, ret_typ, wrap_order=0)], cf.name)))

    if 'wrap_call_primitive' in actions:
        # External: T(call).
        for call, cf in all_calls:
            result.append(Detyper(Wrap(call, cf, [Arg(None, ret_typ, wrap_order=0)], cf.name)))

    if 'wrap_call_cast' in actions:
        # External: cast(T, call).
        for call, cf in all_calls:
            result.append(Detyper(Wrap(call, cf, [Arg(None, ret_typ, wrap_order=0)], cf.name)))

    return result
