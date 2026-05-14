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
from __static__ import box, cast
import sys
import __static__
from __static__ import cast, cbool, int64, box, inline
from typing import Final, Optional, List
from typing import Optional
import time
I_IDLE: Final[int] = 1
I_WORK = 2
I_HANDLERA: Final[int] = 3
I_HANDLERB = 4
I_DEVA: Final[int] = 5
I_DEVB: Final[int] = 6
K_DEV: Final[int] = 1000
K_WORK = 1001
BUFSIZE = 4
BUFSIZE_RANGE = range(BUFSIZE)

class Packet(object):

    def __init__(self, l, i: int64, k):
        self.link = l
        self.ident: int64 = i
        self.kind = box(int64(int64(k)))
        self.datum: int = 0
        self.data = cast(List[int], [0] * BUFSIZE)

    def append_to(self, lst: Optional[Packet]):
        self.link = None
        if lst is None:
            return cast(Packet, self)
        else:
            p: Packet = lst
            next = p.link
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

    def __init__(self):
        self.control = box(int64(1))
        self.count: int64 = 10000

class HandlerTaskRec(TaskRec):

    def __init__(self):
        self.work_in: Optional[Packet] = None
        self.device_in = None

    def workInAdd(self, p: Packet) -> Optional[Packet]:
        self.work_in = cast(Packet, p.append_to(self.work_in))
        return self.work_in

    def deviceInAdd(self, p):
        self.device_in = cast(Packet, cast(Packet, p).append_to(self.device_in))
        return cast(Packet | None, self.device_in)

class WorkerTaskRec(TaskRec):

    def __init__(self) -> None:
        self.destination = box(int64(int64(I_HANDLERA)))
        self.count = box(int64(0))

class TaskState(object):

    def __init__(self):
        self.packet_pending: cbool = True
        self.task_waiting: cbool = False
        self.task_holding: cbool = False

    def packetPending(self) -> TaskState:
        self.packet_pending = True
        self.task_waiting = False
        self.task_holding = False
        return self

    def waiting(self) -> TaskState:
        self.packet_pending = False
        self.task_waiting = True
        self.task_holding = False
        return self

    def running(self) -> TaskState:
        self.packet_pending = False
        self.task_waiting = False
        self.task_holding = False
        return self

    def waitingWithPacket(self):
        self.packet_pending = True
        self.task_waiting = True
        self.task_holding = False
        return cast(TaskState, self)

    @inline
    def isPacketPending(self) -> cbool:
        return self.packet_pending

    @inline
    def isTaskWaiting(self) -> cbool:
        return self.task_waiting

    @inline
    def isTaskHolding(self):
        return box(cbool(self.task_holding))

    @inline
    def isTaskHoldingOrWaiting(self):
        return box(cbool(self.task_holding or (not self.packet_pending and self.task_waiting)))

    @inline
    def isWaitingWithPacket(self):
        return box(cbool(self.packet_pending and self.task_waiting and (not self.task_holding)))
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

    def __init__(self) -> None:
        self.taskTab = cast(List[Task], [None] * TASKTABSIZE)
        self.taskList: Optional[Task] = None
        self.holdCount: int64 = 0
        self.qpktCount: int64 = 0

class Task(TaskState):

    def __init__(self, i, p, w, initialState, r):
        wa = cast(TaskWorkArea, taskWorkArea)
        self.link: Optional[Task] = wa.taskList
        self.ident = box(int64(int64(i)))
        self.priority = box(int64(int64(p)))
        self.input: Optional[Packet] = w
        self.packet_pending = initialState.isPacketPending()
        self.task_waiting = initialState.isTaskWaiting()
        self.task_holding = cbool(initialState.isTaskHolding())
        self.handle = r
        wa.taskList = self
        cast(List[Task], wa.taskTab)[int64(i)] = self

    def fn(self, pkt, r):
        raise NotImplementedError

    def addPacket(self, p: Packet, old: Task) -> Task:
        if self.input is None:
            self.input = p
            self.packet_pending = True
            if int64(self.priority) > int64(old.priority):
                return self
        else:
            p.append_to(self.input)
        return old

    def runTask(self):
        if cbool(TaskState.isWaitingWithPacket(self)):
            msg: Optional[Packet] = self.input
            if msg is not None:
                self.input = msg.link
                if self.input is None:
                    self.running()
                else:
                    self.packetPending()
        else:
            msg = None
        return cast(Task | None, cast(Task | None, self.fn(msg, self.handle)))

    def waitTask(self):
        self.task_waiting = True
        return cast(Task, self)

    def hold(self) -> Optional[Task]:
        taskWorkArea.holdCount += 1
        self.task_holding = True
        return self.link

    def release(self, i: int64) -> Task:
        t = cast(Task, Task.findtcb(self, i))
        t.task_holding = False
        if int64(t.priority) > int64(self.priority):
            return t
        else:
            return self

    def qpkt(self, pkt: Packet):
        t = cast(Task, Task.findtcb(self, pkt.ident))
        taskWorkArea.qpktCount += 1
        pkt.link = None
        pkt.ident = int64(self.ident)
        return cast(Task, t.addPacket(pkt, self))

    def findtcb(self, id: int64) -> Task:
        t = cast(List[Task], taskWorkArea.taskTab)[id]
        return cast(Task, t)

class DeviceTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(box(int64(self)), box(int64(i)), int64(p), w, s, r)

    def fn(self, pkt, r):
        d = cast(DeviceTaskRec, cast(DeviceTaskRec, cast(TaskRec, r)))
        if pkt is None:
            pkt = d.pending
            if pkt is None:
                return cast(Task, cast(Task, self.waitTask()))
            else:
                d.pending = None
                return cast(Task, cast(Task, self.qpkt(pkt)))
        else:
            d.pending = pkt
            if tracing:
                trace(pkt.datum)
            return cast(Task, cast(Task, self.hold()))

class HandlerTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(box(int64(self)), box(int64(i)), int64(p), w, s, r)

    def fn(self, pkt, r):
        h = cast(HandlerTaskRec, cast(HandlerTaskRec, cast(TaskRec, r)))
        if pkt is not None:
            if int64(pkt.kind) == int64(K_WORK):
                h.workInAdd(pkt)
            else:
                h.deviceInAdd(pkt)
        work = h.work_in
        if work is None:
            return cast(Task, cast(Task, self.waitTask()))
        count: int = work.datum
        if count >= BUFSIZE:
            h.work_in = work.link
            return cast(Task, cast(Task, self.qpkt(work)))
        dev = h.device_in
        if dev is None:
            return cast(Task, cast(Task, self.waitTask()))
        h.device_in = dev.link
        dev.datum = cast(List[int], work.data)[count]
        work.datum = count + 1
        return cast(Task, cast(Task, self.qpkt(dev)))

class IdleTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(box(int64(self)), box(int64(i)), 0, None, s, r)

    def fn(self, pkt, r):
        i = cast(IdleTaskRec, cast(IdleTaskRec, cast(TaskRec, r)))
        i.count -= 1
        if i.count == 0:
            return cast(Task | None, self.hold())
        elif int64(i.control) & 1 == 0:
            i.control //= 2
            return cast(Task | None, Task.release(self, int64(I_DEVA)))
        else:
            i.control = box(int64(int64(i.control) // 2 ^ 53256))
            return cast(Task | None, Task.release(self, int64(I_DEVB)))
A: Final[int] = 65

class WorkTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(box(int64(self)), box(int64(i)), int64(p), w, s, r)

    def fn(self, pkt, r):
        w: WorkerTaskRec = cast(WorkerTaskRec, cast(TaskRec, r))
        if pkt is None:
            return cast(Task, cast(Task, self.waitTask()))
        if int64(w.destination) == int64(I_HANDLERA):
            dest: int64 = int64(I_HANDLERB)
        else:
            dest = int64(I_HANDLERA)
        w.destination = box(int64(dest))
        pkt.ident = dest
        pkt.datum = 0
        i = 0
        while i < BUFSIZE:
            x: int64 = int64(w.count) + 1
            w.count = box(int64(x))
            if int64(w.count) > 26:
                w.count = box(int64(1))
            cast(List[int], pkt.data)[i] = A + box(int64(w.count)) - 1
            i = i + 1
        return cast(Task, cast(Task, self.qpkt(pkt)))
taskWorkArea = TaskWorkArea()

def schedule() -> None:
    t: Optional[Task] = taskWorkArea.taskList
    while t is not None:
        if tracing:
            print('tcb =', box(int64(t.ident)))
        if cbool(TaskState.isTaskHoldingOrWaiting(t)):
            t = t.link
        else:
            if tracing:
                trace(chr(ord('0') + box(int64(t.ident))))
            t = cast(Task | None, t.runTask())

class Richards(object):

    def run(self, iterations: int):
        for i in range(iterations):
            taskWorkArea.holdCount = 0
            taskWorkArea.qpktCount = 0
            IdleTask(box(int64(I_IDLE)), box(int64(1)), 10000, TaskState().running(), IdleTaskRec())
            wkq: Optional[Packet] = Packet(None, 0, box(int64(K_WORK)))
            wkq = Packet(wkq, 0, box(int64(K_WORK)))
            WorkTask(box(int64(I_WORK)), box(int64(1000)), wkq, cast(TaskState, TaskState().waitingWithPacket()), WorkerTaskRec())
            wkq = Packet(None, int64(I_DEVA), box(int64(K_DEV)))
            wkq = Packet(wkq, int64(I_DEVA), box(int64(K_DEV)))
            wkq = Packet(wkq, int64(I_DEVA), box(int64(K_DEV)))
            HandlerTask(box(int64(I_HANDLERA)), box(int64(2000)), wkq, cast(TaskState, TaskState().waitingWithPacket()), HandlerTaskRec())
            wkq = Packet(None, int64(I_DEVB), box(int64(K_DEV)))
            wkq = Packet(wkq, int64(I_DEVB), box(int64(K_DEV)))
            wkq = Packet(wkq, int64(I_DEVB), box(int64(K_DEV)))
            HandlerTask(box(int64(I_HANDLERB)), box(int64(3000)), wkq, cast(TaskState, TaskState().waitingWithPacket()), HandlerTaskRec())
            wkq = None
            DeviceTask(box(int64(I_DEVA)), box(int64(4000)), wkq, TaskState().waiting(), DeviceTaskRec())
            DeviceTask(box(int64(I_DEVB)), box(int64(5000)), wkq, TaskState().waiting(), DeviceTaskRec())
            schedule()
            if taskWorkArea.holdCount == 9297 and taskWorkArea.qpktCount == 23246:
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