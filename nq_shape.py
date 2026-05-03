from __static__ import int64, box, Array

def f(_start:int64, _step:int64):
    start=int64(_start); step=int64(_step)
    c = box(start)
    i = box(int64(0))
    while i < 3:
        c = box(int64(c) + step)
        i = box(int64(i) + 1)
    return c
f(0,1)
