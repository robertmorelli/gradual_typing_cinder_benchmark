"""
based on a Java version:
 Based on original version written in BCPL by Dr Martin Richards
 in 1981 at Cambridge University Computer Laboratory, England
 and a C++ version derived from a Smalltalk version written by
 L Peter Deutsch.
 Java version:  Copyright (C) 1995 Sun Microsystems, Inc.
 Translation from C++, Mario Wolczko
 Outer loop added by Alex Jacoby
"""
from __future__ import annotations
import sys
import __static__
from __static__ import cast, cbool, int64, box, inline
from typing import Final, Optional, List
from typing import Optional
import time
I_IDLE = 1
I_WORK: Final[int] = 2
I_HANDLERA = 3
I_HANDLERB: Final[int] = 4
I_DEVA = 5
I_DEVB = 6
K_DEV: Final[int] = 1000
K_WORK = 1001
BUFSIZE: Final[int] = 4
BUFSIZE_RANGE = range(BUFSIZE)

class Packet(object):

    def __init__(self, l, i: int64, k) -> None:
        self.link: Optional[Packet] = l
        self.ident = box(int64(i))
        self.kind: int64 = int64(k)
        self.datum = 0
        self.data = cast(List[int], [0] * BUFSIZE)

    def append_to(self, lst: Optional[Packet]):
        self.link = None
        if lst is None:
            return cast(Packet, self)
        else:
            p: Packet = lst
            next: Optional[Packet] = p.link
            while next is not None:
                p = next
                next = p.link
            p.link = self
            return cast(Packet, lst)

class TaskRec:
    pass

class DeviceTaskRec(TaskRec):

    def __init__(self):
        self.pending: Optional[Packet] = None

class IdleTaskRec(TaskRec):

    def __init__(self) -> None:
        self.control: int64 = 1
        self.count: int64 = 10000

class HandlerTaskRec(TaskRec):

    def __init__(self) -> None:
        self.work_in: Optional[Packet] = None
        self.device_in: Optional[Packet] = None

    def workInAdd(self, p) -> Optional[Packet]:
        self.work_in = cast(Packet, cast(Packet, p).append_to(self.work_in))
        return self.work_in

    def deviceInAdd(self, p):
        self.device_in = cast(Packet, cast(Packet, p).append_to(self.device_in))
        return cast(Optional[Packet], self.device_in)

class WorkerTaskRec(TaskRec):

    def __init__(self) -> None:
        self.destination = box(int64(int64(I_HANDLERA)))
        self.count = box(int64(0))

class TaskState(object):

    def __init__(self):
        self.packet_pending = box(cbool(True))
        self.task_waiting: cbool = False
        self.task_holding = box(cbool(False))

    def packetPending(self):
        self.packet_pending = True
        self.task_waiting = False
        self.task_holding = False
        return cast(TaskState, self)

    def waiting(self):
        self.packet_pending = False
        self.task_waiting = True
        self.task_holding = False
        return cast(TaskState, self)

    def running(self):
        self.packet_pending = False
        self.task_waiting = False
        self.task_holding = False
        return cast(TaskState, self)

    def waitingWithPacket(self) -> TaskState:
        self.packet_pending = True
        self.task_waiting = True
        self.task_holding = False
        return self

    @inline
    def isPacketPending(self):
        return box(cbool(cbool(self.packet_pending)))

    @inline
    def isTaskWaiting(self):
        return box(cbool(self.task_waiting))

    @inline
    def isTaskHolding(self):
        return box(cbool(cbool(self.task_holding)))

    @inline
    def isTaskHoldingOrWaiting(self):
        return box(cbool(cbool(self.task_holding) or (not cbool(self.packet_pending) and self.task_waiting)))

    @inline
    def isWaitingWithPacket(self):
        return box(cbool(cbool(self.packet_pending) and self.task_waiting and (not cbool(self.task_holding))))
tracing = False
layout = 0

def trace(a):
    global layout
    layout -= 1
    if layout <= 0:
        print()
        layout = 50
    print(a, end='')
TASKTABSIZE = 10

class TaskWorkArea(object):

    def __init__(self):
        self.taskTab = cast(List['Task'], [None] * TASKTABSIZE)
        self.taskList = cast(Optional['Task'], None)
        self.holdCount: int64 = 0
        self.qpktCount = box(int64(0))
taskWorkArea = TaskWorkArea()

class Task(TaskState):

    def __init__(self, i, p, w, initialState, r):
        wa: TaskWorkArea = taskWorkArea
        self.link: Optional[Task] = wa.taskList
        self.ident = i
        self.priority: int64 = int64(p)
        self.input = w
        self.packet_pending = box(cbool(cbool(cast(TaskState, initialState).isPacketPending())))
        self.task_waiting = cbool(cast(TaskState, initialState).isTaskWaiting())
        self.task_holding = box(cbool(cbool(cast(TaskState, initialState).isTaskHolding())))
        self.handle = r
        wa.taskList = self
        cast(List['Task'], wa.taskTab)[int64(i)] = self

    def fn(self, pkt, r):
        raise NotImplementedError

    def addPacket(self, p: Packet, old) -> Task:
        if self.input is None:
            self.input = p
            self.packet_pending = True
            if self.priority > cast(Task, old).priority:
                return self
        else:
            cast(Packet, p.append_to(self.input))
        return cast(Task, old)

    def runTask(self):
        if cbool(TaskState.isWaitingWithPacket(self)):
            msg = self.input
            if msg is not None:
                self.input = msg.link
                if self.input is None:
                    cast(TaskState, self.running())
                else:
                    cast(TaskState, self.packetPending())
        else:
            msg = None
        return cast(Optional[Task], cast(Optional[Task], self.fn(msg, self.handle)))

    def waitTask(self) -> Task:
        self.task_waiting = True
        return self

    def hold(self):
        cast(TaskWorkArea, taskWorkArea).holdCount += 1
        self.task_holding = True
        return cast(Optional[Task], self.link)

    def release(self, i):
        t: Task = Task.findtcb(self, int64(i))
        t.task_holding = False
        if t.priority > self.priority:
            return cast(Task, t)
        else:
            return cast(Task, self)

    def qpkt(self, pkt):
        t: Task = Task.findtcb(self, int64(cast(Packet, pkt).ident))
        cast(TaskWorkArea, taskWorkArea).qpktCount += 1
        cast(Packet, pkt).link = None
        cast(Packet, pkt).ident = box(int64(int64(self.ident)))
        return cast(Task, t.addPacket(cast(Packet, pkt), self))

    def findtcb(self, id: int64) -> Task:
        t = cast(List['Task'], cast(TaskWorkArea, taskWorkArea).taskTab)[id]
        return cast(Task, t)

class DeviceTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(self, i, p, w, s, r)

    def fn(self, pkt, r):
        d = cast(DeviceTaskRec, cast(DeviceTaskRec, cast(TaskRec, r)))
        if pkt is None:
            pkt = cast(DeviceTaskRec, d).pending
            if pkt is None:
                return cast(Task, self.waitTask())
            else:
                cast(DeviceTaskRec, d).pending = None
                return cast(Task, cast(Task, self.qpkt(pkt)))
        else:
            cast(DeviceTaskRec, d).pending = pkt
            if tracing:
                trace(cast(Packet, pkt).datum)
            return cast(Task, cast(Task, cast(Optional[Task], self.hold())))

class HandlerTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(self, i, p, w, s, r)

    def fn(self, pkt, r):
        h: HandlerTaskRec = cast(HandlerTaskRec, cast(TaskRec, r))
        if pkt is not None:
            if cast(Packet, pkt).kind == int64(K_WORK):
                h.workInAdd(pkt)
            else:
                cast(Optional[Packet], h.deviceInAdd(pkt))
        work: Optional[Packet] = h.work_in
        if work is None:
            return cast(Task, self.waitTask())
        count: int = work.datum
        if count >= BUFSIZE:
            h.work_in = work.link
            return cast(Task, cast(Task, self.qpkt(work)))
        dev: Optional[Packet] = h.device_in
        if dev is None:
            return cast(Task, self.waitTask())
        h.device_in = dev.link
        dev.datum = cast(List[int], work.data)[count]
        work.datum = count + 1
        return cast(Task, cast(Task, self.qpkt(dev)))

class IdleTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(self, i, 0, None, s, r)

    def fn(self, pkt, r):
        i: IdleTaskRec = cast(IdleTaskRec, cast(TaskRec, r))
        i.count -= 1
        if i.count == 0:
            return cast(Optional[Task], cast(Optional[Task], self.hold()))
        elif i.control & 1 == 0:
            i.control //= 2
            return cast(Optional[Task], cast(Task, Task.release(self, int64(I_DEVA))))
        else:
            i.control = i.control // 2 ^ 53256
            return cast(Optional[Task], cast(Task, Task.release(self, int64(I_DEVB))))
A = 65

class WorkTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(self, i, p, w, s, r)

    def fn(self, pkt, r):
        w = cast(WorkerTaskRec, cast(WorkerTaskRec, cast(TaskRec, r)))
        if pkt is None:
            return cast(Task, self.waitTask())
        if int64(cast(WorkerTaskRec, w).destination) == int64(I_HANDLERA):
            dest: int64 = int64(I_HANDLERB)
        else:
            dest = int64(I_HANDLERA)
        cast(WorkerTaskRec, w).destination = box(int64(dest))
        cast(Packet, pkt).ident = box(int64(dest))
        cast(Packet, pkt).datum = 0
        i = 0
        while i < BUFSIZE:
            x = box(int64(int64(cast(WorkerTaskRec, w).count) + 1))
            cast(WorkerTaskRec, w).count = box(int64(int64(x)))
            if int64(cast(WorkerTaskRec, w).count) > 26:
                cast(WorkerTaskRec, w).count = 1
            cast(List[int], cast(Packet, pkt).data)[i] = A + box(int64(cast(WorkerTaskRec, w).count)) - 1
            i = i + 1
        return cast(Task, cast(Task, self.qpkt(pkt)))

def schedule():
    t: Optional[Task] = cast(TaskWorkArea, taskWorkArea).taskList
    while t is not None:
        if tracing:
            print('tcb =', box(int64(t.ident)))
        if cbool(TaskState.isTaskHoldingOrWaiting(t)):
            t = t.link
        else:
            if tracing:
                trace(chr(ord('0') + box(int64(t.ident))))
            t = cast(Optional[Task], t.runTask())

class Richards(object):

    def run(self, iterations: int) -> bool:
        for i in range(iterations):
            cast(TaskWorkArea, taskWorkArea).holdCount = 0
            cast(TaskWorkArea, taskWorkArea).qpktCount = 0
            IdleTask(int64(I_IDLE), 1, 10000, cast(TaskState, TaskState().running()), IdleTaskRec())
            wkq: Optional[Packet] = Packet(None, 0, int64(K_WORK))
            wkq = Packet(wkq, 0, int64(K_WORK))
            WorkTask(int64(I_WORK), 1000, wkq, TaskState().waitingWithPacket(), WorkerTaskRec())
            wkq = Packet(None, int64(I_DEVA), int64(K_DEV))
            wkq = Packet(wkq, int64(I_DEVA), int64(K_DEV))
            wkq = Packet(wkq, int64(I_DEVA), int64(K_DEV))
            HandlerTask(int64(I_HANDLERA), 2000, wkq, TaskState().waitingWithPacket(), HandlerTaskRec())
            wkq = Packet(None, int64(I_DEVB), int64(K_DEV))
            wkq = Packet(wkq, int64(I_DEVB), int64(K_DEV))
            wkq = Packet(wkq, int64(I_DEVB), int64(K_DEV))
            HandlerTask(int64(I_HANDLERB), 3000, wkq, TaskState().waitingWithPacket(), HandlerTaskRec())
            wkq = None
            DeviceTask(int64(I_DEVA), 4000, wkq, cast(TaskState, TaskState().waiting()), DeviceTaskRec())
            DeviceTask(int64(I_DEVB), 5000, wkq, cast(TaskState, TaskState().waiting()), DeviceTaskRec())
            schedule()
            if cast(TaskWorkArea, taskWorkArea).holdCount == 9297 and int64(cast(TaskWorkArea, taskWorkArea).qpktCount) == 23246:
                pass
            else:
                print('err')
                return False
        return True
if __name__ == '__main__':
    num_iterations = 8
    if len(sys.argv) > 1:
        num_iterations = int(sys.argv[1])
    start_time = time.time()
    Richards().run(num_iterations)
    end_time = time.time()
    runtime = end_time - start_time
    print(runtime)