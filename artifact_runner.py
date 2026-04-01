"""Run and inspect prepared Python artifacts without knowing how they were made."""

from __future__ import annotations

import json
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class RunResult:
    label: str
    file: str
    returncode: int
    stdout: str
    stderr: str


def run_python_artifact(
    python_executable: Path,
    artifact_path: Path,
    label: str | None = None,
) -> RunResult:
    proc = subprocess.run(
        [str(python_executable), str(artifact_path)],
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


def write_run_result(result: RunResult, output_path: Path | None = None) -> Path:
    target = output_path or Path(result.file).with_name(f'run_result_{result.label}.json')
    target.write_text(json.dumps(asdict(result), indent=2, sort_keys=True) + '\n', encoding='utf-8')
    return target


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


def raise_for_failed_run(result: RunResult) -> None:
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
