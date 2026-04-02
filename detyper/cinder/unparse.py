"""Tree-sitter-friendly source unparse helpers for Cinder Python."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from tree_sitter import Node


@dataclass(frozen=True, order=True)
class Edit:
    """A replacement applied to source[start_byte:end_byte]."""

    start_byte: int
    end_byte: int
    replacement: str

    def validate(self) -> None:
        if self.start_byte < 0 or self.end_byte < 0:
            raise ValueError('Edit byte offsets must be non-negative')
        if self.end_byte < self.start_byte:
            raise ValueError('Edit end_byte must be >= start_byte')


def node_text(source: str, node: Node) -> str:
    return source[node.start_byte:node.end_byte]


def node_edit(node: Node, replacement: str) -> Edit:
    return Edit(node.start_byte, node.end_byte, replacement)


def apply_edits(source: str, edits: Iterable[Edit]) -> str:
    ordered = sorted(edits, key=lambda e: (e.start_byte, e.end_byte))
    for edit in ordered:
        edit.validate()
    for prev, cur in zip(ordered, ordered[1:]):
        if cur.start_byte < prev.end_byte:
            raise ValueError(
                f'Overlapping edits: ({prev.start_byte}, {prev.end_byte}) and '
                f'({cur.start_byte}, {cur.end_byte})'
            )

    out = source
    for edit in reversed(ordered):
        out = out[:edit.start_byte] + edit.replacement + out[edit.end_byte:]
    return out


def unparse(source: str, edits: Iterable[Edit] = ()) -> str:
    return apply_edits(source, edits)
