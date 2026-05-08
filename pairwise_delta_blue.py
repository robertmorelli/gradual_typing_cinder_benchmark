from __future__ import annotations

import itertools, subprocess, csv
from collections import defaultdict
from pathlib import Path
from detyper.ast_data import build_ast_data
from detyper.bundle_builder import build_detyper_map_from_ast_data
from detyper.pipeline import build_detyped_program_from_ast_data

SRC=Path('static-python-perf/Benchmark/deltablue/advanced/main.py')
OUT=Path('benchmark_results/deltablue_pairwise')
PY=Path('cinder_env/bin/python')

def tc(path):
 p=subprocess.run([str(PY),'--typecheck-only',str(path)],capture_output=True,text=True,timeout=30)
 return p.returncode==0,(p.stdout+p.stderr).strip().replace('\n',' | ')[-500:]

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 src=SRC.read_text(); ad=build_ast_data(src); m=build_detyper_map_from_ast_data(ad)
 ids=[str(x) for x in m['annotation_ids']]
 by=defaultdict(list)
 for aid in ids:
  r=ad.indexes['annotations'][aid]; by[(r['context'],r['type_kind'])].append(aid)
 print('annotations',len(ids),'groups',len(by))
 rows=[]; bad=[]
 groups=sorted(by)
 for g1,g2 in itertools.combinations_with_replacement(groups,2):
  selected=set(by[g1])|set(by[g2])
  prog=build_detyped_program_from_ast_data(ad,m,tuple(a in selected for a in ids))
  name='__'.join(['_'.join(g1),'_'.join(g2)]).replace('/','_')[:180]+'.py'
  path=OUT/name; path.write_text(prog.source)
  ok,msg=tc(path)
  row={'g1':str(g1),'g2':str(g2),'n':len(selected),'ok':ok,'msg':msg}
  rows.append(row)
  if not ok:
   bad.append((g1,g2,msg))
   print('BAD',g1,g2,msg[:250])
 with (OUT/'pairwise_groups.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['g1','g2','n','ok','msg']); w.writeheader(); w.writerows(rows)
 print('bad groups',len(bad),'csv',OUT/'pairwise_groups.csv')
 # For first bad group, drill annotation pairs.
 if bad:
  g1,g2,_=bad[0]
  print('drill first bad',g1,g2)
  pair_rows=[]
  for a,b in itertools.product(by[g1], by[g2]):
   selected={a,b}
   prog=build_detyped_program_from_ast_data(ad,m,tuple(x in selected for x in ids))
   path=OUT/f'pair_{a}_{b}.py'; path.write_text(prog.source)
   ok,msg=tc(path)
   pair_rows.append({'a':a,'b':b,'ok':ok,'msg':msg})
   if not ok: print('BADPAIR',a,b,msg[:300])
  with (OUT/'first_bad_annotation_pairs.csv').open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=['a','b','ok','msg']); w.writeheader(); w.writerows(pair_rows)

if __name__=='__main__': main()
