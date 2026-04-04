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

    def foo(self: 'Foo', a: int64, b: int64, c: int64, d: int64) -> None:
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))
        self.bar(box(int64(a)), box(int64(b)), box(int64(c)))

    def bar(_self, _a, _b, _c):
        self: Foo = cast(Foo, _self)
        a: int64 = int64(_a)
        b: int64 = int64(_b)
        c: int64 = int64(_c)
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

    def quux(_self, _a):
        self: Foo = cast(Foo, _self)
        a: int64 = int64(_a)
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

def test_calls():
    f = Foo()
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    f.foo(1, 2, 3, 4)
    return
if __name__ == '__main__':
    startTime = time.time()
    test_calls()
    endTime = time.time()
    runtime = endTime - startTime
    print(runtime)