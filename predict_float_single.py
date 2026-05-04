"""Test linear-model prediction on single-annotation perms for float."""
from __future__ import annotations

import tempfile
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from detyper.artifact_runner import run_timed_python_artifact_detailed
from detyper.artifacts import build_source_variant, load_source_artifacts

OUT_DIR = Path('benchmark_results/float_prediction')
RUNS_PER_PERM = 3


def main():
    src = Path('static-python-perf/Benchmark/float/advanced/main.py')
    arts = load_source_artifacts(src, output_dir=OUT_DIR)
    n = len(arts.variant_names)

    data = np.load(OUT_DIR / 'model.npz', allow_pickle=True)
    coef = data['coef']
    intercept = float(data['intercept'])
    print(f'model: intercept={intercept:.4f}s, n_coef={len(coef)}')

    actuals, preds, labels = [], [], []
    with tempfile.TemporaryDirectory(prefix='.float-single-', dir=Path.cwd()) as tmp:
        tmp = Path(tmp)
        for i in range(n):
            perm = tuple(j == i for j in range(n))
            prog = build_source_variant(arts, perm)
            artifact = tmp / f'main_{prog.perm_hex}.py'
            artifact.write_text(prog.source, encoding='utf-8')
            rel = artifact.relative_to(Path.cwd())
            timings = [run_timed_python_artifact_detailed(rel, skip_typecheck=True).timing for _ in range(RUNS_PER_PERM)]
            actual = min(timings)
            pred = intercept + coef[i]
            actuals.append(actual); preds.append(pred); labels.append(arts.variant_names[i])
            print(f'  ann={arts.variant_names[i]:>4}  actual={actual:.4f}s  predicted={pred:.4f}s  err={actual-pred:+.4f}s')

    actuals = np.array(actuals); preds = np.array(preds)
    abs_err = np.abs(actuals - preds)
    rel_err = abs_err / actuals
    print(f'\nmean |err| = {abs_err.mean()*1000:.2f}ms ({rel_err.mean()*100:.2f}%)')
    print(f'max  |err| = {abs_err.max()*1000:.2f}ms ({rel_err.max()*100:.2f}%)')

    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(n)
    ax.bar(x - 0.2, actuals, 0.4, label='actual', color='#1f77b4')
    ax.bar(x + 0.2, preds, 0.4, label='predicted (intercept + cᵢ)', color='#ff7f0e')
    ax.set_xticks(x); ax.set_xticklabels(labels, rotation=45, fontsize=8)
    ax.set_ylabel('runtime (s)')
    ax.set_title(f'float: single-annotation prediction vs actual\nmean err {abs_err.mean()*1000:.1f}ms ({rel_err.mean()*100:.1f}%)')
    ax.axhline(intercept, color='gray', linewidth=0.5, linestyle='--', label=f'baseline (all typed)={intercept:.3f}s')
    ax.legend()
    fig.tight_layout()
    out = OUT_DIR / 'float_single_annotation.png'
    fig.savefig(out, dpi=130)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
