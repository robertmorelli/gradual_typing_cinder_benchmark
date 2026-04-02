"""Core detyper types shared across language/runtime backends."""

from __future__ import annotations

from dataclasses import dataclass

Permutation = tuple[bool, ...]


@dataclass(frozen=True)
class DetypedProgram:
    perm: Permutation
    perm_hex: str
    source: str


def perm_name(perm: Permutation) -> str:
    if not perm:
        return '0x0'
    return hex(int(''.join(str(int(bit)) for bit in perm), 2))
