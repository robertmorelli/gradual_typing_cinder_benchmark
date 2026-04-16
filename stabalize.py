from __future__ import annotations

import random
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path

from artifact_runner import TimedRunResult, run_timed_python_artifact, run_timed_python_artifact_detailed


@dataclass(frozen=True)
class StabilizationResult:
    mean: float
    stdev: float
    total_samples: int
    batches: int
    converged: bool
    ci_lower: float
    ci_upper: float


DEFAULT_BATCH_SIZE = 8
DEFAULT_TOLERANCE = 0.1
DEFAULT_ALPHA = 0.05
DEFAULT_MAX_ITERATIONS = 50
BOOTSTRAP_RESAMPLES = 10_000
DEFAULT_RUN_RETRIES = 20


def foo_stabilizer(
    foo,
    batch_size: int = DEFAULT_BATCH_SIZE,
    tolerance: float = DEFAULT_TOLERANCE,
    alpha: float = DEFAULT_ALPHA,
    max_iterations: int = DEFAULT_MAX_ITERATIONS,
) -> StabilizationResult:
    data = [foo() for _ in range(batch_size)]
    batches = 1
    for _ in range(max_iterations):
        sample_mean = statistics.fmean(data)
        resample_means = sorted(
            statistics.fmean(random.choices(data, k=len(data)))
            for _ in range(BOOTSTRAP_RESAMPLES)
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
        for _ in range(BOOTSTRAP_RESAMPLES)
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


def run_benchmark_script(script_path: Path, retries: int = DEFAULT_RUN_RETRIES) -> float:
    return run_benchmark_script_detailed(script_path, retries=retries).timing


@dataclass(frozen=True)
class DetailedBenchmarkRun:
    timing: float
    attempts: int
    timed_run: TimedRunResult
    attempt_errors: tuple[str, ...]


def run_benchmark_script_detailed(
    script_path: Path,
    retries: int = DEFAULT_RUN_RETRIES,
) -> DetailedBenchmarkRun:
    attempt_errors: list[str] = []
    attempts = retries + 1
    for attempt in range(1, attempts + 1):
        try:
            timed_run = run_timed_python_artifact_detailed(script_path)
            return DetailedBenchmarkRun(
                timing=timed_run.timing,
                attempts=attempt,
                timed_run=timed_run,
                attempt_errors=tuple(attempt_errors),
            )
        except (OSError, RuntimeError) as exc:
            attempt_errors.append(str(exc))
            if attempt == attempts:
                raise

    raise AssertionError('unreachable')


def main() -> None:
    if len(sys.argv) != 2:
        print('usage: python stabalize.py <benchmark_script>', file=sys.stderr)
        raise SystemExit(1)

    script_path = Path(sys.argv[1])
    result = foo_stabilizer(lambda: run_benchmark_script(script_path))
    print(f'{script_path.name}: {result.mean:.4f} (batches={result.batches}, converged={result.converged})')


if __name__ == '__main__':
    main()
