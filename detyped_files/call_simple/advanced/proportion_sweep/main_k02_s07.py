"""Microbenchmark for function call overhead.

This measures simple function calls that are not methods, do not use varargs or
kwargs, and do not use tuple unpacking.

bg:
- annotated all parameters + return types
  the first parameter of ALL functions was untyped
- using Timer
- fixed num iterations (see bottom of file)
- removed command-line parsing
"""
import __static__
from __static__ import int64
import time
from __static__ import box

def foo(_a, _b, _c, _d):
    a: int64 = int64(_a)
    b: int64 = int64(_b)
    c: int64 = int64(_c)
    d: int64 = int64(_d)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)
    bar(a, b, c)

def bar(a: int64, b: int64, c: int64) -> None:
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)
    baz(a, b)

def baz(a: int64, b: int64) -> None:
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))
    quux(box(int64(a)))

def quux(_a):
    a: int64 = int64(_a)
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()
    qux()

def qux() -> None:
    pass

def test_calls() -> None:
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    return
if __name__ == '__main__':
    startTime = time.time()
    test_calls()
    endTime = time.time()
    runtime = endTime - startTime
    print(runtime)