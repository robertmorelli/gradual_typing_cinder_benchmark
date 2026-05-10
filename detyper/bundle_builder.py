"""Stage 2: turn Stage-1 place records plus policy rows into intent bundles.

KEEP THIS FILE BORING.

Threat model, per project owner: if semantic discovery logic appears in this
file, an orphanage full of children gets it.  Do not endanger the children.

Stage 1 owns discovery: which nodes are relevant, which place each node belongs
in, which affinity/slot a place uses, and any per-place payload needed by an
action.  This file must not rediscover AST relationships, classify uses, infer
special cases, or decide that one index implies another.

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
from .intent_types import Arg, intent_to_json, make_preserve_argument_mutations_intent, make_remove_annotation_intent, make_rewrite_param_binding_intent, make_wrap_intent
from .intent_unifiers import IntentSet


def _type_expr(src: str | None) -> ast.expr | None:
    if not src:
        return None
    try:
        parsed = ast.parse(src, mode='eval')
        return parsed.body if isinstance(parsed, ast.Expression) else None
    except SyntaxError:
        return None


def _nonnull_type_expr(annotation_src: str | None, resolved_src: str | None) -> ast.expr | None:
    for src in (annotation_src or '', resolved_src or ''):
        if src.startswith('Final[') and src.endswith(']'):
            return _type_expr(src[len('Final['):-1])
        if src.startswith('Optional[') and src.endswith(']'):
            return _type_expr(src[len('Optional['):-1])
        if '|' in src:
            parts = [part.strip() for part in src.split('|') if part.strip() not in {'None', 'NoneType'}]
            if len(parts) == 1:
                return _type_expr(parts[0])
    return _type_expr(resolved_src) or _type_expr(annotation_src)


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
    type_src = rec.get('resolved_type_src')
    annotation_src = rec.get('annotation_src')
    if annotation_src and ('|' in annotation_src or annotation_src.startswith(('Optional[', 'Union['))):
        type_src = annotation_src
    return _type_expr(type_src)


def _action_type(action: Action, annotation_rec: dict, place_rec: dict, default_typ: ast.expr | None) -> ast.expr | None:
    if action == Action.WRAP_NONNULL_RUNTIME_TYPE:
        return _nonnull_type_expr(annotation_rec.get('annotation_src'), annotation_rec.get('resolved_type_src'))
    if Place(place_rec['place']) == Place.SUBSCRIPT_RESULTS:
        if place_rec.get('is_slice'):
            return _type_expr(place_rec.get('container_type_src')) or default_typ
        return _type_expr(place_rec.get('element_type_src')) or default_typ
    return default_typ


def _make_action_intent(action: Action, target: ast.AST, context: ast.AST, typ: ast.expr | None, rec: dict, place_rec: dict, tree: ast.AST):
    context_name = _func_name(context)
    if action == Action.REMOVE_ANNOTATION:
        return make_remove_annotation_intent(target, context, [Arg(None, None)], context_name)
    if action == Action.REWRITE_PARAM_BINDING and isinstance(target, ast.arg) and isinstance(context, ast.FunctionDef):
        return make_rewrite_param_binding_intent(context, context, [Arg(rec.get('param_index'), typ)], context_name)
    if action == Action.PRESERVE_ARGUMENT_MUTATIONS:
        call_id = place_rec.get('call_id')
        arg_index = place_rec.get('arg_index')
        if call_id is None or arg_index is None:
            return None
        return make_preserve_argument_mutations_intent(tree.detyping_node_index[int(call_id)], tree, [Arg(int(arg_index), typ)], '<module>')
    if wrap_args := _wrap_args(action, typ):
        intent = make_wrap_intent(target, context, wrap_args, context_name)
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
            target = tree.detyping_node_index[int(place_rec['node_id'])]
            context = _annotation_context(target, tree)
            for action in policy.get(place, ()):
                action = Action(action)
                action_typ = _action_type(action, rec, place_rec, typ)
                intent = _make_action_intent(action, target, context, action_typ, rec, place_rec, tree)
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
