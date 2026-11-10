from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();base=root/'domains/securities/reference/message-sets/corporate-actions/2025-2026';items=json.loads((root/'work/documents/src-000079/routing-curation.json').read_text(encoding='utf-8'));reviews=[]
for r in items:
 p=root/r['diagram'];m,b=kb.metadata(p);n=int(r['source_figure'].split('-')[-1]);issue='issue-000027' if n==34 else r.get('issue');visual='partial' if n==34 else 'pass';m.update(review_status='needs-review' if issue else 'reviewed',render_status='pass',visual_review=visual,mermaid_renderer='Mermaid browser API + Chromium 156.0.8078.81',mermaid_version='12.3.0',review_date='2026-11-09',issue_ids=[issue] if issue else [])
 evidence=f"Opened the full source image and rendered reconstruction. Compared all {r['paths']} lettered source paths, {r['outgoing']} outward instruction path(s), message blocks, arrow direction, every internal-process destination, source colors and timing/footnotes. The rendering repositions the source entities but preserves the observed relationships. Line breaks were adjusted and re-rendered to keep labels clear of connectors."
 if n==34:evidence+=' The MT567 IPRC-to-PACK separator cannot be read unambiguously from the supplied low-resolution image; a separate enlarged crop and independent review agree. The reconstruction explicitly labels this uncertainty instead of selecting one or two slash strokes (issue-000027). Other labels and routing were compared.'
 if n==42:evidence+=' Artwork direction and labels match; the source narrative contradiction at P362 remains unresolved (issue-000026), so the page is not marked reviewed.'
 b=b[:b.index('## Review evidence')]+'## Review evidence\n\n'+evidence+' Parse/render passed with Mermaid 12.3.0 and Chromium 156.0.8078.81. Visual comparison on 2026-11-09 Europe/Warsaw; render report UTC date 2026-11-08.\n\n'+kb.link(p,root/'domains/securities/assets/src-000079/reconstructed-routing'/(r['source_figure']+'.png'),'Visually checked reconstruction')+'.\n';kb.put(p,kb.front(m)+b)
 ep=base/'documents/src-000079/diagrams'/(r['source_figure']+'.md');em,eb=kb.metadata(ep);em.update(canonical_diagram=r['diagram'],disposition='deduplicated' if not issue else 'converted-needs-review',visual_review=visual);eb+='\n## Source reconstruction\n\n'+kb.link(ep,p,m['title'])+'. Original and rendered reconstruction visually compared. '+('The recorded source ambiguity remains open.' if issue else 'All source paths and labels checked.')+'\n';kb.put(ep,kb.front(em)+eb)
 fp=root/r['flow'];fm,fb=kb.metadata(fp);fm['manual_curated']=True
 if issue:fm['issue_ids']=sorted(set(fm.get('issue_ids',[])+[issue]));fm['limitations']=list(dict.fromkeys(fm.get('limitations',[])+m['limitations']))
 if n==34:fb=fb.replace('25D::IPRC/PACK','25D::IPRC [separator unclear] PACK');fb+='\nSource-legibility limitation: P332/image34 does not establish whether the MT567 IPRC-to-PACK separator has one or two slash strokes. Both the unmodified original and enlarged inspection crop were reviewed; issue-000027 remains open.\n'
 kb.put(fp,kb.front(fm)+fb)
 for participant in ['account-owner','account-servicer']:
  pp=root/'shared/reference/participants'/('participant-src-000079-'+participant+'.md');pm,pb=kb.metadata(pp);pm['manual_curated']=True
  pm['flows']=sorted(set(pm.get('flows',[])+[fm['flow_id']]))
  entry='\nSource scenario: '+kb.link(pp,fp,fm.get('title','Routing scenario'))+'; '+kb.link(pp,p,'source diagram')+'.\n'
  if entry not in pb:pb+=entry
  kb.put(pp,kb.front(pm)+pb)
 reviews.append({'diagram':r['diagram'],'source_id':'src-000079','source_figure':r['source_figure'],'render':'pass','visual_review':visual,'date':'2026-11-09','timezone':'Europe/Warsaw','mermaid_version':'12.3.0','evidence':evidence,'issue_ids':[issue] if issue else []})
kb.dump(root/'tracking/reviews/corporate-routing-diagrams.json',reviews)
p=base/'flows/flow-src-000079-p270-reversal.md';m,b=kb.metadata(p);m['manual_curated']=True
section='''\n## Direction of reported movements in reversal advice\n\nSource src-000079, Business Scenarios / Scenario 5: Mandatory Event with Reversal of Payment, P344-P346, distinguishes the direction of reported movements from the direction of the message exchange. The preliminary advice of a reversal reports movements opposite to those in the referred movement confirmation: credits become debits and debits become credits (P344). The actual movement reversal reports movements identical to those in the referred confirmation (P345). Where the final entitlements are re-booked after a reversal, the source recommends treating that re-booking as a new payment, subject to the agreed preliminary-advice criteria (P346). Both preliminary advice and reversal messages in image37 flow from the account servicer to the account owner.\n\n'''+kb.link(p,base/'diagrams/routing-scenarios/fig-0037.md','Scenario 5 source reconstruction')+'.\n'
if '## Direction of reported movements in reversal advice' not in b:b+=section
kb.put(p,kb.front(m)+b)
print('Recorded 12 routing reviews; 10 reviewed, 2 needs-review. Added reversal movement-direction distinction.')
