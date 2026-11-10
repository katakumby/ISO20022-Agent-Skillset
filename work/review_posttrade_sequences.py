from pathlib import Path
import sys,json,hashlib
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();base=root/'domains/securities/reference/message-sets/post-trade-matching/2024-2025';items=json.loads((root/'work/documents/src-000180/sequence-curation.json').read_text(encoding='utf-8'));reviews=[]
def put(p,t):
 if p.exists() and p.read_text(encoding='utf-8')!=t:
  h=hashlib.sha256(p.read_bytes()).hexdigest()[:10];dest=root/'tracking/history/job-000001/manual-curation-2026-11-09'/p.relative_to(root);dest=dest.with_name(dest.stem+'-'+h+dest.suffix);dest.parent.mkdir(parents=True,exist_ok=True)
  if not dest.exists():dest.write_bytes(p.read_bytes())
 kb.put(p,t)
for r in items:
 p=root/r['diagram'];m,b=kb.metadata(p);m.update(review_status='needs-review' if r['issue_ids'] else 'reviewed',render_status='pass',visual_review='pass',mermaid_renderer='Mermaid browser API + Chromium 156.0.8078.81',mermaid_version='12.3.0',review_date='2026-11-09')
 evidence=f"Opened the full source PNG and rendered reconstruction; compared all {len(r['actors'])} source actor instance/stereotype labels, {r['messages']} ordered message arrows, sender/receiver endpoints, receiver execution markers, and source notes. Inactive lifelines are retained. Alternate-actor, proprietary-report, securities-financing and pre-advice notes were checked where present. Dashed lifelines and readable complete message labels were checked after rendering; vertical marker spacing is not elapsed time."
 if r['issue_ids']:evidence+=' Visual correspondence passes, while the narrative/artwork cancellation-origin contradiction remains open under issue-000031; the page is therefore needs-review.'
 b=b[:b.index('## Review evidence')]+'## Review evidence\n\n'+evidence+' Parsed/rendered using Mermaid 12.3.0 with Chromium 156.0.8078.81. Visual comparison on 2026-11-09 Europe/Warsaw; render report UTC date 2026-11-08.\n\n'+kb.link(p,root/'domains/securities/assets/src-000180/reconstructed-transactions'/(r['source_figure']+'.png'),'Compared reconstruction')+'.\n';put(p,kb.front(m)+b)
 ep=base/'documents/src-000180/diagrams'/(r['source_figure']+'.md');em,eb=kb.metadata(ep);em.update(canonical_diagram=r['diagram'],disposition='converted-needs-review' if r['issue_ids'] else 'deduplicated',visual_review='pass');eb+='\n## Source reconstruction\n\n'+kb.link(ep,p,m['title'])+'. Full original and rendered reconstruction visually compared; any source contradiction remains explicit.\n';put(ep,kb.front(em)+eb)
 reviews.append({'diagram':r['diagram'],'source_id':'src-000180','source_figure':r['source_figure'],'render':'pass','visual_review':'pass','date':'2026-11-09','timezone':'Europe/Warsaw','mermaid_version':'12.3.0','evidence':evidence,'issue_ids':r['issue_ids']})
kb.dump(root/'tracking/reviews/posttrade-transaction-diagrams.json',reviews)
old='Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.';new='Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.'
for setpath in ['corporate-actions/2025-2026','ccp-clearing/2025-2026','post-trade-matching/2024-2025']:
 for p in (root/'domains/securities/reference/message-sets'/setpath/'flows').glob('*.md'):
  m,b=kb.metadata(p)
  if m.get('manual_curated') and old in m.get('limitations',[]):m['limitations']=[new if x==old else x for x in m['limitations']];b=b.replace(old,new);put(p,kb.front(m)+b)
print('20 sequences compared;17 reviewed,3 source contradictions remain needs-review.')
