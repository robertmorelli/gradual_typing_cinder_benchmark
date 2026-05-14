"""Detype one benchmark file.

Pipeline:
    1. `bun run detyper_ts/phase1.ts <source.py> <db.sqlite>`   (pyright -> sqlite)
    2. detyper.apply.detype(source, db, perm)                   (trivial ast edits + unparse)
"""
from __future__ import annotations

import argparse
import shutil
import sqlite3
import subprocess
from pathlib import Path

from detyper.apply import detype
from detyper.benchmark_harness import benchmark_output_dir, resolve_benchmark_path


REPO = Path(__file__).resolve().parent
PHASE1 = REPO / 'detyper_ts' / 'phase1.ts'
VARIANTS = ('advanced', 'shallow', 'untyped')


def perm_from_hex(value: str, width: int) -> list[bool]:
    try:
        integer = int(value, 16)
    except ValueError:
        raise SystemExit(f'Invalid detype hex: {value}')
    bits = format(integer, f'0{width}b') if width else ''
    if len(bits) > width:
        raise SystemExit(f'Detype hex {value} does not fit {width} detypable annotations')
    return [bit == '1' for bit in bits]


def write_detyped_file(benchmark: str, variant: str, detype_hex: str) -> Path:
    source = resolve_benchmark_path(benchmark, variant=variant)
    out_dir = benchmark_output_dir(source)
    out_dir.mkdir(parents=True, exist_ok=True)

    if variant == 'untyped':
        out_path = out_dir / f'{source.stem}_untyped.py'
        shutil.copyfile(source, out_path)
        return out_path

    db_path = (out_dir / 'phase1.db').resolve()
    source_abs = source.resolve()
    if not db_path.exists() or db_path.stat().st_mtime < source_abs.stat().st_mtime:
        subprocess.run(
            ['bun', 'run', 'phase1.ts', str(source_abs), str(db_path)],
            check=True, cwd=str(PHASE1.parent),
        )
    with sqlite3.connect(db_path) as conn:
        n_annotations = conn.execute('SELECT COUNT(*) FROM annotations').fetchone()[0]

    perm = perm_from_hex(detype_hex, n_annotations)
    detyped = detype(source.read_text(), str(db_path), perm)

    out_path = out_dir / f'{source.stem}_0x{detype_hex}.py'
    out_path.write_text(detyped)
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(description='Detype one benchmark variant.')
    parser.add_argument('benchmark')
    parser.add_argument('variant', choices=VARIANTS)
    parser.add_argument('detype_hex')
    args = parser.parse_args()
    print(write_detyped_file(args.benchmark, args.variant, args.detype_hex))


if __name__ == '__main__':
    main()
