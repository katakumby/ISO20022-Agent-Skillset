from pathlib import Path
import sys,json,re,hashlib
sys.path.insert(0,str(Path('tools').resolve()));import kb
root=Path('.').resolve();s=next(s for s in kb.sources(root) if s['source_id']=='src-000180');base=root/s['set_path'];rec=json.loads((root/'work/documents/src-000180/records.json').read_text(encoding='utf-8'));defs=json.loads((root/'work/documents/src-000181/message-definitions.json').read_text(encoding='utf-8'))
def put(p,t):
 if p.exists() and p.read_text(encoding='utf-8')!=t:
  h=hashlib.sha256(p.read_bytes()).hexdigest()[:10];dest=root/'tracking/history/job-000001/manual-curation-2026-11-09'/p.relative_to(root);dest=dest.with_name(dest.stem+'-'+h+dest.suffix);dest.parent.mkdir(parents=True,exist_ok=True)
  if not dest.exists():dest.write_bytes(p.read_bytes())
 kb.put(p,t)
prefix='participant-src-000180-'
roles={
'B':('executingBroker','FinancialInstitution','ExecutingBroker','broker-executing-broker'),
'C':('centralMatchingUtility','System','CentralMatchingUtility','central-matching-utility-cmu'),
'I':('investmentManager','BusinessActor','InvestmentManager','investment-manager'),
'T':('trustee','BusinessActor','Trustee','trustee'),
'F':('institutionalInvestor','FinancialInstitution','InstitutionalInvestor','institutional-investor'),
'U':('underwriter','FinancialInstitution','Underwriter','underwriter'),
'A':('transferAgent','BusinessActor','TransferAgent','transfer-agent'),
'K':('cashCorrespondent','BusinessActor','CashCorrespondent','cash-correspondent'),
'P':('primeBroker','FinancialInstitution','PrimeBroker','prime-broker')}
newroles=[('trustee','Trustee','P147/P195; image11/P196; P233-P284','The participant that receives forwarded trade confirmations and, if it agrees with the trade details, returns an affirmation to the central matching utility. Other scenarios describe disaffirmation, cancellation receipt, and end-of-process reporting.','Receives confirmations from the CMU; compares the details; affirms or disaffirms; receives forwarded cancellations and end-of-process reports.','The label Trustee in these diagrams is not automatically merged with Custodian or Trust Bank; no institution-level equivalence is established.'),('institutional-investor','Institutional Investor','P154/P204/P209; image13/P205; image14/P210','The own-account-trade participant to which the CMU forwards the executing broker confirmation and from which an affirmation or disaffirmation is received.','Compares confirmation details with its own trade details; affirms when agreed, or disaffirms irreconcilable details.','The source notes an analogous Underwriter/Issuer Agent flow; this is an alternative pair of actors, not an assertion that Institutional Investor and Issuer Agent are equivalent.'),('issuer-agent','Issuer Agent','image13/P205 and image14/P210, note below sequence; activity image5/P155 label','An actor named in the source note as an alternative recipient in an analogous flow with an Underwriter. A standalone definition is not supplied in these passages.','Participates in the alternative Underwriter-to-Issuer-Agent confirmation flow identified by the source figure note.','Kept distinct from Institutional Investor and Underwriter; the source supplies an analogous flow, not an identity equivalence.'),('cash-correspondent','Cash Correspondent','P222/P223/P224; images15-17/P216/P220/P224','The diagram participant that receives a forwarded confirmation after the Transfer Agent response in the duplex flow and can send a confirmation response; the rejection scenario is explicitly titled Rejection by Cash Correspondent.','Receives a forwarded confirmation; returns a response; may reject trade details and receive a forwarded cancellation.','The same narrative passages use Cash Settlement Agent while artwork labels Cash Correspondent. Both labels and their source correspondence are recorded; no general institutional equivalence is assumed.')]
for slug,title,loc,definition,actions,lim in newroles:
 p=root/'shared/reference/participants'/(prefix+slug+'.md')
 if p.exists():continue
 m={'template':False,'document_kind':'participant','review_status':'needs-review','manual_curated':True,'domain':'securities','domains':['securities'],'participant_id':prefix+slug,'title':title,'source_labels':[title],'role_type':'source-scoped business actor in flow','source_ids':['src-000180'],'source_editions':[s['source_edition']],'source_locations':[{'source_id':'src-000180','locator':loc}],'message_sets':['post-trade-matching'],'message_ids':[],'flows':[],'aliases':[],'search_terms':[title],'limitations':[lim,'No identifier scheme is specified in these source passages.']}
 b='# '+title+'\n\n## Definition and context\n\n'+definition+'\n\n## Responsibilities and relationships\n\n'+actions+'\n\n'+lim+'\n\nSource: '+kb.source_link(root,p,s)+'; '+loc+'. No identifier scheme is specified.\n';put(p,kb.front(m)+b)
names={'c':'SecuritiesTradeConfirmation','s':'SecuritiesTradeConfirmationStatusAdvice','r':'SecuritiesTradeConfirmationResponse','x':'SecuritiesTradeConfirmationCancellation','e':'SecuritiesEndOfProcessReport','d':'DeliveryAmountReport'}
through='BCc ICc CTc CTc TCr CBs';own='BCc CFc FCr CBs';duplex='UCc CAc ACr CKc KCr CUs';nodist='BCc CIs CBs ICc CIs CBs';dist='BCc CIc ICc CIs CBs';bilateral='BCc CPs CBs PCc CBs CPs'
# Explicit source arrow order; lower-case final letter selects the exact message label.
specs=[
(11,194,196,146,'BCIT',through,None),
(12,198,200,146,'BCIT',through+' BCx ICx CTx CTx CIs CBs',None),
(13,203,205,153,'BCF',own,'alternative-actors'),
(14,208,210,153,'BCF',own+' BCx CFx CBs','alternative-actors'),
(15,214,216,159,'UCAK',duplex,None),
(16,218,220,159,'UCAK','UCc CAc ACr CUs UCx CAx CUs',None),
(17,222,224,159,'UCAK',duplex+' UCx CAx CKx CUs',None),
(18,227,229,165,'BCIT',through+' BCd CTd BCe ICe CTe CTe','proprietary-report'),
(19,232,234,173,'BCIT',nodist+' CTc CTc TCr CBs',None),
(20,237,239,173,'BCIT',nodist+' ICx BCx CIs CBs','alternative-cancellations'),
(21,241,243,173,'BCIT',nodist+' BCx CIx CBs CTx CTx',None),
(22,245,247,173,'BCIT',nodist+' ICx CBx CIs CTx CTx',None),
(23,249,251,173,'BCIT',nodist+' CTc CTc TCr CBs BCx CIx CBs CTx CTx','source-conflict'),
(24,255,257,180,'BCIT',dist+' CTc CTc TCr CBs',None),
(25,260,262,180,'BCIT',dist+' BCx CIx CBs CTx CTx','source-conflict'),
(26,265,267,180,'BCIT',dist+' ICx CBx CIs CTx CTx',None),
(27,269,271,180,'BCIT',dist+' CTc CTc TCr CBs BCx CIx CBs CTx CTx','source-conflict'),
(28,274,276,185,'BCP',bilateral,'securities-financing'),
(29,278,280,185,'BCP',bilateral+' BCx PCx CBs CPs','securities-financing-cancel'),
(30,283,285,173,'BCIT',nodist+' ICe CTc CTe','pre-advice')]
report=[]
for n,start,para,activity,actors,seq,note in specs:
 fig=next(f for f in rec['figures'] if any(i['target']=='media/image'+str(n)+'.png' for i in f['images']));fid=fig['figure_id'];title=fig['heading_path'][-1];dp=base/'diagrams/business-transactions'/(fid+'.md');flow=next((base/'flows').glob('flow-src-000180-p'+str(start)+'-*.md'));fm,fb=kb.metadata(flow);actflow=next((base/'flows').glob('flow-src-000180-p'+str(activity)+'-*.md'));steps=[{'sender':v[0],'receiver':v[1],'message':names[v[2]]} for v in seq.split()];pids=[prefix+roles[k][3] for k in actors];extra=[]
 if note=='alternative-actors':extra=[prefix+'underwriter',prefix+'issuer-agent']
 if n in [15,16,17]:extra=[prefix+'cash-settlement-agent']
 mapping=[]
 for name in sorted(set(x['message'] for x in steps)):
  dd=[d for d in defs if re.search(r'\b'+re.escape(name)+r'V\d+\b',d['title'])]
  if len(dd)==1:mapping.append({'source_label':name,'message_id':dd[0]['message_id'],'source_id':'src-000181','locator':f"file pages {dd[0]['start_page']}-{dd[0]['end_page']}; "+dd[0]['title']})
 code='---\nconfig:\n  sequence:\n    actorMargin: 35\n    messageMargin: 25\n    mirrorActors: false\n---\nsequenceDiagram\n'
 for k in actors:
  inst,kind,label,slug=roles[k];code+='    participant '+k+' as '+inst+':<br/>«'+kind+'»<br/>'+label+'\n'
 for i,step in enumerate(steps,1):
  code+='    '+step['sender']+'->>+'+step['receiver']+': '+step['message']+'\n    deactivate '+step['receiver']+'\n'
  if note=='proprietary-report' and i==7:code+='    Note left of B: The DeliveryAmountReport<br/>is a Proprietary message\n'
  if note=='pre-advice' and i==8:code+='    Note right of T: Pre advice\n'
 if note=='alternative-actors':code+='    Note over B,F: The flow may also be carried out between<br/>Underwriter and Issuer Agent\n'
 if note=='securities-financing':code+='    Note over B,P: This also applies for Securities Financing Or Off Exchange.<br/>It will not be used to broadcast available securities.\n'
 if note=='securities-financing-cancel':code+='    Note over B,P: This also applies for Securities Financing Or Off exchange.\n'
 issues=['issue-000031'] if note=='source-conflict' else [];limits=['The source sequence is a typical scenario, not a statement that every displayed path is mandatory in all cases. Narrative conditions and alternative new-confirmation/cancellation paths remain in the linked flow.','Source execution markers are retained on receiving lifelines; vertical spacing is adjusted and does not express elapsed time. The original retains exact marker lengths and presentation details.']
 if note=='source-conflict':limits.append('The final narrative sentence assigns a received cancellation to the investment manager although the preceding text and artwork show broker initiation; source contradiction retained under issue-000031.')
 m={'template':False,'document_kind':'diagram','review_status':'needs-review','manual_curated':True,'domain':'securities','diagram_id':fid,'title':title,'diagram_kind':'sequence','content_origin':'source-reconstruction','source_ids':['src-000180'],'source_editions':[s['source_edition']],'source_locations':[{'source_id':'src-000180','locator':' / '.join(fig['heading_path'])+'; P'+str(para)+'; word/media/image'+str(n)+'.png'}],'participants':pids,'flow_ids':[fm['flow_id']],'message_ids':sorted(x['message_id'] for x in mapping),'message_mapping_evidence':mapping,'issue_ids':issues,'render_status':'not-run','visual_review':'not-run','limitations':limits}
 original=root/'domains/securities/assets/src-000180/originals'/('image'+str(n)+'.png');body='# '+title+'\n\n## Source evidence\n\n'+kb.source_link(root,dp,s)+'; P'+str(para)+' and preceding scenario narrative P'+str(start+1)+'. '+kb.link(dp,original,'Unchanged full source figure')+'.\n\n![Source sequence]('+kb.rel(dp,original)+')\n\n## Mermaid reconstruction\n\n```mermaid\n'+code+'```\n\n## Participants and ordered exchanges\n\nSource instance names and stereotypes are retained in the diagram labels. Each occurrence links to a scoped participant record; a source business-actor label is not an assertion that a named institution always plays that role.\n\n'+kb.table(['Source instance / stereotype / label','Canonical scoped role'],[[roles[k][0]+' / '+roles[k][1]+' / '+roles[k][2],kb.link(dp,root/'shared/reference/participants'/(prefix+roles[k][3]+'.md'),roles[k][2])] for k in actors])+'\n'
 rows=[]
 for i,st in enumerate(steps,1):
  bind=next((x for x in mapping if x['source_label']==st['message']),None);ref=kb.link(dp,root/'domains/securities/reference/messages'/bind['message_id']/'index.md',bind['message_id']) if bind else 'Source explicitly identifies proprietary message; no ISO definition assigned';rows.append([str(i),roles[st['sender']][2],roles[st['receiver']][2],st['message'],ref])
 body+=kb.table(['Source order','Sender','Receiver','Source message label','Exact supplied definition'],rows)+'\n## Conditions, alternatives and notes\n\n'
 narrative='\n\n'.join('**'+p['paragraph_id']+'** '+p['text'] for p in rec['paragraphs'] if start<int(p['paragraph_id'][1:])<para and p['text']);body+=narrative+'\n\n'
 if note=='alternative-actors':body+='The source note gives an analogous Underwriter/Issuer Agent pair. Both are linked as narrative participants in the flow; they are not merged with the main ExecutingBroker/InstitutionalInvestor pair.\n\n'
 if note in ['alternative-cancellations','securities-financing-cancel']:body+='The artwork displays cancellations from both counterparties in order; the narrative describes possible alternative initiators or a new confirmation. The reconstruction preserves the depicted arrows without making both cancellations mandatory.\n\n'
 if n in [15,16,17]:body+='The source artwork labels the fourth actor CashCorrespondent, while its narrative uses Cash Settlement Agent. Both contextual labels remain recorded; the rejection-by-Transfer-Agent figure retains the otherwise inactive cash-correspondent lifeline.\n\n'
 if note=='proprietary-report':body+='The DeliveryAmountReport note explicitly classifies that exchange as proprietary. It is retained separately from SecuritiesEndOfProcessReport and is not assigned an invented ISO message identifier.\n\n'
 if note=='pre-advice':body+='The Pre advice note is attached to CMU-to-Trustee SecuritiesTradeConfirmation. P284 states that unmatched investment-manager data must still be matched with broker data later; the pre-advice does not waive that requirement.\n\n'
 if note=='source-conflict':body+='**Source contradiction (issue-000031):** the last narrative sentence says the CMU forwards a cancellation received from the investment manager. Earlier narrative and the figure show broker initiation followed by forwarding to the investment manager. Both claims remain visible; the reconstruction follows the source artwork, without silently correcting the narrative.\n\n'
 body+=kb.link(dp,flow,'Reusable flow')+'; '+kb.link(dp,actflow,'Related activity process')+'.\n\n## Review evidence\n\nFull-size source image inspected. Parsing/rendering and rendered-output comparison pending.\n';put(dp,kb.front(m)+body);put(dp.with_suffix('.mmd'),code)
 fm.update(document_kind='business-flow',manual_curated=True,participants=sorted(set(fm.get('participants',[])+pids+extra)),message_ids=m['message_ids'],message_families=sorted(set(x.rsplit('.',2)[0] for x in m['message_ids'])),message_mapping_evidence=mapping)
 if issues:fm['issue_ids']=sorted(set(fm.get('issue_ids',[])+issues));fm['limitations']=list(dict.fromkeys(fm.get('limitations',[])+limits[-1:]))
 fb=fb.replace('Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.','This source-defined scenario begins with the first confirmation exchange below. Its purpose, conditional agreement/rejection, cancellation alternatives and outcomes are specified by the source narrative. No additional formal preconditions or postconditions are invented. '+kb.link(flow,actflow,'Related activity process')+' provides the broader activity context.')
 fb=fb.replace('Mermaid reconstruction and visual review are pending.','The reconstructed sequence and actual review evidence are linked below.')
 fb+='\n## Curated source sequence\n\n'+kb.link(flow,dp,'Dedicated source reconstruction')+'. The source order is preserved below; typical-sequence arrows do not override narrative conditions or alternatives.\n\n'+kb.table(['Step','Message','Initiating sender','Receiving participant'],[[str(i+1),st['message'],kb.link(flow,root/'shared/reference/participants'/(prefix+roles[st['sender']][3]+'.md'),roles[st['sender']][2]),kb.link(flow,root/'shared/reference/participants'/(prefix+roles[st['receiver']][3]+'.md'),roles[st['receiver']][2])] for i,st in enumerate(steps)])+'\n'
 for pid in extra:fb+='\nAdditional source context: '+kb.link(flow,root/'shared/reference/participants'/(pid+'.md'),pid.removeprefix(prefix).replace('-',' '))+'. This is a narrative/alternative role, not an additional arrow inferred in the main sequence.\n'
 if issues:fb+='\nSource contradiction issue-000031: the final narrative sentence attributes a received cancellation to the investment manager, whereas the preceding narrative and source figure show broker initiation. The diagram preserves artwork direction; the original contradictory sentence remains above.\n'
 put(flow,kb.front(fm)+fb)
 for pid in pids+extra:
  pp=root/'shared/reference/participants'/(pid+'.md');pm,pb=kb.metadata(pp);pm['manual_curated']=True;pm['flows']=sorted(set(pm.get('flows',[])+[fm['flow_id']]));participating=[st for st in steps if prefix+roles[st['sender']][3]==pid or prefix+roles[st['receiver']][3]==pid];rolemsg=[x['message_id'] for x in mapping if any(st['message']==x['source_label'] for st in participating)];pm['message_ids']=sorted(set(pm.get('message_ids',[])+rolemsg));pb+='\nPost-trade matching scenario: '+kb.link(pp,flow,title)+'; '+kb.link(pp,dp,'source sequence')+'. '+('The source diagram shows this participant as sender/receiver in the ordered exchange.' if participating else 'The source identifies this participant as an inactive lifeline or narrative alternative in this scenario.')+'\n';put(pp,kb.front(pm)+pb)
 report.append({'diagram':dp.relative_to(root).as_posix(),'source_figure':fid,'source_image':n,'flow':flow.relative_to(root).as_posix(),'messages':len(steps),'actors':list(actors),'steps':steps,'note':note,'issue_ids':issues})
kb.dump(root/'work/documents/src-000180/sequence-curation.json',report)
print('Authored20PostTrade sequences; participant references and conditions preserved.')
