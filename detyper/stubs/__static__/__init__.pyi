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

class _IntPrim(int):
    # Arithmetic on cinder primitives returns the same primitive type.
    def __add__(self, other: int, /) -> 'Self': ...   # type: ignore[override]
    def __sub__(self, other: int, /) -> 'Self': ...   # type: ignore[override]
    def __mul__(self, other: int, /) -> 'Self': ...   # type: ignore[override]
    def __floordiv__(self, other: int, /) -> 'Self': ...   # type: ignore[override]
    def __mod__(self, other: int, /) -> 'Self': ...   # type: ignore[override]
    def __and__(self, other: int, /) -> 'Self': ...   # type: ignore[override]
    def __or__(self, other: int, /) -> 'Self': ...    # type: ignore[override]
    def __xor__(self, other: int, /) -> 'Self': ...   # type: ignore[override]
    def __lshift__(self, other: int, /) -> 'Self': ...   # type: ignore[override]
    def __rshift__(self, other: int, /) -> 'Self': ...   # type: ignore[override]
    def __neg__(self) -> 'Self': ...                  # type: ignore[override]
    def __pos__(self) -> 'Self': ...                  # type: ignore[override]
    def __invert__(self) -> 'Self': ...               # type: ignore[override]
    def __lt__(self, other: int, /) -> 'cbool': ...   # type: ignore[override]
    def __le__(self, other: int, /) -> 'cbool': ...   # type: ignore[override]
    def __gt__(self, other: int, /) -> 'cbool': ...   # type: ignore[override]
    def __ge__(self, other: int, /) -> 'cbool': ...   # type: ignore[override]
    def __eq__(self, other: object, /) -> 'cbool': ...   # type: ignore[override]
    def __ne__(self, other: object, /) -> 'cbool': ...   # type: ignore[override]


class _FloatPrim(float):
    def __add__(self, other: float, /) -> 'Self': ...   # type: ignore[override]
    def __sub__(self, other: float, /) -> 'Self': ...   # type: ignore[override]
    def __mul__(self, other: float, /) -> 'Self': ...   # type: ignore[override]
    def __truediv__(self, other: float, /) -> 'Self': ...   # type: ignore[override]
    def __mod__(self, other: float, /) -> 'Self': ...   # type: ignore[override]
    def __neg__(self) -> 'Self': ...                    # type: ignore[override]
    def __pos__(self) -> 'Self': ...                    # type: ignore[override]
    def __lt__(self, other: float, /) -> 'cbool': ...   # type: ignore[override]
    def __le__(self, other: float, /) -> 'cbool': ...   # type: ignore[override]
    def __gt__(self, other: float, /) -> 'cbool': ...   # type: ignore[override]
    def __ge__(self, other: float, /) -> 'cbool': ...   # type: ignore[override]
    def __eq__(self, other: object, /) -> 'cbool': ...   # type: ignore[override]
    def __ne__(self, other: object, /) -> 'cbool': ...   # type: ignore[override]


class int64(_IntPrim): ...
class int32(_IntPrim): ...
class int16(_IntPrim): ...
class int8(_IntPrim): ...
class uint64(_IntPrim): ...
class uint32(_IntPrim): ...
class uint16(_IntPrim): ...
class uint8(_IntPrim): ...
class double(_FloatPrim): ...
class float64(_FloatPrim): ...
class float32(_FloatPrim): ...
class cbool(_IntPrim): ...


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

# Cinder's own stub provides this; preserved for full compatibility.
def native(so_path: str): ...

class StaticGeneric(Generic[_T]): ...
