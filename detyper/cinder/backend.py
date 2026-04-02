"""Cinder backend adapter implementing the core backend protocol."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ..core.backend import DetyperBackend
from ..core.types import DetypedProgram, Permutation
from .ast_utils import detypable_function_names
from .pipeline import build_detyped_program, write_detyped_program


@dataclass(frozen=True)
class CinderBackend(DetyperBackend):
    name: str = 'cinder'

    def detypable_function_names(self, source: str) -> list[str]:
        return detypable_function_names(source)

    def build_detyped_program(
        self,
        source: str,
        perm: Permutation,
        fun_names: list[str],
    ) -> DetypedProgram:
        return build_detyped_program(source, perm, fun_names)

    def write_detyped_program(
        self,
        program: DetypedProgram,
        output_dir: Path,
        source_stem: str,
    ) -> Path:
        return write_detyped_program(program, output_dir, source_stem)


CINDER_BACKEND = CinderBackend()
