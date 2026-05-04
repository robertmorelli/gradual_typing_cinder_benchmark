"""Prepare transformed source artifacts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .ast_utils import detypable_annotation_ids, detypable_function_names
from .pipeline import DetypedProgram, Permutation, build_detyped_program, build_detyped_program_from_map, read_detyper_map, write_detyped_program, write_detyper_map


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
        variant_names=detypable_annotation_ids(source),
        output_dir=output_dir or source_path.parent,
        source_stem=source_path.stem,
    )


def detyper_map_path(artifacts: SourceArtifactSet) -> Path:
    return artifacts.output_dir / f'detyper_map_{artifacts.source_stem}.json'


def ensure_detyper_map(artifacts: SourceArtifactSet) -> Path:
    path = detyper_map_path(artifacts)
    if not path.exists():
        write_detyper_map(artifacts.source, path, artifacts.variant_names)
    return path


def build_source_variant(artifacts: SourceArtifactSet, variant: Permutation) -> DetypedProgram:
    path = ensure_detyper_map(artifacts)
    return build_detyped_program_from_map(artifacts.source, read_detyper_map(path), variant)


def write_source_variant(artifacts: SourceArtifactSet, program: DetypedProgram) -> Path:
    return write_detyped_program(program, artifacts.output_dir, artifacts.source_stem)
