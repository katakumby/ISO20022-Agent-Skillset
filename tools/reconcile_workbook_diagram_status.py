"""Reconcile workbook coverage navigation with maintained diagram page metadata."""
from pathlib import Path
import json,re,sys,collections
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'))
from extract_workbooks import write,relative
rp=ROOT/'work/workbook-results.json';rs=json.loads(rp.read_text('utf-8'));counts=collections.Counter()
for r in rs:
 if r.get('format')!='xlsx':continue
 for d in r['diagrams']:
  b=(ROOT/d['page']).read_text('utf-8');m=re.search(r'^review_status: ["\']?([^"\'\n]+)',b,re.M)
  if m:d['review_status']=m[1].strip()
  counts[d.get('review_status','unknown')]+=1
 sid=r['source_id'];wp=ROOT/'work/workbooks'/sid/'workbook.json';w=json.loads(wp.read_text('utf-8'));by={d['figure_id']:d for d in r['diagrams']}
 for sh in w['sheets']:
  for d in sh.get('drawings',[]):
   if d.get('figure_id') in by:d['review_status']=by[d['figure_id']]['review_status']
 write(ROOT,wp,json.dumps(w,ensure_ascii=False,indent=2),'job-000001')
 idx=ROOT/r['output'];cov=idx.parent/'coverage.md';b=cov.read_text('utf-8');n=len(r['diagrams']);reviewed=sum(d.get('review_status')=='reviewed' for d in r['diagrams'])
 summary='All '+str(n)+' picture occurrences have retained assets and dedicated pages. '+str(reviewed)+' occurrence pages are reviewed; '+str(n-reviewed)+' retain their explicitly recorded source/interpretation limitations. Substantive figures have been reconstructed or linked to an exact-image reviewed canonical figure. Workbook table values and complete OOXML metadata are preserved; independent value/range validation is recorded separately. The workbook remains needs-review for worksheet presentation and any listed unresolved diagram interpretations.'
 b=re.sub(r'All \d+ picture occurrences[^\n]*',summary,b)
 b=re.sub(r'Next action:[^\n]*','Next action: resolve any diagram-specific issues below, then complete visual worksheet presentation checks for number-format, merged-header and color semantics against the unchanged originals. Source values, formula/cached-value distinctions and drawing anchors remain available in workbook metadata.',b)
 heading='## Current diagram dispositions'
 if heading in b:b=b.split(heading)[0].rstrip()+'\n'
 b+='\n'+heading+'\n\n| Figure | Source worksheet | Disposition | Review |\n| --- | --- | --- | --- |\n'
 for d in r['diagrams']:b+='| ['+d['figure_id']+']('+relative(cov,ROOT/d['page'])+') | '+d['sheet']+' | '+d.get('disposition','converted')+' | '+d.get('review_status','needs-review')+' |\n'
 write(ROOT,cov,b,'job-000001')
 note='## Current diagram coverage'
 b=idx.read_text('utf-8')
 if note in b:b=b.split(note)[0].rstrip()+'\n'
 b+='\n'+note+'\n\n'+str(reviewed)+' of '+str(n)+' source figure occurrences are reviewed. See [current dispositions](coverage.md#current-diagram-dispositions); diagram scope is distinct from whole-workbook review.\n'
 write(ROOT,idx,b,'job-000001')
write(ROOT,rp,json.dumps(rs,ensure_ascii=False,indent=2),'job-000001');print(json.dumps(dict(counts)))
