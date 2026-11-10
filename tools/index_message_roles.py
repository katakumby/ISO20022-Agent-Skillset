"""Index exact-message Functionality role evidence, without inventing directions.

Only registered exact MDR definition headings are used. Clauses are retained with
source/file-page locators. Lexical extraction is a retrieval aid, not a completed
business review; unknown participants, alternatives, routing and pronouns remain
visible. Re-running picks up newly completed PDF extractions.
"""
from __future__ import annotations
import argparse, collections, hashlib, json, re
from pathlib import Path
import kb

DATE = kb.DATE
ROLE_KEYS=('sender','receiver','initiator','exchange_participants','creator','distribution_recipient','intermediary')
PARTICIPANT_OVERRIDES=[]
SPACE = re.compile(r'\s+')
PURPOSE_VERBS = 'request|instruct|provide|inform|notify|reverse|cancel|report|confirm|reject|accept|query|respond|communicate|advise|advice|enable|ask|obtain|submit|transmit|update|modify|delete|create|identify|indicate|transfer|move|send|receive|return|settle|open|close|support|allow|revoke|make|trigger|execute|establish|validate|manage|collect|acknowledge|exchange|affirm|disaffirm|express|undo'
PURPOSE = re.compile(r'\s+to\s+(?:'+PURPOSE_VERBS+r')\b', re.I)
ROLE_PHRASES = [
 'account owner/requestor', 'account owner', 'account servicer', 'executing/servicing party',
 'executing party', 'servicing party', 'instructing party', 'initiating party', 'instructed agent',
 'instructing agent', 'forwarding agent', 'debtor agent', 'creditor agent', 'previous agent',
 'next party in the payment chain', 'previous party in the payment chain', 'receiver of the payment',
 'non-financial institution customer', 'financial institution customer', 'designated agent',
 'system transaction administrator', 'transaction administrator', 'system administrator',
 'system member', 'system participant', 'directly connected party', 'directly connected system participant',
 'central securities depository participant', 'central securities depository', 'central counterparty',
 'central counter party', 'settlement market infrastructure', 'settlement infrastructure',
 'global custodian', 'local custodian', 'sub-custodian', 'custodian', 'investment management institution',
 'investment manager', 'investor', 'transfer agent', 'registrar', 'securities depository',
 'trade matching utility', 'central matching utility', 'stock exchange', 'broker/dealer', 'broker',
 'affirming party', 'confirming party', 'reporting party', 'reporting agent', 'third party',
 'market data provider', 'market infrastructure', 'payment clearing and settlement system',
 'reimbursement agent', 'beneficiary', 'debtor', 'creditor', 'bank', 'corporate', 'agent', 'customer',
 'member', 'sending MessagingEndpoint', 'receiving MessagingEndpoint', 'MessagingEndpoint',
 'BusinessActor', 'sender of the file', 'receiving party', 'sender', 'receiver', 'payments factory',
 'Business Application A', 'Business Application B', 'recipient', 'intermediary',
]

# These two exact-label links are supported by the curated participant pages and
# src-000197 Functionality p491, which explicitly names the linked functional roles.
# They do not equate institutional examples or participants in other publications.
EXPLICIT_PILOT_LABELS = {
 'participant-settlement-reconciliation-account-owner': ['account owner'],
 'participant-settlement-reconciliation-account-servicer': ['account servicer'],
}

def normalise(text):
 return SPACE.sub(' ', text).strip()

def norm_label(text):
 text = normalise(text).strip(' ,;:.()')
 text=re.sub(r'^to\s+', '', text, flags=re.I)
 text=re.sub(r'\s*/\s*','/',text)
 return re.sub(r'^(?:(?:the|an?|its|their)\s+)+', '', text, flags=re.I).casefold()

def message_name(title):
 part = re.sub(r'^\d+\s+(?:MX\s+)?[a-z]{4}\.\d{3}\.\d{3}\.\d{2,}\s+', '', title)
 return re.sub(r'V\d+$', '', part).strip()

def name_key(value):
 return re.sub(r'[^a-z0-9]', '', re.sub(r'\b(?:the|this|a|message)\b', '', value, flags=re.I).lower())

def participants(root, sources):
 result = []
 for page in sorted((root/'shared/reference/participants').glob('*.md')):
  m, _ = kb.metadata(page)
  if m.get('document_kind') != 'participant': continue
  labels = m.get('source_labels', []) + m.get('aliases', [])
  extra = EXPLICIT_PILOT_LABELS.get(m.get('participant_id'), [])
  scopes = sorted({sources[sid]['set_path'] for sid in m.get('source_ids', []) if sid in sources})
  result.append({'participant_id':m.get('participant_id'), 'path':page.relative_to(root).as_posix(),
   'title':m.get('title', page.stem), 'labels':sorted(set(labels+extra)),
   'extra_label_basis':'src-000197, file p491, §17.1 Scope; same-source curated participant definition' if extra else None,
   'source_ids':m.get('source_ids', []), 'set_paths':scopes})
 return result

def in_scope(participant, source):
 source=source.get('_participant_scope',source)
 return source['source_id'] in participant['source_ids'] or source['set_path'] in participant['set_paths']

def resolve_label(label, source, refs):
 key = norm_label(label)
 effective=source.get('_participant_scope',source)
 candidates = [r for r in refs if in_scope(r, source) and any(norm_label(x)==key for x in r['labels'])]
 direct = [r for r in candidates if effective['source_id'] in r['source_ids']]
 if direct: candidates = direct
 overrides=[r for r in PARTICIPANT_OVERRIDES if r['source_id']==effective['source_id'] and r['message_id']==source.get('_message_id') and norm_label(r['label'])==key and r.get('quote_sha256')==source.get('_quote_sha256')]
 override=None
 if overrides:
  chosen={r['participant_id'] for r in overrides}
  if len(chosen)!=1:raise ValueError('Conflicting contextual participant overrides')
  selected=[r for r in candidates if r['participant_id'] in chosen]
  if len(selected)!=1:raise ValueError('Participant override is not an existing exact-label in-scope candidate: '+str(overrides))
  candidates=selected;override=overrides[0]
 matches = [{'participant_id':r['participant_id'], 'path':r['path'],
  'basis':r['extra_label_basis'] if key in [norm_label(x) for x in EXPLICIT_PILOT_LABELS.get(r['participant_id'],[])] else ('exact label in independently matched T2S child-publication sentence' if source.get('_participant_scope') else 'exact source-scoped label/alias' if source['source_id'] in r['source_ids'] else 'exact label/alias in same message-set publication context'),
  **({'scope_alignment':source['_participant_scope_evidence']} if source.get('_participant_scope_evidence') else {}),
  **({'contextual_override':override,'basis':'Exact message, source, label and Functionality-quote match; '+override['basis']} if override else {})} for r in candidates]
 return {'label':label, 'scope_source_id':source['source_id'],
  'resolution':'resolved' if len(matches)==1 else ('ambiguous' if matches else 'unresolved'),
  'participant':matches[0] if len(matches)==1 else None, 'candidates':matches if len(matches)>1 else []}

def role_expression(text, source, refs):
 text = text.strip(' ,;:.')
 # Examples are not aliases or additional senders. Explicit lists of parties
 # remain lists; parenthetical routing/scenario qualifiers stay in the original
 # expression and are removed only from the lexical lookup label.
 # Remove complete parenthetical examples before qualifier splitting. Otherwise
 # “system member (such as a directly connected party)” becomes a broken label.
 lookup=text
 while re.search(r'\([^()]*\)',lookup):lookup=re.sub(r'\([^()]*\)','',lookup)
 main = re.split(r',?\s+(?:for example|such as|including|either directly|through|on behalf of|which may)\b|,\s*directly\b|\s+directly\s+or\s+through\b',lookup,maxsplit=1,flags=re.I)[0].strip(' ,')
 main = re.sub(r'^In principle,\s*','',main,flags=re.I)
 main=re.sub(r'\s+and\s+vice\s+versa\.?$','',main,flags=re.I)
 lookup=main
 labels = [re.sub(r'^(?:or|and)\s+','',x.strip(),flags=re.I) for x in re.split(r',\s*|\s+(?:or|and)\s+', lookup) if x.strip()]
 return {'expression':text, 'labels':[resolve_label(x,source,refs) for x in labels],
  'alternatives_or_conjunction':bool(re.search(r'\s+(?:or|and)\s+',main)),
  'qualifiers_preserved':text if text!=lookup else None}

def extract_functionality(definition, pages):
 """Retain raw page fragments and parse only the pre-Outline narrative."""
 section = re.match(r'(\d+)\s',definition['title'])
 section = section.group(1) if section else None
 chunks=[]; started=False; stopped=False
 start=definition['start_page']; end=definition['end_page']
 for page in pages[start-1:min(end,start+12)]:
  tx=page['text']
  if not started:
   match=re.search(r'(?:\d+\.1\s+)?MessageDefinition\s+Functionality',tx,re.I)
   if not match: continue
   tx=tx[match.end():];started=True
  stop=re.search(r'\b'+re.escape(section)+r'\.2\s' if section else r'\bMessageDefinition\s+Structure',tx)
  if stop:tx=tx[:stop.start()];stopped=True
  if tx.strip():chunks.append({'page':page['page'],'text':tx.strip()})
  if stop:break
 full=''; spans=[]
 for chunk in chunks:
  begin=len(full);full+=chunk['text']+'\n';spans.append((begin,len(full),chunk['page']))
 outline=re.search(r'(?m)^\s*Outline\s*$',full,re.I)
 narrative=full[:outline.start()] if outline else full
 section_marks=[(m.start(),m.group(1).lower()) for m in re.finditer(r'(?mi)^\s*(Scope|Usage)\s*:?\s*$',narrative)]
 # Split sentences while keeping page provenance and original source text. Line
 # bullets become independent segments so alternative usage paths remain visible.
 units=[]
 boundary=re.compile(r'(?<=[.!?])\s+(?=[A-Z(])|\n\s*[-•]\s+|\n\s*(?=(?:Scope|Usage)\s*:?\s*\n)',re.M)
 begins=[0]+[m.end() for m in boundary.finditer(narrative)]
 ends=[m.start() for m in boundary.finditer(narrative)]+[len(narrative)]
 for begin,end in zip(begins,ends):
  raw=narrative[begin:end].strip(); quote=normalise(raw)
  quote=re.sub(r'^(?:Scope|Usage)\s*:?\s*','',quote,flags=re.I).strip()
  if not quote:continue
  kind='scope'
  for pos,name in section_marks:
   if pos<=begin+len(raw)-len(raw.lstrip()):kind=name
  locs=sorted({pg for a,b,pg in spans if a<end and b>begin})
  units.append({'quote':quote,'raw_quote':raw,'file_pages':locs,'section':kind})
 return chunks,units,{'functionality_found':started,'functionality_end_found':stopped,
  'outline_found':bool(outline),'narrative_file_pages':sorted({p for u in units for p in u['file_pages']})}

def trim_receiver(value):
 value=re.split(r',\s*then\b|\s+in\s+order\s+to\b|\s+containing\s+information\b|\s+based\s+on\s+the\s+following\b|\s+as\s+(?:a\s+)?response\s+to\b',value,maxsplit=1,flags=re.I)[0]
 match=PURPOSE.search(value)
 value=value[:match.start()] if match else value
 value=re.split(r'\s+and\s+(?:(?:can|may|must|shall|will)\s+|is\s+used|provides\s|contains\s)',value,maxsplit=1,flags=re.I)[0]
 value=re.sub(r'\s+to\s*:?\s*$','',value)
 return value.strip(' ,;:.')

def target_for(subject, names, section, first_direction):
 key=name_key(subject)
 if key in names or key in ('', 'it', 'request', 'instruction'):
  return 'current-message' if key not in ('it','request','instruction') else 'anaphoric-context-needs-review'
 if section=='scope' and first_direction and 'message' in subject.lower():
  # Scope may spell out FIToFI. Preserve the source subject as a section-local
  # name; do not declare an alias in any other publication or message version.
  names.add(key);return 'current-message-scope-name-variant'
 return 'related-or-unspecified-message'

def directions(unit, names, first_direction, source, refs):
 q=unit['quote']; claims=[]
 # The subject must be a short message expression. This deliberately does not
 # turn every "sent by" in a usage example into the direction of this message.
 patterns=[
  ('passive',re.compile(r'(?P<subject>(?:The |This |A )?[A-Za-z][A-Za-z0-9 /()-]{0,160}?)\s+(?:is|may be|can be|shall be|must be)\s+(?:(?:also|directly|normally|typically)\s+)*(?:sent|send)\s+(?:by|from)\s+(?P<sender>.+?)\s+to\s+(?P<receiver>.+)',re.I)),
  ('active',re.compile(r'^(?P<sender>(?:An? |The )?[^.;:]{1,170}?)\s+(?:(?:may|can|must|shall|will)\s+)?(?:sends|send|forwards|forward)\s+(?P<subject>(?:an? |the |this )?[A-Za-z][A-Za-z0-9 ]{0,130}?)\s+to\s+(?P<receiver>.+)',re.I)),
  ('scope-sent-by',re.compile(r'^Sent\s+by\s+(?P<sender>.+?)\s+to\s+(?P<receiver>.+)',re.I)),
 ]
 for pattern_name,pattern in patterns:
  match=pattern.search(q)
  if not match:continue
  data=match.groupdict();subject=data.get('subject','This message')
  target=target_for(subject,names,unit['section'],first_direction)
  claim={'kind':'sender-to-receiver','pattern':pattern_name,'message_subject':subject,
   'message_target':target,'receiver':role_expression(trim_receiver(data['receiver']),source,refs)}
  if re.fullmatch(r'(?:it|they|he|she|this|that|this party|that party)',data['sender'].strip(),re.I) or re.match(r'^(?:If|When|Unless|While)\b',data['sender'],re.I):
   claim.update(kind='receiver-only',unresolved_sender_reference=data['sender'],limitation='Sender is a pronoun/reference in this clause; it is retained in the quote and is not resolved automatically.')
  else:claim['sender']=role_expression(data['sender'],source,refs)
  if re.match(r'^(?:'+PURPOSE_VERBS+r')\b',data['receiver'],re.I):
   # "Sent by X to delete..." supplies a purpose, not a receiver.
   del claim['receiver'];claim.update(kind='sender-only',limitation='The clause supplies the sender and a purpose introduced by “to”; it does not explicitly name a receiver.')
  elif re.search(r'\bas\s+(?:a\s+)?(?:reply|response)\s*$',subject,re.I):
   del claim['receiver'];claim.update(kind='sender-only',reply_target_expression=data['receiver'],limitation='The phrase following “to” is the request being answered, not an identified receiving participant.')
  claims.append(claim)
  if claim['kind']=='sender-to-receiver' and re.search(r'\band vice versa\b',q,re.I):
   claims.append({**claim,'pattern':pattern_name+'-explicit-reverse','sender':claim['receiver'],'receiver':claim['sender'],'limitation':'The source explicitly adds “and vice versa”; the two directed claims retain this reciprocal usage.'})
  if claim['kind']=='sender-to-receiver' and re.search(r'\band a message to\b',data['receiver'],re.I):
   parts=re.split(r'\s+and a message to\s+',data['receiver'],flags=re.I)
   claim['receiver']=role_expression(trim_receiver(parts[0]),source,refs)
   for part in parts[1:]:claims.append({**claim,'pattern':pattern_name+'-separate-message-recipient','receiver':role_expression(trim_receiver(part),source,refs),'limitation':'The source explicitly sends a separate message to each named recipient; the two recipients are not merged into one participant label.'})
  break
 if not claims:
  match=re.search(r'(?P<subject>(?:The |This )?[A-Za-z][A-Za-z0-9 /()-]{0,150}?)\s+(?:is|may be|can be)\s+(?:(?:also|directly)\s+)*sent\s+(?:(?:also|directly)\s+)*to\s+(?P<receiver>.+)',q,re.I)
  if match:
   if not re.match(r'^(?:'+PURPOSE_VERBS+r')\b',match['receiver'],re.I):
    claims.append({'kind':'receiver-only','pattern':'passive-sent-to','message_subject':match['subject'],
     'message_target':target_for(match['subject'],names,unit['section'],first_direction),
     'receiver':role_expression(trim_receiver(match['receiver']),source,refs),
     'limitation':'Sender is not supplied by this clause; pronouns or scenario context are not expanded.'})
 match=re.search(r'(?P<subject>(?:The |This )?[A-Za-z][A-Za-z0-9 /()-]{0,150}?)\s+is\s+exchanged\s+between\s+(?P<parties>.+)',q,re.I)
 if match:
  claims.append({'kind':'exchange-participants','pattern':'exchanged-between','message_subject':match['subject'],
   'message_target':target_for(match['subject'],names,unit['section'],first_direction),
   'exchange_participants':role_expression(trim_receiver(match['parties']),source,refs),
   'limitation':'An exchange-between statement establishes participation, not sender/receiver direction.'})
 # Explicit initiator assertions are independent from sender assertions. The
 # preceding subject is retained instead of resolving a pronoun automatically.
 for match in re.finditer(r'\binitiated\s+by\s+(.+?)(?=[,;.]|$)',q,re.I):
  current=any(key and key in name_key(q[:match.start()]) for key in names)
  claims.append({'kind':'initiator','pattern':'initiated-by','message_subject':q[:match.start()].strip(),
   'message_target':'current-message' if current else 'anaphoric-context-needs-review',
   'initiator':role_expression(match.group(1),source,refs)})
 return claims

def literal_mentions(unit, source, refs):
 phrases=set(ROLE_PHRASES)
 for p in refs:
  if in_scope(p,source):phrases.update(x for x in p['labels'] if len(x)>=5 and x.lower() not in ('from','other','party','parties'))
 # Prefer the longest overlapping expression; do not count "agent" separately
 # when a source says "debtor agent".
 patterns=sorted(phrases,key=lambda x:(-len(x),x))
 hits=[]; occupied=[]
 for phrase in patterns:
  if len(phrase)<4:continue
  expr=r'(?<![A-Za-z0-9])'+re.escape(phrase).replace(r'\ ',r'\s+')+r'(?:s)?(?![A-Za-z0-9])'
  for m in re.finditer(expr,unit['quote'],re.I):
   if any(m.start()<b and m.end()>a for a,b in occupied):continue
   occupied.append((m.start(),m.end()))
   label=m.group();resolved=resolve_label(label,source,refs)
   # Singular aliases are not manufactured for plural labels.
   hits.append({'label':label,'start':m.start(),'end':m.end(),'resolution':resolved})
 return sorted(hits,key=lambda h:h['start'])

def role_actions(unit, mentions):
 actions=[]
 for hit in mentions:
  after=unit['quote'][hit['end']:]
  m=re.match(r'\s+(?:(?:may|can|must|shall|will|should)\s+)?(?:also\s+)?(initiates?|receives?|sends?|processes?|requests?|instructs?|confirms?|cancels?|reverses?|maintains?|manages?|provides?|holds?|owns?|acts?|forwards?|submits?|creates?|reports?|queries|executes?|settles?|notifies|informs?)\b',after,re.I)
  if m:actions.append({'role':hit['resolution'],'action_verb':m.group(1),
   'voice':'active',
   'limitation':'This is a literal role/action clause. Its object and conditions remain in the quoted sentence; it is not automatically an action on the indexed message.'})
  before=unit['quote'][:hit['start']]
  passive=re.search(r'\b(created|received|processed|initiated|maintained|managed|provided|held|owned|forwarded|submitted|reported|executed|settled|confirmed|cancelled|reversed)\s*(?:-\s*)?by\s+(?:the\s+|an?\s+)?$',before,re.I)
  if passive:actions.append({'role':hit['resolution'],'action_verb':passive.group(1),'voice':'passive',
   'limitation':'The source explicitly identifies the actor of this passive clause. The object, scope and conditions remain in the source sentence.'})
 return actions

def proof_id(source_id, mid, start, number):
 return f'{source_id}-{mid}-p{start}-c{number:03d}'

def role_links(page, root, expr):
 labels=[]
 for x in expr['labels']:
  if x['participant']:labels.append(kb.link(page,root/x['participant']['path'],x['label']))
  else:labels.append(x['label']+' ('+x['resolution']+')')
 return '; '.join(labels) or expr['expression']

def write_page(root, schema, record, publications, byid):
 page=root/record['path'];folder=page.parent
 metadata={'template':False,'document_kind':'message-roles','review_status':'needs-review',
  'title':record['message_id']+' participant and direction evidence','domain':schema['domain'],
  'message_id':record['message_id'],'message_family':record['message_family'],'namespace':record['namespace'],
  'source_ids':record['source_ids'],'message_sets':record['message_sets'],'role_labels':record['role_labels'],
  'search_terms':record['role_labels'],
  'participant_ids':record['participant_ids'],'role_extraction_status':record['status'],
  'source_locations':record['source_locations'],'limitations':record['limitations'],'updated':DATE}
 text=kb.front(metadata)+'# '+record['message_id']+' participants and message directions\n\n'
 text+='This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.\n\n'
 text+='Coverage: **'+record['status']+'**. '+str(len(record['directions']))+' direction/initiator/exchange clauses; '+str(len(record['participant_ids']))+' uniquely resolved participant references.\n\n'
 for pub in publications:
  sid=pub['source_id'];source=byid[sid]
  text+='## '+sid+' — '+pub['heading']+'\n\n'+kb.source_link(root,page,source)+'; Functionality file pp'+', '.join(map(str,pub.get('file_pages',[])))+'; publication '+str(source.get('source_edition') or 'not established')+'.\n\n'
  if pub.get('error'):
   text+=pub['error']+'\n\n';continue
  text+='### Direction and initiation clauses\n\n'
  if not pub['directions']:text+='No complete sender/receiver pattern was resolved here. This does not establish that the message has no participants. Consult the remaining narrative evidence and original.\n\n'
  for claim in pub['directions']:
   text+='#### '+claim['claim_id']+'\n\n'
   text+='Kind: '+claim['kind']+'; message applicability: **'+claim['message_target']+'**; '+claim['source_id']+' file p'+', '.join(map(str,claim['file_pages']))+', '+claim['section']+'.\n\n'
   for role in ROLE_KEYS:
    if role in claim:text+='- '+role.replace('_',' ').capitalize()+': **'+kb.esc(claim[role]['expression'])+'**. '+role_links(page,root,claim[role])+'.\n'
   text+='\n> '+claim['quote']+'\n\n'
   if claim.get('limitation'):text+=claim['limitation']+'\n\n'
  text+='### Additional role mentions, actions and scenario context\n\nThese are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.\n\n'
  for item in pub['narrative']:
   # Avoid repeating a complete clause already displayed above, but preserve its
   # extra role mentions/actions as references to the same evidence ID.
   text+='**'+item['evidence_id']+' — file p'+', '.join(map(str,item['file_pages']))+', '+item['section']+'.**\n\n'
   labels=[]
   for hit in item['mentions']:
    r=hit['resolution'];p=r['participant']
    labels.append(kb.link(page,root/p['path'],hit['label']) if p else hit['label']+' ('+r['resolution']+')')
   if labels:text+='Mentioned roles: '+ '; '.join(labels)+'.\n\n'
   if item['actions']:text+='Literal actions: '+ '; '.join(x['role']['label']+' '+x['action_verb'] for x in item['actions'])+'.\n\n'
   if item.get('clause_review'):text+='Reviewed clause disposition: **'+item['clause_review']['disposition']+'**. '+item['clause_review']['rationale']+'\n\n'
   if item['direction_claim_ids']:text+='Quoted above in '+', '.join(item['direction_claim_ids'])+'.\n\n'
   else:text+='> '+item['quote']+'\n\n'
  if pub.get('unclassified_narrative'):
   text+='### Remaining Functionality narrative\n\nThese source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.\n\n'
   for item in pub['unclassified_narrative']:text+='**File p'+', '.join(map(str,item['file_pages']))+', '+item['section']+'.**\n\n> '+item['quote']+'\n\n'
  if pub['review_items']:
   text+='### Unresolved extraction and interpretation\n\n'
   for item in pub['review_items']:text+='- '+item['kind']+': '+item['detail']+(' ('+', '.join(item.get('evidence_ids',[]))+')' if item.get('evidence_ids') else '')+'\n'
   text+='\n'
  if pub.get('direction_availability_review'):text+='Functionality role scope was directly reviewed on '+pub['direction_availability_review']['date']+'. '+pub['direction_availability_review']['limitation']+'\n\n'
 text+='## Limitations and navigation\n\n'+'\n'.join('- '+x for x in record['limitations'])+'\n\n'
 links=[kb.link(page,folder/'index.md','Canonical message'),kb.link(page,root/'tracking/issues.md','Issue register')]
 if (folder/'mdr-evidence.md').exists():links.insert(1,kb.link(page,folder/'mdr-evidence.md','Full Functionality and detailed MDR evidence'))
 if (folder/'business.md').exists():links.insert(1,kb.link(page,folder/'business.md','Curated message context'))
 text+=' · '.join(links)+'\n';kb.put(page,text)
 ip=folder/'index.md'
 if ip.exists():
  old=ip.read_text(encoding='utf-8-sig');old=re.sub(r'\n<!-- ROLES-NAV-START -->.*?<!-- ROLES-NAV-END -->\n?','\n',old,flags=re.S)
  kb.put(ip,old.rstrip()+'\n\n<!-- ROLES-NAV-START -->\n'+kb.link(ip,page,'Participants, sender/receiver directions and unresolved narrative roles')+'\n<!-- ROLES-NAV-END -->\n')

def main(root,selection=None):
 global PARTICIPANT_OVERRIDES
 sources=kb.sources(root);byid={s['source_id']:s for s in sources}
 op=root/'catalog/participant-role-overrides.json';PARTICIPANT_OVERRIDES=json.loads(op.read_text(encoding='utf-8')).get('records',[]) if op.exists() else []
 rp=root/'tracking/reviews/message-role-clause-decisions.json';reviews=json.loads(rp.read_text(encoding='utf-8')) if rp.exists() else {};clause_reviews={};availability_reviews={}
 for r in reviews.get('records',[]):
  assert r['source_sha256']==byid[r['source_id']]['sha256'];assert hashlib.sha256(r['quote'].encode()).hexdigest()==r['quote_sha256'];key=(r['source_id'],r['message_id'],r['quote_sha256']);assert key not in clause_reviews;clause_reviews[key]=r
 for r in reviews.get('availability_reviews',[]):availability_reviews[(r['source_id'],r['message_id'])]=r
 canonical,conflicts=kb.canonical_schemas(root,sources)
 schemas={mid:[source] for mid,source in canonical.items()}
 selected_messages=__import__('refresh').selected_messages(root,selection) if selection else None
 definitions=collections.defaultdict(list);manifest_fingerprints={}
 for path in sorted((root/'work/documents').glob('*/message-definitions.json')):
  raw=path.read_bytes();manifest_fingerprints[path.relative_to(root).as_posix()]=hashlib.sha256(raw).hexdigest()
  for definition in json.loads(raw):
   if definition not in definitions[definition['message_id']]:definitions[definition['message_id']].append(definition)
 refs=participants(root,byid);cache={};records=[];all_reviews=[];counts=collections.Counter();scope_alignments=[]
 for mid,schema_sources in sorted(schemas.items()):
  if selected_messages is not None and mid not in selected_messages:continue
  # The canonical message index already records domain/path identity. Its
  # original schema source establishes that same path; no prefix routing.
  schema=schema_sources[0];folder=root/kb.area(schema['domain'])/'reference/messages'/mid
  if not (folder/'index.md').exists():raise ValueError('Missing canonical message index '+str(folder))
  record={'message_id':mid,'message_family':'.'.join(mid.split('.')[:2]),'namespace':schema['namespace'],
   'path':(folder/'roles.md').relative_to(root).as_posix(),'review_status':'needs-review',
   'source_ids':sorted({s['source_id'] for s in schema_sources}|{d['source_id'] for d in definitions[mid]}),
   'message_sets':sorted({s['set_slug'] for s in schema_sources}|{byid[d['source_id']]['set_slug'] for d in definitions[mid]}),
   'source_locations':[],'directions':[],'actions':[],'participants':[],'role_labels':[],'participant_ids':[],
   'source_provenance':[{'source_id':byid[sid]['source_id'],'sha256':byid[sid]['sha256'],'occurrences':byid[sid]['occurrences']} for sid in sorted({s['source_id'] for s in schema_sources}|{d['source_id'] for d in definitions[mid]})],
   'limitations':['Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.',
    'Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.',
    'Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.',
    'Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.'],
   'review_items':[],'clause_reviews':[],'definition_occurrences':len(definitions[mid])}
  publications=[];parsed=0;pending=0;allhits=[]
  for definition in sorted(definitions[mid],key=lambda d:(d['source_id'],d['start_page'])):
   sid=definition['source_id'];source=byid[sid];pagespath=root/'work/documents'/sid/'pages.json'
   pub={'source_id':sid,'source_sha256':source['sha256'],'heading':definition['title'],
    'definition_pages':[definition['start_page'],definition['end_page']], 'directions':[], 'narrative':[], 'unclassified_narrative':[], 'review_items':[]}
   publications.append(pub);record['source_locations'].append({'source_id':sid,'heading':definition['title'], 'file_pages':pub['definition_pages']})
   if not pagespath.exists():
    pending+=1;pub['error']='Exact definition was identified, but page text extraction is pending. Rebuild after the source extraction finishes.';pub['file_pages']=[definition['start_page']];continue
   if sid not in cache:
    cache[sid]=json.loads(pagespath.read_text(encoding='utf-8'))
    if cache[sid].get('source_sha256')!=source['sha256']:raise ValueError('Source/extraction checksum mismatch '+sid)
   chunks,units,boundaries=extract_functionality(definition,cache[sid]['pages']);pub.update(boundaries);pub['file_pages']=[x['page'] for x in chunks]
   if not boundaries['functionality_found']:
    pending+=1;pub['error']='Functionality boundary not resolved; no roles inferred from schema names or a neighbouring version.';continue
   parsed+=1;names={name_key(message_name(definition['title']))};number=0;handled=0;unresolved=collections.defaultdict(list)
   child_quotes=collections.defaultdict(list)
   if sid=='src-000233':
    # The combined T2S PDF contains multiple message sets. Reuse a child's
    # contextual role only for an identical Functionality sentence under the
    # same full message ID; never expand the parent scope by matching names.
    for child in definitions[mid]:
     cid=child['source_id'];cs=byid[cid]
     if cid==sid or cs['collection']!='target2securities_t2s':continue
     cp=root/'work/documents'/cid/'pages.json'
     if not cp.exists():continue
     if cid not in cache:cache[cid]=json.loads(cp.read_text(encoding='utf-8'))
     if cache[cid].get('source_sha256')!=cs['sha256']:raise ValueError('Child extraction checksum mismatch '+cid)
     _,cu,cb=extract_functionality(child,cache[cid]['pages'])
     if not cb['functionality_found']:continue
     for item in cu:child_quotes[item['quote']].append({'source_id':cid,'heading':child['title'],'file_pages':item['file_pages']})
   for unit in units:
    unit_source=source
    aligned=child_quotes.get(unit['quote'],[])
    if len({x['source_id'] for x in aligned})==1:
     proof={'message_id':mid,'parent_source_id':sid,'parent_file_pages':unit['file_pages'],'child_evidence':aligned,'basis':'Exact whitespace-normalized Functionality sentence under the same full message identifier; source occurrences remain separate.'}
     unit_source={**source,'_participant_scope':byid[aligned[0]['source_id']],'_participant_scope_evidence':proof}
     scope_alignments.append(proof)
    qsha=hashlib.sha256(unit['quote'].encode()).hexdigest();unit_source={**unit_source,'_message_id':mid,'_quote_sha256':qsha}
    decision=clause_reviews.get((sid,mid,qsha));claims=directions(unit,names,handled==0,unit_source,refs);mentions=literal_mentions(unit,unit_source,refs);actions=role_actions(unit,mentions)
    if decision:
     assert decision['file_pages']==unit['file_pages'];claims=[]
     for literal in decision['directions']:
      c={k:v for k,v in literal.items() if k not in ROLE_KEYS};c.update(pattern='source-scoped-reviewed-clause',clause_review_date=decision['review_date'],clause_review_quote_sha256=qsha)
      for role in ROLE_KEYS:
       if role in literal:c[role]=role_expression(literal[role],unit_source,refs)
      claims.append(c)
     for a in decision['actions']:actions.append({'role':resolve_label(a['label'],unit_source,refs),'action_verb':a['action_verb'],'voice':'source-reviewed-literal-clause','limitation':a['limitation'],'clause_review_date':decision['review_date']})
    cue=bool(re.search(r'\b(?:sent|sends|send|forwards?|initiated|receiv\w*|instruct\w*|party|parties|agent\w*|participant\w*|owner|servicer|endpoint|actor|custodian|member\w*|intermediary|beneficiary|debtor|creditor)\b',unit['quote'],re.I))
    if not (claims or mentions or actions or cue):pub['unclassified_narrative'].append(unit);continue
    number+=1;eid=proof_id(sid,mid,definition['start_page'],number);claimids=[]
    for i,claim in enumerate(claims,1):
     claimid=eid+'-d'+str(i);claimids.append(claimid)
     claim.update(claim_id=claimid,source_id=sid,source_sha256=source['sha256'],heading=definition['title'],
      file_pages=unit['file_pages'],section=unit['section'],quote=unit['quote'],review_status='needs-review')
     claim['condition_cues']=sorted({m.group().lower() for m in re.finditer(r'\b(?:if|when|may|can|must|shall|except|only|unless|through|directly|on behalf of|for example|such as|or|and/or)\b',unit['quote'],re.I)})
     claim['condition_interpretation']='Full conditions, alternatives, examples and routing remain in the source quote; no conditional branch is inferred.'
     pub['directions'].append(claim);record['directions'].append(claim);handled+=1
     for role in ROLE_KEYS:
      if role in claim:
       for resolution in claim[role]['labels']:
        allhits.append(dict(resolution,usage=role,evidence_id=claimid,file_pages=unit['file_pages'],message_target=claim['message_target']))
    for hit in mentions:
     allhits.append(dict(hit['resolution'],usage='narrative-mention',evidence_id=eid,file_pages=unit['file_pages'],message_target='context-only'))
     if hit['resolution']['resolution']!='resolved':unresolved[(hit['label'],hit['resolution']['resolution'])].append(eid)
    for index,action in enumerate(actions,1):
     record['actions'].append(dict(action,evidence_id=eid+'-a'+str(index),source_id=sid,source_sha256=source['sha256'],
      heading=definition['title'],file_pages=unit['file_pages'],section=unit['section'],quote=unit['quote'],
      message_target='literal-narrative-action-context',review_status='needs-review'))
     allhits.append(dict(action['role'],usage='literal-action',evidence_id=eid+'-a'+str(index),file_pages=unit['file_pages'],message_target='literal-narrative-action-context'))
    review_note={k:decision[k] for k in ('disposition','rationale','review_date','review_scope')} if decision else None
    if decision:record['clause_reviews'].append({'source_id':sid,'evidence_id':eid,'quote_sha256':qsha,**review_note})
    pub['narrative'].append(dict(unit,evidence_id=eid,mentions=mentions,actions=actions,direction_claim_ids=claimids,**({'clause_review':review_note} if review_note else {})))
    if cue and not claims and not decision and re.search(r'\b(?:sent|sends|send|initiated|forwards?|receiv\w*)\b',unit['quote'],re.I):
     pub['review_items'].append({'kind':'unparsed-direction-or-action','detail':'Role-bearing sentence retained without assigning a message direction.','evidence_ids':[eid]})
   for (label,status),ids in sorted(unresolved.items()):
    pub['review_items'].append({'kind':status+'-participant-label','detail':label+' is retained in source scope; no unique explicit participant-label match was selected.','evidence_ids':sorted(set(ids))})
   if not boundaries['functionality_end_found']:
    pub['review_items'].append({'kind':'functionality-end-unresolved','detail':'The next structure heading was not found within the bounded 13-page scan; completeness requires source review.'})
   if not boundaries['outline_found']:
    pub['review_items'].append({'kind':'outline-boundary-unresolved','detail':'No standalone Outline marker was found; any retained structural narrative requires review.'})
   available=availability_reviews.get((sid,mid))
   if available:
    assert available['source_sha256']==source['sha256'];assert sorted(available['unit_quote_sha256'])==sorted(hashlib.sha256(u['quote'].encode()).hexdigest() for u in units);pub['direction_availability_review']=available
   if not pub['directions']:
    pub['review_items'].append({'kind':'source-does-not-state-complete-direction' if available else 'no-explicit-direction-resolved','detail':'Functionality was directly reviewed; it supplies content, actions, participant or header context without a complete named sender/receiver direction. Broader curated business/flow evidence remains available.' if available else 'No complete directed clause was resolved; narrative roles and original evidence remain available.'})
   record['review_items'].extend(dict(x,source_id=sid,heading=definition['title']) for x in pub['review_items'])
  if pending:status='partial-functionality-extraction'
  elif parsed and record['directions']:status='role-evidence-extracted-needs-review'
  elif parsed:status='narrative-only-needs-review'
  else:
   collection_docs=[x for x in sources if x['format'] in ('pdf','docx') and any(x['set_path']==s['set_path'] for s in schema_sources)]
   status='exact-documentation-unmatched' if collection_docs else 'schema-only-business-documentation-unavailable'
   record['limitations'].append('No exact Functionality evidence is currently available. '+('Related collection documentation is supplied; an exact definition has not been matched.' if collection_docs else 'No PDF/DOCX business documentation is supplied in this source message-set context.'))
  record['status']=status;record['parsed_definition_occurrences']=parsed;record['pending_definition_occurrences']=pending
  # All exact source labels and evidence occurrences are retained; only exact
  # duplicate records from the same extraction scope are collapsed.
  unique={json.dumps(hit,sort_keys=True):hit for hit in allhits};record['participants']=list(unique.values())
  record['role_labels']=sorted({x['label'] for x in allhits},key=str.casefold)
  record['participant_ids']=sorted({x['participant']['participant_id'] for x in allhits if x['participant']})
  for hit in allhits:
   if hit['resolution']!='resolved' and hit['usage']!='narrative-mention':record['review_items'].append({'kind':hit['resolution']+'-direction-role','source_id':hit['scope_source_id'],'detail':hit['label'],'evidence_ids':[hit['evidence_id']]})
  rolepage=root/record['path']
  current=kb.metadata(rolepage)[0] if rolepage.exists() else {}
  if selection and (current.get('review_status')=='reviewed' or current.get('manual_curated')):
   record['limitations'].append('Existing curated role page retained; reconcile new candidate evidence before replacing its review.')
   record['candidate_evidence_path']='work/message-roles/'+mid+'.json'
  else:write_page(root,schema,record,publications,byid)
  # Detailed extraction evidence is resumable, source fingerprinted, and separate
  # from bounded catalog results. These records can be independently audited.
  kb.dump(root/'work/message-roles'/f'{mid}.json',{'message_id':mid,'publications':publications})
  records.append(record);counts[status]+=1
  all_reviews.extend(dict(item,message_id=mid,path=record['path']) for item in record['review_items'])
 if selection:
  previous=__import__('refresh').read_json(root/'catalog/message-roles.json',{'records':[]})
  refreshed_ids={r['message_id'] for r in records}
  records=[r for r in previous['records'] if r['message_id'] not in refreshed_ids]+records
  counts=collections.Counter(r.get('status','unknown') for r in records)
 payload={'schema_version':1,'generated':DATE,'root_independent_paths':True,
  'scope':'Exact supplied XSD message definitions; page-leading exact MDR definitions only.',
  'counts':dict(counts),'definition_manifest_sha256':manifest_fingerprints,'records':records}
 kb.dump(root/'catalog/message-roles.json',payload)
 report={'date':DATE,'schema_message_count':len(schemas),'role_record_count':len(records),
  'all_schema_messages_accounted_for':set(schemas)=={r['message_id'] for r in records},
  'definition_occurrences':sum(x['definition_occurrences'] for x in records),
  'parsed_definition_occurrences':sum(x['parsed_definition_occurrences'] for x in records),
  'pending_definition_occurrences':sum(x['pending_definition_occurrences'] for x in records),
  'direction_claims':sum(len(x['directions']) for x in records),'role_occurrences':sum(len(x['participants']) for x in records),
  'literal_action_claims':sum(len(x['actions']) for x in records),
  'source_scoped_clause_dispositions':sum(len(x.get('clause_reviews',[])) for x in records),
  'directly_reviewed_availability_publications':len(availability_reviews),
  'review_items_by_kind':dict(collections.Counter(x['kind'] for x in all_reviews)),
  'unique_resolved_participants':len({p for x in records for p in x['participant_ids']}),
  'counts':dict(counts),'review_items':len(all_reviews),
  'limitations':['Coverage reconciliation is not semantic or visual approval.','Run again after additional page extractions or participant labels become available.']}
 kb.dump(root/'tracking/refresh'/selection['job_id']/'message-role-coverage.json' if selection and selection.get('job_id') else root/'tracking/reviews/message-role-coverage.json',report)
 kb.dump(root/'tracking/refresh'/selection['job_id']/'role-review-items.json' if selection and selection.get('job_id') else root/'work/message-roles/review-items.json',{'date':DATE,'items':all_reviews})
 kb.dump(root/'tracking/refresh'/selection['job_id']/'role-scope-alignment.json' if selection and selection.get('job_id') else root/'tracking/reviews/t2s-role-scope-alignment.json',{'date':DATE,'matched_sentences':len(scope_alignments),'records':scope_alignments,'limitation':'Exact sentence evidence aligns scoped role references only; it is not a general publication/version equivalence claim.'})
 print(json.dumps(report,ensure_ascii=False))

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
 parser.add_argument('--selection',type=Path);parser.add_argument('--job');args=parser.parse_args();root=args.root.resolve()
 selection=__import__('refresh').read_json(args.selection) if args.selection else None
 if args.job:kb.set_write_context(root,args.job)
 if selection:__import__('refresh').check_selection(root,selection,True)
 main(root,selection)
