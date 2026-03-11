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

        if kind == 'none':
            result.append(_d(node, node, Strat(RemoveAnnotation, [Arg(idx, typ)])))

        elif kind == 'checked_list':
            # Keep param name; body gets `name = cast(T, name)`
            result.append(_d(node, node, Strat(ReproParam, [Arg(idx, typ)])))
            for call, cf in free_call_sites:
                result.append(_d(call, module, Strat(AntiAlias, [Arg(idx, typ)])))
            # method call sites: for bound calls (x.f(a)) arg idx = param_idx - 1;
            # for unbound calls (C.f(self, a)) arg idx = param_idx (self is in call.args)
            for call, cf in method_call_sites:
                n_params = len(info.param_types)
                call_arg_idx = idx if len(call.args) == n_params else idx - 1
                if call_arg_idx >= 0:
                    result.append(_d(call, module, Strat(AntiAlias, [Arg(call_arg_idx, typ)])))

        else:
            # Rename to _name; body gets `name: T = wrap(T, _name)`
            result.append(_d(node, node, Strat(ReproParam, [Arg(idx, typ)])))
            # Target the arg node directly so wraps don't interfere with whole-call wraps
            for call, cf in free_call_sites:
                if idx < len(call.args):
                    arg_node = call.args[idx]
                    if kind == 'primitive':
                        result.append(_d(arg_node, cf, Strat(Wrap, [
                            Arg(None, typ, wrap_order=0),
                            Arg(None, None, wrap_order=1),
                        ])))
                    else:
                        result.append(_d(arg_node, cf, Strat(Wrap, [Arg(None, typ, wrap_order=0)])))
            for call, cf in method_call_sites:
                n_params = len(info.param_types)
                call_arg_idx = idx if len(call.args) == n_params else idx - 1
                if call_arg_idx >= 0 and call_arg_idx < len(call.args):
                    arg_node = call.args[call_arg_idx]
                    if kind == 'primitive':
                        result.append(_d(arg_node, cf, Strat(Wrap, [
                            Arg(None, typ, wrap_order=0),
                            Arg(None, None, wrap_order=1),
                        ])))
                    else:
                        result.append(_d(arg_node, cf, Strat(Wrap, [Arg(None, typ, wrap_order=0)])))

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

        # Wrap the assignment value only. Subsequent uses are not wrapped because
        # the annotation is preserved on the AnnAssign, giving Cinder the static type.
        # Wrapping uses would lose type narrowing (e.g. Optional narrowed in if-blocks).
        result.append(_d(ann, node, Strat(Wrap, [Arg(None, typ, wrap_order=0)])))

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
