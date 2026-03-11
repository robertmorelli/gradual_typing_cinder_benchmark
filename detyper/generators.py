"""Task generators: generate_tasks_params, generate_tasks_body, generate_tasks_return."""

import ast
from ast import FunctionDef, Module, AST

from .plan_data import PlanData, classify_type
from .tasks import Arg, Strat, Detyper, RemoveAnnotation, ReproParam, AntiAlias, StripReturn, Wrap
from .transforms import find_returns, find_ann_assigns, find_name_uses_after


def _d(location: AST, context: AST, strat: Strat) -> Detyper:
    d = Detyper()
    d.add(location, context, strat)
    return d


# ── generate_tasks_params ────────────────────────────────────────────────────

def generate_tasks_params(
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
    call_sites = [
        (call, cf) for call, cf in func_uses
        if isinstance(call.func, ast.Name) and call.func.id == name
    ]

    for idx, typ in enumerate(info.param_types):
        if typ is None:
            continue  # unannotated param — no tasks

        kind = classify_type(typ)

        if kind == 'none':
            result.append(_d(node, node, Strat(RemoveAnnotation, [Arg(idx, typ)])))

        elif kind == 'checked_list':
            # Keep param name; body gets `name = cast(T, name)`
            result.append(_d(node, node, Strat(ReproParam, [Arg(idx, typ)])))
            for call, cf in call_sites:
                result.append(_d(call, module, Strat(AntiAlias, [Arg(idx, typ)])))

        else:
            # Rename to _name; body gets `name: T = wrap(T, _name)`
            result.append(_d(node, node, Strat(ReproParam, [Arg(idx, typ)])))
            # Wrap arg[idx] at each call site
            for call, cf in call_sites:
                if idx < len(call.args):
                    if kind == 'primitive':
                        # box(T(arg)) — T inner (order=0), box outer (order=1)
                        result.append(_d(call, cf, Strat(Wrap, [
                            Arg(idx, typ, wrap_order=0),
                            Arg(idx, None, wrap_order=1),  # None = box
                        ])))
                    else:
                        # cast(T, arg)
                        result.append(_d(call, cf, Strat(Wrap, [Arg(idx, typ, wrap_order=0)])))

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

        if kind == 'none':
            continue  # x: None = ... — keep unchanged

        # Wrap the assignment value (index=None = whole node)
        result.append(_d(ann, node, Strat(Wrap, [Arg(None, typ, wrap_order=0)])))

        # Wrap subsequent Name uses for non-CheckedList types
        if kind in ('primitive', 'cast', 'container'):
            var_name = ann.target.id if isinstance(ann.target, ast.Name) else None
            if var_name:
                for name_node in find_name_uses_after(node, var_name, ann):
                    result.append(_d(name_node, node, Strat(Wrap, [
                        Arg(None, typ, wrap_order=0)
                    ])))

    return result


# ── generate_tasks_return ────────────────────────────────────────────────────

def generate_tasks_return(
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
    ret_typ = info.return_type
    kind = classify_type(ret_typ)
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

    if kind == 'none':
        result.append(_d(node, node, Strat(RemoveAnnotation, [Arg(None, None)])))
        return result

    # Strip return annotation for all non-None return types
    result.append(_d(node, node, Strat(RemoveAnnotation, [Arg(None, None)])))

    return_nodes = find_returns(node)

    if kind == 'checked_list':
        # Internal: strip CheckedList[T](...) constructor from return value
        for ret in return_nodes:
            if ret.value is not None:
                result.append(_d(ret, node, Strat(StripReturn, [Arg(None, ret_typ)])))
        # External: wrap call site with CheckedList[T](call)
        for call, cf in all_calls:
            result.append(_d(call, cf, Strat(Wrap, [Arg(None, ret_typ, wrap_order=0)])))

    elif kind == 'primitive':
        # Internal: box(T(return_value))
        for ret in return_nodes:
            if ret.value is not None:
                result.append(_d(ret, node, Strat(Wrap, [
                    Arg(None, ret_typ, wrap_order=0),  # T(...)
                    Arg(None, None, wrap_order=1),     # box(...)
                ])))
        # External: T(call)
        for call, cf in all_calls:
            result.append(_d(call, cf, Strat(Wrap, [Arg(None, ret_typ, wrap_order=0)])))

    else:  # cast / container
        # Internal: no wrap on return value
        # External: cast(T, call)
        for call, cf in all_calls:
            result.append(_d(call, cf, Strat(Wrap, [Arg(None, ret_typ, wrap_order=0)])))

    return result
