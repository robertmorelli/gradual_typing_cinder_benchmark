from __future__ import annotations

from pathlib import Path

from .artifact_runner import TimedRunResult, run_timed_python_artifact_detailed


DEFAULT_BATCH_SIZE = 8
DEFAULT_TOLERANCE = 0.1
DEFAULT_ALPHA = 0.05
DEFAULT_MAX_ITERATIONS = 50
BOOTSTRAP_RESAMPLES = 10_000
DEFAULT_RUN_RETRIES = 20


def run_benchmark_script_detailed(
    script_path: Path,
    retries: int = DEFAULT_RUN_RETRIES,
) -> TimedRunResult:
    for attempt in range(retries + 1):
        try:
            return run_timed_python_artifact_detailed(script_path)
        except (OSError, RuntimeError):
            if attempt == retries:
                raise

    raise AssertionError('unreachable')
