"""Phase 4: read intents from sqlite, apply trivial edits, unparse."""
from __future__ import annotations

import ast
import sqlite3


# Wrap builders: (expr, typ) -> ast.expr. Each is one expression-shape edit.
def _name(s: str) -> ast.expr:
    return ast.Name(id=s, ctx=ast.Load())


def _call(func: ast.expr, *args: ast.expr) -> ast.expr:
    return ast.Call(func=func, args=list(args), keywords=[])


def _prim_name(typ: ast.expr) -> ast.expr:
    return _name(typ.id if isinstance(typ, ast.Name) else ast.unparse(typ))


def _box(e: ast.expr) -> ast.expr:
    return _call(_name('box'), e)


_BUILDERS: dict[str, callable] = {
    'box_wrap':                  lambda e, t: _box(e),
    'cast_wrap':                 lambda e, t: _call(_name('cast'), t, e) if t else _box(e),
    'constructor_wrap':          lambda e, t: _call(t, e) if t else _box(e),
    'primitive_wrap':            lambda e, t: _call(_prim_name(t), e) if t else _box(e),
    'cast_wrap_then_box':        lambda e, t: _box(_call(_name('cast'), t, e)) if t else _box(e),
    'constructor_wrap_then_box': lambda e, t: _box(_call(t, e)) if t else _box(e),
    'primitive_wrap_then_box':   lambda e, t: _box(_call(_prim_name(t), e)) if t else _box(e),
    'unbox_wrap': lambda e, t: e.args[0] if (
        isinstance(e, ast.Call) and isinstance(e.func, ast.Name) and e.func.id == 'box' and e.args
    ) else e,
}


def _typ(src: str | None) -> ast.expr | None:
    if not src:
        return None
    try:
        return ast.parse(src, mode='eval').body
    except SyntaxError:
        return None


class _Replacer(ast.NodeTransformer):
    """Swap exactly the AST node with the given Python id for `replacement`."""
    def __init__(self, target_id: int, replacement: ast.AST):
        self.target_id, self.replacement = target_id, replacement

    def generic_visit(self, node):
        for field, value in list(ast.iter_fields(node)):
            if isinstance(value, list):
                setattr(node, field, [
                    self.replacement if isinstance(c, ast.AST) and id(c) == self.target_id
                    else (self.visit(c) if isinstance(c, ast.AST) else c)
                    for c in value
                ])
            elif isinstance(value, ast.AST):
                if id(value) == self.target_id:
                    setattr(node, field, self.replacement)
                else:
                    self.visit(value)
        return node


def _index(source: str) -> tuple[ast.AST, dict[tuple[int, int], ast.AST], dict[int, ast.AST]]:
    """ast tree + (start,end) byte-range index + parent map."""
    line_starts = [0]
    for i, ch in enumerate(source):
        if ch == '\n':
            line_starts.append(i + 1)
    by_range: dict[tuple[int, int], ast.AST] = {}
    parent: dict[int, ast.AST] = {}
    tree = ast.parse(source)
    for n in ast.walk(tree):
        if getattr(n, 'lineno', None) is not None:
            by_range.setdefault(
                (line_starts[n.lineno - 1] + n.col_offset,
                 line_starts[n.end_lineno - 1] + n.end_col_offset),
                n,
            )
        for c in ast.iter_child_nodes(n):
            parent[id(c)] = n
    return tree, by_range, parent


def _remove_annotation(tree: ast.AST, node: ast.AST, parent: dict[int, ast.AST]) -> None:
    """Nullify the annotation-holding field on the parent of an annotation expression."""
    p = parent.get(id(node))
    if p is None:
        return
    if isinstance(p, ast.AnnAssign) and p.annotation is node:
        # ast.AnnAssign requires an annotation; rewrite to Assign (or drop).
        gp = parent.get(id(p))
        if p.value is None:
            if gp is not None:
                for field, value in ast.iter_fields(gp):
                    if isinstance(value, list) and p in value:
                        value.remove(p)
                        return
        else:
            repl = ast.copy_location(ast.Assign(targets=[p.target], value=p.value), p)
            if gp is not None:
                _Replacer(id(p), repl).visit(gp)
    elif isinstance(p, ast.arg) and p.annotation is node:
        p.annotation = None
    elif isinstance(p, ast.FunctionDef) and p.returns is node:
        p.returns = None


def _apply(tree: ast.AST, node: ast.AST, kind: str, typ_src: str | None, parent: dict[int, ast.AST]) -> None:
    if kind == 'remove_annotation':
        return _remove_annotation(tree, node, parent)
    if kind == 'rewrite_param_binding':
        if isinstance(node, ast.arg):
            node.annotation = None
        return
    if kind == 'unwrap_checked_return_value':
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Call) and node.value.args:
            node.value = node.value.args[0]
        return
    build = _BUILDERS.get(kind)
    if build is None:
        return
    t = _typ(typ_src)
    if isinstance(node, ast.AnnAssign):
        if node.value is not None:
            node.value = build(node.value, t)
    elif isinstance(node, ast.Return):
        if node.value is not None:
            node.value = build(node.value, t)
    elif isinstance(node, ast.Assign):
        node.value = build(node.value, t)
    elif isinstance(node, ast.expr):
        repl = ast.copy_location(build(node, t), node)
        _Replacer(id(node), repl).visit(tree)


def detype(source: str, db_path: str, perm_bits: list[bool] | None = None) -> str:
    conn = sqlite3.connect(db_path)
    conn.execute('DELETE FROM perm_selected')
    if perm_bits is None:
        conn.execute('INSERT INTO perm_selected SELECT annotation_id FROM annotations')
    else:
        ann_ids = [r[0] for r in conn.execute('SELECT annotation_id FROM annotations ORDER BY annotation_id')]
        for i, bit in enumerate(perm_bits):
            if bit and i < len(ann_ids):
                conn.execute('INSERT INTO perm_selected(annotation_id) VALUES (?)', (ann_ids[i],))
    conn.commit()

    tree, by_range, parent = _index(source)
    for kind, start, end, typ_src, _affinity in conn.execute(
        'SELECT kind, start, end, typ_src, affinity FROM selected_intents '
        'ORDER BY start, end, affinity'
    ):
        node = by_range.get((start, end))
        if node is not None:
            _apply(tree, node, kind, typ_src, parent)
    conn.close()

    ast.fix_missing_locations(tree)
    return ast.unparse(tree)
