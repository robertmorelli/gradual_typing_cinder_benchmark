from __static__ import int64, box, clen, Array

def f(pool: Array[int64], _r=-1):
    r = box(int64(_r))
    n = clen(pool)
    if r == -1:
        r = box(n)
    while int64(r) > 0:
        r = box(int64(r) - 1)

f(Array[int64](0))
