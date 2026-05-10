# Cinder compiler internal crash 1

## Summary

Cinder static compilation crashed with an internal `KeyError` while typechecking a generated Richards sample.

This was not a normal `TypedSyntaxError`; the compiler raised an uncaught exception while compiling an inline method that returns a boxed primitive boolean expression.

## Generated trigger

File:

```text
benchmark_results/random_samples/richards/advanced/sample_09_74of136.py
```

Relevant generated code:

```py
@inline
def isTaskHoldingOrWaiting(self):
    return box(cbool(cbool(self.task_holding) or (not self.packet_pending and self.task_waiting)))
```

Called from:

```py
if cbool(TaskState.isTaskHoldingOrWaiting(t)):
    t = t.link
```

## What triggered it

The generated code combines these ingredients:

1. `@inline` function.
2. Return expression is `box(cbool(...))`.
3. The `cbool(...)` argument is a `BoolOp` expression:

   ```py
   cbool(self.task_holding) or (not self.packet_pending and self.task_waiting)
   ```

4. The inline result is immediately passed through another primitive conversion at the callsite:

   ```py
   cbool(TaskState.isTaskHoldingOrWaiting(t))
   ```

During static codegen, Cinder inlines the function, then tries to emit primitive box/unbox code for the nested boolean expression. The compiler asks for the type of the inlined `ast.BoolOp`, but that node is missing from `cur_mod.types`, causing an internal `KeyError`.

## Full copied error tail

```text
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 1112, in visitIf
    self.compileJumpIf(node.test, orelse or end, False)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 1161, in compileJumpIf
    self.get_type(test).emit_jumpif(test, next, is_if_true, self)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 1137, in emit_jumpif
    code_gen.visit(test)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 3000, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 839, in visitCall
    self.get_type(node.func).emit_call(node, self)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 9378, in emit_call
    self.instance.emit_unbox(arg, code_gen)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 9210, in emit_unbox
    code_gen.visit(node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 3000, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 839, in visitCall
    self.get_type(node.func).emit_call(node, self)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 3741, in emit_call
    return self.emit_inline_call(node, code_gen)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 3825, in emit_inline_call
    code_gen.visit(inlined_call.expr)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 3000, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 839, in visitCall
    self.get_type(node.func).emit_call(node, self)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 6553, in emit_call
    code_gen.get_type(node.args[0]).emit_box(node.args[0], code_gen)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 9202, in emit_box
    code_gen.visit(node)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/pycodegen.py", line 3000, in visit
    ret = super().visit(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/visitor.py", line 70, in visit
    return meth(node, *args)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 839, in visitCall
    self.get_type(node.func).emit_call(node, self)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/types.py", line 9372, in emit_call
    arg_type = code_gen.get_type(arg)
  File "/cinder/cinderx/PythonLib/cinderx/compiler/static/__init__.py", line 275, in get_type
    return self.cur_mod.types[node]
KeyError: <ast.BoolOp object at 0x7ffffc491990>
```
