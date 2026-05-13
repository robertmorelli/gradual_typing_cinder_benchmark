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
        if cbool(TaskState.isTaskHoldingOrWaiting(t)):
            pass
