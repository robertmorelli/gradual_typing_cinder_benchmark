"""Prepare artifacts, fuzz shallow variants, run them, and write bench_status.md."""

from __future__ import annotations

import itertools
import math
import random
from dataclasses import dataclass
from pathlib import Path

from artifact_runner import RunResult, raise_for_failed_run
from benchmark_harness import BENCHMARK_ROOT, benchmark_output_dir, resolve_benchmark_path, run_prepared_artifact
from detyper.artifacts import build_source_variant, load_source_artifacts

OUT_FILE = Path('bench_status.md')
SHALLOW_SAMPLE_SEED = 20260415
SHALLOW_MAX_SAMPLES_PER_COUNT = 2
SHALLOW_MAX_TOTAL_SAMPLES = 10


@dataclass(frozen=True)
class CheckResult:
    label: str
    status: str
    detail: str | None = None


def _benchmarks() -> list[str]:
    return sorted(
        path.name for path in BENCHMARK_ROOT.iterdir()
        if path.is_dir() and path.name != '__pycache__'
    )


def _has_variant(name: str, variant: str) -> bool:
    return (BENCHMARK_ROOT / name / variant / 'main.py').exists()


def _unordered_list(items: list[str]) -> str:
    if not items:
        return ''
    return '\n'.join(f'- {item}' for item in sorted(items)) + '\n'


def _timing_failure(result: RunResult) -> str | None:
    try:
        raise_for_failed_run(result, require_parseable_time=True)
    except RuntimeError as exc:
        lines = [line.strip() for line in str(exc).splitlines() if line.strip()]
        if not lines:
            return 'unknown failure'
        if len(lines) == 1:
            return lines[0]
        for line in lines[1:]:
            if not line.startswith('File '):
                return line
        return lines[1]
    return None


def _run_result(label: str, artifact_path: Path) -> CheckResult:
    result = run_prepared_artifact(artifact_path, label=label)
    failure = _timing_failure(result)
    if failure is None:
        return CheckResult(label=label, status='ok')
    return CheckResult(label=label, status='failed', detail=failure)


def _write_labeled_artifact(source_path: Path, variant: tuple[bool, ...], label: str) -> Path:
    artifacts = load_source_artifacts(source_path, output_dir=benchmark_output_dir(source_path))
    program = build_source_variant(artifacts, variant)
    out_dir = artifacts.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f'{artifacts.source_stem}_{program.perm_hex}_{label}.py'
    out_path.write_text(program.source, encoding='utf-8')
    return out_path


def _sample_variants(n: int, rng: random.Random) -> list[tuple[int, tuple[bool, ...]]]:
    if n <= 0:
        return [(0, tuple())]

    anchors = {
        0,
        n,
        1,
        max(0, n - 1),
        max(0, n // 4),
        max(0, n // 2),
        max(0, (3 * n) // 4),
    }
    counts = [count for count in sorted(anchors) if 0 <= count <= n]

    samples: list[tuple[int, tuple[bool, ...]]] = []
    for count in counts:
        combo_count = math.comb(n, count)
        target = min(SHALLOW_MAX_SAMPLES_PER_COUNT, combo_count)
        if target == combo_count:
            variants = [
                tuple(index in chosen for index in range(n))
                for chosen in itertools.combinations(range(n), count)
            ]
        else:
            variants = []
            seen: set[tuple[int, ...]] = set()
            while len(variants) < target:
                chosen = tuple(sorted(rng.sample(range(n), count)))
                if chosen in seen:
                    continue
                seen.add(chosen)
                variants.append(tuple(index in chosen for index in range(n)))
        samples.extend((count, variant) for variant in variants)

    deduped: list[tuple[int, tuple[bool, ...]]] = []
    seen_variants: set[tuple[bool, ...]] = set()
    for count, variant in samples:
        if variant in seen_variants:
            continue
        seen_variants.add(variant)
        deduped.append((count, variant))

    if len(deduped) <= SHALLOW_MAX_TOTAL_SAMPLES:
        return deduped

    trimmed = [deduped[0], deduped[-1]]
    middle = deduped[1:-1]
    needed = max(0, SHALLOW_MAX_TOTAL_SAMPLES - len(trimmed))
    if needed >= len(middle):
        return deduped
    step = len(middle) / needed
    for idx in range(needed):
        trimmed.append(middle[min(len(middle) - 1, int(idx * step))])
    return trimmed


def _check_advanced(name: str) -> tuple[CheckResult, CheckResult]:
    source_path = resolve_benchmark_path(name)
    artifacts = load_source_artifacts(source_path)
    n = len(artifacts.variant_names)
    typed_path = _write_labeled_artifact(source_path, tuple(False for _ in range(n)), 'typed')
    detyped_path = _write_labeled_artifact(source_path, tuple(True for _ in range(n)), 'detyped')
    return (
        _run_result('advanced typed', typed_path),
        _run_result('advanced detyped', detyped_path),
    )


def _check_shallow(name: str) -> list[CheckResult]:
    if not _has_variant(name, 'shallow'):
        return [CheckResult(label='shallow fuzz', status='missing', detail='missing shallow/main.py')]

    source_path = resolve_benchmark_path(name, variant='shallow')
    artifacts = load_source_artifacts(source_path)
    rng = random.Random(f'{SHALLOW_SAMPLE_SEED}:{name}:shallow')
    results: list[CheckResult] = []
    for sample_index, (count, variant) in enumerate(_sample_variants(len(artifacts.variant_names), rng), start=1):
        label = f'shallow k={count} sample={sample_index}'
        artifact_path = _write_labeled_artifact(source_path, variant, f'shallow_k{count:02d}_s{sample_index:02d}')
        results.append(_run_result(label, artifact_path))
    return results


def _check_untyped(name: str) -> CheckResult:
    if not _has_variant(name, 'untyped'):
        return CheckResult(label='untyped', status='missing', detail='missing untyped/main.py')
    return _run_result('untyped', resolve_benchmark_path(name, variant='untyped'))


def _aggregate(results: list[CheckResult]) -> tuple[str, str | None]:
    failed = [result for result in results if result.status == 'failed']
    if failed:
        return 'failed', f'{failed[0].label}: {failed[0].detail}'
    missing = [result for result in results if result.status == 'missing']
    if missing:
        return 'missing', missing[0].detail
    return 'ok', None


def _status_emoji(status: str) -> str:
    return {
        'ok': 'ok',
        'failed': 'failed',
        'missing': 'missing',
    }[status]


def _detail_lines(results: list[CheckResult]) -> list[str]:
    lines: list[str] = []
    for result in results:
        if result.status == 'ok':
            continue
        suffix = f' - {result.detail}' if result.detail else ''
        lines.append(f'- `{result.label}`: `{result.status}`{suffix}')
    return lines


def main() -> None:
    benchmarks = _benchmarks()
    summary_rows: list[dict[str, object]] = []
    diff: dict[str, list[str]] = {
        'advanced_only_failures': [],
        'advanced_and_shallow_failures': [],
        'advanced_and_untyped_failures': [],
        'advanced_shallow_untyped_failures': [],
        'shallow_only_failures': [],
        'untyped_only_failures': [],
        'shallow_and_untyped_failures': [],
        'missing_variants': [],
        'all_green': [],
    }

    print(f'Testing {len(benchmarks)} benchmark directories...')
    for name in benchmarks:
        if not _has_variant(name, 'advanced'):
            summary_rows.append({
                'name': name,
                'advanced_status': 'missing',
                'advanced_detail': 'missing advanced/main.py',
                'shallow_status': 'missing',
                'shallow_detail': 'missing advanced/main.py',
                'untyped_status': 'missing',
                'untyped_detail': 'missing advanced/main.py',
                'advanced_results': [],
                'shallow_results': [],
                'untyped_result': CheckResult(label='untyped', status='missing', detail='missing advanced/main.py'),
            })
            diff['missing_variants'].append(name)
            print(f'  {name}... missing advanced/main.py')
            continue

        print(f'  {name}...', end='', flush=True)
        advanced_results = list(_check_advanced(name))
        shallow_results = _check_shallow(name)
        untyped_result = _check_untyped(name)
        advanced_status, advanced_detail = _aggregate(advanced_results)
        shallow_status, shallow_detail = _aggregate(shallow_results)
        untyped_status, untyped_detail = _aggregate([untyped_result])
        summary_rows.append({
            'name': name,
            'advanced_status': advanced_status,
            'advanced_detail': advanced_detail,
            'shallow_status': shallow_status,
            'shallow_detail': shallow_detail,
            'untyped_status': untyped_status,
            'untyped_detail': untyped_detail,
            'advanced_results': advanced_results,
            'shallow_results': shallow_results,
            'untyped_result': untyped_result,
        })

        advanced_bad = advanced_status == 'failed'
        shallow_bad = shallow_status == 'failed'
        untyped_bad = untyped_status == 'failed'
        missing_any = 'missing' in {advanced_status, shallow_status, untyped_status}

        if missing_any:
            diff['missing_variants'].append(name)
        elif advanced_bad and not shallow_bad and not untyped_bad:
            diff['advanced_only_failures'].append(name)
        elif advanced_bad and shallow_bad and not untyped_bad:
            diff['advanced_and_shallow_failures'].append(name)
        elif advanced_bad and untyped_bad and not shallow_bad:
            diff['advanced_and_untyped_failures'].append(name)
        elif advanced_bad and shallow_bad and untyped_bad:
            diff['advanced_shallow_untyped_failures'].append(name)
        elif shallow_bad and not advanced_bad and not untyped_bad:
            diff['shallow_only_failures'].append(name)
        elif untyped_bad and not advanced_bad and not shallow_bad:
            diff['untyped_only_failures'].append(name)
        elif shallow_bad and untyped_bad and not advanced_bad:
            diff['shallow_and_untyped_failures'].append(name)
        elif not advanced_bad and not shallow_bad and not untyped_bad:
            diff['all_green'].append(name)

        status_bits = [
            f'advanced={advanced_status}',
            f'shallow={shallow_status}',
            f'untyped={untyped_status}',
        ]
        print(f" {' '.join(status_bits)}")

    lines = ['# Benchmark Status\n']
    lines.append('## Summary\n')
    lines.append(
        f'- Benchmarks scanned: `{len(benchmarks)}`\n'
        f'- All green: `{len(diff["all_green"])}`\n'
        f'- Advanced-only failures: `{len(diff["advanced_only_failures"])}`\n'
        f'- Advanced + shallow failures: `{len(diff["advanced_and_shallow_failures"])}`\n'
        f'- Advanced + untyped failures: `{len(diff["advanced_and_untyped_failures"])}`\n'
        f'- Advanced + shallow + untyped failures: `{len(diff["advanced_shallow_untyped_failures"])}`\n'
        f'- Shallow-only failures: `{len(diff["shallow_only_failures"])}`\n'
        f'- Untyped-only failures: `{len(diff["untyped_only_failures"])}`\n'
        f'- Shallow + untyped failures: `{len(diff["shallow_and_untyped_failures"])}`\n'
        f'- Missing variants: `{len(diff["missing_variants"])}`\n'
    )

    lines.append('## Needs Fixing Diff\n')
    lines.append('### Advanced only\n')
    lines.append(_unordered_list(diff['advanced_only_failures']))
    lines.append('### Advanced and shallow\n')
    lines.append(_unordered_list(diff['advanced_and_shallow_failures']))
    lines.append('### Advanced and untyped\n')
    lines.append(_unordered_list(diff['advanced_and_untyped_failures']))
    lines.append('### Advanced, shallow, and untyped\n')
    lines.append(_unordered_list(diff['advanced_shallow_untyped_failures']))
    lines.append('### Shallow only\n')
    lines.append(_unordered_list(diff['shallow_only_failures']))
    lines.append('### Untyped only\n')
    lines.append(_unordered_list(diff['untyped_only_failures']))
    lines.append('### Shallow and untyped\n')
    lines.append(_unordered_list(diff['shallow_and_untyped_failures']))
    lines.append('### Missing variants\n')
    lines.append(_unordered_list(diff['missing_variants']))
    lines.append('### All green\n')
    lines.append(_unordered_list(diff['all_green']))

    lines.append('## Per Benchmark\n')
    lines.append('| benchmark | advanced | shallow fuzz | untyped |')
    lines.append('| --- | --- | --- | --- |')
    for row in summary_rows:
        lines.append(
            f'| {row["name"]} | {_status_emoji(row["advanced_status"])} | '
            f'{_status_emoji(row["shallow_status"])} | {_status_emoji(row["untyped_status"])} |'
        )

    lines.append('\n## Failure Details\n')
    for row in summary_rows:
        detail_lines = (
            _detail_lines(list(row['advanced_results']))
            + _detail_lines(list(row['shallow_results']))
            + _detail_lines([row['untyped_result']])
        )
        if not detail_lines:
            continue
        lines.append(f'### {row["name"]}\n')
        lines.extend(detail_lines)
        lines.append('')

    OUT_FILE.write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')
    print(f'\nWrote {OUT_FILE}')


if __name__ == '__main__':
    main()
