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
from __static__ import box

class Foo(object):
    __slots__ = ()

    def foo(self: 'Foo', a: int64, b: int64, c, d: int64) -> None:
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)
        self.bar(box(int64(a)), b, c)

    def bar(self: 'Foo', a, b: int64, c) -> None:
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))
        self.baz(int64(a), box(int64(b)))

    def baz(self, a: int64, b) -> None:
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

    def quux(self: 'Foo', a) -> None:
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

    def qux(self: 'Foo') -> None:
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