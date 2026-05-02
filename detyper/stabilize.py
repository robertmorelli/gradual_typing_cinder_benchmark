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
class MeanBootstrap:
    mean: float
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


def bootstrap_mean(
    timings: list[float],
    rng: random.Random,
    resamples: int = BOOTSTRAP_RESAMPLES,
    alpha: float = DEFAULT_ALPHA,
) -> MeanBootstrap:
    """Bootstrap percentile CI for the mean.

    Follows Rosenbaum (Design of Observational Studies): resample with
    replacement, compute the mean of each resample, take the alpha/2 and
    1-alpha/2 percentiles of those means.
    """
    point = statistics.fmean(timings) if timings else 0.0
    if len(timings) < 2:
        return MeanBootstrap(mean=point, ci_lower=point, ci_upper=point)
    means = sorted(
        statistics.fmean(rng.choices(timings, k=len(timings)))
        for _ in range(resamples)
    )
    lower_idx = int((alpha / 2) * len(means))
    upper_idx = int((1 - alpha / 2) * len(means)) - 1
    return MeanBootstrap(
        mean=point,
        ci_lower=means[max(0, lower_idx)],
        ci_upper=means[min(len(means) - 1, upper_idx)],
    )


def run_until_stable(
    script_path: Path,
    rng: random.Random,
    batch_size: int = DEFAULT_BATCH_SIZE,
    max_iterations: int = DEFAULT_MAX_ITERATIONS,
    tolerance: float = DEFAULT_TOLERANCE,
    skip_typecheck: bool = False,
) -> StabilizedRun:
    """Run the benchmark in batches until the bootstrap CI on the mean is
    tight enough.

    Stopping rule: stop when the 95% bootstrap CI on the sample mean lies
    within +/- tolerance * mean of the sample mean (matching Rosenbaum's
    containment criterion).
    """
    runs: list[TimedRunResult] = []
    for batch_number in range(1, max_iterations + 2):
        for _ in range(batch_size):
            runs.append(run_benchmark_script_detailed(script_path, skip_typecheck=skip_typecheck))
        timings = [run.timing for run in runs]
        boot = bootstrap_mean(timings, rng)
        mean = boot.mean
        half_width = tolerance * abs(mean)
        converged = (
            boot.ci_lower >= mean - half_width
            and boot.ci_upper <= mean + half_width
        )
        if converged or batch_number == max_iterations + 1:
            return StabilizedRun(
                runs=runs,
                mean=mean,
                stdev=sample_stdev(timings),
                ci_lower=boot.ci_lower,
                ci_upper=boot.ci_upper,
                batches=batch_number,
                converged=converged,
            )
    raise AssertionError('unreachable')