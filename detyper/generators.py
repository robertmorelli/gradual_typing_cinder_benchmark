"""Task generators."""

import ast
from ast import FunctionDef, Module

from .ast_utils import find_ann_assigns, find_assigns_to_name_after, find_name_uses_after, find_returns
from .context_facts import attr_owner_class as fact_attr_owner_class, field_expr_shape, field_ref_fact, local_class_types as fact_local_class_types, primitive_field_read_type
from .plan_data import FuncInfo, PlanData
from .rules import EditName, body_policy_for, classify_type, constructor_param_policy_for, container_element_type, expand_aliases, global_policy_for, inline_param_policy_for, param_call_edits_for, param_policy_for, primitive_intrinsic_return_type, return_policy_for
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


def _has_inline(node: FunctionDef) -> bool:
    return any(
        (isinstance(d, ast.Name) and d.id == 'inline') or
        (isinstance(d, ast.Attribute) and d.attr == 'inline')
        for d in node.decorator_list
    )


def _walk_top_level_exprs(module: Module):
    for stmt in module.body:
        if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        yield from ast.walk(stmt)


def _find_class_init(module: Module, class_name: str | None) -> FunctionDef | None:
    if class_name is None:
        return None
    for stmt in module.body:
        if isinstance(stmt, ast.ClassDef) and stmt.name == class_name:
            for item in stmt.body:
                if isinstance(item, ast.FunctionDef) and item.name == '__init__':
                    return item
    return None


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


def _selected_self_field_types(node: FunctionDef, plan: PlanData) -> dict[str, ast.expr]:
    fields: dict[str, ast.expr] = {}
    for ann in find_ann_assigns(node):
        if not _annotation_selected(plan, ann):
            continue
        if (
            isinstance(ann.target, ast.Attribute)
            and isinstance(ann.target.value, ast.Name)
            and ann.target.value.id == 'self'
        ):
            typ = expand_aliases(ann.annotation, plan.aliases)
            if typ is not None:
                fields[ann.target.attr] = typ
    return fields


def generate_tasks_params_definition(
    node: FunctionDef,
    plan: PlanData,
) -> list[Detyper]:
    info = _detyped_info(node, plan)
    if info is None:
        if not _has_inline(node) or plan.selected_annotation_ids is None:
            return []
        info = plan.funcs.get(node.name)
        if info is None:
            return []

    result: list[Detyper] = []

    for idx, param in enumerate(node.args.args):
        typ = info.param_types[idx] if idx < len(info.param_types) else None
        if typ is None and param.annotation is None:
            continue
        if param.annotation is not None and not _annotation_selected(plan, param):
            continue

        if _has_inline(node):
            typ = expand_aliases(param.annotation, plan.aliases) if param.annotation is not None else typ
            policy = inline_param_policy_for(typ, plan.aliases)
            actions = policy.definition_edits
            if 'wrap_param_uses_with_runtime_type' in policy.body_use_edits:
                for use in find_name_uses_after(node, param.arg, node):
                    result.append(Detyper(make_wrap_intent(use, node, [Arg(None, typ, wrap_order=0)], node.name)))
        elif node.name == '__init__':
            typ = expand_aliases(param.annotation, plan.aliases) if param.annotation is not None else typ
            policy = constructor_param_policy_for(typ, plan.aliases)
            actions = policy.definition_edits
        else:
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
    result: list[Detyper] = []
    if node.name == '__init__':
        for call, caller in all_call_sites:
            if not (isinstance(call.func, ast.Attribute) and call.func.attr == '__init__'):
                continue
            target_class = call.func.value.id if isinstance(call.func.value, ast.Name) else None
            class_params = plan.class_init_params.get(target_class) if target_class else None
            if class_params is None:
                continue
            target_init_def = _find_class_init(module, target_class)
            if target_init_def is None:
                continue
            caller_info = plan.funcs.get(caller.name)
            caller_primitive_params: set[str] = set()
            if caller_info is not None and caller_info.is_detyped:
                for c_arg in caller.args.args:
                    if c_arg.annotation is None:
                        continue
                    c_typ = expand_aliases(c_arg.annotation, plan.aliases)
                    if classify_type(c_typ, plan.aliases) == 'primitive' and _annotation_selected(plan, c_arg):
                        caller_primitive_params.add(c_arg.arg)
            for idx, typ in enumerate(class_params):
                if typ is None or classify_type(typ, plan.aliases) != 'primitive':
                    continue
                arg_index = idx + 1
                if arg_index >= len(call.args) or arg_index >= len(target_init_def.args.args):
                    continue
                target_arg = target_init_def.args.args[arg_index]
                callee_selected = (
                    target_arg.annotation is not None
                    and plan.selected_annotation_ids is not None
                    and target_arg.detyping_id in plan.selected_annotation_ids
                )
                arg_expr = call.args[arg_index]
                caller_is_boxed = isinstance(arg_expr, ast.Name) and arg_expr.id in caller_primitive_params
                if isinstance(arg_expr, ast.Constant):
                    continue
                if callee_selected and not caller_is_boxed:
                    result.append(Detyper(make_wrap_intent(arg_expr, caller, [Arg(None, None, wrap_order=0)], caller.name)))
                elif (not callee_selected) and caller_is_boxed:
                    result.append(Detyper(make_wrap_intent(arg_expr, caller, [Arg(None, typ, wrap_order=0)], caller.name)))
        all_call_sites = [
            (call, caller) for call, caller in all_call_sites
            if not (isinstance(call.func, ast.Attribute) and call.func.attr == '__init__')
        ]
    call_sites = all_call_sites if info.is_detyped else [
        (call, caller) for call, caller in all_call_sites
        if (caller_info := plan.funcs.get(caller.name)) is not None and caller_info.is_detyped
    ]
    if not call_sites:
        return result

    for idx, typ in enumerate(info.param_types):
        if typ is None:
            continue
        boundary = 'detyped_callee' if info.is_detyped else 'typed_callee'
        if boundary == 'detyped_callee':
            for fdef_arg in node.args.args[idx:idx + 1]:
                if fdef_arg.annotation is not None and not _annotation_selected(plan, fdef_arg):
                    typ = None
        if typ is None:
            continue
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
    return fact_local_class_types(func, plan)


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


def generate_tasks_global_annotations(module: Module, plan: PlanData) -> list[Detyper]:
    result: list[Detyper] = []
    for stmt in module.body:
        if not (isinstance(stmt, ast.AnnAssign) and stmt.annotation is not None):
            continue
        if not _annotation_selected(plan, stmt):
            continue
        typ = expand_aliases(stmt.annotation, plan.aliases)
        # Static Python gives module names initialized with None a sticky None type.
        # Removing Optional-ish global annotations turns later object writes into errors.
        if isinstance(stmt.value, ast.Constant) and stmt.value.value is None:
            continue
        actions = global_policy_for(typ, plan.aliases).annotation_edits
        if 'box_primitive_storage_values' in actions and stmt.value is not None:
            result.append(Detyper(make_wrap_intent(stmt, module, [Arg(None, typ, wrap_order=0), Arg(None, None, wrap_order=1)], '<module>')))
        if 'remove_annotation' in actions:
            result.append(Detyper(make_remove_annotation_intent(stmt, module, [Arg(None, None)], '<module>')))
    return result


def generate_tasks_constructor_calls(module: Module, plan: PlanData) -> list[Detyper]:
    result: list[Detyper] = []
    for call in _walk_top_level_exprs(module):
        if not (isinstance(call, ast.Call) and isinstance(call.func, ast.Name)):
            continue
        class_name = call.func.id
        for (cls, idx), typ in (plan.selected_constructor_param_types or {}).items():
            if cls != class_name:
                continue
            wrap_args = _wrap_args_for(constructor_param_policy_for(typ, plan.aliases).call_edits, typ)
            if idx < len(call.args) and wrap_args:
                result.append(Detyper(make_wrap_intent(call.args[idx], module, wrap_args, '<module>')))
    return result


def generate_tasks_body(
    node: FunctionDef,
    plan: PlanData,
) -> list[Detyper]:
    info = _detyped_info(node, plan)
    if info is None:
        if not plan.selected_field_types and not plan.selected_constructor_param_types:
            return []
        info = plan.funcs.get(node.name)
        if info is None:
            return []

    result: list[Detyper] = []
    local_types = _local_class_types(node, plan)
    for idx, arg in enumerate(node.args.args):
        if idx < len(info.param_types):
            name = _annotation_name(info.param_types[idx])
            if name is not None:
                local_types[arg.arg] = name
    local_subscript_value_types = _local_subscript_value_types(node, plan)
    owner_class = plan.func_classes.get(node.detyping_id)
    selected_self_fields = _selected_self_field_types(node, plan)

    def _type_name(typ: ast.expr | None) -> str | None:
        return typ.id if isinstance(typ, ast.Name) else None

    def attr_owner_class(expr: ast.expr) -> str | None:
        return fact_attr_owner_class(expr, owner_class=owner_class, local_types=local_types, plan=plan)

    def selected_field_type(expr: ast.Attribute) -> ast.expr | None:
        fact = field_ref_fact(expr, owner_class=owner_class, local_types=local_types, plan=plan)
        return fact.selected_type if fact is not None else None

    def selected_primitive_field_type(expr: ast.Attribute) -> ast.expr | None:
        typ = selected_field_type(expr)
        if classify_type(typ, plan.aliases) == 'primitive':
            return typ
        owner_cls = attr_owner_class(expr.value)
        if owner_cls is not None and expr.attr in plan.class_fields.get(owner_cls, {}):
            return None
        matches = [typ for (_cls, field), typ in (plan.selected_field_types or {}).items() if field == expr.attr]
        all_declared = [fields[expr.attr] for fields in plan.class_fields.values() if expr.attr in fields]
        if matches and len({ast.dump(item) for item in matches + all_declared}) == 1 and classify_type(matches[0], plan.aliases) == 'primitive':
            return matches[0]
        return None
    local_primitive_assign_types: dict[str, ast.expr] = {}
    for assign in ast.walk(node):
        if isinstance(assign, ast.Assign) and len(assign.targets) == 1 and isinstance(assign.targets[0], ast.Name):
            if isinstance(assign.value, ast.Call) and isinstance(assign.value.func, ast.Name):
                primitive_return = primitive_intrinsic_return_type(assign.value.func.id)
                if primitive_return is not None:
                    local_primitive_assign_types[assign.targets[0].id] = primitive_return

    for call in ast.walk(node):
        if not (isinstance(call, ast.Call) and isinstance(call.func, ast.Name)):
            continue
        class_name = call.func.id
        selected_ctor_types = plan.selected_constructor_param_types or {}
        ctor_types = [
            (idx, typ)
            for (cls, idx), typ in selected_ctor_types.items()
            if cls == class_name
        ]
        if not ctor_types and plan.selected_annotation_ids is None and class_name in plan.class_init_params:
            ctor_types = list(enumerate(plan.class_init_params[class_name]))
        for idx, typ in ctor_types:
            actions = constructor_param_policy_for(typ, plan.aliases).call_edits
            wrap_args = _wrap_args_for(actions, typ)
            if idx < len(call.args) and wrap_args:
                result.append(Detyper(make_wrap_intent(call.args[idx], node, wrap_args, node.name)))

    primitive_params_for_storage: dict[str, ast.expr] = {}
    if info.is_detyped:
        for idx, arg in enumerate(node.args.args):
            if idx < len(info.param_types) and classify_type(info.param_types[idx], plan.aliases) == 'primitive':
                if arg.annotation is None or _annotation_selected(plan, arg):
                    primitive_params_for_storage[arg.arg] = info.param_types[idx]
    for arg in node.args.args:
        if arg.annotation is not None and _annotation_selected(plan, arg):
            arg_typ = expand_aliases(arg.annotation, plan.aliases)
            if classify_type(arg_typ, plan.aliases) == 'primitive':
                primitive_params_for_storage[arg.arg] = arg_typ
    primitive_locals = {
        ann.target.id: expand_aliases(ann.annotation, plan.aliases)
        for ann in find_ann_assigns(node)
        if isinstance(ann.target, ast.Name)
        and _annotation_selected(plan, ann)
        and 'reproject_primitive_context_uses' in body_policy_for(expand_aliases(ann.annotation, plan.aliases), plan.aliases).annotation_edits
    }
    primitive_ann_locals = {
        ann.target.id: expand_aliases(ann.annotation, plan.aliases)
        for ann in find_ann_assigns(node)
        if isinstance(ann.target, ast.Name)
        and _annotation_selected(plan, ann)
        and classify_type(expand_aliases(ann.annotation, plan.aliases), plan.aliases) == 'primitive'
    }
    primitive_context_locals = dict(primitive_locals)
    primitive_context_locals.update(primitive_params_for_storage)
    primitive_context_locals.update(local_primitive_assign_types)
    if primitive_context_locals or plan.selected_field_types:
        primitive_self_assign_values = {
            id(assign.value)
            for assign in ast.walk(node)
            if isinstance(assign, ast.Assign)
            and len(assign.targets) == 1
            and isinstance(assign.targets[0], ast.Name)
            and assign.targets[0].id in primitive_context_locals
        }
        for boolop in ast.walk(node):
            if isinstance(boolop, ast.BoolOp):
                has_cbool = any(isinstance(value, ast.Call) and isinstance(value.func, ast.Name) and value.func.id == 'cbool' for value in boolop.values)
                if has_cbool:
                    for value in boolop.values:
                        if isinstance(value, ast.Compare):
                            operands = [value.left] + list(value.comparators)
                            has_primitive_operand = any(
                                (isinstance(op, ast.Name) and op.id in primitive_context_locals)
                                or (isinstance(op, ast.Attribute) and (selected_primitive_field_type(op) is not None or primitive_field_read_type(op, owner_class=owner_class, local_types=local_types, plan=plan) is not None))
                                for op in operands
                            )
                            if has_primitive_operand:
                                result.append(Detyper(make_wrap_intent(value, node, [Arg(None, ast.Name(id='cbool', ctx=ast.Load()), wrap_order=0)], node.name)))
                for value in boolop.values:
                    if isinstance(value, ast.Attribute) and selected_primitive_field_type(value) is not None:
                        result.append(Detyper(make_wrap_intent(value, node, [Arg(None, ast.Name(id='cbool', ctx=ast.Load()), wrap_order=0)], node.name)))

        boxed_attribute_ids: set[int] = {
            id(call.args[0])
            for call in ast.walk(node)
            if isinstance(call, ast.Call)
            and isinstance(call.func, ast.Name)
            and call.func.id == 'box'
            and len(call.args) == 1
            and isinstance(call.args[0], ast.Attribute)
        }
        for ctx_node in ast.walk(node):
            if isinstance(ctx_node, ast.Compare):
                operands = [ctx_node.left] + list(ctx_node.comparators)
            elif isinstance(ctx_node, ast.BoolOp):
                operands = list(ctx_node.values)
            elif isinstance(ctx_node, ast.BinOp) and id(ctx_node) not in primitive_self_assign_values:
                if isinstance(ctx_node.op, ast.Mod) and isinstance(ctx_node.left, ast.Constant) and isinstance(ctx_node.left.value, str):
                    continue
                operands = [ctx_node.left, ctx_node.right]
            else:
                continue
            binop_context = isinstance(ctx_node, ast.BinOp)
            for op in operands:
                for sub in ast.walk(op):
                    if isinstance(sub, ast.Name) and isinstance(sub.ctx, ast.Load) and sub.id in primitive_context_locals:
                        result.append(Detyper(make_wrap_intent(sub, node, [Arg(None, primitive_context_locals[sub.id], wrap_order=0)], node.name)))
                    elif isinstance(sub, ast.Attribute) and (field_typ := selected_primitive_field_type(sub)) is not None:
                        if binop_context and id(sub) in boxed_attribute_ids:
                            continue
                        result.append(Detyper(make_wrap_intent(sub, node, [Arg(None, field_typ, wrap_order=0)], node.name)))
        for assign in ast.walk(node):
            if isinstance(assign, ast.Assign) and len(assign.targets) == 1 and isinstance(assign.targets[0], ast.Name):
                target_name = assign.targets[0].id
                target_typ = primitive_ann_locals.get(target_name)
                if target_typ is not None and (
                    (isinstance(assign.value, ast.Name) and assign.value.id in primitive_context_locals)
                    or (isinstance(assign.value, ast.Subscript) and isinstance(assign.value.value, ast.Name) and assign.value.value.id in local_subscript_value_types)
                    or (isinstance(assign.value, ast.BinOp))
                ):
                    result.append(Detyper(make_wrap_intent(assign, node, [Arg(None, target_typ, wrap_order=0)], node.name)))
        for ann_assign in find_ann_assigns(node):
            if (
                ann_assign.annotation is not None
                and classify_type(expand_aliases(ann_assign.annotation, plan.aliases), plan.aliases) == 'primitive'
                and isinstance(ann_assign.value, ast.Name)
                and ann_assign.value.id in primitive_context_locals
            ):
                result.append(Detyper(make_wrap_intent(ann_assign.value, node, [Arg(None, primitive_context_locals[ann_assign.value.id], wrap_order=0)], node.name)))
        for sub_node in ast.walk(node):
            if isinstance(sub_node, ast.Subscript) and isinstance(sub_node.value, ast.Name) and sub_node.value.id in local_subscript_value_types:
                for sub in ast.walk(sub_node.slice):
                    if isinstance(sub, ast.Name) and isinstance(sub.ctx, ast.Load) and sub.id in primitive_context_locals:
                        result.append(Detyper(make_wrap_intent(sub, node, [Arg(None, primitive_context_locals[sub.id], wrap_order=0)], node.name)))
        for sub_node in ast.walk(node):
            if isinstance(sub_node, ast.Subscript) and isinstance(sub_node.value, ast.Attribute):
                fact = field_ref_fact(sub_node.value, owner_class=owner_class, local_types=local_types, plan=plan)
                detyped_to_dynamic = False
                if fact is not None and fact.storage_detyped:
                    declared = fact.declared_type
                    if declared is not None and classify_type(declared, plan.aliases) != 'primitive':
                        detyped_to_dynamic = True
                if not detyped_to_dynamic and plan.selected_field_types:
                    attr_name = sub_node.value.attr
                    matches = [
                        typ for (cls, field), typ in plan.selected_field_types.items()
                        if field == attr_name
                    ]
                    if matches and all(classify_type(typ, plan.aliases) != 'primitive' for typ in matches):
                        declared_matches = [fields[attr_name] for fields in plan.class_fields.values() if attr_name in fields]
                        if declared_matches and all(classify_type(typ, plan.aliases) != 'primitive' for typ in declared_matches):
                            detyped_to_dynamic = True
                if not detyped_to_dynamic:
                    continue
                primitive_typed_args: set[str] = set()
                for arg in node.args.args:
                    if arg.annotation is None or _annotation_selected(plan, arg):
                        continue
                    arg_typ = expand_aliases(arg.annotation, plan.aliases)
                    if classify_type(arg_typ, plan.aliases) == 'primitive':
                        primitive_typed_args.add(arg.arg)
                if not primitive_typed_args:
                    continue
                for sub in ast.walk(sub_node.slice):
                    if isinstance(sub, ast.Name) and isinstance(sub.ctx, ast.Load) and sub.id in primitive_typed_args:
                        result.append(Detyper(make_wrap_intent(sub, node, [Arg(None, None, wrap_order=1)], node.name)))
        for ret in find_returns(node):
            if ret.value is None or info.return_type is None:
                continue
            ret_kind = classify_type(info.return_type, plan.aliases)
            if isinstance(ret.value, ast.Name) and ret.value.id in primitive_context_locals and ret_kind == 'primitive':
                result.append(Detyper(make_wrap_intent(ret.value, node, [Arg(None, info.return_type, wrap_order=0)], node.name)))
            if ret_kind == 'primitive' and isinstance(ret.value, ast.UnaryOp) and isinstance(ret.value.operand, ast.Name) and ret.value.operand.id in primitive_context_locals:
                result.append(Detyper(make_wrap_intent(ret.value, node, [Arg(None, info.return_type, wrap_order=0)], node.name)))
            if ret_kind == 'primitive' and isinstance(ret.value, ast.Attribute):
                fact = field_ref_fact(ret.value, owner_class=owner_class, local_types=local_types, plan=plan)
                if fact is not None and fact.storage_detyped and classify_type(fact.selected_type, plan.aliases) == 'primitive':
                    result.append(Detyper(make_wrap_intent(ret.value, node, [Arg(None, info.return_type, wrap_order=0)], node.name)))
            if ret_kind == 'builtin' and isinstance(info.return_type, ast.Name) and info.return_type.id == 'int':
                if isinstance(ret.value, ast.Name) and ret.value.id in primitive_context_locals:
                    result.append(Detyper(make_wrap_intent(ret.value, node, [Arg(None, info.return_type, wrap_order=0)], node.name)))
        for call in ast.walk(node):
            if not isinstance(call, ast.Call):
                continue
            callee_name = None
            if isinstance(call.func, ast.Name):
                callee_name = call.func.id
            elif isinstance(call.func, ast.Attribute):
                callee_name = call.func.attr
            callee_info = plan.funcs.get(callee_name) if callee_name is not None else None
            if callee_name == '__init__':
                callee_info = None
            if callee_info is not None:
                for idx, arg_expr in enumerate(call.args):
                    if idx >= len(callee_info.param_types):
                        continue
                    param_type = callee_info.param_types[idx]
                    if classify_type(param_type, plan.aliases) != 'primitive':
                        continue
                    if isinstance(arg_expr, ast.Name) and arg_expr.id in primitive_context_locals:
                        result.append(Detyper(make_wrap_intent(arg_expr, node, [Arg(None, param_type, wrap_order=0)], node.name)))
                    elif isinstance(arg_expr, ast.Attribute):
                        fact = field_ref_fact(arg_expr, owner_class=owner_class, local_types=local_types, plan=plan)
                        if fact is not None and fact.storage_detyped and classify_type(fact.selected_type, plan.aliases) == 'primitive':
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
            if (
                isinstance(call, ast.Call)
                and isinstance(call.func, ast.Name)
                and call.func.id == 'box'
                and len(call.args) == 1
                and isinstance(call.args[0], ast.Attribute)
                and selected_primitive_field_type(call.args[0]) is not None
            ):
                result.append(Detyper(make_unwrap_box_intent(call, node, [Arg(None, None)], node.name)))

    def call_returns_selected_primitive(expr: ast.expr, primitive_name: str | None = None) -> bool:
        if not isinstance(expr, ast.Call):
            return False
        callee_name = None
        if isinstance(expr.func, ast.Name):
            callee_name = expr.func.id
        elif isinstance(expr.func, ast.Attribute):
            callee_name = expr.func.attr
        if callee_name is None:
            return False
        callee = plan.funcs.get(callee_name)
        if callee is None or callee.return_type is None:
            return False
        if classify_type(callee.return_type, plan.aliases) != 'primitive':
            return False
        if primitive_name is None:
            return True
        return isinstance(callee.return_type, ast.Name) and callee.return_type.id == primitive_name

    field_types_by_name: dict[str, list[ast.expr]] = {}
    for fields in plan.class_fields.values():
        for field, typ in fields.items():
            field_types_by_name.setdefault(field, []).append(typ)
    dynamic_via_field_locals: set[str] = set()
    selected_field_attrs = {attr for (_cls, attr) in (plan.selected_field_types or {})}
    for assign in ast.walk(node):
        if isinstance(assign, ast.Assign) and len(assign.targets) == 1 and isinstance(assign.targets[0], ast.Name) and isinstance(assign.value, ast.Attribute):
            fact = field_ref_fact(assign.value, owner_class=owner_class, local_types=local_types, plan=plan)
            if fact is not None and fact.storage_detyped:
                dynamic_via_field_locals.add(assign.targets[0].id)
            elif assign.value.attr in selected_field_attrs:
                dynamic_via_field_locals.add(assign.targets[0].id)
    for boolop in ast.walk(node):
        if isinstance(boolop, ast.BoolOp):
            has_cbool = any(
                (isinstance(value, ast.Call) and isinstance(value.func, ast.Name) and value.func.id == 'cbool')
                or call_returns_selected_primitive(value, 'cbool')
                for value in boolop.values
            )
            if has_cbool:
                for value in boolop.values:
                    if isinstance(value, ast.Compare):
                        operands = [value.left] + list(value.comparators)
                        has_primitive_operand = any(
                            (isinstance(op, ast.Name) and op.id in primitive_context_locals)
                            or (isinstance(op, ast.Attribute) and primitive_field_read_type(op, owner_class=owner_class, local_types=local_types, plan=plan) is not None)
                            or (isinstance(op, ast.Call) and isinstance(op.func, ast.Name) and classify_type(ast.Name(id=op.func.id, ctx=ast.Load()), plan.aliases) == 'primitive')
                            for op in operands
                        )
                        has_dynamic_operand = any(
                            (isinstance(op, ast.Name) and op.id in dynamic_via_field_locals)
                            or (isinstance(op, ast.Attribute) and (fact := field_ref_fact(op, owner_class=owner_class, local_types=local_types, plan=plan)) is not None and fact.storage_detyped)
                            for op in operands
                        )
                        if has_primitive_operand or has_dynamic_operand:
                            result.append(Detyper(make_wrap_intent(value, node, [Arg(None, ast.Name(id='cbool', ctx=ast.Load()), wrap_order=0)], node.name)))

    primitive_field_types = {
        field: typs[0]
        for field, typs in field_types_by_name.items()
        if len({ast.dump(typ) for typ in typs}) == 1 and classify_type(typs[0], plan.aliases) == 'primitive'
    }

    def primitive_attr_type(expr: ast.Attribute) -> ast.expr | None:
        typ = primitive_field_read_type(expr, owner_class=owner_class, local_types=local_types, plan=plan)
        if typ is not None:
            return typ
        return primitive_field_types.get(expr.attr)

    for boolop in ast.walk(node):
        if isinstance(boolop, ast.BoolOp):
            for value in boolop.values:
                if isinstance(value, ast.Attribute) and primitive_attr_type(value) is not None:
                    result.append(Detyper(make_wrap_intent(value, node, [Arg(None, ast.Name(id='cbool', ctx=ast.Load()), wrap_order=0)], node.name)))

    if info.return_type is not None and classify_type(info.return_type, plan.aliases) == 'builtin' and isinstance(info.return_type, ast.Name) and info.return_type.id == 'int':
        for ret in find_returns(node):
            if isinstance(ret.value, ast.Attribute) and primitive_attr_type(ret.value) is not None:
                result.append(Detyper(make_wrap_intent(ret.value, node, [Arg(None, info.return_type, wrap_order=0)], node.name)))
            elif isinstance(ret.value, ast.UnaryOp) and isinstance(ret.value.operand, ast.Name) and ret.value.operand.id in primitive_context_locals:
                result.append(Detyper(make_wrap_intent(ret.value, node, [Arg(None, info.return_type, wrap_order=0)], node.name)))

    boxed_attribute_ids_outer: set[int] = {
        id(call.args[0])
        for call in ast.walk(node)
        if isinstance(call, ast.Call)
        and isinstance(call.func, ast.Name)
        and call.func.id == 'box'
        and len(call.args) == 1
        and isinstance(call.args[0], ast.Attribute)
    }
    for ctx_node in ast.walk(node):
        if isinstance(ctx_node, ast.Compare):
            operands = [ctx_node.left] + list(ctx_node.comparators)
        elif isinstance(ctx_node, ast.BinOp):
            if isinstance(ctx_node.op, ast.Mod) and isinstance(ctx_node.left, ast.Constant) and isinstance(ctx_node.left.value, str):
                continue
            operands = [ctx_node.left, ctx_node.right]
        else:
            continue
        binop_context = isinstance(ctx_node, ast.BinOp)
        for op in operands:
            for sub in ast.walk(op):
                if isinstance(sub, ast.Attribute) and (field_typ := primitive_attr_type(sub)) is not None:
                    if binop_context and id(sub) in boxed_attribute_ids_outer:
                        continue
                    result.append(Detyper(make_wrap_intent(sub, node, [Arg(None, field_typ, wrap_order=0)], node.name)))

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
            if selected_primitive_field_type(expr) is not None:
                return None
            return primitive_attr_type(expr)
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
                if isinstance(target.value, ast.Attribute):
                    owner_typ = selected_field_type(target.value)
                    if owner_typ is None:
                        owner_cls = attr_owner_class(target.value)
                        if owner_cls is not None:
                            owner_typ = ast.Name(id=owner_cls, ctx=ast.Load())
                    if owner_typ is not None:
                        result.append(Detyper(make_wrap_intent(target.value, node, [Arg(None, owner_typ, wrap_order=0)], node.name)))
                target_owner_cls = attr_owner_class(target.value) if isinstance(target, ast.Attribute) else None
                if isinstance(target, ast.Attribute) and target_owner_cls is None:
                    field_typ = None
                else:
                    field_typ = primitive_attr_type(target)
            if field_typ is None and isinstance(target, ast.Subscript) and isinstance(target.value, ast.Name):
                field_typ = local_subscript_value_types.get(target.value.id)
            if classify_type(field_typ, plan.aliases) == 'primitive':
                if isinstance(target, ast.Attribute) and selected_primitive_field_type(target) is not None:
                    result.append(Detyper(make_wrap_intent(assign, node, [Arg(None, field_typ, wrap_order=0), Arg(None, None, wrap_order=1)], node.name)))
                else:
                    result.append(Detyper(make_wrap_intent(assign, node, [Arg(None, field_typ, wrap_order=0)], node.name)))

    if plan.selected_field_types:
        for assign in ast.walk(node):
            if not isinstance(assign, ast.Assign):
                continue
            for target in assign.targets:
                if isinstance(target, ast.Attribute) and (field_typ := selected_primitive_field_type(target)) is not None:
                    result.append(Detyper(make_wrap_intent(assign, node, [Arg(None, field_typ, wrap_order=0), Arg(None, None, wrap_order=1)], node.name)))

    for ann in find_ann_assigns(node):
        if not _annotation_selected(plan, ann):
            continue
        typ = expand_aliases(ann.annotation, plan.aliases)
        policy = body_policy_for(typ, plan.aliases)
        actions = policy.annotation_edits
        is_self_field = (
            isinstance(ann.target, ast.Attribute)
            and isinstance(ann.target.value, ast.Name)
            and ann.target.value.id == 'self'
        )

        if 'wrap_later_name_uses' in actions and ann.value is None and isinstance(ann.target, ast.Name):
            for use in find_name_uses_after(node, ann.target.id, ann):
                result.append(Detyper(make_wrap_intent(use, node, [Arg(None, typ, wrap_order=0)], node.name)))

        if 'remove_annotation' in actions:
            result.append(Detyper(make_remove_annotation_intent(ann, node, [Arg(None, None)], node.name)))
        if 'box_primitive_storage_values' in actions and is_self_field and classify_type(typ, plan.aliases) == 'primitive':
            if ann.value is not None:
                result.append(Detyper(make_wrap_intent(ann, node, [Arg(None, typ, wrap_order=0), Arg(None, None, wrap_order=1)], node.name)))
            for assign in ast.walk(node):
                if not isinstance(assign, ast.Assign):
                    continue
                if any(isinstance(target, ast.Attribute) and target.attr == ann.target.attr for target in assign.targets):
                    if assign.value is ann.value:
                        continue
                    result.append(Detyper(make_wrap_intent(assign, node, [Arg(None, typ, wrap_order=0), Arg(None, None, wrap_order=1)], node.name)))
        if 'box_primitive_storage_values' in actions and isinstance(ann.target, ast.Name):
            if ann.value is not None and isinstance(ann.value, ast.Constant) and isinstance(ann.value.value, (int, float, bool)):
                result.append(Detyper(make_wrap_intent(ann, node, [Arg(None, typ, wrap_order=0), Arg(None, None, wrap_order=1)], node.name)))
            elif ann.value is not None and primitive_expr_type(ann.value) is not None and not (isinstance(ann.value, ast.Name) and ann.value.id in primitive_context_locals):
                if isinstance(ann.value, ast.Attribute):
                    result.append(Detyper(make_wrap_intent(ann, node, [Arg(None, typ, wrap_order=0), Arg(None, None, wrap_order=1)], node.name)))
                else:
                    result.append(Detyper(make_wrap_intent(ann, node, [Arg(None, None, wrap_order=0)], node.name)))
            elif (
                ann.value is not None
                and isinstance(ann.value, ast.Attribute)
                and not (isinstance(ann.value, ast.Name) and ann.value.id in primitive_context_locals)
            ):
                fact = field_ref_fact(ann.value, owner_class=owner_class, local_types=local_types, plan=plan)
                if fact is not None and fact.storage_detyped and fact.declared_type is not None and classify_type(fact.declared_type, plan.aliases) == 'primitive':
                    result.append(Detyper(make_wrap_intent(ann, node, [Arg(None, typ, wrap_order=0), Arg(None, None, wrap_order=1)], node.name)))
            for assign in ast.walk(node):
                if not isinstance(assign, ast.Assign):
                    continue
                if any(isinstance(target, ast.Name) and target.id == ann.target.id for target in assign.targets):
                    if assign.value is ann.value:
                        continue
                    if any(isinstance(other.target, ast.Name) and other.target.id == ann.target.id and other.annotation is not None and not _annotation_selected(plan, other) for other in find_ann_assigns(node)):
                        continue
                    value_typ = primitive_expr_type(assign.value)
                    if value_typ is not None:
                        if isinstance(assign.value, ast.BinOp):
                            result.append(Detyper(make_wrap_intent(assign, node, [Arg(None, value_typ, wrap_order=0)], node.name)))
                        elif isinstance(assign.value, ast.Attribute):
                            result.append(Detyper(make_wrap_intent(assign, node, [Arg(None, typ, wrap_order=0), Arg(None, None, wrap_order=1)], node.name)))
                        elif not (isinstance(assign.value, ast.Call) and isinstance(assign.value.func, ast.Name) and assign.value.func.id == 'box') and not (isinstance(assign.value, ast.Name) and assign.value.id in primitive_context_locals):
                            result.append(Detyper(make_wrap_intent(assign, node, [Arg(None, None, wrap_order=1)], node.name)))
        if 'wrap_assigned_expression' in actions and not is_self_field:
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

    kept_primitive_ann_names: set[str] = set()
    for ann in find_ann_assigns(node):
        if isinstance(ann.target, ast.Name) and not _annotation_selected(plan, ann):
            ann_typ = expand_aliases(ann.annotation, plan.aliases)
            if classify_type(ann_typ, plan.aliases) == 'primitive':
                kept_primitive_ann_names.add(ann.target.id)
    for arg in node.args.args:
        if arg.annotation is not None and not _annotation_selected(plan, arg):
            arg_typ = expand_aliases(arg.annotation, plan.aliases)
            if classify_type(arg_typ, plan.aliases) == 'primitive':
                kept_primitive_ann_names.add(arg.arg)
    for assign in ast.walk(node):
        if not isinstance(assign, ast.Assign):
            continue
        for target in assign.targets:
            if isinstance(target, ast.Name) and target.id in primitive_context_locals:
                value_typ = primitive_expr_type(assign.value)
                if value_typ is not None and not (isinstance(assign.value, ast.Call) and isinstance(assign.value.func, ast.Name) and assign.value.func.id == 'box') and not (isinstance(assign.value, ast.Name) and assign.value.id in primitive_context_locals):
                    result.append(Detyper(make_wrap_intent(assign, node, [Arg(None, None, wrap_order=1)], node.name)))
                elif isinstance(assign.value, ast.Name) and assign.value.id in kept_primitive_ann_names:
                    result.append(Detyper(make_wrap_intent(assign, node, [Arg(None, None, wrap_order=1)], node.name)))
                elif isinstance(assign.value, ast.Subscript) and isinstance(assign.value.value, ast.Name) and assign.value.value.id in local_subscript_value_types:
                    elem_typ = local_subscript_value_types[assign.value.value.id]
                    if classify_type(elem_typ, plan.aliases) == 'primitive':
                        result.append(Detyper(make_wrap_intent(assign, node, [Arg(None, None, wrap_order=1)], node.name)))
                elif (
                    isinstance(assign.value, ast.Constant)
                    and isinstance(assign.value.value, (int, float, bool))
                    and not isinstance(assign.value.value, bool)
                ):
                    target_typ = primitive_context_locals[target.id]
                    result.append(Detyper(make_wrap_intent(assign, node, [Arg(None, target_typ, wrap_order=0), Arg(None, None, wrap_order=1)], node.name)))

    return result


def generate_tasks_return_definition(
    node: FunctionDef,
    plan: PlanData,
) -> list[Detyper]:
    info = _detyped_info(node, plan)
    if info is None:
        if not _has_inline(node) or plan.selected_annotation_ids is None:
            return []
        info = plan.funcs.get(node.name)
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
        if not _has_inline(node) or plan.selected_annotation_ids is None:
            return []
        info = plan.funcs.get(node.name)
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
            if isinstance(ret_typ, ast.Name) and ret_typ.id == 'cbool':
                for boolop in ast.walk(caller):
                    if not isinstance(boolop, ast.BoolOp):
                        continue
                    if not any(value is call for value in boolop.values):
                        continue
                    caller_owner = plan.func_classes.get(caller.detyping_id)
                    caller_local_types = fact_local_class_types(caller, plan)
                    for value in boolop.values:
                        if isinstance(value, ast.Compare):
                            operands = [value.left] + list(value.comparators)
                            has_primitive_operand = any(
                                (isinstance(op, ast.Attribute) and primitive_field_read_type(op, owner_class=caller_owner, local_types=caller_local_types, plan=plan) is not None)
                                or (isinstance(op, ast.Call) and isinstance(op.func, ast.Name) and classify_type(ast.Name(id=op.func.id, ctx=ast.Load()), plan.aliases) == 'primitive')
                                for op in operands
                            )
                            if has_primitive_operand:
                                result.append(Detyper(make_wrap_intent(value, caller, [Arg(None, ast.Name(id='cbool', ctx=ast.Load()), wrap_order=0)], caller.name)))

    return result
