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
from __static__ import box, cast
import __static__
from __static__ import int64
import time

def foo(a: int64, b: int64, c, d) -> None:
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))
    bar(a, box(b), box(int64(c)))

def bar(a: int64, b, c):
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))
    baz(a, int64(b))

def baz(a: int64, b: int64) -> None:
    quux(box(a))
    quux(box(a))
    quux(box(a))
    quux(box(a))
    quux(box(a))
    quux(box(a))
    quux(box(a))
    quux(box(a))
    quux(box(a))
    quux(box(a))
    quux(box(a))
    quux(box(a))
    quux(box(a))
    quux(box(a))
    quux(box(a))
    quux(box(a))
    quux(box(a))
    quux(box(a))
    quux(box(a))
    quux(box(a))

def quux(a) -> None:
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

def test_calls():
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    foo(1, 2, box(int64(3)), box(int64(4)))
    return
if __name__ == '__main__':
    startTime = time.time()
    test_calls()
    endTime = time.time()
    runtime = endTime - startTime
    print(runtime)