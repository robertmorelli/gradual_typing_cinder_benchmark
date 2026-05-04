"""Random-sample Ridge fit on multiple benchmarks, with 5-fold CV."""
from __future__ import annotations

import argparse
import json
import random
import sys
import tempfile
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import KFold

from detyper.artifact_runner import run_timed_python_artifact_detailed
from detyper.artifacts import build_source_variant, load_source_artifacts

N_SAMPLES = 100
RUNS_PER_PERM = 3
SEED = 42
OUT_ROOT = Path('benchmark_results') / 'multi_prediction'


def collect(arts, perms, tmpdir, label):
    rows = []
    for i, perm in enumerate(perms, start=1):
        prog = build_source_variant(arts, perm)
        artifact = tmpdir / f'main_{prog.perm_hex}.py'
        artifact.write_text(prog.source, encoding='utf-8')
        rel = artifact.relative_to(Path.cwd())
        try:
            timings = [run_timed_python_artifact_detailed(rel, skip_typecheck=True).timing for _ in range(RUNS_PER_PERM)]
            t = min(timings)
        except Exception as exc:
            print(f'  [{label}] [{i}/{len(perms)}] {prog.perm_hex} FAILED: {exc!s:.140}', flush=True)
            continue
        rows.append({'perm': list(perm), 'perm_hex': prog.perm_hex, 'runtime': t, 'all_runs': timings})
        if i % 10 == 0 or i == len(perms):
            print(f'  [{label}] [{i}/{len(perms)}] {prog.perm_hex} t={t:.4f}s', flush=True)
    return rows


def make_perms(n, count, seed):
    rng = random.Random(seed)
    seen = set()
    perms = []
    for boundary in (tuple([False]*n), tuple([True]*n)):
        if boundary not in seen:
            seen.add(boundary); perms.append(boundary)
    while len(perms) < count:
        cand = tuple(rng.random() < 0.5 for _ in range(n))
        if cand in seen: continue
        seen.add(cand); perms.append(cand)
    return perms


def evaluate(rows, n):
    X = np.array([r['perm'] for r in rows], dtype=float)
    y = np.array([r['runtime'] for r in rows])
    model = Ridge(alpha=1.0).fit(X, y)
    train_r2 = model.score(X, y)
    train_pred = model.predict(X)
    train_err = np.abs(y - train_pred)

    cv_pred = np.zeros_like(y)
    kf = KFold(n_splits=5, shuffle=True, random_state=SEED)
    for tr, te in kf.split(X):
        m = Ridge(alpha=1.0).fit(X[tr], y[tr])
        cv_pred[te] = m.predict(X[te])
    cv_err = np.abs(y - cv_pred)
    ss_res = np.sum((y - cv_pred)**2); ss_tot = np.sum((y - y.mean())**2)
    cv_r2 = 1 - ss_res/ss_tot

    return {
        'n_annotations': n,
        'n_samples': len(rows),
        'baseline': float(y.min()),
        'runtime_range': (float(y.min()), float(y.max())),
        'train_r2': float(train_r2),
        'train_mean_err_ms': float(train_err.mean()*1000),
        'train_mean_err_pct': float((train_err/y).mean()*100),
        'cv_r2': float(cv_r2),
        'cv_mean_err_ms': float(cv_err.mean()*1000),
        'cv_mean_err_pct': float((cv_err/y).mean()*100),
        'cv_max_err_ms': float(cv_err.max()*1000),
        'cv_max_err_pct': float((cv_err/y).max()*100),
        'model_coef': model.coef_.tolist(),
        'model_intercept': float(model.intercept_),
    }, X, y, model, cv_pred


def plot(bench, result, X, y, model, cv_pred, out_dir):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    coefs = model.coef_
    order = np.argsort(coefs)
    axes[0].barh(range(len(coefs)), coefs[order],
                 color=['#d62728' if c>0 else '#2ca02c' for c in coefs[order]])
    axes[0].set_yticks([])
    axes[0].set_xlabel('Δ runtime per annotation (s)')
    axes[0].set_title(f'{bench}: per-annotation Ridge coefficients (n={len(coefs)})')
    axes[0].axvline(0, color='black', linewidth=0.5)

    axes[1].scatter(y, model.predict(X), alpha=0.5, label='train', color='#1f77b4')
    axes[1].scatter(y, cv_pred, alpha=0.5, label='5-fold CV', color='#ff7f0e', marker='x')
    lims = [min(y.min(), cv_pred.min()), max(y.max(), cv_pred.max())]
    axes[1].plot(lims, lims, 'k--', linewidth=1)
    axes[1].set_xlabel('actual runtime (s)')
    axes[1].set_ylabel('predicted runtime (s)')
    axes[1].set_title(f"train R²={result['train_r2']:.3f} | CV R²={result['cv_r2']:.3f}\nCV mean err {result['cv_mean_err_ms']:.1f}ms ({result['cv_mean_err_pct']:.1f}%)")
    axes[1].set_aspect('equal')
    axes[1].legend()
    fig.tight_layout()
    fig.savefig(out_dir / f'{bench}_prediction.png', dpi=130)
    plt.close(fig)


def run_one(bench):
    src = Path(f'static-python-perf/Benchmark/{bench}/advanced/main.py')
    out_dir = OUT_ROOT / bench
    out_dir.mkdir(parents=True, exist_ok=True)
    arts = load_source_artifacts(src, output_dir=out_dir)
    n = len(arts.variant_names)
    print(f'\n=== {bench}: {n} annotations ===', flush=True)
    perms = make_perms(n, N_SAMPLES, SEED)
    with tempfile.TemporaryDirectory(prefix=f'.{bench}-pred-', dir=Path.cwd()) as tmp:
        rows = collect(arts, perms, Path(tmp), bench)
    if len(rows) < 10:
        print(f'  [{bench}] only {len(rows)} succeeded — skipping')
        return None
    (out_dir / 'samples.json').write_text(json.dumps(rows, indent=2))
    result, X, y, model, cv_pred = evaluate(rows, n)
    (out_dir / 'result.json').write_text(json.dumps({k:v for k,v in result.items() if k != 'model_coef'}, indent=2))
    plot(bench, result, X, y, model, cv_pred, out_dir)
    print(f'  [{bench}] train R²={result["train_r2"]:.3f}  CV R²={result["cv_r2"]:.3f}  CV mean err {result["cv_mean_err_pct"]:.2f}%')
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('benchmarks', nargs='*', default=['take5', 'chaos', 'spectralnorm', 'fannkuch', 'call_simple'])
    args = ap.parse_args()
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    summary = {}
    for bench in args.benchmarks:
        try:
            r = run_one(bench)
            if r is not None:
                summary[bench] = {k: v for k, v in r.items() if k != 'model_coef'}
        except Exception as exc:
            print(f'[{bench}] ERROR: {exc}', flush=True)

    (OUT_ROOT / 'summary.json').write_text(json.dumps(summary, indent=2))
    print('\n=== SUMMARY ===')
    print(f'{"benchmark":>14}  {"n_ann":>5}  {"baseline":>10}  {"train R²":>9}  {"CV R²":>7}  {"CV mean":>10}  {"CV max":>10}')
    for b, r in summary.items():
        print(f'{b:>14}  {r["n_annotations"]:>5}  {r["baseline"]:>9.4f}s  {r["train_r2"]:>9.3f}  {r["cv_r2"]:>7.3f}  {r["cv_mean_err_pct"]:>9.2f}%  {r["cv_max_err_pct"]:>9.2f}%')


if __name__ == '__main__':
    sys.exit(main())
