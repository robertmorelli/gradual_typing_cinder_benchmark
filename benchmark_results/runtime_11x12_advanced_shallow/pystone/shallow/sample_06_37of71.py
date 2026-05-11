"""
"PYSTONE" Benchmark Program
Static python port made by Sebastian Chaves (sebastiancr@fb.com) based on:


Version:        Python/1.2 (corresponds to C/1.1 plus 3 Pystone fixes)

Author:         Reinhold P. Weicker,  CACM Vol 27, No 10, 10/84 pg. 1013.

                Translated from ADA to C by Rick Richardson.
                Every method to preserve ADA-likeness has been used,
                at the expense of C-ness.

                Translated from C to Python by Guido van Rossum.

Version History:

                Removed built-in time measurement code to have a simpler
                import-less version of it.

                Version 1.1 corrects two bugs in version 1.0:

                First, it leaked memory: in Proc1(), NextRecord ends
                up having a pointer to itself.  I have corrected this
                by zapping NextRecord.PtrComp at the end of Proc1().

                Second, Proc3() used the operator != to compare a
                record to None.  This is rather inefficient and not
                true to the intention of the original benchmark (where
                a pointer comparison to None is intended; the !=
                operator attempts to find a method __cmp__ to do value
                comparison of the record).  Version 1.1 runs 5-10
                percent faster than version 1.0, so benchmark figures
                of different versions can't be compared directly.

                Version 1.2 changes the division to floor division.

                Under Python 3 version 1.1 would use the normal division
                operator, resulting in some of the operations mistakenly
                yielding floats. Version 1.2 instead uses floor division
                making the benchmark an integer benchmark again.

"""
from __future__ import annotations
import __static__
from __static__ import cast
from typing import Final, List
import time
LOOPS: Final[int] = 50000
__version__ = '1.2'
Ident1: Final[int] = 1
Ident2 = 2
Ident3: Final[int] = 3
Ident4: Final[int] = 4
Ident5: Final[int] = 5

class Record:

    def __init__(self, PtrComp: Record | None=None, Discr: int=0, EnumComp: int=0, IntComp=0, StringComp='\x00'):
        self.PtrComp = PtrComp
        self.Discr: int = Discr
        self.EnumComp = EnumComp
        self.IntComp: int = IntComp
        self.StringComp = StringComp

    def copy(self):
        return Record(cast(Record | None, self.PtrComp), self.Discr, self.EnumComp, self.IntComp, self.StringComp)
TRUE: Final[bool] = True
FALSE = False

def pystones(loops=LOOPS):
    Proc0(loops)
IntGlob: int = 0
BoolGlob: bool = FALSE
Char1Glob = '\x00'
Char2Glob: str = '\x00'
Array1Glob: List[int] = [0] * 51
Array2Glob: List[List[int]] = [x[:] for x in [Array1Glob] * 51]
PtrGlb = cast(Record | None, None)
PtrGlbNext = cast(Record | None, None)

def Proc0(loops=LOOPS):
    global IntGlob
    global BoolGlob
    global Char1Glob
    global Char2Glob
    global Array1Glob
    global Array2Glob
    global PtrGlb
    global PtrGlbNext
    for _i in range(loops):
        pass
    PtrGlbNext = Record()
    PtrGlb = Record()
    local_PtrGlb = PtrGlb
    assert local_PtrGlb is not None
    local_PtrGlb.PtrComp = PtrGlbNext
    local_PtrGlb.Discr = Ident1
    local_PtrGlb.EnumComp = Ident3
    local_PtrGlb.IntComp = 40
    local_PtrGlb.StringComp = 'DHRYSTONE PROGRAM, SOME STRING'
    String1Loc = "DHRYSTONE PROGRAM, 1'ST STRING"
    Array2Glob[8][7] = 10
    for _i in range(loops):
        Proc5()
        Proc4()
        IntLoc1: int = 2
        IntLoc2 = 3
        String2Loc: str = "DHRYSTONE PROGRAM, 2'ND STRING"
        EnumLoc = Ident2
        BoolGlob = not Func2(String1Loc, String2Loc)
        IntLoc3: int = 0
        while IntLoc1 < IntLoc2:
            IntLoc3 = 5 * IntLoc1 - IntLoc2
            IntLoc3 = Proc7(IntLoc1, IntLoc2)
            IntLoc1 = IntLoc1 + 1
        Proc8(Array1Glob, Array2Glob, IntLoc1, IntLoc3)
        PtrGlb = cast(Record, Proc1(local_PtrGlb))
        local_PtrGlb = PtrGlb
        assert local_PtrGlb is not None
        CharIndex = 'A'
        while CharIndex <= Char2Glob:
            if EnumLoc == Func1(CharIndex, 'C'):
                EnumLoc = Proc6(Ident1)
            CharIndex = chr(ord(CharIndex) + 1)
        IntLoc3 = IntLoc2 * IntLoc1
        IntLoc2 = IntLoc3 // IntLoc1
        IntLoc2 = 7 * (IntLoc3 - IntLoc2) - IntLoc1
        IntLoc1 = Proc2(IntLoc1)

def Proc1(PtrParIn):
    local_PtrGlb = PtrGlb
    assert local_PtrGlb is not None
    cast(Record, PtrParIn).PtrComp = NextRecord = local_PtrGlb.copy()
    cast(Record, PtrParIn).IntComp = 5
    NextRecord.IntComp = cast(Record, PtrParIn).IntComp
    NextRecord.PtrComp = cast(Record | None, cast(Record, PtrParIn).PtrComp)
    NextRecord.PtrComp = cast(Record | None, Proc3(cast(Record | None, NextRecord.PtrComp)))
    if NextRecord.Discr == Ident1:
        NextRecord.IntComp = 6
        NextRecord.EnumComp = Proc6(cast(Record, PtrParIn).EnumComp)
        NextRecord.PtrComp = cast(Record | None, local_PtrGlb.PtrComp)
        NextRecord.IntComp = Proc7(NextRecord.IntComp, 10)
    else:
        PtrParIn = NextRecord.copy()
    NextRecord.PtrComp = None
    return cast(Record, PtrParIn)

def Proc2(IntParIO: int):
    IntLoc: int = IntParIO + 10
    EnumLoc = 0
    while 1:
        if Char1Glob == 'A':
            IntLoc = IntLoc - 1
            IntParIO = IntLoc - IntGlob
            EnumLoc = Ident1
        if EnumLoc == Ident1:
            break
    return IntParIO

def Proc3(PtrParOut: Record | None):
    global IntGlob
    global PtrGlb
    local_PtrGlb = PtrGlb
    assert local_PtrGlb is not None
    if local_PtrGlb is not None:
        PtrParOut = cast(Record | None, local_PtrGlb.PtrComp)
    else:
        IntGlob = 100
    local_PtrGlb.IntComp = Proc7(10, IntGlob)
    PtrGlb = local_PtrGlb
    return cast(Record | None, PtrParOut)

def Proc4() -> None:
    global Char2Glob
    BoolLoc = Char1Glob == 'A'
    BoolLoc = BoolLoc or BoolGlob
    Char2Glob = 'B'

def Proc5():
    global Char1Glob
    global BoolGlob
    Char1Glob = 'A'
    BoolGlob = FALSE

def Proc6(EnumParIn: int):
    EnumParOut = EnumParIn
    if not Func3(EnumParIn):
        EnumParOut = Ident4
    if EnumParIn == Ident1:
        EnumParOut = Ident1
    elif EnumParIn == Ident2:
        if IntGlob > 100:
            EnumParOut = Ident1
        else:
            EnumParOut = Ident4
    elif EnumParIn == Ident3:
        EnumParOut = Ident2
    elif EnumParIn == Ident4:
        pass
    elif EnumParIn == Ident5:
        EnumParOut = Ident3
    return EnumParOut

def Proc7(IntParI1, IntParI2):
    IntLoc = IntParI1 + 2
    IntParOut: int = IntParI2 + IntLoc
    return IntParOut

def Proc8(Array1Par, Array2Par, IntParI1, IntParI2: int):
    global IntGlob
    IntLoc = IntParI1 + 5
    Array1Par[IntLoc] = IntParI2
    Array1Par[IntLoc + 1] = Array1Par[IntLoc]
    Array1Par[IntLoc + 30] = IntLoc
    for IntIndex in range(IntLoc, IntLoc + 2):
        Array2Par[IntLoc][IntIndex] = IntLoc
    Array2Par[IntLoc][IntLoc - 1] = Array2Par[IntLoc][IntLoc - 1] + 1
    Array2Par[IntLoc + 20][IntLoc] = Array1Par[IntLoc]
    IntGlob = 5

def Func1(CharPar1: str, CharPar2: str):
    CharLoc1 = CharPar1
    CharLoc2 = CharLoc1
    if CharLoc2 != CharPar2:
        return Ident1
    else:
        return Ident2

def Func2(StrParI1, StrParI2: str) -> bool:
    IntLoc: int = 1
    CharLoc = ''
    while IntLoc <= 1:
        if Func1(StrParI1[IntLoc], StrParI2[IntLoc + 1]) == Ident1:
            CharLoc = 'A'
            IntLoc = IntLoc + 1
    if CharLoc >= 'W' and CharLoc <= 'Z':
        IntLoc = 7
    if CharLoc == 'X':
        return TRUE
    elif StrParI1 > StrParI2:
        IntLoc = IntLoc + 7
        return TRUE
    else:
        return FALSE

def Func3(EnumParIn: int):
    EnumLoc: int = EnumParIn
    if EnumLoc == Ident3:
        return TRUE
    return FALSE

def run():
    loops: int = LOOPS
    pystones(loops)
if __name__ == '__main__':
    import sys
    num_iterations = 2
    if len(sys.argv) > 1:
        num_iterations = int(sys.argv[1])
    startTime = time.time()
    for _ in range(num_iterations):
        run()
    endTime = time.time()
    runtime = endTime - startTime
    print(runtime)