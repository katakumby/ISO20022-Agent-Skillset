"""Preserve source-scoped narrative participants absent from definition tables.

Only explicit role mentions already retained with exact MDR Functionality quotes
are eligible. Generic pronouns/sender variables remain unresolved. The combined
T2S publication is excluded here because its internal message-set scopes must
be matched independently. No institution is equated with a functional role.
"""
import argparse,collections,json,re
from pathlib import Path
import kb
import index_message_roles as mr

PLURALS={'account owners':'account owner','banks':'bank','customers':'customer','members':'member','investors':'investor','distributors':'distributor','agents':'agent','market infrastructures':'market infrastructure','financial institutions':'financial institution','non-financial institution customers':'non-financial institution customer'}
EXCLUDE={'agent','sender','receiver','recipient','receiving party','sender of the file'}
FUNCTIONAL={'account owner','account owner/requestor','account servicer','designated agent','initiating party','instructing party','executing party','executing/servicing party','servicing party','member','system member','system participant','directly connected party','directly connected system participant','transaction administrator','system transaction administrator','instructing agent','instructed agent','next party in the payment chain','previous party in the payment chain','previous agent','receiver of the payment','reimbursement agent','reporting agent','third party'}
BUSINESS={'bank','corporate','customer','financial institution','non-financial institution customer','investor','investment manager','investment management institution','registrar','custodian','global custodian','local custodian','sub-custodian','broker','broker/dealer','securities depository','central securities depository','central securities depository participant','central counter party','settlement infrastructure','settlement market infrastructure','market infrastructure','market data provider','stock exchange','trade matching utility','central matching utility','transfer agent','distributor','intermediary','beneficiary','payment clearing and settlement system','payments factory'}

def key(label):
 value=mr.norm_label(label)
 return PLURALS.get(value,value)

def main(root):
 sources={s['source_id']:s for s in kb.sources(root)}
 refs=mr.participants(root,sources)
 records=collections.defaultdict(lambda:{'labels':set(),'evidence':[],'directions':[],'actions':[]})
 ignored=collections.Counter()
 for path in sorted((root/'work/message-roles').glob('*.json')):
  data=json.loads(path.read_text('utf-8'))
  if 'publications' not in data:continue
  mid=data['message_id']
  for pub in data['publications']:
   sid=pub['source_id'];source=sources[sid]
   for unit in pub['narrative']:
    for hit in unit['mentions']:
     label=key(hit['label'])
     if sid=='src-000233':ignored['combined-T2S-needs-child-scope']+=1;continue
     if label in EXCLUDE or label not in FUNCTIONAL|BUSINESS:ignored['generic-or-not-approved-label']+=1;continue
     resolved=mr.resolve_label(hit['label'],source,refs)
     # A prior narrative record is refreshed from original quotes. Other
     # canonical participants keep their content and identity unchanged.
     existing=resolved.get('participant')
     if existing and not existing['participant_id'].startswith('participant-narrative-'):continue
     if resolved['resolution']=='ambiguous':ignored['ambiguous-existing-canonical-records']+=1;continue
     rec=records[sid,label];rec['labels'].add(hit['label'])
     item={'message_id':mid,'evidence_id':unit['evidence_id'],'source_id':sid,'heading':pub['heading'],'file_pages':unit['file_pages'],'section':unit['section'],'quote':unit['quote']}
     if item not in rec['evidence']:rec['evidence'].append(item)
     for claim in pub['directions']:
      if claim['claim_id'].startswith(unit['evidence_id']+'-') and any(key(x['label'])==label for role in ['sender','receiver','initiator','exchange_participants'] for x in claim.get(role,{}).get('labels',[])):
       if claim not in rec['directions']:rec['directions'].append(claim)
     for action in unit['actions']:
      if key(action['role']['label'])==label:
       a={'action_verb':action['action_verb'],'evidence_id':unit['evidence_id'],'quote':unit['quote'],'message_id':mid}
       if a not in rec['actions']:rec['actions'].append(a)
 for (sid,label),rec in records.items():
  rec['participant_id']='participant-narrative-'+sid+'-'+kb.slug(label)
  rec['path']='shared/reference/participants/'+rec['participant_id']+'.md'
 reports=[];groups=collections.defaultdict(list)
 for (sid,label),rec in sorted(records.items()):
  s=sources[sid];page=root/rec['path'];mids=sorted({x['message_id'] for x in rec['evidence']})
  role_type='functional participant role in quoted Functionality context' if label in FUNCTIONAL else 'business role or institutional example in quoted Functionality context'
  locations=[{'source_id':sid,'heading':e['heading'],'file_pages':e['file_pages'],'evidence_id':e['evidence_id']} for e in rec['evidence']]
  limits=['This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.',
   'Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.',
   'Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.',
   'No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.']
  meta={'template':False,'document_kind':'participant','review_status':'needs-review','curated':True,'domain':s['domain'],'participant_id':rec['participant_id'],'title':label.title()+' — '+s['set_title']+' narrative scope','source_ids':[sid],'source_editions':[s['source_edition']] if s.get('source_edition') else [],'source_labels':sorted(rec['labels'],key=str.casefold),'aliases':[],'role_type':role_type,'message_sets':[s['set_slug']],'message_ids':mids,'message_families':sorted({'.'.join(x.split('.')[:2]) for x in mids}),'flows':[],'source_locations':locations,'search_terms':sorted(rec['labels']|{label}),'limitations':limits}
  text=kb.front(meta)+'# '+label.title()+' — '+s['set_title']+'\n\n'
  text+='## Definition and applicable context\n\nThis source names **'+label+'** in the Functionality of the messages listed below. The record is scoped to '+s['set_title']+', '+str(s.get('source_edition') or 'edition not established')+'. Classification: '+role_type+'. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.\n\n'
  text+='The first explicit source context is:\n\n> '+rec['evidence'][0]['quote']+'\n\n'+sid+', file p'+', '.join(map(str,rec['evidence'][0]['file_pages']))+', '+rec['evidence'][0]['heading']+', '+rec['evidence'][0]['section']+'. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.\n\n'
  text+='## Responsibilities, actions and relationships\n\nThe following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.\n\n'
  rows=[]
  for claim in rec['directions']:
   usages=[role for role in ['sender','receiver','initiator','exchange_participants'] if any(key(x['label'])==label for x in claim.get(role,{}).get('labels',[]))]
   other=[]
   for role in ['sender','receiver','initiator','exchange_participants']:
    if role not in claim:continue
    expr=claim[role]['expression'];links=[]
    for res in claim[role]['labels']:
     dest=records.get((sid,key(res['label'])))
     if dest:links.append(kb.link(page,root/dest['path'],res['label']))
     elif res.get('participant'):links.append(kb.link(page,root/res['participant']['path'],res['label']))
    other.append(role+': '+expr+(' ('+'; '.join(links)+')' if links else ''))
   anchor=claim['claim_id'].rsplit('-d',1)[0]
   rows.append([', '.join(usages),claim['message_subject'],claim['message_target'],'; '.join(other),'['+claim['claim_id']+'](#'+anchor+'); file p'+', '.join(map(str,claim['file_pages']))])
  text+=kb.table(['This participant in clause','Source message subject','Message applicability','Other roles / source expressions','Evidence'],rows) if rows else 'No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.\n'
  if rec['actions']:
   text+='\nLiteral action verbs: '+', '.join(sorted({a['action_verb'] for a in rec['actions']}))+'. Their objects, conditions and message context are preserved in the quoted evidence, rather than inferred from the verb alone.\n'
  text+='\n## Complete source evidence\n\n'
  for e in rec['evidence']:
   text+='<a id="'+e['evidence_id']+'"></a>\n\n### '+e['evidence_id']+'\n\n'+sid+'; file p'+', '.join(map(str,e['file_pages']))+'; '+e['heading']+'; '+e['section']+'.\n\n> '+e['quote']+'\n\n'
  text+='## Applicable messages and flow navigation\n\n'
  rows=[]
  for mid in mids:
   schema=next(x for x in sources.values() if x['format']=='xsd' and mid in x.get('message_ids',[]));dest=root/kb.area(schema['domain'])/'reference/messages'/mid/'roles.md'
   rows.append([mid,kb.link(page,dest,'Exact message-role evidence'),', '.join(e['evidence_id'] for e in rec['evidence'] if e['message_id']==mid)])
  text+=kb.table(['Exact message','Canonical evidence','Participant occurrence IDs'],rows)
  flow_index=root/s['set_path']/'flows/index.md'
  text+='\n'+(kb.link(page,flow_index,'Message-set flows') if flow_index.exists() else kb.link(page,root/s['set_path']/'index.md','Message-set reference'))+' is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.\n\n'
  text+='## Source labels, identifiers and limitations\n\nSource spellings: '+', '.join('`'+x+'`' for x in sorted(rec['labels']))+'. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.\n\n'+'\n'.join('- '+x for x in limits)+'\n\n'+kb.source_link(root,page,s)+' · '+kb.link(page,root/'tracking/issues.md','Issue register')+' · '+kb.link(page,root/'catalog/participants.md','Participant catalog')+'\n'
  kb.put(page,text);reports.append({'participant_id':rec['participant_id'],'path':rec['path'],'source_id':sid,'label':label,'message_count':len(mids),'quote_count':len(rec['evidence']),'direction_clause_count':len(rec['directions']),'status':'needs-review'})
  groups[s['set_path']].append((rec,label,s))
 for scope,group in groups.items():
  page=root/scope/'participants-narrative.md';s=group[0][2]
  meta={'template':False,'document_kind':'participant-index','review_status':'needs-review','domain':s['domain'],'source_ids':sorted({x[2]['source_id'] for x in group}),'message_sets':[s['set_slug']],'limitations':['Scoped Functionality evidence; no same-name equivalence across publications inferred.']}
  text=kb.front(meta)+'# Participants preserved from message Functionality\n\nThese source-scoped records supplement participant-definition and role-matrix tables. They retain institutional examples separately from functional roles.\n\n'+kb.table(['Source label','Scoped reference','Source','Evidence occurrences'],[[label,kb.link(page,root/rec['path'],'Participant'),ss['source_id'],len(rec['evidence'])] for rec,label,ss in group])+'\n'+kb.link(page,root/scope/'participants.md','Definition-table participant index')+'\n'
  if not (root/scope/'participants.md').exists():text=text.replace('\n'+kb.link(page,root/scope/'participants.md','Definition-table participant index')+'\n','\n')
  kb.put(page,text)
  base=root/scope/'participants.md'
  if base.exists():
   text=base.read_text('utf-8');text=re.sub(r'\n<!-- NARRATIVE-PARTICIPANTS-START -->.*?<!-- NARRATIVE-PARTICIPANTS-END -->\n?','\n',text,flags=re.S)
   kb.put(base,text.rstrip()+'\n\n<!-- NARRATIVE-PARTICIPANTS-START -->\n'+kb.link(base,page,'Additional participants explicitly named in message Functionality')+'\n<!-- NARRATIVE-PARTICIPANTS-END -->\n')
 report={'date':kb.DATE,'records':reports,'participants':len(reports),'source_scopes':len({x['source_id'] for x in reports}),'evidence_occurrences':sum(x['quote_count'] for x in reports),'ignored_occurrences':dict(ignored),'limitations':['Narrative preservation and source linking do not constitute completed semantic review.','Combined T2S source needs internal child-set scope matching; generic sender/receiver/agent words remain unresolved.']}
 kb.dump(root/'tracking/reviews/narrative-participants.json',report);print(json.dumps({k:v for k,v in report.items() if k!='records'}))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();main(a.root.resolve())
