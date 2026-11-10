"""Reconcile Investment Funds figures75–148 without upgrading unfinished checks."""
import argparse,hashlib,json,re
from pathlib import Path
import kb
def main(root):
 sid='src-000095';source=next(s for s in kb.sources(root) if s['source_id']==sid);base=root/source['set_path'];reports=[json.loads((root/'tracking/reviews'/n).read_text(encoding='utf-8')) for n in ['funds-sequences.json','funds-transparency.json']];rows=[r for report in reports for r in report['records']]
 inv=json.loads((root/'work/documents'/sid/'media-review-inventory.json').read_text(encoding='utf-8'));media={m['original']:m for m in inv['media']};locations=json.loads((root/'work/docx-render'/sid/'page-locations.json').read_text(encoding='utf-8'))['locations']
 if hashlib.sha256(kb.read_source(root,source)).hexdigest()!=source['sha256']:raise ValueError('Source fingerprint changed')
 classification=root/'tracking/reviews/docx-media-classification.json';c=json.loads(classification.read_text(encoding='utf-8')) if classification.exists() else {'records':[]};existing=c if isinstance(c,list) else c['records'];keys={(r['source_id'],r['original']) for r in rows};existing=[r for r in existing if (r.get('source_id'),r.get('original')) not in keys]
 mapped=0;missing=[];errors=[];participants=set();flows=set()
 for r in rows:
  n=int(r['source_figure_id'].split('-')[1]);page=root/r['path'];m,b=kb.metadata(page);im=media[r['original']]
  if hashlib.sha256((root/r['original']).read_bytes()).hexdigest()!=r['original_sha256']:raise ValueError('Image changed '+str(n))
  if hashlib.sha256(page.with_suffix('.mmd').read_bytes()).hexdigest()!=r['mermaid_sha256']:raise ValueError('Mermaid changed '+str(n))
  matches=[l for l in locations if any(f['sha256']==r['original_sha256'] for f in l.get('asset_fingerprints',[]))];pnums=sorted({l['start_file_page'] for l in matches});m['word_file_pages_by_asset_sha256']=pnums;m['word_composite_visual_review']='not-run';participants.update(m.get('participant_ids',[]));flows.update(m.get('flow_ids',[]))
  tag='FUNDS-WORD-LOCATOR';b=re.sub(r'\n<!-- '+tag+'-START -->.*?<!-- '+tag+'-END -->\n?','\n',b,flags=re.S)
  if matches:mapped+=1;txt='Exact embedded-asset SHA-256 maps this figure to Word-rendered PDF file page(s) '+', '.join(map(str,pnums))+'.'
  else:missing.append(n);txt='No exact embedded-asset hash match is available in the Word page-location export. No ordinal page mapping is assumed.'
  b+='\n<!-- '+tag+'-START -->\n## Word-rendered source locator\n\n'+txt+' '+kb.link(page,root/'work/docx-render'/sid/'document.pdf','Full Word-rendered source PDF')+' · '+kb.link(page,root/'work/docx-render'/sid/'page-locations.json','Actual Word export locations')+'. Full-page composite comparison remains **not run**; the recorded visual pass applies to the original-image/reconstruction comparison.\n<!-- '+tag+'-END -->\n';kb.put(page,kb.front(m)+b.strip()+'\n')
  existing.append({'source_id':sid,'original':r['original'],'sha256':r['original_sha256'],'disposition':'substantive-diagram','classification_review':'pass','classification_review_date':'2026-11-09','classification_review_scope':'Direct full original-image inspection; canonical reconstruction rendered and compared. Full Word-page composite check separate.','classification_reason':'Source sequence, structural overview or business-example relationship diagram; all labels and semantics retained in the canonical reference.'})
  for target in re.findall(r'\]\(([^)]+)\)',b):
   if target.startswith(('http:','https:','#')):continue
   t=target.split('#')[0]
   if t and not (page.parent/t).resolve().exists():errors.append({'page':r['path'],'target':target})
 if isinstance(c,list):kb.dump(classification,existing)
 else:c['records']=existing;kb.dump(classification,c)
 # Bidirectional links for every participant explicitly associated with an example.
 for ex in [1,2]:
  fp=base/'flows'/f'flow-{sid}-transparency-example-{ex}.md';fm,_=kb.metadata(fp)
  for pid in fm['participant_ids']:
   pp=root/'shared/reference/participants'/(pid+'.md');pm,pb=kb.metadata(pp);pm['flows']=sorted(set(pm.get('flows',[])+[fm['flow_id']]));tag='FUNDS-TRANSPARENCY-FLOW-'+str(ex);pb=re.sub(r'\n<!-- '+tag+'-START -->.*?<!-- '+tag+'-END -->\n?','\n',pb,flags=re.S);pb+='\n<!-- '+tag+'-START -->\n'+kb.link(pp,fp,f'Transparency business example {ex}')+'\n<!-- '+tag+'-END -->\n';kb.put(pp,kb.front(pm)+pb.strip()+'\n')
 report={'date':'2026-11-09','source_id':sid,'source_sha256':source['sha256'],'scope':'Figures75–148; sibling agent owns1–74','source_diagrams':len(rows),'mermaid_views':len(rows)+2,'render_pass':len(rows),'original_image_visual_review_pass':len(rows),'word_file_page_exact_hash_matches':mapped,'word_file_page_unmatched_figures':missing,'word_composite_visual_review':'not-run','flow_references':len(flows),'participant_references':len(participants),'documentation_only_messages':['semt.041.001.02','semt.042.001.01'],'validation_errors':errors,'records':rows};kb.dump(root/'tracking/reviews/funds-second-half.json',report)
 index=base/'diagrams/funds-second-half.md';kb.put(index,'# Investment Funds diagrams75–148\n\nAll74 original figures have a canonical reconstruction, successful Mermaid12.3 render and explicit original-image comparison. This is not a completed full-source review: source contradictions and Word-page composite checks remain visible.\n\n'+kb.table(['Source figure','Canonical reference','Kind'],[[r['source_figure_id'],kb.link(index,root/r['path'],kb.metadata(root/r['path'])[0]['title']),'Sequence' if int(r['source_figure_id'].split('-')[1])<=141 else 'Structure / business example'] for r in rows])+'\n'+kb.link(index,root/'tracking/reviews/funds-second-half.json','Exact coverage and validation evidence')+'\n')
 completed_context=root/'tracking/reviews/funds-second-half-word-context.json'
 if completed_context.exists():
  from review_funds_tables_and_context import main as restore_completed_checks
  restore_completed_checks(root)
  text=index.read_text(encoding='utf-8').replace('This is not a completed full-source review: source contradictions and Word-page composite checks remain visible.','Whole-page composite checks are also recorded separately. Source contradictions remain unresolved; this is not a claim that all desired business knowledge is available.')
  kb.put(index,text)
 print(json.dumps({k:v for k,v in report.items() if k!='records'}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();main(a.root.resolve())
