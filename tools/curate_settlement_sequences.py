"""Source-inspected Settlement/Reconciliation sequence reconstructions.

Manually maintained diagram transcriptions; not an inferred flow generator.
Source picture labels and optional groups are retained even when prose differs.
"""
import argparse,hashlib,json,re
from pathlib import Path
import kb

SID='src-000196';DATE='2026-11-09'
I='SecuritiesSettlementTransactionInstruction';S='SecuritiesSettlementTransactionStatusAdvice';C='SecuritiesSettlementTransactionConfirmation'
FI='SecuritiesFinancingInstruction';FS='SecuritiesFinancingStatusAdvice';FC='SecuritiesFinancingConfirmation';FM='SecuritiesFinancingModificationInstruction'
M='SecuritiesSettlementConditionsModificationRequest';MS='SecuritiesSettlementConditionModificationStatusAdvice';MSS='SecuritiesSettlementConditionsModificationStatusAdvice'
MR='SecuritiesSettlementTransactionModificationRequest';MRS='SecuritiesSettlementTransactionModificationRequestStatusAdvice'
CP='SecuritiesSettlementTransactionCounterpartyResponse'

def step(a,b,label):return (a,b,label)
def opt(*steps):return list(steps)
def s(a,b,label):return step(a,b,label)
def o(a,b,label):return opt(s(a,b,label))

# Label -> canonical participant slug. Multiple instances of one functional role
# remain separate lifelines; the source narrative specifies their relationship.
P2=[('A','Instructing Party','instructing-party'),('B','Executing Servicing Party','executing-servicing-party')]
F3=[('A','Securities Financing Instructing Party','financing-instructing-party'),('B','Securities Financing Servicing Party','financing-servicing-party'),('C','Settlement Executing Party','settlement-executing-party')]
F2=[F3[0],('B','Securities Financing Servicing Party/Settlement Executing Party','financing-servicing-settlement-executing-party')]
SPLIT=[('A','Client','split-settlement-client'),('B','Instructing/Splitting Party','instructing-splitting-party'),('C','Executing Servicing Party','executing-servicing-party'),('D','Instructing Party','instructing-party'),('E','Client','split-settlement-client')]
TS='SecSetTranStatusAdvice';TC='SecSetTranConfirmation'

DATA={
38:('Intra-position instruction and confirmation','intra-position-instruction',P2,[s('A','B','IntraPositionMovementInstruction'),o('B','A','IntraPositionMovementStatusAdvice'),s('B','A','IntraPositionMovementConfirmation')],[329,334],[]),
40:('Securities financing — three parties','financing-instruction-three-parties',F3,[s('A','B',FI),s('B','C',I+'(open)'),o('B','A',FS),o('C','B',S),o('B','A',FS),s('B','C',I+'(close)'),o('C','B',S),o('B','A',FS),s('C','B',C+' (open)'),s('C','B',C+' (close)'),s('B','A',C+' (open)'),s('B','A',C+' (close)')],[347,360],['The final two source-picture labels are SecuritiesSettlementTransactionConfirmation (open/close), whereas P358–P359 describes SecuritiesFinancingConfirmation. Both claims are preserved; this reconstruction follows the picture.']),
41:('Securities financing — two parties','financing-instruction-two-parties',F2,[s('A','B',FI),o('B','A',FS),o('B','A',FS+' (open)'),o('B','A',FS+' (close)'),s('B','A',FC+' (open)'),s('B','A',FC+' (close)')],[361,367],[]),
42:('Financing modification without position change — three parties','financing-modification-three-parties',F3,[s('A','B',FM),s('B','C','SecuritiesTransactionCancellationRequest'),s('B','C',I+'(close)'),o('B','A',FS),o('C','B',S),o('B','A',FS)],[369,377],[]),
43:('Financing modification without position change — two parties','financing-modification-two-parties',F2,[s('A','B',FM),o('B','A',FS),o('B','A',FS+' (close)')],[378,382],[]),
44:('Financing substitution — three parties','financing-substitution-three-parties',F3,[s('A','B',I+'(RF)'),s('B','C',I+'(RF)'),s('A','B',I+'(DF)'),s('B','C',I+'(DF)'),o('C','B',S),o('B','A',S),o('C','B',S),o('B','A',S),s('C','B',C+'(RF)'),s('B','A',C+'(RF)'),s('C','B',C+'(DF)'),s('B','A',C+'(DF)'),s('B','A',FS)],[383,394],[]),
45:('Financing top-up — three parties','financing-top-up-three-parties',F3,[s('A','B',I+'(DF)'),s('B','C',I+'(DF)'),o('C','B',S),o('B','A',S),s('C','B',C),s('B','A',C),s('B','A',FS)],[395,403],[]),
46:('Financing withdrawal — three parties','financing-withdrawal-three-parties',F3,[s('A','B',I+'(RF)'),s('B','C',I+'(RF)'),o('C','B',S),o('B','A',S),s('C','B',C),s('B','A',C),s('B','A',FS)],[404,414],[]),
47:('Financing substitution — two parties','financing-substitution-two-parties',F2,[s('A','B',I+'(RF)'),s('A','B',I+'(DF)'),o('B','A',S),o('B','A',S),s('B','A',C+'(RF)'),s('B','A',C+'(DF)'),s('B','A',FS)],[415,420],[]),
48:('Financing top-up — two parties','financing-top-up-two-parties',F2,[s('A','B',I+'(DF)'),o('B','A',S),s('B','A',C),s('B','A',FS)],[421,428],[]),
49:('Financing withdrawal — two parties','financing-withdrawal-two-parties',F2,[s('A','B',I+'(RF)'),o('B','A',S),s('B','A',C),s('B','A',FS)],[429,434],[]),
50:('Pair-off instruction sequence','pair-off',P2,[s('A','B',I),o('B','A',S),o('B','A',S),s('A','B',I),o('B','A',S),o('B','A',S),s('B','A','See payment messages')],[435,444],['“See payment messages” is a source cross-reference, not an exact supplied payment-message identifier. The narrative conditions the cash-difference step on successful cancellation and describes both payment directions; the picture shows only one generic arrow.']),
51:('Cash/securities split instruction and confirmation','cash-securities-split',[P2[0],('B','Securities/Cash Instruction Executing/Servicing Party','cash-securities-split-servicing-party'),('C','Securities Leg Executing Party','securities-leg-executing-party'),('D','Cash Leg Executing Party','cash-leg-executing-party')],[s('A','B',I+' (DVP/RVP Split)'),s('B','C',I+' (DF/RF)'),s('B','D','CashTransfer/CashAdvice'),o('C','B',S),o('B','A',S),s('C','B',C),s('B','A',C),s('D','B','ConfirmCashTransfer'),s('B','A','ConfirmCash')],[445,453],['CashTransfer/CashAdvice, ConfirmCashTransfer and ConfirmCash are retained as source labels. No particular payment schema is inferred from them.']),
52:('Release an instruction originally on hold','hold-release',P2,[s('A','B',I+' (Hold:Y)'),o('B','A',S),s('A','B',M+' (Release)'),o('B','A',MS),o('B','A',S),s('B','A',C)],[469,476],[]),
53:('Hold then release an instruction','released-held-released',P2,[s('A','B',I),o('B','A',S),s('A','B',M+' (Hold:Y)'),o('B','A',MS),o('B','A',S),s('A','B',M+' (Release)'),o('B','A',MS),o('B','A',S),s('B','A',C)],[477,487],[]),
54:('Processing change for one transaction','processing-change-one-transaction',P2,[s('A','B',M),o('B','A',MSS)],[488,496],['The picture uses plural “Conditions” in the status-advice name; the supplied exact definition is SecuritiesSettlementConditionModificationStatusAdvice. The diagram label is not silently corrected.']),
55:('Processing change for two transactions','processing-change-multiple-transactions',P2,[s('A','B',M+' (2 transactions)'),o('B','A',MSS+' (Transaction 1)'),o('B','A',S+' (Transaction 1)'),o('B','A',MSS+' (Transaction 2)'),o('B','A',S+' (Transaction 2)')],[497,502],['The picture uses plural “Conditions” in the status-advice name; the supplied exact definition uses singular “Condition”.']),
56:('Modification before settlement with counterparty response','modification-before-settlement',P2+[('C','Instructing Party','instructing-party')],[s('A','B',I),s('C','B',I),opt(s('B','A',S),s('B','A',S)),opt(s('B','C',S),s('B','C',S)),s('A','B',MR),o('B','C',S),o('C','B',CP),o('B','A',MRS),o('B','A',S)],[503,517],['The two Instructing Party lifelines are distinct counterparties in this flow, as stated at P507–P514. The status/request-status arrows are optional in the picture; P515 describes returning request status without explicitly stating optionality.']),
57:('Modification after settlement','modification-after-settlement',P2,[s('A','B',I),opt(s('B','A',S),s('B','A',S)),s('B','A',C),s('A','B',MR),o('B','A',MRS)],[518,526],['The picture marks modification-request status optional, while P525 says the servicing party sends it back. Preserve both presentations.']),
58:('Bilateral splitting — original instructions and cancellation','bilateral-splitting',SPLIT,[s('E','D','SecSetTransInx'),s('A','B','SecSetTransInx'),s('B','C','SecSetTransInx'),s('D','C','SecSetTransInx'),o('C','B',TS),o('C','D',TS),s('D','C','SecTransCxlRequest'),s('B','C','SecTransCxlRequest'),o('D','E','SecTransCxlReqStatusAdvice'),o('B','A','SecTransCxlReqStatusAdvice')],[527,543],['This is part 1 of the four source pictures for bilateral splitting; the original “Flow continues on next page” note is retained. Abbreviated message labels are preserved.']),
59:('Bilateral splitting — two replacement instructions','bilateral-splitting',SPLIT,[s('D','C','SecSetTransInstruction1'),s('B','C','SecSetTransInstruction1'),o('D','E',TS),o('B','A',TS),s('D','C','SecSetTransInstruction2'),s('B','C','SecSetTransInstruction2'),o('D','E',TS),o('B','A',TS)],[527,543],['This is part 2 of the bilateral-splitting source sequence. Instruction1 and Instruction2 are distinct replacements, not versions of a message definition.']),
60:('Bilateral splitting — status propagation','bilateral-splitting',SPLIT,[o('C','D',TS),o('C','B',TS),o('D','E',TS),o('B','A',TS),o('C','D',TS),o('C','B',TS),o('D','E',TS),o('B','A',TS)],[527,543],['This is part 3 of the bilateral-splitting source sequence. Eight separate optional status arrows are retained; similar labels are not deduplicated.']),
61:('Bilateral splitting — settlement confirmations','bilateral-splitting',SPLIT,[s('C','B',TC),s('B','A',TC),s('C','D',TC),s('D','E',TC),s('C','B',TC),s('B','A',TC),s('C','D',TC),s('D','E',TC)],[527,543],['This is part 4 of the bilateral-splitting source sequence. Both replacement transactions produce confirmations on both counterparties’ client chains.']),
62:('Unilateral splitting — instruction and split request','unilateral-splitting',SPLIT,[s('A','B','SecSetTransInx'),s('E','D','SecSetTransInx'),s('B','C','SecSetTransInx'),s('D','C','SecSetTransInx'),o('C','B',TS),o('C','D',TS),o('D','E',TS),o('B','A',TS),s('B','C','SecSetCondModRequest'),o('C','D','SecTrnsCxlReqStatusAdvice'),o('D','E','SecTrnsCxlReqStatusAdvice'),o('C','B','SecTrnsCxlReqStatusAdvice'),o('B','A','SecTrnsCxlReqStatusAdvice')],[544,563],['This is part 1 of the four source pictures for unilateral splitting. The condition-modification request and ensuing cancellation-request-status labels are retained as drawn; no replacement request is invented.']),
63:('Unilateral splitting — status propagation, first picture','unilateral-splitting',SPLIT,[o('C','D',TS),o('D','E',TS),o('C','B',TS),o('B','A',TS),o('C','D',TS),o('C','B',TS),o('D','E',TS),o('B','A',TS)],[544,563],['This is part 2 of the unilateral-splitting source sequence. The eight arrows and optional frames are preserved in their picture order.']),
64:('Unilateral splitting — status propagation, second picture','unilateral-splitting',SPLIT,[o('C','D',TS),o('D','E',TS),o('C','B',TS),o('B','A',TS),o('C','D',TS),o('D','E',TS),o('C','B',TS),o('B','A',TS)],[544,563],['This is part 3 of the unilateral-splitting source sequence. The similar preceding picture is not byte-identical; this picture has different vertical ordering of the last status arrows and remains separate.']),
65:('Unilateral splitting — settlement confirmations','unilateral-splitting',SPLIT,[s('C','D',TC),s('D','E',TC),s('C','B',TC),s('B','A',TC),s('C','D',TC),s('D','E',TC),s('C','B',TC),s('B','A',TC)],[544,563],['This is part 4 of the unilateral-splitting source sequence. Confirmation order follows this picture, independently of the bilateral scenario.']),
66:('Allegement and counterparty response','allegement',[('A','Instructing Party','instructing-party'),('B','Executing/Servicing Party','executing-servicing-party'),('C','Instructing Party','instructing-party')],[s('C','B',I),s('B','A','SecuritiesSettlementTransactionAllegementNotification'),o('A','B',CP),s('B','C',S),o('A','B',I),o('B','A','SecuritiesSettlementTransactionAllegementRemovalAdvice')],[564,571],['The left and right Instructing Party lifelines are the alleged and alleging parties respectively (P565–P570). The picture removal-advice label includes “Transaction”; the exact supplied definition and P570 omit that word.']),
67:('Reporting push mode with third party','reporting-push',P2+[('C','Third Party','reporting-third-party')],[s('B','A','SecuritiesBalanceCustodyReport'),s('B','A','SecuritiesBalanceAccountingReport'),s('B','A','SecuritiesTransactionPostingReport'),s('B','A','SecuritiesTransactionPendingReport'),s('B','A','SecuritiesSettlementTransactionAllegementReport'),s('B','A','IntraPositionMovementPostingReport'),s('B','C','SecuritiesSettlementTransactionAuditTrailReport')],[572,590],['The picture lists available reports. Narrative P582 and account setup determine which reports are supplied; the list is not a requirement to send every report every time.']),
68:('Reporting pull mode with third party','reporting-pull',P2+[('C','Third Party','reporting-third-party')],[s('A','B','SecuritiesStatementQuery'),s('C','B','SecuritiesTransactionStatusQuery'),s('A','B','SecuritiesTransactionStatusQuery'),o('B','A','SecuritiesStatusOrStatementQueryStatusAdvice'),o('B','C','SecuritiesStatusOrStatementQueryStatusAdvice'),s('B','A','SecuritiesBalanceCustodyReport'),s('B','A','SecuritiesBalanceAccountingReport'),s('B','A','SecuritiesTransactionPostingReport'),s('B','A','SecuritiesTransactionPendingReport'),s('B','A','SecuritiesSettlementTransactionAllegementReport'),s('B','C','SecuritiesSettlementTransactionAuditTrailReport'),s('B','A','IntraPositionMovementPostingReport')],[591,605],['The source narrative describes alternative requested statements and optional query-status responses. The list of report arrows is not a requirement to return every report for a query.']),
72:('Portfolio transfer settlement details','portfolio-transfer',[('A','Executing Servicing Party','executing-servicing-party'),('B','Third Party','portfolio-settlement-third-party'),('C','Executing Servicing Party','executing-servicing-party')],[s('C','A','PortfolioTransfer (Delivering settlement details)'),s('A','C','PortfolioTransfer (Receiving settlement details)'),s('A','B','SecuritiesSettlementInstruction (Delivery free)'),s('C','B','SecuritiesSettlementInstruction (Receipt free)')],[627,631],['The source uses generic PortfolioTransfer and SecuritiesSettlementInstruction labels. It does not label the middle Third Party as the client; the client is separately required by the activity narrative. The delivering/receiving detail labels and settlement directions are retained exactly rather than inferred from the left/right lifeline position.']),
}

NEW_PARTICIPANTS={
 'financing-instructing-party':('Securities Financing Instructing Party','Functional participant that sends the financing instruction or modification and receives financing status/confirmation in the financing scenarios.',[346,349,350,357,358,359,362,363,366,373,376,380,381],['Securities Financing Instructing Party']),
 'financing-servicing-party':('Securities Financing Servicing Party','Functional participant that receives a financing instruction, instructs opening/closing settlement legs through a settlement executing party, and returns status/confirmation to the financing instructing party.',[348,349,350,351,354,357,358,359,373,374,376],['Securities Financing Servicing Party']),
 'settlement-executing-party':('Settlement Executing Party','Functional participant that receives settlement-leg instructions and supplies their status and confirmation to the securities financing servicing party.',[348,351,352,353,354,355,356,358,359,374,375],['Settlement Executing Party']),
 'financing-servicing-settlement-executing-party':('Securities Financing Servicing Party / Settlement Executing Party','The two-party financing scenario explicitly combines financing servicing and settlement execution in the same participant. The participant creates and manages the two settlement legs and returns their financing statuses and confirmations.',[362,363,364,365,366,379,380,381],['Securities Financing Servicing Party/Settlement Executing Party','Securities Financing Servicing Party / Settlement Executing Party']),
 'cash-securities-split-servicing-party':('Securities/Cash Instruction Executing/Servicing Party','Receives a versus-payment settlement instruction, separates it into securities and cash legs, and relays status and completion information from the leg executing parties.',[446,447,448,449,450,451,452],['Securities/Cash Instruction Executing/Servicing Party','Securities/Cash instruction Executing/Servicing Party']),
 'securities-leg-executing-party':('Securities Leg Executing Party','Executes the securities leg in the cash/securities split scenario and provides status and settlement confirmation to the participant that split the instruction.',[446,448,449,450,451],['Securities Leg Executing Party']),
 'cash-leg-executing-party':('Cash Leg Executing Party','Executes the cash transfer in the cash/securities split scenario and confirms it to the participant that split the instruction.',[446,448,452],['Cash Leg Executing Party']),
 'portfolio-settlement-third-party':('Third Party — portfolio settlement diagram','Source diagram fig-0072 identifies a Third Party receiving Delivery free and Receipt free settlement instructions. The figure supplies no independent definition or identifier scheme for this label.',[627,628,629,630],['Third Party']),
 'instructing-splitting-party':('Instructing/Splitting Party','The functional participant requesting replacement of an existing settlement instruction by two or more instructions. In bilateral splitting both trade parties instruct and match; in unilateral splitting only one party instructs the split.',[528,530,531,532,533,534,535,537,545,546,547,548,549,550,551,552],['Instructing/Splitting Party','Instructing Splitting Party']),
 'split-settlement-client':('Client — split settlement','A client sends the original settlement instruction through its instructing/splitting party or instructing party and receives relayed statuses and confirmations. Each side of the trade has a separately depicted client instance.',[531,532,533,534,535,537,546,547,548,549,551,552],['Client']),
}
ACTIVITY_TABLES={38:29,40:31,41:32,42:33,43:34,50:35,51:36,52:37,53:37,54:38,55:38,56:39,57:40,58:41,59:41,60:41,61:41,62:41,63:41,64:41,65:41,66:42,67:43,68:44,72:48}
def flow_title(slug,title):return {'bilateral-splitting':'Bilateral splitting','unilateral-splitting':'Unilateral splitting'}.get(slug,title)

def main(root):
 source=next(s for s in kb.sources(root) if s['source_id']==SID);base=root/source['set_path'];out=base/'diagrams/settlement-sequences';flows=base/'flows'
 records=json.loads((root/'work/documents'/SID/'records.json').read_text(encoding='utf-8'))
 paragraphs={int(p['paragraph_id'][1:]):p for p in records['paragraphs']}
 inv=json.loads((root/'work/documents'/SID/'media-review-inventory.json').read_text(encoding='utf-8'))
 media={int(re.search(r'image(\d+)',m['original']).group(1)):m for m in inv['media']}
 defs=json.loads((root/'work/documents/src-000197/message-definitions.json').read_text(encoding='utf-8'))
 name_ids={re.sub(r'V\d+$','',d['title'].split(' ',2)[-1]):d['message_id'] for d in defs}
 # Explicit source picture/name variations are documented on each diagram.
 aliases={MSS:MS,'SecuritiesSettlementTransactionAllegementRemovalAdvice':'SecuritiesSettlementAllegementRemovalAdvice','SecSetTransInx':I,'SecSetTransInstruction1':I,'SecSetTransInstruction2':I,TS:S,TC:C,'SecTransCxlRequest':'SecuritiesTransactionCancellationRequest','SecTransCxlReqStatusAdvice':'SecuritiesTransactionCancellationRequestStatusAdvice','SecTrnsCxlReqStatusAdvice':'SecuritiesTransactionCancellationRequestStatusAdvice','SecSetCondModRequest':M}
 def participant_path(slug):return root/'shared/reference/participants'/('settlement-reconciliation-'+slug+'.md')
 def statements(numbers):return '\n\n'.join('**'+SID+' P'+str(n)+'** — '+paragraphs[n]['text'] for n in numbers if n in paragraphs and paragraphs[n]['text'].strip())
 def locator(numbers):return [{'source_id':SID,'paragraph_id':'P'+str(n),'heading_path':paragraphs[n].get('heading_path',[]),'xml_path':paragraphs[n]['xml_path']} for n in numbers if n in paragraphs]
 def messages(steps):
  labels=[x[2] for item in steps for x in (item if isinstance(item,list) else [item])];found={}
  for label in labels:
   name=re.sub(r'\s*\(.*','',label).strip();key=aliases.get(name,name)
   if key in name_ids:found[name_ids[key]]=key
  return found
 for slug,(title,definition,nums,labels) in NEW_PARTICIPANTS.items():
  page=participant_path(slug);using=list({d[1]:d for d in DATA.values() if any(p[2]==slug for p in d[2])}.values());mids=sorted({m for d in DATA.values() if any(p[2]==slug for p in d[2]) for m in messages(d[3])})
  metadata={'template':False,'document_kind':'participant','review_status':'needs-review','participant_id':'participant-settlement-reconciliation-'+slug,'title':title,'domain':'securities','domains':['securities'],'source_ids':[SID],'source_labels':labels,'aliases':[],'message_sets':['settlement-and-reconciliation'],'source_locations':locator(nums),'message_ids':mids,'flow_ids':['flow-settlement-reconciliation-'+d[1] for d in using],'role_kind':'functional participant role','updated':DATE,'limitations':['This definition is scoped to the cited scenarios. Institution examples do not define or fix the role.','No identifier scheme is specified in these source paragraphs.']}
  body=kb.front(metadata)+'# '+title+'\n\n## Definition and context\n\n'+definition+'\n\n'+kb.source_link(root,page,source)+'; '+', '.join('P'+str(n) for n in nums)+'.\n\n## Responsibilities, relationships and evidence\n\n'+statements(nums)+'\n\n## Applicable flows\n\n'+'\n'.join('- '+kb.link(page,flows/(d[1]+'.md'),flow_title(d[1],d[0])) for d in using)+'\n\n## Identifier schemes and ambiguity\n\nNo identifier scheme is specified in the cited role narrative. The source examples do not make this role identical to a particular institution. A compound participant in a two-party scenario does not merge the separate three-party role definitions.\n'
  if slug=='portfolio-settlement-third-party':body+='\nThe middle diagram lifeline is not equated with the portfolio client or the reporting Third Party. The activity narrative separately names the client and CSD; the figure itself only supplies the label Third Party.\n'
  kb.put(page,body)
 outputs=[]
 for number,(title,slug,people,steps,span,notes) in DATA.items():
  item=media[number];occ=item['occurrences'][0];page=out/(f'fig-{number:04d}.md');mmd=out/(f'fig-{number:04d}.mmd');flow=flows/(slug+'.md');mids=messages(steps)
  code='sequenceDiagram\n'
  for key,label,role in people:code+='  participant '+key+' as '+label+'\n'
  rows=[];num=0
  for entry in steps:
   optional=isinstance(entry,list);entries=entry if optional else [entry]
   if optional:code+='  opt Optional\n'
   for a,b,label in entries:
    num+=1;code+=('    ' if optional else '  ')+a+'->>'+b+': '+label+'\n';rows.append([num,a+' → '+b,label,'Optional' if optional else 'No optional boundary drawn'])
   if optional:code+='  end\n'
  if number in (58,59,60,62,63,64):code+='  Note over A,E: Flow continues on next page\n'
  metadata={'template':False,'document_kind':'diagram','review_status':'needs-review','manual_curated':True,'diagram_id':f'fig-{number:04d}','title':title,'domain':'securities','source_ids':[SID],'source_editions':['March 2026'],'message_sets':['settlement-and-reconciliation'],'message_ids':sorted(mids),'participant_ids':sorted({'participant-settlement-reconciliation-'+p[2] for p in people}),'flow_ids':['flow-settlement-reconciliation-'+slug],'content_origin':'source-reconstruction','diagram_kind':'sequenceDiagram','original_asset':item['original'],'source_locations':[{'source_id':SID,'locator':occ['source_locator'],'heading_path':occ['heading_path'],'xml_path':occ['xml_path'],'figure_id':occ['figure_id']}],'render_status':'not-run','visual_review':'not-run','limitations':notes+['Native sequence arrows preserve direction and ordering; no synchronous/asynchronous execution semantics are inferred from the source arrow glyph.'],'updated':DATE}
  text=kb.front(metadata)+'# '+title+'\n\n'+kb.source_link(root,page,source)+'; '+occ['source_locator']+'; '+ ' / '.join(occ['heading_path'])+'; `'+occ['xml_path']+'`.\n\n'+kb.link(page,root/item['original'],'Original image')+' · '+kb.link(page,flow,'Business flow and narrative responsibilities')+'\n\n'
  text+='## Source reconstruction\n\n```mermaid\n'+code+'```\n\n## Actors and relationships\n\n'
  for key,label,role in people:text+='- **'+key+' — '+label+'**: '+kb.link(page,participant_path(role),'canonical functional participant')+'.\n'
  text+='\nThe source picture is a sequence of directed communications. Each optional rectangle is preserved as its own native optional block, including multiple messages inside the same rectangle. Repeated arrows are separate occurrences, not deduplicated. Building pictograms are replaced with labelled participant lifelines without assigning a particular institution.\n\n'+kb.table(['Order','Direction','Source label','Source optionality'],rows)
  text+='## Message definitions in the supplied edition\n\n'+('\n'.join('- '+kb.link(page,root/'domains/securities/reference/messages'/mid/'index.md',mid+' — '+name) for mid,name in sorted(mids.items())) if mids else 'No exact message identifier is established from the diagram labels alone.')+'\n\nNames are linked to the exact definitions in supplied Part2. Labels retained from the picture are shown in the ordered table above; generic labels are not assigned an invented message ID.\n\n'
  if notes:text+='## Source qualifications and discrepancies\n\n'+'\n'.join('- '+x for x in notes)+'\n\n'
  text+='## Rendering and visual review\n\nPending parse/render and comparison of the reconstruction with the inspected original. The original image is retained; no visual-review pass is claimed by this generation step.\n'
  kb.put(mmd,code);kb.put(page,text)
  evidence=root/occ['evidence_page'];em,eb=kb.metadata(evidence);em['canonical_diagram']=page.relative_to(root).as_posix();em['disposition']='canonical-reconstruction-created-needs-review'
  eb=re.sub(r'\n<!-- CANONICAL-SEQUENCE-START -->.*?<!-- CANONICAL-SEQUENCE-END -->\n?','\n',eb,flags=re.S)
  kb.put(evidence,kb.front(em)+eb.strip()+'\n\n<!-- CANONICAL-SEQUENCE-START -->\n'+kb.link(evidence,page,'Canonical sequence reconstruction, roles and review evidence')+'\n<!-- CANONICAL-SEQUENCE-END -->\n')
  # Existing curated pilot flow prose is preserved and gains a generated source
  # diagram/narrative appendix. New flows are focused source-grounded references.
  related_images=[(n,d) for n,d in DATA.items() if d[1]==slug]
  all_flow_notes=sorted({note for _,d in related_images for note in d[5]})
  all_flow_messages={mid:name for _,d in related_images for mid,name in messages(d[3]).items()}
  appendix='\n<!-- SETTLEMENT-SEQUENCE-START -->\n## Source sequence and full scenario evidence\n\n'+'\n'.join('- '+kb.link(flow,out/(f'fig-{n:04d}.md'),d[0]) for n,d in related_images)+'\n\n'+SID+' P'+str(span[0])+'–P'+str(span[1])+'.\n\n'
  appendix+='### Participants in this source sequence\n\n'+'\n'.join('- '+key+' — '+label+': '+kb.link(flow,participant_path(role),'canonical participant') for key,label,role in people)+'\n\n'
  appendix+='### Ordered activities, conditions and outcomes\n\nThe following source paragraphs retain conditions, alternatives, actor responsibilities and message directions in narrative order. Figure ordering is preserved separately; neither is silently used to erase a disagreement.\n\n'
  nums=[n for n in range(span[0],span[1]+1) if n in paragraphs and paragraphs[n]['text'].strip()]
  appendix+=statements(nums)+'\n\n'
  if number in ACTIVITY_TABLES:
   tid=ACTIVITY_TABLES[number];tp=base/'documents'/SID/'tables'/f'tbl-{tid:04d}.md'
   appendix+='### Source activity responsibilities\n\n'+kb.link(flow,tp,'Activity table T'+str(tid)+' — all steps, descriptions and source Initiator values')+'. The table’s Initiator column concerns the named activity and is not automatically the sender of every message.\n\n'
  if all_flow_notes:appendix+='### Source-specific qualifications\n\n'+'\n'.join('- '+x for x in all_flow_notes)+'\n\n'
  appendix+='<!-- SETTLEMENT-SEQUENCE-END -->\n'
  if flow.exists():
   fm,fb=kb.metadata(flow);fb=re.sub(r'\n<!-- SETTLEMENT-SEQUENCE-START -->.*?<!-- SETTLEMENT-SEQUENCE-END -->\n?','\n',fb,flags=re.S)
   if slug in ('bilateral-splitting','unilateral-splitting'):fm['title']=flow_title(slug,title);fb=re.sub(r'^\s*# .*', '# '+fm['title'],fb,count=1,flags=re.M)
   fm['limitations']=sorted(set(fm.get('limitations',[]))|set(all_flow_notes))
   fm['source_locations']=fm.get('source_locations',[])+[x for x in locator(nums) if x not in fm.get('source_locations',[])]
   fm['participant_ids']=sorted(set(fm.get('participant_ids',[]))|{'participant-settlement-reconciliation-'+p[2] for p in people});fm['message_ids']=sorted(set(fm.get('message_ids',[]))|set(all_flow_messages));fm['diagram_ids']=sorted(set(fm.get('diagram_ids',[]))|{f'fig-{n:04d}' for n,_ in related_images});kb.put(flow,kb.front(fm)+fb.rstrip()+'\n'+appendix)
  else:
   fm={'template':False,'document_kind':'business-flow','review_status':'needs-review','title':flow_title(slug,title),'flow_id':'flow-settlement-reconciliation-'+slug,'domain':'securities','source_ids':[SID],'source_editions':['March 2026'],'message_sets':['settlement-and-reconciliation'],'source_locations':locator(nums),'message_ids':sorted(all_flow_messages),'participant_ids':sorted({'participant-settlement-reconciliation-'+p[2] for p in people}),'diagram_ids':[f'fig-{n:04d}' for n,_ in related_images],'updated':DATE,'limitations':all_flow_notes+['This scenario does not supply a separate formal precondition/postcondition list; conditions and outcomes are retained from the cited narrative.','The source sequence may intentionally omit surrounding participants or unsuccessful paths. No absent path is asserted impossible.']}
   kb.put(flow,kb.front(fm)+'# '+fm['title']+'\n\n## Purpose, trigger and boundaries\n\nThe source-defined scenario is **'+fm['title']+'**. Its trigger, acting participants, conditions, outcomes and alternatives are retained in the precise paragraph evidence below. No additional preconditions or failure paths are inferred from the picture.\n'+appendix)
  outputs.append({'source_id':SID,'source_figure_id':occ['figure_id'],'original':item['original'],'original_sha256':item['original_sha256'],'path':page.relative_to(root).as_posix(),'mermaid_sha256':hashlib.sha256(mmd.read_bytes()).hexdigest(),'flow_path':flow.relative_to(root).as_posix(),'message_arrows':num,'optional_groups':sum(isinstance(x,list) for x in steps),'participant_lifelines':len(people),'source_inspection':'Original image directly inspected at full available resolution; every label, direction, order and optional boundary transcribed.','reconstruction_visual_review':'pending-render-comparison','limitations':notes})
 # Bidirectional navigation is derived from these maintained scenario records.
 by_person={};by_message={}
 for d in DATA.values():
  for _,_,role in d[2]:by_person.setdefault(role,{})[d[1]]=flow_title(d[1],d[0])
  for mid in messages(d[3]):by_message.setdefault(mid,{})[d[1]]=flow_title(d[1],d[0])
 for role,related in by_person.items():
  pp=participant_path(role);pm,pb=kb.metadata(pp);pm['flow_ids']=sorted(set(pm.get('flow_ids',[]))|{'flow-settlement-reconciliation-'+slug for slug in related})
  pb=re.sub(r'\n<!-- SETTLEMENT-FLOW-LINKS-START -->.*?<!-- SETTLEMENT-FLOW-LINKS-END -->\n?','\n',pb,flags=re.S)
  pb+='\n<!-- SETTLEMENT-FLOW-LINKS-START -->\n## Additional source-scoped settlement flows\n\n'+'\n'.join('- '+kb.link(pp,flows/(slug+'.md'),title) for slug,title in sorted(related.items()))+'\n<!-- SETTLEMENT-FLOW-LINKS-END -->\n';kb.put(pp,kb.front(pm)+pb.strip()+'\n')
 for mid,related in by_message.items():
  mp=root/'domains/securities/reference/messages'/mid/'index.md';old=mp.read_text(encoding='utf-8-sig');old=re.sub(r'\n<!-- SETTLEMENT-FLOW-LINKS-START -->.*?<!-- SETTLEMENT-FLOW-LINKS-END -->\n?','\n',old,flags=re.S)
  old+='\n<!-- SETTLEMENT-FLOW-LINKS-START -->\n## Source-scoped settlement flows\n\n'+'\n'.join('- '+kb.link(mp,flows/(slug+'.md'),title) for slug,title in sorted(related.items()))+'\n<!-- SETTLEMENT-FLOW-LINKS-END -->\n';kb.put(mp,old)
 # Record every original object classification, without claiming a detailed
 # visual review of source images inspected only in labelled contact sheets.
 classpath=root/'tracking/reviews/docx-media-classification.json'
 old=json.loads(classpath.read_text(encoding='utf-8')) if classpath.exists() else {'records':[]}
 old_records=old.get('records',[]) if isinstance(old,dict) else old
 classes=[x for x in old_records if x['source_id']!=SID]
 for number,item in sorted(media.items()):
  legend=number in (6,7,8,9)
  classes.append({'source_id':SID,'original':item['original'],'sha256':item['original_sha256'],'disposition':'retained-notation-legend' if legend else 'substantive-diagram','classification_review':'pass','classification_review_date':DATE,'classification_review_scope':'Visual content classification from six labelled contact sheets; not a reconstruction review.','classification_reason':'Activity-diagram start, end, decision or synchronization symbol; substantive legend in source table T27, retained there with original asset.' if legend else 'Source business-role, activity, status, communication overview or sequence diagram; requires dedicated reconstruction and review.'})
 kb.dump(classpath,dict(old if isinstance(old,dict) else {},records=classes))
 kb.dump(root/'work/settlement-sequences.json',{'date':DATE,'source_id':SID,'source_sha256':source['sha256'],'outputs':outputs,'classified_media':len(media),'substantive_diagrams':len(media)-4,'retained_notation_legend_assets':4})
 index=out/'index.md';kb.put(index,kb.front({'template':False,'document_kind':'diagram-index','review_status':'needs-review','domain':'securities','source_ids':[SID],'message_sets':['settlement-and-reconciliation'],'limitations':['Rendering and source comparison status is recorded per diagram.']})+'# Settlement sequence reconstructions\n\n'+kb.table(['Source figure','Reconstruction','Flow','Review'],[[x['source_figure_id'],kb.link(index,root/x['path'],Path(x['path']).stem),kb.link(index,root/x['flow_path'],Path(x['flow_path']).stem),x['reconstruction_visual_review']] for x in outputs]))
 if (root/'tracking/reviews/settlement-sequences.json').exists():
  from record_settlement_sequence_review import main as restore_review
  restore_review(root)
 print(json.dumps({'sequence_reconstructions':len(outputs),'new_participant_records':len(NEW_PARTICIPANTS),'classified_media':len(media),'substantive_diagrams':len(media)-4,'legend_assets':4}))

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);main(parser.parse_args().root.resolve())
