"""Per-permutation pipeline."""

import ast
import subprocess
import sys
from ast import FunctionDef, Module, AST
from functools import reduce
from pathlib import Path

from .plan_data import (
    PlanData, classify_type,
    all_function_defs, all_function_uses, all_method_uses, build_plan_data,
)
from .tasks import (
    Arg, Strat, Detyper, STRAT_PRECEDENCE,
    RemoveAnnotation, ReproParam, AntiAlias, StripReturn, Wrap,
)
from .transforms import make_wrap_expr, make_box_expr
from .generators import generate_tasks_params, generate_tasks_body, generate_tasks_return

Permutation = tuple   # tuple[bool, ...]
GuideType = dict      # dict[str, bool]


def perm_name(perm: Permutation) -> str:
    if not perm:
        return '0x0'
    return hex(int("".join(str(int(b)) for b in perm), 2))


# ── Node replacement helper ───────────────────────────────────────────────────

class _SpecificNodeReplacer(ast.NodeTransformer):
    """Replace a specific AST node (by identity) with a given replacement."""

    def __init__(self, target_id: int, replacement: ast.expr):
        self.target_id = target_id
        self.replacement = replacement

    def generic_visit(self, node: AST) -> AST:
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                new_list = []
                for item in value:
                    if isinstance(item, ast.AST) and id(item) == self.target_id:
                        new_list.append(self.replacement)
                    elif isinstance(item, ast.AST):
                        new_list.append(self.visit(item))
                    else:
                        new_list.append(item)
                setattr(node, field, new_list)
            elif isinstance(value, ast.AST):
                if id(value) == self.target_id:
                    setattr(node, field, self.replacement)
                else:
                    self.visit(value)
        return node


# ── Task application ─────────────────────────────────────────────────────────

def _apply_remove_annotation(node: AST, args: list[Arg]) -> None:
    if isinstance(node, FunctionDef):
        for arg in args:
            if arg.index is None:
                node.returns = None
            else:
                if arg.index < len(node.args.args):
                    node.args.args[arg.index].annotation = None
    elif isinstance(node, ast.AnnAssign):
        node.annotation = None  # sentinel; _post_process converts to Assign


def _apply_repro_param(node: AST, args: list[Arg], plan: PlanData) -> None:
    assert isinstance(node, FunctionDef)
    prepend: list[ast.stmt] = []

    for arg in sorted(args, key=lambda a: a.index if a.index is not None else 0):
        idx = arg.index
        typ = arg.typ
        if idx is None or idx >= len(node.args.args):
            continue

        param = node.args.args[idx]
        orig_name = param.arg
        kind = classify_type(typ)

        if kind == 'checked_list':
            # Keep param name; prepend plain Assign: `name = cast(T, name)`
            param.annotation = None
            stmt: ast.stmt = ast.Assign(
                targets=[ast.Name(id=orig_name, ctx=ast.Store())],
                value=ast.Call(
                    func=ast.Name(id='cast', ctx=ast.Load()),
                    args=[typ, ast.Name(id=orig_name, ctx=ast.Load())],
                    keywords=[],
                ),
                lineno=node.lineno, col_offset=node.col_offset,
            )
        else:
            # Rename param to _name; prepend AnnAssign: `name: T = wrap(_name)`
            new_name = '_' + orig_name
            param.arg = new_name
            param.annotation = None

            src = ast.Name(id=new_name, ctx=ast.Load())
            if kind == 'primitive':
                type_name = typ.id if isinstance(typ, ast.Name) else ast.unparse(typ)
                value: ast.expr = ast.Call(
                    func=ast.Name(id=type_name, ctx=ast.Load()),
                    args=[src], keywords=[],
                )
            else:  # cast / container
                value = ast.Call(
                    func=ast.Name(id='cast', ctx=ast.Load()),
                    args=[typ, src], keywords=[],
                )

            stmt = ast.AnnAssign(
                target=ast.Name(id=orig_name, ctx=ast.Store()),
                annotation=typ,
                value=value,
                simple=1,
                lineno=node.lineno, col_offset=node.col_offset,
            )

        prepend.append(stmt)

    node.body = prepend + node.body


def _apply_anti_alias(node: AST, context: AST, args: list[Arg], module: Module) -> None:
    assert isinstance(node, ast.Call)
    mod_body = module.body

    # Insertion point: after last import
    insert_idx = 0
    for i, stmt in enumerate(mod_body):
        if isinstance(stmt, (ast.Import, ast.ImportFrom)):
            insert_idx = i + 1

    # Collect existing top-level function names for collision avoidance
    existing: set[str] = {
        s.name for s in mod_body if isinstance(s, FunctionDef)
    }

    # Determine callee name for wrapper naming
    if isinstance(node.func, ast.Name):
        callee_name = node.func.id
    elif isinstance(node.func, ast.Attribute):
        callee_name = node.func.attr
    else:
        callee_name = 'unknown'

    sorted_args = sorted(args, key=lambda a: a.index if a.index is not None else -1)
    n_args = len(node.args)

    # Name wrapper after callee + all converted arg indices
    arg_suffix = '_'.join(f'arg{a.index}' for a in sorted_args)
    base = f'_repro_{callee_name}_{arg_suffix}'
    repro_name = base
    n = 2
    while repro_name in existing:
        repro_name = f'{base}_{n}'
        n += 1

    # Build a single wrapper that converts all args and calls f
    wrapper_params = [ast.arg(arg='f')] + [ast.arg(arg=f'arg{i}') for i in range(n_args)]

    body_stmts: list[ast.stmt] = []

    # One conversion assign per arg
    for arg in sorted_args:
        idx = arg.index
        body_stmts.append(ast.Assign(
            targets=[ast.Name(id=f'_arg{idx}', ctx=ast.Store())],
            value=ast.Call(
                func=arg.typ,
                args=[ast.Name(id=f'arg{idx}', ctx=ast.Load())],
                keywords=[],
            ),
            lineno=0, col_offset=0,
        ))

    # Call f with converted args substituted in
    converted = {a.index for a in sorted_args}
    call_args = [
        ast.Name(id=(f'_arg{i}' if i in converted else f'arg{i}'), ctx=ast.Load())
        for i in range(n_args)
    ]
    body_stmts.append(ast.Assign(
        targets=[ast.Name(id='_out', ctx=ast.Store())],
        value=ast.Call(func=ast.Name(id='f', ctx=ast.Load()), args=call_args, keywords=[]),
        lineno=0, col_offset=0,
    ))

    # Mutate originals in place (anti-alias)
    for arg in sorted_args:
        idx = arg.index
        body_stmts.append(ast.Expr(value=ast.Call(
            func=ast.Attribute(
                value=ast.Name(id=f'arg{idx}', ctx=ast.Load()), attr='clear', ctx=ast.Load(),
            ),
            args=[], keywords=[],
        )))
        body_stmts.append(ast.Expr(value=ast.Call(
            func=ast.Attribute(
                value=ast.Name(id=f'arg{idx}', ctx=ast.Load()), attr='extend', ctx=ast.Load(),
            ),
            args=[ast.Name(id=f'_arg{idx}', ctx=ast.Load())],
            keywords=[],
        )))

    body_stmts.append(ast.Return(value=ast.Name(id='_out', ctx=ast.Load())))

    wrapper = FunctionDef(
        name=repro_name,
        args=ast.arguments(
            posonlyargs=[], args=wrapper_params, vararg=None,
            kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[],
        ),
        body=body_stmts,
        decorator_list=[], returns=None,
        lineno=0, col_offset=0,
    )
    ast.fix_missing_locations(wrapper)
    mod_body.insert(insert_idx, wrapper)

    # Rewrite call site once: repro_name(callee_expr, arg0, arg1, ...)
    callee_expr = node.func
    original_args = list(node.args)
    node.func = ast.Name(id=repro_name, ctx=ast.Load())
    node.args = [callee_expr] + original_args


def _apply_strip_return(node: AST) -> None:
    """Strip outer CheckedList[T](...) from a Return value."""
    assert isinstance(node, ast.Return)
    if node.value is not None:
        val = node.value
        if isinstance(val, ast.Call) and val.args:
            node.value = val.args[0]


def _apply_wrap(node: AST, context: AST, args: list[Arg]) -> None:
    # Sort: ALL indexed arg wraps before ALL whole-call wraps, then by wrap_order within each group.
    sorted_args = sorted(args, key=lambda a: (1 if a.index is None else 0, a.wrap_order))

    if isinstance(node, ast.AnnAssign):
        # index is always None here (whole-value wrap)
        # Keep the annotation so Cinder retains the static type for the variable.
        # This is critical for primitive types used in loop counters: without the
        # annotation, Cinder cannot promote literals in arithmetic (e.g. int64 + 1)
        # and produces Union[dynamic, int64] across loop iterations.
        if node.value is not None:
            for arg in sorted_args:
                node.value = make_box_expr(node.value) if arg.typ is None \
                    else make_wrap_expr(node.value, arg.typ)

    elif isinstance(node, ast.Return):
        # index is always None here
        if node.value is not None:
            for arg in sorted_args:
                node.value = make_box_expr(node.value) if arg.typ is None \
                    else make_wrap_expr(node.value, arg.typ)

    elif isinstance(node, ast.Call):
        # Two kinds of args:
        #   index is not None → wrap call.args[index] in place
        #   index is None     → wrap the whole call (external return wrap)
        for arg in sorted_args:
            if arg.index is not None:
                idx = arg.index
                if idx < len(node.args):
                    node.args[idx] = make_box_expr(node.args[idx]) if arg.typ is None \
                        else make_wrap_expr(node.args[idx], arg.typ)
            else:
                # Wrap whole call in place by mutating node fields
                orig_func = node.func
                orig_args = node.args
                orig_kw = node.keywords
                inner: ast.expr = ast.Call(func=orig_func, args=orig_args, keywords=orig_kw)
                outer = make_box_expr(inner) if arg.typ is None \
                    else make_wrap_expr(inner, arg.typ)
                if isinstance(outer, ast.Call):
                    node.func = outer.func
                    node.args = outer.args
                    node.keywords = outer.keywords

    elif isinstance(node, ast.expr):
        # Any expression (ast.Name, ast.Attribute, ast.Constant, etc.) —
        # build wrap around the original node, then replace it in context.
        # For ast.Name we create a fresh Name so the original is abandoned;
        # for all other exprs we wrap the original directly (safe because
        # _SpecificNodeReplacer never recurses into its replacement).
        if isinstance(node, ast.Name):
            inner: ast.expr = ast.Name(id=node.id, ctx=ast.Load())
        else:
            inner = node
        expr: ast.expr = inner
        for arg in sorted_args:
            expr = make_box_expr(expr) if arg.typ is None \
                else make_wrap_expr(expr, arg.typ)
        ast.copy_location(expr, node)
        _SpecificNodeReplacer(id(node), expr).visit(context)


def _apply_task(location: AST, context: AST, strat: Strat, plan: PlanData, module: Module) -> None:
    st = strat.strat_type
    if st is RemoveAnnotation:
        _apply_remove_annotation(location, strat.args)
    elif st is ReproParam:
        _apply_repro_param(location, strat.args, plan)
    elif st is AntiAlias:
        _apply_anti_alias(location, context, strat.args, module)
    elif st is StripReturn:
        _apply_strip_return(location)
    elif st is Wrap:
        _apply_wrap(location, context, strat.args)


# ── Sort key ─────────────────────────────────────────────────────────────────

def _sort_key(entry: tuple, defs: list[FunctionDef]) -> tuple:
    location, context, strat = entry
    func_name = ''
    loc_id = id(location)
    for fdef in defs:
        for child in ast.walk(fdef):
            if id(child) == loc_id:
                func_name = fdef.name
                break
        if func_name:
            break
    lineno = getattr(location, 'lineno', 0) or 0
    col_offset = getattr(location, 'col_offset', 0) or 0
    node_kind = location.__class__.__name__
    prec = STRAT_PRECEDENCE.index(strat.strat_type) if strat.strat_type in STRAT_PRECEDENCE \
        else len(STRAT_PRECEDENCE)
    return (func_name, lineno, col_offset, node_kind, prec)


# ── Post-processing ───────────────────────────────────────────────────────────

def _convert_sentinel_ann_assigns(body: list) -> list:
    """Replace AnnAssigns with annotation=None sentinel with plain Assigns."""
    result = []
    for stmt in body:
        if isinstance(stmt, ast.AnnAssign) and stmt.annotation is None:
            if stmt.value is not None:
                result.append(ast.Assign(
                    targets=[stmt.target],
                    value=stmt.value,
                    lineno=stmt.lineno,
                    col_offset=stmt.col_offset,
                ))
            # bare annotation with no value → drop
        else:
            result.append(stmt)
    return result


def _post_process(module: Module) -> None:
    """Convert AnnAssigns with annotation=None (sentinel) to plain Assigns,
    in ALL statement lists (function bodies, if/while/for/try/with bodies, etc.)."""
    for node in ast.walk(module):
        # Any node that has a 'body' list of statements
        if hasattr(node, 'body') and isinstance(node.body, list):
            node.body = _convert_sentinel_ann_assigns(node.body)
        # Also handle orelse, handlers, finalbody, etc.
        for attr in ('orelse', 'finalbody', 'handlers'):
            val = getattr(node, attr, None)
            if isinstance(val, list):
                if val and isinstance(val[0], list):
                    # handlers is list of ExceptHandler nodes, handled via body above
                    pass
                else:
                    setattr(node, attr, _convert_sentinel_ann_assigns(val))


def _inject_static_imports(module: Module) -> None:
    """Add 'from __static__ import cast, box' for any of those names that are
    used in the module but not already imported from __static__."""
    already: set[str] = set()
    for stmt in module.body:
        if isinstance(stmt, ast.ImportFrom) and stmt.module == '__static__':
            for alias in stmt.names:
                already.add(alias.asname or alias.name)

    needed: set[str] = set()
    for node in ast.walk(module):
        if isinstance(node, ast.Name) and node.id in ('cast', 'box') and node.id not in already:
            needed.add(node.id)

    if not needed:
        return

    insert_idx = 0
    for i, stmt in enumerate(module.body):
        if isinstance(stmt, (ast.Import, ast.ImportFrom)):
            insert_idx = i + 1

    new_import = ast.ImportFrom(
        module='__static__',
        names=[ast.alias(name=n) for n in sorted(needed)],
        level=0,
    )
    ast.fix_missing_locations(new_import)
    module.body.insert(insert_idx, new_import)


# ── Per-permutation pipeline ──────────────────────────────────────────────────

def run_permutation(
    source: str,
    perm: Permutation,
    fun_names: list[str],
    output_dir: Path,
    source_stem: str,
) -> dict:
    tree = ast.parse(source)
    module = tree

    defs = all_function_defs(tree)
    plan_names = {f.name for f in defs}

    func_uses = all_function_uses(tree, plan_names)
    method_uses = all_method_uses(tree, plan_names)

    guide: GuideType = {name: perm[i] for i, name in enumerate(fun_names)}
    plan = build_plan_data(defs, guide)

    all_detypers: list[Detyper] = []
    for fdef in defs:
        all_detypers += generate_tasks_params(fdef, plan, func_uses, method_uses, module)
        all_detypers += generate_tasks_body(fdef, plan, module)
        all_detypers += generate_tasks_return(fdef, plan, func_uses, method_uses, module)

    if all_detypers:
        detyper = reduce(lambda a, b: a + b, all_detypers)
        tasks = detyper.all_tasks()
        tasks.sort(key=lambda t: _sort_key(t, defs))
        for location, context, strat in tasks:
            _apply_task(location, context, strat, plan, module)

    _post_process(module)
    _inject_static_imports(module)
    ast.fix_missing_locations(tree)

    perm_hex = perm_name(perm)
    out_file = output_dir / f"{source_stem}_{perm_hex}.py"
    out_file.write_text(ast.unparse(tree), encoding='utf-8')

    cinder = Path(__file__).parent.parent / 'cinder_env' / 'bin' / 'python'
    proc = subprocess.run(
        [str(cinder), str(out_file)],
        capture_output=True, text=True,
    )

    if proc.returncode != 0:
        raise RuntimeError(
            f"permutation {perm_hex} failed (exit {proc.returncode}):\n"
            f"{proc.stderr or proc.stdout}"
        )

    return {
        'perm': perm,
        'perm_hex': perm_hex,
        'file': str(out_file),
        'returncode': proc.returncode,
        'stdout': proc.stdout,
        'stderr': proc.stderr,
    }
