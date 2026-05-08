"""Stage 2: build detyper_map bundles from ast_data metadata.

Small cave rule: stage 1 finds facts, policy table says what to do, this file
turns place/action pairs into concrete intents.
"""

from __future__ import annotations

import ast

from .ast_data import AstData, ast_from_data
from .kind_context_policy import Action, Place, policy_for
from .intent_types import Arg, intent_to_json, make_preserve_argument_mutations_intent, make_remove_annotation_intent, make_wrap_intent
from .intent_unifiers import IntentSet


def _type_expr(src: str | None) -> ast.expr | None:
    if not src:
        return None
    try:
        parsed = ast.parse(src, mode='eval')
        return parsed.body if isinstance(parsed, ast.Expression) else None
    except SyntaxError:
        return None


def _wrap_args(action: Action, typ: ast.expr | None) -> list[Arg]:
    if action == Action.WRAP_RUNTIME_TYPE:
        return [Arg(None, typ, wrap_order=0)]
    if action == Action.WRAP_BOX:
        return [Arg(None, None, wrap_order=1)]
    if action == Action.WRAP_RUNTIME_TYPE_THEN_BOX:
        return [Arg(None, typ, wrap_order=0), Arg(None, None, wrap_order=1)]
    return []


def _annotation_context(node: ast.AST, tree: ast.AST) -> ast.AST:
    func_id = getattr(node, 'detyping_enclosing_function_id', None)
    if func_id is not None:
        return tree.detyping_node_index[func_id]
    return tree


def _func_name(context: ast.AST) -> str:
    return context.name if isinstance(context, ast.FunctionDef) else '<module>'


def _places(annotation: ast.AST, rec: dict, tree: ast.AST) -> dict[Place, list[ast.AST]]:
    places: dict[Place, list[ast.AST]] = {Place.ANNOTATION_SITE: [annotation]}
    if isinstance(annotation, ast.AnnAssign) and annotation.value is not None:
        places[Place.ANNOTATED_VALUE] = [annotation.value]

    function_id = rec.get('function_id')
    if rec.get('context') in {'function_return_annotation', 'method_return_annotation'} and function_id is not None:
        return_ids = tree.detyping_indexes.get('returns_by_function', {}).get(str(function_id), [])
        if return_ids:
            places[Place.RETURN_VALUES] = [tree.detyping_node_index[int(node_id)] for node_id in return_ids]
        function_call_ids = tree.detyping_indexes.get('function_uses_by_def', {}).get(str(function_id), [])
        if function_call_ids:
            places[Place.FUNCTION_CALL_SITES] = [tree.detyping_node_index[int(node_id)] for node_id in function_call_ids]
        method_call_ids = tree.detyping_indexes.get('method_uses_by_def', {}).get(str(function_id), [])
        if method_call_ids:
            places[Place.METHOD_CALL_SITES] = [tree.detyping_node_index[int(node_id)] for node_id in method_call_ids]

    # Local read links for annotated names/params. Pyright links first, lexical fallback.
    binding_id = None
    if isinstance(annotation, ast.arg):
        for bid, binding in tree.detyping_indexes.get('variables', {}).get('bindings', {}).items():
            if binding.get('node_id') == annotation.detyping_id:
                binding_id = bid
                break
    elif isinstance(annotation, ast.AnnAssign) and isinstance(annotation.target, ast.Name):
        for bid, binding in tree.detyping_indexes.get('variables', {}).get('bindings', {}).items():
            if binding.get('node_id') == annotation.target.detyping_id:
                binding_id = bid
                break
    if binding_id is not None:
        ids = tree.detyping_indexes.get('variables', {}).get('loads_by_binding', {}).get(str(binding_id), [])
        places[Place.LOCAL_READS] = [tree.detyping_node_index[int(node_id)] for node_id in ids]

    if isinstance(annotation, ast.AnnAssign) and isinstance(annotation.target, ast.Name) and rec.get('context', '').startswith('module_global_'):
        global_reads: list[ast.AST] = []
        for bid, binding in tree.detyping_indexes.get('globals', {}).get('bindings', {}).items():
            if binding.get('node_id') == annotation.target.detyping_id:
                ids = tree.detyping_indexes.get('globals', {}).get('uses_by_binding', {}).get(str(bid), [])
                global_reads = [tree.detyping_node_index[int(node_id)] for node_id in ids]
                break
        if global_reads:
            places[Place.MODULE_GLOBAL_READS] = global_reads

    reassign_ids = tree.detyping_indexes.get('reassign_rhs_by_annotation', {}).get(str(annotation.detyping_id), [])
    if reassign_ids:
        places[Place.REASSIGN_RHS] = [tree.detyping_node_index[int(node_id)] for node_id in reassign_ids]

    field_reassign_ids = tree.detyping_indexes.get('field_reassign_rhs_by_annotation', {}).get(str(annotation.detyping_id), [])
    if field_reassign_ids:
        places[Place.FIELD_REASSIGN_RHS] = [tree.detyping_node_index[int(node_id)] for node_id in field_reassign_ids]
    field_read_ids = tree.detyping_indexes.get('field_reads_by_annotation', {}).get(str(annotation.detyping_id), [])
    if field_read_ids:
        places[Place.FIELD_READS] = [tree.detyping_node_index[int(node_id)] for node_id in field_read_ids]
    override_ids = tree.detyping_indexes.get('override_family_annotations_by_annotation', {}).get(str(annotation.detyping_id), [])
    if override_ids:
        places[Place.OVERRIDE_FAMILY_ANNOTATION_SITES] = [tree.detyping_node_index[int(node_id)] for node_id in override_ids]

    call_arg_ids = tree.detyping_indexes.get('call_args_by_param_annotation', {}).get(str(annotation.detyping_id), [])
    if call_arg_ids:
        places[Place.CALL_ARG_TO_DETYPED_PARAM] = [tree.detyping_node_index[int(node_id)] for node_id in call_arg_ids]
    call_args_by_kind = tree.detyping_indexes.get('call_args_by_param_annotation_and_arg_kind', {}).get(str(annotation.detyping_id), {})
    scalar_arg_ids = call_args_by_kind.get('cinder_scalar', [])
    if scalar_arg_ids:
        places[Place.CALL_ARG_TO_DETYPED_PARAM_FROM_CINDER_SCALAR] = [tree.detyping_node_index[int(node_id)] for node_id in scalar_arg_ids]
    object_arg_ids = call_args_by_kind.get('python_user_object', [])
    if object_arg_ids:
        places[Place.CALL_ARG_TO_DETYPED_PARAM_FROM_PYTHON_OBJECT] = [tree.detyping_node_index[int(node_id)] for node_id in object_arg_ids]

    call_result_ids = tree.detyping_indexes.get('call_results_by_return_annotation', {}).get(str(annotation.detyping_id), [])
    if call_result_ids:
        places[Place.CALL_RESULT_FROM_DETYPED_RETURN] = [tree.detyping_node_index[int(node_id)] for node_id in call_result_ids]
    return places


def build_detyper_map_from_ast_data(ast_data: AstData, annotation_ids: list[str] | None = None, target_kind: str = 'dynamic_any') -> dict:
    tree = ast_from_data(ast_data)
    annotations = tree.detyping_indexes.get('annotations', {})
    if annotation_ids is None:
        annotation_ids = [str(item) for item in sorted(int(key) for key in annotations)]

    def add_annotation_policy(detyper: IntentSet, annotation_id: str) -> None:
        rec = annotations.get(str(annotation_id))
        if rec is None:
            return
        node = tree.detyping_node_index[int(annotation_id)]
        context = _annotation_context(node, tree)
        type_src = rec.get('resolved_type_src')
        annotation_src = rec.get('annotation_src')
        if annotation_src and ('|' in annotation_src or annotation_src.startswith(('Optional[', 'Union['))):
            type_src = annotation_src
        typ = _type_expr(type_src)
        context_name = _func_name(context)
        detyper.add(make_remove_annotation_intent(node, context, [Arg(None, None)], context_name))
        places = _places(node, rec, tree)
        policy = policy_for(rec['context'], rec['type_kind'], target_kind)
        for place, actions in policy.items():
            for target in places.get(place, []):
                for action in actions:
                    if action == Action.REMOVE_ANNOTATION:
                        detyper.add(make_remove_annotation_intent(target, _annotation_context(target, tree), [Arg(None, None)], _func_name(_annotation_context(target, tree))))
                        continue
                    if action == Action.PRESERVE_ARGUMENT_MUTATIONS:
                        target_context = _annotation_context(target, tree)
                        detyper.add(make_preserve_argument_mutations_intent(target, target_context, [Arg(None, typ)], _func_name(target_context)))
                        continue
                    if wrap_args := _wrap_args(action, typ):
                        target_context = _annotation_context(target, tree)
                        detyper.add(make_wrap_intent(target, target_context, wrap_args, _func_name(target_context)))

    bundles: dict[str, list[dict]] = {}
    sync_groups = tree.detyping_indexes.get('annotation_sync_groups', {})
    for annotation_id in annotation_ids:
        if annotations.get(str(annotation_id)) is None:
            bundles[str(annotation_id)] = []
            continue
        detyper = IntentSet()
        group_ids = sync_groups.get(str(annotation_id), [int(annotation_id)])
        for group_annotation_id in group_ids:
            add_annotation_policy(detyper, str(group_annotation_id))
        bundles[str(annotation_id)] = [intent_to_json(intent) for intent in detyper.intentions()]

    return {'version': 2, 'target_kind': target_kind, 'annotation_ids': annotation_ids, 'bundles': bundles}
