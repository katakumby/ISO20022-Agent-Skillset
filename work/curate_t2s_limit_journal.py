from pathlib import Path
seed=Path('work/curate_t2s_cashaccount.py').read_text(encoding='utf-8-sig')
exec(seed.split("role('recipient-party'")[0].replace('src-000350','src-000362').replace('src-000351','src-000363'))
role('settlement-bank','Settlement Bank','A query-capable class named by P51 and scope image2; the detailed T6 role table instead defines Payment Bank. Preserve the separate source label without inferring that every settlement bank is a payment bank.','P51/P53; word/media/image2.png')
role('csd-participant','CSD Participant','The financial-institution actor label CSDParticipant occurs in the role/process context diagram. The query taxonomy expressly labels CSD Participants (DCP), supporting a contextual cross-link to the Direct Connected Participant record without identifying an institution.','P96/P111/image3.png; P131/image5.jpeg')
role('system-application','System Application','The source labels SystemApplication with the stereotype System and connects it from LimitProcess in the business-role/process context. It is a system participant in that context, not a legal financial institution or the exclusive sender of a message.','P96/P111; word/media/image3.png')
role('payment-agent','Payment Agent','The context diagram labels PaymentAgent with FinancialInstitution; the communication diagram uses the combined source label Payment Agent/Bank on the instructing side. This supports a contextual cross-link to Payment Bank, not a universal equivalence.','P96/P99/P111; images3/4')
role('credit-provider','Credit Provider','Manages the cash limits whose amount, utilisation and transaction journal are queried and reported. P65 expressly describes an NCB acting as parent and credit provider; the role is not equated with the query sender in every case.','P62/P65/P77/P153')
role('credit-consumer','Credit Consumer','Party whose identification is a mandatory business query attribute. The responsible party and activity date also constrain the query. The supplied examples use a payment bank as the credit consumer.','P51/P64-P66; P169-P170/P192/P223/P230')
role('responsible-party','Responsible Party of the Credit Consumer','Mandatory query attribute for the credit consumer: P65 specifies NCB acting as parent and credit provider or CSD acting as parent of the client. The report includes this identification too.','P65/P80; example P195-P199/P239-P243')
roles=['instructing-party','executing-servicing-party'];spec=[]
def add(n,title,code,desc,slugs=roles,flows=[],tables=[],families=[],issues=[],paragraphs=None):spec.append(dict(n=n,title=title,code=code,desc=desc,slugs=slugs,flows=flows,tables=tables,families=families,issues=issues,paragraphs=paragraphs))
add(1,'Limit-utilisation journal scope exchange','''sequenceDiagram
 participant I as NCBs or Payment/Settlement<br/>Banks
 participant E as Settlement Infrastructure
 I->>E: Limit Utilisation Journal Query (camt.064)
 E->>I: Limit Utilisation Journal Report (camt.065)
''','The scope picture shows an NCB/payment/settlement-bank query to Settlement Infrastructure and the returning report. P51 additionally names CSDs; P62/P77 also name directly connected system participants. Those narrative actors are included in the flow and participant library even though this particular picture omits them. Complete Word6 confirms the floating source text is part of the settlement-infrastructure label, with no additional actor or message. The query/report uses Business Application Header head.001 (P55), not Business File Header.',slugs=roles+['national-central-bank-ncb','payment-bank','settlement-bank','settlement-infrastructure','central-securities-depositories-csd','direct-connected-participant-dcp'],flows=[137],tables=[4,7,8],families=['camt.064','camt.065'])
add(2,'Limit process actors and reporting scope','''usecase-beta
 direction TB
 actor CSDP("«FinancialInstitution» CSDParticipant")
 actor CSD("«FinancialInstitution» CentralSecuritiesDepository")
 actor PAY("«FinancialInstitution» PaymentAgent")
 actor CCP("«BusinessActor» CentralCounterparty")
 actor NCB("«FinancialInstitution» NationalCentralBank")
 actor SYS("«System» SystemApplication")
 BA("«BusinessArea» SettlementAndReconciliation")
 P("«Processes» LimitProcess")
 M("LimitManagement")
 R("LimitReporting")
 J("LimitJournaling")
 BA -- P
 P --> CSDP
 P --> CSD
 P --> PAY
 P --> CCP
 P --> NCB
 P --> SYS
 P -- M
 P -- R
 P -- J
 classDef scope fill:#a7b89c,stroke:#7c8c75
 class R scope
''','Native use-case notation preserves the six actor symbols, source stereotypes, directed LimitProcess-to-actor associations and plain links from the business area and to three process ellipses. No include, extend or inheritance semantics are supplied or invented. Only LimitReporting is green and in the supplied message-set scope; LimitManagement and LimitJournaling are source context (P97/P109). This exact artwork occurs at P96 and P111 and is reconstructed once. The source business-area label SettlementAndReconciliation does not reroute this T2S child set or classify it merely by its camt prefix.',slugs=['csd-participant','central-securities-depositories-csd','payment-agent','central-counterparty','national-central-bank-ncb','system-application'],flows=[132],tables=[6,7,8],families=['camt.064','camt.065'])
add(3,'Limit reporting communication roles','''sequenceDiagram
 participant I as Instructing Party
 participant E as Executing/Servicing Party
 Note left of I: Central Securities Depository<br/>Direct Connected Participant<br/>National Central Bank<br/>Payment Agent/Bank<br/>Central Counterparty<br/>T2S Operator
 Note right of E: Settlement infrastructure
 I->>E: Limit Utilisation Journal Query (camt.064)
 E->>I: Limit Utilisation Journal Report (camt.065)
''','The source lists six contextual business-role alternatives beside Instructing Party and Settlement infrastructure beside Executing/Servicing Party. Dotted annotation leaders point from the two role/lifeline areas toward their labels; these are mapping annotations, not additional message exchanges. T7 independently confirms the mappings. The reconstruction uses native notes for the labels while retaining the exact leader appearance in the original.',slugs=roles+['central-securities-depositories-csd','direct-connected-participant-dcp','national-central-bank-ncb','payment-bank','payment-agent','central-counterparty','t2s-operator','settlement-infrastructure'],flows=[137],tables=[7],families=['camt.064','camt.065'])
add(5,'Query taxonomy and limit-journal scope','''flowchart TB
 Q["Queries"] --> A["A2A"]
 Q --> U["U2A"]
 A -.- U
 A --- Modes((" "))
 U --- Modes
 Modes --> C["CSDs"]
 Modes --> D["CSD Participants (DCP)"]
 Modes --> P["Payment Banks"]
 Modes --> N["NCBs"]
 C --- Actors((" "))
 D --- Actors
 P --- Actors
 N --- Actors
 Actors --> I["Instructions"]
 Actors --> S["Security accounts"]
 Actors --> T["Static Data"]
 Actors --> Cash["Cash accounts"]
 Actors --> Dyn["Dynamic data queries"]
 Actors --> Day["Settlement day"]
 Cash --> Detail["Fourteen cash query/response pairs<br/>retained in linked detail views"]
 style Modes fill:none,stroke:none
 style Actors fill:none,stroke:none
''','Queries branch into A2A/U2A and a shared actor/category taxonomy. The source includes a dashed A2A–U2A connector without a defined meaning, retained as dashed and not interpreted as a message. CSDs, CSD Participants (DCP), Payment Banks and NCBs feed six query categories. Cash accounts has fourteen query/response pairs, with forward solid and return dashed links; only the Limit Utilisation Journal pair is green/in scope. The complete source and two focused detail reconstructions preserve all28 leaf labels and28 message-type link labels. The reconstruction adds a clearly labelled detail-navigation box, not a source process. Other query types are context and are not assigned camt.064/065.',slugs=['central-securities-depositories-csd','direct-connected-participant-dcp','csd-participant','payment-bank','national-central-bank-ncb'],flows=[132],tables=[2,8],families=['camt.064','camt.065'])
add(10,'Participant-triggered limit-journal pull activity','''flowchart TB
 subgraph I["Instructing Party"]
 S((" ")) --> Manage("Manage/Investigate Limits")
 Manage --> Request("Request Limit Utilisation Journal")
 Receive("Receive Report") --> Reconcile("Reconcile Limits")
 Reconcile --> End(((" ")))
 end
 subgraph E["Servicing/Executing Party"]
 Validate("Validate Request") --> Valid{"Valid Request"}
 Valid -->|No| Reject("Send Reject")
 Valid -->|Yes| Process("Process Request")
 Process --> Report("Send Report")
 Reject --> Merge@{ shape: fork }
 Report --> Merge
 end
 Request --> Validate
 Merge --> Receive
 classDef contextual fill:#a8c5e4,stroke:black
 classDef covered fill:#a4aa32,stroke:black
 class Manage,Reconcile contextual
 class Request,Receive,Validate,Reject,Process,Report covered
 style S fill:#4678bb,stroke:#4678bb
''','An instructing party investigating limits triggers Request Limit Utilisation Journal. The servicing/executing party validates the request: No sends a rejection report specifying the operational error; Yes processes and sends the requested report. Both paths reach the source black join bar and return to Receive Report, followed by Reconcile Limits and an end point. The native fork/join bar preserves the source mark without asserting parallel execution: the preceding Yes/No choice is exclusive. T8 requires limits to exist within the instructing party scope; the source states postconditions as none. T10 preserves technical and business validation and the communication-layer handoff.',slugs=roles+['credit-provider','credit-consumer','responsible-party','central-securities-depositories-csd','national-central-bank-ncb','payment-bank','direct-connected-participant-dcp'],flows=[137],tables=[8,10],families=['camt.064','camt.065'])
add(11,'Scheduled limit-journal push activity','''flowchart TB
 subgraph I["Instructing Party"]
 Receive("Receive Report") --> Reconcile("Reconcile Limits")
 Reconcile --> End(((" ")))
 end
 subgraph E["Servicing/Executing Party"]
 S((" ")) --> EOD("Process EOD Reporting")
 EOD --> Request("Request Limit Utilisation Journal")
 Request --> Process("Process Request")
 Process --> Send("Send Report")
 end
 Send --> Receive
 classDef contextual fill:#a8c5e4,stroke:black
 classDef covered fill:#a4aa32,stroke:black
 class EOD,Reconcile contextual
 class Request,Process,Send,Receive covered
 style S fill:#4678bb,stroke:#4678bb
''','The executing/servicing party starts end-of-day reporting, internally requests and processes the report, then sends it to the instructing-party subscriber. No inbound query message is drawn or required for this push activity. T11 explicitly assigns Request, Process and Send to the executing/servicing party and Receive to the subscriber. Reconcile Limits follows receipt. T8 supplies the scheduled end-of-day trigger and existing-limit precondition; no additional acknowledgement, cancellation or reversal message is introduced.',slugs=roles+['instructing-party-subscriber-to-receive-the-report','credit-provider','credit-consumer','responsible-party'],flows=[143],tables=[8,11],families=['camt.065'])
add(12,'Limit-journal business transaction exchange','''sequenceDiagram
 participant I as Instructing Party
 participant E as Execution/Servicing Party
 I->>E: Limit Utilisation Journal Query — camt.064
 E->>I: Limit Utilisation Journal Report — camt.065
''','Instructing Party sends the query to the source-labelled Execution/Servicing Party and receives the report. P151-P153 explains that the central system returns limit amounts, utilisation and the transaction journal managed by the credit provider and matching query criteria. The broader source describes an additional scheduled push mode; this two-message picture depicts the request/response exchange only. Rejection uses the same report with operational error content (T10 and P314-P316), not a distinct cancellation or reversal message.',slugs=roles+['national-central-bank-ncb','central-securities-depositories-csd','payment-bank','direct-connected-participant-dcp','credit-provider','credit-consumer','responsible-party'],flows=[137],tables=[10],families=['camt.064','camt.065'],paragraphs=(150,153))
block=seed[seed.index('for x in spec:'):].replace("'src-000351'","'src-000363'")
block=block.replace("preview=root/'domains/securities/assets'/sid/'derived-previews'/(orig.name+'.png');","preview=orig;").replace('if n==7:','if False:').replace("(['fig-0009'] if n==7 else [])","(['fig-0004'] if n==2 else [])").replace("'class' if n==1 else 'sequence' if n>=10 else 'activity'","'use-case-context' if n==2 else 'taxonomy' if n==5 else 'sequence' if n in [1,3,12] else 'activity'").replace('Cash-account source context:','Limit-journal source context:')
exec(block)
# Preserve the exact duplicate source occurrence and complete page evidence.
for n,pages in {1:[6],2:[9,12],3:[9],5:[13],10:[15],11:[16],12:[18]}.items():
 p=base/'diagrams/curated'/f'fig-{n:04d}.md';m,b=kb.metadata(p);m['source_locations'] += [{'source_id':sid,'locator':'Word rendered file/printed page'+str(pg)} for pg in pages]
 if n==2:m['source_locations'].append({'source_id':sid,'locator':'P111 / fig-0004; same unchanged word/media/image3.png as P96 / fig-0002'})
 b+='\nComplete source pages: '+', '.join(kb.link(p,root/'domains/securities/assets'/sid/'source-page-renders'/f'word-page-{pg:02d}.png',f'Word{pg}') for pg in pages)+'.\n';put(p,kb.front(m)+b)
# Explicit formal conditions apply separately to each supported mode.
for start in [132,137,143]:
 p=next((base/'flows').glob(f'flow-{sid}-p{start}-*.md'));m,b=kb.metadata(p);m['manual_curated']=True;m['flow_scope']='parent process with two modes' if start==132 else 'pull mode' if start==137 else 'push mode';b+='\n## Source-defined conditions and direction\n\nT8 requires limits to exist within the scope of the Instructing Party and states postconditions as none. Its two triggers are a participant query or a scheduled system event at end of day. '+('This is the parent query/report process; the pull and push mode records provide the distinct ordered activities.' if start==132 else 'This mode is triggered by an Instructing Party query and sends camt.064 to Executing/Servicing Party; camt.065 returns data or an operational error.' if start==137 else 'This mode is triggered by the executing system end-of-day event; camt.065 goes to the Instructing Party subscriber without an inbound camt.064 exchange.')+'\n';b+='\nLinked modes: '+', '.join(kb.link(p,next((base/'flows').glob(f'flow-{sid}-p{x}-*.md')),'pull mode' if x==137 else 'push mode') for x in [137,143])+'.\n';put(p,kb.front(m)+b)
for start in [108,134,136,147,150,152]:
 p=next((base/'flows').glob(f'flow-{sid}-p{start}-*.md'));m,b=kb.metadata(p);m.update(document_kind='source-process-section',manual_curated=True);b+='\nCanonical reusable process modes: '+', '.join(kb.link(p,next((base/'flows').glob(f'flow-{sid}-p{x}-*.md')),'pull mode' if x==137 else 'push mode') for x in [137,143])+'.\n';put(p,kb.front(m)+b)
# Narrative-only role relationships and source-specified identifiers.
for slug in ['credit-provider','credit-consumer','responsible-party']:
 pp=root/'shared/reference/participants'/(prefix+slug+'.md');m,b=kb.metadata(pp);b+='\nRelated contextual roles: '+', '.join(kb.link(pp,root/'shared/reference/participants'/(prefix+x+'.md'),x.replace('-',' ')) for x in ['national-central-bank-ncb','central-securities-depositories-csd','payment-bank'])+'. The source examples identify parties with AnyBIC/BICFI and dedicated cash account9000000123 (P169-P170/P192/P197/P223/P230/P241); these are example values, not a universal institution assignment.\n';put(pp,kb.front(m)+b)
print('Authored seven canonical source diagrams and distinct pull/push flows')
