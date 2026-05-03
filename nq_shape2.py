from __static__ import int64, box, clen, Array

def f(pool: Array[int64], _r=-1):
    r = box(int64(_r))
    n = clen(pool)
    if int64(r) == -1:
        r = box(n)
    return r
f(Array[int64](0))
