from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();base=root/'domains/securities/reference/message-sets/corporate-actions/2025-2026';items=json.loads((root/'work/documents/src-000079/activity-curation.json').read_text(encoding='utf-8'));reviews=[]
for r in items:
 p=root/r['diagram'];m,b=kb.metadata(p);m.update(review_status='reviewed',render_status='pass',visual_review='pass',mermaid_renderer='Mermaid browser API + Chromium 156.0.8078.81',mermaid_version='12.3.0',review_date='2026-11-09')
 evidence='Opened full-size unchanged source image or vector preview and rendered PNG. Compared both functional participants, start point, two named activities, source arrow direction and any source note/edge label.' if r['type']=='activity' else 'Opened unchanged source and rendered PNG. Compared both functional participants and all eight exact information-category labels, with seven arrows to Account Owner and one instruction arrow to Account Servicer. Explicitly disclosed the narrower narrative direction in this overview versus the detailed bidirectional source scenario.'
 b=b[:b.index('## Review evidence')]+'## Review evidence\n\n'+evidence+' Parse/render passed with Mermaid 12.3.0 and Chromium 156.0.8078.81. Visual review date 2026-11-09 Europe/Warsaw; the render report records UTC 2026-11-08. Label wrapping/background styling improves legibility without altering source wording.\n\n'+kb.link(p,root/'domains/securities/assets/src-000079/reconstructed-activities'/(r['source_figure']+'.png'),'Visually checked reconstruction')+'.\n';kb.put(p,kb.front(m)+b)
 ep=base/'documents/src-000079/diagrams'/(r['source_figure']+'.md');em,eb=kb.metadata(ep);em.update(canonical_diagram=r['diagram'],disposition='deduplicated',visual_review='pass');eb+='\n## Reviewed reconstruction\n\n'+kb.link(ep,p,m['title'])+'. Source artwork and rendered reconstruction visually compared.\n';kb.put(ep,kb.front(em)+eb)
 if r.get('flow'):
  fp=root/r['flow'];fm,fb=kb.metadata(fp);fm['manual_curated']=True;fb+='\nRelated source activity diagram: '+kb.link(fp,p,m['title'])+'.\n';kb.put(fp,kb.front(fm)+fb)
 for participant in m['participants']:
  pp=root/'shared/reference/participants'/(participant+'.md');pm,pb=kb.metadata(pp);pm['manual_curated']=True;pb+='\nSource activity/overview: '+kb.link(pp,p,m['title'])+'.\n';kb.put(pp,kb.front(pm)+pb)
 reviews.append({'diagram':r['diagram'],'source_id':'src-000079','source_figure':r['source_figure'],'render':'pass','visual_review':'pass','date':'2026-11-09','timezone':'Europe/Warsaw','mermaid_version':'12.3.0','evidence':evidence})
kb.dump(root/'tracking/reviews/corporate-activity-diagrams.json',reviews)
