"""Direct source transcriptions of remaining settlement activities (25–32,36)."""
import re
def item(title,flows,table,code,notes=(),roles=None):
 return dict(title=title,kind='flowchart',flow_slugs=flows,roles=roles or ['instructing-party','executing-servicing-party'],table=table,code=code,notes=list(notes))

REMAINING={
25:item('Hold and release activity',['hold-release','released-held-released'],37,'''flowchart TB
  subgraph I["Instructing Party"]
    S@{shape: f-circ, label: " "} --> Create("Create Instruction")
    Create --> Monitor("Monitor Matching and Settlement Process")
    Monitor --> Needed{"Hold/Process needed?"}
    Needed -->|No| Monitor
    Needed -->|Yes| Choice{"Hold or Release?"}
    Monitor --> Settled{"Settled?"}
    Settled -->|No| Update("Update Status")
    Update --> Monitor
    Settled -->|Yes| Trade(["Settle trade"])
    Trade --> EndI@{shape: framed-circle, label: " "}
  end
  subgraph E["Executing/Servicing Party"]
    Release("Process Release Instruction") --> Join@{shape: fork, label: " "}
    Hold("Process Hold Instruction") --> Join
    Join --> Process("Processing, Matching and Settlement Process")
    Process --> ESettled{"Settled?"}
    ESettled -->|No| EUpdate("Update Status")
    EUpdate --> Process
    ESettled -->|Yes| ETrade(["Settle trade"])
    ETrade --- EndE@{shape: framed-circle, label: " "}
  end
  Create --> Process
  Choice -->|Release| Release
  Choice -->|Hold| Hold
  EUpdate --> Monitor
  classDef focus fill:#d1d8b8,stroke:#111,color:#111
  classDef context fill:#c0d1e5,stroke:#111,color:#111
  class Needed,Choice,Release,Hold focus
  class Create,Monitor,Settled,Update,Trade,Process,ESettled,EUpdate,ETrade context
''',['The source decision is labeled Hold/Process needed?, followed by Hold or Release?. Both labels are preserved, including the wording difference. The source return from executing-party Update Status goes to both its processing activity and the instructing-party monitor. The short executing-party end connector has no clear arrowhead and remains plain.']),
26:item('Other processing-change activity',['processing-change-one-transaction','processing-change-multiple-transactions'],38,'''flowchart TB
  subgraph I["Instructing Party"]
    S@{shape: f-circ, label: " "} --> Request("Request Modification")
    Request --> Monitor("Monitor modification request")
    Monitor --> ID{"Processed?"}
    ID -->|No| IE@{shape: framed-circle, label: " "}
    ID -->|Yes| IX("Update original transaction")
    IX --> IU(["Update Status of original instruction"])
    IU --> IE
  end
  subgraph E["Executing/Servicing Party"]
    Process("Process modification request") --> ED{"Processed?"}
    ED -->|No| Reject(["Reject"])
    ED -->|Yes| EX("Update original transaction")
    EX --> EU(["Update Status of original instruction"])
    Reject --> EE@{shape: framed-circle, label: " "}
    EU --> EE
    Reject --> Join@{shape: fork, label: " "}
    EU --> Join
  end
  Request --> Process
  Join --> Monitor
  classDef focus fill:#d1d8b8,stroke:#111,color:#111
  class Request,Monitor,ID,IX,IU,Process,ED,Reject,EX,EU focus
''',['The two source Processed? decisions are distinct: one is the executing party’s processing decision, the other the instructing party’s interpretation while monitoring. Both success and rejection paths and the source outcome bar are retained.']),
27:item('Modification before settlement activity',['modification-before-settlement'],39,'''flowchart TB
  subgraph I["Instructing Party"]
    S@{shape: f-circ, label: " "} --> Create("Create Instruction")
    Monitor("Monitor Matching and Settlement Process") --> Needed{"Modification needed?"}
    Needed -->|No| Monitor
    Needed -->|Yes| Request("Request Modification")
    IM("Monitor Modification Request") --> IV{"Validated?"}
    IV -->|Yes| IX("Update original transaction")
    IX --> Monitor
    IV -->|No| IP{"Pending?"}
    IP -->|Yes| IM
    IP -->|No| Monitor
  end
  subgraph E["Executing/Servicing Party"]
    Process("Processing, Matching and Settlement Process")
    Validate("Validation Modification request") --> VD{"Validated?"}
    VD -->|No| Reject(["Reject"])
    VD -->|Yes| Need{"Cpy response Needed"}
    Need -->|YES| Send("Send Status Advice")
    Need -->|No| EM("Monitor Modification Request")
    Send --> Status(["Provide Status on Modification"])
    EM --> Possible{"Update Possible"}
    Possible -->|No| Status
    Possible -->|YES| EX("Update original transaction")
    EX --> Status
    Reject --> Status
    Status --> Process
    Reject --> EndBar@{shape: fork, label: " "}
    EX --> EndBar
  end
  subgraph C["Counterparty"]
    Review("Review Status") --> Decision{"Response?"}
    Decision -->|YES| Response("Provide a response")
  end
  Create --> Process
  Request --> Validate
  Status --> IM
  Send --> Review
  Decision -->|No| EM
  Response --> EM
  classDef focus fill:#d1d8b8,stroke:#111,color:#111
  classDef context fill:#c0d1e5,stroke:#111,color:#111
  class Request,IM,IV,IX,IP,Validate,VD,Reject,Need,EM,Possible,EX,Status,Decision focus
  class Create,Monitor,Needed,Process,Send,Review,Response context
''',['The Counterparty lane is a separate participant instance. The matching sequence and P507–P514 identify the other instructing party; the generic role reference does not collapse both instances into one participant in this flow.','The source’s terminal horizontal bar has two incoming routes and no visible outgoing route. It is retained as a bar rather than replaced with an invented end state. The picture has no direct arrow from Request Modification to Monitor Modification Request; monitoring is entered from the returned modification status.','All validation, counterparty-response, pending and update-possible branches are retained. The enlarged connector inspection distinguishes line crossings with bridges from actual joins.']),
28:item('Modification after settlement activity',['modification-after-settlement'],40,'''flowchart TB
  subgraph I["Instructing Party"]
    S@{shape: f-circ, label: " "} --> Instruct("Instruct")
    IM("Monitor Matching and Settlement Process") --> IS{"Settled?"}
    IS -->|No| IU("Update Status")
    IU --> IM
    IS -->|Yes| IX(["Settle instruction"])
    IX --> Modification{"Modification?"}
    Modification -->|No| IE1@{shape: framed-circle, label: " "}
    Modification -->|Yes| Request("Request Modification")
    Request --> MM("Monitor modification request")
    MM --> MD{"Processed?"}
    MD -->|Yes| Update("Update original transaction")
    MD -->|No| Pending{"Pending?"}
    Pending -->|Yes| MM
    Pending -->|No| IE2@{shape: framed-circle, label: " "}
    Update --> IE2
  end
  subgraph E["Executing/Servicing Party"]
    EP("Process instruction") --> PD{"Processed?"}
    PD -->|No| PU("Update Status")
    PD -->|Yes| EM("Matching and Settlement Process")
    EM --> ES{"Settled?"}
    ES -->|No| EU("Update Status")
    EU --> EM
    ES -->|Yes| EX(["Settle instruction"])
    EX --> EModification{"Modification?"}
    EModification -->|No| EE1@{shape: framed-circle, label: " "}
    EModification -->|Yes| MP("Process modification request")
    MP --> Processed{"Processed?"}
    Processed -->|Yes| Original("Update original transaction")
    Processed -->|No| EPending{"Pending?"}
    EPending -->|Yes| Status("Provide Status on Modification")
    EPending -->|No| Reject(["Reject"])
    Reject --> Status
    Reject --> EE2@{shape: framed-circle, label: " "}
    Original --> Other("Other Process")
    Original --> Status
    Other --> Status
    Other --> EE2
  end
  Instruct --> EP
  PU --> Instruct
  EU --> IM
  EX --> IM
  Request --> MP
  Status --> MM
  classDef focus fill:#d1d8b8,stroke:#111,color:#111
  classDef context fill:#c0d1e5,stroke:#111,color:#111
  class Modification,Request,MM,MD,Update,Pending,EModification,MP,Processed,Original,EPending,Status,Reject,Other focus
  class Instruct,IM,IS,IU,IX,EP,PD,PU,EM,ES,EU,EX context
''',['Settlement is shown before the modification decision in both lanes. Other Process is deliberately generic in the source. No extra business meaning or message is assigned to it. All four end markers, pending loops and status-return routes remain separate.']),
29:item('Split settlement activity',['bilateral-splitting','unilateral-splitting'],41,'''flowchart TB
  subgraph C["Client"]
    S@{shape: f-circ, label: " "} --> CP("Instruction processing")
    CM("Monitor Settlement Process") --> CD{"Settled?"}
    CD -->|No| CU("Update Status")
    CU --> CM
    CD -->|Yes| CX(["Settle trade"])
    CX --> CE@{shape: framed-circle, label: " "}
  end
  subgraph I["Instructing Party"]
    IP("Instruction processing") --> Needed{"Split Needed?"}
    Needed -->|Yes| Split("Instruct Split")
    Needed -->|No| IM("Monitor Settlement Process")
    IM --> ID{"Settled?"}
    ID -->|No| IU("Update Status")
    IU --> IM
    ID -->|Yes| IX(["Settle trade"])
    IX --> IE@{shape: framed-circle, label: " "}
  end
  subgraph E["Executing Party"]
    EP("Instruction processing") --> EM("Matching and Settlement Process")
    ESplit("Execute Split") --> EM
    EM --> ED{"Settled?"}
    ED -->|No| EU("Update Status")
    EU --> EM
    ED -->|Yes| EX(["Settle trade"])
    EX --> EE@{shape: framed-circle, label: " "}
    EU --> Join@{shape: fork, label: " "}
    EX --> Join
  end
  CP --> IP
  IP --> EP
  CP -.- Split
  Split --> ESplit
  Join --> IM
  IU --> CM
  IX --> CM
  classDef focus fill:#d1d8b8,stroke:#111,color:#111
  classDef context fill:#c0d1e5,stroke:#111,color:#111
  class Needed,Split,ESplit focus
  class CP,CM,CD,CU,CX,IP,IM,ID,IU,IX,EP,EM,ED,EU,EX context
''',['The original dashed connection from the client’s Instruction processing to Instruct Split has no clear arrowhead and remains a dashed plain connection. It is distinct from the solid instruction-processing chain.','This activity picture has three lanes, whereas the detailed bilateral/unilateral sequences also show the opposite trade side and its client. The full flows retain those narrative/sequence participants.'],['split-settlement-client','instructing-party','instructing-splitting-party','executing-servicing-party']),
30:item('Allegement activity',['allegement'],42,'''flowchart TB
  subgraph I["InstructingParty"]
    Process("ProcessAllegement") --> Sent{"InstructionSentOrNot?"}
    Sent -->|Yes| Investigate("InvestigateAnd ContactCpty")
    Sent -->|No| Initiator{"InitiatorOrNot?"}
    Initiator -->|Yes| Instruct("Instruct")
    Initiator -->|No| Client("AllegeClient")
  end
  subgraph E["ServicingParty"]
    S@{shape: f-circ, label: " "} --> Allege("Allege")
    Match("ProcessingAnd MatchingProcess") --> Matched{"MatchedWithAlleged Instruction?"}
    Matched -->|Yes| Remove("RemoveAllegement")
    Matched -->|No| Cpty("AllegeCpty")
  end
  Allege --> Process
  Instruct --> Match
  Remove --> Process
''',['The source contains decision annotations (InstructionSentOrNot?, InitiatorOrNot?, MatchedWithAllegedInstruction?) attached to diamonds. They are placed inside native decision nodes here. Original compact activity names and Yes/No branches are retained.','The activity picture does not separately draw the alleged client or counterparty as swimlanes. The full flow and sequence retain the two instructing-party instances and the parties named in the narrative.']),
36:item('Portfolio transfer activity',['portfolio-transfer'],48,'''flowchart TB
  subgraph R["Executing/Servicing Party Receiving Custodian"]
    RP("Process the request to receive") --> RS("Send the receiving SettlementDetais")
    RR("Reconcile Delivering settlement Details") --> RD{"Any discrepancies?"}
    RD -->|No| RI("Instruct settlement Receipt Free to CSD")
    RI --> RE@{shape: framed-circle, label: " "}
    RD -->|Yes| RX("Investigate with customer")
    RX --> RD
  end
  subgraph D["Executing/Servicing Party Delivering Custodian"]
    DP("Process the request to deliver") --> DS("Send the delivering SettlementDetais")
    DR("Reconcile receiving settlement Details and possible position breaks with client") --> DD{"Any discrepancies?"}
    DD -->|No| DI("Instruct settlement Delivery Free to CSD")
    DI --> DE@{shape: framed-circle, label: " "}
    DD -->|Yes| DX("Investigate with customer")
    DX --> DD
  end
  subgraph C["Client"]
    S@{shape: f-circ, label: " "} --> Advise("Advise the move of position")
    Investigate("Discrepancies investigation") --> Advise
  end
  Advise --> RP
  Advise --> DP
  RS --> DR
  DS --> RR
  RX --> Investigate
  DX --> Investigate
  classDef focus fill:#d1d8b8,stroke:#111,color:#111
  classDef context fill:#c0d1e5,stroke:#111,color:#111
  class RS,RR,RD,RI,RX,DS,DR,DD,DI,DX,Investigate focus
  class RP,DP,Advise context
''',['The receiving and delivering custodians are two instances of Executing/Servicing Party. The Client starts the move and participates in discrepancy investigation; it is not the unlabeled Third Party in the separate portfolio sequence.','CSD is named in the settlement-instruction actions but is not drawn as a swimlane. Its participant reference remains linked. The original SettlementDetais spelling is retained in the two send-activity labels.'],['executing-servicing-party','portfolio-transfer-client','csd-icsd']),
}

def reporting(pull=False):
 if pull:
  return '''flowchart TB
  subgraph I["Instructing Party"]
    Request("Request statement")
    Reconcile("Reconciliation process") --> Investigate("Investigate and solve breaks")
  end
  subgraph E["Executing/Servicing Party"]
    Process("Process Request") --> PD{"Processed?"}
    PD -->|No| Update("Update Status")
    PD -->|Yes| Requested{"Statement requested?"}
    Requested --> TransSplit@{shape: fork, label: " "}
    TransSplit --> RT("Report Transactions")
    TransSplit --> RI("Report Intra-position movements")
    Requested --> HoldSplit@{shape: fork, label: " "}
    HoldSplit --> RC("Report holdings (custody)")
    HoldSplit --> RA("Report holdings (accounting)")
    Requested --> PendingSplit@{shape: fork, label: " "}
    PendingSplit --> RP("Report Pending Transaction")
    PendingSplit --> RL("Report Allegements")
    RT --> Holds@{shape: fork, label: " "}
    RI --> Holds
    RC --> Holds
    RA --> Holds
    RP --> Pending@{shape: fork, label: " "}
    RL --> Pending
  end
  Request --> Process
  Update --> Request
  Holds --> Reconcile
  Pending --> Reconcile
  classDef focus fill:#d1d8b8,stroke:#111,color:#111
  class Request,Reconcile,Investigate,Process,PD,Update,Requested,RT,RI,RC,RA,RP,RL focus
'''
 return '''flowchart TB
  subgraph I["Instructing Party"]
    subgraph IC["Settlement context"]
      S@{shape: f-circ, label: " "} --> Instruct("Instruct settlement")
      IM("Monitor Matching and Settlement Process") --> ID{"Settled?"}
      ID -->|No| IU("Update Status")
      IU --> IM
      ID -->|Yes| IX(["Settle instruction"])
    end
    subgraph IR["Reconciliation"]
      ReconcileP("Reconcile Pending Transaction Statuses") --> Investigate("Investigate and solve breaks")
      ReconcileH("Reconcile Holdings") --> Investigate
    end
  end
  subgraph E["Executing/Servicing Party"]
    subgraph EC["Settlement context"]
      Process("Process instruction") --> PD{"Processed?"}
      PD -->|No| PU("Update Status")
      PD -->|Yes| EM("Matching and Settlement Process")
      EM --> ED{"Settled?"}
      ED -->|No| EU("Update Status")
      EU --> EM
      ED -->|Yes| EX(["Settle instruction"])
      EX --- End@{shape: framed-circle, label: " "}
      EX --> Join@{shape: fork, label: " "}
      EU --> Join
      EX --> Fan@{shape: fork, label: " "}
    end
    subgraph ER["Reporting"]
      RT("Report Transactions") --> Holds@{shape: fork, label: " "}
      RI("Report Intra-position movements") --> Holds
      RC("Report holding (custody)") --> Holds
      RA("Report holdings (accounting)") --> Holds
      RP("Report Pending Transaction") --> Pending@{shape: fork, label: " "}
      RL("Report Allegements") --> Pending
    end
  end
  Instruct --> Process
  PU --> Instruct
  Join --> IM
  IU -.-> ReconcileP
  IX -.-> ReconcileH
  Fan -.-> RT
  Fan -.-> RI
  Fan -.-> RC
  Fan -.-> RA
  EU -.-> RP
  EU -.-> RL
  Holds --> ReconcileH
  Pending --> ReconcileP
  classDef focus fill:#d1d8b8,stroke:#111,color:#111
  classDef context fill:#c0d1e5,stroke:#111,color:#111
  class ReconcileP,ReconcileH,Investigate,RT,RI,RC,RA,RP,RL focus
  class Instruct,IM,ID,IU,IX,Process,PD,PU,EM,ED,EU,EX context
'''

REMAINING[31]=item('Reporting push activity',['reporting-push'],43,reporting(),['The source separates blue settlement context from green reporting/reconciliation by a horizontal dashed divider. Named nested groups here make that separation explicit; the group captions are explanatory, not additional source participants.','Dashed dependencies from settlement activities to reports/reconciliation remain dashed. The original bars and both reconciliation routes are retained. Reports are selected by account setup and narrative conditions; the bars do not mean every report must be sent on every occasion.','The source picture shows only instructing and executing/servicing lanes. The narrative also includes a Third Party for audit-trail reporting; its linked canonical participant and flow remain available.'],['instructing-party','executing-servicing-party','reporting-third-party'])
REMAINING[32]=item('Reporting pull activity',['reporting-pull'],44,reporting(True),['The source Statement requested? diamond distributes to three bars for transaction/intra-position, holdings and pending/allegement report categories. No Yes/No branch labels or default report are invented. Both result bars feed the reconciliation process.','The diagram shows only the two main parties. The full pull flow includes the Third Party named in the narrative and detailed sequence.'],['instructing-party','executing-servicing-party','reporting-third-party'])

for data in REMAINING.values():
 code=data['code']
 for shape,style in [('fork','fill:#111,stroke:#111'),('framed-circle','fill:#fff,stroke:#111,stroke-width:3px'),('f-circ','fill:#4472c4,stroke:#4472c4')]:
  nodes=re.findall(r'(\w+)@\{shape: '+shape+r',',code)
  if nodes:
   name=shape.replace('-','');code+='  classDef '+name+' '+style+'\n  class '+','.join(nodes)+' '+name+'\n'
 data['code']=code
