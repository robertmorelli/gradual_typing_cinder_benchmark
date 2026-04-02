"""Prepare transformed source artifacts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .backends import get_backend
from .core.types import DetypedProgram, Permutation


@dataclass(frozen=True)
class SourceArtifactSet:
    source_path: Path
    source: str
    variant_names: list[str]
    output_dir: Path
    source_stem: str
    backend_name: str


def load_source_artifacts(
    source_path: Path,
    output_dir: Path | None = None,
    backend_name: str = 'cinder',
) -> SourceArtifactSet:
    backend = get_backend(backend_name)
    source = source_path.read_text(encoding='utf-8')
    return SourceArtifactSet(
        source_path=source_path,
        source=source,
        variant_names=backend.detypable_function_names(source),
        output_dir=output_dir or source_path.parent,
        source_stem=source_path.stem,
        backend_name=backend_name,
    )


def build_source_variant(artifacts: SourceArtifactSet, variant: Permutation) -> DetypedProgram:
    backend = get_backend(artifacts.backend_name)
    return backend.build_detyped_program(artifacts.source, variant, artifacts.variant_names)


def write_source_variant(artifacts: SourceArtifactSet, program: DetypedProgram) -> Path:
    backend = get_backend(artifacts.backend_name)
    return backend.write_detyped_program(program, artifacts.output_dir, artifacts.source_stem)
