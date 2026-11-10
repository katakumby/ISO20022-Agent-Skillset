from pathlib import Path
from PIL import Image
seed=Path('work/curate_t2s_cashaccount.py').read_text(encoding='utf-8-sig')
exec(seed.split("role('recipient-party'")[0].replace('src-000350','src-000365').replace('src-000351','src-000366'))
role('authorised-user','Authorised User','A user granted appropriate rights can request creation or update of a Security CSD Link or Account Link. This authorization context does not identify a particular institution or equate an individual user with the Instructing Party institution.','P57-P60/P75-P83')
role('authorised-party','Authorised Party','The narrative party permitted to request link creation or maintenance. The executing system must know the instructing party and grant appropriate privileges (T8/T9); source P58/P60/P76/P83 supplies this authorization context.','P58/P60/P76/P83; T8/T9')
role('issuer-csd','Issuer CSD','A CSD identified as the issuer-side endpoint of a Security CSD Link. P58 lists its identification among link-creation data; example P233-P235 links ISIN XXABCDEFGHI1 to issuer CSD CSDAXXYYAAA. The source does not say this endpoint necessarily sends the request.','P58; P233-P235')
role('investor-csd','Investor CSD','A CSD identified as the investor-side endpoint of a Security CSD Link. P58 permits issuer or investor identification; P283-P287 identifies a maintenance target by the ISIN–Investor CSD pair. The source does not equate this endpoint with the sender.','P58; P283-P287')
role('technical-issuer','Technical Issuer','A party whose identification is listed as Security CSD Link creation information. No independent definition, institution identity, or request-sending responsibility is supplied in this passage.','P58')
roles=['instructing-party','executing-servicing-party'];spec=[]
def add(n,title,code,desc,slugs=roles,flows=[],tables=[],families=[],issues=[],paragraphs=None):spec.append(dict(n=n,title=title,code=code,desc=desc,slugs=slugs,flows=flows,tables=tables,families=families,issues=issues,paragraphs=paragraphs))
create=['reda.045','reda.049','reda.047','reda.051'];modify=['reda.046','reda.050','reda.047','reda.051'];allfam=sorted(set(create+modify))
add(1,'Link reference-data role mappings','''flowchart LR
 N["NCB"] --> I["Instructing party"]
 C1["CSD"] --> I
 CO["Corporate"] --> I
 B["Bank"] --> I
 MI["Market Infrastructure"] --> E["Executing/Servicing Party"]
 MD["Market Data Provider"] --> E
 C2["CSD"] --> E
''','Seven source arrows map business-role labels to two functional participant roles. The CSD appears in both relationships and remains one scoped record; an institution can act in either role. Source T7 additionally permits Market Data Provider as Instructing Party, which is absent from this typical-roles picture and remains included in the library/flows. The arrows are associations, not inheritance. Source P102 erroneously calls this Party Reference Data; cover/body and actual link messages establish Link Reference Data, retained under issue-000049.',slugs=roles+['national-central-bank-ncb','central-securities-depositories-csd','corporate','bank','market-infrastructure','market-data-provider'],tables=[5,6,7],issues=['issue-000049'])
add(2,'Link creation and modification overview','''flowchart TB
 S((" ")) --> C("Link Creation")
 S --> M("Link Modification")
 C --- E(((" ")))
 M --- E
 style S fill:#0079b8,stroke:#0079b8
 style E fill:black,stroke:black
 classDef scope fill:#75ac3d,stroke:#75ac3d,color:white
 class C,M scope
''','A single start branches to Link Creation and Link Modification, which converge at an end point. The source does not draw an exclusive-choice diamond or a parallel bar, so neither execution constraint is inferred. P110 says the overview is not exhaustive. T8/T9 supply distinct known-party/privilege preconditions and acknowledgment postconditions for creation versus modification.',slugs=roles+['authorised-user','authorised-party'],flows=[120,122],tables=[8,9],families=allfam)
activity='''flowchart TB
 subgraph I["Instructing Party"]
 Start((" ")) --> Instruction("Instruction")
 Merge{" "} --> Monitor("Monitor")
 Monitor --> Accepted2{"Accepted"}
 Accepted2 -.->|No| Instruction
 Accepted2 -->|Yes| End(((" ")))
 end
 subgraph E["Executing Party"]
 Validate("Validate") --> Accepted1{"Accepted"}
 Accepted1 -->|Yes| Process("Process")
 Accepted1 -->|No| Report("Report")
 end
 Instruction --> Validate
 Process -->|Status &lt;&lt;Accepted&gt;&gt;| Merge
 Report -->|Status &lt;&lt;Rejected&gt;&gt;| Merge
 style Start fill:#548ed4,stroke:#548ed4
 style End fill:black,stroke:black
 classDef step fill:#d9e4bf,stroke:black
 class Instruction,Monitor,Validate,Process,Report step
'''
for n,title,flow,table,fams in [(7,'Link creation activity with validation and retry',120,11,create),(8,'Link modification activity with validation and retry',122,12,modify)]:
 add(n,title,activity,'Instruction passes from Instructing Party to Executing Party Validate. Accepted leads to Process and an Accepted status; No leads to Report and a Rejected status. Both return through a merge to Monitor. The instructing-side Accepted decision ends on Yes and follows the dashed No loop back to Instruction. The table separately defines QUEUED when a valid instruction cannot yet be processed: it is resubmitted to validation after a specific event. No QUEUED branch is drawn in this activity, and that narrative path is retained explicitly. '+('T11 checks novelty and whether the instruction is already handled; successful timely creation produces COMPLETED.' if n==7 else 'T12 checks existence and whether the data can be updated; successful timely update produces COMPLETED.'),slugs=roles+['authorised-user','authorised-party']+(['issuer-csd','investor-csd','technical-issuer'] if n==7 else ['investor-csd']),flows=[flow],tables=[8 if n==7 else 9,table],families=fams)
for n,title,start,req,fams,lo,hi,success in [(9,'Link creation confirmation sequence',139,'Creation Request (reda.045/reda.049)',create,144,151,True),(10,'Link creation rejection sequence',153,'Creation Request (reda.045/reda.049)',create,158,174,False),(11,'Link modification confirmation sequence — source role-label conflict',177,'Maintenance Request (reda.046/reda.050)',modify,190,195,True),(12,'Link modification rejection sequence — source role-label conflict',197,'Maintenance Request (reda.046/reda.050)',modify,212,227,False)]:
 right='Executing/Servicing Party' if n<11 else 'Instructing Party<br/>(right source label)';code='sequenceDiagram\n participant I as Instructing Party\n participant E as '+right+'\n Note over I,E: '+('Creation' if n<11 else 'Modification')+' process\n I->>E: Security CSD Link/Account Link '+req+'\n E-->>I: Security CSD Link/Account Link Status Advice (reda.047/reda.051): QUEUED\n E'+('->>' if success else '-->>')+'I: Security CSD Link/Account Link Status Advice (reda.047/reda.051): '+('COMPLETED' if success else 'REJECTED')+'\n';desc='The source shows the request left-to-right, an optional QUEUED advice right-to-left with a dashed line, and the final '+('solid COMPLETED' if success else 'dashed REJECTED')+' advice. The adjacent narrative says delayed processing might be reported, so QUEUED is not mandatory in every execution. '+('Successful processing returns identification of the link.' if success else 'Rejection can occur immediately or after dequeuing/revalidation with changed data. Multiple rejection reasons are permitted; all reasons and the queued alternative are retained in the adjacent source narrative below.')
 if n>=11:desc+=' Both source actor boxes literally say Instructing Party (Word20/21, images11/12). The narrative identifies the receiving/responding role as Executing/Servicing Party. This reconstruction preserves the literal artwork; narrative message directions are maintained separately, and issue-000049 remains unresolved. No second institution identity is invented from the duplicate label.'
 add(n,title,code,desc,flows=[start],families=fams,issues=['issue-000049'] if n>=11 else [],paragraphs=(lo,hi))
block=seed[seed.index('for x in spec:'):].replace("'src-000351'","'src-000366'")
block=block.replace("preview=root/'domains/securities/assets'/sid/'derived-previews'/(orig.name+'.png');","preview=(root/'domains/securities/assets'/sid/'derived-previews'/(orig.name+'.png')) if orig.suffix in ['.emf','.wmf'] else orig;").replace('if n==7:','if False:').replace("(['fig-0009'] if n==7 else [])","[]").replace("'class' if n==1 else 'sequence' if n>=10 else 'activity'","'role-map' if n==1 else 'sequence' if n>=9 else 'activity'").replace('Cash-account source context:','Link-reference source context:')
exec(block)
# Complete composite originals for both modification sequences, preserving the source role-label error.
for n,page,box in [(11,20,(90,275,780,550)),(12,21,(90,210,780,485))]:
 full=root/'domains/securities/assets'/sid/'source-page-renders'/f'word-page-{page:02d}.png';crop=full.parent/f'fig-{n:04d}-complete-crop.png';Image.open(full).crop(box).save(crop);p=base/'diagrams/curated'/f'fig-{n:04d}.md';m,b=kb.metadata(p);b=b.replace('![Complete source figure]('+kb.rel(p,root/'domains/securities/assets'/sid/'originals/image11.png')+')','![Complete source composite]('+kb.rel(p,crop)+')');b+='\nComplete native composite source: '+kb.link(p,full,f'Word file/printed page{page}')+'; '+kb.link(p,crop,'complete figure crop')+'. Original actor fragments are preserved separately and do not contain the native connector text.\n';m['source_locations'].append({'source_id':sid,'locator':f'Complete Word file/printed page{page}; composite native drawing P'+('179' if n==11 else '200')});put(p,kb.front(m)+b)
# Parent process references include ordered table evidence without losing the source section pages.
for parent,activityp,table,scenarios in [(120,128,11,[139,153]),(122,132,12,[177,197])]:
 fp=next((base/'flows').glob(f'flow-{sid}-p{parent}-*.md'));ap=next((base/'flows').glob(f'flow-{sid}-p{activityp}-*.md'));m,b=kb.metadata(fp);am,ab=kb.metadata(ap);part=ab[ab.index('## Ordered activities'):ab.index('## Messages and alternative paths')];b+='\n## Ordered source activities\n\n'+part+'\nSource scenario alternatives: '+', '.join(kb.link(fp,next((base/'flows').glob(f'flow-{sid}-p{x}-*.md')),'confirmation' if j==0 else 'rejection') for j,x in enumerate(scenarios))+'.\n';m['source_locations']+=am['source_locations'];put(fp,kb.front(m)+b)
 am.update(document_kind='source-process-section',manual_curated=True);ab+='\nCanonical reusable flow: '+kb.link(ap,fp,m['title'])+'.\n';put(ap,kb.front(am)+ab)
for start in [108,124,126,136,145,158,190,192,212,214]:
 p=next((base/'flows').glob(f'flow-{sid}-p{start}-*.md'));m,b=kb.metadata(p);m.update(document_kind='source-process-section',manual_curated=True);b+='\nReusable flows: '+', '.join(kb.link(p,next((base/'flows').glob(f'flow-{sid}-p{x}-*.md')),'creation' if x==120 else 'modification') for x in [120,122])+'.\n';put(p,kb.front(m)+b)
for start in [177,197]:
 p=next((base/'flows').glob(f'flow-{sid}-p{start}-*.md'));m,b=kb.metadata(p);m['issue_ids']=['issue-000049'];b+='\nSource direction qualification: narrative P178/P191/P193/P198/P213/P215 gives the receiving/responding role as Executing/Servicing Party; the two source drawings incorrectly duplicate the Instructing Party label. Both claims are retained under issue-000049.\n';put(p,kb.front(m)+b)
# Shared business context and status rules remain distinct from XSD cardinalities.
p=base/'link-business-rules.md';m={'template':False,'document_kind':'business-rules','manual_curated':True,'review_status':'needs-review','title':'Link creation, maintenance and lifecycle rules','domain':'securities','source_ids':[sid],'message_sets':[s['set_slug']],'message_ids':[d['message_id'] for d in defs],'source_locations':[{'source_id':sid,'locator':'P57–P96; T8/T9/T11/T12; P145–P227'}],'limitations':['Part1 business statements are not a substitute for exact schema cardinalities.']};text='# Link creation, maintenance and lifecycle rules\n\n'+kb.source_link(root,p,s)+'; P57–P96.\n\nSecurity CSD Link creation links a financial instrument to an issuer or investor CSD. P58 lists financial-instrument, CSD, technical-issuer and issuance-account identifications, maintenance responsibility, and validity dates. Account Link creation links securities and dedicated cash accounts; P76–P80 lists default use for settlement, auto-collateralisation and cash legs, plus validity dates. Maintenance updates an existing corresponding link. These are source business descriptions; the exact XSD determines field/group cardinalities.\n\nFor either link, REJECTED may have multiple reasons: missing/incorrect mandatory data, a request not being a new occurrence, inadequate creation rights, or a request already received and being processed (P64–P69/P87–P92). Modification can additionally fail because data cannot be updated (P216–P227). QUEUED means processing has been delayed; a valid request blocked by timing is submitted again to validation after a specific event (T11/T12). COMPLETED means successful processing. A request may be rejected after revalidation with new data.\n\nCreation requires a known, privileged Instructing Party that identified a coverage gap and needs the link for its activities (T8). Modification requires the known, privileged party and a changed link attribute (T9). Both source postconditions are acknowledgment of processing. No cancellation or reversal messages are supplied for these flows.\n\n'+kb.table(['Flow','Source'],[[kb.link(p,next((base/'flows').glob(f'flow-{sid}-p{x}-*.md')),label),loc] for x,label,loc in [(120,'Creation','T8/T11'),(122,'Modification','T9/T12')]])+'\n';put(p,kb.front(m)+text)
for start in [120,122]:
 p=next((base/'flows').glob(f'flow-{sid}-p{start}-*.md'));m,b=kb.metadata(p);b+='\n'+kb.link(p,base/'link-business-rules.md','Complete link business conditions and lifecycle statuses')+'.\n';put(p,kb.front(m)+b)
print('Eight diagrams authored; native-composite role conflict preserved; six substantive flow references')
