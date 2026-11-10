from pathlib import Path
from PIL import Image
seed=Path('work/curate_t2s_cashaccount.py').read_text(encoding='utf-8-sig')
exec(seed.split("role('recipient-party'")[0].replace('src-000350','src-000353').replace('src-000351','src-000354'))
role('central-bank','Central Bank','P74-P79 names CBs as senders of collateral-value creation, eligible-securities creation/deletion and close-link creation/deletion. This scope is retained separately from the specifically defined National Central Bank business role.','P74-P79; T2 abbreviations')
role('party-authorised-by-central-bank-or-payment-bank','Party authorised by a central bank or payment bank','A delegated actor expressly permitted in P75/P78 to send eligible-securities creation or deletion requests. Authorisation by a central bank/payment bank is the source relationship; no particular institution is identified.','P75/P78')
role('party-authorised-by-csd','Party authorised by a CSD','A delegated actor expressly permitted by P76 to send an eligible counterpart CSD creation request on the CSD authorisation relationship. Kept distinct from central-bank/payment-bank delegated actors.','P76')
for n,pg,box in [(9,16,(105,418,905,752)),(10,17,(105,160,905,495)),(11,18,(105,300,905,640)),(12,19,(105,130,905,462))]:
 src=root/'domains/securities/assets'/sid/'source-page-renders'/f'word-page-{pg}.png';Image.open(src).crop(box).save(src.parent/f'fig-{n:04d}-complete-crop.png')
roles=['instructing-party','executing-servicing-party'];spec=[]
def add(n,title,code,desc,slugs=roles,flows=[],tables=[],families=[],issues=[],paragraphs=None):spec.append(dict(n=n,title=title,code=code,desc=desc,slugs=slugs,flows=flows,tables=tables,families=families,issues=issues,paragraphs=paragraphs))
create=['reda.024','reda.025','reda.026','reda.027','reda.028','reda.044'];delete=['reda.075','reda.077','reda.028'];allfamilies=create+['reda.075','reda.077']
add(1,'Collateral-reference business-role context','''flowchart LR
 DB["Central Database System"] --> I["Instructing Party"]
 CM["Collateral Management System"] --> I
 N["NationalCentralBank"] --> I
 P["Payment Bank"] --> I
 C["Central Securities Depository"] --> I
 M["Market Infrastructure"] --> E["Executing/Servicing Party"]
 linkStyle default stroke:blue
''','Five blue directed role associations point to Instructing Party; Market Infrastructure points to Executing/Servicing Party. T5 defines those functional participants. T7 instead labels its columns Account Servicer/Account Owner, with the five first business roles (including Central Database System in this publication) mapped as servicers and Market Infrastructure as owner. No equivalence with T5 is established. Both vocabularies remain separate under issue-000038. These role associations are not message exchanges.',slugs=roles+['central-database-system','collateral-management-system','national-central-bank','payment-bank','central-securities-depository-csd','market-infrastructure','account-servicer','account-owner'],tables=[5,6,7],issues=['issue-000038'])
add(2,'Collateral-reference maintenance overview','''flowchart TB
 S((" ")) --> V("Create<br/>Securities<br/>Valuation")
 S --> A("Create Auto-<br/>Collateralisation<br/>Eligibility Link")
 S --> C("Create Close<br/>Link")
 S --> E("Create Eligible<br/>Counterpart<br/>CSD")
 S --> DC("Delete Close<br/>Link")
 S --> DA("Delete Auto-<br/>Collateralisation<br/>Eligibility Link")
 V --> End(((" ")))
 A --> End
 C --> End
 E --> End
 DC --> End
 DA --> End
 style S fill:#0070b5,stroke:#0070b5
 classDef activity fill:#9bbb59
 class V,A,C,E,DC,DA activity
''','The source start branches into six maintenance activities: four creations (securities valuation, auto-collateralisation eligibility link, close link and eligible counterpart CSD) and two deletions (close link and auto-collateralisation eligibility link). All lead to the same end. No exclusive-choice or parallel bar is drawn. T8/T9 require the instructing party to be known and to identify the required coverage change; acknowledgement of processing is the stated postcondition. Their creation/deletion conditions remain separate.',flows=[104,105],tables=[8,9],families=allfamilies)
add(7,'Collateral-reference creation/deletion activity reused','''flowchart TB
 subgraph I["Instructing Party"]
 S((" ")) --> Instruction("Instruction")
 Merge{" "} --> Monitor("Monitor")
 Monitor --> IA{"Accepted"}
 IA -->|Yes| End(((" ")))
 IA -.->|No| Instruction
 end
 subgraph E["Executing Party"]
 Validate("Validate") --> EA{"Accepted"}
 EA -->|Yes| Process("Process")
 EA -->|No| Report("Report")
 end
 Instruction --> Validate
 Process -->|"Status &lt;&lt;Accepted&gt;&gt;"| Merge
 Report -->|"Status &lt;&lt;Rejected&gt;&gt;"| Merge
 style S fill:#548dd4,stroke:#548dd4
 linkStyle default stroke:#548dd4
''','The identical artwork is used for creation at P112 and deletion at P116. Instruction crosses to Validate. An accepted instruction goes to Process and returns Status <<Accepted>>; a rejected instruction goes to Report and returns Status <<Rejected>>. A merge diamond leads to Monitor, then the second Accepted decision ends on Yes or follows a dashed No loop back to Instruction. T11/T12 add a substantive QUEUED case absent from the artwork: if valid but timing does not permit processing, QUEUED is sent and the instruction is resubmitted to validation after a specific event. This narrative participant responsibility is preserved without inventing a diagram branch. T12 still says time permits creation in its deletion validation row; issue-000043 records that wording.',flows=[110,115],tables=[11,12],families=allfamilies,issues=['issue-000043'])
for n,title,fp,status,isdelete,pra in [(9,'Collateral-reference creation completed',121,'COMPLETED',False,(127,133)),(10,'Collateral-reference creation rejected',134,'REJECTED',False,(140,146)),(11,'Collateral-reference deletion completed',149,'COMPLETED',True,(155,159)),(12,'Collateral-reference deletion rejected',160,'REJECTED',True,(166,170))]:
 req='Auto-Collateralisation Eligibility Link/Close Link Delete Request (reda.075, reda.077)' if isdelete else 'Security Valuation/Auto-Collateralisation Eligibility Link/Close Link/Eligible Counterpart CSD Create Request (reda.024, reda.025, reda.027, reda.026)'
 response='Collateral Data Status Advice/Eligible Counterpart CSD Status Advice (reda.028/reda.044): '+status
 code='sequenceDiagram\n participant I as Instructing Party\n participant E as Executing/Servicing Party\n Note over I,E: '+('Deletion Process' if isdelete else 'Creation Process')+'\n I->>E: '+req+'\n E->>I: '+response+'\n'
 desc='The Instructing Party sends a '+('deletion instruction for an existing auto-collateralisation eligibility link or close link' if isdelete else 'creation instruction for a security valuation, auto-collateralisation eligibility link, close link or eligible counterpart CSD')+'. The Executing/Servicing Party returns '+status+' and identifies the reference data '+('processed' if status=='COMPLETED' else 'rejected')+'. Request items are alternatives within the combined source label, not a requirement to send all request messages. '
 if isdelete:desc+='The source response label includes reda.044, but P80 associates deletion075/077 with reda.028 while P82 associates reda.044 with creation026. The original label is retained under issue-000043; reda.044 is recorded as a disputed source assertion rather than a confirmed deletion-response mapping.'
 else:desc+='P80 explicitly associates requests024/025/027 with status028; P82 associates request026 with status044. The combined artwork label does not mean every creation request receives both status messages.'
 add(n,title,code,desc,flows=[fp],families=delete if isdelete else create,issues=['issue-000043'] if isdelete else [],paragraphs=pra)
# Use the inspected source-specific definitions with the common local authoring block.
block=seed[seed.index('for x in spec:'):]
block=block.replace("'src-000351'","'src-000354'").replace("'; file pages'","'; file pages'")
block=block.replace("preview=root/'domains/securities/assets'/sid/'derived-previews'/(orig.name+'.png');", "preview=(root/'domains/securities/assets'/sid/'derived-previews'/(orig.name+'.png')) if orig.suffix=='.emf' else orig;\n if n>=9:orig=root/'work/docx-render'/sid/'document.pdf';preview=root/'domains/securities/assets'/sid/'source-page-renders'/f'{fid}-complete-crop.png'\n ")
block=block.replace("'; word/'+fig['images'][0]['target']", "('; Word file/printed page '+str(n+7)) if n>=9 else ' / '.join(fig['heading_path'])+'; '+fig['locator']+'; word/'+fig['images'][0]['target']")
block=block.replace('Cash Account Audit Trail Query/Response process; P141; fig-0009; same word/media/image7.emf bytes','Collateral Reference Data deletion; P116; fig-0008; same word/media/image7.emf bytes')
block=block.replace("'class' if n==1 else 'sequence' if n>=10 else 'activity'","'participant-context' if n==1 else 'sequence' if n>=9 else 'activity'")
block=block.replace('The same unchanged image7.emf occurs twice (P132/fig-0007 and P141/fig-0009).','The same unchanged image7.emf occurs twice (P112/fig-0007 and P116/fig-0008).')
block=block.replace("(['fig-0009'] if n==7 else [])","(['fig-0008'] if n==7 else [])").replace('Cash-account source context:','Collateral-reference source context:')
exec(block)
# Narrow flow applicability; disputed deletion044 is evidence only, not a confirmed binding.
for start,fams in [(104,create),(105,delete),(110,create),(115,delete)]:
 p=next((base/'flows').glob(f'flow-{sid}-p{start}-*.md'));m,b=kb.metadata(p);mids=[d['message_id'] for d in defs if '.'.join(d['message_id'].split('.')[:2]) in fams];m.update(message_ids=mids,message_families=fams);b+='\nExact confirmed bindings for this process: '+', '.join(kb.link(p,root/'domains/securities/reference/messages'/mid/'index.md',mid) for mid in mids)+'. Source response family044 in deletion sequences remains disputed under issue-000043.\n';put(p,kb.front(m)+b)
for n in [11,12]:
 p=base/'diagrams/curated'/f'fig-{n:04d}.md';m,b=kb.metadata(p);m['disputed_message_ids']=['reda.044.001.01'];m['source_locations'].append({'source_id':sid,'locator':'Functionality P80/P82 compared with deletion sequence '+('P152' if n==11 else 'P163')});put(p,kb.front(m)+b)
# Authorised actor applicability is source-specific, not name-based equivalence.
for slug,fams,loc in [('central-bank',['reda.024','reda.025','reda.027','reda.075','reda.077'],'P74/P75/P77-P79'),('party-authorised-by-central-bank-or-payment-bank',['reda.025','reda.075'],'P75/P78'),('party-authorised-by-csd',['reda.026'],'P76')]:
 pp=root/'shared/reference/participants'/(prefix+slug+'.md');m,b=kb.metadata(pp);m['message_ids']=[d['message_id'] for d in defs if '.'.join(d['message_id'].split('.')[:2]) in fams];m['flows']=[kb.metadata(next((base/'flows').glob(f'flow-{sid}-p104-*.md')))[0]['flow_id']]+([kb.metadata(next((base/'flows').glob(f'flow-{sid}-p105-*.md')))[0]['flow_id']] if any(x in fams for x in ['reda.075','reda.077']) else []);b+='\nExplicit originating-message applicability ('+loc+'): '+', '.join(kb.link(pp,root/'domains/securities/reference/messages'/mid/'index.md',mid) for mid in m['message_ids'])+'.\n';put(pp,kb.front(m)+b)
 for start in ([104,105] if any(x in fams for x in ['reda.075','reda.077']) else [104]):
  fp=next((base/'flows').glob(f'flow-{sid}-p{start}-*.md'));fm,fb=kb.metadata(fp);fm['participants']=sorted(set(fm.get('participants',[])+[prefix+slug]));fb+='\nNarrative authorised sender: '+kb.link(fp,pp,m['title'])+'; '+loc+'. Only the message applicability listed in that participant record is established.\n';put(fp,kb.front(fm)+fb)
