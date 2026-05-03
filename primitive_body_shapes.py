from __static__ import int64, box

def f(n: int64):
    i = 0
    while int64(i) < n + 1:
        name = 'v%s' % i
        if int64(i) == n:
            pass
        i = i + 1
    return

f(10)
