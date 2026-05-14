from __static__ import int64, cbool

class Foo:
    def __init__(self, x: int64) -> None:
        self.x: int64 = x

    def is_pos(self) -> cbool:
        return cbool(self.x > 0)


def main() -> None:
    f = Foo(int64(5))
    print(f.is_pos())
