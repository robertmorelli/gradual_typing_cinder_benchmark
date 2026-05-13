"""Cinder static-compiler crash: KeyError on BoolOp inside @inline body.

Trigger conditions (all required):
  1. A class field annotated `cbool` (`packet_pending`).
  2. Another class field whose `cbool` annotation has been REMOVED
     (`task_holding` — its RHS still constructs a boxed cbool, but the
     annotation is gone, so cinder treats reads of it as dynamic).
  3. An `@inline` method on the class whose body returns
     `box(cbool(<BoolOp combining a dynamic and a cbool>))`.
  4. A caller that loops on a dynamic-typed local and invokes the inline
     method via the unbound `Class.method(obj)` form inside `cbool(...)`.

The `while ... is not None:` loop narrows `t` enough to bypass the
"invalid union type Union[cbool, dynamic]" static check that would
otherwise fire — and code-gen then crashes inside emit_box -> emit_call
when it tries `cur_mod.types[BoolOp_node]` and finds no entry.

  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 275, in get_type
      return self.cur_mod.types[node]
  KeyError: <ast.BoolOp object at 0x...>
"""

from __static__ import cbool, box, inline

class TaskState(object):
    def __init__(self) -> None:
        self.packet_pending: cbool = True
        self.task_holding = box(cbool(False))

    @inline
    def isTaskHoldingOrWaiting(self):
        return box(cbool(cbool(self.task_holding) or self.packet_pending))


def schedule(holder) -> None:
    t = holder
    while t is not None:
        cbool(TaskState.isTaskHoldingOrWaiting(t));
