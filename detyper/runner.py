"""Per-permutation pipeline."""

import ast
import subprocess
import sys
from ast import Module
from functools import reduce
from pathlib import Path

from .plan_data import all_function_defs, all_function_uses, all_method_uses, build_plan_data
from .tasks import Detyper
from .generators import (
    generate_tasks_params_definition,
    generate_tasks_params_calls,
    generate_tasks_body,
    generate_tasks_return_definition,
    generate_tasks_return_calls,
)

Permutation = tuple   # tuple[bool, ...]
GuideType = dict      # dict[str, bool]


def perm_name(perm: Permutation) -> str:
    if not perm:
        return '0x0'
    return hex(int("".join(str(int(b)) for b in perm), 2))


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
        all_detypers += generate_tasks_params_definition(fdef, plan)
        all_detypers += generate_tasks_params_calls(fdef, plan, func_uses, method_uses, module)
        all_detypers += generate_tasks_body(fdef, plan, module)
        all_detypers += generate_tasks_return_definition(fdef, plan)
        all_detypers += generate_tasks_return_calls(fdef, plan, func_uses, method_uses)

    detyper = reduce(lambda a, b: a + b, all_detypers, Detyper())
    detyper.execute()

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
