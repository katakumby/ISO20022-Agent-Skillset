from pathlib import Path
seed=Path('work/curate_t2s_cashaccount.py').read_text(encoding='utf-8-sig')
exec(seed.split("role('recipient-party'")[0].replace('src-000350','src-000356').replace('src-000351','src-000357'))
role('central-system','Central System','The platform receiving collateral-value queries, with T2S given as an example. It applies actor roles, privileges and data access rights; P148 says it returns error or collateral-value response exclusively.','P119-P129/P148; images3/9')
role('system-user','System User','The narrative query user, whose ability to query and obtain data depends on the parent actor roles and access rights. U2A is the technical mode connecting a T2S user through a GUI, while A2A connects software applications (T2).','P123/P127; T2 U2A/A2A')
role('settlement-bank','Settlement Bank','A source query-actor class shown with CSDs, payment banks and NCBs in the query overview. P125 allows cash-related queries according to access rights. No formal standalone definition is provided here.','P125; image2/P130')
role('bank-example','Bank A (hierarchy example)','An illustrative level3 actor in the role/access-rights hierarchy beneath the level2 CSD B instance. Securities Account1,2,n are shown beneath Bank A. No actual institution is identified and no legal account-ownership relationship is inferred.','image1.wmf/P108; P110')
role('broker-example','Broker A (hierarchy example)','An illustrative level3 actor in the role/access-rights hierarchy beneath the level2 CSD B instance; no actual institution or additional responsibility is identified.','image1.wmf/P108')
role('central-counterpart','Central Counterpart (source label)','A level3 actor label in the role/access-rights hierarchy beneath CSD B. The source also gives central counterparty as one possible directly connected participant in T6; this record preserves the diagram label without identifying an institution.','image1.wmf/P108; T6')
roles=['system-member','system-transaction-administrator'];spec=[]
def add(n,title,code,desc,slugs=roles,flows=[],tables=[],families=[],issues=[],paragraphs=None):spec.append(dict(n=n,title=title,code=code,desc=desc,slugs=slugs,flows=flows,tables=tables,families=families,issues=issues,paragraphs=paragraphs))
add(1,'T2S hierarchy of roles and access rights','''flowchart TB
 subgraph L1["Level 1"]
 O["T2S Operator"]
 end
 subgraph L2["Level 2"]
 CA["CSD A"]
 CB2["CSD B"]
 CN["CSD n"]
 N["NCB"]
 end
 subgraph L3["Level 3"]
 CB3["CSD B"]
 B["Bank A"]
 BR["Broker A"]
 CP["Central Counterpart"]
 PB["Payment Bank"]
 end
 subgraph L4["Level 4"]
 S1["Securities Account 1"]
 S2["Securities Account 2"]
 SN["Securities Account n"]
 C1["T2S Dedicated<br/>Cash Account 1"]
 Cn["T2S Dedicated<br/>Cash Account n"]
 end
 O --> CA
 O --> CB2
 O --> CN
 O --> N
 CB2 --> CB3
 CB2 --> B
 CB2 --> BR
 CB2 --> CP
 B --> S1
 B --> S2
 B --> SN
 N --> PB
 PB --> C1
 PB --> Cn
 Note["Source ellipses: additional CSDs at Level2;<br/>additional participants at Level3;<br/>additional securities/cash accounts at Level4.<br/>Gray source boundary contains NCB, Payment Bank<br/>and T2S dedicated cash accounts across Levels2–4."]
 classDef cash fill:#d3d3d3,stroke:black
 class N,PB,C1,Cn cash
''','This is a four-level role/access-rights hierarchy, not legal ownership or schema containment. T2S Operator has links to CSD A, CSD B, CSD n and NCB. The level2 CSD B links to a separate level3 CSD B instance, Bank A, Broker A and Central Counterpart. Bank A links to Securities Accounts1,2,n. NCB links to Payment Bank, which links to Dedicated Cash Accounts1,n. Source ellipses retain open-ended series, not numerical multiplicities. P110 says the gray area is dedicated-cash-account static data; an NCB acting as home-country CSD and providing dedicated accounts exists in both CSD and NCB roles. The reconstruction shades the four relevant node classes and explicitly documents the cross-level gray boundary; the original retains its exact enclosure.',slugs=['t2s-operator','central-securities-depositories-csd','national-central-bank-ncb','payment-bank','bank-example','broker-example','central-counterpart'],tables=[6,7])
code='''flowchart TB
 Q["Queries"] --> U["U2A"]
 Q --> A["A2A"]
 U --- Modes((" "))
 A --- Modes
 Modes --> C["CSDs"]
 Modes --> S["Settlement Banks"]
 Modes --> P["Payment Banks"]
 Modes --> N["NCBs"]
 C --- Actors((" "))
 S --- Actors
 P --- Actors
 N --- Actors
 Actors --> Ins["Instructions"]
 Actors --> Sec["Security account"]
 Actors --> Cash["Cash account"]
 Actors --> Day["Settlement day"]
 Actors --> Dyn["Dynamic data queries"]
 Actors --> Static["Static data"]
'''
groups={'Ins':['Settlement Instruction','Settlement Instruction Current Status','Settlement Instruction Status Audit Trail','Settlement Instruction Audit Trail','Settlement Transaction'],'Sec':['Security Account Position','Security Account Position History'],'Cash':['T2S Dedicated Cash Account Balance','T2S Dedicated Cash Account Posting Query','Outstanding Auto-Collateralisation Credit','Overall Liquidity','Cash Forecast','Limit','Immediate Liquidity Transfer Order List Query','Limit Utilisation Journal','Limit Utilisation','Total Collateral Value','Collateral Value per Cash Account','Collateral Value of a Security','Cash Account List','Immediate Liquidity Transfer Order Detail Query'],'Day':['T2S Calendar','T2S Diary'],'Dyn':['Report'],'Static':['Several queries available (e.g. Liquidity Transfer Orders and Liquidity Transfer Order Link Set)']}
for parent,labels in groups.items():
 for i,label in enumerate(labels):code+=' '+parent+' --> '+parent+str(i)+'["'+label+'"]\n'
code+=' style Modes fill:none,stroke:none\n style Actors fill:none,stroke:none\n'
add(2,'Central-system query taxonomy and communication modes',code,'The source is a query taxonomy rather than a use-case diagram: rectangular categories and directed branches, no actor/use-case ellipses or include/extend relationships. Queries branch to U2A and A2A; a shared connector reaches CSDs, Settlement Banks, Payment Banks and NCBs; another shared connector reaches six categories. The categories have5 instruction queries,2 securities-account queries,14 cash-account queries,2 settlement-day queries,1 dynamic report query and1 static-data example box. In the source, the fourteen cash queries connect outward from a common vertical trunk; adjacent left/right boxes are not bidirectional messages to each other. Invisible connector cues retain those shared trunks without adding actions. P121-P129 restrict every query and returned data to actor roles, privileges and access rights; this taxonomy is not blanket authorisation. U2A/A2A definitions are retained in T2.',slugs=['central-system','system-user','central-securities-depositories-csd','settlement-bank','payment-bank','national-central-bank-ncb'],tables=[2])
add(3,'Collateral-query processing with data stores','''flowchart TB
 Top("Interface") --> Q1["Collateral Value<br/>of securities<br/>query"]
 subgraph QM["Query Management"]
 P("1 - Plausibility Check") --> D1{" "}
 D1 -->|ok| Q2["Collateral Value<br/>of securities<br/>query"]
 Q2 --> Check("2 - Check Permission On Query Request")
 Check --> D2{" "}
 D2 -->|ok| Q3["Collateral Value<br/>of securities<br/>query"]
 Q3 --> Extract("3 - Extracting Data for Query")
 Extract --> D3{" "}
 D3 -->|ok| Data["Queried data"]
 D1 -->|Not ok| Merge{" "}
 D2 -->|Not ok| Merge
 D3 -->|Not ok| Merge
 Merge --> Error["Error data queries"]
 SD["&lt;&lt;data store&gt;&gt;<br/>SD"] --- Bus((" "))
 DD["&lt;&lt;data store&gt;&gt;<br/>DD"] --- Bus
 Bus --> P
 Bus --> Check
 Bus --> Extract
 end
 Q1 --> P
 Data --> Bottom("Interface")
 Error --> Bottom
 style Bus fill:none,stroke:none
''','The interface submits a collateral-value-of-securities query into Query Management. Plausibility, permission and extraction run in order. Each Not ok route merges into Error data queries; successive ok routes reach Queried data. Both outputs return to the interface. The SD and DD data stores connect to a common trunk supplying all three processing steps; the artwork does not assign one store exclusively to one check. The SD/DD acronyms are retained without unsupported expansion because the supplied glossary does not define them. Three repeated query object boxes are kept as separate occurrences. Boundary and object-underlining presentation remain fully available in the original.',slugs=roles+['central-system','settlement-infrastructure'],flows=[138],tables=[9],families=['colr.001','colr.002'])
add(8,'Collateral-query member and administrator activity','''flowchart TB
 subgraph M["System Member"]
 Start((" ")) --> Query("Instruct Collateral<br/>Value of securities<br/>Query")
 ErrorEnd(((" ")))
 DataEnd(((" ")))
 end
 subgraph A["System Transaction<br/>Administrator"]
 P("Process<br/>CheckPlausibility") --> PD{"Check<br/>successful?"}
 PD -->|No| Error("Process Deliver<br/>Error Message")
 PD -->|Yes| C("Process<br/>CheckPermission")
 C --> CD{"Check<br/>successful?"}
 CD -->|No| Error
 CD -->|Yes| Extract("Process<br/>ExtractDataForQuery")
 Extract -->|Yes| ED{"Extracting<br/>successful?"}
 ED -->|No| Error
 ED -->|Yes| Deliver("Process<br/>Deliver Queried<br/>Data Response<br/>Message")
 end
 Query --> P
 Error --> ErrorEnd
 Deliver --> DataEnd
 style Start fill:#4678bb,stroke:#4678bb
''','System Member sends the query to System Transaction Administrator. Failure of plausibility, permission or extraction leads to Deliver Error Message and a member end point. All successful checks lead to Deliver Queried Data Response Message and a distinct member end point. The Yes label on the ExtractDataForQuery-to-decision arrow is retained exactly as drawn, in addition to the decision Yes/No labels. T9 lists the same three rejection reasons. P140 maps the instructing party context to direct participant/payment bank/CSD and the executing/receiving role to settlement infrastructure.',slugs=roles+['instructing-party','executing-servicing-party','settlement-infrastructure','settlement-infrastructure-direct-participant','payment-bank','central-securities-depositories-csd'],flows=[138],tables=[9],families=['colr.001','colr.002'])
add(9,'Collateral-value communication overview','''sequenceDiagram
 participant I as NCB, CSD or<br/>directly connected<br/>Central System party
 participant E as Central System<br/>(e.g. T2S platform)
 I->>E: COLLATERAL VALUE QUERY
 E->>I: ERROR RESPONSE MESSAGE
 E->>I: COLLATERAL VALUE RESPONSE
''','An NCB, CSD or directly connected Central System party queries the Central System for current securities collateral value. The source picture shows both error and value response arrows; P148 explicitly says they are mutually exclusive. No sequential error-then-success requirement is inferred. P148 describes the value as the intraday-credit amount a party may receive by collateralising its securities. P83 requires the actual selection timestamp and balance snapshot time/types in the response context. This is collateral-value reporting, not securities movement reversal or a collateral creation instruction.',slugs=roles+['national-central-bank-ncb','central-securities-depositories-csd','settlement-infrastructure-direct-participant','central-system'],flows=[138],families=['colr.001','colr.002'],paragraphs=(148,148))
add(10,'Collateral-value query rejection or execution sequence','''sequenceDiagram
 participant M as System<br/>Member
 participant A as System<br/>Transaction<br/>Administrator
 M->>A: CollateralValueQuery
 alt 1: Rejection
 A->>M: CollateralValueReport
 Note right of A: Contains a<br/>rejection<br/>reason
 else 2: Execution
 A->>M: CollateralValueReport
 end
''','System Member sends CollateralValueQuery to System Transaction Administrator. The source has two separately drawn alternative frames: alt1 Rejection returns CollateralValueReport with a rejection reason; alt2 Execution returns CollateralValueReport. A single native Mermaid alt/else expresses the explicit exclusivity stated by P148; the original preserves the two separate frame boxes. The ERROR RESPONSE MESSAGE in the preceding overview is therefore a rejection-bearing CollateralValueReport, not an invented distinct ISO message.',flows=[138],tables=[9],families=['colr.001','colr.002'])
block=seed[seed.index('for x in spec:'):]
block=block.replace("'src-000351'","'src-000357'")
block=block.replace("preview=root/'domains/securities/assets'/sid/'derived-previews'/(orig.name+'.png');","preview=(root/'domains/securities/assets'/sid/'derived-previews'/(orig.name+'.png')) if orig.suffix in ['.emf','.wmf'] else orig;")
block=block.replace("if n==7:","if False:").replace("(['fig-0009'] if n==7 else [])","[]").replace("'class' if n==1 else 'sequence' if n>=10 else 'activity'","'role-access-model' if n==1 else 'taxonomy' if n==2 else 'sequence' if n>=9 else 'activity'").replace('Cash-account source context:','Collateral-reporting source context:')
exec(block)
# Give one reusable flow the complete trigger, query variants, conditions and outcomes.
fp=next((base/'flows').glob(f'flow-{sid}-p138-*.md'));m,b=kb.metadata(fp);m['title']='Collateral-value query management';m['search_terms']=list(dict.fromkeys(m.get('search_terms',[])+['total collateral value','cash account','security collateral value','intraday credit','access rights','error rejection']));b+='\n## Purpose, trigger, conditions and outcomes\n\nP81-P96 defines three usages: total current collateral value of earmarked available securities per cash account; collateral value per cash account and security; and value of a specified security in each linked securities account. A System Member query triggers the process (T9). Actor privileges and data access rights restrict execution and returned data (P121/P125/P129); no additional formal precondition is invented. Successful processing returns data with the selection timestamp, securities balance type and balance snapshot time (P83). Failed plausibility, permission or extraction returns a rejection reason (T9). P148 makes error and value responses mutually exclusive.\n\nThe source role mapping and T5/T6 distinctions are contextual. One institution may occur as CSD and NCB simultaneously (P110); neither functional participant role is equated with a named institution.\n';put(fp,kb.front(m)+b)
# Connect narrative-only participants and keep broader process headings as source sections.
for start in [132,144]:
 p=next((base/'flows').glob(f'flow-{sid}-p{start}-*.md'));sm,sb=kb.metadata(p);sm.update(document_kind='source-process-section',manual_curated=True);sb+='\nCurated reusable flow: '+kb.link(p,fp,'Collateral-value query management')+'.\n';put(p,kb.front(sm)+sb)
for slug in ['system-member','instructing-party','executing-servicing-party']:
 pp=root/'shared/reference/participants'/(prefix+slug+'.md');pm,pb=kb.metadata(pp);pb+='\nClassification nuance: T5 defines System Member as a participant, while T6 repeats that definition in Business Roles and labels Instructing/Executing parties there. T7 supplies the explicit mappings. These source classifications are preserved as context, not collapsed into an institution identity.\n';put(pp,kb.front(pm)+pb)
