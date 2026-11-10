"""Source 196 figure 1: scoped illustrative institutions and communication graph."""
import re
import kb

SCOPE_ROLES={
 'scope-customer':('Customer','The Customer in the settlement communication-scope illustration sends receipt/delivery instructions to the Custodian and receives status/processing advice, settlement confirmation, centrally generated transaction advice and allegement.','Customer'),
 'scope-custodian':('Custodian','The Custodian in this illustration receives the Customer’s receipt/delivery instruction and sends a receipt/delivery instruction to the Sub-Custodian. Status, confirmation, generated transaction advice and allegement point back through the illustrated chain.','Custodian'),
 'scope-sub-custodian':('Sub-Custodian — Account Owner 3','The illustration explicitly labels this Sub-Custodian as Account Owner 3 in its relationship with the CSD’s Account Servicer 3. It sends receipt/delivery instructions and transaction-processing commands to the CSD and receives the depicted advice/confirmation/allegement categories.','Sub-Custodian Account Owner 3'),
 'scope-broker':('Broker','The Broker in this illustration sends a receipt/delivery instruction to its local agent and receives the depicted status/processing advice, settlement confirmation, generated transaction advice and allegement.','Broker'),
 'scope-brokers-local-agent':("Broker’s Local Agent — Account Owner 2","The illustration explicitly labels the Broker’s Local Agent as Account Owner 2 in its relationship with the CSD’s Account Servicer 2. It receives the broker’s instruction, instructs the CSD and receives the illustrated advice/confirmation/allegement categories.","Broker's Local Agent Account Owner 2"),
}

code='''flowchart LR
  Customer["Customer"]
  Custodian["Custodian"]
  Sub["Sub-Custodian<br/>Account Owner 3"]
  Broker["Broker"]
  Agent["Broker's Local Agent<br/>Account Owner 2"]
  CSD["Central Securities Depository<br/>Account Servicer 3 / Account Servicer 2"]
'''
for a,b in [('Customer','Custodian'),('Custodian','Sub'),('Broker','Agent'),('Sub','CSD'),('Agent','CSD')]:
 code+='  '+a+' -->|Receipt or Delivery instruction| '+b+'\n'
 if b=='CSD':code+='  '+a+' -->|Transaction Processing Command| '+b+'\n'
 for label in ['Settlement Status and Processing Advice','Settlement Confirmation','Centrally Generated Transaction Advice','Allegement']:
  code+='  '+b+' -->|'+label+'| '+a+'\n'
code+='  Sub -.-|Account Owner 3 / Account Servicer 3| CSD\n  Agent -.-|Account Owner 2 / Account Servicer 2| CSD\n'

SCOPE={1:dict(title='Settlement communication scope and account relationships',kind='flowchart',flow_slugs=['instruction-confirmation','transaction-generation','allegement'],roles=list(SCOPE_ROLES)+['account-owner','account-servicer','csd-icsd'],table=None,code=code,notes=[
'This is a communication-scope illustration, not a temporal sequence or a requirement to send every category. Generic message categories remain generic and are not assigned an exact message definition solely from this picture.',
'Customer, Custodian, Sub-Custodian, Broker, Broker’s Local Agent and Central Securities Depository are the source labels. The sub-custodian/local-agent appearances repeated in different parts of the original artwork are consolidated into one node per exact labeled participant here.',
'The original dotted account relationships explicitly pair Account Owner 3 with Account Servicer 3 and Account Owner 2 with Account Servicer 2. These are depicted relationships, not claims that an institution always holds that role. Institution pictograms are represented as labeled boxes; the original asset preserves their appearance.',
])}

def participants(root,source,diagram):
 base=root/source['set_path'];participants=root/'shared/reference/participants'
 for slug,(title,definition,label) in SCOPE_ROLES.items():
  page=participants/('settlement-reconciliation-'+slug+'.md')
  meta={'template':False,'document_kind':'participant','review_status':'needs-review','manual_curated':True,'participant_id':'participant-settlement-reconciliation-'+slug,'title':title,'domains':['securities'],'domain':'securities','message_sets':['settlement-and-reconciliation'],'source_ids':['src-000196'],'source_labels':[label],'aliases':[],'source_locations':[{'source_id':'src-000196','paragraph_id':'P145','figure_id':'fig-0001','heading_path':['Scope and Functionality','Scope'],'xml_path':'/w:document/w:body/w:p[145]'}],'role_kind':'illustrative institution/business participant; figure-scoped','message_ids':[],'flow_ids':['flow-settlement-reconciliation-'+x for x in SCOPE[1]['flow_slugs']],'limitations':['The supplied picture is the scope of this record. It gives no formal institution definition or identifier scheme.','No equivalence with another same-named participant in a different collection is asserted.'],'updated':'2026-11-09'}
  body=kb.front(meta)+'# '+title+'\n\n'+definition+'\n\n'+kb.source_link(root,page,source)+'; Scope, settlement communication illustration, P145 / fig-0001.\n\n'+kb.link(page,diagram,'Communication graph, unchanged source artwork and visual review')+'\n\n## Context and relationships\n\nThe source illustrates business participants using institutional pictograms. Its account-owner/account-servicer labels apply to the specific depicted relationship. They do not make an institutional category identical to a functional account role. No source-supported alias or identifier scheme is stated in this picture.\n\n## Related flows\n\n'+'\n'.join('- '+kb.link(page,base/'flows'/(f+'.md'),f.replace('-',' ')) for f in SCOPE[1]['flow_slugs'])+'\n'
  if slug in ('scope-sub-custodian','scope-brokers-local-agent'):body+='\n'+kb.link(page,participants/'settlement-reconciliation-account-owner.md','Functional account-owner role')+' · '+kb.link(page,participants/'settlement-reconciliation-account-servicer.md','Functional account-servicer role')+'\n'
  kb.put(page,body)
