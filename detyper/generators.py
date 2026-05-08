"""Tiny task generators over staged AST indexes.

The old generator layer tried to discover facts while deciding edits.  Stage 1
now owns discovery.  This file should stay boring: look up indexed nodes, apply
policy, emit intents.
"""

from __future__ import annotations

import ast
from ast import FunctionDef, Module

from .plan_data import PlanData
from .rules import (
    body_policy_for,
    constructor_param_policy_for,
    expand_aliases,
    global_policy_for,
    inline_param_policy_for,
    param_policy_for,
    resolve_annotation,
    return_policy_for,
)
from .intent_types import Arg, make_remove_annotation_intent, make_rewrite_param_binding_intent, make_wrap_intent
from .intent_unifiers import IntentSet

CallSite = tuple[ast.Call, FunctionDef]


def _indexes(node: ast.AST) -> dict:
    indexes = getattr(node, 'detyping_indexes', None)
    if indexes is None:
        raise ValueError('generators require staged AstData indexes')
    return indexes


def _by_id(node: ast.AST) -> dict[int, ast.AST]:
    by_id = getattr(node, 'detyping_node_index', None)
    if by_id is None:
        raise ValueError('generators require staged AstData node index')
    return by_id


def _selected(plan: PlanData, node: ast.AST) -> bool:
    return plan.selected_annotation_ids is None or node.detyping_id in plan.selected_annotation_ids


def _has_inline(node: FunctionDef) -> bool:
    info = _indexes(node).get('functions', {}).get(str(node.detyping_id), {})
    return bool(info.get('is_inline'))


def _typ(expr: ast.expr | None, plan: PlanData) -> ast.expr | None:
    return expand_aliases(resolve_annotation(expr), plan.aliases)


def _func_info(node: FunctionDef, plan: PlanData):
    return plan.funcs.get(node.name)


def _remove_if(policy_actions, node: ast.AST, context: ast.AST, func_name: str) -> list[IntentSet]:
    if 'remove_annotation' not in policy_actions:
        return []
    return [IntentSet(make_remove_annotation_intent(node, context, [Arg(None, None)], func_name))]


def generate_tasks_global_annotations(module: Module, plan: PlanData) -> list[IntentSet]:
    out: list[IntentSet] = []
    by_id = _by_id(module)
    for raw_id, rec in _indexes(module).get('annotations', {}).items():
        if rec.get('kind') != 'global':
            continue
        ann = by_id[int(raw_id)]
        if not isinstance(ann, ast.AnnAssign) or not _selected(plan, ann):
            continue
        out += _remove_if(global_policy_for(_typ(ann.annotation, plan), plan.aliases).annotation_edits, ann, module, '<module>')
    return out


def generate_tasks_constructor_calls(module: Module, plan: PlanData) -> list[IntentSet]:
    # Constructor call wrapping is semantic and will come back as an indexed fact.
    return []


def generate_tasks_params_definition(node: FunctionDef, plan: PlanData) -> list[IntentSet]:
    info = _func_info(node, plan)
    if info is None:
        return []
    out: list[IntentSet] = []
    inline = _has_inline(node)
    for idx, arg in enumerate(node.args.args):
        if arg.annotation is None or not _selected(plan, arg):
            continue
        typ = _typ(arg.annotation, plan)
        if inline:
            actions = inline_param_policy_for(typ, plan.aliases).definition_edits
        elif node.name == '__init__':
            actions = constructor_param_policy_for(typ, plan.aliases).definition_edits
        else:
            actions = param_policy_for(typ, plan.aliases).definition_edits
        args = [Arg(idx, typ)]
        if 'box' in actions:
            args.append(Arg(idx, None, wrap_order=1))
        if 'remove_annotation' in actions:
            out.append(IntentSet(make_remove_annotation_intent(node, node, args, node.name)))
        elif 'rewrite_param_binding' in actions:
            out.append(IntentSet(make_rewrite_param_binding_intent(node, node, args, node.name)))
    return out


def generate_tasks_params_calls(node: FunctionDef, plan: PlanData, func_uses: list[CallSite], method_uses: list, module: Module) -> list[IntentSet]:
    # Call boundary edits need callee/caller value-shape facts. Stage 1 now indexes
    # the sites; the next pass should add the shape facts and keep this tiny.
    return []


def generate_tasks_body(node: FunctionDef, plan: PlanData) -> list[IntentSet]:
    out: list[IntentSet] = []
    by_id = _by_id(node)
    for ann_id in _indexes(node).get('ann_assigns_by_function', {}).get(str(node.detyping_id), []):
        ann = by_id[int(ann_id)]
        if not isinstance(ann, ast.AnnAssign) or ann.annotation is None or not _selected(plan, ann):
            continue
        typ = _typ(ann.annotation, plan)
        policy = body_policy_for(typ, plan.aliases)
        out += _remove_if(policy.annotation_edits, ann, node, node.name)
        if 'wrap_assigned_expression' in policy.annotation_edits and ann.value is not None:
            out.append(IntentSet(make_wrap_intent(ann, node, [Arg(None, typ, wrap_order=0)], node.name)))
    return out


def generate_tasks_return_definition(node: FunctionDef, plan: PlanData) -> list[IntentSet]:
    info = _func_info(node, plan)
    if info is None or node.returns is None or not _selected(plan, node):
        return []
    return _remove_if(return_policy_for(info.return_type or _typ(node.returns, plan), plan.aliases).definition_edits, node, node, node.name)


def generate_tasks_return_calls(node: FunctionDef, plan: PlanData, func_uses: list[CallSite], method_uses: list) -> list[IntentSet]:
    # Return value/call wrapping will be restored from indexed call/value facts.
    return []
