from __future__ import annotations
from math import sin, cos, sqrt
from __static__ import CheckedList, inline
from typing import final
import time
from __static__ import cast
'\nbg:\n- add `ITERATIONS` constant\n- remove `main` function\n- add missing type annotations\n- replace `xrange` with `range`\n- remove unused imports\n'

@final
class Point(object):

    def __init__(self: Point, i):
        x = sin(i)
        self.x: float = x
        self.y = cos(i) * 3
        self.z: float = x * x / 2

    def normalize(self):
        x = self.x
        y: float = self.y
        z: float = self.z
        norm: float = sqrt(x * x + y * y + z * z)
        self.x /= norm
        self.y /= norm
        self.z /= norm

    def maximize(self, other):
        self.x = self.x if self.x > cast(Point, other).x else cast(Point, other).x
        self.y = self.y if self.y > cast(Point, other).y else cast(Point, other).y
        self.z = self.z if self.z > cast(Point, other).z else cast(Point, other).z
        return cast(Point, self)

def maximize_all(points: CheckedList[Point]) -> Point:
    next: Point = points[0]
    for p in points[1:]:
        next = cast(Point, next.maximize(p))
    return next

def normal_point(i: int) -> Point:
    p = Point(float(i))
    p.normalize()
    return p

@inline
def benchmark(n: int):
    return cast(Point, maximize_all(CheckedList[Point](map(normal_point, range(n)))))
POINTS = 200000
if __name__ == '__main__':
    start_time = time.time()
    cast(Point, benchmark(POINTS))
    end_time = time.time()
    runtime = end_time - start_time
    print(runtime)