"""Source377 figure transcriptions inspected against originals and Word composites."""
from intrabalance_diagram_data import PREFIX
DATA={}
def row(n,title,page,start,end,tables,code,families=(),roles=('instructing-party','executing-servicing-party'),notes=()):
 DATA[n]=dict(title=title,page=page,start=start,end=end,tables=tables,code=code.strip()+'\n',families=list(families),roles=list(roles),notes=list(notes))
row(1,'Securities reference-data business roles and functional participants',11,133,142,[5,6,7],'''usecase-beta
direction LR
actor I("Instructing party")
actor E("Executing/Servicing Party")
actor C("CSD")
actor O("Corporate")
actor M("Market Infrastructure")
actor D("Market Data Provider")
C --> I
O --> I
M --> E
D --> E
''',roles=['instructing-party','executing-servicing-party','central-securities-depositories-csd','corporate','market-infrastructure','market-data-provider'],notes=['The four source institution labels are plain text pointing to two functional actor glyphs. Native Mermaid actors retain all six labels and directed assignments; extra actor glyphs are a notation adaptation, not new institutions or participant definitions. No inheritance, include/extend or system boundary is asserted.','P134–P135 distinguish BusinessRole entities from functional Participants, but P136 then calls user/debtor/creditor/investor examples of BusinessRoles. Literal source wording remains issue-000051; the many-to-many relationship is not collapsed.'])
row(2,'Securities reference-data high-level processes',13,143,150,[8,9,10,11,12],PREFIX+'''S@{ shape: dbl-circ, label: " " }
G["Generate Statement"]:::grey
Q["Query"]:::grey
C["Create Security"]:::grey
M["Modify Security"]:::grey
D["Delete Security"]:::grey
E@{ shape: dbl-circ, label: " " }
S --> G --> E
S --> Q --> E
S --> C --> E
S --> M --> E
S --> D --> E
''',notes=['Both original terminal symbols are hollow concentric circles; they are preserved as double circles rather than silently replaced with filled UML start/end glyphs.','The connectors share unmarked junction lines. No concurrency bar or decision is invented. P144 explicitly says this high-level scope is not exhaustive. The source paragraph P150 says General Statement, while the picture says Generate Statement.'])
ACT=PREFIX+'''subgraph A["Instructing Party"]
S@{ shape: f-circ, label: " " }
I("Instruction"):::green
J{" "}:::blue
N("Monitor"):::green
V{"Accepted"}:::blue
E@{ shape: fr-circ, label: " " }
end
subgraph B["Executing Party"]
C("Validate"):::green
D{"Accepted"}:::blue
P("Process"):::green
R("Report"):::green
end
S --> I --> C --> D
D -->|Yes| P
D -->|No| R
P -->|"Status «Accepted»"| J
R -->|"Status «Rejected»"| J
J --> N --> V
V -->|Yes| E
V -.->|No| I
'''
for n,title,page,start,end,tables,fams in [(7,'Security creation activity',15,154,155,[8,14],['reda.006','reda.008']),(8,'Security modification activity',17,156,158,[9,15],['reda.007','reda.029']),(9,'Security deletion activity',18,159,161,[10,16],['reda.013','reda.030'])]:
 row(n,title,page,start,end,tables,ACT,fams,['instructing-party','executing-party','executing-servicing-party'],['The source artwork uses Accepted/Rejected activity labels. The activity table and transaction messages distinguish COMPLETED, QUEUED and REJECTED. No equality of these separate status vocabularies is inferred.','Source edge labels are literally Status <<Accepted>> and Status <<Rejected>>. Mermaid uses typographic double-angle guillemets around the unchanged values because ASCII angle groups are stripped as HTML by this renderer.','The final No branch is dashed and returns to Instruction; the source does not supply a retry deadline or retry count. The blank diamond merges the accepted/rejected reporting paths without an added condition.','Executing Party is the literal swimlane label; corresponding table rows use Executing/Servicing Party. Scoped records retain that explicit contextual relationship.'])
for n,title,page,start,end,tables,process,response,fams in [(10,'Security query and audit-trail query activity',19,162,164,[11,17],'Process Query','Response',['reda.010','reda.012','reda.033','reda.034']),(11,'Security activity statement production',20,165,168,[12,18],'Process Statement','Reporting',['reda.009'])]:
 code=PREFIX+'''subgraph A["Instructing Party"]
I("Instruction"):::green
N("Monitor"):::green
end
subgraph B["Executing Party"]
P("'''+process+'''"):::green
R("'''+response+'''"):::green
end
I --> P --> R --> N
'''
 notes=['No start/end glyph or error decision is supplied in this activity picture. The linked table/narrative preserves additional error conditions without adding unseen diagram nodes.']
 if n==11:notes+=['T18 explicitly says the initial instruction is outside this process and no message is created for it. P315–P316 describe the statement as unilateral and unsolicited; no request message is inferred from the conceptual Instruction arrow.','T12 calls the recipient Recipient Party; the picture and transaction narrative call it Instructing Party. These source-scoped roles are linked without asserting global equivalence.']
 row(n,title,page,start,end,tables,code,fams,['instructing-party','executing-party','executing-servicing-party']+(['recipient-party'] if n==11 else []),notes)
def sequence(n,title,page,start,end,tables,steps,notes=()):
 code='%%{init: {"sequence": {"mirrorActors": false, "width": 230}, "themeVariables": {"actorBkg": "#bfd4ee", "actorBorder": "#222"}}}%%\nsequenceDiagram\nparticipant A as Instructing Party\nparticipant B as Executing/Servicing Party\n'
 for a,b,label,dash in steps:code+=a+('-->>' if dash else '->>')+b+': '+label+'\n'
 import re
 families=sorted(set(re.findall(r'reda\.\d{3}',code)))
 row(n,title,page,start,end,tables,code,families,notes=notes);DATA[n]['steps']=steps
for n,kind,request,status,page,start,end,tables,result in [(12,'Creation','006','008',22,172,183,[8,14],'COMPLETED'),(13,'Creation','006','008',23,185,206,[8,14],'REJECTED'),(14,'Maintenance','007','029',24,211,223,[9,15],'COMPLETED'),(15,'Maintenance','007','029',25,231,252,[9,15],'REJECTED'),(16,'Deletion','013','030',26,254,265,[10,16],'COMPLETED'),(17,'Deletion','013','030',27,270,292,[10,16],'REJECTED')]:
 steps=[('A','B',f'Security {kind} Request (reda.{request})',False),('B','A',f'Security {kind} Status Advice (reda.{status}): QUEUED',True),('B','A',f'Security {kind} Status Advice (reda.{status}): {result}',False)]
 notes=['The source shows QUEUED with a dashed connector; narrative says this status might be sent when processing is delayed, for example during a night-time cycle. The picture does not make queuing compulsory.','The narrative covers immediate validation rejection and re-validation after queuing, including multiple reasons, beyond the three pictured arrows. No second mandatory rejection is inferred.'] if result=='REJECTED' else ['The dashed QUEUED advice is conditional in the narrative, for example a running night-time cycle; the picture does not make it compulsory.']
 if n==14:notes+=['P217 says the instruction contains restriction type/timeframe inside security maintenance context. That source statement remains visible under issue-000051, without extending it to every maintenance request.']
 sequence(n,'Security '+kind.lower()+' — '+('confirmation' if result=='COMPLETED' else 'rejection'),page,start,end,tables,steps,notes)
sequence(18,'Security query and report exchange',28,294,302,[11,17],[('A','B','Security Query (reda.010)',False),('B','A','Security Report (reda.012): ERROR',True),('B','A','Security Report (reda.012)',False)],['The error path is conditional on excessive processing time, an unsuitable criteria combination or no result set (P300). The picture does not use an alt frame, so both literal arrows remain without declaring both responses mandatory. No timeout threshold is supplied.'])
sequence(19,'Securities audit-trail query and report exchange',28,303,310,[11,17],[('A','B','Securities Audit Trail Query (reda.033)',False),('B','A','Securities Audit Trail Report (reda.034): ERROR',True),('B','A','Securities Audit Trail Report (reda.034)',False)],['The query retrieves the complete audit trail on a specific security (P306). Error conditions and successful-result descriptions are alternatives in P308/P310, without a numeric timeout. No mandatory dual response is inferred.'])
sequence(20,'Unsolicited security activity advice',29,312,317,[12,18],[('B','A','Security Activity Advice (reda.009)',False)],['The source statement covers securities-reference-data changes during the business day and is sent unilaterally in an unsolicited manner (P315–P316). T12 requires a standing instruction; T18 says an initiating instruction is outside the message scope.'])
DATA[20]['roles'].append('recipient-party')
