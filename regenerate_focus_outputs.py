from __future__ import annotations

from pathlib import Path

from detyper.ast_data import build_ast_data
from detyper.bundle_builder import build_detyper_map_from_ast_data
from detyper.pipeline import build_detyped_program_from_ast_data


def regenerate_max_detyped(benchmark: str = 'deltablue', variant: str = 'advanced') -> Path:
    src_path = Path('static-python-perf/Benchmark') / benchmark / variant / 'main.py'
    out_path = Path('benchmark_results') / f'{benchmark}_max_detyped.py'
    src = src_path.read_text()
    ast_data = build_ast_data(src)
    detyper_map = build_detyper_map_from_ast_data(ast_data)
    program = build_detyped_program_from_ast_data(ast_data, detyper_map, tuple(True for _ in detyper_map['annotation_ids']))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(program.source)
    return out_path


if __name__ == '__main__':
    path = regenerate_max_detyped()
    print(path)
