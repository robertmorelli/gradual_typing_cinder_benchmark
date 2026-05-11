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
I_IDLE: Final[int] = 1
I_WORK = 2
I_HANDLERA = 3
I_HANDLERB = 4
I_DEVA: Final[int] = 5
I_DEVB = 6
K_DEV: Final[int] = 1000
K_WORK: Final[int] = 1001
BUFSIZE = 4
BUFSIZE_RANGE = range(BUFSIZE)

class Packet(object):

    def __init__(self, l: Optional[Packet], i: int64, k: int64):
        self.link = l
        self.ident = box(int64(i))
        self.kind: int64 = k
        self.datum: int = 0
        self.data = cast(List[int], [0] * BUFSIZE)

    def append_to(self, lst: Optional[Packet]):
        self.link = None
        if lst is None:
            return cast(Packet, self)
        else:
            p = cast(Packet, lst)
            next: Optional[Packet] = cast(Packet, p).link
            while next is not None:
                p = next
                next = cast(Packet, p).link
            cast(Packet, p).link = self
            return cast(Packet, lst)

class TaskRec:
    pass

class DeviceTaskRec(TaskRec):

    def __init__(self):
        self.pending = cast(Optional['Packet'], None)

class IdleTaskRec(TaskRec):

    def __init__(self):
        self.control: int64 = 1
        self.count: int64 = 10000

class HandlerTaskRec(TaskRec):

    def __init__(self):
        self.work_in = cast(Optional['Packet'], None)
        self.device_in: Optional[Packet] = None

    def workInAdd(self, p):
        self.work_in = cast(Packet, cast(Packet, p).append_to(self.work_in))
        return cast(Optional[Packet], self.work_in)

    def deviceInAdd(self, p: Packet):
        self.device_in = cast(Packet, p.append_to(self.device_in))
        return cast(Optional[Packet], self.device_in)

class WorkerTaskRec(TaskRec):

    def __init__(self):
        self.destination = box(int64(int64(I_HANDLERA)))
        self.count = box(int64(0))

class TaskState(object):

    def __init__(self):
        self.packet_pending: cbool = True
        self.task_waiting = box(cbool(False))
        self.task_holding = box(cbool(False))

    def packetPending(self):
        self.packet_pending = True
        self.task_waiting = False
        self.task_holding = False
        return cast(TaskState, self)

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
    def isPacketPending(self):
        return box(cbool(self.packet_pending))

    @inline
    def isTaskWaiting(self):
        return box(cbool(cbool(self.task_waiting)))

    @inline
    def isTaskHolding(self) -> cbool:
        return cbool(self.task_holding)

    @inline
    def isTaskHoldingOrWaiting(self):
        return box(cbool(cbool(self.task_holding) or (not self.packet_pending and cbool(self.task_waiting))))

    @inline
    def isWaitingWithPacket(self) -> cbool:
        return self.packet_pending and cbool(self.task_waiting) and (not cbool(self.task_holding))
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
        self.taskTab: List[Task] = [None] * TASKTABSIZE
        self.taskList: Optional[Task] = None
        self.holdCount: int64 = 0
        self.qpktCount = box(int64(0))
taskWorkArea = TaskWorkArea()

class Task(TaskState):

    def __init__(self, i, p, w, initialState, r):
        wa = cast(TaskWorkArea, taskWorkArea)
        self.link: Optional[Task] = cast(TaskWorkArea, wa).taskList
        self.ident = i
        self.priority = p
        self.input = w
        self.packet_pending = cbool(cast(TaskState, initialState).isPacketPending())
        self.task_waiting = box(cbool(cbool(cast(TaskState, initialState).isTaskWaiting())))
        self.task_holding = box(cbool(cast(TaskState, initialState).isTaskHolding()))
        self.handle = r
        cast(TaskWorkArea, wa).taskList = self
        cast(TaskWorkArea, wa).taskTab[int64(i)] = self

    def fn(self, pkt, r):
        raise NotImplementedError

    def addPacket(self, p: Packet, old) -> Task:
        if self.input is None:
            self.input = p
            self.packet_pending = True
            if int64(self.priority) > int64(cast(Task, old).priority):
                return self
        else:
            cast(Packet, p.append_to(self.input))
        return cast(Task, old)

    def runTask(self):
        if TaskState.isWaitingWithPacket(self):
            msg: Optional[Packet] = self.input
            if msg is not None:
                self.input = msg.link
                if self.input is None:
                    self.running()
                else:
                    cast(TaskState, self.packetPending())
        else:
            msg = None
        return cast(Optional[Task], cast(Optional[Task], self.fn(msg, self.handle)))

    def waitTask(self):
        self.task_waiting = True
        return cast(Task, self)

    def hold(self):
        cast(TaskWorkArea, taskWorkArea).holdCount += 1
        self.task_holding = True
        return cast(Optional[Task], self.link)

    def release(self, i: int64) -> Task:
        t = Task.findtcb(self, box(int64(i)))
        cast(Task, t).task_holding = False
        if int64(cast(Task, t).priority) > int64(self.priority):
            return t
        else:
            return self

    def qpkt(self, pkt: Packet):
        t = Task.findtcb(self, pkt.ident)
        cast(TaskWorkArea, taskWorkArea).qpktCount += 1
        pkt.link = None
        pkt.ident = box(int64(int64(self.ident)))
        return cast(Task, cast(Task, t).addPacket(pkt, self))

    def findtcb(self, id):
        t = cast(TaskWorkArea, taskWorkArea).taskTab[int64(id)]
        return cast(Task, cast(Task, t))

class DeviceTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(self, i, p, w, s, r)

    def fn(self, pkt, r):
        d: DeviceTaskRec = cast(DeviceTaskRec, cast(TaskRec, r))
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
                trace(cast(Packet, pkt).datum)
            return cast(Task, cast(Task, cast(Optional[Task], self.hold())))

class HandlerTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(self, i, p, w, s, r)

    def fn(self, pkt, r):
        h = cast(HandlerTaskRec, cast(HandlerTaskRec, cast(TaskRec, r)))
        if pkt is not None:
            if cast(Packet, pkt).kind == int64(K_WORK):
                cast(Optional[Packet], cast(HandlerTaskRec, h).workInAdd(pkt))
            else:
                cast(Optional[Packet], cast(HandlerTaskRec, h).deviceInAdd(pkt))
        work = cast(HandlerTaskRec, h).work_in
        if work is None:
            return cast(Task, cast(Task, self.waitTask()))
        count: int = work.datum
        if count >= BUFSIZE:
            cast(HandlerTaskRec, h).work_in = work.link
            return cast(Task, cast(Task, self.qpkt(work)))
        dev: Optional[Packet] = cast(HandlerTaskRec, h).device_in
        if dev is None:
            return cast(Task, cast(Task, self.waitTask()))
        cast(HandlerTaskRec, h).device_in = dev.link
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
            return cast(Optional[Task], cast(Optional[Task], self.hold()))
        elif cast(IdleTaskRec, i).control & 1 == 0:
            cast(IdleTaskRec, i).control //= 2
            return cast(Optional[Task], Task.release(self, int64(I_DEVA)))
        else:
            cast(IdleTaskRec, i).control = cast(IdleTaskRec, i).control // 2 ^ 53256
            return cast(Optional[Task], Task.release(self, int64(I_DEVB)))
A: Final[int] = 65

class WorkTask(Task):

    def __init__(self, i, p, w, s, r):
        Task.__init__(self, i, p, w, s, r)

    def fn(self, pkt, r):
        w = cast(WorkerTaskRec, cast(WorkerTaskRec, cast(TaskRec, r)))
        if pkt is None:
            return cast(Task, cast(Task, self.waitTask()))
        if int64(cast(WorkerTaskRec, w).destination) == int64(I_HANDLERA):
            dest: int64 = int64(I_HANDLERB)
        else:
            dest = int64(I_HANDLERA)
        cast(WorkerTaskRec, w).destination = box(int64(dest))
        cast(Packet, pkt).ident = box(int64(dest))
        cast(Packet, pkt).datum = 0
        i = 0
        while i < BUFSIZE:
            x: int64 = int64(cast(WorkerTaskRec, w).count) + 1
            cast(WorkerTaskRec, w).count = box(int64(x))
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
            IdleTask(int64(I_IDLE), 1, 10000, TaskState().running(), IdleTaskRec())
            wkq: Optional[Packet] = Packet(None, 0, int64(K_WORK))
            wkq = Packet(wkq, 0, int64(K_WORK))
            WorkTask(int64(I_WORK), 1000, wkq, cast(TaskState, TaskState().waitingWithPacket()), WorkerTaskRec())
            wkq = Packet(None, int64(I_DEVA), int64(K_DEV))
            wkq = Packet(wkq, int64(I_DEVA), int64(K_DEV))
            wkq = Packet(wkq, int64(I_DEVA), int64(K_DEV))
            HandlerTask(int64(I_HANDLERA), 2000, wkq, cast(TaskState, TaskState().waitingWithPacket()), HandlerTaskRec())
            wkq = Packet(None, int64(I_DEVB), int64(K_DEV))
            wkq = Packet(wkq, int64(I_DEVB), int64(K_DEV))
            wkq = Packet(wkq, int64(I_DEVB), int64(K_DEV))
            HandlerTask(int64(I_HANDLERB), 3000, wkq, cast(TaskState, TaskState().waitingWithPacket()), HandlerTaskRec())
            wkq = None
            DeviceTask(int64(I_DEVA), 4000, wkq, TaskState().waiting(), DeviceTaskRec())
            DeviceTask(int64(I_DEVB), 5000, wkq, TaskState().waiting(), DeviceTaskRec())
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