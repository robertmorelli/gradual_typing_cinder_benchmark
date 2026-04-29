"""Run and inspect prepared Python artifacts without knowing how they were made."""

from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RunResult:
    label: str
    file: str
    returncode: int
    stdout: str
    stderr: str


@dataclass(frozen=True)
class TimedRunResult:
    timing: float
    result: RunResult


def _artifact_python_executable() -> str:
    cinder_python = os.environ.get('CINDER_PYTHON')
    if cinder_python:
        return cinder_python

    cinder_env = os.environ.get('CINDER_ENV')
    if cinder_env:
        candidate = Path(cinder_env) / 'bin' / 'python'
        if candidate.exists():
            return str(candidate)

    local_candidate = Path('cinder_env/bin/python')
    if local_candidate.exists():
        return str(local_candidate)

    raise RuntimeError(
        'Could not find the Cinder Python runtime. Set CINDER_PYTHON or CINDER_ENV, '
        'or run setup so cinder_env/bin/python exists.'
    )


def run_python_artifact(
    artifact_path: Path,
    label: str | None = None,
) -> RunResult:
    proc = subprocess.run(
        [_artifact_python_executable(), str(artifact_path)],
        capture_output=True,
        text=True,
    )
    return RunResult(
        label=label or artifact_path.stem,
        file=str(artifact_path),
        returncode=proc.returncode,
        stdout=proc.stdout,
        stderr=proc.stderr,
    )


def parse_stdout_time(stdout: str) -> float | None:
    try:
        return float(stdout.strip().splitlines()[0])
    except (ValueError, IndexError):
        return None


def non_jit_stderr_lines(stderr: str) -> list[str]:
    bad: list[str] = []
    for raw in stderr.splitlines():
        line = raw.strip()
        if not line:
            continue
        if not line.startswith('JIT:'):
            bad.append(raw)
    return bad


def raise_for_failed_run(result: RunResult, *, require_parseable_time: bool = False) -> None:
    if result.returncode != 0:
        raise RuntimeError(
            f'artifact {result.label} failed (exit {result.returncode}):\n'
            f'{result.stderr or result.stdout}'
        )

    bad_stderr = non_jit_stderr_lines(result.stderr)
    if bad_stderr:
        preview = '\n'.join(bad_stderr[:20])
        raise RuntimeError(
            f'artifact {result.label} emitted non-JIT stderr:\n{preview}'
        )

    if require_parseable_time and parse_stdout_time(result.stdout) is None:
        raise RuntimeError(
            f'artifact {result.label} produced no parseable timing output:\n'
            f'{result.stdout or result.stderr}'
        )


def run_timed_python_artifact_detailed(
    artifact_path: Path,
    label: str | None = None,
) -> TimedRunResult:
    result = run_python_artifact(artifact_path, label=label)
    raise_for_failed_run(result, require_parseable_time=True)
    timing = parse_stdout_time(result.stdout)
    if timing is None:
        raise RuntimeError(
            f'artifact {result.label} produced no parseable timing output:\n'
            f'{result.stdout or result.stderr}'
        )
    return TimedRunResult(timing=timing, result=result)
