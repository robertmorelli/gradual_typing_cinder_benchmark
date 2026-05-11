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

def foo(a: int64, b: int64, c: int64, d) -> None:
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))
    bar(box(int64(a)), b, box(int64(c)))

def bar(a, b: int64, c):
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))
    baz(a, box(int64(b)))

def baz(a, b) -> None:
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))
    quux(int64(a))

def quux(a: int64):
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

def qux():
    pass

def test_calls():
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    foo(1, 2, 3, 4)
    return
if __name__ == '__main__':
    startTime = time.time()
    test_calls()
    endTime = time.time()
    runtime = endTime - startTime
    print(runtime)