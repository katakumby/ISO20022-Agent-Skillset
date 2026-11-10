"""Check message-role evidence against original PDF bytes and targeted semantics."""
import argparse, hashlib, io, json, re
from pathlib import Path
from urllib.parse import unquote
from pypdf import PdfReader
import kb
from index_message_roles import ROLE_KEYS, norm_label

def main(root):
 payload=json.loads((root/'catalog/message-roles.json').read_text(encoding='utf-8'))
 records={r['message_id']:r for r in payload['records']}
 sources={s['source_id']:s for s in kb.sources(root)}
 schema_ids={m for s in sources.values() if s['format']=='xsd' for m in s['message_ids']}
 errors=[]; original_cache={}; page_cache={}; quote_checks=0; link_checks=0;disposition_checks=0;override_checks=0;all_override_checks=0
 def norm(text):return re.sub(r'\s+',' ',text).strip()
 def original_text(sid,pages):
  if sid not in original_cache:
   data=kb.read_source(root,sources[sid]);actual=hashlib.sha256(data).hexdigest()
   if actual!=sources[sid]['sha256']:raise ValueError('Original source checksum changed: '+sid)
   original_cache[sid]=PdfReader(io.BytesIO(data))
  for page in pages:
   key=(sid,page)
   if key not in page_cache:page_cache[key]=original_cache[sid].pages[page-1].extract_text() or ''
  return norm(' '.join(page_cache[(sid,page)] for page in pages))
 if set(records)!=schema_ids:errors.append({'kind':'schema-role-coverage','missing':sorted(schema_ids-set(records)),'extra':sorted(set(records)-schema_ids)})
 for mid,record in records.items():
  if not record['namespace'].endswith(':'+mid):errors.append({'kind':'namespace','message_id':mid})
  page=root/record['path'];meta,body=kb.metadata(page)
  if meta.get('message_id')!=mid or meta.get('document_kind')!='message-roles' or meta.get('review_status')!='needs-review':errors.append({'kind':'page-metadata','message_id':mid})
  if '{{' in body or '}}' in body:errors.append({'kind':'template-placeholder','message_id':mid})
  for match in re.finditer(r'\]\((<?[^\n)]+>?)\)',body):
   target=unquote(match.group(1).strip('<>')).split('#',1)[0]
   if not target or re.match(r'^[a-z]+:',target,re.I):continue
   link_checks+=1
   if not (page.parent/target).resolve().exists():errors.append({'kind':'broken-link','message_id':mid,'target':target})
  for claim in record['directions']+record.get('actions',[]):
   quote_checks+=1
   original=original_text(claim['source_id'],claim['file_pages'])
   if norm(claim['quote']) not in original:errors.append({'kind':'quote-not-in-original','message_id':mid,'evidence_id':claim.get('claim_id') or claim['evidence_id']})
   if claim['source_sha256']!=sources[claim['source_id']]['sha256']:errors.append({'kind':'claim-checksum','message_id':mid})
  for hit in record['participants']:
   if hit['participant']:
    target=root/hit['participant']['path'];m,_=kb.metadata(target)
    if m.get('participant_id')!=hit['participant']['participant_id']:errors.append({'kind':'participant-reference','message_id':mid,'participant':hit['participant']})
  for hit in record['directions']:
   for role in ROLE_KEYS:
    if role in hit:
     for label in hit[role]['labels']:
      # Regressions caught by inspecting original source sentences: a purpose
      # infinitive, a request being answered, and an unresolved pronoun are not
      # named recipient/sender participants.
      value=norm(label['label']).lower()
      if value in ('a','an','the','vice versa','it','it will','then the payment method is called the serial method') or '(' in value or ')' in value or (role=='receiver' and (re.match(r'^(acknowledge|delete|express|provide)\b',value) or re.search(r'\b(?:modify|cancel|backup|delete).* request$',value))):errors.append({'kind':'nonparticipant-role-label','message_id':mid,'label':value})
      if label.get('participant',{}):
       ov=label['participant'].get('contextual_override')
       if ov:
        override_checks+=1
        if ov['message_id']!=mid or ov['quote_sha256']!=hashlib.sha256(hit['quote'].encode()).hexdigest() or norm_label(ov['label'])!=norm_label(label['label']) or ov['participant_id']!=label['participant']['participant_id']:errors.append({'kind':'contextual-override-proof','message_id':mid,'claim_id':hit['claim_id']})
  detailed=json.loads((root/'work/message-roles'/f'{mid}.json').read_text(encoding='utf-8'))
  unit_by_id={u['evidence_id']:u for p in detailed['publications'] for u in p['narrative']}
  for ph in record['participants']:
   ov=(ph.get('participant') or {}).get('contextual_override')
   if not ov:continue
   all_override_checks+=1;eid=re.sub(r'-(?:a|d)\d+$','',ph['evidence_id']);unit=unit_by_id.get(eid)
   if not unit or ov['message_id']!=mid or ov['quote_sha256']!=hashlib.sha256(unit['quote'].encode()).hexdigest() or norm_label(ov['label'])!=norm_label(ph['label']) or ov['participant_id']!=ph['participant']['participant_id']:errors.append({'kind':'contextual-participant-override-proof','message_id':mid,'evidence_id':ph['evidence_id']})
  for pub in detailed['publications']:
   for unit in pub['narrative']:
    if unit.get('clause_review'):
     disposition_checks+=1
     if norm(unit['quote']) not in original_text(pub['source_id'],unit['file_pages']):errors.append({'kind':'reviewed-clause-not-in-original','message_id':mid,'evidence_id':unit['evidence_id']})
 samples=[]
 expected=[
  ('sese.020.001.09','src-000197',458,'account owner','account servicer','Cancellation request: owner requests cancellation of an existing instruction; sender is not inferred to be an initiator.'),
  ('sese.026.001.12','src-000197',654,'account servicer','account owner','Settlement reversal: direction differs from the owner-to-servicer cancellation request.'),
  ('semt.020.001.07','src-000197',406,'account servicer','account owner','Securities message cancellation is distinct from settlement reversal; usage exclusions remain quoted in the role page.'),
  ('seev.037.001.17','src-000080',665,'account servicer','account owner or its designated agent','Corporate-action movement reversal retains the alternative designated-agent recipient and exact publication.'),
  ('camt.003.001.08','src-000015',13,'member','transaction administrator','Operational cash management query; member is retained as a scoped unresolved label where no exact alias exists.'),
  ('camt.004.001.10','src-000015',48,'transaction administrator','member','Operational response direction differs from query; separate push-mode initiation clause retains its condition.'),
  ('camt.052.001.14','src-000005',4,'account servicer','account owner or to a party authorised by the account owner','Bank-to-customer reporting retains an authorised-party alternative; it is not merged with operational cash management.'),
  ('pain.001.001.13','src-000174',4,'initiating party','forwarding agent or debtor agent','Direct and relay alternatives are retained. The later “It will forward” clause has no invented sender label.'),
  ('pacs.008.001.14','src-000163',702,'debtor agent','creditor agent','FinancialInstitutionToFinancialInstitution scope spelling is local to this exact definition; intermediary routing remains in the quote.'),
 ]
 for mid,sid,pg,sender,receiver,note in expected:
  matches=[d for d in records[mid]['directions'] if d['source_id']==sid and pg in d['file_pages'] and d['kind']=='sender-to-receiver' and sender in d['sender']['expression'].lower() and receiver in d['receiver']['expression'].lower() and d['message_target'] in ('current-message','current-message-scope-name-variant')]
  result={'message_id':mid,'source_id':sid,'file_page':pg,'expected_sender_expression':sender,'expected_receiver_expression':receiver,'pass':bool(matches),'note':note}
  samples.append(result)
  if not matches:errors.append({'kind':'sample-direction','message_id':mid})
 for mid in ('head.001.001.04','head.002.001.01'):
  directions=[d for d in records[mid]['directions'] if d['kind']=='sender-to-receiver' and d['message_target'].startswith('current-message')]
  passed=not directions
  samples.append({'message_id':mid,'pass':passed,'note':'Header Functionality roles are retained without inventing a fixed business sender/receiver direction.'})
  if not passed:errors.append({'kind':'header-inferred-direction','message_id':mid})
 schema_only=[r for r in records.values() if r['status']=='schema-only-business-documentation-unavailable']
 if any(r['directions'] or r.get('actions') for r in schema_only):errors.append({'kind':'schema-only-inferred-business-role'})
 samples.append({'kind':'schema-only','records':len(schema_only),'pass':not any(r['directions'] or r.get('actions') for r in schema_only),'note':'Schema-only messages expose unavailable business evidence without inferred participant directions.'})
 same_role=[r for r in records['sese.020.001.09']['participants'] if r['usage']=='sender' and r['participant']]
 other_role=[r for r in records['seev.037.001.17']['participants'] if r['usage']=='receiver' and r['participant'] and 'owner' in r['label']]
 scoped=bool(same_role and other_role and same_role[0]['participant']['participant_id']!=other_role[0]['participant']['participant_id'])
 samples.append({'kind':'same-label-distinct-context','pass':scoped,'note':'Settlement account-owner and corporate-action account-owner references remain distinct source-scoped definitions.'})
 if not scoped:errors.append({'kind':'scoped-participant-sample'})
 extra_samples=[
  ('auth.047.001.01',lambda r:any(d['kind']=='creation-and-distribution' and d.get('creator',{}).get('expression')=='ESMA' and 'sender' not in d for d in r['directions']),'ESMA creator and intended distribution recipient remain distinct from wire sender/receiver.'),
  ('head.001.001.04',lambda r:any(d['kind']=='creator' and d['message_target']=='business-message-with-accompanying-header' for d in r['directions']),'BAH composition records creation of a Business Message with header, not an invented fixed header sender/receiver pair.'),
  ('admi.007.001.01',lambda r:any(d['pattern'].endswith('explicit-reverse') for d in r['directions']),'Explicit vice-versa direction is retained without making vice versa a participant.'),
  ('camt.064.001.01',lambda r:any('directly connected system participant' in d.get('exchange_participants',{}).get('expression','') and any('directly connected system participant' in x['label'] for x in d.get('exchange_participants',{}).get('labels',[])) for d in r['directions']),'Directly connected participant is not truncated to an article by routing-qualifier splitting.'),
  ('sese.037.001.09',lambda r:any(d['message_target']=='current-message-conditional-return' and d['sender']['expression']=='receiving account servicer' and d['receiver']['expression']=='delivering account servicer' for d in r['directions']),'Conditional portfolio-return direction reverses the servicing roles only under the stated missing-chain condition.'),
  ('sese.023.001.13',lambda r:any(d['message_target']=='current-message-copy-or-copyduplicate-option' and 'sender' not in d and d['receiver']['expression']=='third party' for d in r['directions']),'Informational-copy receiver is explicit; copy sender is not inferred from the ordinary instruction direction.'),
  ('setr.058.001.03',lambda r:any(d['message_target']=='current-message-qualified-source-wording' and 'is ent by' in d['quote'] for d in r['directions']),'Visually confirmed source typo remains literal and qualified, while explicit by/to role expressions stay retrievable.'),
  ('acmt.025.001.02',lambda r: any(x['kind']=='source-does-not-state-complete-direction' for x in r['review_items']) and not r['directions'],'The source only describes query content; missing named direction stays visible after direct Functionality review.')]
 for mid,check,note in extra_samples:
  passed=check(records[mid]);samples.append({'message_id':mid,'pass':passed,'note':note})
  if not passed:errors.append({'kind':'reviewed-clause-regression','message_id':mid})
 report={'date':kb.DATE,'catalog_snapshot_sha256':hashlib.sha256((root/'catalog/message-roles.json').read_bytes()).hexdigest(),
  'role_records':len(records),'original_pdf_sources_checked':len(original_cache),'original_pdf_pages_checked':len(page_cache),
  'direction_and_action_quotes_checked_against_original_pdf':quote_checks,'relative_links_checked':link_checks,
  'reviewed_clause_dispositions_checked_against_original_pdf':disposition_checks,'contextual_direction_overrides_checked':override_checks,
  'all_contextual_participant_overrides_checked':all_override_checks,
  'all_schema_messages_accounted_for':set(records)==schema_ids,'sample_semantic_checks':samples,'errors':errors,
  'result':'pass' if not errors else 'fail',
  'review_scope':'Exact source-quote, metadata, link and targeted semantic checks. Not exhaustive semantic approval of every role, condition or source table/diagram.'}
 kb.dump(root/'tracking/reviews/message-role-audit.json',report)
 print(json.dumps({k:v for k,v in report.items() if k not in ('sample_semantic_checks',)},ensure_ascii=False))
 for document in original_cache.values():document.stream.close()
 return not errors

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);args=parser.parse_args()
 raise SystemExit(0 if main(args.root.resolve()) else 1)
