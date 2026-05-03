from __static__ import int64

class C:
    def __init__(self):
        self.x: int64 = 0

def f(n: int64):
    i = 0
    c = C()
    c.x = int64(i)
    if c.x != int64(i):
        pass
    return

f(1)
