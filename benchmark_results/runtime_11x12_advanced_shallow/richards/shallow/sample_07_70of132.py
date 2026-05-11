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
I_IDLE: Final[int] = 1
I_WORK: Final[int] = 2
I_HANDLERA = 3
I_HANDLERB: Final[int] = 4
I_DEVA = 5
I_DEVB: Final[int] = 6
K_DEV = 1000
K_WORK = 1001
BUFSIZE = 4
BUFSIZE_RANGE = list(range(BUFSIZE))

class Packet(object):

    def __init__(self, l, i, k: int):
        self.link: Packet | None = l
        self.ident = i
        self.kind = k
        self.datum: int = 0
        self.data = cast(List[int], [0] * BUFSIZE)

    def append_to(self, lst) -> Packet:
        self.link = None
        if lst is None:
            return self
        else:
            p = lst
            next = p.link
            while next is not None:
                p = next
                next = p.link
            p.link = self
            return lst

class TaskRec(object):
    pass

class DeviceTaskRec(TaskRec):

    def __init__(self) -> None:
        self.pending = None

class IdleTaskRec(TaskRec):

    def __init__(self) -> None:
        self.control: int = 1
        self.count: int = 10000

class HandlerTaskRec(TaskRec):

    def __init__(self):
        self.work_in = None
        self.device_in = None

    def workInAdd(self, p: Packet) -> Packet | None:
        self.work_in = p.append_to(cast(Packet | None, self.work_in))
        return cast(Packet | None, self.work_in)

    def deviceInAdd(self, p):
        self.device_in = cast(Packet, p).append_to(cast(Packet | None, self.device_in))
        return cast(Packet | None, cast(Packet | None, self.device_in))

class WorkerTaskRec(TaskRec):

    def __init__(self):
        self.destination: int = I_HANDLERA
        self.count: int = 0

class TaskState(object):

    def __init__(self):
        self.packet_pending = True
        self.task_waiting = False
        self.task_holding = False

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

    def isPacketPending(self):
        return self.packet_pending

    def isTaskWaiting(self) -> bool:
        return self.task_waiting

    def isTaskHolding(self):
        return self.task_holding

    def isTaskHoldingOrWaiting(self):
        return self.task_holding or (not self.packet_pending and self.task_waiting)

    def isWaitingWithPacket(self) -> bool:
        return self.packet_pending and self.task_waiting and (not self.task_holding)
tracing: bool = False
layout: int = 0

def trace(a):
    global layout
    layout -= 1
    if layout <= 0:
        print()
        layout = 50
    print(a, end='')
TASKTABSIZE: Final[int] = 10

class TaskWorkArea(object):

    def __init__(self):
        self.taskTab = [None] * TASKTABSIZE
        self.taskList: Task | None = None
        self.holdCount = 0
        self.qpktCount = 0
taskWorkArea = TaskWorkArea()

class Task(TaskState):

    def __init__(self, i, p, w, initialState, r):
        self.link = cast(TaskWorkArea, taskWorkArea).taskList
        self.ident: int = i
        self.priority = p
        self.input: Packet | None = w
        self.packet_pending: bool = cast(TaskState, initialState).isPacketPending()
        self.task_waiting = cast(TaskState, initialState).isTaskWaiting()
        self.task_holding = cast(TaskState, initialState).isTaskHolding()
        self.handle: TaskRec = r
        cast(TaskWorkArea, taskWorkArea).taskList = self
        cast(TaskWorkArea, taskWorkArea).taskTab[i] = self

    def fn(self, pkt, r):
        raise NotImplementedError

    def addPacket(self, p: Packet, old) -> Task:
        if self.input is None:
            self.input = p
            self.packet_pending = True
            if self.priority > cast(Task, old).priority:
                return self
        else:
            p.append_to(self.input)
        return cast(Task, old)

    def runTask(self):
        if self.isWaitingWithPacket():
            msg = self.input
            assert msg is not None
            self.input = msg.link
            if self.input is None:
                self.running()
            else:
                cast(TaskState, self.packetPending())
        else:
            msg = None
        return cast(Task | None, cast(Task | None, self.fn(msg, self.handle)))

    def waitTask(self):
        self.task_waiting = True
        return cast(Task, self)

    def hold(self):
        cast(TaskWorkArea, taskWorkArea).holdCount += 1
        self.task_holding = True
        return cast(Task | None, cast(Task | None, self.link))

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
        return cast(Task, t.addPacket(cast(Packet, pkt), self))

    def findtcb(self, id: int):
        t = cast(TaskWorkArea, taskWorkArea).taskTab[id]
        assert t is not None
        return cast(Task, t)

class DeviceTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(self, i, p, w, s, r)

    def fn(self, pkt, r):
        d = cast(DeviceTaskRec, cast(DeviceTaskRec, cast(TaskRec, r)))
        if pkt is None:
            pkt = cast(Packet | None, cast(DeviceTaskRec, d).pending)
            if pkt is None:
                return cast(Task, cast(Task, self.waitTask()))
            else:
                cast(DeviceTaskRec, d).pending = None
                return cast(Task, cast(Task, self.qpkt(pkt)))
        else:
            cast(DeviceTaskRec, d).pending = pkt
            if tracing:
                trace(cast(Packet, pkt).datum)
            return cast(Task, cast(Task, cast(Task | None, self.hold())))

class HandlerTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(self, i, p, w, s, r)

    def fn(self, pkt, r):
        h: HandlerTaskRec = cast(HandlerTaskRec, cast(TaskRec, r))
        if pkt is not None:
            if cast(Packet, pkt).kind == K_WORK:
                h.workInAdd(pkt)
            else:
                cast(Packet | None, h.deviceInAdd(pkt))
        work = cast(Packet | None, h.work_in)
        if work is None:
            return cast(Task, cast(Task, self.waitTask()))
        count = work.datum
        if count >= BUFSIZE:
            h.work_in = work.link
            return cast(Task, cast(Task, self.qpkt(work)))
        dev = cast(Packet | None, h.device_in)
        if dev is None:
            return cast(Task, cast(Task, self.waitTask()))
        h.device_in = dev.link
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
            return cast(Task | None, cast(Task | None, self.hold()))
        elif cast(IdleTaskRec, i).control & 1 == 0:
            cast(IdleTaskRec, i).control //= 2
            return cast(Task | None, cast(Task, self.release(I_DEVA)))
        else:
            cast(IdleTaskRec, i).control = cast(IdleTaskRec, i).control // 2 ^ 53256
            return cast(Task | None, cast(Task, self.release(I_DEVB)))
A: Final[int] = 65

class WorkTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(self, i, p, w, s, r)

    def fn(self, pkt, r):
        w = cast(WorkerTaskRec, cast(WorkerTaskRec, cast(TaskRec, r)))
        if pkt is None:
            return cast(Task, cast(Task, self.waitTask()))
        if cast(WorkerTaskRec, w).destination == I_HANDLERA:
            dest = I_HANDLERB
        else:
            dest = I_HANDLERA
        cast(WorkerTaskRec, w).destination = dest
        cast(Packet, pkt).ident = dest
        cast(Packet, pkt).datum = 0
        i = 0
        while i < BUFSIZE:
            x = cast(WorkerTaskRec, w).count + 1
            cast(WorkerTaskRec, w).count = x
            if cast(WorkerTaskRec, w).count > 26:
                cast(WorkerTaskRec, w).count = 1
            cast(List[int], cast(Packet, pkt).data)[i] = A + cast(WorkerTaskRec, w).count - 1
            i = i + 1
        return cast(Task, cast(Task, self.qpkt(pkt)))

def schedule():
    t: Task | None = cast(TaskWorkArea, taskWorkArea).taskList
    while t is not None:
        if tracing:
            print('tcb =', t.ident)
        if t.isTaskHoldingOrWaiting():
            t = cast(Task | None, t.link)
        else:
            if tracing:
                trace(chr(ord('0') + t.ident))
            t = cast(Task | None, t.runTask())

class Richards(object):

    def run(self, iterations: int) -> bool:
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
            DeviceTask(I_DEVA, 4000, wkq, cast(TaskState, TaskState().waiting()), DeviceTaskRec())
            DeviceTask(I_DEVB, 5000, wkq, cast(TaskState, TaskState().waiting()), DeviceTaskRec())
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