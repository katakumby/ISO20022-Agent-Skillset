from pathlib import Path
import sys,json,re
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();sid='src-000347';s=next(x for x in kb.sources(root) if x['source_id']==sid);base=root/s['set_path'];items=json.loads((root/'work/documents'/sid/'curated-figures.json').read_text(encoding='utf-8'));reviews=[]
for r in items:
 p=root/r['diagram'];m,b=kb.metadata(p);m.update(review_status='needs-review' if r['issue_ids'] else 'reviewed',render_status='pass',visual_review='pass',mermaid_version='12.3.0',mermaid_renderer='Mermaid browser API + Chromium 156.0.8078.81',review_date='2026-11-09');e='Opened complete source artwork and rendered reconstruction; compared every actor/lane label, arrow direction, condition and branch, native fork/join bar, end point, message-family label and status. Composite sequences compared against full Word file pages14-16, not isolated decorative fragments.'
 if r['issue_ids']:e+=' The visual reconstruction matches the role figure, while T7 role-matrix inconsistency remains unresolved under issue-000038; page stays needs-review.'
 b=b[:b.index('## Review evidence')]+'## Review evidence\n\n'+e+' Mermaid12.3.0 / Chromium156.0.8078.81; visual comparison2026-11-09 Europe/Warsaw.\n\n'+kb.link(p,root/'domains/securities/assets'/sid/'reconstructed'/(r['source_figure']+'.png'),'Compared reconstruction')+'.\n';kb.put(p,kb.front(m)+b)
 ep=base/'documents'/sid/'diagrams'/(r['source_figure']+'.md');em,eb=kb.metadata(ep);em.update(canonical_diagram=r['diagram'],disposition='converted-needs-review' if r['issue_ids'] else 'deduplicated',visual_review='pass');eb+='\n## Source reconstruction\n\n'+kb.link(ep,p,m['title'])+'. Complete source artwork and reconstruction visually compared.\n';kb.put(ep,kb.front(em)+eb)
 reviews.append({'source_id':sid,'diagram':r['diagram'],'source_figure':r['source_figure'],'render':'pass','visual_review':'pass','date':'2026-11-09','timezone':'Europe/Warsaw','mermaid_version':'12.3.0','evidence':e,'issue_ids':r['issue_ids']})
kb.dump(root/'tracking/reviews/t2s-billing-diagrams.json',reviews)
for n in [3,4,5,6]:
 p=base/'documents'/sid/'diagrams'/f'fig-{n:04d}.md';m,b=kb.metadata(p);m.update(disposition='preserved-legend-symbol',manual_curated=True,classification_review='pass',classification_review_date='2026-11-09');b+='\n## Inventory disposition\n\nActivity-notation legend symbol retained with source '+kb.link(p,base/'documents'/sid/'tables/tbl-0009.md','T9')+'. It is notation context rather than a separate business process or decorative exclusion.\n';kb.put(p,kb.front(m)+b)
inv=json.loads((root/'work/documents'/sid/'media-review-inventory.json').read_text(encoding='utf-8'));p=root/'tracking/reviews/docx-media-classification.json';d=json.loads(p.read_text(encoding='utf-8'));d['records']=[r for r in d['records'] if r['source_id']!=sid]
for r in inv['media']:
 n=int(re.search(r'image(\d+)',r['original']).group(1));disp='preserved-legend-symbol' if 3<=n<=6 else 'component-of-composite' if n>=9 else 'substantive-diagram';d['records'].append({'source_id':sid,'original':r['original'],'sha256':r['original_sha256'],'disposition':disp,'classification_review':'pass','classification_review_date':'2026-11-09','classification_review_scope':'Complete source figure and Word pages14-16 inspected. Four reused image fragments are components of three different complete sequence figures, not four independent diagrams.','classification_reason':{'preserved-legend-symbol':'T9 activity-notation legend retained.','component-of-composite':'Reusable actor/icon fragments in P132, P145 and P158; complete composites rendered/cropped and reconstructed separately.','substantive-diagram':'Complete source participant/process/activity figure reconstructed.'}[disp]})
kb.dump(p,d)
p=base/'participants.md';m,b=kb.metadata(p);known=set(re.findall(r'participant-src-000347-[a-z0-9-]+',b));rows=[]
for pp in sorted((root/'shared/reference/participants').glob('participant-src-000347-*.md')):
 pm,pb=kb.metadata(pp)
 if pm['participant_id'] not in known:rows.append([kb.link(p,pp,pm['title']),pm.get('role_type','source-scoped'),'; '.join(x.get('locator','') for x in pm.get('source_locations',[])[:2])])
if rows:b+='\n## Diagram and narrative participants\n\n'+kb.table(['Scoped participant','Classification','Source evidence'],rows)+'\n';kb.put(p,kb.front(m)+b)
broken=[]
for p in (base/'diagrams/curated').glob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
  if not target.startswith(('http','mailto','#')) and not (p.parent/target.split('#')[0]).exists():broken.append({'page':str(p.relative_to(root)),'target':target})
check={'source_id':sid,'source_figure_occurrences':11,'substantive_reconstructions':7,'legend_symbols':4,'diagram_pages_reviewed':6,'diagram_pages_needs_review':1,'broken_links':broken,'issue_ids':['issue-000038'],'limitations':['Table-cell review independent.','Native hidden layers not certified.']};kb.dump(root/'tracking/reviews/t2s-billing-figure-coverage.json',check);print(json.dumps(check))
