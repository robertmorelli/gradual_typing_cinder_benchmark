"""detyper CLI.

    python3 detyper.py typecheck <benchmark> <a|s> <hex>   # cinder static check
    python3 detyper.py run       <benchmark> <a|s> <hex>   # run via cinder_env
    python3 detyper.py runfast   <benchmark> <a|s> <hex>   # run with --skip-typecheck
    python3 detyper.py show      <benchmark> <a|s> <hex>   # print detyped source
    python3 detyper.py refresh   <benchmark> <a|s> <hex>   # discard cached db, rebuild, then run
    python3 detyper.py getmax    <benchmark> <a|s>         # print max hex (all bits set)

The sqlite db at detyped_files/<bench>/<variant>/phase1.db is reused across
runs. Use `refresh` to invalidate it (e.g. after editing the benchmark source).
"""
from __future__ import annotations

# Load helpers from ./detyper/ as a sibling package without colliding on the name
# (since this file is also `detyper.py`). We do an explicit file load.
import importlib.util as _ilu
import argparse
import sqlite3
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent


def _load(modname: str, path: Path):
    spec = _ilu.spec_from_file_location(modname, path)
    mod = _ilu.module_from_spec(spec)
    sys.modules[modname] = mod
    spec.loader.exec_module(mod)
    return mod


_apply = _load('_dt_apply', REPO / 'detyper' / 'apply.py')
_runner = _load('_dt_runner', REPO / 'detyper' / 'artifact_runner.py')
_harness = _load('_dt_harness', REPO / 'detyper' / 'benchmark_harness.py')

detype = _apply.detype
_activated_shell_command = _runner._activated_shell_command
benchmark_output_dir = _harness.benchmark_output_dir
resolve_benchmark_path = _harness.resolve_benchmark_path

PHASE1 = REPO / 'detyper_ts' / 'phase1.ts'


def _db_path(source: Path) -> Path:
    out_dir = benchmark_output_dir(source)
    out_dir.mkdir(parents=True, exist_ok=True)
    return (out_dir / 'phase1.db').resolve()


def _build_db(source: Path, force: bool = False) -> Path:
    """Reuse the cached sqlite db unless `force` is set; (re)build via bun."""
    db = _db_path(source)
    if force and db.exists():
        db.unlink()
    if not db.exists():
        subprocess.run(
            ['bun', 'run', 'phase1.ts', str(source.resolve()), str(db)],
            check=True, cwd=str(PHASE1.parent),
        )
    return db


_VARIANT = {'a': 'advanced', 's': 'shallow', 'advanced': 'advanced', 'shallow': 'shallow'}


def _detyped_source(benchmark: str, variant: str, hex_str: str, *, refresh: bool = False) -> tuple[Path, str]:
    source = resolve_benchmark_path(benchmark, variant=variant)
    db = _build_db(source, force=refresh)
    n = sqlite3.connect(db).execute('SELECT COUNT(*) FROM annotations').fetchone()[0]
    width = n
    integer = int(hex_str, 16)
    bits = format(integer, f'0{width}b') if width else ''
    if len(bits) > width:
        raise SystemExit(f'Detype hex {hex_str} does not fit {width} annotations')
    perm = [b == '1' for b in bits]
    return source, detype(source.read_text(), str(db), perm)


def _write_detyped(benchmark: str, variant: str, hex_str: str, *, refresh: bool = False) -> Path:
    source, detyped = _detyped_source(benchmark, variant, hex_str, refresh=refresh)
    out_dir = benchmark_output_dir(source)
    out_path = out_dir / f'{source.stem}_0x{hex_str}.py'
    out_path.write_text(detyped)
    return out_path


def _cinder_run(path: Path, *, skip_typecheck: bool) -> int:
    cmd = ['python']
    if skip_typecheck:
        cmd.append('--skip-typecheck')
    cmd.append(str(path))
    proc = subprocess.run(_activated_shell_command(cmd))
    return proc.returncode


def _cinder_typecheck(path: Path) -> int:
    proc = subprocess.run(
        _activated_shell_command(['python', '-m', 'cinderx.compiler', str(path), '-o', '/tmp/typecheck.cbc'])
    )
    return proc.returncode


_COMMANDS = ('typecheck', 'run', 'runfast', 'show', 'refresh', 'getmax')


def _split_args(argv: list[str]) -> argparse.Namespace:
    # Accept both `<cmd> <bench> <variant> [<hex>]` and `<bench> <variant> <cmd> [<hex>]`.
    rest = list(argv)
    cmd = next((a for a in rest if a in _COMMANDS), None)
    if cmd is None:
        raise SystemExit(f"first or last positional must be one of {_COMMANDS}")
    rest.remove(cmd)
    if len(rest) < 2:
        raise SystemExit('need <benchmark> <variant> [<hex>]')
    benchmark, variant, *tail = rest
    hex_str = tail[0] if tail else None
    return argparse.Namespace(command=cmd, benchmark=benchmark, variant=variant, hex=hex_str)


def main() -> None:
    args = _split_args(sys.argv[1:])
    if args.variant not in _VARIANT:
        raise SystemExit(f'variant must be one of {tuple(_VARIANT.keys())}, got {args.variant!r}')
    variant = _VARIANT[args.variant]

    if args.command == 'getmax':
        source = resolve_benchmark_path(args.benchmark, variant=variant)
        db = _build_db(source)
        n = sqlite3.connect(db).execute('SELECT COUNT(*) FROM annotations').fetchone()[0]
        print(hex((1 << n) - 1)[2:] if n else '0')
        return

    if args.hex is None:
        sys.exit(f"`{args.command}` requires a hex argument")

    if args.command == 'show':
        _, detyped = _detyped_source(args.benchmark, variant, args.hex)
        sys.stdout.write(detyped)
        return

    refresh = (args.command == 'refresh')
    path = _write_detyped(args.benchmark, variant, args.hex, refresh=refresh)
    if args.command == 'typecheck':
        sys.exit(_cinder_typecheck(path))
    if args.command in ('run', 'refresh'):
        sys.exit(_cinder_run(path, skip_typecheck=False))
    if args.command == 'runfast':
        sys.exit(_cinder_run(path, skip_typecheck=True))


if __name__ == '__main__':
    main()
