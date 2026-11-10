from pathlib import Path
import sys,json,re
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();s=next(s for s in kb.sources(root) if s['source_id']=='src-000052');base=root/s['set_path'];rec=json.loads((root/'work/documents/src-000052/records.json').read_text(encoding='utf-8'));cp='participant-src-000052-central-counterparty';cm='participant-src-000052-individual-or-general-clearing-member';csd='participant-src-000052-central-securities-depository-csd';spec=[]
def add(n,p,title,code,desc,flowstart=None,process=None,table=None,extra=[]):spec.append(dict(n=n,p=p,title=title,code=code,description=desc,flowstart=flowstart,process=process,table=table,extra=extra))
add(1,104,'CCP and Clearing Member participant context','''flowchart LR
  CM1["CM (ICM or GCM)"] <-.-> CCP["CCP"]
  CCP <-.-> CM2["CM (ICM or GCM)"]
''','Two source instances of the same Clearing Member functional role flank the CCP; both dashed associations are bidirectional. The artwork does not identify a particular institution or distinguish these instances as buyer and seller. T10 defines the functional participants and T11 maps business roles to them. General and individual clearing memberships remain distinct contextual cases within the canonical definition.')
add(2,111,'Clearing business-process scope','''flowchart TB
  C["Clearing"]
  T(["Trade Management"])
  subgraph R["Risk Management"]
    N(["Netting and Margining"])
    D(["Default Fund Contribution"])
  end
  subgraph S["Settlement Management"]
    SN(["Settlement (Netting)"])
    B(["Buy in"])
  end
  subgraph RP["Reporting"]
    Cash(["Cash"])
    Fails(["Fails"])
  end
  CM(["Collateral Management"])
  C --> T
  C --> N
  C --> D
  C --> SN
  C --> B
  C --> RP
  C --> CM
  style RP fill:#b0b0b0
  style CM fill:#b0b0b0
''','The seven outward arrows from Clearing identify high-level scope relationships, not temporal message exchanges or UML include/extend semantics. Risk Management contains Netting and Margining plus Default Fund Contribution; Settlement Management contains Settlement (Netting) and Buy in; Reporting contains Cash and Fails. Reporting and Collateral Management are shaded out-of-scope context. P109 expressly says the diagram is non-exhaustive and shows those two processes only for completeness.',108)
add(5,192,'Trade Management activities','''flowchart LR
  subgraph C["CCP"]
    S1(("Start"))
    Accept("Accept trade")
    S2(("Start"))
    D{"Cancellation received<br/>from trading venue?"}
    Cancel("Cancel Trade Leg")
    E2((("End")))
    N1["Trading venue notifies the CCP<br/>that accepts the trade<br/>(OUT of SCOPE)"]:::outside
    N2["Trading venue may request a cancellation<br/>in case of an error in specific data<br/>(OUT of SCOPE)"]:::outside
  end
  subgraph M["Clearing Member"]
    Process("Process Instruction")
    ProcessC("Process Cancellation")
    E1((("End")))
    E3((("End")))
  end
  S1 --> Accept --> Process --> E1
  S2 --> D
  D -->|No| E2
  D -->|Yes| Cancel --> ProcessC --> E3
''','Two separate source start points represent the accepted-trade and cancellation paths. The negative cancellation decision ends immediately; the positive branch cancels the trade leg and the member processes the cancellation. Pink trading-venue notes provide out-of-scope trigger context, not additional message arrows. T12 preserves the independent trade-matching cases, contact with a trading member firm, and the opposite-trade alternative. Start/End words are explanatory marker labels added to the source circles.',191,113,12,['trading-venue','trading-member-firm','buyer','seller'])
add(6,195,'Risk Management: Netting activities','''flowchart LR
  subgraph C["CCP"]
    N["End Of Real<br/>Time Session"]
    S(("Start"))
    Net("Position Netting")
  end
  subgraph M["Clearing Member"]
    Process("Process Information")
    E((("End")))
  end
  N --> S --> Net --> Process --> E
''','The end-of-real-time-session milestone leads to position netting by the CCP and information processing by the clearing member. T13 additionally describes a business-session status message, house/client margin-account netting, reconciliation using netting parameters, and possible intraday margin on provisional net positions. The milestone box is source context, not an ISO message name.',194,125,13)
add(7,197,'Risk Management: Margining activities','''flowchart TB
  subgraph C["CCP"]
    S(("Start"))
    Calc("Calculate a risk<br/>(initial and variation margin)")
    Follow("Margin Call follow up")
    Accept{"Accept?"}
    Fork["━━━"]:::bar
    Debit("OPTIONAL<br/>Direct debit from CM cash account<br/>(OUT of SCOPE)"):::outside
    Receive("Receive Securities/Cash<br/>(OUT of SCOPE)"):::outside
  end
  subgraph M["Clearing Member"]
    Process("Process Information")
    EndInfo((("End")))
    Propose("Optional: Propose Collateral")
    New{"New proposal?"}
    EndNo((("End")))
    Deliver("Deliver Securities/Cash<br/>(OUT of SCOPE)"):::outside
  end
  E((("End")))
  S --> Calc --> Process --> EndInfo
  S --> Follow
  Follow -->|Scenario 1| Debit --> E
  Follow -->|Scenario 2| Propose --> Accept
  Accept -->|No| New
  New -->|Yes| Propose
  New -->|No| EndNo
  Accept -->|Yes| Fork
  Fork --> Receive --> E
  Fork --> Deliver --> E
''','The source start branches to risk calculation/information and margin-call follow-up. Scenario 1 permits automatic cash debit; Scenario 2 allows the member to propose collateral. CCP rejection leads to the member choosing whether to propose again; acceptance reaches a parallel bar, followed by receiving and delivering securities/cash. The three out-of-scope cash/securities paths share the source end marker. The source bar is retained as a thick bar symbol, not converted into an exclusive decision. T14 supplies collateral-deficit conditions and the CCP-rule dependency.',196,131,14)
add(8,199,'Risk Management: Default Fund Contribution activities','''flowchart LR
  subgraph C["CCP"]
    S(("Start"))
    Assess("Assess participant risk level")
    Calc("Calculate the default fund contribution")
    D{"Sufficient?"}
    Pay["Payment Process<br/>(OUT of SCOPE)"]:::outside
  end
  subgraph M["Clearing Member"]
    Process("Process Information")
  end
  E((("End")))
  S --> Assess --> Calc
  Calc --> Process --> E
  Calc --> D
  D -->|Yes| E
  D -->|No| Pay
''','The CCP assesses risk and calculates the contribution, while the member processes the result. A sufficient contribution reaches the source end marker; a deficit enters an out-of-scope payment process. The source does not draw an end beyond the payment process, so none is added. T15 preserves daily/monthly calculation, automatic debit or payment on behalf under power of attorney, optional margin calls, and possible return of excess.',198,137,15)
add(9,202,'Settlement Management: Settlement Netting activities','''flowchart TB
  subgraph D["CSD"]
    Start(("Start"))
    Report["Report the settlement results<br/>(OUT OF SCOPE)"]:::outside
    Events["Report the list of Corporate Events<br/>(OUT OF SCOPE)"]:::outside
    ProcessD["Process the instructions<br/>(OUT OF SCOPE)"]:::outside
  end
  subgraph C["CCP"]
    Update("OPTIONAL<br/>Update Position/Instructions<br/>(CNS only)")
    Net("OPTIONAL<br/>Trade Netting")
    Apply("OPTIONAL<br/>Corporate Events management<br/>(CCP applies CE on impacted positions)")
    Build("Build Settlement Instructions/Obligation")
    Send("Send the Settlement Instruction/Obligation")
  end
  subgraph M["Clearing Member"]
    ProcessM["Process the information<br/>(OUT OF SCOPE)"]:::outside
  end
  E((("End")))
  Start --> Report --> Update --> Net --> Apply --> Build --> Send
  Events --> Apply
  Send --> ProcessD --> E
  Send --> ProcessM --> E
  Send --> E
''','Three source lanes assign CSD reporting/processing, CCP updates/netting/event application/instruction building, and clearing-member information processing. The three CCP optional activities remain individually labeled; CNS-only applies to position/instruction update. Both CSD event input and settlement results are preserved, as are all three final paths. T16 additionally describes clearing-member instructions to a paying agent, the power-of-attorney exception, and failed-trade reporting when the general clearing member is absent from the settlement chain.',201,155,16,['paying-agent'])
add(10,205,'Settlement Management: Buy-In activities','''flowchart TB
  subgraph C["CCP"]
    Time["X days after the intended settlement date"]:::outside
    S(("Start"))
    Warn("Warning: Identify positions subject to buy in")
    Ack("Acknowledge the request")
    Eack((("End")))
    Notify("Notify buy in process has been launched")
    Fork["━━━"]:::bar
    CancelC["Cancel settlement instruction sent to CSD<br/>(OUT of SCOPE)"]:::outside
    Confirm("Confirm the buy in process")
    Pay["Payment Process<br/>(OUT OF SCOPE)"]:::outside
    Date["At Buy in Date +1"]:::note
  end
  subgraph M["Clearing Member"]
    Info1("Process Information")
    Ask{"Ask for a delay?"}
    Info2("Process Information")
    Info3("Process Information")
    CancelM["Cancel the settlement instruction<br/>sent to Settlement Agent<br/>(OUT OF SCOPE)"]:::outside
  end
  E1((("End")))
  E2((("End")))
  Time --> S --> Warn --> Info1 --> Ask
  Ask -->|yes| Ack --> Eack
  Ask -->|no| E1
  Warn -->|And/or| Notify
  Notify --> Info2 --> E1
  Notify --> Fork
  Fork --> CancelC --> E1
  Fork --> Confirm
  Confirm --> Info3 --> CancelM --> E2
  Confirm --> Pay --> E2
''','The warning starts X days after intended settlement date. A clearing member may request delay; the CCP acknowledges and that response path ends. The source also has a thin curved warning-to-launch connector annotated And/or; it is preserved as a directed And/or relationship without imposing an exclusive decision. Launch notification reaches a source parallel bar feeding CCP settlement-instruction cancellation and later buy-in confirmation. Confirmation is annotated Buy in Date +1 and leads to out-of-scope payment and member cancellation of its settlement-agent instruction. T17 says acknowledgment is by telephone, delay is valid only for continuous netting systems, and confirmation is one business day after buy-in. Source labels are retained; no fixed number of days is invented.',204,161,17,['settlement-agent','preferred-brokers'])
report=[]
for x in spec:
 n=x['n'];fig=next(f for f in rec['figures'] if any(i['target'].startswith('media/image'+str(n)+'.') for i in f['images']));fid=fig['figure_id'];dp=base/'diagrams/processes'/(fid+'.md');image=fig['images'][0];asset=root/image['asset'];preview=asset if asset.suffix.lower()=='.png' else root/'domains/securities/assets/src-000052/derived-previews'/(asset.name+'.png');code='---\nconfig:\n  themeCSS: ".edgeLabel p {background-color:#ffffff !important;}"\n  flowchart:\n    htmlLabels: true\n---\n'+x['code']+'  classDef outside fill:#e6b6d6,stroke:#111,color:#111\n  classDef bar fill:#111,stroke:#111,color:#111\n  classDef note fill:#fff,stroke:#777,color:#111\n'
 participants=[cp,cm]+['participant-src-000052-'+slug for slug in x['extra']]
 if n in [9,10]:participants.append(csd)
 flow=next((base/'flows').glob('flow-src-000052-p'+str(x['flowstart'])+'-*.md')) if x['flowstart'] else None
 fm,fb=kb.metadata(flow) if flow else ({},'')
 m={'template':False,'document_kind':'diagram','review_status':'needs-review','manual_curated':True,'domain':'securities','diagram_id':fid,'title':x['title'],'diagram_kind':'participant-context' if n==1 else ('business-process-scope' if n==2 else 'activity'),'content_origin':'source-reconstruction','source_ids':['src-000052'],'source_editions':[s['source_edition']],'source_locations':[{'source_id':'src-000052','locator':' / '.join(fig['heading_path'])+'; direct-body paragraph P'+str(x['p'])+'; word/'+image['target']+('; T'+str(x['table']) if x['table'] else '')}],'participants':participants if n!=2 else [],'flow_ids':[fm['flow_id']] if flow else [],'render_status':'not-run','visual_review':'not-run','limitations':['Mermaid layout differs from the source. Source labels, arrow endpoints, participant boundaries, conditions and out-of-scope annotations are retained. Start/End words explain unlabeled source markers.']}
 b='# '+x['title']+'\n\n## Source evidence\n\n'+kb.source_link(root,dp,s)+'; P'+str(x['p'])+'. '+kb.link(dp,asset,'Unchanged original image')+'; '+kb.link(dp,preview,'Viewable source rendering')+'.\n\n![Source diagram]('+kb.rel(dp,preview)+')\n\n## Mermaid reconstruction\n\n```mermaid\n'+code+'```\n\n## Actors, activities and relationships\n\n'+x['description']+'\n\n'
 if x['table']:b+=kb.link(dp,base/'documents/src-000052/tables'/f"tbl-{x['table']:04d}.md",'Complete activity responsibility table T'+str(x['table']))+'.\n\n'
 if flow:b+=kb.link(dp,flow,'Reusable process and full source narrative')+'.\n\n'
 if n==10:b+='The Date +1 text is a note on Confirm the buy in process, not a separate activity. The three end markers remain separate; bar branches and all cancellation/payment paths are retained.\n\n'
 b+='## Review evidence\n\nFull-size original/EMF preview inspected. Mermaid parsing, rendering and rendered comparison pending.\n';kb.put(dp,kb.front(m)+b);kb.put(dp.with_suffix('.mmd'),code)
 if flow and n!=2:
  process=next((base/'flows').glob('flow-src-000052-p'+str(x['process'])+'-*.md'));pm,pb=kb.metadata(process)
  fm.update(document_kind='business-flow',manual_curated=True,participants=sorted(set(fm.get('participants',[])+participants)))
  fb=fb.replace('Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.','The source activity diagram and table establish the ordered responsibilities below. Formal process definition, trigger, preconditions and postconditions are preserved in '+kb.link(flow,process,'the related source process')+'.')
  fb=fb.replace('Mermaid reconstruction and visual review are pending.','The source reconstruction and actual review record are linked below.')
  fb+='\n## Curated activity and relationship account\n\n'+x['description']+'\n\n'+kb.link(flow,dp,'Source activity reconstruction')+'.\n\n'
  for pid in participants:fb+='- '+kb.link(flow,root/'shared/reference/participants'/(pid+'.md'),pid.removeprefix('participant-src-000052-').replace('-',' '))+'.\n'
  kb.put(flow,kb.front(fm)+fb)
  for pid in participants:
   pp=root/'shared/reference/participants'/(pid+'.md');mm,bb=kb.metadata(pp);mm['manual_curated']=True;mm['flows']=sorted(set(mm.get('flows',[])+[fm['flow_id']]));bb+='\nActivity responsibilities: '+kb.link(pp,flow,x['title'])+'; '+kb.link(pp,dp,'source diagram')+'. Narrative-only participants remain distinct from the drawn lanes.\n';kb.put(pp,kb.front(mm)+bb)
 report.append({'diagram':dp.relative_to(root).as_posix(),'source_figure':fid,'source_image':n,'flow':flow.relative_to(root).as_posix() if flow else None,'kind':m['diagram_kind'],'description':x['description']})
kb.dump(root/'work/documents/src-000052/process-curation.json',report)
print('Authored 8 CCP participant/process/activity diagrams.')
