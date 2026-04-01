"""Benchmark-side helpers that operate only on prepared runnable files."""

from __future__ import annotations

import sys
from pathlib import Path

from artifact_runner import RunResult, run_python_artifact, write_run_result

BENCHMARK_ROOT = Path('static-python-perf/Benchmark')
CINDER_PYTHON = Path('cinder_env/bin/python')


def resolve_benchmark_path(path_or_name: str) -> Path:
    candidate = Path(path_or_name)
    if candidate.exists():
        return candidate
    if '/' not in path_or_name:
        benchmark_main = BENCHMARK_ROOT / path_or_name / 'advanced' / 'main.py'
        if benchmark_main.exists():
            return benchmark_main
    print(f'Error: file not found: {candidate}', file=sys.stderr)
    raise SystemExit(1)


def benchmark_output_dir(source_path: Path) -> Path:
    try:
        benchmark_index = source_path.parts.index('Benchmark')
        relative = Path(*source_path.parts[benchmark_index + 1:-1])
    except (ValueError, TypeError):
        relative = Path(source_path.parent.name)
    return Path('detyped_files') / relative


def run_prepared_artifact(artifact_path: Path, label: str) -> RunResult:
    result = run_python_artifact(CINDER_PYTHON, artifact_path, label=label)
    write_run_result(result)
    return result
