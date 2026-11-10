from pathlib import Path
import sys,json,re,hashlib
sys.path.insert(0,'tools');import kb
root=Path('.').resolve();sid='src-000004';s=next(x for x in kb.sources(root) if x['source_id']==sid);base=root/s['set_path'];rec=json.loads((root/'work/documents'/sid/'records.json').read_text(encoding='utf-8'));defs=json.loads((root/'work/documents/src-000005/message-definitions.json').read_text(encoding='utf-8'));prefix='participant-'+sid+'-';out=[]
seed=Path('work/curate_t2s_cashaccount.py').read_text(encoding='utf-8-sig');exec(seed[seed.index('def put('):seed.index("role('recipient-party'")].replace("'securities'","'payments'"))
role('initiating-party','Initiating Party','The party receiving payment-transaction status from the first or forwarding agent throughout the payment lifecycle. It is named in the process diagram and narrative, although absent from the four formal participant rows. Positive/negative status does not establish an exact status-message version.','P100/P110; T12; Word11-12')
role('first-agent','First Agent','The first agent gives payment status to the Initiating Party and can investigate the transaction through the payment chain. This is a contextual position in the chain, not a named institution.','P110; T12; Word12')
role('final-agent','Final Agent','The final agent registers the payment in the creditor account; the source describes conveying that status through preceding agents or investigation from the first/forwarding agent.','P110; Word12')
roles=['account-owner','account-servicer'];spec=[]
def add(n,title,code,desc,slugs=roles,flows=[],tables=[],families=[],issues=[],paragraphs=None,kind='activity'):spec.append(dict(n=n,title=title,code=code,desc=desc,slugs=slugs,flows=flows,tables=tables,families=families,issues=issues,paragraphs=paragraphs,kind=kind))
add(1,'Bank-to-customer roles and contextual generalisations','''classDiagram
 class O["AccountOwner"]
 class S["AccountServicer"]
 class C["Creditor"]
 class D["Debtor"]
 class CA["CreditorAgent"]
 class DA["DebtorAgent"]
 class R["Recipient"]
 class F["ForwardingAgent"]
 O <|-- C
 O <|-- D
 O <|-- CA
 O <|-- DA
 S <|-- CA
 S <|-- DA
''','All eight source actors carry the BusinessActor stereotype. Six hollow-triangle connectors terminate at AccountOwner or AccountServicer: Creditor and Debtor connect to AccountOwner; each agent connects to both functional roles. Recipient and ForwardingAgent have no connector in the artwork. Class generalisation syntax preserves these arrowheads while replacing actor icons with boxes. T8 is a separate mapping: Creditor, Debtor and System Member map to Account Owner; Creditor Agent, Debtor Agent and Market Infrastructure map to Account Servicer. Its narrower entries do not erase the diagram or assert that one institution always plays the same role. T6 defines Recipient by authorisation and Forwarding Agent by routing responsibility.',slugs=roles+['creditor','debtor','creditor-agent','debtor-agent','recipient','forwarding-agent','market-infrastructure','system-member'],tables=[6,7,8],kind='class')
add(2,'Reporting business-process actor overview','''usecase-beta
 actor D as "Debtor"
 actor DA as "DebtorAgent"
 actor CA as "CreditorAgent"
 actor C as "Creditor"
 actor I as "InitiatingParty"
 usecase R as "Report"
 usecase REC as "Reconcile"
 usecase TX as "Report on payment transaction"
 usecase ST as "Report on payment transaction status"
 D -- R
 DA -- R
 CA -- R
 C -- R
 R -- REC
 R -- TX
 R -- ST
 ST -- I
''','The source has five BusinessActor figures and four BusinessProcess ovals, connected by undirected plain lines. Actor labels carry the source namespace note from DICO_BusinessActorsAndRoles. There is no drawn boundary, inheritance, include or extend arrow. Native use-case notation retains that actor/process topology. T9-T12 and P102-P110 supply the four process definitions, triggers and conditions; status-chain roles First Agent and Final Agent are narrative participants absent from this overview. The generic status process has no specified exact message and is not assigned a camt reporting definition.',slugs=roles+['debtor','debtor-agent','creditor','creditor-agent','initiating-party','forwarding-agent','first-agent','final-agent'],flows=[101,104,107,109],tables=[9,10,11,12],kind='usecase')
add(7,'Cash positioning across internal systems and account servicer','''flowchart TB
 subgraph T["TreasurySystem"]
 Forecast("Forecast transactions")
 end
 subgraph L["LiquiditySystem"]
 Collect("Collect available funds for funding") --> Funding("Provide funding final amount")
 end
 subgraph R["ReconciliationSystem"]
 Reconciled("Provide today's reconciled balance")
 end
 subgraph P["PositionSystem"]
 Prior("Provide prior position")
 end
 subgraph E["CashPositionEvaluationSystem"]
 Start((" ")) --> Consolidate("Consolidate data") --> Adjust("Adjust prior position to actual") --> New("Set new positions") --> Updated("Provide updated balance info")
 Close("Close balance positions") --> End(((" ")))
 end
 subgraph A["AccountServicer"]
 Balance("Provide balance info")
 Tx("Provide transaction info")
 end
 Forecast --> Consolidate
 Reconciled --> Consolidate
 Prior --> Consolidate
 Balance --> Consolidate
 Tx --> Consolidate
 Updated --> Collect
 Funding --> Close
''','Six lanes and every source information/control arrow are retained. The evaluation system combines five input streams, adjusts positions, provides updated balances to liquidity collection, receives the funding final amount and closes positions. T14 specifies ledger, available and forward balances; intraday transaction reporting may include balances although intraday reconciliation usually is not done. Forecasts may repeat. Closure occurs when cash activity ceases or market close removes funding/investment options. The two literal Cash Position Evaluation Position initiator cells differ from the System lane and other rows; both labels remain scoped under issue-000060, without an unsupported alias merge.',slugs=roles+['treasury-system','liquidity-system','reconciliation-system','position-system','cash-position-evaluation-system','cash-position-evaluation-position'],flows=[115],tables=[14],issues=['issue-000060'])
add(8,'Optional notifications to the account owner','''flowchart TB
 subgraph O["AccountOwner"]
 Receive("Receive Notification") --> End(((" ")))
 end
 subgraph S["AccountServicer"]
 Start((" ")) --> Process("Process transaction") --> Book("Book cash movement") --> Settle("Interbank clearing and settlement")
 Process --> N1("Send notification 1")
 Book --> N2("Send notification2")
 Settle --> N3("Send notification3")
 end
 N1 --> Receive
 N2 --> Receive
 N3 --> Receive
''','Each of the three processing stages can notify the Account Owner. T15 explicitly makes every depicted notification optional and dependent on the owner/servicer agreement; the artwork does not require all three sends. Early notification can precede final booking, booking can include conversion and charges, and notification may support cash positioning, reconciliation or investigation. The source Receive notification description and AccountOwner lane assign receipt to the owner while its T15 Initiator cell literally says Account Servicer. That unresolved source responsibility conflict is preserved as issue-000060. No message ID is printed in this activity.',slugs=roles,flows=[117],tables=[15],issues=['issue-000060'])
add(9,'Transaction reconciliation initiated by the account owner','''flowchart TB
 subgraph A["AccountingSystem"]
 Book1("Book cash movement1") --> Send2("Send cash movement information2")
 end
 subgraph R["ReconciliationSystem"]
 Receive("Receive cash movement information") --> Reconcile("Reconcile") --> End(((" ")))
 end
 subgraph T["TreasurySystem"]
 Start((" ")) --> Initiate("Initiate transaction")
 end
 subgraph S["AccountServicer"]
 Process("Receive and process transaction") --> Book2("Book Cash movement2") --> Send1("Send cash movement information 1")
 end
 Initiate --> Book1
 Initiate --> Process
 Send1 --> Receive
 Send2 --> Receive
''','Treasury initiates the financial leg; the internal accounting and external servicing branches book and send their cash-movement information to the reconciliation system. The source contains two outgoing arrows without a fork bar; no exclusive decision is introduced. T16 requires matching internal and external feeds and identifies unmatched items as possible investigation triggers. P121 distinguishes aggregate financial reconciliation from detailed individual information; the total paid is analysed with specifications in detailed reports. The underlying transaction may be with a third party or the account servicer. This activity names systems, not an exact message exchange.',slugs=roles+['accounting-system','reconciliation-system','treasury-system','counterparty'],flows=[119],tables=[16],paragraphs=(121,121))
add(10,'Transaction reconciliation initiated by a counterparty','''flowchart TB
 subgraph A["AccountingSystem"]
 BookL("Book liability/claim") --> SendL("Send liability/claim information")
 end
 subgraph R["ReconciliationSystem"]
 Receive("Receive information") --> Reconcile("Reconcile") --> End(((" ")))
 end
 subgraph S["AccountServicer"]
 Process("Receive and process transaction") --> Book("Book cash movement") --> Send("Send cash movement information")
 end
 subgraph C["Counterparty"]
 Start((" ")) --> Initiate("Initiate transaction") --> Fork@{ shape: fork }
 end
 Fork --> BookL
 Fork --> Process
 SendL --> Receive
 Send --> Receive
 style Fork fill:#d9d9d9,stroke:#777
''','The counterparty initiates the commercial transaction and its financial leg. A source fork bar splits toward internal liability/claim booking and servicing-side receipt/processing. The counterparty account servicer may differ from the account owner account servicer; intermediary financial institutions may transmit the transaction (T17). The two feeds converge in reconciliation; unmatched items can trigger investigation. P124 explains aggregate financial reconciliation, including lockbox, against detailed transaction specifications. The source pale vertical bar is preserved as a native fork with pale styling; it is not an exclusive choice.',slugs=roles+['accounting-system','reconciliation-system','counterparty'],flows=[122],tables=[17],paragraphs=(124,124))
add(11,'Reporting scenario 1: intraday report then end-of-day statement','''sequenceDiagram
 participant S as Account Servicer
 participant O as Account Owner
 S->>O: BankToCustomerAccountReport
 S->>O: BankToCustomerStatement
''','Under the agreed service, one or more intraday reports provide booked and pending movements; at end of business day the statement summarises all booked entries and provides booked and available balances. Both arrows run Account Servicer to Account Owner. Source names are resolved to the four exact definitions listed in this edition and companion Part2; no version comparison is inferred.',flows=[131],families=['camt.052','camt.053'],paragraphs=(132,132),kind='sequence')
add(12,'Reporting scenario 2: credit threshold, intraday report and statement','''sequenceDiagram
 participant S as Account Servicer
 participant O as Account Owner
 S->>O: BankToCustomerDebitCreditNotification
 S->>O: BankToCustomerAccountReport
 S->>O: BankToCustomerStatement
''','The agreed service sends notifications for incoming credits above a threshold, an intraday report at a pre-agreed time with all booked/pending movements since business-day start and booked/expected balances, then an end-of-day statement of booked entries with booked/available balances. The threshold is not supplied numerically and is not invented.',flows=[134],families=['camt.052','camt.053','camt.054'],paragraphs=(135,135),kind='sequence')
add(13,'Reporting scenario 3: authorised recipient relays information','''sequenceDiagram
 participant S as Account Servicer
 participant R as Recipient
 participant O as Account Owner
 S->>R: BankToCustomerDebitCreditNotification
 R->>O: BankToCustomerDebitCreditNotification<br/>or similar internal message
 S->>R: BankToCustomerStatement
 R->>O: BankToCustomerStatement<br/>or similar internal message
''','The account owner authorises the Recipient to receive account information. The source explicitly allows an internal message for the Recipient-to-Owner legs, so those legs are not guaranteed ISO 20022 exchanges. The diagram contains notification and statement only; no account-report arrow is added. Recipient is not equated with Forwarding Agent.',slugs=roles+['recipient'],flows=[137],families=['camt.053','camt.054'],paragraphs=(138,138),kind='sequence')
add(14,'Reporting through a forwarding agent','''sequenceDiagram
 participant S as Account Servicer
 participant F as Forwarding Agent
 participant O as Account Owner
 S->>F: BankToCustomerAccountReport OR<br/>BankToCustomerStatement
 F->>O: BankToCustomerAccountReport OR<br/>BankToCustomerStatement
''','The Forwarding Agent is a concentrating institution for the Account Owner. The three parties agree which reporting messages are sent. P141 also allows the final recipient to be a party authorised by the owner; this Recipient role is narrative context not drawn as a fourth actor. Both OR alternatives remain alternatives rather than a mandatory pair.',slugs=roles+['forwarding-agent','recipient'],flows=[140],families=['camt.052','camt.053'],paragraphs=(141,141),kind='sequence')
add(15,'Direct reporting request to the account servicer','''sequenceDiagram
 participant O as Account Owner
 participant S as Account Servicer
 O->>S: AccountReportingRequest
 Note right of S: Based on the request, the account servicer<br/>will send back the correct message definition
 S->>O: BankToCustomerAccountReport
 S->>O: BankToCustomerStatement
 S->>O: BankToCustomerDebitCreditNotification
''','The owner requests reporting directly; the servicer sends the requested definition to the owner. The three drawn return arrows enumerate available message definitions; the annotation makes selection dependent on the request. They are not a source requirement to send all three. The order and annotation are retained without inventing explicit alt frames absent from the original.',flows=[144],families=['camt.052','camt.053','camt.054','camt.060'],paragraphs=(145,147),kind='sequence')
add(16,'Relay reporting request and response','''sequenceDiagram
 participant O as Account Owner
 participant F as Forwarding Agent
 participant S as Account Servicer
 O->>F: AccountReportingRequest
 F->>S: AccountReportingRequest
 S->>F: BankToCustomerAccountReport
 F->>O: BankToCustomerAccountReport
 Note over O,S: Same principle applies to the statement<br/>and the debit/credit notification messages
''','The owner communicates with the servicer through a Forwarding Agent. P151 permits the owner either to send an AccountReportingRequest to that agent or request the agent to issue one; the latter request is not assigned an invented XML format. The forwarded request reaches the servicer, which responds through the agent. The same principle applies to statements and debit/credit notifications, as the source note states.',slugs=roles+['forwarding-agent'],flows=[149],families=['camt.052','camt.053','camt.054','camt.060'],paragraphs=(150,153),kind='sequence')
for x in spec:
 n=x['n'];fid=f'fig-{n:04d}';fig=next(f for f in rec['figures'] if f['figure_id']==fid);p=base/'diagrams/curated'/f'{fid}.md';orig=root/fig['images'][0]['asset'];pids=[prefix+z for z in x['slugs']];dlist=[d for d in defs if '.'.join(d['message_id'].split('.')[:2]) in x['families']];mids=[d['message_id'] for d in dlist];flowpaths=[next((base/'flows').glob(f'flow-{sid}-p{start}-*.md')) for start in x['flows']];loc=' / '.join(fig['heading_path'])+'; '+fig['locator']+'; word/'+fig['images'][0]['target'];locations=[{'source_id':sid,'locator':loc}]+[{'source_id':'src-000005','locator':d['title']+'; file pages'+str(d['start_page'])+'-'+str(d['end_page'])} for d in dlist]
 m={'template':False,'document_kind':'diagram','manual_curated':True,'review_status':'needs-review','domain':'payments','diagram_id':fid,'title':x['title'],'diagram_kind':x['kind'],'content_origin':'source-reconstruction','source_ids':[sid]+(['src-000005'] if mids else []),'source_editions':[s['source_edition']],'source_locations':locations,'participants':pids,'flow_ids':[kb.metadata(fp)[0]['flow_id'] for fp in flowpaths],'message_ids':mids,'message_sets':[s['set_slug']],'render_status':'not-run','visual_review':'not-run','issue_ids':x['issues'],'limitations':['Native Mermaid preserves source relationships; original raster retains exact typography, icons, colors and geometry.']}
 body='# '+x['title']+'\n\n## Source evidence\n\n'+kb.source_link(root,p,s)+'; '+loc+'. '+kb.link(p,orig,'Unchanged original figure')+'.\n\n![Complete source figure]('+kb.rel(p,orig)+')\n\n## Mermaid reconstruction\n\n```mermaid\n'+x['code']+'```\n\n## Roles, activities and alternatives\n\n'+x['desc']+'\n\n'+kb.table(['Source-scoped role','Canonical reference'],[[z.replace('-',' '),kb.link(p,root/'shared/reference/participants'/(prefix+z+'.md'),z.replace('-',' '))] for z in x['slugs']])+'\n'
 if x['tables']:body+='Complete source responsibilities/conditions: '+', '.join(kb.link(p,base/'documents'/sid/'tables'/f'tbl-{t:04d}.md','T'+str(t)) for t in x['tables'])+'.\n\n'
 if dlist:body+='## Exact message evidence\n\n'+kb.table(['Source family','Exact supplied definition','Companion MDR Part2 locator'],[['.'.join(d['message_id'].split('.')[:2]),kb.link(p,root/'domains/payments/reference/messages'/d['message_id']/'index.md',d['message_id']),d['source_id']+'; '+d['title']+'; file pages'+str(d['start_page'])+'-'+str(d['end_page'])] for d in dlist])+'\n'
 if flowpaths:body+='Reusable flows: '+', '.join(kb.link(p,fp,kb.metadata(fp)[0]['title']) for fp in flowpaths)+'.\n\n'
 body+='## Review evidence\n\nComplete source artwork inspected; Mermaid rendering and visual comparison pending.\n';put(p,kb.front(m)+body);put(p.with_suffix('.mmd'),x['code'])
 for fp in flowpaths:
  fm,fb=kb.metadata(fp);fm.update(manual_curated=True,document_kind='business-flow',participants=sorted(set(fm.get('participants',[])+pids)),message_ids=mids,message_families=x['families']);fm['limitations']=[v for v in fm.get('limitations',[]) if not v.startswith('Source-delimited draft')];fm['limitations'].append('Business conditions and source contradictions are separate from XML validation.');fb=fb.replace('Mermaid reconstruction and visual review are pending.','Canonical source reconstruction and actual review evidence are linked below.');fb+='\n## Curated source flow\n\n'+x['desc']+'\n\n'+kb.link(fp,p,'Complete source diagram')+'.\n'
  if x['paragraphs']:
   lo,hi=x['paragraphs'];fb+='\n### Adjacent source narrative\n\n'+'\n\n'.join('**'+q['paragraph_id']+'** '+q['text'] for q in rec['paragraphs'] if lo<=int(q['paragraph_id'][1:])<=hi and q['text'])+'\n'
  fb+='\nScoped participants: '+', '.join(kb.link(fp,root/'shared/reference/participants'/(pid+'.md'),pid.removeprefix(prefix).replace('-',' ')) for pid in pids)+'.\n';put(fp,kb.front(fm)+fb)
 for pid in pids:
  pp=root/'shared/reference/participants'/(pid+'.md');pm,pb=kb.metadata(pp);pm.update(manual_curated=True,flows=sorted(set(pm.get('flows',[])+m['flow_ids'])),message_ids=sorted(set(pm.get('message_ids',[])+mids)));pb+='\nBank-to-customer source context: '+kb.link(pp,p,x['title'])+'. '+', '.join(kb.link(pp,fp,'flow '+kb.metadata(fp)[0]['title']) for fp in flowpaths)+'.\n';put(pp,kb.front(pm)+pb)
 out.append({'diagram':p.relative_to(root).as_posix(),'source_figure':fid,'source_occurrences':[fid],'original':orig.relative_to(root).as_posix(),'preview':orig.relative_to(root).as_posix(),'issue_ids':x['issues']})
for start in [98,112,114,126,128]:
 p=next((base/'flows').glob(f'flow-{sid}-p{start}-*.md'));m,b=kb.metadata(p);m.update(document_kind='source-process-section',manual_curated=True);put(p,kb.front(m)+b)
kb.dump(root/'work/documents'/sid/'curated-figures.json',out);print('12 canonical source reconstructions, 14 substantive flow references')
