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

    def foo(self, a, b, c, d):
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

    def bar(self, a, b, c):
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

    def baz(self, a, b):
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

    def quux(self, a):
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

    def qux(self):
        pass

def test_calls():
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