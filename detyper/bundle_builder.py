"""Stage 2: turn Stage-1 place records plus policy rows into intent bundles.

KEEP THIS FILE BORING.

Threat model, per project owner: if semantic discovery logic appears in this
file, an orphanage full of children gets it.  Do not endanger the children.

Stage 1 owns discovery: which candidate edit nodes are relevant, which place
each edit node belongs in, which affinity/slot a place uses, and any per-place
facts needed by an action.  A place record's node_id is always the node the
resulting intent edits.  Places are edit locations, not parent/child relation
records.  This file must not rediscover AST relationships, classify uses, infer
special cases, retarget from a subject node to an edit node, or decide that one
index implies another.

Allowed here:
- read annotation records and Stage-1 place_records_by_annotation;
- look up policy(context, source_kind, target_kind);
- translate one policy action at one place record into one concrete intent.

If logic wants to ask "is this a slice?", "is this a module global?", "which
call argument is this?", or "what node should this place target?", that logic
belongs in ast_data.py as explicit Stage-1 data, not here.
"""

from __future__ import annotations

import ast

from .ast_data import AstData, ast_from_data
from .kind_context_policy import Action, Place, is_smoothing_action, policy_for
from .intent_types import Arg, intent_to_json, make_remove_annotation_intent, make_rewrite_param_binding_intent, make_wrap_intent
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
    if action in (Action.WRAP_RUNTIME_TYPE, Action.WRAP_NONNULL_RUNTIME_TYPE):
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


def _annotation_type(rec: dict) -> ast.expr | None:
    return _type_expr(rec.get('runtime_type_src') or rec.get('resolved_type_src') or rec.get('annotation_src'))


def _action_type(action: Action, annotation_rec: dict, place_rec: dict, default_typ: ast.expr | None) -> ast.expr | None:
    if action == Action.WRAP_NONNULL_RUNTIME_TYPE:
        return _type_expr(annotation_rec.get('nonnull_type_src')) or default_typ
    return _type_expr(place_rec.get('runtime_type_src')) or default_typ


def _make_action_intent(action: Action, edit_node: ast.AST, context: ast.AST, typ: ast.expr | None, rec: dict, place_rec: dict):
    context_name = _func_name(context)
    if action == Action.REMOVE_ANNOTATION:
        return make_remove_annotation_intent(edit_node, context, [Arg(None, None)], context_name)
    if action == Action.REWRITE_PARAM_BINDING and isinstance(edit_node, ast.arg) and isinstance(context, ast.FunctionDef):
        return make_rewrite_param_binding_intent(context, context, [Arg(rec.get('param_index'), typ)], context_name)
    if wrap_args := _wrap_args(action, typ):
        intent = make_wrap_intent(edit_node, context, wrap_args, context_name)
        intent.affinity = place_rec.get('affinity')
        intent.policy_place = place_rec.get('place')
        intent.policy_action = str(action)
        intent.smoothing = is_smoothing_action(action)
        intent.slot_key = place_rec.get('slot_key')
        intent.all_symmetric_key = place_rec.get('all_symmetric_key')
        intent.all_symmetric_total = place_rec.get('all_symmetric_total')
        return intent
    return None


def build_detyper_map_from_ast_data(ast_data: AstData, annotation_ids: list[str] | None = None, target_kind: str = 'dynamic_any') -> dict:
    tree = ast_from_data(ast_data)
    annotations = tree.detyping_indexes.get('annotations', {})
    place_records_by_annotation = tree.detyping_indexes.get('place_records_by_annotation', {})
    if annotation_ids is None:
        annotation_ids = [str(item) for item in sorted(int(key) for key in annotations)]

    def add_annotation_policy(detyper: IntentSet, annotation_id: str) -> None:
        rec = annotations.get(str(annotation_id))
        if rec is None:
            return
        annotation_node = tree.detyping_node_index[int(annotation_id)]
        annotation_context = _annotation_context(annotation_node, tree)
        typ = _annotation_type(rec)
        detyper.add(make_remove_annotation_intent(annotation_node, annotation_context, [Arg(None, None)], _func_name(annotation_context)))
        policy = policy_for(rec['context'], rec['type_kind'], target_kind)

        for place_rec in place_records_by_annotation.get(str(annotation_id), []):
            place = Place(place_rec['place'])
            edit_node = tree.detyping_node_index[int(place_rec['node_id'])]
            for action in policy.get(place, ()):
                action = Action(action)
                context = _annotation_context(edit_node, tree)
                action_typ = _action_type(action, rec, place_rec, typ)
                intent = _make_action_intent(action, edit_node, context, action_typ, rec, place_rec)
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
