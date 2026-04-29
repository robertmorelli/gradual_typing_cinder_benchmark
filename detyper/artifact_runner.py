"""Run and inspect prepared Python artifacts without knowing how they were made."""

from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass
from pathlib import Path

CINDER_DAEMON_NAME = 'cinder-env-daemon'
INFRA_RETRIES = 2


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
    skip_typecheck: bool = False,
) -> RunResult:
    command = [_artifact_python_executable()]
    if skip_typecheck:
        command.append('--skip-typecheck')
    command.append(str(artifact_path))

    proc = subprocess.run(
        command,
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


def should_reset_cinder_daemon(result: RunResult) -> bool:
    output = result.stderr + result.stdout
    return (
        result.returncode == 137
        or f'container name "/{CINDER_DAEMON_NAME}" is already in use' in output
        or 'is not running' in output
    )


def reset_cinder_daemon() -> None:
    subprocess.run(
        ['docker', 'rm', '-f', CINDER_DAEMON_NAME],
        capture_output=True,
        text=True,
    )


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
    skip_typecheck: bool = False,
) -> TimedRunResult:
    for attempt in range(INFRA_RETRIES + 1):
        result = run_python_artifact(artifact_path, label=label, skip_typecheck=skip_typecheck)
        try:
            raise_for_failed_run(result, require_parseable_time=True)
        except RuntimeError:
            if attempt < INFRA_RETRIES and should_reset_cinder_daemon(result):
                reset_cinder_daemon()
                continue
            raise

        timing = parse_stdout_time(result.stdout)
        if timing is None:
            raise RuntimeError(
                f'artifact {result.label} produced no parseable timing output:\n'
                f'{result.stdout or result.stderr}'
            )
        return TimedRunResult(timing=timing, result=result)

    raise AssertionError('unreachable')


def run_typecheck_python_artifact(
    artifact_path: Path,
    label: str | None = None,
) -> RunResult:
    command = [
        _artifact_python_executable(),
        '--typecheck-only',
        str(artifact_path),
    ]
    proc = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )
    result = RunResult(
        label=label or artifact_path.stem,
        file=str(artifact_path),
        returncode=proc.returncode,
        stdout=proc.stdout,
        stderr=proc.stderr,
    )
    raise_for_failed_run(result)
    return result
