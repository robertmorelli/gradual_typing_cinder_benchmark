# Detyper Implementation Plan

## Overview

You are implementing a detyper for Meta's Static Python (a statically typed CPython variant). The detyper takes a `.py` file written in Static Python and produces a semantically equivalent version with some or all type annotations removed and replaced with runtime casting/boxing operations at boundaries.

Read `STRAT.md` before implementing anything. It specifies every transform.

---

## Running Python

Just use `python <file>.py`. The environment is already configured.

---

## Project Structure

```
detyper/
├── plan_data.py         # PlanData, FuncInfo, type resolution
├── tasks.py             # Arg, Strat, StratType subclasses, Detyper
├── generators.py        # generate_tasks_* functions
├── transforms.py        # wrap() and reproject helpers
├── runner.py            # per-permutation pipeline
└── main.py              # CLI
```

---

## Core Data Structures

### Type Annotations

Static Python annotations are AST nodes, not runtime Python types. Use `ast.expr` (or a `TypeSpec` alias) to represent annotation types throughout. Never use runtime `type` objects for annotation values — things like `CheckedList[int64]` exist only as AST.

```python
TypeSpec = ast.expr  # alias for clarity
```

### `FuncInfo`

```python
class FuncInfo(NamedTuple):
    fun_name: str
    param_types: list[TypeSpec | None]  # positional params in order, None if unannotated
    return_type: TypeSpec | None        # None if no return annotation
    is_detyped: bool                    # from permutation guide
```

### `PlanData`

```python
class PlanData:
    funcs: dict[str, FuncInfo]   # fun_name -> FuncInfo
```

Functions are identified by name only. No class qualification. No inheritance tracking.

---

## Function Name Assumptions and Signature Merging

All functions with the same name are assumed to be related by some inheritance structure. This is the only case handled. Any other relationship between same-named functions is not supported.

When building `PlanData`, group all `FunctionDef` nodes by `fun_name` and merge into a single `FuncInfo` per name. Apply the following fatal error rules during merging:

- **Arity mismatch**: if two defs with the same name have different numbers of params, abort with a clear error.
- **Param annotation conflict**: if any param position has two non-`None` annotations that differ, abort.
- **Return annotation conflict**: if two non-`None` return annotations differ, abort.

If annotations are consistent (or one is `None` and the other is not), use the non-`None` value. If both are `None`, the merged type is `None`.

Because of this merging, `all_function_uses` and `all_method_uses` results can always be resolved to a single `FuncInfo` by name lookup.

---

## AST Visitors

Run three visitors up front to collect all node references. These are the only `ast.NodeVisitor` instances in the codebase.

```python
def all_function_defs(tree: AST) -> list[FunctionDef]
    # returns all FunctionDef nodes in the file

def all_function_uses(tree: AST) -> list[tuple[Call, FunctionDef]]
    # Call.func is Name — free function calls
    # returns (call_node, containing_functiondef_node) for every such call site

def all_method_uses(tree: AST) -> list[tuple[Call, FunctionDef]]
    # Call.func is Attribute — method calls
    # returns (call_node, containing_functiondef_node) for every such call site
```

**Unknown callees:** If a call site's callee name does not appear in `PlanData`, silently ignore it. Do not error. This covers builtins, imported functions, and any other unresolved calls. Visitors should skip unresolved names without raising.

After the visitor phase, use node references directly. Targeted local traversal within a node (e.g. finding all `Return` nodes inside a specific `FunctionDef`) is fine and expected. Avoid global re-traversal of the whole tree.

---

## Permutations

A permutation is `tuple[bool, ...]` where index `i` corresponds to `fun_names[i]` and `True` means detype that function.

```python
Permutation = tuple[bool, ...]
GuideType = dict[str, bool]   # fun_name -> is_detyped
```

`fun_names` is the sorted (alphabetical) list of all function names in the file. Alphabetical order ensures the mapping from permutation bits to functions is stable and visitor-order-independent.

Permutation naming: interpret the bool tuple as a binary number, format as hex string.

```python
def perm_name(perm: Permutation) -> str:
    return hex(int("".join(str(int(b)) for b in perm), 2))
```

---

## Task Algebra

### `Arg`

```python
class Arg(NamedTuple):
    index: int | None       # param index, or None for whole-node operations
    typ: TypeSpec | None
    wrap_order: int = 0     # for multi-layer wraps, lower = inner
```

### `Strat`

```python
class Strat:
    strat_type: type[StratType]
    args: list[Arg]

    def __add__(self, other: Strat) -> Strat:
        # assert same strat_type
        # merge and canonicalize args (see Canonicalization below)
```

### Canonicalization in `Strat.__add__`

- `RemoveAnnotation`, `ReproParam`, `AntiAlias`: deduplicate args by `(index, ast.dump(typ))`. Keep one copy of each unique arg.
- `Wrap`: deduplicate exact duplicate args by `(index, ast.dump(typ), wrap_order)`. Preserve deterministic order after dedup. Collapse idempotent repeats: `box(box(...))`, `cast(T, cast(T, ...))`, `T(T(...))` → single wrap. If incompatible wrappers remain after dedup, keep them all and let typecheck/runtime surface the issue.
- No fatal errors in `Strat.__add__`. Canonicalize and continue.

### `Detyper`

```python
class Detyper:
    tasks: dict[AST, dict[AST, dict[type[StratType], Strat]]]
    # keys: [location_node][context_node][StratType]

    def __add__(self, other: Detyper) -> Detyper:
        # 3-level dict merge, Strat.__add__ at leaves only when all 3 keys match
```

### `StratType` subclasses

`RemoveAnnotation`, `ReproParam`, `AntiAlias`, `Wrap`. Each implements:

```python
def trans(self, node: AST, context: AST, args: list[Arg], plan: PlanData) -> None:
    # mutates the AST in place — no cloning, no reparsing
```

**Mutation contract:** `trans` mutates the tree in place only. Never clone subtrees or reparse source during the apply phase. Cloning or reparsing mid-apply will invalidate other task node references and cause incorrect output.

`RemoveAnnotation` strips the annotation from a node with no runtime replacement. Used exclusively for `None`-typed annotations. No `Wrap` or `AntiAlias` is ever generated for `None`-typed params, body assignments, or returns — only `RemoveAnnotation`.

---

## Strat Precedence

When applying tasks, `StratType` ordering is fixed. Apply in this order:

```
RemoveAnnotation → ReproParam → AntiAlias → Wrap
```

Within the same `StratType`, sort alphabetically by `StratType.__name__` (all same here) then by `wrap_order` ascending (inner wraps applied before outer). This precedence is used for the final sort key and must not be changed.

---

## Task Application Order

**Task application must be fully deterministic.** Non-deterministic application will produce incorrect or inconsistent wrap ordering across runs.

Sort tasks by the following composite key before applying:

```python
(func_name, lineno, col_offset, node_kind, strat_precedence)
```

Where:
- `func_name` — name of the containing function (`""` for top-level)
- `lineno`, `col_offset` — from the location node's source position
- `node_kind` — `node.__class__.__name__`
- `strat_precedence` — integer index into the fixed precedence list above

Do not use `id(node)` as a sort key. It is not stable across runs.

---

## Task Generators

Each generator takes a single function def node and a `PlanData` and returns `list[Detyper]`. Generators produce one `Detyper` per unitary transform. The caller sums them all.

```python
def generate_tasks_params(node: FunctionDef, plan: PlanData) -> list[Detyper]
def generate_tasks_body(node: FunctionDef, plan: PlanData) -> list[Detyper]
def generate_tasks_return(node: FunctionDef, plan: PlanData) -> list[Detyper]
```

**If `plan.funcs[name].is_detyped` is False, all generators must return `[]` immediately.**

### `generate_tasks_params`

For each annotated param in the detyped function:
- If annotation is `None` type: generate a `RemoveAnnotation` task only
- For `CheckedList` params: generate a `ReproParam` task on the function node and an `AntiAlias` task on each call site node
- For all other types: generate a `ReproParam` task on the function node with `(index, typ)` and a `Wrap` task on the arg node at each call site with `(None, typ)`

### `generate_tasks_body`

For each `AnnAssign` in the function body:
- If annotation is `None` type: generate a `RemoveAnnotation` task only
- For primitive types: generate a `Wrap` task on the assignment node and `Wrap` tasks on all subsequent uses of the variable within the function body
- For `CheckedList` types: generate a `Wrap` task using the `CheckedList[T](...)` constructor form
- For container passthrough types (`Array` etc): generate a `Wrap` task using `cast(T, ...)`
- For all other types: generate a `Wrap` task using `cast(T, ...)` (see STRAT.md for full type dispatch)

### `generate_tasks_return`

For each `Return` node inside the detyped function:
- If return annotation is `None` or absent: generate a `RemoveAnnotation` task on the function node only
- For `CheckedList` return type: internal — strip the `CheckedList[T](...)` constructor from the return value. External — wrap each call site with `CheckedList[T](...)`
- For primitive return type: internal — wrap return value with `box(T(...))`. External — wrap each call site with `T(...)`
- For all other types: internal — no wrap. External — wrap each call site with `cast(T, ...)` (see STRAT.md)

---

## Helper Function Insertion (AntiAlias)

`AntiAlias.trans` generates a new top-level helper function and inserts it into the module. For `AntiAlias` tasks, `context` must be the `Module` node, not the containing `FunctionDef`.

Naming convention:
- Base name: `_repro_{callee_name}_arg{target_index}`
- Collision suffix: `_2`, `_3`, ... (check existing names in module before inserting)

Insertion point: after the last import statement in the module body. If no imports exist, insert at the top of the module body.

---

## Pipeline Per Permutation

For each permutation:

1. Parse AST from source
2. Run all three visitors on the tree to get `defs`, `uses`, and `method_uses`
3. Build `PlanData` from `defs` + permutation guide (merge signatures, abort on conflict)
4. For each function def node, call all three generators, collect all `list[Detyper]` results
5. **If `all_detypers` is empty** (no functions being detyped): skip to step 8
6. Sum all `Detyper` instances into one: `detyper = reduce(lambda a, b: a + b, all_detypers)`
7. Sort and apply tasks in deterministic order (see Task Application Order and Strat Precedence)
8. `ast.fix_missing_locations(tree)`
9. `ast.unparse(tree)` → write to `detyped_files/<original_stem>_<perm_hex>.py`
10. Run: `python detyped_files/<original_stem>_<perm_hex>.py`
11. Return result

---

## Output Files

Detyped files go to `detyped_files/` relative to the source file. Filename:

```
<original_stem>_<perm_hex>.py
```

Where `perm_hex` is the result of `perm_name()` e.g. `0x1a`.

---

## CLI

```
python main.py <benchmark_file>
  --show-perm <hex>   print transformed source for a specific permutation and exit
  --test              run fully typed and fully detyped once, print return codes and output
```

---

## Constraints and Assumptions

- Source files are UTF-8, `.py` only
- No function-inside-function, no class-inside-class, no class-inside-function
- No function name shadowing outside of inheritance
- All functions with the same name are related by inheritance — no other case is handled
- Signature merging is fatal on conflict — arity mismatch, param annotation conflict, or return annotation conflict all abort
- `None` annotations use `RemoveAnnotation` only — no `Wrap` or `AntiAlias` is ever generated for `None` cases
- Unknown call sites (callee not in `PlanData`) are silently ignored by visitors
- AST nodes are reference-stable. Node references collected by visitors remain valid through the full pipeline.
- All generators are pure (no AST mutation). Mutation only happens in `trans`.
- `trans` mutates in place only — no cloning or reparsing during apply phase
- Task application order is fully deterministic via source-stable sort keys and fixed strat precedence
