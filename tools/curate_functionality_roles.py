"""Curate complete Functionality role labels from supplied evidence; parser fragments stay unassigned."""
from pathlib import Path
import json,sys,re,hashlib,collections
sys.path.insert(0,str(Path(__file__).resolve().parent));import kb,extract_workbooks
root=Path(__file__).resolve().parents[1];extract_workbooks.DATE='2026-11-09';srcs={x['source_id']:x for x in kb.sources(root)}
units=collections.defaultdict(list)
for p in (root/'work/message-roles').glob('*.json'):
 r=json.loads(p.read_text('utf-8'))
 for pub in r.get('publications',[]):
  for i,u in enumerate(pub['narrative']+pub.get('unclassified_narrative',[]),1):
   v=dict(u,message_id=r['message_id'],heading=pub['heading']);v.setdefault('evidence_id',pub['source_id']+'-'+r['message_id']+'-p'+str(u['file_pages'][0])+'-c'+str(i).zfill(3));units[pub['source_id']].append(v)
def put(p,t):extract_workbooks.write(root,p,t,'job-000001')
def matches(sid,labels):
 if sid=='src-000197' and labels==['client']:return [u for u in units[sid]if u['message_id']=='sese.040.001.06' and re.search(r'\bclient\b',u['quote'],re.I)]
 if sid=='src-000321' and labels in [['entity'],['authority']]:return [u for u in units[sid] if u['message_id']=='auth.044.001.03' and ('an '+labels[0]) in u['quote']]
 return [u for u in units[sid]if any(re.search(r'(?<!\w)'+re.escape(label)+r'(?!\w)',u['quote'],re.I)for label in labels)]
changes=[]
def alias(pid,sid,labels,basis):
 p=root/'shared/reference/participants'/f'{pid}.md';m,b=kb.metadata(p);evidence=matches(sid,labels);assert evidence,(pid,sid,labels)
 m.setdefault('source_locations',[]);m['source_labels']=sorted(set(m.get('source_labels',[])+labels));m['source_ids']=sorted(set(m['source_ids']+[sid]));m['message_ids']=sorted(set(m.get('message_ids',[])+[e['message_id']for e in evidence]));m['message_families']=sorted(set('.'.join(x.split('.')[:2])for x in m['message_ids']))
 for e in evidence:
  loc=dict(source_id=sid,heading=e['heading'],file_pages=e['file_pages'],evidence_id=e['evidence_id'])
  if loc not in m['source_locations']:m['source_locations'].append(loc)
 marker='FUNCTIONALITY-ALIASES-'+sid;b=re.sub(r'\n<!-- '+marker+r' -->.*?<!-- /'+marker+r' -->\n?','\n',b,flags=re.S)
 b+='\n<!-- '+marker+' -->\n## Additional literal publication labels\n\n'+basis+'\n\n'+kb.table(['Source label','Source context'],[[label,'; '.join(e['evidence_id']for e in evidence if re.search(r'(?<!\w)'+re.escape(label)+r'(?!\w)',e['quote'],re.I))]for label in labels])+'\n'+''.join('> '+e['quote']+'\n\n'+sid+', file pages'+', '.join(map(str,e['file_pages']))+'; '+e['heading']+'.\n\n'for e in evidence)+'<!-- /'+marker+' -->\n';put(p,kb.front(m)+b);changes.append(dict(kind='source-supported-label',participant_id=m.get('participant_id',pid),source_id=sid,labels=labels,evidence_ids=[e['evidence_id']for e in evidence]))
def new(sid,slug,labels,definition):
 pid='participant-functionality-'+sid+'-'+slug;p=root/'shared/reference/participants'/f'{pid}.md';evidence=matches(sid,labels);assert evidence,(sid,labels)
 source=srcs[sid];ids=sorted(set(e['message_id']for e in evidence));m=dict(template=False,document_kind='participant',review_status='needs-review',manual_curated=True,domain='shared',domains=[source['domain']],participant_id=pid,title=labels[0]+' — '+source['set_title']+' Functionality',source_ids=[sid],source_editions=[source['source_edition']],source_labels=labels,aliases=[],role_type='functional participant explicitly named in message Functionality',message_sets=[source['set_slug']],message_ids=ids,message_families=sorted(set('.'.join(x.split('.')[:2])for x in ids)),source_locations=[dict(source_id=sid,heading=e['heading'],file_pages=e['file_pages'],evidence_id=e['evidence_id'])for e in evidence],identifier_schemes=[],limitations=['Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.','A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.','Mention in an example, routing clause or alternative is not automatically an independent sender or receiver.'])
 body='# '+m['title']+'\n\n'+kb.source_link(root,p,source)+'\n\n## Definition and business context\n\n'+definition+'\n\nThis record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.\n\n## Responsibilities, actions and relationships\n\nThe complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.\n\n'+''.join('### '+e['evidence_id']+'\n\n'+sid+', file page'+(',s 'if len(e['file_pages'])>1 else' ')+', '.join(map(str,e['file_pages']))+'; '+e['heading']+'.\n\n> '+e['quote']+'\n\n'for e in evidence)+'## Applicable exact messages\n\n'+kb.table(['Exact definition','Role evidence'],[[mid,kb.link(p,root/next(x['path']for x in json.loads((root/'catalog/messages.json').read_text('utf-8'))['messages']if x['message_id']==mid),'Canonical message')]for mid in []]) # navigation follows actual source role artifacts below
 for mid in ids:
  candidates=list((root/'shared/reference/messages'/mid).glob('roles.md'))+list((root/'domains').glob('*/reference/messages/'+mid+'/roles.md'))
  if candidates:body+='- '+kb.link(p,candidates[0],mid)+'\n'
 body=body.replace('| Exact definition | Role evidence |\n| --- | --- |\n','')
 body+='\n## Identity and unresolved scope\n\nSource labels: '+', '.join(labels)+'. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.\n';put(p,kb.front(m)+body);changes.append(dict(kind='scoped-narrative-participant',participant_id=pid,source_id=sid,labels=labels,evidence_ids=[e['evidence_id']for e in evidence],path=p.relative_to(root).as_posix()))
# Full labels supported by explicitly defined roles and quoted publication context.
alias('participant-src-000320-nca','src-000321',['national competent authority','national competent authorities','all national competent authorities'],'T11 row3 of source320 explicitly expands NCA as National Competent Authority. Source321 uses the full singular/plural labels; the quantifier all remains a qualifier in the quoted distribution scope.')
alias('participant-narrative-src-000344-member','src-000344',['member of the system'],'The longer phrase is the exact source noun phrase behind this existing scoped Member record. The reverse-direction wording remains in the quote.')
alias('participant-narrative-src-000015-member','src-000015',['member of the system'],'The exact source noun phrase names the existing narrative Member; this does not equate it with the separately defined standing-order System Member role.')
alias('participant-src-000095-professional-investor','src-000096',['professional investors'],'Plural spelling of the same source-defined business-role label in report-recipient examples.')
alias('participant-src-000095-regulator','src-000096',['regulators'],'Plural spelling of the same source-defined business-role label in report-recipient examples.')
alias('participant-src-000095-requesting-party','src-000096',['report users'],'Plural spelling of Report User; the source quote retains the reporting context and does not assert that every report is solicited.')
alias('participant-src-000365-executing-servicing-party','src-000366',['executing/ servicing party'],'The source uses a spacing variant of Executing/Servicing Party in AccountLinkMaintenanceRequest.')
alias('participant-src-000368-national-central-bank-ncb','src-000369',['national central bank'],'The unabbreviated name is explicitly the same business-role label as National Central Bank (NCB); source context remains PartyQuery/PartyReport.')
alias('settlement-reconciliation-account-servicer','src-000197',['another account servicer'],'Another identifies the counterparty in the same source-defined account-servicer role; sender and receiver may have the same function while remaining distinct parties.')
# Additional participants named in Functionality, absent from the reusable formal role definitions.
specs=[
('src-000344','central-system',['Central System'],'Recipient of the ResendRequest sent by a system member or its authorised parties. The T2S platform is an example of this role in the quoted source, not a universal alias.'),
('src-000344','party-authorised-by-system-member',['any parties authorised by them'],'Alternative sender authorised by the system member in the ResendRequest scope sentence; the authorising relationship is explicit in that sentence.'),
('src-000321','trading-venue',['trading venue','trading venues'],'Reporting-side participant explicitly named for financial-instrument reference, transparency, activity, cancellation and related reporting. Its institutional type is not equated with one of the separate source business roles.'),
('src-000321','entity',['entity'],'Entity named as a user of FinancialInstrumentReportingEquityTradingActivityResult to provide computed equity trading-activity results; its institution type remains unspecified.'),
('src-000321','authority',['authority'],'Authority named as a user of FinancialInstrumentReportingEquityTradingActivityResult to provide computed equity trading-activity results; no automatic equivalence with a particular competent or supervisory authority is inferred.'),
('src-000005','party-authorised-by-account-owner',['party authorised by the account owner'],'Alternative recipient authorised by the account owner for account reports, statements or debit/credit notifications. It is distinct from the account owner and from the account servicer.'),
('src-000005','account-servicing-institution',['account servicing institutions'],'Recipient institution for AccountReportingRequest, selected from the account owner’s servicing institutions. The quoted direct or forwarding-agent route remains explicit.'),
('src-000369','payment-bank',['payment bank'],'Institutional-role example explicitly allowed to query and receive party reference data in PartyQuery and PartyReport.'),
('src-000369','trading-party',['trading party'],'Participant explicitly allowed to query and receive party reference data in PartyQuery and PartyReport.'),
('src-000197','csd',['CSD'],'Central-securities-depository label appearing in this exact settlement Functionality context; no automatic equivalence with every CSD/ICSD source-role record is asserted.'),
('src-000197','securities-financing-account-servicer',['securities financing transaction account servicer'],'Account-servicer function specifically scoped by the source to securities-financing transactions. The named responsibilities and relationships remain those of the quoted message clauses.'),

('src-000096','report-recipient',['report recipient'],'Recipient-side reporting role in the quoted investment-funds messages, including source-defined institutional examples. It does not establish a requirement to have requested the report.'),
]
specs.extend([
('src-000197','global-custodian-customer',['global custodian customer','customer'],'Global custodian on whose behalf the sub-custodian agent acts or manages securities-financing transactions, as explicitly stated in the account-owner/servicer relationship examples. It is a relationship-specific customer, not every portfolio-transfer or split-settlement client.'),
('src-000197','message-copy-third-party',['third party'],'Third party receiving an informational copy or re-sent copy of the current message, using BAH facilities where stated. This copying role does not establish settlement-instruction or transaction-audit-trail responsibilities.'),
('src-000197','allegement-client',['client'],'Client to whom an allegement may have been passed in the SecuritiesSettlementTransactionAllegementReport source clause. No equivalence with the portfolio-transfer or split-settlement client is inferred.')])
for args in specs:new(*args)
# Generic Sender/Receiver/agent labels still convey real contextual participation; preserve their narrow evidence without institutional inference.
issues=json.loads((root/'work/message-roles/review-items.json').read_text('utf-8'))['items'];generic=collections.defaultdict(set)
for x in issues:
 if x['kind']!='unresolved-participant-label':continue
 label=x['detail'].split(' is retained in source scope;')[0]
 if label.lower()in ['sender','receiver','recipient','agent','agents','receiving party']:generic[x['source_id']].add(label)
for sid,labels in generic.items():
 for group in [sorted([x for x in labels if x.lower()in ['agent','agents']]),sorted([x for x in labels if x.lower()=='sender']),sorted([x for x in labels if x.lower()in ['receiver','recipient','receiving party']])]:
  if not group:continue
  slug='agent'if group[0].lower()in ['agent','agents']else'sender'if group[0].lower()=='sender'else'recipient'
  new(sid,slug,group,'Generic '+slug+' function explicitly named in this publication’s quoted message Functionality. Its precise capacity and counterparties are retained per clause rather than being inferred from the generic label.')
kb.dump(root/'tracking/reviews/participant-functionality-labels.json',{'date':'2026-11-09','changes':changes,'method':'Exact source Functionality quotes, paired formal definitions where stated, and source-scoped canonical records. No parser modification or index refresh performed.'})
print(json.dumps({'changed_records':len(changes),'new_records':sum(x['kind']=='scoped-narrative-participant'for x in changes),'source_supported_alias_records':sum(x['kind']=='source-supported-label'for x in changes)}))
