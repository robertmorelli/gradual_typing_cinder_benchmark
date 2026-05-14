"""SQLite-backed middle pipeline: annotations + places + policy -> intents.

Replaces the dict-based bundle_builder + IntentSet annihilation. Type info is
stored in a per-node lookup table (`node_types`) instead of being carried on
each intent row, so intents are pure (kind, location_id, affinity).

The output JSON shape matches what `pipeline.build_detyper_map_from_ast_data`
used to produce, with two changes:
  - bundles[*][i] no longer have 'typ' or 'nonnull_typ' fields.
  - The top-level dict carries a 'node_types' field: { node_id (str) -> typ_src }.
"""

from __future__ import annotations

import re
import sqlite3
from typing import Any

from .ast_data import AstData, ast_from_data
from .kind_context_policy import Action, POLICY, Place, affinity_for_place


# Match pyright LSP hover headers like:
#   "(constant) NORMAL: Strength"
#   "(variable) edits: CheckedList[UrnaryConstraint]"
#   "(parameter) mark: int64"
#   "(attribute) self.strength: int64"
#   "(field) ...: T"
#   "(method) Foo.bar(...) -> RET"
#   "(function) baz(...) -> RET"
_HOVER_TYPED_RE = re.compile(
    r'^\((?:constant|variable|parameter|attribute|field|property|argument|symbol)\)\s+'
    r'(?:[\w.]+):\s*(?P<typ>[^\n]+?)\s*$'
)
_HOVER_RETURN_RE = re.compile(r'->\s*(?P<typ>[^\n]+?)\s*(?:\n|$)')


def _extract_typ_src(hover: str | None) -> str | None:
    """Pull a parseable type-expression source from a pyright hover string."""
    if not hover:
        return None
    first = hover.lstrip().split('\n', 1)[0].strip()
    m = _HOVER_TYPED_RE.match(first)
    if m:
        return m.group('typ').strip()
    # "class Foo(...)" -- the expression is the class itself; use the bare name.
    m = re.match(r'^class\s+(?P<name>\w+)', first)
    if m:
        return m.group('name')
    # Callable: "(function|method) name(...) -> RET" -- use the return type.
    m = _HOVER_RETURN_RE.search(hover)
    if m:
        return m.group('typ').strip()
    return None


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------

_SCHEMA = """
CREATE TABLE annotations (
    id          INTEGER PRIMARY KEY,
    context     TEXT NOT NULL,
    type_kind   TEXT NOT NULL,
    typ_src     TEXT,
    nonnull_typ_src TEXT
);
CREATE TABLE places (
    annotation_id INTEGER NOT NULL,
    place         TEXT NOT NULL,
    node_id       INTEGER NOT NULL
);
CREATE INDEX idx_places_ann ON places(annotation_id);
CREATE TABLE policy (
    context     TEXT NOT NULL,
    source_kind TEXT NOT NULL,
    target_kind TEXT NOT NULL,
    place       TEXT NOT NULL,
    action      TEXT NOT NULL
);
CREATE INDEX idx_policy_lookup ON policy(context, source_kind, target_kind, place);
CREATE TABLE sync_groups (
    annotation_id INTEGER NOT NULL,
    member_id     INTEGER NOT NULL
);
CREATE TABLE node_types (
    node_id INTEGER PRIMARY KEY,
    typ_src TEXT,
    nonnull_typ_src TEXT
);
CREATE TABLE intents (
    rowid_pk      INTEGER PRIMARY KEY AUTOINCREMENT,
    annotation_id INTEGER NOT NULL,
    location_id   INTEGER NOT NULL,
    kind          TEXT NOT NULL,
    affinity      TEXT
);
"""


# ---------------------------------------------------------------------------
# Action -> concrete intent kind
# ---------------------------------------------------------------------------

_PRIMITIVE_TYPE_KINDS = frozenset({'cinder_scalar'})  # primitive numerics
_CHECKED_CONTAINER_TYPE_KINDS = frozenset({'cinder_checked_container'})


def _resolve_kind(action: str, type_kind: str) -> str | None:
    """Given a POLICY action + the annotation's source type_kind, pick a concrete intent kind."""
    if action == Action.REMOVE_ANNOTATION:
        return 'remove_annotation'
    if action == Action.REWRITE_PARAM_BINDING:
        return 'rewrite_param_binding'
    if action == Action.UNWRAP_CHECKED_RETURN_VALUE:
        return 'unwrap_checked_return_value'
    if action == Action.UNWRAP_BOX:
        return 'unbox_wrap'
    if action == Action.WRAP_BOX:
        return 'box_wrap'
    if action == Action.WRAP_CONSTRUCTOR:
        return 'constructor_wrap'
    if action == Action.WRAP_CAST:
        return 'cast_wrap'
    if action == Action.WRAP_NONNULL_RUNTIME_TYPE:
        return 'cast_wrap'  # nonnull goes through cast; type chosen from nonnull_typ_src by apply
    if action == Action.WRAP_RUNTIME_TYPE:
        if type_kind in _PRIMITIVE_TYPE_KINDS:
            return 'primitive_wrap'
        if type_kind in _CHECKED_CONTAINER_TYPE_KINDS:
            return 'constructor_wrap'
        return 'cast_wrap'
    if action == Action.WRAP_RUNTIME_TYPE_THEN_BOX:
        if type_kind in _PRIMITIVE_TYPE_KINDS:
            return 'primitive_wrap_then_box'
        if type_kind in _CHECKED_CONTAINER_TYPE_KINDS:
            return 'constructor_wrap_then_box'
        return 'cast_wrap_then_box'
    return None


def _uses_nonnull(action: str) -> bool:
    return action == Action.WRAP_NONNULL_RUNTIME_TYPE


_WRAP_KINDS = frozenset({
    'cast_wrap', 'constructor_wrap', 'primitive_wrap',
    'cast_wrap_then_box', 'constructor_wrap_then_box', 'primitive_wrap_then_box',
    'box_wrap',
})


# ---------------------------------------------------------------------------
# Engine
# ---------------------------------------------------------------------------

class SqliteEngine:
    def __init__(self) -> None:
        self.conn = sqlite3.connect(':memory:')
        self.conn.executescript(_SCHEMA)

    def close(self) -> None:
        self.conn.close()

    # --- build ---------------------------------------------------------------

    def load_policy(self, policy_table: dict = POLICY) -> None:
        rows = []
        for context, by_source in policy_table.items():
            for source_kind, by_target in by_source.items():
                for target_kind, places in by_target.items():
                    for place, actions in places.items():
                        place_v = place.value if hasattr(place, 'value') else str(place)
                        for action in (actions or ()):
                            action_v = action.value if hasattr(action, 'value') else str(action)
                            rows.append((context, source_kind, target_kind, place_v, action_v))
        self.conn.executemany(
            'INSERT INTO policy(context, source_kind, target_kind, place, action) VALUES (?,?,?,?,?)',
            rows,
        )

    def load_ast_data(self, ast_data: AstData) -> tuple[dict, list[str]]:
        tree = ast_from_data(ast_data)
        annotations = tree.detyping_indexes.get('annotations', {})
        place_indexes = tree.detyping_indexes.get('place_records_by_annotation', {})
        sync_groups = tree.detyping_indexes.get('annotation_sync_groups', {})

        # Populate node_types from pyright (one type per node, single source of truth).
        # ast_data.nodes[node_id]['attrs']['pyright_type'] is pyright's LSP hover text,
        # which we parse with _extract_typ_src below.
        node_rows = []
        for nid_str, info in ast_data.nodes.items():
            hover = info.get('attrs', {}).get('pyright_type')
            typ_src = _extract_typ_src(hover) if hover else None
            if typ_src:
                node_rows.append((int(nid_str), typ_src, typ_src))
        if node_rows:
            self.conn.executemany(
                'INSERT OR REPLACE INTO node_types(node_id, typ_src, nonnull_typ_src) VALUES (?,?,?)',
                node_rows,
            )

        ann_rows = []
        for ann_id_str, rec in annotations.items():
            ann_rows.append((
                int(ann_id_str),
                rec.get('context', ''),
                rec.get('type_kind', ''),
                rec.get('runtime_type_src'),
                rec.get('nonnull_type_src'),
            ))
        self.conn.executemany(
            'INSERT INTO annotations(id, context, type_kind, typ_src, nonnull_typ_src) VALUES (?,?,?,?,?)',
            ann_rows,
        )

        place_rows = []
        for ann_id_str, places in place_indexes.items():
            ann_id = int(ann_id_str)
            for place_name, node_ids in places.items():
                for nid in node_ids:
                    place_rows.append((ann_id, place_name, int(nid)))
        self.conn.executemany('INSERT INTO places VALUES (?,?,?)', place_rows)

        sg_rows = []
        for ann_id_str, members in sync_groups.items():
            for m in members:
                sg_rows.append((int(ann_id_str), int(m)))
        self.conn.executemany('INSERT INTO sync_groups VALUES (?,?)', sg_rows)

        annotation_ids = [str(i) for i in sorted(int(k) for k in annotations)]
        return sync_groups, annotation_ids

    # --- emit ----------------------------------------------------------------

    def emit_intents_for_annotation(self, ann_id: int, target_kind: str) -> list[tuple[str, int, str | None, str | None, str | None]]:
        """Emit (kind, location_id, affinity, typ_src, nonnull_typ_src) tuples for one annotation."""
        # Pull the annotation's metadata.
        row = self.conn.execute(
            'SELECT context, type_kind, typ_src, nonnull_typ_src FROM annotations WHERE id=?',
            (ann_id,),
        ).fetchone()
        if row is None:
            return []
        context, type_kind, typ_src, nonnull_typ_src = row

        # remove_annotation at annotation site itself.
        results: list[tuple[str, int, str | None, str | None, str | None]] = [
            ('remove_annotation', ann_id, None, None, None)
        ]

        # Walk policy x places.
        rows = self.conn.execute(
            """
            SELECT p.place, p.node_id, pol.action
              FROM places AS p
              JOIN policy AS pol
                ON pol.context = ?
               AND pol.source_kind = ?
               AND pol.target_kind = ?
               AND pol.place = p.place
             WHERE p.annotation_id = ?
            """,
            (context, type_kind, target_kind, ann_id),
        ).fetchall()

        raw: list[tuple[str, int, str | None, str | None]] = []  # (kind, loc, affinity, typ_for_annihilate)
        for place, node_id, action in rows:
            kind = _resolve_kind(action, type_kind)
            if kind is None:
                continue
            affinity = affinity_for_place(place)
            # Type stored at node for apply-time use.
            t_src = nonnull_typ_src if _uses_nonnull(action) else typ_src
            # node_types is populated from pyright in load_ast_data, not per-emission.
            raw.append((kind, node_id, affinity, t_src))

        # Annihilate producer/consumer pairs at the same location, when their effective types match
        # and the kind matches. (Mirrors the previous IntentSet annihilation.)
        by_loc: dict[int, dict[str, tuple[str, int, str | None, str | None]]] = {}
        for entry in raw:
            kind, loc, aff, t_src = entry
            if kind not in _WRAP_KINDS or aff not in ('producer', 'consumer'):
                continue
            by_loc.setdefault(loc, {})[aff] = entry
        drop_ids: set[int] = set()
        for loc, slots in by_loc.items():
            p = slots.get('producer')
            c = slots.get('consumer')
            if p is not None and c is not None and p[3] == c[3]:
                drop_ids.add(id(p))

        # Collision check.
        seen: dict[tuple[int, str, str | None], bool] = {}
        for entry in raw:
            if id(entry) in drop_ids:
                continue
            key = (entry[1], entry[0], entry[2])
            if key in seen:
                raise RuntimeError(
                    f'Intent collision in annotation {ann_id}: two {entry[0]} '
                    f'(affinity={entry[2]}) at location_id={entry[1]}'
                )
            seen[key] = True

        for entry in raw:
            if id(entry) in drop_ids:
                continue
            # entry = (kind, loc, affinity, t_src)
            results.append((entry[0], entry[1], entry[2], entry[3], nonnull_typ_src))

        results.sort(key=lambda t: (t[1], t[2] or ''))
        return results

    def _set_node_type(self, node_id: int, typ_src: str | None, nonnull_typ_src: str | None) -> None:
        # Last write wins; annihilation handles same-type cases.
        self.conn.execute(
            'INSERT OR REPLACE INTO node_types(node_id, typ_src, nonnull_typ_src) VALUES (?,?,?)',
            (node_id, typ_src, nonnull_typ_src),
        )

    def all_node_types(self) -> dict[str, str | None]:
        rows = self.conn.execute('SELECT node_id, typ_src FROM node_types').fetchall()
        return {str(nid): typ for nid, typ in rows}


# ---------------------------------------------------------------------------
# Public API: build the detyper map JSON
# ---------------------------------------------------------------------------

def build_detyper_map(ast_data: AstData, annotation_ids: list[str] | None = None, target_kind: str = 'dynamic_any') -> dict:
    eng = SqliteEngine()
    try:
        eng.load_policy()
        sync_groups, all_ids = eng.load_ast_data(ast_data)
        if annotation_ids is None:
            annotation_ids = all_ids

        bundles: dict[str, list[dict]] = {}
        for ann_id_str in annotation_ids:
            members = sync_groups.get(str(ann_id_str), [int(ann_id_str)])
            intents: list[tuple[str, int, str | None, str | None, str | None]] = []
            for mem in members:
                intents.extend(eng.emit_intents_for_annotation(int(mem), target_kind))
            intents.sort(key=lambda t: (t[1], t[2] or ''))
            bundles[str(ann_id_str)] = [
                {'kind': k, 'location_id': loc, 'affinity': aff, 'typ_src': t, 'nonnull_typ_src': nt}
                for (k, loc, aff, t, nt) in intents
            ]

        node_types = eng.all_node_types()
        return {
            'version': 3,
            'target_kind': target_kind,
            'annotation_ids': annotation_ids,
            'annotation_sync_groups': sync_groups,
            'bundles': bundles,
            'node_types': node_types,
        }
    finally:
        eng.close()
