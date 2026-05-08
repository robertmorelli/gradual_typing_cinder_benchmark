from __future__ import annotations

import argparse, csv, itertools, subprocess
from collections import defaultdict
from pathlib import Path
from detyper.ast_data import build_ast_data
from detyper.bundle_builder import build_detyper_map_from_ast_data
from detyper.pipeline import build_detyped_program_from_ast_data

PY=Path('cinder_env/bin/python')

def tc(path: Path):
    p=subprocess.run([str(PY),'--typecheck-only',str(path)],capture_output=True,text=True,timeout=45)
    return p.returncode==0,(p.stdout+p.stderr).strip().replace('\n',' | ')[-500:]

def run(bench: str, variant: str):
    srcp=Path('static-python-perf/Benchmark')/bench/variant/'main.py'
    outdir=Path('benchmark_results')/'pairwise'/bench/variant; outdir.mkdir(parents=True,exist_ok=True)
    src=srcp.read_text(); ad=build_ast_data(src); m=build_detyper_map_from_ast_data(ad); ids=[str(x) for x in m['annotation_ids']]
    by=defaultdict(list)
    for aid in ids:
        r=ad.indexes['annotations'][aid]; by[(r['context'],r['type_kind'])].append(aid)
    rows=[]; bad=[]; groups=sorted(by)
    print(f'== {bench} {variant}: annotations={len(ids)} groups={len(groups)} ==')
    for g1,g2 in itertools.combinations_with_replacement(groups,2):
        selected=set(by[g1])|set(by[g2])
        prog=build_detyped_program_from_ast_data(ad,m,tuple(a in selected for a in ids))
        name='__'.join(['_'.join(g1),'_'.join(g2)]).replace('/','_')[:180]+'.py'
        path=outdir/name; path.write_text(prog.source)
        ok,msg=tc(path)
        rows.append({'g1':str(g1),'g2':str(g2),'n':len(selected),'ok':ok,'msg':msg})
        if not ok:
            bad.append((g1,g2,msg)); print('BAD',g1,g2,msg[:220])
    with (outdir/'pairwise_groups.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['g1','g2','n','ok','msg']); w.writeheader(); w.writerows(rows)
    # Drill each bad group up to first 20 bad annotation pairs.
    drill=[]
    for g1,g2,_ in bad:
        count=0
        for a,b in itertools.product(by[g1],by[g2]):
            selected={a,b}
            prog=build_detyped_program_from_ast_data(ad,m,tuple(x in selected for x in ids))
            path=outdir/f'pair_{a}_{b}.py'; path.write_text(prog.source)
            ok,msg=tc(path)
            if not ok:
                drill.append({'g1':str(g1),'g2':str(g2),'a':a,'b':b,'ok':ok,'msg':msg})
                print(' BADPAIR',a,b,msg[:220])
                count+=1
                if count>=20: break
    with (outdir/'bad_annotation_pairs.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['g1','g2','a','b','ok','msg']); w.writeheader(); w.writerows(drill)
    print(f'bad_groups={len(bad)} bad_pairs_logged={len(drill)} out={outdir}')

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('benchmark'); ap.add_argument('variant'); args=ap.parse_args(); run(args.benchmark,args.variant)
