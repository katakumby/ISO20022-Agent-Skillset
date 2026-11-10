from pathlib import Path
seed=Path('work/curate_t2s_cashaccount.py').read_text(encoding='utf-8-sig')
exec(seed.split("role('recipient-party'")[0].replace('src-000350','src-000374').replace('src-000351','src-000375'))
role('account-owner','Account Owner','Party who owns the securities account identified in the optional AccountOwner block of the Securities Account Position Response. P258 also permits account owner as a history-query search criterion. Account ownership is a functional relationship and is not equated with the query sender in every flow.','P171-P174/P258; Word12/25')
role('account-servicer','Account Servicer','Party managing the account on behalf of the account owner: registration and booking of entries, balance calculation and account information. This is optional in the position response (P173-P174), mandatory and non-repetitive in the penalties report (P193-P194). It is not automatically equated with a named institution or with every technical sender.','P173-P174/P193-P194; Word12-13')
role('csd-participant','CSD Participant','Actor shown as CSDParticipant with FinancialInstitution stereotype. Penalty reporting supplies penalties imposed on or credited to the CSD participant itself; a CSD receives information for its data-scope participants. This label is not universally equated with a directly connected participant.','P181/P204/P277-P279; Word13/14/25-26')
role('system-application','System Application','SystemApplication is the system-stereotyped actor in the settlement/reconciliation context. The source does not assign it as the business owner of every account or as a separate message sender.','P204/image6; Word14')
role('payment-bank','Payment Bank','Named example of a directly connected T2S participant sending a settlement query and receiving a response. It is a contextual business-role example, not an identity of every instructing party.','P103/P133/P260/P268; Word9-10/25')
role('settlement-bank','Settlement Bank','Named alongside payment bank as an example of a directly connected T2S participant in settlement-query and response usage. No general equivalence of the two labels is asserted.','P103/P133/P260/P268; Word9-10/25')
role('authorised-party','Party Authorised by a CSD','May receive a securities account position response from T2S where authorised by the CSD. Source permissions and data scope govern access; this role is not assumed to own the account.','P158/P275; T8; Word12/17/25')
role('external-csd','External CSD','For penalties reporting, receives information about penalties imposed on or credited to that External CSD itself. The source places it beside the CSD-participant case without claiming universal equivalence.','P279; Word26')
role('penalty-debtor','Penalty Debtor','Debtor is one of the reporting criteria for previously calculated cash penalties. The report can identify parties on whom penalties are imposed; this record is scoped to penalty reporting, not payment-debtor roles in other domains.','T12 row2; P181/P277-P279; Word13/23/25-26')
role('penalty-creditor','Penalty Creditor','Creditor is one of the reporting criteria for previously calculated cash penalties. The report can identify parties credited with penalties; this record is scoped to penalty reporting.','T12 row2; P181/P277-P279; Word13/23/25-26')
role('t2s-actor','T2S Actor','Contextual platform actor addressed by position queries and penalties reports. For penalties, P277 specifies CSDs or CSD participants, with data scope and External CSD treatment in P278-P279. The label remains broader than any one institution type.','P56/P158-P164/P277-P279; Word6/12/25-26')
role('national-central-bank','National Central Bank','T6 T2S Operator definition includes NCBs participating in T2S among managed T2S actors. This narrative management relationship does not assign NCB as a confirmed sender of these five messages.','T6 row6; Word15')
roles=['instructing-party','executing-servicing-party'];spec=[]
def add(n,title,code,desc,slugs=roles,flows=[],tables=[],families=[],issues=[],paragraphs=None):spec.append(dict(n=n,title=title,code=code,desc=desc,slugs=slugs,flows=flows,tables=tables,families=families,issues=issues,paragraphs=paragraphs))
add(1,'Securities account position query and response exchange','''sequenceDiagram
 participant I as Instructing Party
 participant S as Servicing Party
 I->>S: 1. Securities Account Position Query (semt.025)
 S->>I: 2. Securities Account Position Response (semt.040)
''','A CSD or directly connected party sends criteria and an optional date range to T2S acting as Servicing Party. The response covers matching positions across the accounts and securities selected. Complete Word6 displays this image only: embedded legacy actor fragments/text in the same paragraph do not create extra visible actors or a second response. P258 adds the error-family sese.022, absent from this success-only picture; its exact version is not specified here.',slugs=roles+['servicing-party','central-securities-depositories-csd','direct-connected-participant-dcp','account-owner','account-servicer','authorised-party','t2s-actor'],flows=[232],tables=[8,10],families=['semt.025','semt.040'],paragraphs=(257,258))
add(2,'Securities settlement transaction query and response exchange','''sequenceDiagram
 participant I as Instructing Party
 participant E as Executing/Servicing Party
 I->>E: 1. Securities Settlement Transaction Query (semt.026)
 E->>I: 2. Securities Settlement Transaction Query Response (semt.027)
''','A CSD or directly connected T2S participant sends an instruction, current-status or status-period query. The response returns matching settlement instructions. P266 specifies a sese.022-family response on business error; this success-only picture omits that alternative. The exact error-message definition is not resolved from Part1.',slugs=roles+['central-securities-depositories-csd','direct-connected-participant-dcp','payment-bank','settlement-bank','settlement-infrastructure'],flows=[239],tables=[8,11],families=['semt.026','semt.027'],paragraphs=(259,273))
add(3,'Penalty reporting in settlement instruction context','''sequenceDiagram
 participant I as Instructing Party
 participant E as Executing/Servicing Party
 I->>E: 1. Securities Settlement Transaction Instruction (sese.023)
 E-->>I: 2. Securities Settlement Transaction Status Advice (sese.024)
 E-->>I: 3. Securities Transaction Penalties Report (semt.044)
''','The first instruction and returning status advice are surrounding context; only semt.044 is the green in-scope report. Cash penalties are computed daily for instructions unsettled after their intended settlement date and can be modified by a CSD or recalculated after reference-data changes. The picture retains the solid instruction and dashed returning status/report directions. The report is system-triggered (T8/T12), so the three arrows do not require one immediate penalty report for every instruction. Source sese.023/sese.024 family labels are retained without choosing an exact definition from another edition.',slugs=roles+['servicing-party','settlement-infrastructure','central-securities-depositories-csd','csd-participant','external-csd','account-servicer','penalty-debtor','penalty-creditor','t2s-actor'],flows=[243],tables=[8,12],families=['semt.044'],paragraphs=(276,279))
add(4,'Securities reporting actors and process context','''usecase-beta
 direction TB
 actor CP("«FinancialInstitution» CSDParticipant")
 actor CSD("«FinancialInstitution» CentralSecuritiesDepository")
 actor CCP("«BusinessActor» CentralCounterparty")
 actor SYS("«System» SystemApplication")
 BA("«BusinessArea» SettlementAndReconciliation")
 P("«Processes»")
 BA --> CP
 BA --> CSD
 BA --> CCP
 BA --> SYS
 BA -- P
''','Native use-case notation preserves four actor symbols, their stereotypes, the directed business-area-to-actor links and the plain business-area/process link. The lower process hierarchy is reconstructed in the linked detail view, preserving its rectangles, diamonds, ellipses, dashed arrows and green reporting scope. No include/extend or inheritance semantics are inferred. P205 explicitly identifies only green reporting processes as scope; surrounding instruction, cancellation, modification and confirmation processes are context.',slugs=['csd-participant','central-securities-depositories-csd','central-counterparty','system-application','t2s-operator','national-central-bank'],flows=[224],tables=[6,7,8],families=['semt.025','semt.026','semt.027','semt.040','semt.044'])
add(5,'Securities reporting business-process overview','''flowchart TB
 B["Settlement & Reconciliation"] --> I(["Instruction"])
 B --> R(["Reconciliation"])
 B --> S(["Status reporting"])
 B --> C(["Confirmation"])
 I --> M(["Modification"])
 I --> X(["Cancellation request"])
 M --> S
 X --> S
 C --> S
 C --> V(["Reversal"])
 R --> Rep(["Reporting"])
 R --> Q(["Query / Response"])
 classDef context fill:#b7cbe3,stroke:black
 classDef scope fill:#8df4cd,stroke:black
 class B,I,S,C,M,X,V context
 class R,Rep,Q scope
''','The source overview links Settlement & Reconciliation to Instruction, Status reporting, Confirmation and Reconciliation. Instruction branches to Modification and Cancellation request, both pointing to Status reporting. Confirmation points to Status reporting and Reversal. Reconciliation points to Reporting and Query/Response; these three nodes alone are green. Cancellation requests and reversals remain distinct contextual processes; the diagram does not assign their messages to the five reporting definitions.',slugs=roles+['settlement-infrastructure','central-securities-depositories-csd','direct-connected-participant-dcp'],flows=[224],tables=[8],families=['semt.025','semt.026','semt.027','semt.040','semt.044'])
add(10,'Securities position query activity with access and error decisions','''flowchart TB
 subgraph I["Instructing Party"]
 S((" ")) --> Reconcile("Reconcile Securities Positions")
 Receive("Process Status") --> Success{"Succesful Process?"}
 Success -->|No| Fail(((" ")))
 Success -->|Yes| Update("Update Securities Account Position")
 Update --> End(((" ")))
 end
 subgraph SP["Servicing Party"]
 Validate("Validate Request") --> Access{"Does the Party have Access Right<br/>To Securities Account Position query"}
 Access -->|No| Error("Update Status")
 Access -->|Yes| Query("Querying process in function<br/>with the selected criteria")
 end
 Reconcile --> Validate
 Error --> Receive
 Query --> Receive
 classDef stage fill:#c5cba6,stroke:black
 class Reconcile,Receive,Update,Validate,Error,Query,Success,Access stage
 style S fill:black,stroke:black
''','The Instructing Party initiates reconciliation by querying securities positions. Servicing Party validates access and the technical/business request: an unsuccessful check updates status and sends an error; a valid query retrieves matching data. Both return to Process Status. The Instructing Party ends on failure or updates its position reconciliation on success. T10 defines the update as an external reconciliation process, not a platform ownership transfer or settlement instruction. P258 names sese.022 for error and requires account or account owner for history queries.',slugs=roles+['servicing-party','account-owner','account-servicer','authorised-party','central-securities-depositories-csd','direct-connected-participant-dcp','t2s-actor'],flows=[232],tables=[8,10],families=['semt.025','semt.040'])
add(11,'Securities settlement query activity and operational-error branch','''flowchart TB
 subgraph I["Instructing Party"]
 S((" ")) --> Send("Send Securities Settlement<br/>Instructions Query")
 Monitor("Monitor") --> Reconcile("Reconcile")
 Reconcile --> End(((" ")))
 end
 subgraph E["Servicing/Executing Party"]
 Process("Process Query") --> Decision{"Processed"}
 Decision -->|No| Error("Error Processing")
 Error --> SendError("Send Error Response")
 Decision -->|Yes| Response("Send Securities Settlement<br/>Instructions Query Response")
 SendError --> Merge@{ shape: fork }
 Response --> Merge
 end
 Send --> Process
 Merge --> Monitor
 classDef stage fill:#d0e7cf,stroke:black
 class Send,Monitor,Reconcile,Process,Decision,Error,SendError,Response stage
 style Merge fill:black,stroke:black
 style S fill:black,stroke:#55baff
''','The query initiator requests instructions matching its criteria. Executing/Servicing Party validates the query. The No branch adds operational error details and sends an error response; Yes sends the requested instruction response. Both source arrows join at the black bar and return to Monitor, then Reconcile. The preceding Yes/No decision is exclusive; the bar is retained without inventing parallel execution. The original vertical bar appears horizontally in this top-down native layout. T11 and P266 identify the error alternative; the exact sese.022 definition is unspecified.',slugs=roles+['central-securities-depositories-csd','direct-connected-participant-dcp','payment-bank','settlement-bank'],flows=[239],tables=[8,11],families=['semt.026','semt.027'])
add(12,'Scheduled cash-penalty reporting activity','''flowchart TB
 subgraph I["Instructing Party"]
 Monitor("Monitor") --> Reconcile("Reconcile")
 Reconcile --> End(((" ")))
 end
 subgraph SP["Servicing Party"]
 S((" ")) --> Event("System/Event Triggered")
 Event --> Required{"Report Required"}
 Required -->|No| None(((" ")))
 Required -->|Yes| Generate("Generate Report")
 Generate --> Success{"Success"}
 Success -->|No| Error("Error Processing")
 Error --> Failed(((" ")))
 Success -->|Yes| Report("Report Cash Penalties Calculated")
 end
 Report --> Monitor
 classDef context fill:#9bc9f1,stroke:black
 classDef scope fill:#c2c6a6,stroke:black
 class Event,Error,Reconcile context
 class Required,Generate,Success,Report,Monitor scope
 style S fill:black,stroke:black
''','Servicing Party starts from a system event. If no report is required, the process ends. Otherwise it generates the report; a failure goes through internal Error Processing and ends without a drawn outbound error message. Success reports cash penalties to the subscribing Instructing Party, which monitors and reconciles. T12 requires report interest/configuration and criteria such as business day, debtor and creditor; T8 also requires static-data privileges and in-scope existing business objects. The technical sender is T2S; the recipient functional label does not imply that the subscriber initiated this scheduled event.',slugs=roles+['servicing-party','settlement-infrastructure','central-securities-depositories-csd','csd-participant','external-csd','account-servicer','penalty-debtor','penalty-creditor','t2s-actor'],flows=[243],tables=[8,12],families=['semt.044'])
add(13,'Reconciliation across status, penalty and settlement information','''flowchart TB
 S((" ")) --> I["Instruction"]
 I --> Status["Status reporting"]
 Status --> Penalty["Cash Penalties Calculation"]
 Penalty --> Confirm["Settlement Confirmation"]
 Status --> Reconcile["Reconciliation"]
 Penalty --> Reconcile
 Confirm --> Reconcile
 Reconcile --> End(((" ")))
 classDef context fill:#b7cbe3,stroke:black
 class I,Status,Penalty,Confirm context
 style Reconcile fill:#cafa9e,stroke:black
 style S fill:#4678bb,stroke:#4678bb
''','The context diagram starts with Instruction then Status reporting, Cash Penalties Calculation and Settlement Confirmation. Each of the last three information stages feeds Reconciliation, the only green node, which leads to the final symbol. This is a high-level business context, not a claim that every instruction incurs a penalty or that each arrow is a separate XML message. P250 explicitly includes pending and posted transactions and computed penalties if any.',slugs=roles+['account-owner','account-servicer','central-securities-depositories-csd','csd-participant','penalty-debtor','penalty-creditor'],flows=[224],tables=[8],families=['semt.025','semt.026','semt.027','semt.040','semt.044'],paragraphs=(247,252))
block=seed[seed.index('for x in spec:'):].replace("'src-000351'","'src-000375'")
block=block.replace("preview=root/'domains/securities/assets'/sid/'derived-previews'/(orig.name+'.png');","preview=(root/'domains/securities/assets'/sid/'derived-previews'/(orig.name+'.png')) if orig.suffix.lower() in ['.emf','.wmf'] else orig;").replace('if n==7:','if False:').replace("(['fig-0009'] if n==7 else [])","[]").replace("'class' if n==1 else 'sequence' if n>=10 else 'activity'","'use-case-context' if n==4 else 'sequence' if n in [1,2,3] else 'activity'").replace('Cash-account source context:','Securities and penalty reporting source context:')
exec(block)
# Source-family references outside the supplied exact reporting definitions remain unresolved.
for n,fams in {1:['sese.022'],2:['sese.022'],3:['sese.023','sese.024'],10:['sese.022'],11:['sese.022']}.items():
 p=base/'diagrams/curated'/f'fig-{n:04d}.md';m,b=kb.metadata(p);m['related_message_families']=fams;m['limitations'].append('Related family references do not specify an exact version in this Part1; no arbitrary exact definition is assigned.');put(p,kb.front(m)+b)
# The native actor context and the source process shape hierarchy are complementary detail views.
p=base/'diagrams/curated/fig-0004-processes.md';code='''flowchart TB
 P(["«Processes»"]) -.-> I["Instruction"]
 P -.-> C["Confirmation"]
 P -.-> R["Reconciliation"]
 I -.-> M{"Modification Request"}
 I -.-> X{"Cancellation Request"}
 M -.-> S(["«Status reporting»"])
 X -.-> S
 C -.-> S
 R -.-> Q(["«Query / Response»"])
 R -.-> Rep(["«Reporting»"])
 classDef context fill:#d6e4fb,stroke:#7097cd
 classDef scope fill:#d4e3cd,stroke:#80b260
 class P,I,C,M,X,S context
 class R,Q,Rep scope
''';m={'template':False,'document_kind':'diagram-detail','manual_curated':True,'review_status':'needs-review','diagram_id':'fig-0004-processes','title':'Reporting process hierarchy detail','domain':'securities','content_origin':'source-reconstruction','diagram_kind':'process-context','source_ids':[sid],'source_locations':[{'source_id':sid,'locator':'P204/image6.png; Word14; lower process hierarchy'}],'message_sets':[s['set_slug']],'render_status':'not-run','visual_review':'not-run','limitations':['Source rectangles, diamond request nodes and dashed relationships retained; no exclusive decision semantics inferred from the request diamonds.']};body='# Reporting process hierarchy detail\n\n'+kb.link(p,base/'diagrams/curated/fig-0004.md','Actor-context parent')+'; '+kb.link(p,root/'domains/securities/assets'/sid/'originals/image6.png','Complete unchanged original')+'.\n\n```mermaid\n'+code+'```\n\nThis detail preserves the lower source hierarchy, all dashed arrow directions and green Reconciliation/Query-Response/Reporting scope. Modification and Cancellation Request diamonds are source process labels; they are not asserted to form an exclusive choice. Native actor notation is preserved in the parent view.\n';put(p,kb.front(m)+body);put(p.with_suffix('.mmd'),code)
p=base/'diagrams/curated/fig-0004.md';m,b=kb.metadata(p);b+='\nComplete lower hierarchy: '+kb.link(p,base/'diagrams/curated/fig-0004-processes.md','process detail')+'.\n';put(p,kb.front(m)+b)
# Formal reusable scope: one parent and three distinct modes; broad headings and functionality excerpts are not independent flows.
for start in [220,226,228,247,257,259,267,274,276]:
 p=next((base/'flows').glob(f'flow-{sid}-p{start}-*.md'));m,b=kb.metadata(p);m.update(document_kind='source-process-section',manual_curated=True);b+='\nReusable mode references: '+', '.join(kb.link(p,next((base/'flows').glob(f'flow-{sid}-p{x}-*.md')),label) for x,label in [(232,'position query/response'),(239,'settlement query/response'),(243,'penalty report')])+'.\n';put(p,kb.front(m)+b)
for start in [224,232,239,243]:
 p=next((base/'flows').glob(f'flow-{sid}-p{start}-*.md'));m,b=kb.metadata(p);m.update(manual_curated=True,document_kind='business-flow',flow_scope='parent process with query/report modes' if start==224 else 'query mode' if start in [232,239] else 'scheduled reporting mode');b+='\n## Preconditions, trigger and outcome\n\nT8 requires the relevant business objects to exist within the instructing party scope and criteria, and static-data privileges for report reception. Postconditions are explicitly None. Query modes are initiated by the Instructing Party; penalty reporting is initiated by a scheduled system event. T12 additionally requires the subscriber to have configured interest in receiving the report.\n'
 if start in [232,239]:m['related_message_families']=['sese.022'];b+='\nBusiness-error response uses the sese.022 family (P258/P266). Its exact version is unspecified here. No cancellation or settlement reversal is implied by that error.\n'
 if start==243:b+='\nDaily reports cover a given business day; modified-penalty reports cover changes since previous recalculation, including removal, reinclusion, reallocation, switching and reference-data-driven updates; monthly reports aggregate the previous month using the last available penalty amounts (P181/P183/P185). CSDs receive data-scope party penalties; CSD participants or External CSDs receive their own penalties (P277-P279).\n'
 put(p,kb.front(m)+b)
print('Nine canonical diagrams plus process detail; four reusable flow records')
