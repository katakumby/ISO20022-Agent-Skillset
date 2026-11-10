"""Source359 diagrams transcribed after direct original/complete Word-page inspection."""
DATA={}
def spec(n,title,page,pstart,pend,tables,roles,code,notes=()):
 DATA[n]=dict(title=title,page=page,start=pstart,end=pend,tables=tables,roles=roles,code=code.strip()+'\n',notes=list(notes))
PREFIX='''%%{init: {"flowchart": {"htmlLabels": false, "wrappingWidth": 260}}}%%
flowchart TB
classDef green fill:#c5d0a5,stroke:#222,color:#000
classDef blue fill:#bfd4ee,stroke:#222,color:#000
classDef grey fill:#eeeeee,stroke:#555,color:#000
classDef bar fill:#222,stroke:#222,color:#222
'''
ROLES=['instructing-party','servicing-executing-party']
spec(2,'Intra-balance management in its business context',13,151,174,[8,9,10,11,12,13,14,15,16,17,18],['csd-participant','central-counterparty','national-central-bank','system-application','payment-agent','central-securities-depository'],'''usecase-beta
direction TB
S("SettlementAndReconciliation")
C("CashManagement")
L("LimitManagement")
I("IntraBalanceManagement")
R("CashManagementReporting")
actor A("«FinancialInstitution» CSDParticipant")
actor B("«BusinessActor» CentralCounterparty")
actor D("«FinancialInstitution» NationalCentralBank")
actor E("«System» SystemApplication")
actor F("«FinancialInstitution» PaymentAgent")
actor G("«FinancialInstitution» CentralSecuritiesDepository")
S -- C
C -- L
C -- I
C -- R
C --> A
C --> B
C --> D
C --> E
C --> F
C --> G
''',['The source has no enclosing system boundary and no include/extend labels. Plain process associations and directed actor associations are preserved; no generalization is inferred.','Source IntraBalanceManagement is green; all other process ovals are grey context. The original retains this colour distinction; the native use-case layout retains exact labels, stereotypes and connector semantics.'])
spec(3,'Instruction, status, confirmation and contextual processes',17,175,178,[],[],PREFIX+'''S@{ shape: f-circ, label: " " }
I["Instruction"]:::green
T["Status reporting"]:::green
C["Confirmation"]:::green
V["Reversal"]:::blue
R["Reconciliation"]:::blue
E@{ shape: fr-circ, label: " " }
S --> I --> T
T --> C
T --> E
C --> V
C --> R --> E
''',['P176 distinguishes green main processes from blue context. No extra outgoing edge is supplied for Reversal.'])
spec(4,'Modification and cancellation with status reporting',18,175,178,[],[],PREFIX+'''S@{ shape: f-circ, label: " " }
M["Modification Request"]:::green
C["Cancellation Request"]:::green
T["Status reporting"]:::green
V["Reversal"]:::blue
R["Reconciliation"]:::blue
E@{ shape: fr-circ, label: " " }
S --> M
S --> C
M --> T
C --> T
T --> E
T --> V
T --> R --> E
''',['Plain unlabelled connector junctions are normalized to common endpoints, not converted to decisions or concurrency bars. Source has no condition making both requests mandatory.'])
spec(5,'Reconciliation and its movement lifecycle context',19,175,182,[],[],PREFIX+'''S@{ shape: f-circ, label: " " }
I["Movement Instruction"]:::blue
D{" "}:::blue
C["Cancellation request"]:::blue
M["Modification Request"]:::blue
J["━━━━━━━━"]:::bar
T["Status reporting"]:::blue
F["Confirmation"]:::blue
V["Reversal"]:::blue
R["Reconciliation"]:::green
A["Cancellation advice"]:::blue
E@{ shape: fr-circ, label: " " }
S --> I
I --> D
I --> T
D -->|Cancellation needed| C
D -->|Modification needed| M
C --> J
M --> J
J --> T
T --> F
T --> A
F --> V
F --> R
F --> A
R --> A
R --> E
''',['The small bridge where the Confirmation-to-Reversal connector crosses Status reporting-to-Confirmation is not a connection. Both Confirmation-to-Reconciliation and Confirmation-to-Reversal remain distinct outgoing paths.','Cancellation advice and Reversal are context processes here, not proof that this message set supplies corresponding exact message definitions.'])
spec(10,'External intra-balance movement activity',21,189,192,[8,9,10,20],ROLES,PREFIX+'''subgraph A["IntructingParty"]
S@{ shape: f-circ, label: " " }
M("ManageCash"):::grey
I("InstructSubBalanceMovement"):::green
J["┃"]:::bar
N("Monitor"):::green
R("Reconcile"):::grey
E@{ shape: fr-circ, label: " " }
end
subgraph B["ServicingExecutingParty"]
P("ProcessInstruction"):::green
V{"Validated"}:::green
F["━━━━━━━━"]:::bar
K["┃"]:::bar
T("AdviseStatus"):::green
X("SettleInstruction"):::green
D{"Settled"}:::green
C("ConfirmMovement"):::green
end
S --> M --> I --> P --> V
V -->|No| K
V -->|Yes| F
F --> K
F --> X --> D
D -->|No| K
D -->|Yes| C
D -->|Partial Settlement| C
K --> T --> J
C --> J --> N --> R --> E
''',['The literal lane label IntructingParty is misspelled in the artwork. T20 calls the contextual activity Manage Liquidity whereas the picture says ManageCash.','T20 describes Yes/No settled results; the picture additionally explicitly shows Partial Settlement. Both paths are preserved.'])
spec(11,'Internal intra-balance movement activity',22,193,196,[8,9,10,21],['third-party','servicing-executing-party'],PREFIX+'''subgraph A["ThirdParty"]
J["┃"]:::bar
N("Monitor"):::green
R("Reconcile"):::grey
E@{ shape: fr-circ, label: " " }
end
subgraph B["ServicingExecutingParty"]
S@{ shape: f-circ, label: " " }
P("ProcessInstruction"):::green
X("SettleInstruction"):::green
D{"Settled"}:::green
T("AdviseStatus"):::green
C("ConfirmMovement"):::green
end
S --> P --> X --> D
D -->|No| T
D -->|Yes| C
D -->|Partial Settlement| C
T --> J
C --> J --> N --> R --> E
''',['T21 repeats Process Instruction as two table rows; the picture has one occurrence. The table is preserved intact, without fabricating a second picture activity.','The picture and T21 assign Monitor/Reconcile to Third Party. Transaction narrative P235/P237 instead says Instructing Party; no global equivalence is inferred.'])
spec(12,'Modification and cancellation activity',23,197,199,[11,12,13,22],ROLES,PREFIX+'''subgraph A["InstructingParty"]
S@{ shape: f-circ, label: " " }
M("Manage Liquidity"):::grey
I("Request IntraBalanceMovement Modification/Cancellation"):::green
N("Monitor"):::green
R("Reconcile"):::grey
E@{ shape: fr-circ, label: " " }
end
subgraph B["ServicingExecutingParty"]
P("Process Request"):::green
V{"Validated?"}:::green
F["━━━━━━━━"]:::bar
J["┃"]:::bar
T("Advise Status"):::green
X("Modify/Cancel IntraBalanceMovement Instruction"):::green
D{"Executed?"}:::green
end
S --> M --> I --> P --> V
V -->|No| J
V -->|Yes| F
F -->|Yes| J
F -->|Yes| X --> D
D -->|No| J
D -->|Yes| J
J --> T --> N --> R --> E
''',['Both Executed? branches feed Advise Status. T22 distinguishes a positive advice when execution succeeds; the picture does not supply separate status-message nodes.'])
spec(13,'Push modification and cancellation reporting activity',25,200,203,[16,23],['instructing-party','servicing-party'],PREFIX+'''subgraph A["Instructing Party"]
N("Monitor"):::green
R("Reconcile"):::grey
E@{ shape: fr-circ, label: " " }
end
subgraph B["Servicing Party"]
S@{ shape: f-circ, label: " " }
T("System Event Triggered"):::grey
D{"Report Required"}:::green
E1@{ shape: fr-circ, label: " " }
G("Generate Report"):::green
V{"Successful Process?"}:::green
X("Error Processing"):::grey
E2@{ shape: fr-circ, label: " " }
P("Send Intra Balance Movement Cancellation/Modification Report"):::green
end
S --> T --> D
D -->|No| E1
D -->|Yes| G
G -->|Yes| V
V -->|No| X --> E2
V --> P --> N --> R --> E
''',['T23 names Servicing/Executing Party Instructing Party jointly for the event initiator; the drawing places the event only in Servicing Party lane.','T23 Error Processing says operational errors are added to a response before routing to Instructing Party; the source picture instead ends that error branch in the servicing lane. No missing response arrow is invented.'])
spec(14,'Pull modification and cancellation reporting activity',27,204,207,[16,24],['instructing-party','servicing-party'],PREFIX+'''subgraph A["Instructing Party"]
Q("Send Intra Balance Movement Cancellation/Modification Query"):::green
N("Monitor"):::green
R("Reconcile"):::grey
E@{ shape: fr-circ, label: " " }
end
subgraph B["Servicing Party"]
V("Validate Request"):::green
D{"Successful Process?"}:::green
X("Error Processing"):::grey
P("Send Intra Balance Movement Cancellation/Modification Report"):::green
end
Q --> V --> D
D -->|No| X --> P
D -->|Yes| P
P --> N --> R --> E
''',['No start-point glyph is drawn in the source. T24 separately lists Generate Report; the picture proceeds directly from Validate Request to Successful Process? and therefore has no invented Generate Report box.'])
spec(15,'Pending and posting reporting activity',28,208,210,[17,18,25],ROLES,PREFIX+'''subgraph A["InstructingParty"]
N("Monitor"):::green
R("Reconcile"):::blue
E@{ shape: fr-circ, label: " " }
end
subgraph B["ServicingExecutingParty"]
S@{ shape: f-circ, label: " " }
T("SystemEvent Triggered"):::blue
D{"Report Required"}:::green
E1@{ shape: fr-circ, label: " " }
G("Generate Report"):::green
V{"Success"}:::green
X("Error Processing"):::blue
E2@{ shape: fr-circ, label: " " }
P("Report Pending/Settled Instructions"):::green
end
S --> T --> D
D -->|No| E1
D -->|Yes| G --> V
V -->|No| X --> E2
V -->|Yes| P --> N --> R --> E
''',['T25 Successful Process and Monitor rows refer to Cancellation/Modification Report, despite the pending/posting heading and picture. Those copied labels remain visible as issue-000047.','T25 jointly names Servicing/Executing Party Instructing Party as event initiator and says Error Processing routes a response; the picture shows the event only in the servicing lane and an error end point.'])
spec(16,'Movement query and response activity',30,211,215,[14,15,26],ROLES,PREFIX+'''subgraph A["Instructing Party"]
S@{ shape: f-circ, label: " " }
Q("Query Cash Movement Instructions"):::green
N("Monitor"):::green
R("Reconcile"):::blue
E@{ shape: fr-circ, label: " " }
end
subgraph B["Servicing/Executing Party"]
P("Process Query"):::green
D{"Processed?"}:::green
X("Error Processing"):::green
T("Send Cash Movemenrt Instruction Response"):::green
end
S --> Q --> P --> D
D -->|No| X --> T
D -->|Yes| T
T --> N --> R --> E
''',['The picture prints Movemenrt in the response activity; it is preserved literally. T26 uses Send Intra Balance Movement Report and the transaction sequence uses IntraBalanceMovementQueryResponse. These source labels remain distinct.','T15 names a system-event trigger while requiring receipt of an incoming query; this wording is retained, without imposing a timing rule beyond the source.'])

def seq(n,title,page,start,end,tables,left,right,steps,notes=()):
 code='%%{init: {"sequence": {"mirrorActors": false, "width": 220}, "themeVariables": {"actorBkg": "#ffffff", "actorBorder": "#000000"}, "themeCSS": ".actor-line { stroke-dasharray: 8 6 !important; stroke: #000 !important; }"}}%%\nsequenceDiagram\n'
 code+='participant A as '+left[0]+'\nparticipant B as '+right[0]+'\n'
 for a,b,label,dashed,color in steps:code+=a+('-->>' if dashed else '->>')+b+': '+label+'\n'
 spec(n,title,page,start,end,tables,[left[1],right[1]],code,notes)
 DATA[n]['steps']=steps;DATA[n]['actor_labels']={'A':left[0],'B':right[0]}
P=('Instructing Party','instructing-party');X=('Servicing/Executing Party','servicing-executing-party');V=('Servicing Party','servicing-party')
def s(a,b,name,code,dashed=False,color='green'):return(a,b,'IntraBalanceMovement'+name+' (camt.'+code+')',dashed,color)
seq(17,'External cash settlement restriction creation',31,219,228,[8,9,10,20],P,X,[s('A','B','Instruction','066'),s('B','A','StatusAdvice','067'),s('B','A','Confirmation','068')])
seq(18,'Internal cash settlement restriction creation',32,230,237,[8,9,10,21],('Third Party','third-party'),X,[s('B','A','StatusAdvice','067',True),s('B','A','Confirmation','068')],['P231 and the picture say Third Party; P235 and P237 say Instructing Party. Both explicit recipients are retained, without silently equating the roles.'])
seq(19,'Modification and cancellation transaction exchange',33,238,253,[11,12,13,22],P,X,[s('A','B','Instruction','066',color='black'),s('B','A','StatusAdvice','067',color='black'),s('A','B','ModificationRequest','072'),s('B','A','ModificationRequestStatusAdvice','073'),s('A','B','CancellationRequest','074'),s('B','A','CancellationRequestStatusAdvice','075')],['Long labels and some code suffixes are clipped in the local Word rendering. Their complete source text is preserved in the drawing text at P240; reconstructed labels recover that text. The picture supplies no alt frame making modification and cancellation alternatives, so none is invented.'])
seq(20,'Cancellation query and report exchange',35,256,266,[12,13,16,24],P,V,[s('A','B','CancellationRequest','074',color='black'),s('B','A','CancellationRequestStatusAdvice','075',True,'black'),s('A','B','CancellationQuery','082'),s('B','A','CancellationReport','083')],['Clipped source labels and code suffixes are recovered from the original drawing text P258.'])
seq(21,'Modification query and report exchange',36,269,280,[11,13,16,24],P,V,[s('A','B','ModificationRequest','072',color='black'),s('B','A','ModificationRequestStatusAdvice','073',True,'black'),s('A','B','ModificationQuery','080'),s('B','A','ModificationReport','081')],['The outgoing green query arrow has no visible text in the local Word render. Its exact name/code is retained in native source drawing text P271, and P277–P278 independently describe it. The reconstruction restores that supplied label and does not claim the local render displays it.'])
seq(22,'Event-triggered cancellation and modification reporting',37,282,296,[16,23],P,V,[('A','B','IntraBalanceMovementCancellationRequest (camt.074)<br/>IntraBalanceMovementModificationRequest (camt.072)',False,'black'),('B','A','IntraBalanceMovementCancellationRequestStatusAdvice (camt.075)<br/>IntraBalanceMovementModificationRequestStatusAdvice (camt.073)',True,'black'),s('B','A','CancellationReport','083'),s('B','A','ModificationReport','081')],['The complete rendered picture shows one request arrow and one dashed status arrow; the labels cover cancellation/modification variants. Both native source labels are preserved on those shared arrows, without adding unseen connectors. The modification-status label and code suffixes are clipped/overlapped in the local Word view but present at P284 and P291–P292.','The two report arrows are separate in the source. No query arrow is supplied in this event-triggered scenario.'])
seq(23,'Pending and posting report exchange',38,298,308,[17,18,25],P,X,[s('A','B','Instruction','066',color='black'),s('B','A','PendingReport','085',True),s('B','A','PostingReport','084',True)])
seq(24,'Movement query and response exchange',39,310,316,[14,15,26],P,X,[s('A','B','Query','078'),s('B','A','QueryResponse','079')])
