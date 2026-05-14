"""
The Computer Language Benchmarks Game
http://benchmarksgame.alioth.debian.org/
Contributed by Sokolov Yura, modified by Tupteq.
"""
from __future__ import annotations
from __static__ import box, cast
import __static__
from __static__ import box, int64, Array
from typing import Callable, List
import sys
import time
DEFAULT_ARG = 9

def fannkuch(nb: int) -> int:
    n: int64 = int64(nb)
    count: Array[int64] = Array[int64](nb)
    i = box(int64(0))
    while int64(i) < n:
        count[int64(i)] = int64(i) + 1
        i += 1
    max_flips: int64 = 0
    m: int64 = n - 1
    r = box(int64(n))
    perm1 = Array[int64](nb)
    perm = Array[int64](nb)
    i = box(int64(0))
    while int64(i) < n:
        perm1[int64(i)] = int64(i)
        perm[int64(i)] = int64(i)
        i += 1
    perm0: Array[int64] = Array[int64](nb)
    while 1:
        while int64(r) != 1:
            count[int64(r) - 1] = int64(r)
            r -= 1
        if perm1[0] != 0 and perm1[m] != m:
            i = box(int64(0))
            while int64(i) < n:
                perm[int64(i)] = perm1[int64(i)]
                i += 1
            flips_count = box(int64(0))
            k: int64 = perm[0]
            while k:
                i = box(int64(k))
                while int64(i) >= 0:
                    perm0[int64(i)] = perm[k - int64(i)]
                    i -= 1
                i = box(int64(k))
                while int64(i) >= 0:
                    perm[int64(i)] = perm0[int64(i)]
                    i -= 1
                flips_count += 1
                k = perm[0]
            if int64(flips_count) > max_flips:
                max_flips = int64(flips_count)
        while int64(r) != n:
            first = box(int64(perm1[0]))
            i = box(int64(1))
            while int64(i) <= int64(r):
                perm1[int64(i) - 1] = perm1[int64(i)]
                i += 1
            perm1[int64(r)] = int64(first)
            count[int64(r)] -= 1
            if count[int64(r)] > 0:
                break
            r += 1
        else:
            return box(max_flips)
    return 0
if __name__ == '__main__':
    num_iterations = 1
    if len(sys.argv) > 1:
        num_iterations = int(sys.argv[1])
    start_time = time.time()
    for _ in range(num_iterations):
        res = fannkuch(DEFAULT_ARG)
        assert res == 30
    end_time = time.time()
    runtime = end_time - start_time
    print(runtime / num_iterations)