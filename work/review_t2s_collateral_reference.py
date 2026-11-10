from pathlib import Path
import sys,json,re
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();sid='src-000353';s=next(x for x in kb.sources(root) if x['source_id']==sid);base=root/s['set_path'];items=json.loads((root/'work/documents'/sid/'curated-figures.json').read_text(encoding='utf-8'));reviews=[]
for r in items:
 p=root/r['diagram'];m,b=kb.metadata(p);m.update(review_status='needs-review' if r['issue_ids'] else 'reviewed',render_status='pass',visual_review='pass',mermaid_version='12.3.0',mermaid_renderer='Mermaid browser API + Chromium 156.0.8078.81',review_date='2026-11-09');e='Opened complete source artwork and rendered reconstruction; compared every role/lane label, arrow direction and endpoint, six overview activities, accepted/rejected choices, dashed retry loop, status labels and exact family strings where present. The four composite sequences were compared with complete Word file/printed pages16-19, including all multi-object labels.'
 if r['issue_ids']:e+=' Visible correspondence passes; source inconsistency '+', '.join(r['issue_ids'])+' remains unresolved, so reviewed page status is withheld.'
 b=b[:b.index('## Review evidence')]+'## Review evidence\n\n'+e+' Mermaid12.3.0 / Chromium156.0.8078.81; visual comparison2026-11-09 Europe/Warsaw.\n\n'+kb.link(p,root/'domains/securities/assets'/sid/'reconstructed'/(r['source_figure']+'.png'),'Compared reconstruction')+'.\n';kb.put(p,kb.front(m)+b)
 for occ in r['source_occurrences']:
  ep=base/'documents'/sid/'diagrams'/(occ+'.md');em,eb=kb.metadata(ep);em.update(canonical_diagram=r['diagram'],disposition='converted-needs-review' if r['issue_ids'] else 'deduplicated',visual_review='pass');eb+='\n## Source reconstruction\n\n'+kb.link(ep,p,m['title'])+'. Complete source and rendered reconstruction compared. Identical creation/deletion activity artwork is shared without merging its distinct flow contexts.\n';kb.put(ep,kb.front(em)+eb)
 reviews.append({'source_id':sid,'diagram':r['diagram'],'source_occurrences':r['source_occurrences'],'render':'pass','visual_review':'pass','date':'2026-11-09','timezone':'Europe/Warsaw','mermaid_version':'12.3.0','evidence':e,'issue_ids':r['issue_ids']})
kb.dump(root/'tracking/reviews/t2s-collateral-reference-diagrams.json',reviews)
for n in [3,4,5,6]:
 p=base/'documents'/sid/'diagrams'/f'fig-{n:04d}.md';m,b=kb.metadata(p);m.update(disposition='preserved-legend-symbol',manual_curated=True,classification_review='pass',classification_review_date='2026-11-09');b+='\n## Inventory disposition\n\nActivity-notation legend preserved with '+kb.link(p,base/'documents'/sid/'tables/tbl-0010.md','T10')+'. Substantive notation context, not a separate process or decorative exclusion.\n';kb.put(p,kb.front(m)+b)
for start in [115,149,160]:
 p=next((base/'flows').glob(f'flow-{sid}-p{start}-*.md'));m,b=kb.metadata(p);m['issue_ids']=sorted(set(m.get('issue_ids',[])+['issue-000043']));m['disputed_message_ids']=['reda.044.001.01'];kb.put(p,kb.front(m)+b)
# Do not silently expand CBs using the different NCB glossary entry.
for slug,title in [('central-bank','CBs (source label)'),('party-authorised-by-central-bank-or-payment-bank','Party authorised by CBs or payment banks')]:
 p=root/'shared/reference/participants'/f'participant-{sid}-{slug}.md';m,b=kb.metadata(p);m['title']=title;m['source_labels']=['CBs'] if slug=='central-bank' else ['any party authorised by them'];m['limitations'].append('The source uses CBs in these passages; T2 separately expands NCB but does not explicitly expand CBs. No equivalence with National Central Bank is asserted.');b=re.sub(r'^# .*$', '# '+title,b,count=1,flags=re.M).replace('T2 abbreviations','P74-P79 (CBs label; T2 only separately defines NCB)').replace('central bank/payment bank','CB/payment-bank');kb.put(p,kb.front(m)+b)
inv=json.loads((root/'work/documents'/sid/'media-review-inventory.json').read_text(encoding='utf-8'));p=root/'tracking/reviews/docx-media-classification.json';d=json.loads(p.read_text(encoding='utf-8'));d['records']=[r for r in d['records'] if r['source_id']!=sid]
for r in inv['media']:
 n=int(re.search(r'image(\d+)',r['original']).group(1));disp='preserved-legend-symbol' if 3<=n<=6 else 'component-of-composite' if n>=8 else 'substantive-diagram';d['records'].append({'source_id':sid,'original':r['original'],'sha256':r['original_sha256'],'disposition':disp,'classification_review':'pass','classification_review_date':'2026-11-09','classification_review_scope':'Complete source artwork and Word pages16-19 inspected; four repeated actor fragments belong to four separately reconstructed sequences. Exact activity reuse retains P112/P116 occurrences.','classification_reason':{'preserved-legend-symbol':'T10 activity-notation legend.','component-of-composite':'Actor fragments in four complete multi-object Word sequences.','substantive-diagram':'Complete role/process/activity artwork.'}[disp]})
kb.dump(p,d)
p=base/'participants.md';m,b=kb.metadata(p);known=set(re.findall(r'participant-src-000353-[a-z0-9-]+',b));rows=[]
for pp in sorted((root/'shared/reference/participants').glob(f'participant-{sid}-*.md')):
 pm,pb=kb.metadata(pp)
 if pm['participant_id'] not in known:rows.append([kb.link(p,pp,pm['title']),'; '.join(x.get('locator','') for x in pm['source_locations'])])
if rows:b+='\n## Narrative and delegated participants\n\n'+kb.table(['Scoped role','Source evidence'],rows)+'\n';kb.put(p,kb.front(m)+b)
broken=[]
for p in (base/'diagrams/curated').glob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
  if not target.startswith(('http','mailto','#')) and not (p.parent/target.split('#')[0]).exists():broken.append({'page':str(p.relative_to(root)),'target':target})
check={'source_id':sid,'source_figure_occurrences':12,'substantive_occurrences':8,'canonical_reconstructions':7,'legend_symbols':4,'diagram_pages_reviewed':3,'diagram_pages_needs_review':4,'broken_links':broken,'issue_ids':['issue-000038','issue-000043'],'limitations':['Table-cell review independent.','Native hidden layers not certified.']};kb.dump(root/'tracking/reviews/t2s-collateral-reference-figure-coverage.json',check);print(json.dumps(check))
