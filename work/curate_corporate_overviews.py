from pathlib import Path
import json,sys
sys.path.insert(0,str(Path('tools').resolve()))
import kb
root=Path('.').resolve();s=next(s for s in kb.sources(root) if s['source_id']=='src-000079');out=root/s['set_path']/'diagrams'/'overview';out.mkdir(parents=True,exist_ok=True)
roles=['global-custodian','sub-custodian','stock-exchange','clearing-agent','icsd','csd','market-data-provider','institutional-investor','fund-manager','broker','beneficial-owner','account-servicer','account-owner']
codes={
'fig-0001':'''flowchart LR
  subgraph SERVICER["Account Servicer side"]
    S["Account Servicer"]
    SM["Market Data Provider"] --> S
    SB["Broker"] --> S
    SI["ICSD"] --> S
    SC["CSD"] --> S
    SX["Clearing"] --> S
    SS["Stock Exchange"] --> S
    SU["Sub Custodian"] --> S
    SG["Global Custodian"] --> S
  end
  subgraph OWNER["Account Owner side"]
    O["Account Owner"]
    OG["Global Custodian"] --> O
    OI["ICSD"] --> O
    OB["Broker"] --> O
    OF["Beneficial Owner"] --> O
    OM["Fund Manager"] --> O
    OC["CSD"] --> O
    OS["Sub Custodian"] --> O
    ON["Institutional Investor"] --> O
  end
''',
'fig-0002':'''flowchart TB
  ROOT["Corporate Actions processes"]
  ROOT --- EV(["Event Notification"])
  ROOT --- BAL(["Balance/Entitlement Notification"])
  ROOT --- REM(["Reminder"])
  ROOT --- ELE(["Election"])
  ROOT --- PRE(["Movement Preliminary Advice"])
  ROOT --- CON(["Movement Confirmation"])
  ROOT --- REV(["Movement Reversal"])
  ROOT --- CAN(["Cancellation"])
  ROOT --- STAT(["Status Reporting"])
  EV --- EVA(["Amendment"])
  EV --- EVW(["Withdrawal"])
  EV --- EVR(["Notification Reminder"])
  BAL --- BALA(["Amendment"])
  CON --- UND(["Underlying resource movement"])
  CON --- OUT(["Outturn Distribution"])
  CAN --- CAA(["Cancellation Advice"])
  CAN --- CAR(["Cancellation Request"])
  STAT --- ES(["Event Status"])
  ES --- EPS(["Event Processing Status"])
  ES --- EST(["Event Stage"])
  STAT --- IS(["Instruction Status"])
  STAT --- CS(["Cancellation Status"])
  STAT --- IST(["Instructions Statement"])
''',
'fig-0003':'''flowchart TB
  subgraph S["Account Servicer"]
    PROCESS("Process Cancellation Request")
    B1["Request accepted? (source bar)"]
    REPORT("Report Cancellation Request Status")
    NOTIFY("Go to Notify balance/entitlement process")
    PROCESS --> B1
    B1 -->|Yes| NOTIFY
    B1 -->|Yes| REPORT
    B1 -->|No| REPORT
  end
  subgraph O["Account Owner"]
    START(("Start")) --> REQUEST("Request Cancellation of Instruction")
    STATUS("Process Cancellation status") --> B2["Status OK? (source bar)"]
    B2 -->|No| ENDN(("End: No"))
    B2 -->|Yes| ENDY(("End: Yes"))
    B2 -->|Yes| ELECT("Instruct election")
  end
  REQUEST --> PROCESS
  REPORT --> STATUS
'''}
items=[
('fig-0001','Corporate Actions business roles and functional participants','directed-role-associations','P136','image2.png','fig-0002',roles,[],'''The artwork has two separated sides. Eight source labels point to Account Servicer: Market Data Provider, Broker, ICSD, CSD, Clearing, Stock Exchange, Sub Custodian, and Global Custodian. Eight source labels point to Account Owner: Global Custodian, ICSD, Broker, Beneficial Owner, Fund Manager, CSD, Sub Custodian, and Institutional Investor. Labels appearing on both sides are represented separately in the drawing but link to the same scoped business-role record.

P132-P135 define business roles versus functional participants and explicitly state a many-to-many relationship. An institution is not permanently equated with either functional participant. T8 gives the two participant definitions; T9 gives business-role definitions; T10 supplies the role-to-participant mapping. The source label Clearing corresponds to Clearing Agent in T10; both source labels are preserved. Issuer and Issuer Agent occur in T9 but are absent from this overview and T10. Their absence from the drawing is not evidence that they do not participate in the business context.

The arrows show source-supported role participation. They do not specify message direction, inheritance, composition, ownership or cardinality. The two enclosing boxes in this reconstruction denote the two visually separated sides of the source; no system boundary is asserted. Decorative actor silhouettes and the central dashed divider are represented by labeled nodes and the two sides. There are no source use-case ellipses or include/extend relationships in this figure.'''),
('fig-0002','Corporate Actions business-process hierarchy','business-process-hierarchy','P144','image3.png','fig-0003',[],[],'''The source groups nine high-level processes under Corporate Actions processes. Event Notification has Amendment, Withdrawal, and Notification Reminder; Balance/Entitlement Notification has Amendment; Movement Confirmation has Underlying resource movement and Outturn Distribution; Cancellation has Cancellation Advice and Cancellation Request; Status Reporting has Event Status, Instruction Status, Cancellation Status, and Instructions Statement. Event Status has Event Processing Status and Event Stage. Reminder, Election, Movement Preliminary Advice and Movement Reversal have no further child shown in this artwork.

Connections have no arrowheads in the original. They are preserved as undirected grouping connectors, not message exchanges, sequencing, UML inheritance, or use-case include/extend relationships. Ovals identify business processes here; source P143 explicitly calls this a high-level BusinessProcesses diagram. The source does not provide actors or a system boundary in this hierarchy. Process definitions, triggers, preconditions, postconditions, and responsible roles are preserved separately in T11-T19 and reusable flow pages.'''),
('fig-0003','Corporate action instruction cancellation activities','activity','P184','image14.emf','fig-0014',['account-servicer','account-owner'],['flow-src-000079-p154-cancellation'],'''The Account Owner initiates Request Cancellation of Instruction, which travels to the Account Servicer's Process Cancellation Request activity. At the source bar annotated Request accepted?, two outgoing paths labeled Yes lead to Go to Notify balance/entitlement process and Report Cancellation Request Status; the No path also leads to Report Cancellation Request Status. The Account Servicer sends the status to the Account Owner's Process Cancellation status activity. At the source bar annotated Status OK?, No and Yes each lead to a separate endpoint, while another Yes path leads to Instruct election.

The source legend T20 defines a bar as initiating several actions in parallel. The two bars are retained as source-bar nodes with every outgoing edge and label. The source mixes these bars with Yes/No conditions; it does not establish exclusive-choice semantics or the synchronization/join behavior. Do not infer that the two Yes branches are exclusive. This is an explicit notation limitation requiring business review, not an inferred execution rule.

The source note says to see the previous diagram for detailed Announcement, Confirmation and Instruction activities (P182, image13.emf). This cancellation diagram intentionally shows the two functional participants and a subset of the full business activity sequence. No external initiator or designated agent is added to the artwork. Message bindings come from the separately cited cancellation flow; this activity artwork itself uses activity names, not exact message identifiers.''')]
for did,title,kind,pid,img,origfig,participants,flows,explain in items:
 page=out/(did+'.md');mmd=out/(did+'.mmd');mmd.write_text(codes[did],encoding='utf-8')
 original=root/'domains/securities/assets/src-000079/originals'/img
 preview=root/'domains/securities/assets/src-000079/derived-previews'/f'{img}.png' if img.endswith('.emf') else original
 evidence=root/s['set_path']/'documents/src-000079/diagrams'/f'{origfig}.md'
 meta=dict(template=False,document_kind='diagram',review_status='needs-review',manual_curated=True,domain='securities',diagram_id=did,title=title,diagram_kind=kind,content_origin='source-reconstruction',source_ids=['src-000079'],source_editions=[s['source_edition']],source_locations=[{'source_id':'src-000079','locator':f'BusinessRoles and Participants / BusinessProcess Description / BusinessActivities as applicable; direct-body paragraph {pid}; word/media/{img}'}],participants=['participant-src-000079-'+r for r in participants],flow_ids=flows,render_status='not-run',visual_review='not-run',limitations=['Source conditional paths are drawn from parallel bars; exclusive-choice semantics are not established.'] if did=='fig-0003' else [])
 text=kb.front(meta)+'# '+title+'\n\n## Source evidence\n\n'+kb.source_link(root,page,s)+f'; direct-body paragraph {pid}, word/media/{img}. '+kb.link(page,evidence,'Extraction occurrence')+'.\n\n'+kb.link(page,original,'Unchanged original asset')+'.\n\n!['+title+']('+kb.rel(page,preview)+')\n\n## Mermaid reconstruction\n\n```mermaid\n'+codes[did]+'```\n\n## Meaning and boundaries\n\n'+explain+'\n\n'
 if participants:text+='## Scoped participants\n\n'+ '\n'.join('- '+kb.link(page,root/'shared/reference/participants'/('participant-src-000079-'+r+'.md'),r.replace('-',' ').title()) for r in participants)+'\n\n'
 if flows:text+='## Related flow\n\n'+ '\n'.join(kb.link(page,root/s['set_path']/'flows'/(f+'.md'),f) for f in flows)+'\n\n'
 text+='## Review evidence\n\nThe original was opened at full resolution. Mermaid parsing, rendering, and visual comparison of the rendered output remain pending. No pass is claimed yet.\n';kb.put(page,text)
print(str(out))
