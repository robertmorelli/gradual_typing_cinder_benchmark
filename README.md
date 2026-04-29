# Gradual Typing Cinder Benchmark

Run setup once:

```bash
bash setup.sh
```

Run the experiment:

```bash
python3 run_experiment.py
```

Run a small smoke test:

```bash
python3 run_experiment.py --limit 1
```

Write one detyped file:

```bash
python3 make_detyped_file.py deltablue advanced 0x0
```

Refresh the benchmark status CSV:

```bash
python3 get_bench_status.py
```

`run_experiment.py` uses `bench_status.csv` when it exists and runs rows marked `all_green`. Outputs are CSV-only under `benchmark_results/experiment_<timestamp>/`.

Each experiment contains:

```text
<benchmark>_<advanced|shallow|untyped>_raw.csv
<benchmark>_<advanced|shallow|untyped>_summary.csv
files/
```

The benchmark orchestrator runs with `python3`. Prepared benchmark artifacts run with the Cinder Python runtime from `CINDER_PYTHON`, `CINDER_ENV/bin/python`, or `cinder_env/bin/python`.
