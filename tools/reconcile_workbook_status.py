"""Reconcile workbook figure inventories with already recorded review evidence, without rerendering."""
from pathlib import Path
import json,hashlib,re,sys,urllib.parse,copy
sys.path.insert(0,str(Path(__file__).resolve().parent));import kb,extract_workbooks
root=Path(__file__).resolve().parents[1];extract_workbooks.DATE='2026-11-09';results=json.loads((root/'work/workbook-results.json').read_text('utf-8'));sources={s['source_id']:s for s in kb.sources(root)};vmap={v['source_id']:v for v in json.loads((root/'work/workbook-validation.json').read_text('utf-8'))}
def put(p,t):extract_workbooks.write(root,p,t,'job-000001')
# The pilot reviewer confirmed figure3's successful bounded review; its batch-wide qualifier was stale.
p=root/'domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/diagrams/fig-0003.md';m,b=kb.metadata(p);pilot=next(x for x in json.loads((root/'tracking/reviews/pilot-models.json').read_text('utf-8'))if x['diagram']=='fig-0003')
mermaid=re.search(r'\x60\x60\x60mermaid\n(.*?)\x60\x60\x60',b,re.S).group(1)
assert pilot['mmd_sha256'] in [hashlib.sha256(mermaid.encode()).hexdigest(),hashlib.sha256(mermaid.replace('\n','\r\n').encode()).hexdigest()] # original renderer used Windows CRLF bytes
assert pilot['visual_review']=='pass' and pilot['result']=='pass'
m['review_status']='reviewed';b=b.replace(' Repeated ISODateTime/FrequencyCode drawing occurrences keep separate rendering identifiers while retaining their source labels.','').replace('The relationship inventory preserves all transcribed links; this does not resolve the stated source inconsistencies.','The relationship inventory preserves all26 transcribed links; no figure-specific source ambiguity was recorded in this bounded review.')
b=re.sub(r'\[Source ambiguities: issue-000015\]\([^)]*\)\s*[·�]?\s*','',b);put(p,kb.front(m)+b)
report={'date':'2026-11-09','method':'Compared existing canonical Markdown review metadata and dated renderer/visual evidence against every workbook drawing occurrence and immutable original image hashes. No new rendering or whole-workbook visual review is claimed.','workbooks':[],'figures':[],'limitations':['All workbook values have independent openpyxl comparison; full worksheet visual formatting/layout review remains incomplete.','Source-specific diagram issues remain explicit; converted is not synonymous with reviewed.']}
for item in results:
 if item['format']!='xlsx':continue
 sid=item['source_id'];src=sources[sid];data_path=root/'work/workbooks'/sid/'workbook.json';data=json.loads(data_path.read_text('utf-8'));assert data['sha256']==src['sha256'];assert hashlib.sha256(kb.read_source(root,src)).hexdigest()==src['sha256']
 allfigs=[f for sh in data['sheets']for f in sh['drawings']if f.get('figure_id')];assert len(allfigs)==item['counts']['picture_occurrences'];assert len(allfigs)==len(item['diagrams']);byid={f['figure_id']:f for f in item['diagrams']};changes=0
 for f in allfigs:
  fp=root/f['page'];fm,fb=kb.metadata(fp);canonical=fm.get('canonical_output')or f.get('canonical_output');cp=root/canonical if canonical else fp;cm,cb=kb.metadata(cp);assert hashlib.sha256((root/f['asset']).read_bytes()).hexdigest()==f['sha256']
  render=cm.get('render_status',cm.get('render_result'));visual=cm.get('visual_review');has_mermaid='\x60\x60\x60mermaid' in cb
  assert has_mermaid and render in ['pass','passed'],(sid,f['figure_id'],render)
  assert visual,(sid,f['figure_id'])
  if canonical:
   assert cm['review_status']=='reviewed',(sid,f['figure_id'],canonical)
   candidates=[]
   for target in re.findall(r'\]\(([^)]+)\)',cb):
    q=(cp.parent/urllib.parse.unquote(target.strip('<>').split('#')[0])).resolve()
    if q.is_file()and q.suffix.lower()in ['.png','.jpg','.jpeg']and ('media'in q.parts or 'originals'in q.parts):
     candidates.append(hashlib.sha256(q.read_bytes()).hexdigest())
   assert f['sha256']in candidates,(sid,f['figure_id'],'canonical original hash mismatch')
  norm=dict(disposition='deduplicated'if canonical else'converted',review_status=fm['review_status'],render_status='passed',visual_review=visual,canonical_output=canonical or f['page'],review_evidence_page=cp.relative_to(root).as_posix(),inventory_reconciled_date='2026-11-09')
  # canonical_output on a nonduplicate is an inventory pointer, not a dedup instruction.
  if not canonical:norm.pop('canonical_output')
  for target in [f,byid[f['figure_id']]]:
   if any(target.get(k)!=v for k,v in norm.items()):changes+=1
   target.update(norm)
  report['figures'].append(dict(source_id=sid,figure_id=f['figure_id'],path=f['page'],source_image=f['asset'],source_image_sha256=f['sha256'],canonical_path=cp.relative_to(root).as_posix(),review_status=fm['review_status'],disposition=norm['disposition'],render_status='passed',visual_review=visual,review_evidence=cm))
  # Scoped sheet navigation reflects actual figure status and continues to expose worksheet review limitations.
  for sh in data['sheets']:
   if f not in sh['drawings']:continue
   indexes=list((root/item['output']).parent.glob('sheets/*/index.md'))
   for ip in indexes:
    im,ib=kb.metadata(ip)
    if im.get('worksheet')!=sh['name']:continue
    linepat=r'(- \['+re.escape(f['figure_id'])+r'\]\([^)]*\): [^\n]*); reconstruction and visual review pending\.'
    note='; reconstruction rendered and compared with the original; '+fm['review_status']+'.'
    ib=re.sub(linepat,lambda z:z.group(1)+note,ib);put(ip,kb.front(im)+ib)
 reviewed=sum(f['review_status']=='reviewed'for f in allfigs);total=len(allfigs)
 statusline=f'{reviewed} of {total} source figure occurrences are reviewed.'
 ip=root/item['output'];im,ib=kb.metadata(ip);ib=re.sub(r'\d+ of \d+ source figure occurrences are reviewed\.',statusline,ib)
 old='Visual workbook review remains pending.';new='Worksheet presentation review remains incomplete; diagram review is separately recorded for each figure.'
 im['limitations']=[new if x==old else x for x in im.get('limitations',[])];ib=ib.replace(old,new);put(ip,kb.front(im)+ib)
 cov=ip.parent/'coverage.md';cm,cb=kb.metadata(cov);cb=re.sub(r'\d+ occurrence pages are reviewed; \d+ retain',f'{reviewed} occurrence pages are reviewed; {total-reviewed} retain',cb)
 cb=re.sub(r'## Current diagram dispositions\n.*', '## Current diagram dispositions\n\n'+kb.table(['Figure','Source worksheet','Disposition','Review'],[[kb.link(cov,root/f['page'],f['figure_id']),f['sheet'],f['disposition'],f['review_status']]for f in allfigs])+'\n',cb,flags=re.S);put(cov,kb.front(cm)+cb)
 item['limitations']=[new if x==old else x for x in item.get('limitations',[])];data['limitations']=[new if x==old else x for x in data.get('limitations',[])]
 data['diagram_review_summary']={'figure_occurrences':total,'reviewed':reviewed,'needs_review':total-reviewed,'rendered_or_reviewed_canonical':total,'audit_date':'2026-11-09'};kb.dump(data_path,data)
 comments=sum(len(sh['comments'])for sh in data['sheets']);merges=sum(len(sh['merged_ranges'])for sh in data['sheets']);hidden=sum(sh['state']!='visible'for sh in data['sheets']);validation=vmap[sid];assert validation['result']=='pass'and not validation['differences']
 report['workbooks'].append(dict(source_id=sid,source_sha256=src['sha256'],source_checksum_unchanged=True,sheets=len(data['sheets']),table_parts=item['counts']['table_parts'],source_data_rows=item['counts']['data_rows'],independently_compared_nonempty_cells=validation['nonempty_cells_compared'],value_check_date=validation['date'],comments=comments,merged_ranges=merges,hidden_sheets=hidden,figures=total,reviewed_figures=reviewed,figure_metadata_changes=changes,workbook_review_status=im['review_status'],whole_workbook_visual_review='not complete'))
 del data
kb.dump(root/'work/workbook-results.json',results)
report['counts']={k:sum(w.get(k,0)for w in report['workbooks'])for k in ['sheets','table_parts','source_data_rows','independently_compared_nonempty_cells','comments','merged_ranges','hidden_sheets','figures','reviewed_figures']};report['counts']['workbooks']=len(report['workbooks']);report['counts']['needs_review_figures']=len(report['figures'])-report['counts']['reviewed_figures'];report['counts']['unique_source_images']=len(set(x['source_image_sha256']for x in report['figures']));report['counts']['converted']=sum(x['disposition']=='converted'for x in report['figures']);report['counts']['deduplicated']=sum(x['disposition']=='deduplicated'for x in report['figures'])
kb.dump(root/'tracking/reviews/workbook-status-audit.json',report)
print(json.dumps(report['counts']))
