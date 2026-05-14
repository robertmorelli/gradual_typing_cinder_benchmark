"""Microbenchmark for method call overhead on types that define __slots__.

This measures simple method calls for objects with no dicts that are
predictable, do not use varargs or kwargs, and do not use tuple unpacking.
When an object has no __dict__ attribute, the JIT can optimize away most of the
attribute lookup.  This benchmark measures how well it can do that.

bg:
- annotated all parameters + return types
- using Timer
- removed command-line parsing
"""
from __static__ import box, cast
import __static__
from __static__ import int64
import time

class Foo(object):
    __slots__ = ()

    def foo(self: 'Foo', a, b, c, d) -> None:
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))
        self.bar(box(int64(a)), int64(b), box(int64(c)))

    def bar(self: 'Foo', a, b: int64, c):
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)
        self.baz(box(int64(a)), b)

    def baz(self: 'Foo', a, b: int64) -> None:
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))
        self.quux(box(int64(a)))

    def quux(self: 'Foo', a):
        self.qux()
        self.qux()
        self.qux()
        self.qux()
        self.qux()
        self.qux()
        self.qux()
        self.qux()
        self.qux()
        self.qux()
        self.qux()
        self.qux()
        self.qux()
        self.qux()
        self.qux()
        self.qux()
        self.qux()
        self.qux()
        self.qux()
        self.qux()

    def qux(self: 'Foo'):
        pass

def test_calls() -> None:
    f = Foo()
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    f.foo(box(int64(1)), box(int64(2)), box(int64(3)), box(int64(4)))
    return
if __name__ == '__main__':
    startTime = time.time()
    test_calls()
    endTime = time.time()
    runtime = endTime - startTime
    print(runtime)