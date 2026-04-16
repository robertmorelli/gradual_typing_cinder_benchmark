"""Pure detyping pipeline with no benchmark execution side effects."""

from __future__ import annotations

import ast
from ast import Module
from dataclasses import dataclass
from functools import reduce
from pathlib import Path

from .ast_utils import all_function_defs, all_function_uses, all_method_uses
from .generators import (
    generate_tasks_body,
    generate_tasks_params_calls,
    generate_tasks_params_definition,
    generate_tasks_return_calls,
    generate_tasks_return_definition,
)
from .plan_data import build_plan_data
from .tasks import Detyper

Permutation = tuple[bool, ...]
GuideType = dict[str, bool]


@dataclass(frozen=True)
class DetypedProgram:
    perm: Permutation
    perm_hex: str
    source: str


def perm_name(perm: Permutation) -> str:
    if not perm:
        return '0x0'
    return hex(int(''.join(str(int(bit)) for bit in perm), 2))


def _convert_sentinel_ann_assigns(body: list[ast.stmt]) -> list[ast.stmt]:
    """Replace AnnAssign(annotation=None) sentinels with plain Assign nodes."""
    result: list[ast.stmt] = []
    for stmt in body:
        if isinstance(stmt, ast.AnnAssign) and stmt.annotation is None:
            if stmt.value is not None:
                result.append(ast.Assign(
                    targets=[stmt.target],
                    value=stmt.value,
                    lineno=stmt.lineno,
                    col_offset=stmt.col_offset,
                ))
            continue
        result.append(stmt)
    return result


def _post_process(module: Module) -> None:
    """Normalize sentinel nodes across every statement list in the module."""
    for node in ast.walk(module):
        if hasattr(node, 'body') and isinstance(node.body, list):
            node.body = _convert_sentinel_ann_assigns(node.body)
        for attr in ('orelse', 'finalbody', 'handlers'):
            value = getattr(node, attr, None)
            if isinstance(value, list):
                if value and isinstance(value[0], list):
                    continue
                setattr(node, attr, _convert_sentinel_ann_assigns(value))


def _inject_static_imports(module: Module) -> None:
    """Import cast/box from __static__ if the transformed module now needs them."""
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
    for index, stmt in enumerate(module.body):
        if isinstance(stmt, (ast.Import, ast.ImportFrom)):
            insert_idx = index + 1

    new_import = ast.ImportFrom(
        module='__static__',
        names=[ast.alias(name=name) for name in sorted(needed)],
        level=0,
    )
    ast.fix_missing_locations(new_import)
    module.body.insert(insert_idx, new_import)


def build_detyped_program(
    source: str,
    perm: Permutation,
    fun_names: list[str],
) -> DetypedProgram:
    """Apply the pure detyping transform for one permutation."""
    tree = ast.parse(source)
    module = tree

    defs = all_function_defs(tree)
    plan_names = {f.name for f in defs}
    func_uses = all_function_uses(tree, plan_names)
    method_uses = all_method_uses(tree, plan_names)

    guide: GuideType = dict(zip(fun_names, perm))
    plan = build_plan_data(module, defs, guide)

    all_detypers: list[Detyper] = []
    for fdef in defs:
        all_detypers += generate_tasks_params_definition(fdef, plan)
        all_detypers += generate_tasks_params_calls(fdef, plan, func_uses, method_uses, module)
        all_detypers += generate_tasks_body(fdef, plan)
        all_detypers += generate_tasks_return_definition(fdef, plan)
        all_detypers += generate_tasks_return_calls(fdef, plan, func_uses, method_uses)

    detyper = reduce(lambda left, right: left + right, all_detypers, Detyper())
    detyper.execute()

    _post_process(module)
    _inject_static_imports(module)
    ast.fix_missing_locations(tree)

    return DetypedProgram(
        perm=perm,
        perm_hex=perm_name(perm),
        source=ast.unparse(tree),
    )


def write_detyped_program(
    program: DetypedProgram,
    output_dir: Path,
    source_stem: str,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    out_file = output_dir / f'{source_stem}_{program.perm_hex}.py'
    out_file.write_text(program.source, encoding='utf-8')
    return out_file
