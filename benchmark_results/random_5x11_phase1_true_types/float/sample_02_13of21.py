from __future__ import annotations
from __static__ import box, cast
from math import sin, cos, sqrt
from __static__ import CheckedList, inline
from typing import final
import time
'\nbg:\n- add `ITERATIONS` constant\n- remove `main` function\n- add missing type annotations\n- replace `xrange` with `range`\n- remove unused imports\n'

@final
class Point(object):

    def __init__(self: Point, i: float):
        x: float = sin(i)
        self.x = x
        self.y: float = cos(i) * 3
        self.z: float = x * x / 2

    def normalize(self: Point):
        x = self.x
        y = self.y
        z = self.z
        norm = sqrt(x * x + y * y + z * z)
        self.x /= norm
        self.y /= norm
        self.z /= norm

    def maximize(self: Point, other):
        self.x = self.x if self.x > cast(Point, other).x else cast(Point, other).x
        self.y = self.y if self.y > cast(Point, other).y else cast(Point, other).y
        self.z = self.z if self.z > cast(Point, other).z else cast(Point, other).z
        return cast(Point, self)

def maximize_all(points) -> Point:
    next = cast(Point, cast(CheckedList[Point], points)[0])
    for p in cast(CheckedList[Point], points)[1:]:
        next = cast(Point, next.maximize(p))
    return next

def normal_point(i: int):
    p = Point(float(i))
    p.normalize()
    return cast(Point, p)

@inline
def benchmark(n: int):
    return cast(Point, maximize_all(CheckedList[Point](map(normal_point, range(n)))))
POINTS: int = 200000
if __name__ == '__main__':
    start_time = time.time()
    benchmark(POINTS)
    end_time = time.time()
    runtime = end_time - start_time
    print(runtime)