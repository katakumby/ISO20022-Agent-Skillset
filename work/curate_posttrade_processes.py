from pathlib import Path
import json,sys,hashlib,re
from PIL import Image
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();s=next(s for s in kb.sources(root) if s['source_id']=='src-000180');base=root/s['set_path'];rec=json.loads((root/'work/documents/src-000180/records.json').read_text(encoding='utf-8'));prefix='participant-src-000180-';out=[]
def put(p,t):
 if p.exists() and p.read_text(encoding='utf-8')!=t:
  h=hashlib.sha256(p.read_bytes()).hexdigest()[:10];dest=root/'tracking/history/job-000001/manual-curation-2026-11-09'/p.relative_to(root);dest=dest.with_name(dest.stem+'-'+h+dest.suffix);dest.parent.mkdir(parents=True,exist_ok=True)
  if not dest.exists():dest.write_bytes(p.read_bytes())
 kb.put(p,t)
def participant(slug,title,definition,loc):
 p=root/'shared/reference/participants'/(prefix+slug+'.md')
 if p.exists():return
 m={'template':False,'document_kind':'participant','manual_curated':True,'review_status':'needs-review','domain':'securities','domains':['securities'],'participant_id':prefix+slug,'title':title,'source_labels':[title],'role_type':'source-scoped business actor','source_ids':['src-000180'],'source_editions':[s['source_edition']],'source_locations':[{'source_id':'src-000180','locator':loc}],'message_sets':['post-trade-matching'],'message_ids':[],'flows':[],'aliases':[],'limitations':['No identifier scheme or additional general definition is supplied at this locator. Context-specific role is not merged with similarly labelled roles elsewhere.']}
 put(p,kb.front(m)+'# '+title+'\n\n'+definition+'\n\nSource: '+kb.source_link(root,p,s)+'; '+loc+'.\n')
participant('party','Party','The central business actor in the Post Trade Matching role-context figure. Plain association rays connect it with eleven named business actors. The artwork does not establish inheritance or assert that one institution fills every role.','P114; Word rendered page10; fig-0002')
participant('financial-intermediary','Financial Intermediary','A business actor drawn at the bottom right of the role-context figure. A plain ray extends from near Party toward this actor, ending just short of its symbol as do several other source rays; no specific responsibility, direction or inheritance is inferred.','P114; Word rendered page10; fig-0002')
participant('affirmation-party','Affirmation Party','The exact business-actor label in the role-context figure, associated with Party. T7 uses the label Affirming Party; the label variation is exposed without asserting unsupported general equivalence.','P114; Word rendered page10; fig-0002; compare T7')
participant('trade-counterparty','Trade Counterparty','In the out-of-scope Market-Side Confirmation Process, the executing party seeks a counterparty willing to buy or sell the required securities and amount at a given price; the two counterparties exchange details for each agreed trade.','P126')
participant('settlement-agent','Settlement Agent','The scope illustration places this role in Clearing & Settlement, linked bidirectionally to Trade Matching and to (I)CSD. The illustration does not define additional responsibilities or a particular institution.','P87/P89; image1.emf; fig-0001')
participant('icsd-scope-actor','(I)CSD','The scope illustration labels this clearing/settlement actor (I)CSD and links it bidirectionally to Settlement Agent. No particular institution is identified.','P87/P89; image1.emf; fig-0001')
# Preserve complete source composite crops with rendered-page parent evidence.
for pg,box,fid in [(10,(0,420,1075,1010),'fig-0002'),(13,(0,450,1241,1030),'fig-0003')]:
 parent=root/'domains/securities/assets/src-000180/source-page-renders'/f'word-page-{pg:04d}.png';target=parent.parent/(fid+'-complete-crop.png');Image.open(parent).crop(box).save(target)

def add(fid,title,code,desc,slugs,flowstart=None,table=None,extra=''):
 fig=next(f for f in rec['figures'] if f['figure_id']==fid);dp=base/'diagrams/processes'/(fid+'.md');pids=[prefix+x for x in slugs];flow=next((base/'flows').glob('flow-src-000180-p'+str(flowstart)+'-*.md')) if flowstart else None
 if fig['images']:
  orig=root/fig['images'][0]['asset'];name=orig.name;preview=root/'domains/securities/assets/src-000180/derived-previews'/(name+'.png');preview=preview if preview.exists() else orig
 else:orig=root/'work/docx-render/src-000180/document.pdf';preview=root/'domains/securities/assets/src-000180/source-page-renders'/(fid+'-complete-crop.png')
 loc=' / '.join(fig['heading_path'])+'; '+fig['locator'];loc+=('; Word rendered page '+('10' if fid=='fig-0002' else '13')) if not fig['images'] else '; word/'+fig['images'][0]['target']
 limits=['Spatial layout is adapted to native Mermaid flowchart notation. Original artwork retains exact geometry and decorative actor icons; no additional business relationship is inferred from node proximity.']
 if fid>='fig-0007':limits+=['Unlabelled circles, diamonds, continuation lines and message endpoints are retained without adding action names. Solid gray and dashed blue connectors retain their source distinction; the source does not supply a full formal execution semantics for every disconnected marker.']
 m={'template':False,'document_kind':'diagram','manual_curated':True,'review_status':'needs-review','domain':'securities','diagram_id':fid,'title':title,'diagram_kind':'activity' if flowstart and fid>='fig-0007' else 'business-context','content_origin':'source-reconstruction','source_ids':['src-000180'],'source_editions':[s['source_edition']],'source_locations':[{'source_id':'src-000180','locator':loc}],'participants':pids,'flow_ids':[],'message_ids':[],'render_status':'not-run','visual_review':'not-run','limitations':limits}
 if flow:
  fm,fb=kb.metadata(flow);m['flow_ids']=[fm['flow_id']];fm.update(manual_curated=True,participants=sorted(set(fm.get('participants',[])+pids)))
  fb=fb.replace('Mermaid reconstruction and visual review are pending.','The dedicated source reconstruction and recorded visual checks are linked below.');fb+='\n## Curated process interpretation\n\n'+desc+'\n\n'+kb.link(flow,dp,'Complete source diagram reconstruction')+'. '+extra+'\n'
  fm['limitations']=[x for x in fm.get('limitations',[]) if x!='Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.'];fm['limitations'].append('Table review remains independent of source-diagram reconstruction review.');put(flow,kb.front(fm)+fb)
 text='# '+title+'\n\n## Source evidence\n\n'+kb.source_link(root,dp,s)+'; '+loc+'. '+kb.link(dp,orig,'Unchanged original figure or complete rendered document')+'.\n\n![Complete source figure]('+kb.rel(dp,preview)+')\n\n## Mermaid reconstruction\n\n```mermaid\n'+code+'```\n\n## Actors, activities and relationships\n\n'+desc+'\n\n'+extra+'\n\n'+kb.table(['Source-scoped participant','Canonical record'],[[x.replace('-',' '),kb.link(dp,root/'shared/reference/participants'/(prefix+x+'.md'),x.replace('-',' '))] for x in slugs])+'\n'
 if flow:text+='Reusable source flow: '+kb.link(dp,flow,fm['title'])+'. All narrative conditions and activity-table rows remain there.\n\n'
 if table:text+='Responsibilities and activities: '+kb.link(dp,base/'documents/src-000180/tables'/f'tbl-{table:04d}.md','Source table T'+str(table))+'.\n\n'
 if not fig['images']:text+='The crop is derived from the complete Word render, with the parent page retained. Word produced a STYLEREF header error outside these figure crops; it is a rendering limitation, not a source business claim.\n\n'
 text+='## Review evidence\n\nOriginal figure inspected; Mermaid rendering and output comparison pending.\n';put(dp,kb.front(m)+text);put(dp.with_suffix('.mmd'),code)
 for pid in pids:
  pp=root/'shared/reference/participants'/(pid+'.md');pm,pb=kb.metadata(pp);pm['manual_curated']=True
  if flow:pm['flows']=sorted(set(pm.get('flows',[])+[fm['flow_id']]))
  pb+='\nSource context: '+kb.link(pp,dp,title)+('. '+kb.link(pp,flow,'Reusable flow') if flow else '')+'.\n';put(pp,kb.front(pm)+pb)
 out.append({'diagram':dp.relative_to(root).as_posix(),'source_figure':fid,'original':orig.relative_to(root).as_posix(),'preview':preview.relative_to(root).as_posix(),'flow':flow.relative_to(root).as_posix() if flow else None,'participants':pids})

add('fig-0001','Post-trade communication scope','''flowchart TB
 subgraph Pre["Pre-trade"]
 IM["Investment Manager"] <-.-> BD["Broker/Dealer"]
 end
 subgraph Trade["Trade"]
 Spacer["No activity box drawn in source trade band"]
 end
 subgraph Post["Post-trade"]
 subgraph TM["Trade Matching"]
 TN["Trade Notification"]
 AL["Allocation"]
 MA["Matching"]
 CO["Confirmation"]
 EN["Enrichment"]
 AF["Affirmation"]
 SP["Settlement preparation"]
 RE["Reporting"]
 end
 end
 subgraph CS["Clearing & Settlement"]
 SA["Settlement Agent"] <--> CSD["(I)CSD"]
 end
 IM <--> TM
 BD <--> TM
 TM <--> SA
 classDef inscope fill:green,color:white;
 classDef other fill:#aaa,color:white;
 class TN,AL,MA,CO,AF inscope;
 class EN,SP,RE other;
 style Spacer fill:none,stroke:none,color:#666
 linkStyle 0,1,4 stroke:#999
 linkStyle 2,3 stroke:green
''','P87 explicitly states that green identifies scope. The five green Trade Matching activities are Trade Notification, Allocation, Matching, Confirmation and Affirmation. Enrichment, Settlement preparation and Reporting are gray. Investment Manager and Broker/Dealer are joined by a dotted bidirectional link; each connects bidirectionally to the Trade Matching boundary in green. Gray bidirectional links connect Trade Matching to Settlement Agent and Settlement Agent to (I)CSD. No internal ordering among the eight contained activity boxes is drawn. Four lifecycle bands are preserved; the explanatory empty-band label is explicitly a reconstruction cue, not a source activity.',['investment-manager','broker','settlement-agent','icsd-scope-actor'])
add('fig-0002','Post-trade business-actor context','''flowchart TB
 P["Party<br/>(Business Actor)"]
 IM["Investment Manager<br/>(Business Actor)"] --- P
 EX["Exchange<br/>(Business Actor)"] --- P
 EB["Executing Broker<br/>(Business Actor)"] --- P
 CSD["Central Securities Depository<br/>(Business Actor)"] --- P
 PB["Prime Broker<br/>(Business Actor)"] --- P
 CU["Custodian<br/>(Business Actor)"] --- P
 AP["Affirmation Party<br/>(Business Actor)"] --- P
 CP["Confirmation Party<br/>(Business Actor)"] --- P
 CCP["Central Counterparty<br/>(Business Actor)"] --- P
 CMU["Central Matching Utility<br/>(Business Actor)"] --- P
 FI["Financial Intermediary<br/>(Business Actor)"] --- P
''','Twelve business-actor symbols appear. Eleven plain association rays connect the central Party context with surrounding actors. Several rays stop short of their actor symbols, including the ray toward Financial Intermediary; the reconstruction retains that association with this endpoint-spacing qualification. There are no use-case ellipses, include/extend links, inheritance triangles or multiplicities in this figure. P111–113 distinguishes real-world business roles from functional participants and states that their relationship is many-to-many. T7/T8 provides the separate definitions and role mapping. The source label Affirmation Party is retained separately from the table label Affirming Party.',['party','investment-manager','exchange','broker-executing-broker','central-securities-depositories','prime-broker','custodian','affirmation-party','confirmation-party','central-counterparty','central-matching-utility-cmu','financial-intermediary'],table=8)
add('fig-0003','Trade lifecycle process overview','''flowchart TB
 subgraph OOS["Out Of scope"]
 O["Order Process"] --> M["Market-Side Confirmation Process"]
 end
 M --> N["Notification of Execution Process"]
 N --> D1{"Matching Process"}
 D1 -->|Allocation| A["Allocation Process"]
 A --> D2{"Matching Process"}
 D2 --> C["Confirmation/Affirmation Process"]
 D1 -->|"/No Allocation"| C
 style OOS fill:#fff,stroke:red,stroke-width:2px
''','The source begins with Order Process and Market-Side Confirmation Process above its red scope boundary, both explicitly out of scope. Notification of Execution leads to the first Matching Process decision. Its Allocation path passes through Allocation Process and a second Matching Process before Confirmation/Affirmation; its /No Allocation path goes directly to Confirmation/Affirmation. Two separately occurring matching diamonds are retained. P122 warns that further updates and diagrams would precede final publication; that source qualification is preserved. P125–129 defines the activity responsibilities: instructing party places the order and allocates blocks; executing party seeks the counterparty, reports execution and sends client confirmations; counterparties agree market-side details; matching can be central or local, with positive affirmation in some markets.',['instructing-party','executing-servicing-party','trade-counterparty','central-matching-utility-cmu'],flowstart=120)
kb.dump(root/'work/documents/src-000180/process-curation.json',out)
print('Three overview reconstructions authored')
