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
import __static__
from __static__ import int64
import time
from __static__ import box, cast

class Foo(object):
    __slots__ = ()

    def foo(_self, _a, _b, _c, _d):
        self: Foo = cast(Foo, _self)
        a: int64 = int64(_a)
        b: int64 = int64(_b)
        c: int64 = int64(_c)
        d: int64 = int64(_d)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)
        self.bar(a, b, c)

    def bar(self: 'Foo', a: int64, b: int64, c: int64) -> None:
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))
        self.baz(box(int64(a)), box(int64(b)))

    def baz(_self, _a, _b):
        self: Foo = cast(Foo, _self)
        a: int64 = int64(_a)
        b: int64 = int64(_b)
        self.quux(a)
        self.quux(a)
        self.quux(a)
        self.quux(a)
        self.quux(a)
        self.quux(a)
        self.quux(a)
        self.quux(a)
        self.quux(a)
        self.quux(a)
        self.quux(a)
        self.quux(a)
        self.quux(a)
        self.quux(a)
        self.quux(a)
        self.quux(a)
        self.quux(a)
        self.quux(a)
        self.quux(a)
        self.quux(a)

    def quux(self: 'Foo', a: int64) -> None:
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

    def qux(_self):
        self: Foo = cast(Foo, _self)
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