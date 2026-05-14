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

def foo(a, b, c, d):
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))
    bar(box(int64(a)), box(int64(b)), box(int64(c)))

def bar(a, b, c) -> None:
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))
    baz(int64(a), box(int64(b)))

def baz(a: int64, b):
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

def qux():
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