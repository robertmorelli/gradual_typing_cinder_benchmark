
## body box primitive

From:
```python
def bump() -> int64:
    n: int64 = 41
    return n + 1
```

To:
```python
# detyper-status: types_removed
def bump() -> int64:
    n = box(int64(41))
    return int64(n) + 1
```

## body cast all

From:
```python
class Widget:
    def tick(self) -> None:
        return None


def make_widget() -> Widget:
    return Widget()


def run() -> None:
    w: Widget = make_widget()
    w.tick()
```

To:
```python
class Widget:

    # detyper-status: types_kept
    def tick(self) -> None:
        return None

# detyper-status: types_kept
def make_widget() -> Widget:
    return Widget()

# detyper-status: types_removed
def run() -> None:
    w = cast(Widget, make_widget())
    cast(Widget, w).tick()
```

## body cast container passthrough

From:
```python
def first_value(xs: Array[int64]) -> int64:
    arr: Array[int64] = xs
    return arr[int64(0)]
```

To:
```python
# detyper-status: types_removed
def first_value(xs: Array[int64]) -> int64:
    arr = cast(Array[int64], xs)
    return cast(Array[int64], arr)[int64(0)]
```

## body construct container

From:
```python
def first_value() -> int64:
    xs: CheckedList[int64] = CheckedList[int64]([1, 2, 3])
    return xs[0]
```

To:
```python
# detyper-status: types_removed
def first_value() -> int64:
    xs = CheckedList[int64]([1, 2, 3])
    return int64(xs[0])
```

## body detype none

From:
```python
def keep_none_annotation():
    x: None = None
    return x
```

To:
```python
def keep_none_annotation():
    x: None = None
    return x
```

## checkedlist reprojection

From:
```python
def bar(xs: CheckedList[int64], ys: CheckedList[int64]) -> None:
    xs.append(int64(2))
    ys.append(int64(3))


def foo() -> int64:
    x: CheckedList[int64] = CheckedList[int64]()
    x.append(int64(1))
    y: CheckedList[int64] = CheckedList[int64]()
    y.append(int64(4))
    bar(x, y)
    return x[int64(1)] + y[int64(1)]
```

To:
```python
def _repro_bar_arg0(f, arg0, arg1):
    _arg0 = CheckedList[int64](arg0)
    _out = f(_arg0, arg1)
    arg0.clear()
    arg0.extend(_arg0)
    return _out


def _repro__repro_bar_arg0_arg2(f, arg0, arg1, arg2):
    _arg2 = CheckedList[int64](arg2)
    _out = f(arg0, arg1, _arg2)
    arg2.clear()
    arg2.extend(_arg2)
    return _out




def bar(xs, ys) -> None:
    xs = cast(CheckedList[int64], xs)
    ys = cast(CheckedList[int64], ys)
    xs.append(int64(2))
    ys.append(int64(3))


def foo() -> int64:
    x = CheckedList[int64](CheckedList[int64]())
    x.append(int64(1))
    y = CheckedList[int64](CheckedList[int64]())
    y.append(int64(4))
    _repro__repro_bar_arg0_arg2(_repro_bar_arg0, bar, x, y)
    return int64(x[int64(1)]) + int64(y[int64(1)])
```

## cleanup checkedlist return wraps

From:
```python
x = CheckedList[int64](foo())


def foo():
    return CheckedList[int64]([int64(1)])
```

To:
```python
x = CheckedList[int64](foo())


def foo():
    return [int64(1)]
```

## inline cleanup

From:
```python
@inline
def project(_x):
    x: int64 = int64(_x)
    return x
```

To:
```python
@inline
# detyper-status: types_removed
def project(_x):
    return int64(_x)
```

## param box primitive

From:
```python
def add_one(x: int64) -> int64:
    return x + 1


def use(v: int64) -> int64:
    out: int64 = add_one(v)
    return out
```

To:
```python
# detyper-status: types_removed
def add_one(_x) -> int64:
    x: int64 = int64(_x)
    return x + 1

# detyper-status: types_kept
def use(v: int64) -> int64:
    out: int64 = add_one(box(v))
    return out
```

## param cast all

From:
```python
class Foo:
    pass


def echo(foo: Foo) -> Foo:
    return foo


def use(x: Foo) -> Foo:
    out: Foo = echo(x)
    return out
```

To:
```python
class Foo:
    pass

# detyper-status: types_removed
def echo(_foo) -> Foo:
    foo: Foo = cast(Foo, _foo)
    return foo

# detyper-status: types_kept
def use(x: Foo) -> Foo:
    out: Foo = echo(cast(Foo, x))
    return out
```

## param cast container passthrough

From:
```python
def first(xs: Array[int64]) -> int64:
    return xs[int64(0)]


def use(src: Array[int64]) -> int64:
    out: int64 = first(src)
    return out
```

To:
```python
# detyper-status: types_removed
def first(_xs) -> int64:
    xs: Array[int64] = cast(Array[int64], _xs)
    return xs[int64(0)]

# detyper-status: types_kept
def use(src: Array[int64]) -> int64:
    out: int64 = first(cast(Array[int64], src))
    return out
```

## param construct container

From:
```python
def first(xs: CheckedList[int64]) -> int64:
    return xs[0]


def use(src: CheckedList[int64]) -> int64:
    out: int64 = first(src)
    return out
```

To:
```python
# detyper-status: types_removed
def first(xs) -> int64:
    xs = cast(CheckedList[int64], xs)
    return xs[0]

# detyper-status: types_kept
def use(src: CheckedList[int64]) -> int64:
    out: int64 = first(CheckedList[int64](src))
    return out
```

## param detype none

From:
```python
def echo(x):
    return x
```

To:
```python
def echo(x):
    return x
```

## return box primitive

From:
```python
def inc(x: int64) -> int64:
    return x + 1


def use(v: int64) -> int64:
    out: int64 = inc(v)
    return out
```

To:
```python
# detyper-status: types_removed
def inc(x: int64):
    return box(int64(x + 1))

# detyper-status: types_kept
def use(v: int64) -> int64:
    out: int64 = int64(inc(v))
    return out
```

## return cast all

From:
```python
class Foo:
    pass


def make_foo() -> Foo:
    return Foo()


def use() -> Foo:
    out: Foo = make_foo()
    return out
```

To:
```python
class Foo:
    pass

# detyper-status: types_removed
def make_foo():
    return Foo()

# detyper-status: types_kept
def use() -> Foo:
    out: Foo = cast(Foo, make_foo())
    return out
```

## return cast container passthrough

From:
```python
def make_items(xs: Array[int64]) -> Array[int64]:
    return xs


def use(v: Array[int64]) -> int64:
    out: Array[int64] = make_items(v)
    return out[int64(0)]
```

To:
```python
# detyper-status: types_removed
def make_items(xs: Array[int64]):
    return xs

# detyper-status: types_kept
def use(v: Array[int64]) -> int64:
    out: Array[int64] = cast(Array[int64], make_items(v))
    return out[int64(0)]
```

## return construct container

From:
```python
def make_items() -> CheckedList[int64]:
    return CheckedList[int64]([1, 2, 3])


def use() -> int64:
    out: CheckedList[int64] = make_items()
    return out[0]
```

To:
```python
# detyper-status: types_removed
def make_items():
    return [1, 2, 3]

# detyper-status: types_kept
def use() -> int64:
    out: CheckedList[int64] = CheckedList[int64](make_items())
    return out[0]
```

## return detype none

From:
```python
def reset() -> None:
    pass


def greet(name: str) -> None:
    print(name)
```

To:
```python
# detyper-status: types_removed
def reset():
    pass


# detyper-status: types_removed
def greet(name: str):
    print(name)
```

## wrapper cleanup

From:
```python
class Foo:
    pass


def demo(x):
    a = cast(Foo, cast(Foo, x))
    b = int64(int64(1))
    c = box(box(int64(2)))
    return a, b, c
```

To:
```python
class Foo:
    pass

# detyper-status: types_kept
def demo(x):
    a = cast(Foo, x)
    b = int64(1)
    c = box(int64(2))
    return (a, b, c)
```
