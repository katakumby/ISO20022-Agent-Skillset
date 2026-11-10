"""Manually transcribed financing/pair-off/split activity pictures 13–18."""
def entry(title,flow,roles,table,code,notes=()):
 return dict(title=title,kind='flowchart',flow_slugs=[flow],roles=roles,table=table,code=code,notes=list(notes))

def monitor(p,verb):
 return f'''    {p}M("{verb}")
    {p}U("Update Status")
    {p}OD{{"Opening Settled?"}}
    {p}CD{{"Closing settled?"}}
    {p}OS(["Settle Opening"])
    {p}CS(["Settle Closing"])
    {p}SJ@{{shape: fork, label: " "}}
    {p}OJ@{{shape: fork, label: " "}}
    {p}End@{{shape: framed-circle, label: " "}}
    {p}M --> {p}OD
    {p}OD -->|No| {p}SJ
    {p}OD -->|Yes| {p}OS
    {p}OS --> {p}CD
    {p}CD -->|No| {p}SJ
    {p}CD -->|Yes| {p}CS
    {p}SJ --> {p}U
    {p}U --> {p}M
    {p}OS --> {p}OJ
    {p}CS --> {p}OJ
    {p}CS --> {p}End
'''

def finance(two=False):
 left='Settlement Instructing Party' if two else 'Securities Financing Instructing Party'
 right='Securities Financing Servicing Party/Settlement Executing Party' if two else 'Securities Financing Servicing Party'
 code=f'''flowchart TB
  subgraph I["{left}"]
    IS@{{shape: f-circ, label: " "}}
    IA("Instruct securities financing transaction")
    IS --> IA
'''+monitor('I','Monitor securities financing transaction')+'''    IOJ --> IU
  end
'''+f'''  subgraph B["{right}"]
    BP("Process instruction")
    BD{{"Processed?"}}
    BR("Update Status")
    BP --> BD
    BD -->|No| BR
'''
 if two:
  code+='''    BA("Create Securities Financing Transactions")
    BO("Process opening leg")
    BC("Process closing leg")
    BA --> BO
    BA --> BC
    BO --> BM
    BC --> BM
'''
 else:code+='    BA("Instruct settlement and monitor")\n'
 code+='    BD -->|Yes| BA\n'+monitor('B','Manage securities financing transaction' if two else 'Monitor securities financing transaction')+'  end\n'
 if not two:
  code+='''  subgraph C["Settlement Executing Party"]
    CO("Process instruction")
    CC("Process instruction")
    CD{"Processed?"}
    CR("Update Status")
    CM("Matching and Settlement Process")
    CS{"Settled?"}
    CU("Update Status")
    CX(["Settle instruction"])
    CE@{shape: framed-circle, label: " "}
    CO --> CD
    CC --> CD
    CD -->|No| CR
    CD -->|Yes| CM
    CM --> CS
    CS -->|No| CU
    CU --> CM
    CS -->|Yes| CX
    CX --> CE
  end
  BA -->|Opening leg| CO
  BA -->|Closing leg| CC
  CR --> BA
  CU -->|Opening Statuses / Closing Statuses| BM
  CX -->|Opening Settlement / Closing Settlement| BM
'''
 code+='''  IA --> BP
  BR --> IA
  BU --> IM
  BOJ --> IM
  classDef main fill:#d1d8b8,stroke:#111,color:#111
  classDef context fill:#c0d1e5,stroke:#111,color:#111
  class IA,IM,IOD,ICD,IOS,ICS,BP,BD,BA,BM,BOD,BCD,BOS,BCS main
  class IU,BU,BR context
'''
 if two:code+='  class BO,BC context\n'
 else:code+='  class CO,CC,CD,CR,CM,CS,CU,CX context\n'
 return code

def modification(two=False):
 name='Securities Financing Servicing Party/Settlement Executing Party' if two else 'Securities Financing Servicing Party'
 code='''flowchart TB
  subgraph I["Securities Financing Instructing Party"]
    IS@{shape: f-circ, label: " "} --> IA("Request modification")
    IM("Monitor modification request") --> ID{"Modified?"}
    ID -->|No| IE@{shape: framed-circle, label: " "}
    ID -->|Yes| IX("Modify securities financing transaction")
  end
'''+f'''  subgraph B["{name}"]
    BP("Process Modification") --> BD{{"Processed?"}}
    BD -->|No| BR("Update Status")
    BD -->|Yes| BX("Replace closing leg")
    BX --> BU("Update Status")
    BU --> BE@{{shape: framed-circle, label: " "}}
'''
 if two:code+='    BX --> CM("Matching and Settlement Process")\n  end\n'
 else:code+='''  end
  subgraph C["Settlement Executing Party"]
    CP("Process instruction") --> CD{"Processed?"}
    CD -->|No| CU("Update Status")
    CD -->|Yes| CM("Matching and Settlement Process")
  end
  BX --> CP
  CU --> BX
'''
 code+='''  IA --> BP
  BR --> IA
  BU --> IM
  classDef main fill:#d1d8b8,stroke:#111,color:#111
  classDef context fill:#c0d1e5,stroke:#111,color:#111
  class IA,IM,ID,IX,BP,BD,BX main
  class BR,BU,CM context
'''
 if not two:code+='  class CP,CD,CU context\n'
 return code

FINANCING={
13:entry('Financing instruction activity — three parties','financing-instruction-three-parties',['financing-instructing-party','financing-servicing-party','settlement-executing-party'],31,finance(),['Separate opening and closing instructions feed the settlement executing party. Opening and closing settlement checks, both status loops and four source bars remain distinct. The source outcome bars connect opening/closing outcomes onward without asserting that mutually exclusive routes must complete together.']),
14:entry('Financing instruction activity — two parties','financing-instruction-two-parties',['financing-instructing-party','financing-servicing-settlement-executing-party'],32,finance(True),['The picture labels its left lane Settlement Instructing Party; the activity table uses Securities Financing Instruction Party, and the two-party sequence uses Securities Financing Instructing Party. The picture label is preserved. The linked financing participant is contextual, not a new unsupported global synonym.','The combined servicing/executing participant creates and processes both opening and closing legs. Both participants separately monitor opening and closing settlement, with source bars and return paths retained.']),
15:entry('Financing modification activity — three parties','financing-modification-three-parties',['financing-instructing-party','financing-servicing-party','settlement-executing-party'],33,modification(),['The modification picture concerns replacement of the closing leg. Modified? No reaches an endpoint; Yes reaches Modify securities financing transaction. No further outgoing edge from that activity is invented. The settlement executing party’s matching/settlement process remains a separate lane.']),
16:entry('Financing modification activity — two parties','financing-modification-two-parties',['financing-instructing-party','financing-servicing-settlement-executing-party'],34,modification(True),['The combined servicing/executing party replaces the closing leg and enters matching/settlement processing. The source picture does not add an endpoint after Modify securities financing transaction or Matching and Settlement Process.']),
17:entry('Pair-off activity','pair-off',['instructing-party','executing-servicing-party'],35,'''flowchart TB
  subgraph I["Instructing Party"]
    S@{shape: f-circ, label: " "} --> II("Instruct settlement(s)")
    IP("Pair-off")
    IM("Monitor and settle Pair-off")
  end
  subgraph E["Executing/Servicing Party"]
    EP("Process instruction(s)") --> ED{"Processed?"}
    ED -->|No| ER("Update Status")
    ED -->|Yes| EM("Matching and Settlement Process")
    PP("Process Pair-off") --> PD{"Processed?"}
    PD -->|No| PR("Update Status")
    PD -->|Yes| PC("Cancel paired-off instructions")
    PC --> EM
    EM --> Cash("Wire or receive cash difference")
    Cash --> End@{shape: framed-circle, label: " "}
  end
  II --> EP
  ER --> II
  IP --> PP
  PR --> IP
  Cash --> IM
  classDef main fill:#d1d8b8,stroke:#111,color:#111
  classDef context fill:#c0d1e5,stroke:#111,color:#111
  class IP,IM,PP,PD,PR,PC,Cash main
  class II,EP,ED,ER,EM context
''',['The original settlement-processing branch is blue context; the pair-off/cancellation/cash-difference branch is green foreground. The cash difference may be wired or received, as the source activity explicitly states. No particular payment message is inferred.']),
18:entry('Cash/securities split activity','cash-securities-split',['instructing-party','cash-securities-split-servicing-party','securities-leg-executing-party','cash-leg-executing-party'],36,'''flowchart TB
  subgraph I["Instructing Party"]
    IA("Instruct a securities/cash split settlement")
    IM("Monitor Matching and Settlement Process") --> ID{"Settled?"}
    ID -->|No| IU("Update Status")
    IU --> IM
    ID -->|Yes| IX(["Settle trade"])
  end
  subgraph E["Securities-cash instruction Executing party"]
    Split("Split securities/cash instruction")
    In@{shape: fork, label: " "} --> Monitor("Monitor securities and cash settlement process")
    Monitor --> CashD{"Cash Settled?"}
    CashD -->|No| U("Update Status")
    CashD -->|Yes| SecD{"Securities Settled?"}
    SecD -->|No| U
    SecD -->|Yes| Trade(["Settle trade"])
    U --> Monitor
    U --> Out@{shape: fork, label: " "}
    Trade --> Out
  end
  subgraph SL["Securities leg executing party"]
    SP("Processing, matching and settlement of securities leg") --> SD{"Settled?"}
    SD -->|No| SU("Update Status")
    SU --> SP
    SD -->|Yes| SX(["Settle Securities"])
  end
  subgraph CL["Cash leg executing party"]
    CP("Process cash leg") --> CX(["Settle Cash"])
  end
  IA --> Split
  Split --> SP
  Split --> CP
  SU --> In
  SX --> In
  CX --> In
  Out --> IM
  classDef main fill:#d1d8b8,stroke:#111,color:#111
  classDef context fill:#c0d1e5,stroke:#111,color:#111
  class IA,Split,Monitor,CashD,SecD,U,Trade main
  class IM,ID,IU,IX,SP,SD,SU,SX,CP,CX context
''',['Four source swimlanes, separate cash/securities execution and both source bars are retained. Cash Settled? is checked before Securities Settled? in the source picture. No new start/end markers or cash-message identifiers are added. The activity’s Securities-cash instruction Executing party is linked to its cash/securities split scenario role, retaining the source label.']),
}

import re
for data in FINANCING.values():
 code=data['code']
 for shape,style in [('fork','fill:#111,stroke:#111'),('framed-circle','fill:#fff,stroke:#111,stroke-width:3px'),('f-circ','fill:#4472c4,stroke:#4472c4')]:
  nodes=re.findall(r'(\w+)@\{shape: '+shape+r',',code)
  if nodes:
   name=shape.replace('-','')
   code+='  classDef '+name+' '+style+'\n  class '+','.join(nodes)+' '+name+'\n'
 data['code']=code
