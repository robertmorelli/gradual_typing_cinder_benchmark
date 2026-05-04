"""Task generators."""

import ast
from ast import FunctionDef, Module

from .ast_utils import find_ann_assigns, find_assigns_to_name_after, find_name_uses_after, find_returns
from .plan_data import FuncInfo, PlanData
from .rules import EditName, body_policy_for, classify_type, container_element_type, expand_aliases, param_call_edits_for, param_policy_for, primitive_intrinsic_return_type, return_policy_for
from .tasks import (
    Arg,
    Detyper,
    make_preserve_argument_mutations_intent,
    make_remove_annotation_intent,
    make_rewrite_param_binding_intent,
    make_unwrap_box_intent,
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


def _annotation_selected(plan: PlanData, node: ast.AST) -> bool:
    return plan.selected_annotation_ids is None or node.detyping_id in plan.selected_annotation_ids


def generate_tasks_params_definition(
    node: FunctionDef,
    plan: PlanData,
) -> list[Detyper]:
    info = _detyped_info(node, plan)
    if info is None:
        return []

    result: list[Detyper] = []

    for idx, param in enumerate(node.args.args):
        typ = info.param_types[idx] if idx < len(info.param_types) else None
        if typ is None and param.annotation is None:
            continue
        if param.annotation is not None and not _annotation_selected(plan, param):
            continue

        policy = param_policy_for(typ, plan.aliases)
        actions = policy.definition_edits

        args = [Arg(idx, typ)]
        if 'box' in actions:
            args.append(Arg(idx, None, wrap_order=1))

        if 'remove_annotation' in actions:
            result.append(Detyper(make_remove_annotation_intent(node, node, args, node.name)))
            continue

        if 'rewrite_param_binding' in actions:
            result.append(Detyper(make_rewrite_param_binding_intent(node, node, args, node.name)))

    return result


def generate_tasks_params_calls(
    node: FunctionDef,
    plan: PlanData,
    func_uses: list[CallSite],
    method_uses: list,
    module: Module,
) -> list[Detyper]:
    info = plan.funcs.get(node.name)
    if info is None:
        return []

    all_call_sites = _iter_call_sites(node.name, func_uses, method_uses)
    call_sites = all_call_sites if info.is_detyped else [
        (call, caller) for call, caller in all_call_sites
        if (caller_info := plan.funcs.get(caller.name)) is not None and caller_info.is_detyped
    ]
    if not call_sites:
        return []
    result: list[Detyper] = []

    for idx, typ in enumerate(info.param_types):
        if typ is None:
            continue
        for fdef_arg in node.args.args[idx:idx + 1]:
            if fdef_arg.annotation is not None and not _annotation_selected(plan, fdef_arg):
                typ = None
        if typ is None:
            continue
        boundary = 'detyped_callee' if info.is_detyped else 'typed_callee'
        actions = param_call_edits_for(typ, boundary, plan.aliases)

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


def _annotation_name(typ: ast.expr | None) -> str | None:
    if isinstance(typ, ast.Name):
        return typ.id
    return None


def _call_return_type(expr: ast.expr, plan: PlanData) -> ast.expr | None:
    if not isinstance(expr, ast.Call):
        return None
    if isinstance(expr.func, ast.Name):
        info = plan.funcs.get(expr.func.id)
    elif isinstance(expr.func, ast.Attribute):
        info = plan.funcs.get(expr.func.attr)
    else:
        info = None
    return info.return_type if info is not None else None


def _local_class_types(func: FunctionDef, plan: PlanData) -> dict[str, str]:
    local_types: dict[str, str] = {}
    for stmt in ast.walk(func):
        if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name):
            typ = _call_return_type(stmt.value, plan)
            name = _annotation_name(typ)
            if name is not None:
                local_types[stmt.targets[0].id] = name
        elif isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
            name = _annotation_name(expand_aliases(stmt.annotation, plan.aliases))
            if name is not None:
                local_types[stmt.target.id] = name
    return local_types


def _local_subscript_value_types(func: FunctionDef, plan: PlanData) -> dict[str, ast.expr]:
    result: dict[str, ast.expr] = {}
    for ann in find_ann_assigns(func):
        if not isinstance(ann.target, ast.Name):
            continue
        typ = expand_aliases(ann.annotation, plan.aliases)
        element_type = container_element_type(typ, plan.aliases)
        if element_type is not None:
            result[ann.target.id] = element_type
    return result


def generate_tasks_body(
    node: FunctionDef,
    plan: PlanData,
) -> list[Detyper]:
    info = _detyped_info(node, plan)
    if info is None:
        return []

    result: list[Detyper] = []
    local_types = _local_class_types(node, plan)
    local_subscript_value_types = _local_subscript_value_types(node, plan)
    local_primitive_assign_types: dict[str, ast.expr] = {}
    for assign in ast.walk(node):
        if isinstance(assign, ast.Assign) and len(assign.targets) == 1 and isinstance(assign.targets[0], ast.Name):
            if isinstance(assign.value, ast.Call) and isinstance(assign.value.func, ast.Name):
                primitive_return = primitive_intrinsic_return_type(assign.value.func.id)
                if primitive_return is not None:
                    local_primitive_assign_types[assign.targets[0].id] = primitive_return

    for call in ast.walk(node):
        if isinstance(call, ast.Call) and isinstance(call.func, ast.Name) and call.func.id in plan.class_init_params:
            for idx, typ in enumerate(plan.class_init_params[call.func.id]):
                if idx < len(call.args) and classify_type(typ, plan.aliases) in ('primitive', 'cast', 'container'):
                    result.append(Detyper(make_wrap_intent(call.args[idx], node, [Arg(None, typ, wrap_order=0)], node.name)))

    primitive_params_for_storage = {
        arg.arg: info.param_types[idx]
        for idx, arg in enumerate(node.args.args)
        if idx < len(info.param_types) and classify_type(info.param_types[idx], plan.aliases) == 'primitive'
    }
    primitive_locals = {
        ann.target.id: expand_aliases(ann.annotation, plan.aliases)
        for ann in find_ann_assigns(node)
        if isinstance(ann.target, ast.Name)
        and 'reproject_primitive_context_uses' in body_policy_for(expand_aliases(ann.annotation, plan.aliases), plan.aliases).annotation_edits
    }
    primitive_context_locals = dict(primitive_locals)
    primitive_context_locals.update(primitive_params_for_storage)
    if primitive_context_locals:
        primitive_self_assign_values = {
            id(assign.value)
            for assign in ast.walk(node)
            if isinstance(assign, ast.Assign)
            and len(assign.targets) == 1
            and isinstance(assign.targets[0], ast.Name)
            and assign.targets[0].id in primitive_context_locals
        }
        for ctx_node in ast.walk(node):
            if isinstance(ctx_node, ast.Compare):
                operands = [ctx_node.left] + list(ctx_node.comparators)
            elif isinstance(ctx_node, ast.BinOp) and id(ctx_node) not in primitive_self_assign_values:
                if isinstance(ctx_node.op, ast.Mod) and isinstance(ctx_node.left, ast.Constant) and isinstance(ctx_node.left.value, str):
                    continue
                operands = [ctx_node.left, ctx_node.right]
            else:
                continue
            for op in operands:
                for sub in ast.walk(op):
                    if isinstance(sub, ast.Name) and isinstance(sub.ctx, ast.Load) and sub.id in primitive_context_locals:
                        result.append(Detyper(make_wrap_intent(sub, node, [Arg(None, primitive_context_locals[sub.id], wrap_order=0)], node.name)))
        for sub_node in ast.walk(node):
            if isinstance(sub_node, ast.Subscript):
                for sub in ast.walk(sub_node.slice):
                    if isinstance(sub, ast.Name) and isinstance(sub.ctx, ast.Load) and sub.id in primitive_context_locals:
                        result.append(Detyper(make_wrap_intent(sub, node, [Arg(None, primitive_context_locals[sub.id], wrap_order=0)], node.name)))
        for call in ast.walk(node):
            if not isinstance(call, ast.Call):
                continue
            callee_name = None
            if isinstance(call.func, ast.Name):
                callee_name = call.func.id
            elif isinstance(call.func, ast.Attribute):
                callee_name = call.func.attr
            callee_info = plan.funcs.get(callee_name) if callee_name is not None else None
            if callee_info is not None:
                for idx, arg_expr in enumerate(call.args):
                    if idx < len(callee_info.param_types) and isinstance(arg_expr, ast.Name) and arg_expr.id in primitive_context_locals:
                        param_type = callee_info.param_types[idx]
                        if classify_type(param_type, plan.aliases) == 'primitive':
                            result.append(Detyper(make_wrap_intent(arg_expr, node, [Arg(None, param_type, wrap_order=0)], node.name)))
            if (
                isinstance(call, ast.Call)
                and isinstance(call.func, ast.Name)
                and call.func.id == 'box'
                and len(call.args) == 1
                and isinstance(call.args[0], ast.Name)
                and call.args[0].id in primitive_context_locals
            ):
                result.append(Detyper(make_unwrap_box_intent(call, node, [Arg(None, None)], node.name)))

    primitive_field_types = {
        field: typ
        for fields in plan.class_fields.values()
        for field, typ in fields.items()
        if classify_type(typ, plan.aliases) == 'primitive'
    }

    def primitive_expr_type(expr: ast.expr) -> ast.expr | None:
        if isinstance(expr, ast.Name) and expr.id in primitive_locals:
            return primitive_locals[expr.id]
        if isinstance(expr, ast.Name) and expr.id in local_subscript_value_types:
            return ast.Name(id='int64', ctx=ast.Load())
        if isinstance(expr, ast.Name) and expr.id in local_primitive_assign_types:
            return local_primitive_assign_types[expr.id]
        if isinstance(expr, ast.Call) and isinstance(expr.func, ast.Name):
            as_type = ast.Name(id=expr.func.id, ctx=ast.Load())
            if classify_type(as_type, plan.aliases) == 'primitive':
                return as_type
            primitive_return = primitive_intrinsic_return_type(expr.func.id)
            if primitive_return is not None:
                return primitive_return
        if isinstance(expr, ast.Attribute):
            return primitive_field_types.get(expr.attr)
        if isinstance(expr, ast.Subscript) and isinstance(expr.value, ast.Name):
            typ = local_subscript_value_types.get(expr.value.id)
            if classify_type(typ, plan.aliases) == 'primitive':
                return typ
        if isinstance(expr, ast.BinOp):
            left = primitive_expr_type(expr.left)
            right = primitive_expr_type(expr.right)
            return left if left is not None else right
        return None

    for assign in ast.walk(node):
        if not isinstance(assign, ast.Assign):
            continue
        for target in assign.targets:
            field_typ = None
            if isinstance(target, ast.Attribute):
                if isinstance(target.value, ast.Name) and target.value.id in local_types:
                    field_typ = plan.class_fields.get(local_types[target.value.id], {}).get(target.attr)
                if field_typ is None:
                    field_typ = primitive_field_types.get(target.attr)
            if field_typ is None and isinstance(target, ast.Subscript) and isinstance(target.value, ast.Name):
                field_typ = local_subscript_value_types.get(target.value.id)
            if classify_type(field_typ, plan.aliases) == 'primitive':
                result.append(Detyper(make_wrap_intent(assign, node, [Arg(None, field_typ, wrap_order=0)], node.name)))

    for ann in find_ann_assigns(node):
        if not _annotation_selected(plan, ann):
            continue
        typ = expand_aliases(ann.annotation, plan.aliases)
        policy = body_policy_for(typ, plan.aliases)
        actions = policy.annotation_edits

        if 'wrap_later_name_uses' in actions and ann.value is None and isinstance(ann.target, ast.Name):
            for use in find_name_uses_after(node, ann.target.id, ann):
                result.append(Detyper(make_wrap_intent(use, node, [Arg(None, typ, wrap_order=0)], node.name)))

        if 'remove_annotation' in actions:
            result.append(Detyper(make_remove_annotation_intent(ann, node, [Arg(None, None)], node.name)))
        if 'box_primitive_storage_values' in actions and isinstance(ann.target, ast.Name):
            if ann.value is not None and isinstance(ann.value, ast.Constant) and isinstance(ann.value.value, (int, float, bool)):
                result.append(Detyper(make_wrap_intent(ann, node, [Arg(None, typ, wrap_order=0), Arg(None, None, wrap_order=1)], node.name)))
            elif ann.value is not None and primitive_expr_type(ann.value) is not None and not (isinstance(ann.value, ast.Name) and ann.value.id in primitive_context_locals):
                result.append(Detyper(make_wrap_intent(ann, node, [Arg(None, None, wrap_order=0)], node.name)))
            for assign in ast.walk(node):
                if not isinstance(assign, ast.Assign):
                    continue
                if any(isinstance(target, ast.Name) and target.id == ann.target.id for target in assign.targets):
                    if assign.value is ann.value:
                        continue
                    value_typ = primitive_expr_type(assign.value)
                    if value_typ is not None:
                        if isinstance(assign.value, ast.BinOp):
                            result.append(Detyper(make_wrap_intent(assign, node, [Arg(None, value_typ, wrap_order=0)], node.name)))
                        elif not (isinstance(assign.value, ast.Call) and isinstance(assign.value.func, ast.Name) and assign.value.func.id == 'box') and not (isinstance(assign.value, ast.Name) and assign.value.id in primitive_context_locals):
                            result.append(Detyper(make_wrap_intent(assign, node, [Arg(None, None, wrap_order=1)], node.name)))
        if 'wrap_assigned_expression' in actions:
            result.append(Detyper(make_wrap_intent(ann, node, [Arg(None, typ, wrap_order=0)], node.name)))

    primitive_storage_assign_values = {
        id(assign.value)
        for assign in ast.walk(node)
        if isinstance(assign, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id in primitive_context_locals for target in assign.targets)
    }
    for binop in ast.walk(node):
        if isinstance(binop, ast.BinOp) and id(binop) in primitive_storage_assign_values:
            for sub in ast.walk(binop):
                if isinstance(sub, ast.Name) and isinstance(sub.ctx, ast.Load) and sub.id in primitive_context_locals:
                    result.append(Detyper(make_wrap_intent(sub, node, [Arg(None, primitive_context_locals[sub.id], wrap_order=0)], node.name)))

    for assign in ast.walk(node):
        if not isinstance(assign, ast.Assign):
            continue
        for target in assign.targets:
            if isinstance(target, ast.Name) and target.id in primitive_context_locals:
                value_typ = primitive_expr_type(assign.value)
                if value_typ is not None and not (isinstance(assign.value, ast.Call) and isinstance(assign.value.func, ast.Name) and assign.value.func.id == 'box') and not (isinstance(assign.value, ast.Name) and assign.value.id in primitive_context_locals):
                    result.append(Detyper(make_wrap_intent(assign, node, [Arg(None, None, wrap_order=1)], node.name)))

    return result


def generate_tasks_return_definition(
    node: FunctionDef,
    plan: PlanData,
) -> list[Detyper]:
    info = _detyped_info(node, plan)
    if info is None:
        return []

    ret_typ = info.return_type
    if node.returns is not None and not _annotation_selected(plan, node):
        return []
    if ret_typ is None and node.returns is not None:
        ret_typ = node.returns
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
    if node.returns is not None and not _annotation_selected(plan, node):
        return []
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
