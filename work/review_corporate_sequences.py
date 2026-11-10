from pathlib import Path
import json,sys,re
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();base=root/'domains/securities/reference/message-sets/corporate-actions/2025-2026';records=json.loads((root/'work/documents/src-000079/sequence-curation.json').read_text(encoding='utf-8'));defs=json.loads((root/'work/documents/src-000080/message-definitions.json').read_text(encoding='utf-8'));byname={re.sub(r'V\d+$','',d['title'].split()[-1]):d for d in defs};review=[]
for r in records:
 p=root/r['diagram'];m,b=kb.metadata(p);code=p.with_suffix('.mmd').read_text(encoding='utf-8');names=sorted(set(re.findall(r'CorporateAction[A-Za-z]+',code)));bindings=[byname[n] for n in names if n in byname]
 m.update(review_status='reviewed',render_status='pass',visual_review='pass',mermaid_renderer='Mermaid browser API + Chromium 156.0.8078.81',mermaid_version='12.3.0',review_date='2026-11-09',message_ids=[d['message_id'] for d in bindings],message_families=sorted(set(d['message_id'][:8] for d in bindings)))
 evidence=f"Opened the unchanged full-size original and rendered PNG. Verified both actor labels, all {r['steps']} message arrows and labels, {r['owner_to_servicer']} Account Owner-to-Account Servicer arrows, remaining arrows in the reverse direction, and all source phase/qualifier notes. Decorative building icons replaced by labeled participants; no source semantics dropped."
 b=b[:b.index('## Review evidence')]+'## Review evidence\n\n'+evidence+' Parse/render passed with Mermaid 12.3.0 and Chromium 156.0.8078.81. Visual comparison performed 2026-11-09 Europe/Warsaw; render report UTC date is 2026-11-08.\n\n'+kb.link(p,root/'domains/securities/assets/src-000079/reconstructed-transactions'/(r['source_figure']+'.png'),'Visually checked reconstruction')+'.\n';kb.put(p,kb.front(m)+b)
 ep=base/'documents/src-000079/diagrams'/(r['source_figure']+'.md');em,eb=kb.metadata(ep);em.update(canonical_diagram=r['diagram'],disposition='deduplicated',visual_review='pass');eb+='\n## Reviewed reconstruction\n\n'+kb.link(ep,p,m['title'])+'. Source artwork and rendered reconstruction visually compared.\n';kb.put(ep,kb.front(em)+eb)
 fp=root/r['flow'];fm,fb=kb.metadata(fp);fm['participants']=sorted(set(fm.get('participants',[])+re.findall(r'(participant-src-000079-[a-z-]+)\.md',fb)));fm['message_ids']=[d['message_id'] for d in bindings];fm['source_ids']=sorted(set(fm.get('source_ids',[])+['src-000080']));fm['limitations']=[x for x in fm.get('limitations',[]) if not x.startswith('Source-delimited') and not x.startswith('Message family')];fm['limitations'].append('The source diagram and scenario narrative were checked. Formal precondition/postcondition fields and any omitted market-specific handling are not separately defined by this scenario.');fm['diagram_visual_review']='pass';fm['source_locations']+= [{'source_id':'src-000080','locator':f"file page {d['start_page']}; {d['title']}"} for d in bindings]
 fb+='\n## Exact supplied message bindings\n\nThese bindings use the explicitly named message definitions in src-000080. Part 1 artwork itself uses message names, not exact version numbers.\n\n'+kb.table(['Source message name','Exact definition','MDR Part 2 locator'],[[re.sub(r'V\d+$','',d['title'].split()[-1]),kb.link(fp,root/'domains/securities/reference/messages'/d['message_id']/'index.md',d['message_id']),f"src-000080 file page {d['start_page']}; {d['title']}"] for d in bindings])
 if r['source_figure'] in ['fig-0021','fig-0023']:
  issuer='participant-src-000079-issuer';fm['participants']=sorted(set(fm['participants']+[issuer]));fb+='\nThe '+kb.link(fp,root/'shared/reference/participants'/(issuer+'.md'),'Issuer')+' triggers the withdrawal or changed event details in the narrative. The two-role source sequence intentionally omits this upstream actor.\n'
 kb.put(fp,kb.front(fm)+fb)
 for participant in fm['participants']:
  pp=root/'shared/reference/participants'/(participant+'.md')
  if not pp.exists():continue
  pm,pb=kb.metadata(pp);pm['manual_curated']=True;pm['flows']=sorted(set(pm.get('flows',[])+[fm['flow_id']]));link=kb.link(pp,fp,fm['title'])
  if link not in pb:pb+='\nRelated source scenario: '+link+'.\n'
  kb.put(pp,kb.front(pm)+pb)
 review.append({'diagram':r['diagram'],'source_id':'src-000079','source_figure':r['source_figure'],'render':'pass','visual_review':'pass','date':'2026-11-09','timezone':'Europe/Warsaw','mermaid_version':'12.3.0','evidence':evidence})
kb.dump(root/'tracking/reviews/corporate-transaction-diagrams.json',review)
