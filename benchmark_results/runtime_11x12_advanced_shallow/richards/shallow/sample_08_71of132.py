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
import __static__
from __static__ import cast
import sys
from typing import Final, List
import time
I_IDLE = 1
I_WORK: Final[int] = 2
I_HANDLERA: Final[int] = 3
I_HANDLERB = 4
I_DEVA: Final[int] = 5
I_DEVB = 6
K_DEV: Final[int] = 1000
K_WORK = 1001
BUFSIZE = 4
BUFSIZE_RANGE: List[int] = list(range(BUFSIZE))

class Packet(object):

    def __init__(self, l, i: int, k) -> None:
        self.link = l
        self.ident = i
        self.kind = k
        self.datum = 0
        self.data = cast(List[int], [0] * BUFSIZE)

    def append_to(self, lst):
        self.link = None
        if lst is None:
            return cast(Packet, self)
        else:
            p = lst
            next = cast(Packet | None, p.link)
            while next is not None:
                p = next
                next = cast(Packet | None, p.link)
            p.link = self
            return cast(Packet, lst)

class TaskRec(object):
    pass

class DeviceTaskRec(TaskRec):

    def __init__(self) -> None:
        self.pending: Packet | None = None

class IdleTaskRec(TaskRec):

    def __init__(self) -> None:
        self.control: int = 1
        self.count: int = 10000

class HandlerTaskRec(TaskRec):

    def __init__(self):
        self.work_in = None
        self.device_in: Packet | None = None

    def workInAdd(self, p) -> Packet | None:
        self.work_in = cast(Packet, cast(Packet, p).append_to(cast(Packet | None, self.work_in)))
        return cast(Packet | None, self.work_in)

    def deviceInAdd(self, p: Packet) -> Packet | None:
        self.device_in = cast(Packet, p.append_to(self.device_in))
        return self.device_in

class WorkerTaskRec(TaskRec):

    def __init__(self) -> None:
        self.destination = I_HANDLERA
        self.count: int = 0

class TaskState(object):

    def __init__(self):
        self.packet_pending = True
        self.task_waiting: bool = False
        self.task_holding: bool = False

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

    def waitingWithPacket(self) -> TaskState:
        self.packet_pending = True
        self.task_waiting = True
        self.task_holding = False
        return self

    def isPacketPending(self):
        return self.packet_pending

    def isTaskWaiting(self):
        return self.task_waiting

    def isTaskHolding(self) -> bool:
        return self.task_holding

    def isTaskHoldingOrWaiting(self):
        return self.task_holding or (not self.packet_pending and self.task_waiting)

    def isWaitingWithPacket(self):
        return self.packet_pending and self.task_waiting and (not self.task_holding)
tracing = False
layout = 0

def trace(a):
    global layout
    layout -= 1
    if layout <= 0:
        print()
        layout = 50
    print(a, end='')
TASKTABSIZE: Final[int] = 10

class TaskWorkArea(object):

    def __init__(self) -> None:
        self.taskTab = [None] * TASKTABSIZE
        self.taskList = None
        self.holdCount = 0
        self.qpktCount: int = 0
taskWorkArea = TaskWorkArea()

class Task(TaskState):

    def __init__(self, i, p, w, initialState, r):
        self.link: Task | None = cast(Task | None, cast(TaskWorkArea, taskWorkArea).taskList)
        self.ident: int = i
        self.priority = p
        self.input: Packet | None = w
        self.packet_pending: bool = cast(TaskState, initialState).isPacketPending()
        self.task_waiting = cast(TaskState, initialState).isTaskWaiting()
        self.task_holding: bool = cast(TaskState, initialState).isTaskHolding()
        self.handle = r
        cast(TaskWorkArea, taskWorkArea).taskList = self
        cast(TaskWorkArea, taskWorkArea).taskTab[i] = self

    def fn(self, pkt, r):
        raise NotImplementedError

    def addPacket(self, p, old: Task):
        if self.input is None:
            self.input = cast(Packet, p)
            self.packet_pending = True
            if self.priority > old.priority:
                return cast(Task, self)
        else:
            cast(Packet, cast(Packet, p).append_to(self.input))
        return cast(Task, old)

    def runTask(self):
        if self.isWaitingWithPacket():
            msg = self.input
            assert msg is not None
            self.input = cast(Packet | None, msg.link)
            if self.input is None:
                self.running()
            else:
                self.packetPending()
        else:
            msg = None
        return cast(Task | None, cast(Task | None, self.fn(msg, cast(TaskRec, self.handle))))

    def waitTask(self) -> Task:
        self.task_waiting = True
        return self

    def hold(self) -> Task | None:
        cast(TaskWorkArea, taskWorkArea).holdCount += 1
        self.task_holding = True
        return self.link

    def release(self, i: int):
        t = cast(Task, self.findtcb(i))
        t.task_holding = False
        if t.priority > self.priority:
            return cast(Task, t)
        else:
            return cast(Task, self)

    def qpkt(self, pkt):
        t = cast(Task, self.findtcb(cast(Packet, pkt).ident))
        cast(TaskWorkArea, taskWorkArea).qpktCount += 1
        cast(Packet, pkt).link = None
        cast(Packet, pkt).ident = self.ident
        return cast(Task, cast(Task, t.addPacket(cast(Packet, pkt), self)))

    def findtcb(self, id):
        t = cast(TaskWorkArea, taskWorkArea).taskTab[id]
        assert t is not None
        return cast(Task, t)

class DeviceTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(self, i, p, w, s, r)

    def fn(self, pkt, r):
        d: DeviceTaskRec = cast(DeviceTaskRec, cast(TaskRec, r))
        if pkt is None:
            pkt = d.pending
            if pkt is None:
                return cast(Task, self.waitTask())
            else:
                d.pending = None
                return cast(Task, cast(Task, self.qpkt(pkt)))
        else:
            d.pending = pkt
            if tracing:
                trace(cast(Packet, pkt).datum)
            return cast(Task, cast(Task, self.hold()))

class HandlerTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(self, i, p, w, s, r)

    def fn(self, pkt, r):
        h = cast(HandlerTaskRec, cast(HandlerTaskRec, cast(TaskRec, r)))
        if pkt is not None:
            if cast(Packet, pkt).kind == K_WORK:
                cast(HandlerTaskRec, h).workInAdd(pkt)
            else:
                cast(HandlerTaskRec, h).deviceInAdd(pkt)
        work = cast(Packet | None, cast(HandlerTaskRec, h).work_in)
        if work is None:
            return cast(Task, self.waitTask())
        count = work.datum
        if count >= BUFSIZE:
            cast(HandlerTaskRec, h).work_in = cast(Packet | None, work.link)
            return cast(Task, cast(Task, self.qpkt(work)))
        dev = cast(HandlerTaskRec, h).device_in
        if dev is None:
            return cast(Task, self.waitTask())
        cast(HandlerTaskRec, h).device_in = cast(Packet | None, dev.link)
        dev.datum = cast(List[int], work.data)[count]
        work.datum = count + 1
        return cast(Task, cast(Task, self.qpkt(dev)))

class IdleTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(self, i, 0, None, s, r)

    def fn(self, pkt, r):
        i = cast(IdleTaskRec, cast(IdleTaskRec, cast(TaskRec, r)))
        cast(IdleTaskRec, i).count -= 1
        if cast(IdleTaskRec, i).count == 0:
            return cast(Task | None, self.hold())
        elif cast(IdleTaskRec, i).control & 1 == 0:
            cast(IdleTaskRec, i).control //= 2
            return cast(Task | None, cast(Task, self.release(I_DEVA)))
        else:
            cast(IdleTaskRec, i).control = cast(IdleTaskRec, i).control // 2 ^ 53256
            return cast(Task | None, cast(Task, self.release(I_DEVB)))
A = 65

class WorkTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(self, i, p, w, s, r)

    def fn(self, pkt, r):
        w: WorkerTaskRec = cast(WorkerTaskRec, cast(TaskRec, r))
        if pkt is None:
            return cast(Task, self.waitTask())
        if w.destination == I_HANDLERA:
            dest = I_HANDLERB
        else:
            dest = I_HANDLERA
        w.destination = dest
        cast(Packet, pkt).ident = dest
        cast(Packet, pkt).datum = 0
        i = 0
        while i < BUFSIZE:
            x = w.count + 1
            w.count = x
            if w.count > 26:
                w.count = 1
            cast(List[int], cast(Packet, pkt).data)[i] = A + w.count - 1
            i = i + 1
        return cast(Task, cast(Task, self.qpkt(pkt)))

def schedule() -> None:
    t = cast(TaskWorkArea, taskWorkArea).taskList
    while t is not None:
        if tracing:
            print('tcb =', cast(Task, t).ident)
        if cast(Task, t).isTaskHoldingOrWaiting():
            t = cast(Task, t).link
        else:
            if tracing:
                trace(chr(ord('0') + cast(Task, t).ident))
            t = cast(Task | None, cast(Task, t).runTask())

class Richards(object):

    def run(self, iterations) -> bool:
        for i in range(iterations):
            cast(TaskWorkArea, taskWorkArea).holdCount = 0
            cast(TaskWorkArea, taskWorkArea).qpktCount = 0
            IdleTask(I_IDLE, 1, 10000, TaskState().running(), IdleTaskRec())
            wkq = Packet(None, 0, K_WORK)
            wkq = Packet(wkq, 0, K_WORK)
            WorkTask(I_WORK, 1000, wkq, TaskState().waitingWithPacket(), WorkerTaskRec())
            wkq = Packet(None, I_DEVA, K_DEV)
            wkq = Packet(wkq, I_DEVA, K_DEV)
            wkq = Packet(wkq, I_DEVA, K_DEV)
            HandlerTask(I_HANDLERA, 2000, wkq, TaskState().waitingWithPacket(), HandlerTaskRec())
            wkq = Packet(None, I_DEVB, K_DEV)
            wkq = Packet(wkq, I_DEVB, K_DEV)
            wkq = Packet(wkq, I_DEVB, K_DEV)
            HandlerTask(I_HANDLERB, 3000, wkq, TaskState().waitingWithPacket(), HandlerTaskRec())
            wkq = None
            DeviceTask(I_DEVA, 4000, wkq, TaskState().waiting(), DeviceTaskRec())
            DeviceTask(I_DEVB, 5000, wkq, TaskState().waiting(), DeviceTaskRec())
            schedule()
            if cast(TaskWorkArea, taskWorkArea).holdCount == 9297 and cast(TaskWorkArea, taskWorkArea).qpktCount == 23246:
                pass
            else:
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