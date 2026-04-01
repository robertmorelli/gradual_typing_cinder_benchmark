from __future__ import annotations

import random
import statistics
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class StabilizationResult:
    mean: float
    stdev: float
    total_samples: int
    batches: int
    converged: bool
    ci_lower: float
    ci_upper: float


def _default_python_executable() -> str:
    cinder_python = Path('cinder_env/bin/python')
    if cinder_python.exists():
        return str(cinder_python)
    return sys.executable


def foo_stabilizer(foo, batch_size=8, tolerance=0.1, alpha=0.05, max_iterations=50) -> StabilizationResult:
    data = [foo() for _ in range(batch_size)]
    batches = 1
    for _ in range(max_iterations):
        sample_mean = statistics.fmean(data)
        resample_means = sorted(
            statistics.fmean(random.choices(data, k=len(data)))
            for _ in range(10_000)
        )
        lower_index = int((alpha / 2) * len(resample_means))
        upper_index = int((1 - alpha / 2) * len(resample_means)) - 1
        ci_lower = resample_means[max(0, lower_index)]
        ci_upper = resample_means[min(len(resample_means) - 1, upper_index)]
        margin = abs(sample_mean * tolerance)
        if (sample_mean - margin) <= ci_lower and ci_upper <= (sample_mean + margin):
            return StabilizationResult(
                mean=sample_mean,
                stdev=statistics.stdev(data),
                total_samples=len(data),
                batches=batches,
                converged=True,
                ci_lower=ci_lower,
                ci_upper=ci_upper,
            )
        data.extend(foo() for _ in range(batch_size))
        batches += 1

    sample_mean = statistics.fmean(data)
    resample_means = sorted(
        statistics.fmean(random.choices(data, k=len(data)))
        for _ in range(10_000)
    )
    lower_index = int((alpha / 2) * len(resample_means))
    upper_index = int((1 - alpha / 2) * len(resample_means)) - 1
    ci_lower = resample_means[max(0, lower_index)]
    ci_upper = resample_means[min(len(resample_means) - 1, upper_index)]
    return StabilizationResult(
        mean=sample_mean,
        stdev=statistics.stdev(data),
        total_samples=len(data),
        batches=batches,
        converged=False,
        ci_lower=ci_lower,
        ci_upper=ci_upper,
    )


def run_benchmark_script(script_path: Path, python_executable: str | None = None) -> float:
    executable = python_executable or _default_python_executable()
    proc = subprocess.run(
        [executable, str(script_path)],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f'benchmark script failed ({proc.returncode}): {script_path}\n'
            f'{proc.stderr or proc.stdout}'
        )
    return float(proc.stdout.strip().splitlines()[0])


def main() -> None:
    if len(sys.argv) != 2:
        print('usage: python stabalize.py <benchmark_script>', file=sys.stderr)
        raise SystemExit(1)

    script_path = Path(sys.argv[1])
    result = foo_stabilizer(lambda: run_benchmark_script(script_path))
    print(f'{script_path.name}: {result.mean:.4f} (batches={result.batches}, converged={result.converged})')


if __name__ == '__main__':
    main()
