from __future__ import annotations

import random
import statistics
from dataclasses import dataclass
from pathlib import Path

from .artifact_runner import TimedRunResult, run_timed_python_artifact_detailed


DEFAULT_BATCH_SIZE = 8
DEFAULT_TOLERANCE = 0.1
DEFAULT_ALPHA = 0.05
DEFAULT_MAX_ITERATIONS = 50
BOOTSTRAP_RESAMPLES = 10_000
DEFAULT_RUN_RETRIES = 20


@dataclass(frozen=True)
class StdevBootstrap:
    stdev: float
    ci_lower: float
    ci_upper: float


@dataclass(frozen=True)
class StabilizedRun:
    runs: list[TimedRunResult]
    mean: float
    stdev: float
    ci_lower: float
    ci_upper: float
    batches: int
    converged: bool


def run_benchmark_script_detailed(
    script_path: Path,
    retries: int = DEFAULT_RUN_RETRIES,
    skip_typecheck: bool = False,
) -> TimedRunResult:
    for attempt in range(retries + 1):
        try:
            return run_timed_python_artifact_detailed(script_path, skip_typecheck=skip_typecheck)
        except (OSError, RuntimeError):
            if attempt == retries:
                raise

    raise AssertionError('unreachable')


def sample_stdev(timings: list[float]) -> float:
    if len(timings) < 2:
        return 0.0
    return statistics.stdev(timings)


def bootstrap_stdev(
    timings: list[float],
    rng: random.Random,
    resamples: int = BOOTSTRAP_RESAMPLES,
    alpha: float = DEFAULT_ALPHA,
) -> StdevBootstrap:
    if len(timings) < 2:
        return StdevBootstrap(stdev=0.0, ci_lower=0.0, ci_upper=0.0)

    stdevs = sorted(
        sample_stdev(rng.choices(timings, k=len(timings)))
        for _ in range(resamples)
    )
    lower = int((alpha / 2) * len(stdevs))
    upper = int((1 - alpha / 2) * len(stdevs)) - 1
    return StdevBootstrap(
        stdev=sample_stdev(timings),
        ci_lower=stdevs[max(0, lower)],
        ci_upper=stdevs[min(len(stdevs) - 1, upper)],
    )


def run_until_stable(
    script_path: Path,
    rng: random.Random,
    batch_size: int = DEFAULT_BATCH_SIZE,
    max_iterations: int = DEFAULT_MAX_ITERATIONS,
    tolerance: float = DEFAULT_TOLERANCE,
    skip_typecheck: bool = False,
) -> StabilizedRun:
    runs: list[TimedRunResult] = []

    for batch_number in range(1, max_iterations + 2):
        for _ in range(batch_size):
            runs.append(run_benchmark_script_detailed(script_path, skip_typecheck=skip_typecheck))

        timings = [run.timing for run in runs]
        stdev = bootstrap_stdev(timings, rng)
        mean = statistics.fmean(timings)
        converged = stdev.ci_upper <= abs(mean * tolerance)
        if converged or batch_number == max_iterations + 1:
            return StabilizedRun(
                runs=runs,
                mean=mean,
                stdev=stdev.stdev,
                ci_lower=stdev.ci_lower,
                ci_upper=stdev.ci_upper,
                batches=batch_number,
                converged=converged,
            )

    raise AssertionError('unreachable')
