from pathlib import Path
import sys,json,re,hashlib
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();sid='src-000350';s=next(x for x in kb.sources(root) if x['source_id']==sid);base=root/s['set_path'];rec=json.loads((root/'work/documents'/sid/'records.json').read_text(encoding='utf-8'));defs=json.loads((root/'work/documents/src-000351/message-definitions.json').read_text(encoding='utf-8'));prefix='participant-'+sid+'-';out=[]
def put(p,t):
 if p.exists() and p.read_text(encoding='utf-8')!=t:
  h=hashlib.sha256(p.read_bytes()).hexdigest()[:10];old=root/'tracking/history/job-000001/manual-curation-2026-11-09'/p.relative_to(root);old=old.with_name(old.stem+'-'+h+old.suffix);old.parent.mkdir(parents=True,exist_ok=True)
  if not old.exists():old.write_bytes(p.read_bytes())
 kb.put(p,t)
def role(slug,title,definition,loc):
 p=root/'shared/reference/participants'/(prefix+slug+'.md')
 if p.exists():return
 m={'template':False,'document_kind':'participant','manual_curated':True,'review_status':'needs-review','domain':'securities','domains':['securities'],'participant_id':prefix+slug,'title':title,'source_labels':[title],'role_type':'source-scoped functional participant','source_ids':[sid],'source_editions':[s['source_edition']],'source_locations':[{'source_id':sid,'locator':loc}],'message_sets':[s['set_slug']],'message_ids':[],'flows':[],'aliases':[],'limitations':['No identifier scheme or general institution equivalence is stated in this passage.']};put(p,kb.front(m)+'# '+title+'\n\n'+definition+'\n\nSource '+kb.source_link(root,p,s)+'; '+loc+'.\n')
role('recipient-party','Recipient Party','T10 names this functional recipient of the automatically generated Cash Account Activity Advice. A standing instruction must be in place at the Executing/Servicing Party. The activity and sequence use Instructing Party for the receiving lane; the two contextual labels are linked without assuming equivalence outside this flow.','T10 rows2-5; P95/P164; image8/P137 and image10/P162')
roles=['instructing-party','executing-servicing-party'];spec=[]
def add(n,title,code,desc,slugs=roles,flows=[],tables=[],families=[],issues=[],paragraphs=None):spec.append(dict(n=n,title=title,code=code,desc=desc,slugs=slugs,flows=flows,tables=tables,families=families,issues=issues,paragraphs=paragraphs))
add(1,'Cash account business-role context','''classDiagram
 class I["Instructing Party"]
 class E["Executing/Servicing Party"]
 class DB["Central Database System"]
 class CM["Collateral Management System"]
 class N["National Central Bank"]
 class P["Payment Bank"]
 class C["Central Securities Depository"]
 class M["Market Infrastructure"]
 I <|-- DB
 I <|-- CM
 I <|-- N
 I <|-- P
 I <|-- C
 E <|-- M
''','Five hollow-triangle connections point toward Instructing Party from Central Database System, Collateral Management System, National Central Bank, Payment Bank and Central Securities Depository. Market Infrastructure points with the same hollow-triangle notation toward Executing/Servicing Party. Native class notation preserves the source arrowheads; it does not turn these contextual functional roles into institution identities or a validated ontology. T5 defines functional participants; T7 instead maps Account Servicer/Owner columns and omits Central Database System. Both source vocabularies and the unresolved correspondence are retained under issue-000038.',slugs=roles+['central-database-system','collateral-management-system','national-central-bank','payment-bank','central-securities-depository-csd','market-infrastructure','account-servicer','account-owner'],tables=[5,6,7],issues=['issue-000038'])
add(2,'Cash account query, report and advice overview','''flowchart TB
 S((" ")) --> Q("Account Query List")
 Q --> R("Account List Report")
 R --> End(((" ")))
 S --> A("Cash Account Activity<br/>Advice")
 A --> End
 S --> TQ("Cash Account Audit<br/>Trail Query")
 TQ --> TR("Cash Account Audit<br/>Trail Report")
 TR --> End
 style S fill:#31879b,stroke:black
 classDef activity fill:#d7e4bd,stroke:black
 class Q,R,A,TQ,TR activity
''','One start symbol leads to three paths: Account Query List followed by Account List Report; unsolicited Cash Account Activity Advice; and Cash Account Audit Trail Query followed by Cash Account Audit Trail Report. All converge at a common end. No exclusive-choice diamond or parallel bar is drawn. T8/T9 require both parties to know the query type and define report content as all retrieved records. T10 requires a standing instruction for automatically produced activity advice and names acknowledgement of sending as postcondition; this does not add an acknowledgement arrow to the artwork.',slugs=roles+['recipient-party'],flows=[123,124,125],tables=[8,9,10],families=['acmt.025','acmt.026','reda.038','reda.039','reda.040'])
query='''flowchart TB
 subgraph I["Instructing Party"]
 Instruction("Instruction")
 Monitor("Monitor")
 end
 subgraph E["Executing Party"]
 Process("Process Query") --> Response("Response")
 end
 Instruction --> Process
 Response --> Monitor
'''
add(7,'Cash account query/response activity reused in two processes',query,'Instructing Party Instruction goes to Executing Party Process Query, followed by Response returning to Instructing Party Monitor. This exact source media is reused at P132 for Account Query List and P141 for Cash Account Audit Trail Query/Response. T12 and T14 retain separate business scope while sharing these four actions. Excessive processing time or inability to provide a positive response causes an error with code and explanation; those narrative alternatives are not drawn as separate branches here. No extra decision is invented.',flows=[130,140],tables=[12,14],families=['acmt.025','acmt.026','reda.039','reda.040'])
add(8,'Cash account activity advice activity','''flowchart TB
 subgraph I["Instructing Party"]
 Instruction("Instruction")
 Monitor("Monitor")
 end
 subgraph E["Executing Party"]
 Process("Process Statement") --> Reporting("Reporting")
 end
 Instruction --> Process
 Reporting --> Monitor
''','The source activity includes an Instruction arrow to Process Statement, then Reporting back to Monitor. T13 explicitly says a request to run a statement is outside the current process and NO message will be created for it. T10 supplies the actual standing-instruction precondition and automatic trigger, and P95/P164 says advice is pushed unilaterally to subscribing parties. The diagram is reconstructed as drawn while that scope exclusion remains explicit; no request message is invented.',slugs=roles+['recipient-party'],flows=[135],tables=[10,13],families=['reda.038'])
for n,title,fp,q,r,pra in [(10,'Account query/list sequence',148,'AccountQueryList (acmt.025)','AccountListReport (acmt.026)',(153,159)),(12,'Cash account audit-trail query/response sequence',166,'CashAccountAuditTrailQuery (reda.039)','CashAccountAuditTrailReport (reda.040)',(170,176))]:
 code='sequenceDiagram\n participant I as Instructing Party\n participant E as Executing/Servicing Party\n Note over I,E: '+('Account Query/List Process' if n==10 else 'Cash Account Audit Trail Query/Response Process')+'\n I->>E: '+q+'\n E-->>I: '+r+': ERROR\n E->>I: '+r+'\n';add(n,title,code,'The source displays a query from Instructing Party to Executing/Servicing Party, a dashed ERROR response and a solid normal response in that vertical order. The narrative distinguishes negative and successful scenarios: excessive processing time, wrong criteria combination or no result may produce the error. Both response arrows are preserved as alternatives, not a requirement to send an error followed by a normal result. The audit-trail process retrieves a complete audit trail for the specified cash account; the account-query process returns data meeting its query criteria.',flows=[fp],families=['acmt.025','acmt.026'] if n==10 else ['reda.039','reda.040'],paragraphs=pra)
add(11,'Cash account activity advice push sequence','''sequenceDiagram
 participant I as Instructing Party
 participant E as Executing/Servicing Party
 Note over I,E: Cash Account Activity Advice Process
 E->>I: CashAccountActivityAdvice (reda.038)
''','Executing/Servicing Party unilaterally sends CashAccountActivityAdvice to Instructing Party. P164 specifies changes to cash-account reference data during the business day. P91-P95 includes creation, modification and deletion, with advice elements varying by requestor scope and delivery to subscribers. Recipient Party in T10 is also linked as a contextual narrative role; no extra sender or request exchange is added.',slugs=roles+['recipient-party'],flows=[161],tables=[10,13],families=['reda.038'],paragraphs=(163,164))
for x in spec:
 n=x['n'];fid=f'fig-{n:04d}';fig=next(f for f in rec['figures'] if f['figure_id']==fid);p=base/'diagrams/curated'/f'{fid}.md';orig=root/fig['images'][0]['asset'];preview=root/'domains/securities/assets'/sid/'derived-previews'/(orig.name+'.png');pids=[prefix+z for z in x['slugs']];dlist=[d for d in defs if '.'.join(d['message_id'].split('.')[:2]) in x['families']];mids=[d['message_id'] for d in dlist];flowpaths=[next((base/'flows').glob(f'flow-{sid}-p{start}-*.md')) for start in x['flows']];loc=' / '.join(fig['heading_path'])+'; '+fig['locator']+'; word/'+fig['images'][0]['target'];locations=[{'source_id':sid,'locator':loc}]
 if n==7:locations.append({'source_id':sid,'locator':'Cash Account Audit Trail Query/Response process; P141; fig-0009; same word/media/image7.emf bytes'})
 locations += [{'source_id':'src-000351','locator':d['title']+'; file pages'+str(d['start_page'])+'-'+str(d['end_page'])} for d in dlist]
 m={'template':False,'document_kind':'diagram','manual_curated':True,'review_status':'needs-review','domain':'securities','diagram_id':fid,'title':x['title'],'diagram_kind':'class' if n==1 else 'sequence' if n>=10 else 'activity','content_origin':'source-reconstruction','source_ids':[sid]+(['src-000351'] if mids else []),'source_editions':[s['source_edition']],'source_locations':locations,'participants':pids,'flow_ids':[kb.metadata(fp)[0]['flow_id'] for fp in flowpaths],'message_ids':mids,'message_sets':[s['set_slug']],'render_status':'not-run','visual_review':'not-run','issue_ids':x['issues'],'limitations':['Visible artwork reconstructed with native Mermaid notation; exact decorative symbols and source geometry retained in original. Native embedded Visio originals/static inspection are preserved separately; hidden content is not certified by preview review.']}
 body='# '+x['title']+'\n\n## Source evidence\n\n'+kb.source_link(root,p,s)+'; '+loc+'. '+kb.link(p,orig,'Unchanged original figure')+'.\n\n![Complete source figure]('+kb.rel(p,preview)+')\n\n## Mermaid reconstruction\n\n```mermaid\n'+x['code']+'```\n\n## Roles, activities and alternatives\n\n'+x['desc']+'\n\n'+kb.table(['Source-scoped role','Canonical reference'],[[z.replace('-',' '),kb.link(p,root/'shared/reference/participants'/(prefix+z+'.md'),z.replace('-',' '))] for z in x['slugs']])+'\n'
 if x['tables']:body+='Source responsibilities/conditions: '+', '.join(kb.link(p,base/'documents'/sid/'tables'/f'tbl-{t:04d}.md','T'+str(t)) for t in x['tables'])+'.\n\n'
 if dlist:body+='## Exact message evidence\n\n'+kb.table(['Source family','Exact supplied definition','Companion MDR Part2 locator'],[['.'.join(d['message_id'].split('.')[:2]),kb.link(p,root/'domains/securities/reference/messages'/d['message_id']/'index.md',d['message_id']),d['source_id']+'; '+d['title']+'; file pages'+str(d['start_page'])+'-'+str(d['end_page'])] for d in dlist])+'\n'
 body+='Reusable flows: '+', '.join(kb.link(p,fp,kb.metadata(fp)[0]['title']) for fp in flowpaths)+'.\n\n' if flowpaths else ''
 if n==7:body+='The same unchanged image7.emf occurs twice (P132/fig-0007 and P141/fig-0009). It is reconstructed once; both distinct flow records and source occurrences link here.\n\n'
 body+='## Review evidence\n\nComplete source artwork inspected; Mermaid rendering and visual comparison pending.\n';put(p,kb.front(m)+body);put(p.with_suffix('.mmd'),x['code'])
 for fp in flowpaths:
  fm,fb=kb.metadata(fp);fm.update(manual_curated=True,document_kind='business-flow',participants=sorted(set(fm.get('participants',[])+pids)),message_ids=mids,message_families=x['families']);fm['limitations']=[v for v in fm.get('limitations',[]) if not v.startswith('Source-delimited draft')];fm['limitations'].append('Diagram review and table-cell review have separate evidence.');fb=fb.replace('Mermaid reconstruction and visual review are pending.','A canonical source reconstruction and actual review evidence are linked below.');fb+='\n## Curated source flow\n\n'+x['desc']+'\n\n'+kb.link(fp,p,'Complete source diagram')+'.\n'
  if x['paragraphs']:
   lo,hi=x['paragraphs'];fb+='\n### Adjacent source narrative\n\n'+'\n\n'.join('**'+q['paragraph_id']+'** '+q['text'] for q in rec['paragraphs'] if lo<=int(q['paragraph_id'][1:])<=hi and q['text'])+'\n'
  fb+='\nScoped participants: '+', '.join(kb.link(fp,root/'shared/reference/participants'/(pid+'.md'),pid.removeprefix(prefix).replace('-',' ')) for pid in pids)+'.\n';put(fp,kb.front(fm)+fb)
 for pid in pids:
  pp=root/'shared/reference/participants'/(pid+'.md');pm,pb=kb.metadata(pp);pm.update(manual_curated=True,flows=sorted(set(pm.get('flows',[])+m['flow_ids'])),message_ids=sorted(set(pm.get('message_ids',[])+mids)));pb+='\nCash-account source context: '+kb.link(pp,p,x['title'])+'. '+', '.join(kb.link(pp,fp,'flow '+kb.metadata(fp)[0]['title']) for fp in flowpaths)+'.\n';put(pp,kb.front(pm)+pb)
 out.append({'diagram':p.relative_to(root).as_posix(),'source_figure':fid,'source_occurrences':[fid]+(['fig-0009'] if n==7 else []),'original':orig.relative_to(root).as_posix(),'preview':preview.relative_to(root).as_posix(),'issue_ids':x['issues']})
kb.dump(root/'work/documents'/sid/'curated-figures.json',out);print('Seven canonical diagrams for eight substantive source occurrences')
