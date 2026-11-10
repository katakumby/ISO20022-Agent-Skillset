from pathlib import Path
import json,sys
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();base=root/'domains/securities/reference/message-sets/corporate-actions/2025-2026';out=base/'diagrams/overview'
check=[('fig-0001','fig-0002','All sixteen role-to-participant arrows, both functional roles, all business-role labels and the two source sides match. Decorative silhouettes and side divider are explicitly represented differently. No inheritance or message direction was inferred.'),('fig-0002','fig-0003','All nine top-level processes and all fourteen named child-process nodes, including the two Event Status children, match their source grouping. All connectors are undirected. Source ovals are represented as process nodes without inferred use-case semantics.'),('fig-0003','fig-0014','All seven named activities, start and two end points, both source-bar labels, all seven Yes/No branch labels and two cross-participant arrows match. Source bars remain explicitly identified; ambiguity issue-000020 prevents a reviewed business interpretation.')]
reviews=[]
for did,original,evidence in check:
 p=out/(did+'.md');m,b=kb.metadata(p);m.update(render_status='pass',visual_review='pass',review_status='needs-review' if did=='fig-0003' else 'reviewed',mermaid_renderer='Mermaid browser API + Chromium 156.0.8078.81',mermaid_version='12.3.0',review_date='2026-11-09')
 if did=='fig-0003':m['issue_ids']=['issue-000020']
 text='The unchanged original and Mermaid-rendered PNG were both opened and compared on 2026-11-09 (Europe/Warsaw). '+evidence+' Parse and render passed with Mermaid 12.3.0 and Chromium 156.0.8078.81. The render report records the UTC date 2026-11-08; local visual review date is 2026-11-09.\n\n'+kb.link(p,root/'domains/securities/assets/src-000079/reconstructed-overview'/(did+'.png'),'Rendered reconstruction')+'.\n'
 b=b[:b.index('## Review evidence')]+ '## Review evidence\n\n'+text;kb.put(p,kb.front(m)+b)
 ep=base/'documents/src-000079/diagrams'/(original+'.md');em,eb=kb.metadata(ep);em.update(canonical_diagram=p.relative_to(root).as_posix(),disposition='deduplicated' if did!='fig-0003' else 'reconstructed-needs-review',visual_review='pass');eb+='\n## Curated reconstruction\n\n'+kb.link(ep,p,m['title'])+'. Source and rendered reconstruction visually compared; '+('business interpretation remains open under issue-000020.' if did=='fig-0003' else 'canonical reconstruction reviewed.')+'\n';kb.put(ep,kb.front(em)+eb)
 reviews.append({'diagram':p.relative_to(root).as_posix(),'source_id':'src-000079','source_figure':original,'render':'pass','visual_review':'pass','date':'2026-11-09','timezone':'Europe/Warsaw','mermaid_version':'12.3.0','evidence':evidence,'limitations':m.get('limitations',[])})
 for part in m.get('participants',[]):
  pp=root/'shared/reference/participants'/(part+'.md');pm,pb=kb.metadata(pp);pm['manual_curated']=True
  link=kb.link(pp,p,m['title'])
  if link not in pb:pb+='\nSource diagram: '+link+'.\n'
  kb.put(pp,kb.front(pm)+pb)
 for flow in m.get('flow_ids',[]):
  fp=base/'flows'/(flow+'.md');fm,fb=kb.metadata(fp);fm['manual_curated']=True;fb+='\nSource activity diagram: '+kb.link(fp,p,m['title'])+'. The conditional use of parallel bars remains ambiguous (issue-000020).\n';kb.put(fp,kb.front(fm)+fb)
kb.dump(root/'tracking/reviews/corporate-overview-diagrams.json',reviews)
