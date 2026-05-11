"""Stage 2: dumb table join from Stage-1 indexes plus policy to minimal intents."""

from __future__ import annotations

import ast

from .ast_data import AstData, ast_from_data
from .kind_context_policy import Action, Place, affinity_for_place, policy_for
from .intent_types import intent_to_json, make_remove_annotation_intent, make_rewrite_param_binding_intent, make_wrap_intent, make_unwrap_box_intent, make_unwrap_checked_return_value_intent
from .intent_unifiers import IntentSet


def _type_expr(src: str | None) -> ast.expr | None:
    if not src:
        return None
    try:
        parsed = ast.parse(src, mode='eval')
        return parsed.body if isinstance(parsed, ast.Expression) else None
    except SyntaxError:
        return None


def _annotation_type(rec: dict) -> ast.expr | None:
    return _type_expr(rec.get('runtime_type_src'))


def _nonnull_type(rec: dict) -> ast.expr | None:
    return _type_expr(rec.get('nonnull_type_src'))


def _make_action_intent(action: Action, edit_node: ast.AST, typ: ast.expr | None, nonnull_typ: ast.expr | None, affinity: str | None):
    if action == Action.REMOVE_ANNOTATION:
        return make_remove_annotation_intent(edit_node)
    if action == Action.REWRITE_PARAM_BINDING:
        return make_rewrite_param_binding_intent(edit_node, typ=typ)
    if action == Action.WRAP_RUNTIME_TYPE:
        return make_wrap_intent(edit_node, typ=typ, nonnull_typ=nonnull_typ, affinity=affinity)  # type: ignore[arg-type]
    if action == Action.WRAP_NONNULL_RUNTIME_TYPE:
        return make_wrap_intent(edit_node, typ=nonnull_typ or typ, nonnull_typ=nonnull_typ, affinity=affinity)  # type: ignore[arg-type]
    if action == Action.WRAP_BOX:
        return make_wrap_intent(edit_node, typ=None, nonnull_typ=nonnull_typ, affinity=affinity)  # type: ignore[arg-type]
    if action == Action.WRAP_RUNTIME_TYPE_THEN_BOX:
        # Minimal intent shape cannot represent ordered multi-step wraps anymore.
        return make_wrap_intent(edit_node, typ=typ, nonnull_typ=nonnull_typ, affinity=affinity)  # type: ignore[arg-type]
    if action == Action.UNWRAP_BOX:
        return make_unwrap_box_intent(edit_node)
    if action == Action.UNWRAP_CHECKED_RETURN_VALUE:
        return make_unwrap_checked_return_value_intent(edit_node)
    return None


def build_detyper_map_from_ast_data(ast_data: AstData, annotation_ids: list[str] | None = None, target_kind: str = 'dynamic_any') -> dict:
    tree = ast_from_data(ast_data)
    annotations = tree.detyping_indexes.get('annotations', {})
    place_indexes_by_annotation = tree.detyping_indexes.get('place_records_by_annotation', {})
    if annotation_ids is None:
        annotation_ids = [str(item) for item in sorted(int(key) for key in annotations)]

    def add_annotation_policy(detyper: IntentSet, annotation_id: str) -> None:
        rec = annotations.get(str(annotation_id))
        if rec is None:
            return
        annotation_node = tree.detyping_node_index[int(annotation_id)]
        typ = _annotation_type(rec)
        nonnull_typ = _nonnull_type(rec)
        detyper.add(make_remove_annotation_intent(annotation_node))
        policy = policy_for(rec['context'], rec['type_kind'], target_kind)

        for place_name, node_ids in place_indexes_by_annotation.get(str(annotation_id), {}).items():
            place = Place(place_name)
            affinity = affinity_for_place(place)
            for node_id in node_ids:
                edit_node = tree.detyping_node_index[int(node_id)]
                for action in policy.get(place, ()):
                    intent = _make_action_intent(Action(action), edit_node, typ, nonnull_typ, affinity)
                    if intent is not None:
                        detyper.add(intent)

    bundles: dict[str, list[dict]] = {}
    sync_groups = tree.detyping_indexes.get('annotation_sync_groups', {})
    for annotation_id in annotation_ids:
        if annotations.get(str(annotation_id)) is None:
            bundles[str(annotation_id)] = []
            continue
        detyper = IntentSet()
        for group_annotation_id in sync_groups.get(str(annotation_id), [int(annotation_id)]):
            add_annotation_policy(detyper, str(group_annotation_id))
        bundles[str(annotation_id)] = [intent_to_json(intent) for intent in detyper.intentions()]

    return {'version': 2, 'target_kind': target_kind, 'annotation_ids': annotation_ids, 'annotation_sync_groups': sync_groups, 'bundles': bundles}
