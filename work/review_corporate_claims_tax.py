from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();base=root/'domains/securities/reference/message-sets/corporate-actions/2025-2026';items=json.loads((root/'work/documents/src-000079/claims-tax-curation.json').read_text(encoding='utf-8'));reviews=[]
for r in items:
 p=root/r['diagram'];m,b=kb.metadata(p);m.update(review_status='reviewed',render_status='pass',visual_review='pass',mermaid_renderer='Mermaid browser API + Chromium 156.0.8078.81',mermaid_version='12.3.0',review_date='2026-11-09')
 evidence=f"Opened full-size original vector preview and rendered PNG. Verified both functional participants, Message Gateway and Payment Management Process in the Account Owner context, all {r['paths']} incoming and {r['paths']} outgoing paths, their letter labels and arrow directions, all source message-block qualifiers, and the orange preliminary-advice/cancellation versus black confirmation paths. Node layout changes do not add temporal constraints; source path letters remain authoritative."
 b=b[:b.index('## Review evidence')]+'## Review evidence\n\n'+evidence+' Parse/render passed with Mermaid 12.3.0 and Chromium 156.0.8078.81. Visual review date 2026-11-09 Europe/Warsaw; render report UTC date 2026-11-08.\n\n'+kb.link(p,root/'domains/securities/assets/src-000079/reconstructed-claims-tax'/(r['source_figure']+'.png'),'Visually checked reconstruction')+'.\n';kb.put(p,kb.front(m)+b)
 ep=base/'documents/src-000079/diagrams'/(r['source_figure']+'.md');em,eb=kb.metadata(ep);em.update(canonical_diagram=r['diagram'],disposition='deduplicated',visual_review='pass');eb+='\n## Reviewed reconstruction\n\n'+kb.link(ep,p,m['title'])+'. Original and rendered reconstruction visually compared.\n';kb.put(ep,kb.front(em)+eb)
 reviews.append({'diagram':r['diagram'],'source_id':'src-000079','source_figure':r['source_figure'],'render':'pass','visual_review':'pass','date':'2026-11-09','timezone':'Europe/Warsaw','mermaid_version':'12.3.0','evidence':evidence})
for participant in ['account-owner','account-servicer']:
 pp=root/'shared/reference/participants'/('participant-src-000079-'+participant+'.md');pm,pb=kb.metadata(pp);pm['manual_curated']=True;pm['flows']=sorted(set(pm.get('flows',[])+['flow-corporate-actions-market-claims-tax-refunds']));pb+='\nRelated source flow: '+kb.link(pp,root/items[0]['flow'],'Market claim, compensation and tax refund preliminary advice')+'.\n';kb.put(pp,kb.front(pm)+pb)
kb.dump(root/'tracking/reviews/corporate-claims-tax-diagrams.json',reviews)
