"""Manual transcription of source95 transparency diagrams; no XSD inferred."""
def structural():
 data={}
 def entry(title,nodes,edges,notes):return {'title':title,'nodes':nodes,'edges':edges,'notes':notes,'kind':'flowchart','scope':'source message structure illustration'}
 top=['Message Identification [1.1]','Sender [1.1]','Receiver [1.1]','Pagination [1.1]','Statement General Details [1.1]']
 account=['Account Identification [1.1]','Account Owner [1.1]','Account Servicer [1.1]','Beneficial Owner [0.n]']
 nodes={'M':['Message overview']+top,'S':['Safekeeping Account And Holdings [0.n]']+account,'L1':['Account Sub Level 1 [0.n]']+account,'L2':['Account Sub Level 2 [0.n]'],'D2':['Account Sub Level 2 Difference [0.n]'],'D1':['Account Sub Level 1 Difference [0.n]']}
 edges=[('M','S','contains'),('S','L1','underlying related accounts'),('S','D1','contains'),('L1','L2','contains'),('L1','D2','contains')]
 for p in ['S','L1']:
  nodes[p+'B']=['Balance Details [0.n]']
  nodes[p+'BA']=['Balance For Account [1.n]','Financial Instrument Identification [1.1]']
  nodes[p+'F']=['Balance For Financial Instrument [1..n]','Item Date [1.1]','Holdings [1.1] Choice','Holdings Indicator OR Holding Balance [1.1]','  Settled Balance [0.1]','  Traded Balance [0.1]','Price [0.n]']
  nodes[p+'A']=['Agent [0.1]'];edges +=[(p,p+'B','contains'),(p+'B',p+'BA','contains'),(p+'BA',p+'F','contains'),(p+'B',p+'A','contains')]
 data[142]=entry('Transparency report — source structural overview',nodes,edges,['For the Safekeeping Account And Holdings, the sender specifies holdings of underlying accounts specified in Account Sub Level 1.','An account at Account Sub Level 1 is related to the Safekeeping Account above; it may specify holdings for underlying accounts in Account Sub Level 2.','Inside Account Sub Level 2 is Account Sub Level 3; inside 3 is 4; inside 4 is 5; and so on. The source permits 9 account levels below the top-level Safekeeping Account.','The source’s dot-separated cardinality labels are retained literally. Holdings is explicitly a choice, not two independently mandatory fields. These are source-illustration claims; no supplied schema for semt.041.001.02 is available.'])
 def bal(prefix,values=False,bd='Balance Details [0.n]',bfa='Balance For Account [0.n]'):
  return [bd,bfa,'Financial Instrument ISIN [1.1]','Balance For Financial Instrument [1..n]']
 nodes={'M':['Sender CUSALULL','Receiver ICSDLULL','Statement General Details [1.1]','Sender Business Role [1.1] AOWN'],'S':['Safekeeping Account And Holdings [0.n]','Identification [1.1] CUSA1111','Owner [1.1] CUSALULL','Servicer [1.1] ICSDLULL']};edges=[('M','S','contains')]
 for i,(acct,owner,settled,traded) in enumerate([('AAXX-c1','AAXXLULL',90,100),('AAYY-c2','AAXXLULL',110,120),('AAZZ-c3','AAZZLULL',400,420)],1):
  k='L'+str(i);nodes[k]=[f'Account Sub Level 1 [0.n] (Repetition {i})',f'Identification [1.1] {acct}',f'Owner [1.1] {owner}','Servicer [1.1] CUSALULL','Balance Details [0.n]','Balance For Account [1.n]','Financial Instrument ISIN [1.1] ISIN LU1234567890','Balance For Financial Instrument [1..n]','Date [1.1] 2017-02-27','Holdings [1.1]','Holding Balance [1.1]',f'Settled Balance [0.1] UNITS {settled}',f'Traded Balance [0.1] UNITS {traded}'];edges.append(('S',k,'contains'))
 data[144]=entry('Transparency example 1 — message 1 structure',nodes,edges,['The source callout describes CUSA1111 as the sender’s omnibus account for underlying clients AAXX, AAYY and AAZZ.','Each financial-instrument balance may repeat per ISIN held in the indicated client account; this example has only one ISIN. The three callouts print AAXX-c1, AAYY-c2 and AAYY-c3, although the third actual account box is AAZZ-c3.','The second account’s picture owner is AAXXLULL. P5820 instead associates AAYY with AAYYLLUU; later P5837 uses AAYYLULL. All literal claims are retained (issue-000040).'])
 for num,role in [(145,'ASER'),(146,'AOWN')]:
  nodes={'M':['Sender [1.1] ICSDLULL','Receiver [1.1] CUSALULL','Statement General Details [1.1]',f'Sender Business Role [1.1] {role}'],'S':['Safekeeping Account And Holdings [1.1]' if num==145 else 'Safekeeping Account [1.1]','Identification [1.1] Account 111111','Owner [1.1] ICSDLULL','Servicer [1.1] TRAGLULL'],'L1':['Account Sub Level 1 [0.n] (Repetition 1)','Identification [1.1] Account CUSA1111','Owner [1.1] CUSALULL','Servicer [1.1] ICSDLULL']+bal('',bd='Balance Details [0.n]' if num==145 else 'Balance Details')};edges=[('M','S','contains'),('S','L1','contains')]
  for i,(acct,owner) in enumerate([('AAXX-c1','AAXXLULL'),('AAYY-c2','AAYYLULL'),('AAZZ-c3','AAYYLULL' if num==145 else 'AAZZLULL')],1):
   k='C'+str(i);nodes[k]=[f'Account Sub Level 2 [0.n] (Repetition {i})',f'Identification [1.1] Account {acct}',f'Owner [1.1] {owner}','Servicer [1.1] CUSALULL']+bal('',bd='Balance Details [0.n]' if num==145 else 'Balance Details');edges.append(('L1',k,'contains'))
  notes=['The top omnibus account is owned by ICSD on behalf of its underlying clients; CUSA1111 is owned by CUSA on behalf of AAXX, AAYY and AAZZ.','Literal picture account 111111 differs from 11111111 in example1 flow fig143 and P5868. The variants are not silently normalised.']
  if num==145:notes.append('The third client account AAZZ-c3 prints owner AAYYLULL, whereas P5840 identifies AAZZLULL. The picture value is retained (issue-000040).')
  else:notes+=['This is the first of two panels for message 5. Figure147 continues with Account Sub Level 1 repetition 2 for CUSB.','The picture prints receiver CUSALULL, while P5868 and flow fig143 send message 5 to TRAG (TRAGLULL). The picture receiver is retained, not corrected.','Balance Details has no printed cardinality in this panel; no missing cardinality is inferred.']
  data[num]=entry('Transparency example 1 — message '+('2 structure' if num==145 else '5 structure, CUSA branch'),nodes,edges,notes)
 nodes={'L1':['Account Sub Level 1 [0.n] (Repetition 2)','Identification [1.1] Account CUSB2222','Owner [1.1] CUSBLULL','Servicer [1.1] ICSDLULL']+bal('',bd='Balance Details')};edges=[]
 for i,(acct,owner) in enumerate([('BBXX-c1','BBXXLULL'),('BBYY-c2','BBYYLULL')],1):
  k='C'+str(i);nodes[k]=[f'Account Sub Level 2 [0.n] (Repetition {i})',f'Identification [1.1] Account {acct}',f'Owner [1.1] {owner}','Servicer [1.1] CUSBLULL']+bal('',bd='Balance Details');edges.append(('L1',k,'contains'))
 data[147]=entry('Transparency example 1 — message 5 structure, CUSB branch',nodes,edges,['This is the continuation of figure146’s message 5, not an independent message. The omitted top-level header/account belongs to that first panel.','The omnibus account CUSB2222 is owned by CUSB on behalf of underlying clients BBXX and BBYY.','Balance Details has no printed cardinality in this panel. The source’s omitted cardinalities are not filled from another diagram.'])
 return data

def custody():
 data={}
 for number,clients,custs in [(143,{'CUSA':['AAXX','AAYY','AAZZ'],'CUSB':['BBXX','BBYY']},['CUSA','CUSB']),(148,{'CUSC':['CCXX','CCYY']},['CUSC'])]:
  nodes={'ICSD':['ICSD','International Central Securities Depository','Account Owner to TRAG','Account Servicer to '+', '.join(custs)],'TRAG':['TRAG','Transfer Agent','Account Servicer to ICSD']};edges=[]
  for cust,cs in clients.items():
   nodes[cust]=[cust,'Custodian','Account Owner to ICSD','Account Servicer to '+', '.join(cs)];edges.append((cust,'ICSD','account-owner / account-servicer relationship'))
   for i,c in enumerate(cs,1):nodes[c]=[c,f'(client {i})','Account Owner'];edges.append((c,cust,'account-owner / account-servicer relationship'))
  edges.append(('ICSD','TRAG','account-owner / account-servicer relationship'))
  if number==143:
   messages=[('CUSA','ICSD','[1] Securities Balance Transparency Report semt.041'),('ICSD','CUSA','[2] Securities Balance Transparency Report semt.041'),('CUSB','ICSD','[3] Securities Balance Transparency Report semt.041'),('ICSD','CUSB','[4] Securities Balance Transparency Report semt.041'),('ICSD','TRAG','[5] Securities Balance Transparency Report semt.041')]
   notes=['[1] CUSA reports a breakdown of account CUSA1111 into the three accounts it services for clients.','[2] ICSD reports the holding in CUSA1111 that it services for CUSA, enriched with place of safekeeping; it echoes the clients’ holdings enriched with agent codes.','[3] CUSB reports a breakdown of account CUSB1111 into the two accounts it services for clients.','[4] ICSD reports the holding in CUSB2222 that it services for CUSB, enriched with place of safekeeping; it echoes clients’ holdings enriched with agent codes.','[5] ICSD reports a breakdown of omnibus account 11111111 into CUSA1111 and CUSB2222, each further broken down into that custodian’s client accounts.','The source’s [3] CUSB1111 differs from [4] and [5] CUSB2222; both labels are preserved (issue-000040).']
  else:
   messages=[('CUSC','ICSD','[1] Securities Balance Transparency Report semt.041'),('ICSD','CUSC','[2] Securities Balance Transparency Report semt.041'),('ICSD','TRAG','[3] Securities Balance Transparency Report semt.041')]
   notes=['[1] CUSC reports a breakdown of account CUSC3333 into its two client accounts.','[2] ICSD reports the holding in CUSC3333 that it services for CUSC, enriched with place of safekeeping; it echoes clients’ holdings enriched with agent codes.','[3] ICSD reports a breakdown of omnibus account 11111111 into the account it services for CUSC, CUSC3333, and its two underlying client accounts.']
  notes+=['The source marks upstream in the custody chain toward the client side (left), and downstream toward the transfer agent (right).','Hollow blue Account Owner markers and filled orange Account Servicer markers are expressed as labelled relationship edges and node role labels. These are roles in specific relationships; each custodian and ICSD occupies both roles at different links. No cardinality or ownership key is inferred.']
  data[number]={'title':'Transparency of holdings — custody-chain example '+('1' if number==143 else '2'),'nodes':nodes,'edges':edges,'messages':messages,'notes':notes,'kind':'flowchart','scope':'source business-example relationships and numbered report flows'}
 return data
