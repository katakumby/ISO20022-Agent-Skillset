"""Directly inspected source status charts; source 196, figures 19–24."""

ROLES=['instructing-party','executing-servicing-party']
def entry(title,flows,code,notes):
 return dict(title=title,kind='flowchart',flow_slugs=flows,roles=ROLES,table=None,code=code,notes=notes)

STATUS={
19:entry('Settlement instruction status processes',['instruction-confirmation'],'''flowchart TB
  subgraph Common["COMMON"]
    S@{shape:f-circ,label:" "}
    T["Technical and business validation Process?"]
    A{"Accepted for further processing?"}
    RR{"Rejection or Repair"}
    Repair@{shape:doc,label:"Repair Status"}
    Reject@{shape:doc,label:"Rejection Status"}
    Accepted@{shape:doc,label:"Accepted status"}
    S ==> T
    T -->|Y| A
    A -->|Y| Accepted
    A -->|N| RR
    RR -->|Repair| Repair
    Repair --> A
    RR -->|Rejection| Reject
  end
  subgraph Intermediary["INTERMEDIARY"]
    R1@{shape:sm-circ,label:" "}
    IP["Internal Further Processing?"]
    Pending{"Pending?"}
    PP@{shape:doc,label:"Pending Processing Status"}
    Next@{shape:doc,label:"Next Status"}
    R2@{shape:sm-circ,label:" "}
    IM["Inferred Matching Process?"]
    ID{"Matched?"}
    IU@{shape:doc,label:"Inferred Unmatched Status"}
    IMatched@{shape:doc,label:"Inferred Matched"}
    R1 ==> IP
    IP -->|Y| Pending
    IP -->|N| R2
    Pending -->|Y| PP
    PP --> Pending
    Pending -->|N| Next
    Pending -->|N| ID
    Next --> R2
    R1 ==> R2
    R2 ==> IM
    IM -->|Y| ID
    ID -->|N| IU
    IU --> Next
    ID -->|Y| IMatched
  end
  subgraph Market["MARKET STATUS"]
    R3@{shape:sm-circ,label:" "}
    MP["Matching Process?"]
    MD{"Matched?"}
    Unmatched@{shape:doc,label:"Unmatched Status"}
    Matched@{shape:doc,label:"Matched"}
    R4@{shape:sm-circ,label:" "}
    SP["Settlement Process?"]
    Date{"Before or After instructed settlement date?<br/>(See chapter 7)"}
    PD{"Pending?"}
    Ready@{shape:doc,label:"Ready for settlement"}
    PR@{shape:doc,label:"Pending reason"}
    FD{"Failing?"}
    Recycled@{shape:doc,label:"Recycled"}
    FR@{shape:doc,label:"Failing reason"}
    Done[["Settlement Confirmation"]]
    R3 ==> MP
    MP -->|Y| MD
    MP -->|N| R4
    MD -->|Y| Matched
    MD -->|N| Unmatched
    Matched --> R4
    R3 ==> R4
    R4 ==> SP
    SP -->|Y| Date
    SP -->|N| Done
    Date -->|Before| PD
    PD -->|N| Ready
    PD -->|Y| PR
    PR --> PD
    Date -->|After| FD
    FD -->|N| Recycled
    FD -->|Y| FR
    FR --> FD
    Ready ==> Done
    Recycled ==> Done
  end
  S ==> R1
  T -->|N| R1
  Accepted --> R1
  IMatched --> R3
  IM -->|N| R3
  ID -->|Y| MD
  R2 ==> R3
  Unmatched --> IMatched
  classDef process fill:#ddd,stroke:#111,color:#111
  class T,A,RR,IP,Pending,IM,ID,MP,MD,SP,Date,PD,FD process
''',[
'The message function is INST. Common status is potentially provided by all parties. Intermediary statuses are provided on processes performed at a party other than the CSD; market statuses concern processes at the CSD. For a transaction settled at an intermediary (for example an internal transfer), market statuses are sent, according to the source note.',
'Internal Further Processing and Inferred Matching may run in parallel. Inferred matching is not official; the account servicer may deduce it from allegement-report analysis. It is not a market matching status.',
'A market matching status is an official matching status from the CSD. Matching and settlement may run in parallel; in that parallel process, an unmatched trade has only pending/failing status or reason pertaining to the account owner, not the counterparty.',
'The source states that PENDING changes to FAILING at END of Settlement Date. A matched instruction that is pending/failing may become unmatched again, for example after cancellation from a counterparty.',
'The source uses a heavy vertical process spine, document-shaped status outputs, feedback paths and COMMON / INTERMEDIARY / MARKET STATUS boundaries. Native layout reflows the spine, without turning the parallel-process notes into a mandatory serial algorithm. Small unlabeled junctions are routing points, not participants or added business activities.',
]),
20:entry('Cancellation-request status processes',['cancellation-request'],'''flowchart TB
  subgraph I["INTERMEDIARY STATUS"]
    S@{shape:f-circ,label:" "}
    T["Technical and business validation Process?"]
    A{"Accepted for further processing?"}
    Reject@{shape:doc,label:"Rejection Status"}
    Accepted@{shape:doc,label:"Accepted status"}
    R@{shape:sm-circ,label:" "}
    IP["Internal Processing?"]
    P{"Pending?"}
    PS@{shape:doc,label:"Pending Status"}
    D{"Denied?"}
    DS@{shape:doc,label:"Denied Status"}
    S ==> T
    T -->|Y| A
    A -->|N| Reject
    A -->|Y| Accepted
    T -->|N| R
    Accepted --> R
    S ==> R
    R ==> IP
    IP -->|Y| P
    P -->|Y| PS
    PS --> P
    P -->|N| D
    D -->|Y| DS
  end
  subgraph M["MARKET STATUS"]
    MR@{shape:sm-circ,label:" "}
    B["Bilateral cancellation needed?"]
    Both{"Both received?"}
    Await@{shape:doc,label:"Awaiting counterparty cancellation"}
    Done@{shape:doc,label:"Cancellation request executed"}
    MR ==> B
    B -->|Y| Both
    B -->|N| Done
    Both -->|N| Await
    Await --> Both
    Both -->|Y| Done
  end
  R ==> MR
  IP -->|N| MR
  D -->|N| MR
''',['Intermediary and market status boundaries, rejection, accepted, pending, denied and bilateral-cancellation paths are retained. Pending returns to its decision; awaiting counterparty cancellation returns to Both received?. Neither accepted status nor pending status means the cancellation request has been executed. Small unlabeled junctions reproduce the original process spine.']),
21:entry('Cancellation status and reason',['cancellation-advice'],'''flowchart TB
  S@{shape:f-circ,label:" "} --> C["Cancelled by Executing Party?"]
  C -->|Y| O@{shape:doc,label:"Cancellation Status and Reason"}
  C -->|N| C
''',['The source shows one process box, a Y route to Cancellation Status and Reason, and an N loop back to the same process. Its label does not itself distinguish every cancellation-message type; see the linked flow’s documented source conflict.']),
22:entry('Intra-position instruction status processes',['intra-position-instruction'],'''flowchart TB
  S@{shape:f-circ,label:" "}
  T["Technical and business validation Process?"]
  A{"Accepted for further processing?"}
  Reject@{shape:doc,label:"Rejection Status"}
  Accepted@{shape:doc,label:"Accepted status"}
  R@{shape:sm-circ,label:" "}
  IP["Internal Processing?"]
  P{"Pending?"}
  PS@{shape:doc,label:"Pending Status"}
  Done[["Intra-position advice"]]
  S ==> T
  S ==> R
  T -->|Y| A
  T -->|N| R
  A -->|N| Reject
  A -->|Y| Accepted
  Accepted --> R
  R ==> IP
  IP -->|Y| P
  IP -->|N| Done
  P -->|Y| PS
  PS --> P
  P -->|N| Done
''',['All source branches are retained, including bypassing technical validation and internal processing when the corresponding process box has an N branch. The bottom label is the source’s generic Intra-position advice; no exact message identifier is inferred from that label alone.']),
23:entry('Statement or status query validation',['reporting-pull'],'''flowchart TB
  S@{shape:f-circ,label:" "} ==> T["Technical and business validation Process?"]
  T -->|Y| A{"Accepted for further processing?"}
  T -->|N| Done[["Requested statement or status"]]
  A -->|N| Reject@{shape:doc,label:"Rejection Status"}
  A -->|Y| Done
''',['The source has no accepted-status output for this chart. Acceptance routes to Requested statement or status, while non-acceptance routes to Rejection Status.']),
24:entry('Modification-request status processes',['processing-change-one-transaction','processing-change-multiple-transactions','modification-before-settlement','modification-after-settlement'],'''flowchart TB
  S@{shape:f-circ,label:" "}
  T["Technical and business validation Process?"]
  A{"Accepted for further processing?"}
  Reject@{shape:doc,label:"Rejection Status"}
  Accepted@{shape:doc,label:"Accepted status"}
  R@{shape:sm-circ,label:" "}
  IP["Internal Processing?"]
  P{"Pending?"}
  PS@{shape:doc,label:"Pending Status"}
  Done["Modification process"]
  S ==> T
  S ==> R
  T -->|Y| A
  T -->|N| R
  A -->|N| Reject
  A -->|Y| Accepted
  Accepted --> R
  R ==> IP
  IP -->|Y| P
  IP -->|N| Done
  P -->|Y| PS
  PS --> P
  P -->|N| Done
''',['The final box is Modification process, not a confirmation of completed modification. Rejection, accepted and pending outputs and the pending feedback route are retained.']),
}
