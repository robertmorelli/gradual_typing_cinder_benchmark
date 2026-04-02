"""Backend registry."""

from __future__ import annotations

from .cinder.backend import CINDER_BACKEND
from .core.backend import DetyperBackend

_BACKENDS: dict[str, DetyperBackend] = {
    CINDER_BACKEND.name: CINDER_BACKEND,
}


def available_backends() -> list[str]:
    return sorted(_BACKENDS.keys())


def get_backend(name: str = 'cinder') -> DetyperBackend:
    try:
        return _BACKENDS[name]
    except KeyError as exc:
        raise ValueError(f'Unknown detyper backend: {name}') from exc
