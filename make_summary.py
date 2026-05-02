"""Build summary CSVs from benchmark_results/*_raw.csv files."""

from __future__ import annotations

import argparse
import csv
import re
import statistics
from collections import defaultdict
from pathlib import Path

from make_detyped_file import VARIANTS
from run_experiment import OUTPUT_ROOT, SUMMARY_FIELDS

CHUNKS_PATH = OUTPUT_ROOT / 'chunks.json'


def load_chunks(path: Path = CHUNKS_PATH) -> dict[str, dict[str, int]]:
    if not path.exists():
        return {}
    import json
    return json.loads(path.read_text(encoding='utf-8'))


def expected_chunk_paths(root: Path, benchmark: str, variant: str, chunks: int) -> list[Path]:
    if chunks == 1:
        return [root / f'{benchmark}_{variant}_raw.csv']
    return [root / f'{benchmark}_{variant}_{part}_{chunks}_raw.csv' for part in range(1, chunks + 1)]


def summary_name_for_group(group_name: str) -> str:
    return f'{group_name}_summary.csv'


def group_name_for_raw(raw_path: Path) -> str:
    name = raw_path.name
    if not name.endswith('_raw.csv'):
        raise ValueError(f'not a raw CSV: {raw_path}')

    stem = name.removesuffix('_raw.csv')
    stem = re.sub(r'_\d+_\d+$', '', stem)

    for variant in VARIANTS:
        suffix = f'_{variant}'
        if stem.endswith(suffix):
            return stem

    raise ValueError(f'cannot infer benchmark/variant from {raw_path}')


def summarize_raw(paths: list[Path]) -> list[dict[str, object]]:
    timings_by_proportion: dict[str, list[float]] = defaultdict(list)

    for path in paths:
        with path.open('r', newline='', encoding='utf-8') as handle:
            for row in csv.DictReader(handle):
                timings_by_proportion[row['proportion']].append(float(row['run_length']))

    rows: list[dict[str, object]] = []
    for proportion in sorted(timings_by_proportion, key=float):
        timings = timings_by_proportion[proportion]
        rows.append({
            'proportion': proportion,
            'average_runtime': repr(statistics.fmean(timings)),
            'min_runtime': repr(min(timings)),
            'max_runtime': repr(max(timings)),
        })
    return rows


def write_summary(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=SUMMARY_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def make_summaries(root: Path) -> None:
    chunks_config = load_chunks(root / 'chunks.json')
    groups: dict[str, list[Path]] = defaultdict(list)
    for raw_path in sorted(root.glob('*_raw.csv')):
        groups[group_name_for_raw(raw_path)].append(raw_path)

    for benchmark, variants in chunks_config.items():
        for variant, chunks in variants.items():
            group_name = f'{benchmark}_{variant}'
            expected = expected_chunk_paths(root, benchmark, variant, chunks)
            missing = [path for path in expected if not path.exists()]
            if missing:
                names = ', '.join(path.name for path in missing)
                print(f'warning: missing chunks for {group_name}: {names}', flush=True)
            groups[group_name] = [path for path in expected if path.exists()]

    for group_name, raw_paths in sorted(groups.items()):
        if not raw_paths:
            continue
        out_path = root / summary_name_for_group(group_name)
        write_summary(out_path, summarize_raw(raw_paths))
        joined = ', '.join(path.name for path in raw_paths)
        print(f'wrote {out_path} from {joined}', flush=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Build summary CSVs from raw benchmark CSVs')
    parser.add_argument('--root', type=Path, default=OUTPUT_ROOT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    make_summaries(args.root)


if __name__ == '__main__':
    main()
