"""Build source162 figure pages from explicit transcription; review remains pending."""
from pathlib import Path
import json,hashlib,kb,extract_workbooks
from curate_payments_clearing_sequences import SPECS,FLOW
from payments_clearing_activities import models
root=Path(__file__).resolve().parents[1];SID='src-000162';DATE='2026-11-09';extract_workbooks.DATE=DATE
src=next(x for x in kb.sources(root) if x['source_id']==SID);base=root/src['set_path'];out=base/'diagrams/clearing';mmd=root/'work/payments-clearing/mmd'
FLOW.update({1:111,2:124,3:137,4:137,5:137,6:137,7:138,8:154,9:157,10:159,11:161})
PAGES={1:11,2:15,3:17,4:17,5:17,6:17,7:17,8:20,9:21,10:22,11:22,12:25,13:25,14:26,15:27,16:28,17:29,18:30,19:31,20:32,21:34,22:35,23:35,24:36,25:37,26:38,27:39,28:39,29:40,30:41,31:42,32:43,33:44,34:45,35:46,36:47,37:48,38:50,39:51,40:52,41:54,42:56,43:57,44:58,45:59,46:60,47:61,48:62,49:63}
for n,x in SPECS.items():
 x['kind']='sequenceDiagram';x['code']='sequenceDiagram\n'+''.join('participant '+i+' as '+v[0]+'\n' for i,v in x['actors'].items())
 for j,(a,b,l) in enumerate(x['events']):
  if n==16 and j==4:x['code']+='alt Case A: intermediary has not booked debtor-agent account\n'
  if n==16 and j==5:x['code']+='else Case B: intermediary has booked debtor-agent account\n'
  x['code']+=a+'->>'+b+': '+l+'\n'
 if n==16:x['code']+='end\n'
 if n==37:x['code']+='Note over DA,D: See note: optional simplified<br/>instruction (P475/P493)\n'
 if n==13:x['notes'].append('Word-rendered page25 has an unlabelled 0 above the middle pictogram; full page retains it. No additional participant or relationship is inferred from that isolated glyph.')
SPECS.update(models())
init=json.loads((root/'work/payments-initiation/models.json').read_text('utf8'))['models']
for n,k in [(8,10),(9,11),(10,12)]:
 q=next(x for x in init if x['figure_id']==f'fig-{k:04d}');p=root/q['path'];m,_=kb.metadata(p)
 SPECS[n]={'kind':m['diagram_kind'],'actors':q['actors'],'events':q['events'],'notes':['Byte-identical source artwork; source162 P'+str({8:154,9:157,10:159}[n])+' context and complete Word page checked. Responsibilities retain separate source162 participant scope.'],'canonical':q['path']}
for n in range(3,7):
 SPECS[n]={'kind':'activity-legend','actors':{},'events':[],'notes':['T23 row'+str(n-1)+' defines the same start/end/choice/parallel symbol. Exact image and source-context equivalence checked against reviewed canonical Funds legend.'],'canonical':f'domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-{n+2:04d}.md'}
inv=json.loads((root/'work/documents'/SID/'media-review-inventory.json').read_text('utf8'));media={int(o['figure_id'][4:]):(m,o) for m in inv['media'] for o in m['occurrences']};fence=chr(96)*3;results=[]
for n,x in sorted(SPECS.items()):
 p=out/f'fig-{n:04d}.md';item,occ=media[n];fl=next((base/'flows').glob(f'flow-{SID}-p{FLOW[n]}-*.md'));fm,_=kb.metadata(fl);issues=['issue-000054'] if n in [19,40,43,49] else []
 notes=x['notes']+['Source participant icons/labels denote contextual roles; they do not fix an institution to one role. Unused lifelines remain visible.','Source message names establish family-level flow context; supplied exact schema versions are separately identified.','Mermaid preserves connections and order; original retains precise geometry, pictograms and line style. Whole-page Word rendering checked for composite context.']
 title=' / '.join(occ['heading_path'][1:])+' — figure '+str(n)
 meta={'template':False,'document_kind':'diagram-occurrence' if x.get('canonical') else 'diagram','review_status':'needs-review','manual_curated':True,'diagram_id':f'fig-{n:04d}','title':title,'domain':'payments','source_ids':[SID],'source_editions':[src['source_edition']],'message_sets':['payments-clearing-and-settlement'],'participant_ids':sorted({'participant-'+SID+'-'+z for _,ss in x['actors'].values() for z in ss}),'flow_ids':[fm['flow_id']],'content_origin':'source-occurrence' if x.get('canonical') else 'source-reconstruction','diagram_kind':x['kind'],'original_asset':item['original'],'source_locations':[{'source_id':SID,'locator':occ['source_locator'],'heading_path':occ['heading_path'],'xml_path':occ['xml_path'],'rendered_file_page':PAGES[n]}],'render_status':'not-run','visual_review':'not-run','limitations':notes,'issue_ids':issues,'updated':DATE}
 body='# '+title+'\n\n'+kb.source_link(root,p,src)+'; '+occ['source_locator']+'; Word file/printed page '+str(PAGES[n])+'.\n\n'+kb.link(p,root/item['original'],'Original figure')+' · '+kb.link(p,root/f'domains/payments/assets/{SID}/word-render/page-{PAGES[n]:03d}.png','Complete Word-rendered page')+' · '+kb.link(p,fl,'Reusable flow')+'\n\n## Source reconstruction\n\n'
 if x.get('canonical'):meta['canonical_diagram']=x['canonical'];body+=kb.link(p,root/x['canonical'],'Reviewed canonical reconstruction')+'\n\n'
 else:
  code=x['code'];body+=fence+'mermaid\n'+code+fence+'\n\n';extract_workbooks.write(root,mmd/f'fig-{n:04d}.mmd',code,'job-000001')
 body+='## Participants and roles\n\n'+kb.table(['Occurrence','Literal label','Scoped roles'],[[i,label,'; '.join(kb.link(p,root/'shared/reference/participants'/f'participant-{SID}-{z}.md',z) for z in ss)] for i,(label,ss) in x['actors'].items()])+'\n## Relationships and activities\n\n'+kb.table(['Order','From','To','Literal connection'],[[j+1,*e] for j,e in enumerate(x['events'])])+'\n## Source qualifications\n\n'+'\n'.join('- '+z for z in notes)+'\n\n## Rendering and visual review\n\nPending actual parse/render and comparison.\n'
 extract_workbooks.write(root,p,kb.front(meta)+body,'job-000001')
 r={'figure_id':f'fig-{n:04d}','path':p.relative_to(root).as_posix(),'original':item['original'],'original_sha256':item['original_sha256'],'source_locator':occ['source_locator'],'word_file_page':PAGES[n],'flow':fl.relative_to(root).as_posix(),'flow_start':FLOW[n],'actors':x['actors'],'events':x['events'],'limitations':notes,'issue_ids':issues,'review_status':'needs-review','visual_review':{'status':'not-run'}}
 if x.get('canonical'):r.update(canonical_diagram=x['canonical'],disposition='deduplicated')
 else:r.update(mermaid=(mmd/f'fig-{n:04d}.mmd').relative_to(root).as_posix(),mermaid_sha256=hashlib.sha256(x['code'].encode()).hexdigest(),disposition='source-reconstruction')
 results.append(r)
kb.dump(root/'work/payments-clearing/models.json',{'source_id':SID,'source_sha256':src['sha256'],'models':results,'word_context_checked_pages':sorted(set(PAGES.values()))})
print(json.dumps({'figures':len(results),'reconstructions':sum('mermaid' in x for x in results),'deduplicated':sum('canonical_diagram' in x for x in results)}))
