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

def foo(a: int64, b, c: int64, d):
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))
    bar(box(a), int64(b), box(c))

def bar(a, b: int64, c) -> None:
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)
    baz(box(int64(a)), b)

def baz(a, b: int64) -> None:
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

def quux(a):
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
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    foo(1, box(int64(2)), 3, box(int64(4)))
    return
if __name__ == '__main__':
    startTime = time.time()
    test_calls()
    endTime = time.time()
    runtime = endTime - startTime
    print(runtime)