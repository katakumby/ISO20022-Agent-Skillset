"""Source380 transcriptions: direct original and whole Word-page inspection."""
from intrabalance_diagram_data import PREFIX
DATA={}
def row(n,title,page,start,end,tables,code,families=(),roles=('instructing-party','executing-servicing-party'),notes=()):
 DATA[n]=dict(title=title,page=page,start=start,end=end,tables=tables,code=code.strip()+'\n',families=list(families),roles=list(roles),notes=list(notes))
def sequence(n,title,page,start,end,steps,receiver,notes):
 code='%%{init: {"sequence": {"mirrorActors": false,"width": 250}}}%%\nsequenceDiagram\nparticipant A as Instructing Party\nparticipant B as '+receiver+'\n'
 for a,b,label,dash in steps:code+=a+('-->>' if dash else '->>')+b+': '+label+'\n'
 if n in (2,3):code+='Note over A,B: PUSH/PULL\n'
 import re
 row(n,title,page,start,end,[4,5,6,7,8],code,sorted(set(re.findall(r'semt\.\d{3}',code))),['instructing-party','executing-servicing-party']+(['servicing-party'] if n in (2,3) else []),notes);DATA[n]['steps']=steps;DATA[n]['receiver_label']=receiver
sequence(1,'Intra-position movement query, response and pending report',6,91,100,[('A','B','Intra Position Movement Query (semt.028)',False),('B','A','Intra Position Movement Query Response (semt.029)',False),('B','A','Intra Position Movement Pending Report (semt.034)',True)],'Executing/Servicing Party',['The first two messages are the pull query/response; the dotted pending-report arrow is an independently configured push report, not a compulsory third step after every query (P98–P99).','Source arrows distinguish query green, response black and pending report blue. Native sequence rendering retains labels and line styles; these colors are stated here rather than interpreted as extra message states.'])
sequence(2,'Settlement-condition modification request query and report',7,101,110,[('A','B','Instruct Settlement Condition Modification Request (sese.030)',False),('B','A','Report processing status (sese.031)',True),('A','B','Request Securities Settlement Modification Request Query (semt.030)',False),('B','A','Provide Securities Settlement Modification Report (semt.031)',False)],'Servicing Party',['The original green arrows are query/report scope; black instruction/status arrows provide the preceding business context. Exact versions of context families sese.030 and sese.031 are not supplied by this figure and are not guessed.','P108 describes pull retrieval of a previously sent modification request. P109 separately describes delta or full push reporting configured by subscription. PUSH/PULL belongs to the report arrow; no mandatory query is inferred for a push report.'])
sequence(3,'Transaction cancellation request query and report',8,111,119,[('A','B','Instruct Securities Transaction Cancellation Request (sese.020)',False),('B','A','Report processing status (sese.027)',True),('A','B','Request Securities Transaction Cancellation Request Query (semt.032)',False),('B','A','Securities Transaction Cancellation Report (semt.033)',False)],'Servicing Party',['The original green arrows are query/report scope; black cancellation/status arrows provide context. Exact versions of context families sese.020 and sese.027 are not identified in this picture.','The query/report concerns previously sent cancellation instructions for settlement or intra-position movements (P117). It is not a settlement reversal. P119 requires the Business Application Header family head.001 without choosing an exact version.','P117 supports either pull or push. No query is inferred as a prerequisite for an independently configured push report.'])
row(4,'Settlement Restrictions business-area, role and process scope',13,232,247,[5,6,7],PREFIX+'''A(["«BusinessArea» SettlementAndReconciliation"]):::grey
C["«FinancialInstitution» CSDParticipant"]:::grey
P["«BusinessActor» CentralCounterparty"]:::grey
D["«FinancialInstitution» CentralSecuritiesDepository"]:::grey
Y["«System» SystemApplication"]:::grey
PR(["«Processes»"]):::blue
I["Instruction"]:::blue
CF["Confirmation"]:::blue
R["Reconciliation"]:::green
M{"Modification Request"}:::blue
X{"Cancellation Request"}:::blue
S(["«Status reporting»"]):::blue
Q(["«Query / Response»"]):::green
RP(["«Reporting»"]):::green
A --> C
A --> P
A --> D
A --> Y
A -.- PR
PR -.-> I
PR -.-> CF
PR -.-> R
I -.-> M
I -.-> X
M -.-> S
X -.-> S
CF -.-> S
R -.-> Q
R -.-> RP
''',roles=['csd-participant','central-counterparty','central-securities-depositories-csd','system-application','instructing-party','executing-servicing-party','settlement-infrastructure','direct-connected-participant-dcp','t2s-operator'],notes=['This is a mixed business-area/process-scope figure, not an ordered transaction. Flowchart notation preserves the source rectangles, diamonds, ellipses, stereotype labels and solid/dashed edge semantics. Actor pictograms are replaced by labeled boxes; no inheritance or institutional equivalence is inferred from the outbound area arrows.','Only green reconciliation/query/reporting processes are in this message set; blue instruction, confirmation, modification, cancellation and status reporting provide context (P238). The diamonds label requests in this scope map; no runtime decision condition is invented.','P233–P235 distinguish entities from functional roles but then reuse the BusinessRole label for functional examples. Source wording is retained with the registered source issue.'])
row(5,'Settlement and reconciliation high-level process relationships',16,248,254,[8],'''usecase-beta
direction TB
R["Settlement & Reconciliation"]
I("Instruction")
S("Status reporting")
C("Confirmation")
RC("Reconciliation")
M("Modification")
X("Cancellation request")
RV("Reversal")
RP("Reporting")
Q("Query / Response")
R --> I
R --> S
R --> C
R --> RC
I --> M
I --> X
M --> S
X --> S
C --> S
C --> RV
RC --> RP
RC --> Q
style RC fill:#85f4c5,stroke:#222,color:#000
style RP fill:#85f4c5,stroke:#222,color:#000
style Q fill:#85f4c5,stroke:#222,color:#000
style R fill:#bfd4ee,stroke:#222,color:#000
style I fill:#bfd4ee,stroke:#222,color:#000
style S fill:#bfd4ee,stroke:#222,color:#000
style C fill:#bfd4ee,stroke:#222,color:#000
style M fill:#bfd4ee,stroke:#222,color:#000
style X fill:#bfd4ee,stroke:#222,color:#000
style RV fill:#bfd4ee,stroke:#222,color:#000
''',notes=['Native Mermaid12 use-case notation preserves the source process ellipses and rectangular root. Ordinary directed associations retain the source arrow direction; no include/extend or inheritance relation is invented.','Green reconciliation/reporting/query-response are in scope; the other blue processes provide context (P249). Confirmation connects to Reversal and Status reporting. Cancellation request connects to Status reporting; it is not equated with Reversal.','T8 gives query and scheduled-system-event triggers, existing instructions within the party’s scope and matching criteria, and Static Data privileges for reports. It states postconditions None, rather than an inferred settlement outcome.'])
row(10,'Pull-mode intra-position movement query processing',17,259,262,[8,10],PREFIX+'''subgraph A["Instructing Party"]
S@{ shape: f-circ, label: " " }
Q("Query Intra-Position Movement Instructions"):::green
M("Monitor"):::green
R("Reconcile"):::blue
E@{ shape: fr-circ, label: " " }
end
subgraph B["Servicing/Executing Party"]
P("Process Query"):::green
D{"Processed?"}:::green
ER("Error Processing"):::green
SE("Send Error Response"):::green
SR("Send Intra Pos Movemenrt Instruction Response"):::green
J[" "]:::bar
end
S --> Q --> P --> D
D -->|No| ER --> SE --> J
D -->|Yes| SR --> J
J --> M --> R --> E
''',['semt.028','semt.029'],['instructing-party','executing-servicing-party','servicing-executing-party'],['The literal source response label spells Movemenrt; it is not silently corrected. The source vertical bar and converging error/response lines remain explicit. T9 defines a bar as parallel initiation, but the source drawing uses it where these branches converge; no new concurrent business action is inferred.','T10 includes technical and business validation, operational error preparation, routing the response, monitoring and external reconciliation. Business errors may use sese.022 under P284; no exact sese.022 version is inferred.'])
row(11,'Push-mode pending intra-position movement reporting',19,263,265,[8,11],PREFIX+'''subgraph A["InstructingParty"]
M("Monitor"):::green
R("Reconcile"):::blue
EA@{ shape: fr-circ, label: " " }
end
subgraph B["ServicingExecutingParty"]
S@{ shape: f-circ, label: " " }
T("SystemEvent Triggered"):::blue
D{"Report Required"}:::green
EN@{ shape: fr-circ, label: " " }
G("Generate Report"):::green
V{"Success"}:::green
ER("Error Processing"):::blue
EE@{ shape: fr-circ, label: " " }
RP("Report Pending Instructions"):::green
end
S --> T --> D
D -->|No| EN
D -->|Yes| G --> V
V -->|No| ER --> EE
V -->|Yes| RP --> M --> R --> EA
''',['semt.034'],['instructing-party','executing-servicing-party','servicing-executing-party'],['Source lane labels omit spaces/slashes; these literal labels remain in the picture while T11 supplies Executing/Servicing Party responsibilities.','Reporting depends on subscription rules in Static Data. No-report and failed-generation branches terminate locally; no error message is added to these push paths. P216 allows full or delta; P217 defines the T2S delta contents as new pending instructions or pending instructions modified/cancelled since the previous report.'])
row(12,'Pull-mode cancellation or modification query processing',20,268,271,[8,12],PREFIX+'''subgraph A["Instructing Party"]
Q("Send Settlement/IntraPosition Movement Cancellation/Modification Query"):::green
M("Monitor"):::green
R("Reconcile")
E@{ shape: fr-circ, label: " " }
end
subgraph B["Servicing Party"]
V("Validate Request"):::green
D{"Successful Process?"}:::green
ER("Error Processing")
SE("Send Error Response")
SR("Send Settlement/IntraPosition Movement Cancellation/ModificationResponse"):::green
end
Q --> V --> D
D -->|No| ER
ER -->|Yes| SE --> M
D -->|Yes| SR --> M
M --> R --> E
''',['semt.030','semt.031','semt.032','semt.033'],['instructing-party','executing-servicing-party','servicing-party'],['The source has no start glyph and places a literal Yes label between Error Processing and Send Error Response; this is preserved without inventing another decision. The successful source node says Response, while the activity table calls the output Report.','T12 applies technical and business validation and operational-error processing to queries about earlier cancellation/modification requests. It does not itself cancel or modify the underlying instruction. Business-error message family sese.022 is cited in P291/P302 without an exact version.'])
row(13,'Push-mode cancellation or modification report processing',22,272,275,[8,13],PREFIX+'''subgraph A["Instructing Party"]
M("Monitor"):::green
R("Reconcile")
EA@{ shape: fr-circ, label: " " }
end
subgraph B["Servicing Party"]
S@{ shape: f-circ, label: " " }
T("System Event Triggered")
D{"Report Required"}:::green
EN@{ shape: fr-circ, label: " " }
G("Generate Report"):::green
V{"Successful Process?"}:::green
ER("Error Processing")
EE@{ shape: fr-circ, label: " " }
RP("Send Settlement/ Intra Position Movement Cancellation/Modification Report"):::green
end
S --> T --> D
D -->|No| EN
D -->|Yes| G
G -->|Yes| V
V -->|No| ER --> EE
V --> RP --> M --> R --> EA
''',['semt.031','semt.033'],['instructing-party','executing-servicing-party','servicing-party'],['The Yes label is printed before the Successful Process? decision, on the Generate Report arrow; its success branch has no label. The reconstruction preserves this placement.','T13 checks subscription rules, generates matching previously received cancellation/modification instructions and ends locally when no report is required or generation fails. Configured report scopes and delta criteria are detailed in P297/P307; no query prerequisite is inferred.'])
row(14,'Transaction reconciliation in instruction, cancellation and modification context',24,276,281,[8],PREFIX+'''S@{ shape: f-circ, label: " " }
I["Settlement or Intra-Position Movement Instruction"]:::blue
D{" "}:::blue
C["Cancellation request"]:::blue
M["Modification Request"]:::blue
J[" "]:::bar
SR["Status reporting"]:::blue
R["Reconciliation"]:::green
E@{ shape: fr-circ, label: " " }
S --> I
I --> SR
I --> D
D -->|Cancellation needed| C --> J
D -->|Modification needed| M --> J
J --> SR --> R --> E
''',roles=['instructing-party','executing-servicing-party'],notes=['This diagram supplies transaction context, not an exact message sequence. The direct instruction-to-status path and the two request paths are distinct; it supplies no reversal node or requirement to execute both requests.','P278 says reconciliation covers pending and posted transactions using associated data. The diagram’s bar is retained without adding execution semantics beyond the source legend. Green reconciliation is in scope; blue surrounding actions provide context.'])
