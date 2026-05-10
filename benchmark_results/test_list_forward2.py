from __static__ import cast
from typing import List
class Task: pass
x=cast(List["Task"], [Task()])
print(x)
