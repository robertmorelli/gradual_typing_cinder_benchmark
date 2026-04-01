# Gradual Typing Cinder Benchmark

This repo has two main jobs:

- `detyper/` prepares transformed Python source variants
- the benchmark scripts run prepared Python files under the local Cinder runtime

## Run Benchmarks

Run the default stabilized benchmark:

```bash
python3 bench.py
```

Run a specific benchmark file:

```bash
python3 bench.py main.py
python3 bench.py static-python-perf/Benchmark/nbody/advanced/main.py
```

Run files relative to a benchmark directory:

```bash
python3 bench.py --benchmark-dir static-python-perf/Benchmark/nbody/advanced main.py
```

`bench.py` uses `stabalize.py`, which repeatedly runs the benchmark until the timing estimate stabilizes.

## Run Bench Status

Run the full typed-vs-detyped sweep:

```bash
python3 get_bench_status.py
```

That script:

- prepares typed and fully-detyped artifacts
- runs both under Cinder
- writes [bench_status.md](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/bench_status.md)

Look in [bench_status.md](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/bench_status.md) for:

- `Detyping works`
- `Detyping broken`
- `Benchmark broken`

Generated benchmark artifacts and run results live under [detyped_files](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyped_files).

## Run The Detyper

Print a variant without running it:

```bash
python3 detype.py static-python-perf/Benchmark/call_simple/advanced/main.py --show-perm 0x0
```

Write a specific variant:

```bash
python3 detype.py static-python-perf/Benchmark/call_simple/advanced/main.py --write-perm 0x3f --output-dir /tmp/detyper-out
```

Write all variants:

```bash
python3 detype.py static-python-perf/Benchmark/call_simple/advanced/main.py --write-all --output-dir /tmp/detyper-out
```

Write a typed baseline, intermediate random variants, and a fully detyped variant:

```bash
python3 detype.py static-python-perf/Benchmark/call_simple/advanced/main.py --write-by-proportion --output-dir /tmp/detyper-out
```

## Intent Lookup

If you want to answer:

> "This kind of type in this kind of location causes what edits?"

the source of truth is [detyper/rules.py](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyper/rules.py).

The main policy tables are:

- [PARAM_POLICIES](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyper/rules.py#L123)
- [BODY_POLICIES](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyper/rules.py#L147)
- [RETURN_POLICIES](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyper/rules.py#L162)

Examples:

- parameter annotation -> `definition_edits` + `call_edits`
- body annotation -> `annotation_edits`
- return annotation -> `definition_edits` + `value_edits` + `call_edits`

The code that turns those policy rows into actual intents is [detyper/generators.py](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyper/generators.py).

## Intent Merging

If you want to answer:

> "I have intent A and intent B on the same node. What happens?"

the canonical combiner is [resolve_same_node_intentions()](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyper/tasks.py#L152).

That function is the intended place to read the rule.

Supporting pieces:

- intent data model: [Intent](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyper/tasks.py#L32)
- same-kind merge: [merge_intentions_of_same_kind()](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyper/tasks.py#L108)
- execution order: [INTENTION_EXECUTION_ORDER](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyper/tasks.py#L126)
- application dispatch: [apply_intent()](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyper/tasks.py#L368)

`Detyper` itself just:

- collects intents
- groups them by node
- canonicalizes each same-node group
- applies the surviving intents

See [Detyper](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyper/tasks.py#L387).

## Useful Files

- [bench.py](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/bench.py): stabilized benchmark entrypoint
- [stabalize.py](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/stabalize.py): repeated-run stabilizer
- [get_bench_status.py](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/get_bench_status.py): full typed-vs-detyped sweep
- [benchmark_harness.py](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/benchmark_harness.py): benchmark-side runner glue
- [artifact_runner.py](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/artifact_runner.py): run prepared Python artifacts
- [detyper/artifacts.py](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyper/artifacts.py): prepare transformed artifacts
- [detyper/pipeline.py](/Users/robertmorelli/Documents/personal-repos/gradual_typing_cinder_benchmark/detyper/pipeline.py): pure source-to-source transform
