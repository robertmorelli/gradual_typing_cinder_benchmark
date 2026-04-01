"""Prepare transformed source artifacts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .ast_utils import detypable_function_names
from .pipeline import DetypedProgram, Permutation, build_detyped_program, write_detyped_program


@dataclass(frozen=True)
class SourceArtifactSet:
    source_path: Path
    source: str
    variant_names: list[str]
    output_dir: Path
    source_stem: str


def load_source_artifacts(source_path: Path, output_dir: Path | None = None) -> SourceArtifactSet:
    source = source_path.read_text(encoding='utf-8')
    return SourceArtifactSet(
        source_path=source_path,
        source=source,
        variant_names=detypable_function_names(source),
        output_dir=output_dir or source_path.parent,
        source_stem=source_path.stem,
    )


def build_source_variant(artifacts: SourceArtifactSet, variant: Permutation) -> DetypedProgram:
    return build_detyped_program(artifacts.source, variant, artifacts.variant_names)


def write_source_variant(artifacts: SourceArtifactSet, program: DetypedProgram) -> Path:
    return write_detyped_program(program, artifacts.output_dir, artifacts.source_stem)
