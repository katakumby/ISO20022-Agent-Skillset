from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();base=root/'domains/securities/reference/message-sets/corporate-actions/2025-2026';items=json.loads((root/'work/documents/src-000079/timeline-curation.json').read_text(encoding='utf-8'));reviews=[]
for r in items:
 p=root/r['diagram'];m,b=kb.metadata(p);m.update(review_status='reviewed',render_status='pass',visual_review='pass',mermaid_renderer='Mermaid browser API + Chromium 156.0.8078.81',mermaid_version='12.3.0',review_date='2026-11-09');evidence=f"Opened the source PNG and Mermaid render. Compared both functional actors, all {r['activities']} ordered phases and activity labels, {r['owner_to_servicer']} owner-to-servicer arrow(s) and remaining servicer-to-owner arrows, plus every date/deadline label. Horizontal source time axis is represented vertically; P161 event-dependent ordering/concurrency limitation is retained."
 b=b[:b.index('## Review evidence')]+'## Review evidence\n\n'+evidence+' Parse/render passed with Mermaid 12.3.0 and Chromium 156.0.8078.81. Visual comparison on 2026-11-09 Europe/Warsaw; render report UTC date 2026-11-08.\n\n'+kb.link(p,root/'domains/securities/assets/src-000079/reconstructed-timelines'/(r['source_figure']+'.png'),'Visually checked reconstruction')+'.\n';kb.put(p,kb.front(m)+b)
 ep=base/'documents/src-000079/diagrams'/(r['source_figure']+'.md');em,eb=kb.metadata(ep);em.update(canonical_diagram=r['diagram'],disposition='deduplicated',visual_review='pass');eb+='\n## Reviewed reconstruction\n\n'+kb.link(ep,p,m['title'])+'. Original and rendered reconstruction visually compared.\n';kb.put(ep,kb.front(em)+eb)
 for participant in ['account-owner','account-servicer']:
  pp=root/'shared/reference/participants'/('participant-src-000079-'+participant+'.md');pm,pb=kb.metadata(pp);pm['manual_curated']=True;pb+='\nSource timeline: '+kb.link(pp,p,m['title'])+'.\n';kb.put(pp,kb.front(pm)+pb)
 reviews.append({'diagram':r['diagram'],'source_id':'src-000079','source_figure':r['source_figure'],'render':'pass','visual_review':'pass','date':'2026-11-09','timezone':'Europe/Warsaw','mermaid_version':'12.3.0','evidence':evidence})
kb.dump(root/'tracking/reviews/corporate-timeline-diagrams.json',reviews)
