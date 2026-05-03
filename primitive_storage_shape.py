from __static__ import int64, double, box
class C:
    def __init__(self):
        self.x: int64 = 3
        self.y: double = 2.0

def f():
    c = C()
    k = box(c.x)
    while k:
        i = 0
        c.x = int64(k - i)
        k = box(c.x - 1)
    m = box(c.y)
    z = 1.0 / m
    c.y = double(z)

f()
