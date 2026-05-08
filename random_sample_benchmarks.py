from __future__ import annotations

import argparse, csv, random, subprocess
from pathlib import Path
from detyper.ast_data import build_ast_data
from detyper.bundle_builder import build_detyper_map_from_ast_data
from detyper.pipeline import build_detyped_program_from_ast_data

BENCHMARKS = ['call_method','call_method_slots','call_simple','chaos','deltablue','fannkuch','float','nbody','nqueens','pystone','richards']
VARIANTS = ['advanced','shallow']
PY = Path('cinder_env/bin/python')
OUT = Path('benchmark_results/random_samples')

def typecheck(path: Path) -> tuple[bool,str]:
    p=subprocess.run([str(PY),'--typecheck-only',str(path)],capture_output=True,text=True,timeout=45)
    return p.returncode==0,(p.stdout+p.stderr).strip().replace('\n',' | ')[-500:]

def sample_perms(n:int, samples:int, rng:random.Random):
    if n==0: return [tuple()]
    perms=[]
    perms.append(tuple(False for _ in range(n)))
    perms.append(tuple(True for _ in range(n)))
    for _ in range(samples):
        perms.append(tuple(rng.choice([False,True]) for _ in range(n)))
    # unique, preserve order
    out=[]; seen=set()
    for p in perms:
        if p not in seen: seen.add(p); out.append(p)
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--samples',type=int,default=10); ap.add_argument('--seed',type=int,default=1729)
    args=ap.parse_args(); rng=random.Random(args.seed); OUT.mkdir(parents=True,exist_ok=True)
    rows=[]
    for bench in BENCHMARKS:
      for variant in VARIANTS:
        src_path=Path('static-python-perf/Benchmark')/bench/variant/'main.py'
        if not src_path.exists():
            rows.append({'benchmark':bench,'variant':variant,'sample':'missing','detyped':0,'total':0,'ok':False,'msg':'missing source'})
            print('MISSING',bench,variant); continue
        try:
            src=src_path.read_text(); ad=build_ast_data(src); m=build_detyper_map_from_ast_data(ad); ids=[str(x) for x in m['annotation_ids']]
        except Exception as e:
            rows.append({'benchmark':bench,'variant':variant,'sample':'build','detyped':0,'total':0,'ok':False,'msg':repr(e)})
            print('BUILDFAIL',bench,variant,e); continue
        for i,perm in enumerate(sample_perms(len(ids),args.samples,rng)):
            try:
                prog=build_detyped_program_from_ast_data(ad,m,perm)
                outdir=OUT/bench/variant; outdir.mkdir(parents=True,exist_ok=True)
                out=outdir/f'sample_{i:02d}_{sum(perm)}of{len(ids)}.py'; out.write_text(prog.source)
                ok,msg=typecheck(out)
            except Exception as e:
                ok=False; msg=repr(e)
            rows.append({'benchmark':bench,'variant':variant,'sample':i,'detyped':sum(perm),'total':len(ids),'ok':ok,'msg':msg})
            print(('OK' if ok else 'FAIL'), bench, variant, f'sample={i}', f'{sum(perm)}/{len(ids)}', msg[:180] if not ok else '')
    csv_path=OUT/'summary.csv'
    with csv_path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['benchmark','variant','sample','detyped','total','ok','msg']); w.writeheader(); w.writerows(rows)
    print(csv_path)
    # compact aggregate
    print('\nAGGREGATE')
    for bench in BENCHMARKS:
      for variant in VARIANTS:
        rs=[r for r in rows if r['benchmark']==bench and r['variant']==variant]
        if not rs: continue
        ok=sum(1 for r in rs if r['ok']); print(f'{bench:18} {variant:8} {ok}/{len(rs)} ok')

if __name__=='__main__': main()
