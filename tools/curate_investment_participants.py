"""Curate the explicitly scoped participant roles in the Investment Funds Parties model."""
from pathlib import Path
import json,sys,re,collections
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'));import kb
from extract_workbooks import fm,write,relative,esc
SID='src-000097';JOB='job-000001';source=next(s for s in kb.sources(ROOT) if s['source_id']==SID);base=Path(source['set_path']);wb=base/'workbooks'/SID
w=json.loads((ROOT/'work/workbooks'/SID/'workbook.json').read_text('utf-8'));sh=next(s for s in w['sheets'] if s['name']=='FullBusinessModel');rows=collections.defaultdict(dict)
for c in sh['cells']:
 m=re.match('([A-Z]+)([0-9]+)',c['cell']);rows[int(m[2])][m[1]]=c['value']
names='Role AssetPartyRole GuaranteePartyRole IssuerRole GuarantorRole InvestmentFundPartyRole AccountPartyRole InvestmentAccountPartyRole FundOrderDesk Auditor FundManagerRole PlacementAgent Settlor FundAdministratorRole Grantor FundAccountantRole FundPromoter LegalGuardianRole TrusteeRole AdministratorRole Nominee'.split()
def slug(n):return re.sub(r'(?<!^)(?=[A-Z])','-',n).lower()
paths={n:Path('shared/reference/participants')/('investment-funds-model-'+slug(n)+'.md') for n in names}
def lk(p,t,label):return '['+label+']('+relative(ROOT/p,ROOT/t)+')'
def put(p,b):write(ROOT,ROOT/p,b,JOB)
def evidence(p,i):
 tp=next(t for t in sh['table_pages'] if t['row_start']<=i<=t['row_end']);return lk(p,Path(tp['path']),'FullBusinessModel!A'+str(i)+':F'+str(i))
figure=wb/'diagrams/fig-0006.md';records=[]
for name in names:
 rr=[(i,r) for i,r in rows.items() if r.get('A')==name];i,definition=next((i,r) for i,r in rr if not r.get('B'));attrs=[(j,r) for j,r in rr if r.get('B')];parent=definition.get('C');children=[n for n in names if any(r.get('A')==n and not r.get('B') and r.get('C')==name for r in rows.values())];p=paths[name];pid=p.stem;aliases=['fund promoter','fund sponsor'] if name=='FundManagerRole' else [];limitations=['This business-model role definition does not by itself establish an initiating, sending, receiving or executing role for any exact message or ordered flow.']
 if name=='Grantor':limitations.append('The supplied definition only identifies a grantor role in the hedge-funds industry; detailed actions are not defined here.')
 if name=='FundPromoter':limitations.append('The local definition is only “Fund Promoter”; the source establishes its FundManagerRole parent, but gives no additional local responsibilities.')
 meta=fm(domain='shared',document_kind='participant',review_status='needs-review',curated=True,participant_id=pid,title=name+' — Investment Funds business model',source_labels=[name],aliases=aliases,role_type='contextual business role',applicable_domains=['securities'],source_ids=[SID],source_editions=[source['source_edition']],source_locations=['FullBusinessModel!A'+str(min(j for j,r in rr))+':F'+str(max(j for j,r in rr)),'Parties; xl/drawings/drawing6.xml; anchor 1'],message_sets=['investment-funds'],message_ids=[],flows=[],limitations=limitations)
 b=meta+'# '+name+' — Investment Funds business model\n\n## Definition and applicable context\n\n'+definition['D']+'\n\nEvidence: '+evidence(p,i)+'. This record is scoped to the supplied Investment Funds Part 3 model and its Parties diagram. It describes a business role; the institution or person playing it may perform different functional roles in different relationships. The model does not equate a role with a permanent institutional identity.\n\n## Responsibilities and actions\n\n'+definition['D']+'\n\n'+evidence(p,i)+' supplies these duties and qualifications. Parent-role definitions and source-defined local attributes below provide additional context. No message direction is inferred from class inheritance or an association.\n\n## Relationships with other participants\n\n'
 if parent in paths:b+='Specializes '+lk(p,paths[parent],parent)+'; parent is explicitly recorded in column C of '+evidence(p,i)+'.\n\n'
 else:b+='The component declaration supplies no parent role.\n\n'
 if children:b+='Source-defined specializations: '+', '.join(lk(p,paths[n],n) for n in children)+'. These are inheritance relationships in the '+lk(p,figure,'reviewed Parties model')+', not aliases.\n\n'
 if name=='FundAccountantRole':b+='The definition explicitly permits subcontracting by the '+lk(p,paths['FundAdministratorRole'],'fund administrator')+'.\n\n'
 if name=='FundManagerRole':b+='The source definition uses “fund promoter” and “fund sponsor” as aliases. The same model also contains a distinct '+lk(p,paths['FundPromoter'],'FundPromoter subtype')+'; the subtype record is retained and is not collapsed merely because its label also appears as an alias.\n\n'
 if name in ['FundManagerRole','FundAccountantRole']:
  other=Path('shared/reference/participants')/('participant-src-000095-fund-manager.md' if name=='FundManagerRole' else 'participant-src-000095-fund-accountant.md')
  b+='The separately scoped '+lk(p,other,'Part 1 narrative business-role record')+' supplies process-specific participation and functional-role mappings. Its overlapping definition is a navigational connection; those process claims are not automatically transferred to this model definition.\n\n'
 b+='## Local attributes, relationships and identifier evidence\n\n'
 if attrs:
  b+='| Source attribute | Definition | Type or related component | Opposite role | Precise evidence |\n| --- | --- | --- | --- | --- |\n'
  for j,r in attrs:b+='| '+' | '.join([esc(r.get('B')),esc(r.get('D')),esc(r.get('E')),esc(r.get('F')),evidence(p,j)])+' |\n'
 else:b+='No local attribute row is supplied for this component; inherited context remains available through the parent-role links. This does not establish absence of identifiers in every business usage.\n'
 b+='\nNo external participant identifier scheme is specified by these local rows. References to an Account, InvestmentAccount or RolePlayer identify a related conceptual component; they are not themselves a supplied BIC, LEI or account-number scheme. Source code-type names such as PartyRoleCode or FATCAFormTypeCode remain separately defined types, not an invented identifier list.\n\n## Flows, messages and model evidence\n\nApplicable domain: Securities. Applicable message set: Investment Funds. '+lk(p,base/'flows/index.md','Process references')+' and '+lk(p,base/'participants.md','message-set participants')+' provide additional independently sourced context. No exact message or ordered flow is assigned solely from this conceptual view. The '+lk(p,figure,'Parties diagram')+' is a reusable role hierarchy, and the '+lk(p,wb/'diagrams/fig-0005.md','Account model')+' supplies related account context without changing this role’s scope.\n\n## Provenance, review and limitations\n\n'+kb.source_link(ROOT,ROOT/p,source)+'; '+evidence(p,i)+'. Source definitions and the complete role hierarchy were visually checked on 2026-11-09. Source diagram reconstructions parsed/rendered with Mermaid 12.3.0 and were visually compared. This record remains needs-review for process-specific actor/message applicability, which the model does not supply.\n\n'+''.join('- '+x+'\n' for x in limitations)
 put(p,b);records.append(dict(participant_id=pid,path=p.as_posix(),label=name,source_id=SID,row=i))
idx=wb/'participants.md';b=fm(domain='securities',document_kind='participant-index',review_status='needs-review',curated=True,source_ids=[SID],message_sets=['investment-funds'])+'# Investment Funds model participants\n\nThese 21 records preserve the contextual role definitions and inheritance in Parties and FullBusinessModel. They do not turn conceptual-model associations into message directions.\n\n| Source role | Canonical scoped participant | Declaration |\n| --- | --- | --- |\n'
for r in records:b+='| '+r['label']+' | '+lk(idx,Path(r['path']),r['participant_id'])+' | '+evidence(idx,r['row'])+' |\n'
put(idx,b)
p=base/'participants.md';b=(ROOT/p).read_text('utf-8');addition='\n## Business-model participant definitions\n\n'+lk(p,idx,'Investment Funds model participant index')+' provides 21 additional source-scoped business-role records from src-000097, including the complete Parties hierarchy. Model scope and Part 1 functional process mappings remain distinct.\n'
if '## Business-model participant definitions' not in b:put(p,b+addition)
p=figure;b=(ROOT/p).read_text('utf-8');addition='\n## Canonical participant records\n\n'+lk(p,idx,'All 21 scoped role records')+' provide definitions, responsibilities, parent/subtype relationships and precise workbook-row evidence.\n'
if '## Canonical participant records' not in b:put(p,b+addition)
put(Path('work/investment-workbook-models/participants-report.json'),json.dumps(records,ensure_ascii=False,indent=2));print(json.dumps({'participants':len(records),'index':idx.as_posix()}))
