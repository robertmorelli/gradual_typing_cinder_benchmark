from __future__ import annotations
from math import sin, cos, sqrt
from __static__ import CheckedList, inline
from typing import final
import time
from __static__ import cast
'\nbg:\n- add `ITERATIONS` constant\n- remove `main` function\n- add missing type annotations\n- replace `xrange` with `range`\n- remove unused imports\n'

@final
class Point(object):

    def __init__(self, i) -> None:
        x = sin(i)
        self.x = x
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

    def maximize(self, other: Point) -> Point:
        self.x = self.x if self.x > other.x else other.x
        self.y = self.y if self.y > other.y else other.y
        self.z = self.z if self.z > other.z else other.z
        return self

def maximize_all(points: CheckedList[Point]):
    next = cast(Point, points[0])
    for p in points[1:]:
        next = cast(Point, next).maximize(p)
    return cast(Point, next)

def normal_point(i):
    p = Point(float(i))
    p.normalize()
    return cast(Point, p)

@inline
def benchmark(n):
    return cast(Point, cast(Point, maximize_all(CheckedList[Point](map(normal_point, range(n))))))
POINTS = 200000
if __name__ == '__main__':
    start_time = time.time()
    cast(Point, benchmark(POINTS))
    end_time = time.time()
    runtime = end_time - start_time
    print(runtime)