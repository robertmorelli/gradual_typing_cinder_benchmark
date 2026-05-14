# less

Things to delete from phase1.ts so the code only does its job:
  pyright tells the truth → we copy it into sqlite. Nothing in between.

## Delete

### 1. `classifyTypeKind` + `normalize` + `_CINDER_SCALARS`
Regex / string matching on a printed type expression. Pyright already gives us
a structured `Type` with a category and a class. Replace with a single function
that inspects `Type.category` and `ClassType.shared.fullName`:

```
__static__.int64 / int32 / ...           → cinder_scalar
__static__.CheckedList / CheckedDict     → cinder_checked_container
builtins.list / dict / set / Mapping     → python_container
builtins.tuple                           → python_tuple
builtins.int / float / str / bool / ...  → python_scalar
typing.Iterator / Generator / Iterable   → iterator
builtins.NoneType / Type.None            → none_only
TypeCategory.Union containing NoneType   → optional
TypeCategory.Union otherwise             → union
TypeCategory.Function                    → callable
anything else (instance class)           → python_user_object
```

No regex. No string normalization. The "kind" comes from the type itself.

### 2. `isOptionalIsh(typSrc)`
String search for `| None` / `Optional[`. The Type from pyright is a `Union`
with `NoneType` as a member, or it isn't. Inspect the structure.

### 3. `sliceText(node)` for annotation `typ_src`
We slice the source text just to store a printable annotation. Use
`evaluator.printType(t)` instead — same string, but from pyright's Type, not
from the source bytes. The source-text slice goes away.

### 4. `functionName(funcNode)`
Used to detect `__init__` for the constructor branches. Pyright knows whether
a function is a class init via its declaration flags. Read that instead of
checking `.d.name.d.value === '__init__'`. (Acceptable for now if we keep ONE
named comparison and ban the pattern elsewhere, but better gone.)

### 5. `isSelfAttribute(expr)`
String check for `expr.d.leftExpr.d.value === 'self'`. We use this to decide
whether `target.x` is a field. Pyright's declaration tells us if the symbol
belongs to a class scope; ask pyright. Or skip the check entirely — the
declaration node we record points at the field NameNode regardless.

### 6. `shapeOf(expr)` for ANNOTATED_VALUE_LITERAL vs ANNOTATED_VALUE
Checks `nodeType === Constant/List/Dict/...` to call something a "literal".
Pyright's `Type` for the expression carries `literalValue` for actual literal
types (`Literal[5]`, `Literal[None]`) and the type of a list literal is
`list[...]` already narrowed. Use the Type, not the node shape.

(Compromise: shape-vs-value is sometimes a syntactic distinction the policy
actually cares about — e.g. "RHS is a `[]` literal vs a call". If that
distinction must stay, keep shapeOf but use it only at the policy level, and
note that this is a structural property, not a type one.)

### 7. `attributeMemberName(attr)` / `nameValue(name)`
Unused once symbol resolution is the only path. The places loop no longer
needs to compare names; pyright tells us what declaration each Name refers to.

### 8. `allNameReads` / `allAttributeNodes` / `allCallNodes` / etc.
We collect these globals during a manual walk so we can iterate later. The
parse tree's preorder walk is already available; collecting + iterating is
just a worse version of "iterate once and emit places inline". Replace with
a single tree walk during the same pass that writes `nodes`.

### 9. `pyNodeByKey` / `dbNodeById` / `nodeIdByKey` / `nodeIdByStart`
Three overlapping maps from (kind, start, end) → ParseNode or node_id. One
is enough: record `nodeIdByRef = new Map<ParseNode, number>()` as we walk and
use it everywhere.

### 10. Manual `enclosingFunction(node)` / `enclosingClass(node)`
Walks `node.parent` repeatedly. Pyright's `ParseTreeUtils` already exposes
`getEnclosingClass`, `getEnclosingFunction` — use those.

### 11. The whole `annotationsByContext = db.query(...)` round-trip
We just wrote the annotations table; round-tripping through SQL to get them
back is wasteful. Keep an in-memory array as we insert and iterate that.

## Net effect
Phase 1 becomes one pass:
  1. parse + bind via pyright
  2. preorder walk, for each node:
     - insert `nodes` row
     - insert `node_types` row from `evaluator.getType(node)`
     - if node is an annotation site: classify by `Type`, insert `annotations`
  3. second walk for places: for each Name / Attribute, ask pyright for its
     declaration, look up the annotation, emit one `places` row classified
     by parent node type (the only structural check that's actually
     structural).
  4. `db.exec(policy.sql)`.

That's it. No string parsing, no name comparisons, no per-category if-trees
arguing with pyright.
