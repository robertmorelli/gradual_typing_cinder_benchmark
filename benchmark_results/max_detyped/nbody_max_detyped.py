"""
N-body benchmark from the Computer Language Benchmarks Game.

This is intended to support Unladen Swallow's pyperf.py. Accordingly, it has been
modified from the Shootout version:
- Accept standard Unladen Swallow benchmark options.
- Run report_energy()/advance() in a loop.
- Reimplement itertools.combinations() to work with older Python versions.

Pulled from:
http://benchmarksgame.alioth.debian.org/u64q/program.php?test=nbody&lang=python3&id=1

Contributed by Kevin Carson.
Modified by Tupteq, Fredrik Johansson, and Daniel Nanz.
"""
import __static__
from __static__ import double, CheckedList, CheckedDict, box, int64
import time
from __static__ import cast
__contact__ = 'collinwinter@google.com (Collin Winter)'
DEFAULT_ITERATIONS = 20000
DEFAULT_REFERENCE = 'sun'
PI = 3.141592653589793
SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

class Vector:

    def __init__(self, x, y, z):
        self.x = box(double(x))
        self.y = box(double(y))
        self.z = box(double(z))

    def __repr__(self):
        return f'Vector({(box(double(self.x)), box(double(self.y)), box(double(self.z)))})'

class Body:

    def __init__(self, _pos, _v, mass):
        pos = cast(Vector, _pos)
        v = cast(Vector, _v)
        self.pos = pos
        self.v = v
        self.mass = box(double(mass))

    def __repr__(self):
        return f'Body({cast(Vector, self.pos)}, {cast(Vector, self.v)}, {box(double(self.mass))})'

def combinations(l):
    l = cast(CheckedList[Body], l)
    'Pure-Python implementation of itertools.combinations(l, 2).'
    result = []
    for x in range(len(l) - 1):
        ls = CheckedList[Body](l[x + 1:])
        for y in ls:
            result.append((l[x], y))
    return result
BODIES = CheckedDict[str, Body]({'sun': Body(Vector(box(double(0.0)), box(double(0.0)), box(double(0.0))), Vector(box(double(0.0)), box(double(0.0)), box(double(0.0))), box(double(double(SOLAR_MASS)))), 'jupiter': Body(Vector(box(double(4.841431442464721)), box(double(-1.1603200440274284)), box(double(-0.10362204447112311))), Vector(box(double(0.001660076642744037 * double(DAYS_PER_YEAR))), box(double(0.007699011184197404 * double(DAYS_PER_YEAR))), box(double(-6.90460016972063e-05 * double(DAYS_PER_YEAR)))), box(double(0.0009547919384243266 * double(SOLAR_MASS)))), 'saturn': Body(Vector(box(double(8.34336671824458)), box(double(4.124798564124305)), box(double(-0.4035234171143214))), Vector(box(double(-0.002767425107268624 * double(DAYS_PER_YEAR))), box(double(0.004998528012349172 * double(DAYS_PER_YEAR))), box(double(2.3041729757376393e-05 * double(DAYS_PER_YEAR)))), box(double(0.0002858859806661308 * double(SOLAR_MASS)))), 'uranus': Body(Vector(box(double(12.894369562139131)), box(double(-15.111151401698631)), box(double(-0.22330757889265573))), Vector(box(double(0.002964601375647616 * double(DAYS_PER_YEAR))), box(double(0.0023784717395948095 * double(DAYS_PER_YEAR))), box(double(-2.9658956854023756e-05 * double(DAYS_PER_YEAR)))), box(double(4.366244043351563e-05 * double(SOLAR_MASS)))), 'neptune': Body(Vector(box(double(15.379697114850917)), box(double(-25.919314609987964)), box(double(0.17925877295037118))), Vector(box(double(0.0026806777249038932 * double(DAYS_PER_YEAR))), box(double(0.001628241700382423 * double(DAYS_PER_YEAR))), box(double(-9.515922545197159e-05 * double(DAYS_PER_YEAR)))), box(double(5.1513890204661145e-05 * double(SOLAR_MASS))))})
SYSTEM = CheckedList[Body](CheckedList[Body](BODIES.values()))
PAIRS = combinations(CheckedList[Body](SYSTEM))

def advance(dt, n, bodies=CheckedList[Body](SYSTEM), pairs=PAIRS):
    bodies = cast(CheckedList[Body], bodies)
    for i in range(n):
        for b1, b2 in pairs:
            pos1 = cast(Vector, cast(Body, b1).pos)
            pos2 = cast(Vector, cast(Body, b2).pos)
            dx = box(double(double(pos1.x) - double(pos2.x)))
            dy = box(double(double(pos1.y) - double(pos2.y)))
            dz = box(double(double(pos1.z) - double(pos2.z)))
            mag = double(dt) * (double(dx) * double(dx) + double(dy) * double(dy) + double(dz) * double(dz)) ** double(-1.5)
            b1m = double(cast(Body, b1).mass) * mag
            b2m = double(cast(Body, b2).mass) * mag
            v1 = cast(Vector, cast(Body, b1).v)
            v2 = cast(Vector, cast(Body, b2).v)
            v1.x -= double(dx) * b2m
            v1.y -= double(dy) * b2m
            v1.z -= double(dz) * b2m
            v2.x += double(dx) * b1m
            v2.y += double(dy) * b1m
            v2.z += double(dz) * b1m
        for body in bodies:
            r = cast(Vector, body.pos)
            v = cast(Vector, body.v)
            r.x += double(dt) * double(v.x)
            r.y += double(dt) * double(v.y)
            r.z += double(dt) * double(v.z)

def report_energy(bodies=CheckedList[Body](SYSTEM), pairs=PAIRS, e=0.0):
    bodies = cast(CheckedList[Body], bodies)
    for b1, b2 in pairs:
        pos1 = cast(Vector, cast(Body, b1).pos)
        pos2 = cast(Vector, cast(Body, b2).pos)
        dx = double(pos1.x) - double(pos2.x)
        dy = double(pos1.y) - double(pos2.y)
        dz = double(pos1.z) - double(pos2.z)
        e -= double(cast(Body, b1).mass) * double(cast(Body, b2).mass) / (dx * dx + dy * dy + dz * dz) ** 0.5
    for body in bodies:
        v = cast(Vector, cast(Body, body).v)
        e += double(cast(Body, body).mass) * (double(v.x) * double(v.x) + double(v.y) * double(v.y) + double(v.z) * double(v.z)) / 2.0
    return box(double(double(e)))

def offset_momentum(ref, bodies, px=0.0, py=0.0, pz=0.0):
    bodies = cast(CheckedList[Body], bodies)
    for body in bodies:
        v = cast(Vector, cast(Body, body).v)
        m = box(double(cast(Body, body).mass))
        px -= double(v.x) * double(m)
        py -= double(v.y) * double(m)
        pz -= double(v.z) * double(m)
    m = box(double(double(cast(Body, ref).mass)))
    v = cast(Vector, cast(Body, ref).v)
    v.x = box(double(double(px) / double(m)))
    v.y = box(double(double(py) / double(m)))
    v.z = box(double(double(pz) / double(m)))

def bench_nbody(loops, reference, iterations):
    offset_momentum(BODIES[reference], CheckedList[Body](SYSTEM))
    range_it = range(loops)
    for _ in range_it:
        double(report_energy(CheckedList[Body](SYSTEM), PAIRS))
        advance(box(double(0.01)), iterations, CheckedList[Body](SYSTEM), PAIRS)
        double(report_energy(CheckedList[Body](SYSTEM), PAIRS))

def run():
    num_loops = 5
    bench_nbody(num_loops, DEFAULT_REFERENCE, DEFAULT_ITERATIONS)
if __name__ == '__main__':
    import sys
    num_loops = 5
    startTime = time.time()
    bench_nbody(num_loops, DEFAULT_REFERENCE, DEFAULT_ITERATIONS)
    endTime = time.time()
    runtime = endTime - startTime
    print(runtime)