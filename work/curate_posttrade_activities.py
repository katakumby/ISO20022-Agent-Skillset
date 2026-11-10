from pathlib import Path
import json
exec(Path('work/curate_posttrade_processes.py').read_text(encoding='utf-8-sig').split("add('fig-0001'")[0])
class G:
 def __init__(self,lanes):self.lanes=lanes;self.nodes={k:[] for k in lanes};self.edges=[];self.blue=[]
 def n(self,l,k,text='',shape='box'):
  sym={'box':('["','"]'),'decision':('{"','"}'),'circle':('(("','"))'),'match':('(["','"])'),'cue':('["','"]')}[shape];self.nodes[l].append(k+sym[0]+(text or ' ')+sym[1]);return k
 def e(self,a,b,label='',blue=False):
  x=a+(' -.-> ' if blue else ' --> ')+(('|"'+label+'"| ') if label else '')+b;self.edges.append(x)
  if blue:self.blue.append(len(self.edges)-1)
 def end(self,l,start=None,label='To settlement<br/>process'):
  self.n(l,l+'EndCircle',shape='circle');self.n(l,l+'EndChoice',shape='decision');self.n(l,l+'End',label,shape='circle')
  if start:self.e(start,l+'EndCircle',blue=True)
  self.e(l+'EndCircle',l+'EndChoice',blue=True);self.e(l+'EndChoice',l+'End',blue=True)
 def code(self):
  t='flowchart TB\n subgraph Prior["Earlier lifecycle bands (gray in source)"]\n EP["Execution process"]\n AP["Allocation/Confirmation/Affirmation process"]\n end\n subgraph Trade["Trade Matching Process"]\n'
  for k,title in self.lanes.items():
   t+=' subgraph '+k+'Lane["'+title+'"]\n direction TB\n'+'\n'.join(' '+n for n in self.nodes[k])+'\n end\n'
  t+='\n'.join(' '+x for x in self.edges)+'\n end\n style Prior fill:#ddd,stroke:#ddd\n style CLane fill:#b5b5b5,stroke:#777\n linkStyle default stroke:#777\n'
  if self.blue:t+=' linkStyle '+','.join(map(str,self.blue))+' stroke:#3268d8\n'
  return t
 def entry(self,l,target):self.n(l,l+'In','Incoming continuation<br/>(unlabelled source line)','cue');self.e(l+'In',target,blue=True)
 def cancel(self,l):self.n(l,l+'Cancel','Cancel Confirmation')
 def rework(self,l,choice,targets):
  self.n(l,choice,shape='decision')
  for x in targets:self.e(choice,x,blue=True)

def affirmation(g,recipient='T',broker='B',tag=''):
 d=tag+'Assess';dis=tag+'Dis';aff=tag+'Aff';cd=tag+'CDis';ca=tag+'CAff';bd=tag+'BRework';g.n(recipient,d,shape='decision');g.n(recipient,dis,'Send Disaffirmation');g.n(recipient,aff,'Send Affirmation');g.n('C',cd,'Send Disaffirmation<br/>Status message');g.n('C',ca,'Send Affirmation<br/>Status message');g.rework(broker,bd,[broker+'Send',broker+'Cancel']);g.e(d,dis,'N.G.',True);g.e(d,aff,'O.K.',True);g.e(dis,cd,'Disaffirmation message');g.e(cd,bd,'Disaffirmation Status message');g.e(aff,ca,'Affirmation message');g.end(broker);g.e(ca,broker+'EndCircle','Affirmation Status message');g.end('C',ca);g.end(recipient,aff);return d

def local(kind):
 through=kind=='through';own=kind=='own';lanes={'B':'Broker' if through else 'Broker / Underwriter','C':'Central Matching Utility'}
 if through:lanes['I']='IM'
 lanes['T']='Trustee' if through else 'Institutional Investor / Issuer Agent';g=G(lanes)
 for l in ['B']+(['I'] if through else []):g.n(l,l+'Send','Send Confirmation');g.entry(l,l+'Send');g.cancel(l)
 g.n('C','CFB','Send Confirmation<br/>(Broker)');g.e('BSend','CFB');d=affirmation(g)
 g.e('CFB',d)
 if through:g.n('C','CFI','Send Confirmation<br/>(IM)');g.e('ISend','CFI');g.e('CFI',d)
 else:g.entry('T',d)
 g.n('C','CancelEndpoint',shape='circle');g.e('BCancel','CancelEndpoint')
 if through:g.e('ICancel','CancelEndpoint')
 g.n('C','CStatus','Send Cancellation<br/>Status Advice');g.n('B','BCancelReceipt',shape='circle');g.e('CStatus','BCancelReceipt');g.n('I' if through else 'T','OtherCancelReceipt',shape='circle');g.e('CStatus','OtherCancelReceipt')
 if through:
  g.rework('B','BCancelChoice',['BSend','BCancel']);g.rework('I','ICancelChoice',['ISend','ICancel'])
 return g

g=local('through');add('fig-0007','Through-type local matching activity',g.code(),'Broker and IM submit separate confirmations; CMU forwards each to Trustee. Trustee evaluates the details and follows N.G. to disaffirmation or O.K. to affirmation. CMU sends the corresponding status to Broker; disaffirmation loops to a new confirmation or cancellation, while affirmation continues toward settlement in the Broker, CMU and Trustee lanes. Cancellation inputs terminate at an unlabelled source endpoint within CMU; the separate cancellation-status action points to Broker and IM receipts. Two unconnected cancellation-choice diamonds remain as drawn. P147 says affirmation binds the trade details. T9 allows cancellation with a new confirmation, or cancellation of the trade without a new confirmation.',['broker','investment-manager','central-matching-utility-cmu','central-matching-utility-jasdec','trustee','trust-bank'],146,9,'The activity artwork says Trustee while T9 says Trust Bank. Both scoped records are linked; this local correspondence does not establish general institutional equivalence. Unlabelled endpoint symbols preserve source geometry without inventing a receiving activity.')
g=local('own');add('fig-0008','Own-account local matching activity',g.code(),'Broker / Underwriter sends its confirmation through CMU to Institutional Investor / Issuer Agent. The recipient compares details: N.G. leads to disaffirmation and a status returning to the sender; O.K. leads to affirmation, status and settlement continuations. Cancellation enters the CMU lane at an unlabelled endpoint; a separate cancellation-status action points to sender and recipient receipts. P154 binds the trade on affirmation. T10 preserves cancellation/new-confirmation alternatives and disaffirmation conditions.',['broker','underwriter','central-matching-utility-cmu','central-matching-utility-jasdec','institutional-investor','issuer-agent'],153,10,'Slash-separated actor labels describe source alternatives, not a merger of institutions or role definitions.')
# Duplex: first acceptance gates forwarding to cash settlement agent, then second acceptance.
g=G({'B':'Underwriter','C':'Central Matching Utility','A':'Transfer Agent','T':'Cash Settlement Agent'});g.n('B','BSend','Send Confirmation');g.entry('B','BSend');g.cancel('B');g.n('C','CF1','Send Confirmation<br/>(Underwriter)');g.e('BSend','CF1');g.n('A','ADec',shape='decision');g.e('CF1','ADec');g.n('A','ADis','Send Disaffirmation');g.n('A','AAff','Send Affirmation');g.e('ADec','ADis','N.G.',True);g.e('ADec','AAff','O.K.',True);g.n('C','CD1','Send Disaffirmation<br/>Status message');g.e('ADis','CD1','Disaffirmation message');g.rework('B','BD1',['BSend','BCancel']);g.e('CD1','BD1','Disaffirmation Status message');g.n('C','CF2','Send Confirmation<br/>(Underwriter)');g.e('AAff','CF2','Affirmation message');d=affirmation(g,tag='Second');g.e('CF2',d);g.n('C','CancelEndpoint',shape='circle');g.e('BCancel','CancelEndpoint');g.n('C','CStatus','Send Cancellation<br/>Status Advice');g.n('B','BReceipt',shape='circle');g.n('A','AReceipt',shape='circle');g.e('CStatus','BReceipt');g.e('CStatus','AReceipt');add('fig-0009','Duplex local matching activity',g.code(),'Underwriter confirmation first goes through CMU to Transfer Agent. N.G. returns a disaffirmation status and rework/cancellation path to Underwriter. O.K. sends affirmation to CMU, which forwards the same underwriter confirmation to Cash Settlement Agent. Its N.G. and O.K. branches separately disaffirm or affirm. CMU sends the final status to Underwriter; accepted trade continues to settlement. The cancellation-status action has source arrows to Underwriter and Transfer Agent receipts; no additional cash-agent cancellation arrow is inserted in this activity diagram. P160 and T11 supply the corresponding responsibilities and conditions.',['underwriter','central-matching-utility-cmu','central-matching-utility-jasdec','transfer-agent','cash-settlement-agent'],159,11,'The sequence figures use CashCorrespondent for a related fourth actor. The source labels remain distinct; the linked sequence preserves its own cancellation arrows.')
# Central matching common graph; matching-status decisions and cancellation receipts remain separate.
def central(distribute=False,bilateral=False):
 lanes={'B':'Broker','C':'Central Matching Utility','I':'Broker' if bilateral else 'IM'}
 if not bilateral:lanes['T']='Trustee'
 g=G(lanes)
 for l in ['B','I']:g.n(l,l+'Send','Send Confirmation');g.cancel(l);g.n(l,l+'CancelReceipt',shape='circle');g.n(l,l+'MatchChoice',shape='decision');g.e(l+'MatchChoice',l+'Send','N (Unmatched)',True);g.e(l+'MatchChoice',l+'Cancel','N (Unmatched)',True)
 g.n('C','Match','Matching Process','match');g.entry('B','BSend')
 if distribute:
  g.n('C','CFDist','Send Confirmation<br/>(IM)');g.e('BSend','CFDist');g.n('I','ICompare',shape='decision');g.e('CFDist','ICompare');g.entry('I','ICompare');g.e('ICompare','ISend','O.K.',True)
 else:g.e('BSend','Match');g.entry('I','ISend')
 g.e('ISend','Match')
 for l in ['B','I']:g.e(l+'Cancel','Match');g.e('Match',l+'CancelReceipt','Cancellation Status message(s)');g.e('Match',l+'MatchChoice','Matching Status message(s)')
 if bilateral:
  for l in ['B','C','I']:g.end(l);g.e('Match' if l=='C' else l+'MatchChoice',l+'EndCircle','Y (Matched)',True)
 else:
  g.n('C','CFI','Send Confirmation<br/>(IM)');g.n('C','CFB','Send Confirmation<br/>(Broker)');g.e('Match','CFI','Y (Matched)',True);g.e('Match','CFB','Y (Matched)',True);d=affirmation(g);g.e('CFI',d);g.e('CFB',d)
 return g
for fid,dist,title,p,t in [('fig-0011',False,'Tripartite central matching without distribution',173,13),('fig-0012',True,'Tripartite central matching with distribution',180,14)]:
 g=central(dist);add(fid,title,g.code(),('With distribution, Broker confirmation is first forwarded by CMU to IM; the initial IM O.K. comparison leads to its own confirmation. The top CMU forwarding box is labelled Send Confirmation (IM) in the source, although P181 describes forwarding Broker data; that exact box label is retained. ' if dist else 'Without distribution, Broker and IM independently send confirmations to the matching process. ')+ 'The CMU matching process returns cancellation status to receipt circles and matching status to each party decision. N (Unmatched) returns toward a new confirmation or cancellation; Y (Matched) forwards both confirmations to Trustee. Trustee N.G. disaffirms and prompts Broker rework; O.K. affirms, produces status and permits settlement continuations. P174/P181 and T13/T14 preserve the timing, agreement and cancellation alternatives.',['broker','investment-manager','central-matching-utility-cmu','central-matching-utility-jasdec','trustee','trust-bank'],p,t,'The source matching process is a narrow orange ellipse; native Mermaid uses a labelled rounded node while preserving all associated arrows. Color and exact shape remain in the original. Cancellation receipt markers do not imply a settlement reversal.')
g=central(bilateral=True);add('fig-0013','Bilateral central matching activity',g.code(),'The source activity labels both outer lanes Broker. Each submits a confirmation or cancellation to CMU. Cancellation status goes to the corresponding receipt marker; matching status goes to a local choice. N (Unmatched) loops to a new confirmation or cancellation; Y (Matched) continues toward settlement in both broker lanes and the CMU lane. P186 identifies the second narrative actor as Prime Broker. The reconstruction preserves the two identical artwork lane labels while linking the narrative-specific role separately.',['broker','prime-broker','central-matching-utility-cmu','central-matching-utility-jasdec'],185,15,'Both Broker lane instances remain distinct; the canonical business role may appear in more than one instance. The source does not specify an institution name.')
# Listed derivatives: retain end-of-day reporting separately from proprietary delivery report.
g=G({'B':'Broker','C':'Central Matching Utility','I':'IM','T':'Trustee'})
for l in ['B','I']:g.n(l,l+'Send','Send Confirmation');g.entry(l,l+'Send');g.n('C','CConf'+l,'Send Confirmation<br/>('+('Broker' if l=='B' else 'IM')+')');g.e(l+'Send','CConf'+l)
g.n('T','TConf',shape='decision');g.e('CConfB','TConf');g.e('CConfI','TConf');g.n('B','BDelivery','Send Delivery<br/>Amount Report');g.n('C','CDelivery','Send Delivery<br/>Amount Report');g.n('T','TDelivery',shape='decision');g.e('BDelivery','CDelivery');g.e('CDelivery','TDelivery')
for l in ['B','I']:g.n(l,l+'EOD','Send “End Of Day”<br/>Report of Confirmation');g.n('C','CEOD'+l,'Send “End Of Day”<br/>Report of Confirmation<br/>('+('Broker' if l=='B' else 'IM')+')');g.e(l+'EOD','CEOD'+l)
g.n('T','TEOD',shape='circle');g.e('CEODB','TEOD');g.e('CEODI','TEOD');g.n('B','BEODDelivery','Send “End Of Day”<br/>Report of Delivery<br/>Amount Report');g.n('C','CEODDelivery','Send “End Of Day”<br/>Report of Delivery<br/>Amount Report');g.n('T','TDelReceipt',shape='circle');g.e('BEODDelivery','CEODDelivery');g.e('CEODDelivery','TDelReceipt');g.end('B','BEOD');g.e('BEODDelivery','BEndCircle',blue=True);g.n('C','CEnd',shape='circle');g.e('CEODDelivery','CEnd',blue=True);g.n('T','TSetDecision',shape='decision');g.n('T','TSet','To settlement<br/>process','circle');g.e('TDelReceipt','TSetDecision',blue=True);g.e('TSetDecision','TSet',blue=True);g.n('T','TNAVDecision',shape='decision');g.n('T','TNAV','To NAV calculation<br/>process','circle');g.e('TEOD','TNAVDecision',blue=True);g.e('TNAVDecision','TNAV',blue=True)
code=g.code();code=code.replace(' end\n subgraph Trade',' end\n Context["Source blue rounded boundary: Matching process of Listed Derivatives (Through Type); contains confirmation and delivery-amount-report exchanges only"]\n subgraph Trade',1)
add('fig-0010','Listed-derivatives end-of-process reporting activity',code,'The source blue rounded area groups the initial through-type confirmation exchanges and delivery amount reporting. Broker and IM confirmations are forwarded separately to Trustee. Broker Delivery Amount Report is forwarded to Trustee as a separate exchange. After the respective daily confirmations, Broker and IM send End Of Day Report of Confirmation; CMU forwards both into one Trustee receipt marker leading to NAV calculation. Broker End Of Day Report of Delivery Amount Report is forwarded into a separate Trustee receipt leading to settlement. Broker settlement continuation receives dashed lines from both of its report actions. CMU has its own unlabelled end marker after delivery-report forwarding. P166 and T12 preserve timing and responsibilities.',['broker','investment-manager','central-matching-utility-cmu','central-matching-utility-jasdec','trustee','trust-bank'],165,12,'The original blue grouping and darker delivery row span several participant lanes. Mermaid describes this complete boundary in an explicit labelled note rather than duplicating the same node inside overlapping subgraphs. Source grouping, not additional process ordering, is intended. DeliveryAmountReport is explicitly proprietary in sequence figure21/P229; it is not merged with ISO SecuritiesEndOfProcessReport.')
old=json.loads((root/'work/documents/src-000180/process-curation.json').read_text(encoding='utf-8'));kb.dump(root/'work/documents/src-000180/process-curation.json',old+out);print('Seven activity reconstructions authored')
