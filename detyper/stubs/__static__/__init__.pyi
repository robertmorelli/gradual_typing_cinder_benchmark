"""Type stubs for cinder's `__static__` primitives, vendored for pyright.

Cinder's own first-party stubs (`cinder_env/cinder/cinderx/cinder_stubs/`)
intentionally don't model `int64`, `cbool`, `cast`, `box`, `CheckedList`, etc.
as real types because cinder's static-python compiler handles them directly.
Pyright needs them to be real classes/functions to reason about source written
against the `from __static__ import ...` API.

This file is consumed by pyright via a stub-path configuration. It is never
imported at runtime (the actual runtime lives in cinder's PythonLib/__static__).
"""

from typing import Any, Generic, Iterable, Iterator, Mapping, TypeVar, overload

_T = TypeVar('_T')
_K = TypeVar('_K')
_V = TypeVar('_V')


# ---------------------------------------------------------------------------
# Primitive numeric types.
# ---------------------------------------------------------------------------

class int64(int): ...
class int32(int): ...
class int16(int): ...
class int8(int): ...
class uint64(int): ...
class uint32(int): ...
class uint16(int): ...
class uint8(int): ...
class double(float): ...
class float64(float): ...
class float32(float): ...
class cbool(int): ...


# ---------------------------------------------------------------------------
# Typed containers.
# ---------------------------------------------------------------------------

class CheckedList(list[_T], Generic[_T]):
    def __init__(self, items: Iterable[_T] = ...) -> None: ...


class CheckedDict(dict[_K, _V], Generic[_K, _V]):
    def __init__(self, items: Mapping[_K, _V] = ...) -> None: ...


# Lowercase aliases used internally by cinder.
chklist = CheckedList
chkdict = CheckedDict


# ---------------------------------------------------------------------------
# Type-narrowing and boxing primitives.
# ---------------------------------------------------------------------------

@overload
def cast(typ: type[_T], val: object) -> _T: ...
@overload
def cast(typ: Any, val: object) -> Any: ...

def box(val: object) -> object: ...
def unbox(val: object) -> object: ...
def clen(c: object) -> int: ...


# ---------------------------------------------------------------------------
# Decorators / class markers.
# ---------------------------------------------------------------------------

def inline(f: _T) -> _T: ...
def final(f: _T) -> _T: ...
def dynamic_return(f: _T) -> _T: ...

class StaticGeneric(Generic[_T]): ...
