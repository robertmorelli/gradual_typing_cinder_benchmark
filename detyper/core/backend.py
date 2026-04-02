"""Backend interfaces for dependency-injected detyping."""

from __future__ import annotations

from pathlib import Path
from typing import Protocol

from .types import DetypedProgram, Permutation


class DetyperBackend(Protocol):
    name: str

    def detypable_function_names(self, source: str) -> list[str]:
        ...

    def build_detyped_program(
        self,
        source: str,
        perm: Permutation,
        fun_names: list[str],
    ) -> DetypedProgram:
        ...

    def write_detyped_program(
        self,
        program: DetypedProgram,
        output_dir: Path,
        source_stem: str,
    ) -> Path:
        ...
