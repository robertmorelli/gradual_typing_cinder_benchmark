"""Pure Tree-sitter detyping pipeline for the Cinder backend."""

from __future__ import annotations

from pathlib import Path

from ..core.types import DetypedProgram, Permutation, perm_name
from .ast_utils import (
    all_function_defs,
    import_insert_byte,
    imported_static_names,
    parse_source,
    root_function_defs,
)
from .plan_data import build_plan_data
from .tasks import Detyper
from .unparse import Edit, unparse

GuideType = dict[str, bool]


def build_detyped_program(
    source: str,
    perm: Permutation,
    fun_names: list[str],
) -> DetypedProgram:
    root = parse_source(source)
    defs = all_function_defs(root, source)
    guide: GuideType = dict(zip(fun_names, perm))
    plan = build_plan_data(defs, guide)
    detyper = Detyper.from_source(source, root, defs, plan)

    edits: list[Edit] = []
    for info in root_function_defs(defs):
        target = info.node.parent if info.node.parent is not None and info.node.parent.type == 'decorated_definition' else info.node
        edits.append(Edit(
            start_byte=target.start_byte,
            end_byte=target.end_byte,
            replacement=detyper.rewrite_top_level(target),
        ))

    insert_at = import_insert_byte(source, root)
    existing_static_imports = imported_static_names(source, root)
    required_imports = [
        name
        for name in ('box', 'cast')
        if getattr(detyper, f'requires_{name}', False) and name not in existing_static_imports
    ]
    inserted_chunks: list[str] = []
    if required_imports:
        inserted_chunks.append(f"from __static__ import {', '.join(sorted(required_imports))}\n")
    if detyper.wrapper_defs:
        inserted_chunks.extend(wrapper + '\n' for wrapper in reversed(detyper.wrapper_defs))
    if inserted_chunks:
        edits.append(Edit(start_byte=insert_at, end_byte=insert_at, replacement=''.join(inserted_chunks)))

    return DetypedProgram(
        perm=perm,
        perm_hex=perm_name(perm),
        source=unparse(source, edits),
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
