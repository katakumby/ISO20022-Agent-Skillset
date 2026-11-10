from pathlib import Path
import sys,json
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();base=root/'domains/securities/reference/message-sets/corporate-actions/2025-2026';out=base/'diagrams/detailed-activities';out.mkdir(parents=True,exist_ok=True);s=next(x for x in kb.sources(root) if x['source_id']=='src-000079');prefix='---\nconfig:\n  themeCSS: ".edgeLabel p {background-color:#ffffff !important;} .edgeLabel rect {fill:#ffffff !important;opacity:1!important;}"\n  flowchart:\n    htmlLabels: true\n---\n'
codes={10:'''flowchart TB
 START(("Start")) --> A["Event Announcement process"]
 A --> D1{" "}
 D1 -->|"Amendment needed"| AM1["Amendment Process"]
 AM1 --> A
 D1 -->|"Event Cancelled (by issuer)"| W["Withdrawal Process"]
 W --> E1(("End"))
 D1 -->|"Event Cancelled by AS"| C1["Cancellation Process"]
 C1 --> E2(("End"))
 D1 --> B["Eligibility / Entitlement notification process"]
 B --> D2{" "}
 D2 -->|"Amendment needed"| AM2["Amendment Process"]
 AM2 --> B
 D2 -->|"Event Cancelled by AS"| C2["Cancellation Process"]
 C2 --> D3{" "}
 D3 --> B
 D3 --> E3(("End"))
 D2 --> J((" "))
 J --> D4{" "}
 D4 --> P1["Pre-advice of Movement"]
 D4 --> CO["Movement Confirmation"]
 P1 --> CO
 CO --> D5{" "}
 D5 --> E4(("End"))
 D5 -->|"Reversal needed"| D6{" "}
 D6 --> P2["Pre-advice of Movement"]
 D6 --> R["Movement Reversal"]
 P2 --> R
 R --> D7{" "}
 J -.- D7
 D7 --> E5(("End"))
 NOTE["General remark: sequence varies between corporate action events; this flow illustrates a possible sequence."]
''',11:'''flowchart TB
 START(("Start")) --> A["Event Announcement process"]
 A --> D1{" "}
 D1 -->|"Amendment needed"| AM1["Amendment Process"]
 AM1 --> A
 D1 -->|"Event Cancelled (by issuer)"| W["Withdrawal Process"]
 W --> E1(("End"))
 D1 -->|"Event Cancelled by AS"| C1["Cancellation Process"]
 C1 --> E2(("End"))
 D1 --> B["Eligibility / Entitlement notification Process (Preliminary)"]
 B --> D2{" "}
 D2 -->|"Amendment needed"| AM2["Amendment Process"]
 AM2 --> B
 D2 -->|"Event Cancelled by AS"| C2["Cancellation Process"]
 C2 --> D3{" "}
 D3 --> B
 D3 --> E3(("End"))
 D2 --> I["Instruction process"]
 I --> D4{" "}
 D4 -->|"Trx needs cancellation"| C3["Cancellation Process"]
 C3 --> D5{" "}
 D5 --> I
 D5 --> E4(("End"))
 D4 --> F["Eligibility / Entitlement notification Process (Final)"]
 F --> D6{" "}
 D6 -->|"Event Cancelled by AS"| C4["Cancellation Process"]
 C4 --> D7{" "}
 D7 --> F
 D7 --> E5(("End"))
 D6 --> P1["Pre-advice of Movement"]
 D6 --> J((" "))
 J --> CO["Confirmation"]
 P1 --> CO
 CO --> D8{" "}
 D8 --> E6(("End"))
 D8 -->|"Reversal needed"| D9{" "}
 D9 --> P2["Pre-advice of Movement"]
 D9 --> R["Movement Reversal"]
 P2 --> R
 R --> D10{" "}
 J -.- D10
 D10 --> E7(("End"))
 NOTE["General remark: sequence varies between corporate action events; this flow illustrates a possible sequence."]
''',12:'''flowchart TB
 subgraph S["Account Servicer"]
 START(("Start")) --> A("Announce new CA event")
 A --> B1["Source bar: Event confirmed?"]
 B1 -->|Yes| B2["Source bar"]
 B1 -->|No| U("Update CA event announcement")
 B2 -->|"Details complete"| B3["Source bar"]
 B2 -->|"Details preliminary"| U
 B3 --> U
 B3 --> N("Notify Balance and Entitlements")
 U --> B4["Source bar: Event confirmed/details complete?"]
 B4 -->|Yes| N
 B4 -->|No| U
 N --> B5["Source bar"]
 B5 --> UB("Update Balance and Entitlements")
 B5 --> C("Confirm cash/securities postings")
 UB --> C
 C --> B6["Source bar"]
 B6 --> ES1(("End"))
 B6 --> R("Reverse cash/securities postings")
 R --> B7["Source bar"]
 B7 --> C
 B7 --> ES2(("End"))
 end
 subgraph O["Account Owner"]
 OA("Process new CA event")
 OU("Process update")
 ON("Process notification")
 OUB("Process update")
 OC("Reflect cash/securities movements") --> EO1(("End"))
 OR("Reflect cash/securities movements reversal") --> EO2(("End"))
 end
 A --> OA
 U --> OU
 N --> ON
 UB --> OUB
 C --> OC
 R --> OR
 NOTE["Once confirmed, a CA event can be withdrawn by the issuer at any time. Event withdrawal and notification cancellation are described in separate activity diagrams."]
''',13:'''flowchart TB
 subgraph S["Account Servicer"]
 START(("Start")) --> A("Announce new CA event")
 REM("Reminder")
 PROC("Process Instruction") --> B1["Source bar: Processed?"]
 B1 -->|Yes| NEXT("Go to next activity")
 B1 -->|Yes| REPORT("Report Instruction Status")
 B1 -->|No| REPORT
 N1["Response deadline approaching? Uninstructed balance remaining?"]
 end
 subgraph O["Account Owner"]
 OA("Process new CA announcement") --> E1(("End"))
 OA --> INSTR("Instruct election")
 B2["Source bar"] --> E2(("End"))
 B2 --> INSTR
 STATUS("Process Instruction status") --> B3["Source bar: Status OK?"]
 B3 -->|Yes| E3(("End"))
 B3 -->|No| E4(("End"))
 B3 -->|No| INSTR
 end
 A --> OA
 REM --> B2
 INSTR --> PROC
 REPORT --> STATUS
 N1 -.- REM
 NOTE["See previous diagram for detailed Announcement and Confirmation activities."]
'''}
items=[(10,170,172,'Mandatory reorganisation without options','REOR/MAND and DISN/MAND',None),(11,173,175,'Corporate action processes with options','REOR/CHOS, DISN/CHOS and REOR/VOLU',None),(12,177,178,'Generic non-elective corporate action activities',None,20),(13,180,182,'Elective instruction activities',None,20)];summary=[]
for num,hp,pi,title,scope,issue in items:
 did=f'fig-{num:04d}';p=out/(did+'.md');flow=next((base/'flows').glob(f'flow-src-000079-p{hp}-*.md'));fm,fb=kb.metadata(flow);ext='emf' if num==13 else 'png';code=prefix+codes[num];(out/(did+'.mmd')).write_text(code,encoding='utf-8')
 limitation='The source dashed connector between the pre-confirmation region and final post-reversal merge has no clearly readable arrowhead in the supplied PNG. It is reconstructed as an undirected dashed connection; no reverse loop or extra execution order is inferred.' if num<12 else 'Source T20 defines bars as parallel actions, yet this artwork combines bars with Yes/No conditional labels. Every source branch is retained; exclusive-choice and synchronization semantics remain unresolved under issue-000020.'
 meta=dict(template=False,document_kind='diagram',review_status='needs-review',manual_curated=True,domain='securities',diagram_id=did,title=title,diagram_kind='activity',content_origin='source-reconstruction',source_ids=['src-000079'],source_editions=[s['source_edition']],source_locations=[{'source_id':'src-000079','locator':f'Description of BusinessActivities / {title}; P{pi}; word/media/image{num}.{ext}; T20 symbol legend'}],participants=['participant-src-000079-account-servicer','participant-src-000079-account-owner'] if num>=12 else [],flow_ids=[fm['flow_id']],render_status='not-run',visual_review='not-run',limitations=[limitation],issue_ids=['issue-000020'] if issue else [])
 orig=root/'domains/securities/assets/src-000079/originals'/f'image{num}.{ext}';preview=root/'domains/securities/assets/src-000079/derived-previews'/f'image{num}.emf.png' if ext=='emf' else orig
 explanation=('This high-level process view is scoped by P171/P174 to '+scope+'. It contains event announcement/amendment, issuer withdrawal, account-servicer cancellation, eligibility/entitlement, optional preliminary advice, confirmation and reversal paths. '+('The options flow additionally contains preliminary and final eligibility phases, instruction processing and transaction cancellation.' if num==11 else '')+' Every unlabeled source diamond remains an unlabeled diamond; no unstated guard is supplied. The small blank junction circle is a derived routing aid for the source line junction, not a new business activity. The general source note says event sequences can vary and this is only a possible sequence. The source does not draw participant lanes here; responsible roles must be retrieved from the named process references, not inferred from box position.' if num<12 else 'The source lanes assign activities to Account Servicer and Account Owner. Named activities, all cross-lane arrows, all source endpoints, and repeated Yes/No branches are preserved. Source bars are explicitly labeled as bars in the reconstruction rather than converted into exclusive decision diamonds. Annotation boxes are retained as source notes, not extra activities or participants. The source note defines omitted context and is reproduced in the diagram.')
 text=kb.front(meta)+'# '+title+'\n\n'+kb.source_link(root,p,s)+f'; Description of BusinessActivities / {title}; P{pi}; word/media/image{num}.{ext}. '+kb.link(p,orig,'Unchanged original')+'.\n\n![Source preview]('+kb.rel(p,preview)+')\n\n## Mermaid reconstruction\n\n```mermaid\n'+code+'```\n\n## Process and participant semantics\n\n'+explanation+'\n\n## Unresolved source notation\n\n'+limitation+'\n\n'+kb.link(p,flow,'Reusable flow and surrounding source narrative')+'.\n\n## Review evidence\n\nFull-size source inspected. Rendered comparison pending; semantic limitation remains open.\n';kb.put(p,text)
 fm.update(document_kind='business-flow',manual_curated=True);fm['limitations']=list(dict.fromkeys(fm.get('limitations',[])+[limitation]));fb+='\n## Source activity reconstruction\n\n'+explanation+'\n\n'+kb.link(flow,p,title)+'. '+limitation+'\n';kb.put(flow,kb.front(fm)+fb);summary.append({'diagram':p.relative_to(root).as_posix(),'source_figure':did,'flow':flow.relative_to(root).as_posix(),'limitation':limitation})
kb.dump(root/'work/documents/src-000079/detailed-activity-curation.json',summary)
