"""Run a small CSV-only benchmark compatibility check."""

from __future__ import annotations

import argparse
import csv
import random
from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory

from detyper.artifact_runner import run_timed_python_artifact_detailed
from detyper.artifacts import build_source_variant, load_source_artifacts
from detyper.benchmark_harness import BENCHMARK_ROOT, resolve_benchmark_path

STATUS_FIELDS = [
    'benchmark',
    'category',
    'advanced_status',
    'advanced_error',
    'shallow_status',
    'shallow_error',
    'untyped_status',
    'untyped_error',
]
VARIANTS = ('advanced', 'shallow', 'untyped')
RNG_SEED = 20260429


@dataclass(frozen=True)
class VariantStatus:
    status: str
    error: str = ''


def benchmark_names() -> list[str]:
    return sorted(
        path.name
        for path in BENCHMARK_ROOT.iterdir()
        if path.is_dir() and path.name != '__pycache__'
    )


def has_variant(benchmark: str, variant: str) -> bool:
    return (BENCHMARK_ROOT / benchmark / variant / 'main.py').exists()


def sample_variants(total: int, rng: random.Random) -> list[tuple[bool, ...]]:
    if total == 0:
        return [tuple()]

    samples = {
        tuple(False for _ in range(total)),
        tuple(True for _ in range(total)),
    }
    if total > 1:
        middle = max(1, min(total - 1, total // 2))
        chosen = set(rng.sample(range(total), middle))
        samples.add(tuple(index in chosen for index in range(total)))
    return sorted(samples)


def write_artifact(source_path: Path, variant: tuple[bool, ...], output_dir: Path) -> Path:
    artifacts = load_source_artifacts(source_path, output_dir=output_dir)
    program = build_source_variant(artifacts, variant)
    artifact_path = output_dir / f'{artifacts.source_stem}_{program.perm_hex}.py'
    artifact_path.parent.mkdir(parents=True, exist_ok=True)
    artifact_path.write_text(program.source, encoding='utf-8')
    return artifact_path


def run_artifact(path: Path) -> None:
    run_timed_python_artifact_detailed(path)


def check_generated_variant(benchmark: str, variant_name: str, tmp_root: Path, rng: random.Random) -> VariantStatus:
    if not has_variant(benchmark, variant_name):
        return VariantStatus('missing', f'missing {variant_name}/main.py')

    source_path = resolve_benchmark_path(benchmark, variant=variant_name)
    artifacts = load_source_artifacts(source_path)
    output_dir = tmp_root / benchmark / variant_name

    try:
        for sample in sample_variants(len(artifacts.variant_names), rng):
            run_artifact(write_artifact(source_path, sample, output_dir))
    except Exception as exc:
        return VariantStatus('failed', str(exc).strip())

    return VariantStatus('ok')


def check_untyped(benchmark: str) -> VariantStatus:
    if not has_variant(benchmark, 'untyped'):
        return VariantStatus('missing', 'missing untyped/main.py')

    try:
        run_artifact(resolve_benchmark_path(benchmark, variant='untyped'))
    except Exception as exc:
        return VariantStatus('failed', str(exc).strip())

    return VariantStatus('ok')


def category_for(advanced: VariantStatus, shallow: VariantStatus, untyped: VariantStatus) -> str:
    statuses = {
        'advanced': advanced.status,
        'shallow': shallow.status,
        'untyped': untyped.status,
    }
    if all(status == 'ok' for status in statuses.values()):
        return 'all_green'
    if any(status == 'missing' for status in statuses.values()):
        return 'missing_variants'

    failed = [name for name, status in statuses.items() if status == 'failed']
    return '_and_'.join(failed) + '_failures'


def check_benchmark(benchmark: str, tmp_root: Path, rng: random.Random) -> dict[str, str]:
    advanced = check_generated_variant(benchmark, 'advanced', tmp_root, rng)
    shallow = check_generated_variant(benchmark, 'shallow', tmp_root, rng)
    untyped = check_untyped(benchmark)
    return {
        'benchmark': benchmark,
        'category': category_for(advanced, shallow, untyped),
        'advanced_status': advanced.status,
        'advanced_error': advanced.error,
        'shallow_status': shallow.status,
        'shallow_error': shallow.error,
        'untyped_status': untyped.status,
        'untyped_error': untyped.error,
    }


def write_status(rows: list[dict[str, str]], output_path: Path) -> None:
    with output_path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=STATUS_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Write bench_status.csv')
    parser.add_argument('benchmarks', nargs='*', help='Benchmarks to check. Defaults to every benchmark directory.')
    parser.add_argument('--output', type=Path, default=Path('bench_status.csv'))
    parser.add_argument('--seed', type=int, default=RNG_SEED)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    names = args.benchmarks or benchmark_names()
    rng = random.Random(args.seed)
    rows: list[dict[str, str]] = []

    with TemporaryDirectory(prefix='.bench-status-', dir=Path.cwd()) as tmp:
        tmp_root = Path(tmp).relative_to(Path.cwd())
        for index, name in enumerate(names, start=1):
            print(f'{index}/{len(names)} {name}', flush=True)
            rows.append(check_benchmark(name, tmp_root, rng))
            write_status(rows, args.output)

    print(f'Wrote {args.output}', flush=True)


if __name__ == '__main__':
    main()
