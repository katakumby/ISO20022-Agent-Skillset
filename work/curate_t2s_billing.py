from pathlib import Path
import sys,json,re,hashlib
from PIL import Image
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();sid='src-000347';s=next(x for x in kb.sources(root) if x['source_id']==sid);base=root/s['set_path'];rec=json.loads((root/'work/documents'/sid/'records.json').read_text(encoding='utf-8'));prefix='participant-'+sid+'-';records=[]
def put(p,t):
 if p.exists() and p.read_text(encoding='utf-8')!=t:
  h=hashlib.sha256(p.read_bytes()).hexdigest()[:10];old=root/'tracking/history/job-000001/manual-curation-2026-11-09'/p.relative_to(root);old=old.with_name(old.stem+'-'+h+old.suffix);old.parent.mkdir(parents=True,exist_ok=True)
  if not old.exists():old.write_bytes(p.read_bytes())
 kb.put(p,t)
def role(slug,title,definition,loc,actions):
 p=root/'shared/reference/participants'/(prefix+slug+'.md')
 if p.exists():return
 m={'template':False,'document_kind':'participant','manual_curated':True,'review_status':'needs-review','domain':'securities','domains':['securities'],'participant_id':prefix+slug,'title':title,'source_labels':[title],'role_type':'source-scoped operational participant','source_ids':[sid],'source_editions':[s['source_edition']],'source_locations':[{'source_id':sid,'locator':loc}],'message_sets':['t2s-billing'],'message_ids':[],'flows':[],'aliases':[],'limitations':['No identifier scheme is assigned to this role in the cited passage. Contextual functional-role correspondences do not identify a particular institution.']}
 put(p,kb.front(m)+'# '+title+'\n\n'+definition+'\n\n## Responsibilities and relationships\n\n'+actions+'\n\nSource '+kb.source_link(root,p,s)+'; '+loc+'.\n')
role('system-member','System Member','The billing-data requester and invoice/report recipient in the billing activities. P117 and P122 explicitly identify this participant with the Instructing Party within those flows.','T8; P117/image7/P119; P122/image8/P124','Requests cumulative or itemised data; handles errors and returned data; receives cumulative invoice or invoice cancellation. T8 allows inquiry of generated invoices regardless of cancelled/not-confirmed status; the Billing Reference (Invoice Number) distinct search criterion can ensure active confirmed data.')
role('system-transaction-administrator','System Transaction Administrator','The query activity participant identified with the executing party by P117.','P117; image7/P119; T10','Validates the request, checks permissions, searches billing data, extracts requested information and delivers cumulative or itemised data. Validation, permission or data-availability failure leads to error generation.')
role('settlement-infrastructure','Settlement Infrastructure','The billing report activity participant identified with the executing party by P122.','P122; image8/P124; T11','Checks billing event, generates invoice data, delivers and stores cumulative invoices, or generates/delivers invoice cancellation when invoice processing is cancelled.')
role('central-system','Central System','The system named in the formal billing-process definition and trigger. The source does not separately define its identity relative to the activity participant labels.','T8 rows2-4','Sends invoices, cancellation status, consumption data, or query responses; retains invoice data and generates corresponding-period billing events. The record remains distinct from the separately defined Central Database System.')
role('operator','Operator','The narrative participant that has submitted an invoice cancellation request before the cancellation-status report is generated.','P166-P168','Submits the prior cancellation request; cancellation status is reported after its processing. The source does not draw this participant in the typical report sequence or identify the cancellation-request message.')
for n,pg,box in [(9,14,(105,430,905,770)),(10,15,(105,245,905,580)),(11,16,(105,220,905,555))]:
 src=root/'domains/securities/assets'/sid/'source-page-renders'/f'word-page-{pg}.png';Image.open(src).crop(box).save(src.parent/f'fig-{n:04d}-complete-crop.png')
spec=[]
def add(n,title,code,desc,slugs,flowstart=None,table=None,message_ids=[],issue=False,narrative=None):spec.append(dict(n=n,title=title,code=code,desc=desc,slugs=slugs,flowstart=flowstart,table=table,message_ids=message_ids,issue=issue,narrative=narrative))
add(1,'Billing business roles and functional participants','''flowchart LR
 DB["Central Database System"] --> I["Instructing Party"]
 CM["Collateral Management System"] --> I
 N["NationalCentralBank"] --> I
 P["Payment Bank"] --> I
 C["Central Securities Depository"] --> I
 M["Market Infrastructure"] --> E["Executing/Servicing Party"]
 linkStyle default stroke:blue
''','Five blue directed associations point from Central Database System, Collateral Management System, NationalCentralBank, Payment Bank and Central Securities Depository to Instructing Party. Market Infrastructure points to Executing/Servicing Party. These are source role associations, not message-exchange arrows. T5 defines these functional participants. T7 instead uses Account Servicer and Account Owner columns, omits Central Database System and does not establish equivalence to T5. Both vocabularies remain separate under issue-000038.',['central-database-system','collateral-management-system','national-central-bank','payment-bank','central-securities-depository-csd','market-infrastructure','instructing-party','executing-servicing-party','account-servicer','account-owner'],table=7,issue=True)
add(2,'Billing process overview','''flowchart TB
 S((" ")) --> Q("Query Billing<br/>information")
 S --> R("Billing Report")
 Q -.-> R
 Q --> E(((" ")))
 R --> E
 style S fill:#0070b5,stroke:#0070b5
 style Q fill:#9bbb59
 style R fill:#9bbb59
''','One source start point has separate arrows to Query Billing information and Billing Report. A dotted directed relationship goes from the query to the report. Both process boxes lead to a shared end point. The overview does not draw an exclusive-choice diamond or a parallel bar. T8 provides the formal trigger, preconditions and postconditions.',['system-member','central-system','instructing-party','executing-servicing-party'],110,8,['camt.076.001.01','camt.077.001.01'])
add(7,'Query billing information activity','''flowchart TB
 subgraph I["System Member"]
 S((" ")) --> Q("Process<br/>RequestBillingData")
 H("Process<br/>HandleError") --> End(((" ")))
 D("ProcessBillingData") --> End
 J[" "] --> D
 end
 subgraph E["SystemTransaction<br/>Administrator"]
 V("Process<br/>Validate") --> VD{"Validation<br/>successful?"}
 VD -->|No| Err("Process<br/>GenerateError")
 VD -->|Yes| C("Process<br/>CheckPermission")
 C --> CD{"PermissionCheck<br/>successful?"}
 CD -->|No| Err
 CD -->|Yes| Search("Process<br/>SearchForData")
 Search --> Available{"Billing Data<br/>available?"}
 Available -->|No| Err
 Available -->|Yes| Extract("Process<br/>ExtractDataForQuery")
 Extract --> Type{"Cumulative<br/>or Itemised<br/>Data?"}
 Type -->|Itemised| Item("Process<br/>DeliverItemisedBillingData")
 Type -->|Cumulative| Cumu("Process<br/>DeliverCumulativeBilling<br/>Data")
 end
 Q --> V
 Err --> H
 Item --> J
 Cumu --> J
 style J fill:black,stroke:black
 style S fill:#4678bb,stroke:#4678bb
''','System Member starts by requesting billing data. System Transaction Administrator checks validation, permission and availability in sequence; any No branch generates an error, returned for handling before termination. All Yes branches reach extraction and the cumulative/itemised choice. The selected delivery path crosses the source black bar before System Member processes the data and reaches the shared end. P117 maps System Member to Instructing Party and System Transaction Administrator to executing party. T10 additionally checks new/already-handled occurrence and requires REJECTED with errors/reasons when validation fails. The bar is preserved as drawn; the mutually exclusive data-type branches are not silently converted into a requirement for both reports.',['system-member','system-transaction-administrator','instructing-party','executing-servicing-party'],116,10,['camt.076.001.01','camt.077.001.01'])
add(8,'Billing report activity','''flowchart TB
 subgraph I["System Member"]
 R("Process<br/>ReceiveCumulativeInvoice") --> IE(((" ")))
 RC("Process<br/>ReceiveInvoiceCancellation") --> IE
 end
 subgraph E["Settlement<br/>Infrastructure"]
 S((" ")) --> Check("Process<br/>CheckEvent")
 Check --> Event{"Event<br/>reached?"}
 Event -->|No| E1(((" ")))
 Event -->|Yes| Generate("Process<br/>GenerateInvoiceData")
 Generate --> Cancel{"Invoice<br/>processing<br/>cancelled?"}
 Cancel -->|No| Fork[" "]
 Fork --> Deliver("Process<br/>DeliverCumulativeInvoice")
 Fork --> Store("Process<br/>StoreBillingData")
 Store --> E2(((" ")))
 Cancel -->|Yes| GC("Process<br/>GenerateInvoiceCancellation")
 GC --> DC("Process<br/>DeliverInvoiceCancellation")
 end
 Deliver --> R
 DC --> RC
 style Fork fill:black,stroke:black
 style S fill:#4678bb,stroke:#4678bb
''','Settlement Infrastructure checks whether the event has been reached. No ends locally; Yes generates invoice data. If invoice processing is not cancelled, the source parallel bar initiates cumulative-invoice delivery and billing-data storage; storage ends locally, while System Member receives the invoice. If cancelled, cancellation is generated and delivered to System Member. Both receipt paths lead to its shared end. P122 explicitly maps Settlement Infrastructure to executing party and System Member to Instructing Party. T11 says periodic processing returns invoices to subscribed instructing parties. P161-P168 separately describes official invoice/NCB-only consumption reports at the business-day event and cancellation-status reports after processing an operator cancellation request.',['system-member','settlement-infrastructure','instructing-party','executing-servicing-party','operator','national-central-bank'],121,11,['camt.077.001.01'])
for n,title,p,status,start,stop in [(9,'Successful billing information query',129,'COMPLETED',130,140),(10,'Rejected billing information query',142,'REJECTED',143,153)]:
 code='sequenceDiagram\n participant I as Instructing Party\n participant E as Executing/Servicing Party\n Note over I,E: Query Process\n I->>E: Cumulative/Itemised Billing Report Request (camt.076)\n E->>I: Billing Report (camt.077): '+status+'\n'
 desc='The Instructing Party requests cumulative or itemised billing data, specifying invoice, period and (for itemised queries) securities account, cash account or participant. '+('The Executing/Servicing Party returns the requested information and COMPLETED status.' if n==9 else 'The Executing/Servicing Party returns REJECTED and the business or operational error causing the rejection. The report is not a settlement reversal or invoice-cancellation instruction.')
 add(n,title,code,desc,['instructing-party','executing-servicing-party','system-member','system-transaction-administrator'],p,None,['camt.076.001.01','camt.077.001.01'],narrative=(start,stop))
add(11,'Billing report push sequence','''sequenceDiagram
 participant I as Instructing Party
 participant E as Executing/Servicing Party
 Note over I,E: Report Process
 E->>I: Invoice / Consumption Data / Cancellation Report (camt.077)
''','Executing/Servicing Party sends one depicted billing report to Instructing Party. Official invoice and consumption data (for NCBs only) are communicated when the specific business-day event is reached. Invoice cancellation status is communicated after processing a cancellation request previously submitted by the operator. The operator and its preceding request are narrative context, intentionally absent from this one-arrow report illustration; no cancellation-request message identifier is invented.',['instructing-party','executing-servicing-party','system-member','settlement-infrastructure','operator','national-central-bank'],156,None,['camt.077.001.01'],narrative=(157,168))
for x in spec:
 n=x['n'];fid=f'fig-{n:04d}';fig=next(f for f in rec['figures'] if f['figure_id']==fid);p=base/'diagrams/curated'/f'{fid}.md';flow=next((base/'flows').glob(f"flow-{sid}-p{x['flowstart']}-*.md")) if x['flowstart'] else None;original=root/fig['images'][0]['asset'];preview=original
 if n==1:preview=root/'domains/securities/assets'/sid/'derived-previews/image1.emf.png'
 if n>=9:original=root/'work/docx-render'/sid/'document.pdf';preview=root/'domains/securities/assets'/sid/'source-page-renders'/f'{fid}-complete-crop.png'
 loc=' / '.join(fig['heading_path'])+'; '+fig['locator']+('; Word rendered file page '+str(n+5) if n>=9 else '; word/'+fig['images'][0]['target']);pids=[prefix+slug for slug in x['slugs']]
 m={'template':False,'document_kind':'diagram','manual_curated':True,'review_status':'needs-review','domain':'securities','diagram_id':fid,'title':x['title'],'diagram_kind':'sequence' if n>=9 else 'activity' if n in [2,7,8] else 'participant-context','content_origin':'source-reconstruction','source_ids':[sid],'source_editions':[s['source_edition']],'source_locations':[{'source_id':sid,'locator':loc}],'participants':pids,'flow_ids':[],'message_ids':x['message_ids'],'message_sets':['t2s-billing'],'render_status':'not-run','visual_review':'not-run','issue_ids':['issue-000038'] if x['issue'] else [],'limitations':['Spatial layout and decorative institution icons are adapted; labels, direction, source decisions and bars remain explicit. Institution pictograms do not establish institutional identity.']}
 if flow:fm,fb=kb.metadata(flow);m['flow_ids']=[fm['flow_id']]
 body='# '+x['title']+'\n\n## Source evidence\n\n'+kb.source_link(root,p,s)+'; '+loc+'. '+kb.link(p,original,'Unchanged original asset or complete source render')+'.\n\n![Complete source figure]('+kb.rel(p,preview)+')\n\n## Mermaid reconstruction\n\n```mermaid\n'+x['code']+'```\n\n## Participants, responsibilities and alternatives\n\n'+x['desc']+'\n\n'+kb.table(['Source-scoped role','Canonical reference'],[[slug.replace('-',' '),kb.link(p,root/'shared/reference/participants'/(prefix+slug+'.md'),slug.replace('-',' '))] for slug in x['slugs']])+'\n'
 if x['table']:body+='Full source table: '+kb.link(p,base/'documents'/sid/'tables'/f"tbl-{x['table']:04d}.md",'T'+str(x['table']))+'.\n\n'
 if x['message_ids']:body+='## Exact message evidence\n\nThe supplied companion MDR Part2 src-000346 defines BillingReportRequestV01 at file pages4-10 and BillingReportV01 at pages11-111. P46 explicitly directs variant/version lookup to Part2.\n\n'+kb.table(['Exact supplied definition','Canonical reference'],[[mid,kb.link(p,root/'domains/securities/reference/messages'/mid/'index.md',mid)] for mid in x['message_ids']])+'\n'
 if flow:body+='Reusable flow: '+kb.link(p,flow,fm['title'])+'.\n\n'
 body+='## Review evidence\n\nComplete source artwork inspected; Mermaid render and visual comparison pending.\n';put(p,kb.front(m)+body);put(p.with_suffix('.mmd'),x['code'])
 if flow:
  fm.update(manual_curated=True,document_kind='business-flow',participants=sorted(set(fm.get('participants',[])+pids)),message_ids=x['message_ids'],message_families=sorted(set('.'.join(mid.split('.')[:2]) for mid in x['message_ids'])));fm['limitations']=[v for v in fm.get('limitations',[]) if not v.startswith('Source-delimited draft')];fm['limitations'].append('Flow interpretation checked against its linked source diagram; table review is recorded separately.')
  fb=fb.replace('Mermaid reconstruction and visual review are pending.','Dedicated source reconstruction and actual review evidence are linked below.').replace('No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.','The curated scoped participant links below resolve diagram and narrative roles for this flow.')
  fb+='\n## Curated source process\n\n'+x['desc']+'\n\n'+kb.link(flow,p,'Complete source diagram reconstruction')+'.\n'
  if x['narrative']:
   lo,hi=x['narrative'];fb+='\n### Complete adjacent scenario narrative\n\n'+'\n\n'.join('**'+q['paragraph_id']+'** '+q['text'] for q in rec['paragraphs'] if lo<=int(q['paragraph_id'][1:])<=hi and q['text'] and q['paragraph_id'] not in ['P132','P145','P158'])+'\n'
  fb+='\n'+kb.table(['Participant','Source-specific responsibility'],[[kb.link(flow,root/'shared/reference/participants'/(prefix+slug+'.md'),slug.replace('-',' ')),'Use the ordered source activities and narrative above; mapped functional roles are explicit in P117/P122 where applicable.'] for slug in x['slugs']])+'\n';put(flow,kb.front(fm)+fb)
 for pid in pids:
  pp=root/'shared/reference/participants'/(pid+'.md');pm,pb=kb.metadata(pp);pm['manual_curated']=True
  if flow:pm['flows']=sorted(set(pm.get('flows',[])+[fm['flow_id']]))
  pm['message_ids']=sorted(set(pm.get('message_ids',[])+x['message_ids']));pb+='\nBilling source context: '+kb.link(pp,p,x['title'])+('. '+kb.link(pp,flow,'Reusable flow') if flow else '')+'.'+(' Source role-matrix inconsistency remains open under issue-000038.' if x['issue'] else '')+'\n';put(pp,kb.front(pm)+pb)
 records.append({'diagram':p.relative_to(root).as_posix(),'source_figure':fid,'original':original.relative_to(root).as_posix(),'preview':preview.relative_to(root).as_posix(),'issue_ids':m['issue_ids'],'flow':flow.relative_to(root).as_posix() if flow else None})
kb.dump(root/'work/documents'/sid/'curated-figures.json',records);print('Seven T2S Billing figures authored with scoped participants and flows')
