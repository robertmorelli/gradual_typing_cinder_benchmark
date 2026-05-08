from __future__ import annotations

import csv
from pathlib import Path
from matrix_benchmark import run_matrix

BENCHMARKS = [
    'call_method', 'call_method_slots', 'call_simple', 'chaos', 'deltablue',
    'fannkuch', 'float', 'nbody', 'nqueens', 'pystone', 'richards',
]
VARIANTS = ['advanced', 'shallow']


def main() -> None:
    summary_rows = []
    for benchmark in BENCHMARKS:
        for variant in VARIANTS:
            source = Path('static-python-perf/Benchmark') / benchmark / variant / 'main.py'
            if not source.exists():
                print(f'MISSING {benchmark} {variant}: {source}')
                continue
            out_dir = Path('benchmark_results') / 'all_kind_context_matrices' / benchmark / variant
            print(f'\n=== {benchmark} {variant} ===')
            csv_path = run_matrix(source, out_dir)
            rows = list(csv.DictReader(csv_path.open(encoding='utf-8')))
            present = [r for r in rows if r['status'] != 'N/A']
            bad = [r for r in present if r['status'] != 'OK']
            summary_rows.append({
                'benchmark': benchmark,
                'variant': variant,
                'present_cells': len(present),
                'ok_cells': len(present) - len(bad),
                'bad_cells': len(bad),
                'bad_cell_list': ' | '.join(f"{r['context']} / {r['type_kind']} = {r['status']} ({r['success']}/{r['sampled']})" for r in bad),
                'matrix_csv': str(csv_path),
            })
    out = Path('benchmark_results') / 'all_kind_context_matrices' / 'summary.csv'
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['benchmark','variant','present_cells','ok_cells','bad_cells','bad_cell_list','matrix_csv'])
        writer.writeheader(); writer.writerows(summary_rows)
    print(f'\nSUMMARY {out}')
    for r in summary_rows:
        print(f"{r['benchmark']:18} {r['variant']:8} ok={r['ok_cells']}/{r['present_cells']} bad={r['bad_cells']} {r['bad_cell_list']}")


if __name__ == '__main__':
    main()
