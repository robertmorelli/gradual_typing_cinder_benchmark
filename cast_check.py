import __static__
from __static__ import CheckedList, cast
x: CheckedList[int] = CheckedList[int]()
print('type:', type(x).__name__, 'len:', len(x))
cast(CheckedList[int], x)