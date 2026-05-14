-- detyper sqlite schema.
-- TS phase 1 writes; Python phase 4 reads.

PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

CREATE TABLE meta (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

-- Parse tree.
CREATE TABLE nodes (
    node_id   INTEGER PRIMARY KEY,        -- preorder index in TS walk
    kind      TEXT    NOT NULL,           -- pyright ParseNodeType name
    start     INTEGER NOT NULL,           -- inclusive byte offset
    end       INTEGER NOT NULL,           -- exclusive byte offset
    parent_id INTEGER REFERENCES nodes(node_id)
);
CREATE INDEX idx_nodes_range ON nodes(start, end);

-- Pyright's type per expression node. Sparse.
CREATE TABLE node_types (
    node_id INTEGER PRIMARY KEY REFERENCES nodes(node_id),
    typ_src TEXT
);

-- Annotations: every annotation site detyper can flip to dynamic.
CREATE TABLE annotations (
    annotation_id INTEGER PRIMARY KEY,
    node_id       INTEGER NOT NULL REFERENCES nodes(node_id),
    context       TEXT    NOT NULL,
    type_kind     TEXT    NOT NULL,
    typ_src       TEXT    NOT NULL
);

-- For each annotation, the AST nodes that fall into each place category.
CREATE TABLE places (
    annotation_id INTEGER NOT NULL REFERENCES annotations(annotation_id),
    place         TEXT    NOT NULL,
    node_id       INTEGER NOT NULL REFERENCES nodes(node_id),
    PRIMARY KEY (annotation_id, place, node_id)
);

-- Override-family expansion (default: each annotation is its own group).
CREATE TABLE sync_groups (
    annotation_id INTEGER NOT NULL REFERENCES annotations(annotation_id),
    member_id     INTEGER NOT NULL REFERENCES annotations(annotation_id),
    PRIMARY KEY (annotation_id, member_id)
);

-- Static policy: (context, type_kind, place) -> intent_kind.
CREATE TABLE policy (
    context     TEXT NOT NULL,
    source_kind TEXT NOT NULL,
    target_kind TEXT NOT NULL,
    place       TEXT NOT NULL,
    intent_kind TEXT NOT NULL,
    PRIMARY KEY (context, source_kind, target_kind, place, intent_kind)
);

-- Place -> affinity. Static.
CREATE TABLE affinities (
    place    TEXT PRIMARY KEY,
    affinity TEXT NOT NULL CHECK (affinity IN ('producer','consumer'))
);

-- Per-run selection (annotation ids the user wants detyped).
CREATE TABLE perm_selected (
    annotation_id INTEGER PRIMARY KEY REFERENCES annotations(annotation_id)
);

-- Phase 3 join. Apply reads this view.
CREATE VIEW intents AS
SELECT
    a.annotation_id, p.node_id, n.start, n.end,
    pol.intent_kind  AS kind,
    aff.affinity     AS affinity,
    a.typ_src        AS typ_src
FROM annotations a
JOIN places p   ON p.annotation_id = a.annotation_id
JOIN nodes  n   ON n.node_id       = p.node_id
JOIN policy pol ON pol.context     = a.context
              AND pol.source_kind  = a.type_kind
              AND pol.target_kind  = 'dynamic_any'
              AND pol.place        = p.place
LEFT JOIN affinities aff ON aff.place = p.place
UNION ALL
-- Every annotation_site gets an unconditional remove_annotation.
SELECT a.annotation_id, p.node_id, n.start, n.end,
       'remove_annotation', NULL, a.typ_src
FROM annotations a
JOIN places p ON p.annotation_id = a.annotation_id AND p.place = 'annotation_site'
JOIN nodes  n ON n.node_id = p.node_id;

CREATE VIEW selected_intents AS
SELECT DISTINCT i.*
FROM intents i
JOIN sync_groups sg ON sg.member_id     = i.annotation_id
JOIN perm_selected ps ON ps.annotation_id = sg.annotation_id;
