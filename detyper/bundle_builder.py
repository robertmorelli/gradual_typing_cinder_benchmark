"""Stage 2: build per-annotation bundles. Now backed by sqlite_engine."""

from __future__ import annotations

from .ast_data import AstData
from .sqlite_engine import build_detyper_map as _sqlite_build


def build_detyper_map_from_ast_data(ast_data: AstData, annotation_ids: list[str] | None = None, target_kind: str = 'dynamic_any') -> dict:
    return _sqlite_build(ast_data, annotation_ids=annotation_ids, target_kind=target_kind)
