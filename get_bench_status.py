"""Prepare artifacts, run them, and write bench_status.md."""

from __future__ import annotations

from pathlib import Path

from artifact_runner import RunResult, raise_for_failed_run
from benchmark_harness import BENCHMARK_ROOT, benchmark_output_dir, resolve_benchmark_path, run_prepared_artifact
from detyper.artifacts import build_source_variant, load_source_artifacts

OUT_FILE = Path('bench_status.md')


def _benchmarks_with_advanced_main() -> list[str]:
    return sorted(path.parent.parent.name for path in BENCHMARK_ROOT.glob('*/advanced/main.py'))


def _benchmarks_without_advanced_main() -> list[str]:
    return sorted(
        path.name for path in BENCHMARK_ROOT.iterdir()
        if path.is_dir() and not (path / 'advanced' / 'main.py').exists()
        and path.name != '__pycache__'
    )


def _unordered_list(items: list[str]) -> str:
    if not items:
        return ''
    return '\n'.join(f'- {item}' for item in sorted(items)) + '\n'


def _write_labeled_artifact(source_path: Path, variant: tuple[bool, ...], label: str) -> Path:
    artifacts = load_source_artifacts(source_path, output_dir=benchmark_output_dir(source_path))
    program = build_source_variant(artifacts, variant)
    out_dir = artifacts.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f'{artifacts.source_stem}_{program.perm_hex}_{label}.py'
    out_path.write_text(program.source, encoding='utf-8')
    return out_path


def _run_test_triplet(name: str) -> tuple[RunResult, RunResult, RunResult]:
    source_path = resolve_benchmark_path(name)
    artifacts = load_source_artifacts(source_path)
    n = len(artifacts.variant_names)

    typed_path = _write_labeled_artifact(source_path, tuple(False for _ in range(n)), 'typed')
    detyped_path = _write_labeled_artifact(source_path, tuple(True for _ in range(n)), 'detyped')
    untyped_path = resolve_benchmark_path(name, variant='untyped')

    return (
        run_prepared_artifact(typed_path, label='typed'),
        run_prepared_artifact(detyped_path, label='detyped'),
        run_prepared_artifact(untyped_path, label='untyped'),
    )


def _timing_failure(result: RunResult) -> str | None:
    try:
        raise_for_failed_run(result, require_parseable_time=True)
    except RuntimeError as exc:
        return str(exc).splitlines()[0]
    return None


def main() -> None:
    categories: dict[str, list[str]] = {
        'works': [],
        'detype_broken': [],
        'bench_broken': [],
    }

    benchmarks = _benchmarks_with_advanced_main()
    no_advanced = _benchmarks_without_advanced_main()

    print(f'Testing {len(benchmarks)} benchmarks...')
    for name in benchmarks:
        print(f'  {name}...', end='', flush=True)
        typed_result, detyped_result, untyped_result = _run_test_triplet(name)
        typed_failure = _timing_failure(typed_result)
        detyped_failure = _timing_failure(detyped_result)
        untyped_failure = _timing_failure(untyped_result)
        if typed_failure is not None:
            categories['bench_broken'].append(name)
            print(f' broken ({typed_failure})')
        elif detyped_failure is not None:
            categories['detype_broken'].append(name)
            print(f' detyping broken ({detyped_failure})')
        elif untyped_failure is not None:
            categories['bench_broken'].append(name)
            print(f' untyped broken ({untyped_failure})')
        else:
            categories['works'].append(name)
            print(' ok')

    lines = ['# Benchmark Status\n']
    lines.append('## Detyping works\n')
    lines.append(_unordered_list(categories['works']))
    lines.append('## Detyping broken\n')
    lines.append(_unordered_list(categories['detype_broken']))
    lines.append('## Benchmark broken\n')
    lines.append(_unordered_list(categories['bench_broken']))
    lines.append('## No advanced/main.py\n')
    lines.append(_unordered_list(no_advanced))

    OUT_FILE.write_text('\n'.join(lines), encoding='utf-8')
    print(f'\nWrote {OUT_FILE}')


if __name__ == '__main__':
    main()
