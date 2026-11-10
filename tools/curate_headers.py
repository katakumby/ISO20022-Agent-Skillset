"""Curate supplied header roles and scenarios with exact source locators."""
from pathlib import Path
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from extract_workbooks import fm,write,relative
ROOT=Path(__file__).resolve().parents[1];JOB='job-000001'
SOURCES={s['source_id']:s for s in json.loads((ROOT/'catalog/sources.json').read_text('utf-8'))['sources']}
MUG='shared/reference/message-sets/business-application-header/2021-11-03-v3.0'
FLOWBASE=MUG+'/flows'
CONCEPT='shared/reference/concepts/business-application-header-and-business-file-header.md'
def src(page,sid,loc):
 s=SOURCES[sid];o=s['occurrences'][0];return '['+sid+']('+relative(ROOT/page,ROOT/o['path'])+')'+(' archive member '+o['archive_member'] if o.get('archive_member') else '')+', '+loc
def link(page,target,label):return '['+label+']('+relative(ROOT/page,ROOT/target)+')'
def save(page,title,body,**meta):
 write(ROOT,ROOT/page,fm(domain='shared',**meta)+'# '+title+'\n\n'+body+'\n',JOB)
roles=[
 ('bah-sending-messaging-endpoint','Sending MessagingEndpoint',['Sending MessagingEndpoint','From','Business Application A (in MUG sender scenarios)'],
  'The endpoint that creates this Business Message for a receiving endpoint that will process it. This is a functional role for a particular message, not an institution class.',
  'Creates a new Business Message and accompanying BAH for each business event. Identifies its business recipient in To. The transport sending address may differ. Its BusinessMessageIdentifier identifies the message unambiguously to its creator.',
  [('src-000011','file/printed page 4 §2.1; page 5 §2.1 D; page 9 §2.4.2'),('src-000012','file/printed pages 9–11 §2.2')],
  'The From field uses Party51Choice: organisation/person identification or financial-institution identification. BICFI, clearing-system member identification, LEI and other identifiers are optional choices within the selected structures; none is a universal identity requirement for this role (src-000011 pp9–11).'),
 ('bah-receiving-messaging-endpoint','Receiving MessagingEndpoint',['Receiving MessagingEndpoint','To','Business Application B (in MUG receiver scenarios)'],
  'The endpoint designated by the sending endpoint as the ultimate processor of this Business Message. It is a functional recipient role, not a fixed type of institution.',
  'Processes the business message. In a possible-duplicate scenario, processes it as original only if the original was not received; otherwise takes action to avoid processing it again. Its transport receiving address may differ from this business identity.',
  [('src-000011','file/printed page 4 §2.1; page 11 §2.4.3; page 15 §2.4.11'),('src-000012','file/printed page 19 §2.10')],
  'The To field uses Party51Choice with organisation/person or financial-institution identification. Particular identifiers depend on the chosen structure and implementation context (src-000011 pp11–13).'),
 ('bah-business-intermediary','Business application acting as intermediary',['Business Application in the middle','middle man that processes the Business Message'],
  'An intermediary that performs business processing is a business application in the guide. The same application is the recipient of one Business Message and sender of a different Business Message.',
  'Processes the first Business Message, appears as its BAH recipient, then creates a different Business Message and appears as the second BAH sender. This role is distinct from forwarding alone.',
  [('src-000012','file/printed page 4 §1.4; pages 9–10 §2.2')],
  'The guide supplies no separate institution identifier scheme for this scoped role; the BAH From/To identification fields apply to each relevant message.'),
 ('bah-technical-forwarder','Technical intermediary that forwards a Business Message',['technical middle man'],
  'A transport intermediary that performs no business function on the message. This is a functional transport role and is not identified as a BAH business sender or receiver solely because it forwards the message.',
  'Forwards to the correct business application without opening or changing the Business Message. Only transport headers change in the forwarding scenario. The guide warns that connecting networks with incompatible non-ISO header mechanisms can lose business information when BAH is omitted.',
  [('src-000012','file/printed page 4 §1.4; pages 9–10 §2.2')],
  'No BAH identity is assigned merely because of technical forwarding. The source does not define a transport-address scheme.'),
 ('bfh-system-user','Business File Header system user',['SystemUser','SysUsr'],
  'A user account defined in static data. It represents an individual or application interacting with a system administrator such as T2S. It is a functional access role, not an institution.',
  'Triggers available functions. Available functions follow the privileges granted to that user. The administrator provides no attribute distinguishing individuals from applications.',
  [('src-000349','file/printed page 7 §2.4.1.2.1 SystemUser')],
  'SystemUser is optional Max140Text within optional ApplicationSpecifics; the source defines a static-data account but no globally unique identifier scheme.'),
 ('bfh-system-administrator','Business File Header system administrator',['System administrator'],
  'The system with which a system user interacts in the SystemUser definition. T2S is given as an example. This scoped role is not equated with an account servicer or any other institution role.',
  'Exposes functions that system users trigger according to the privileges for which they are grantees. The supplied SystemUser definition states no attribute distinguishing human users from applications.',
  [('src-000349','file/printed page 7 §2.4.1.2.1 SystemUser')],
  'No identifier scheme for this role is defined in the cited section.')
]
scenarios=[
 ('business-message-exchange','Send a Business Message','2.2','9–11',
  'A sending business application creates and sends a Business Message to its receiving business application.',
  'A business message is to be exchanged. The guide does not supply further process-specific preconditions.',
  [('Sending endpoint','Creates the BAH and message; populates From, To, BusinessMessageIdentifier, MessageDefinitionIdentifier and CreationDate.','Sending endpoint → receiving endpoint'),
   ('Technical forwarder, if present','Forwards without business processing. Only the transport header changes.','Business sender and receiver remain the same'),
   ('Business intermediary, if present','Processes the first Business Message and creates a different Business Message; it is recipient on the first and sender on the second.','Distinct first and second exchanges')],
  'Forwarding and business processing are different branches. The source notes implementation challenges when non-ISO network headers cannot carry required business information without BAH.',
  'The intended receiving business application receives the business message. No settlement, accounting or payment outcome is specified.',
  ['bah-sending-messaging-endpoint','bah-receiving-messaging-endpoint','bah-business-intermediary','bah-technical-forwarder']),
 ('character-set','Declare additional character sets','2.3','11–12',
  'Inform the receiving application that relevant text elements may contain non-Basic-Latin characters.',
  'Text may contain additional character sets.',
  [('Sending endpoint','Lists each additional character set in CharacterSet, separated by semicolons, and sends the message.','Sending endpoint → receiving endpoint'),
   ('Receiving endpoint','Interprets relevant text within the stated character sets.','Receives business message')],
  'More constrained text datatypes retain their own constraints; the BAH character-set statement does not override them.',
  'The receiver can identify declared character sets; no further processing postcondition is specified.',
  ['bah-sending-messaging-endpoint','bah-receiving-messaging-endpoint']),
 ('business-service','Identify the business service','2.4','12',
  'Let the receiver relate the Business Message unambiguously to the service in which it is used.',
  'Normally used when a business message can be used in multiple services. Service may be provider-defined or bilaterally/multilaterally agreed.',
  [('Sending endpoint','Populates BusinessService with the service identification and sends the message.','Sending endpoint → receiving endpoint'),
   ('Receiving endpoint','Relates the message to the identified business service.','Receives business message')],
  'The guide does not define service identifiers or alternative failure paths.',
  'Business-service context is identified.',
  ['bah-sending-messaging-endpoint','bah-receiving-messaging-endpoint']),
 ('market-practice','Identify an implementation specification','2.5','13–14',
  'Indicate the market-practice specification with which the message complies.',
  'Parties have agreed a business context. A market practice restricts the underlying message and may extend it through extensions or supplementary data.',
  [('Sending endpoint','Supplies MarketPractice Registry and Identification identifying the specification within that registry.','Sending endpoint → receiving endpoint')],
  'Identification can include a URN, version or date; the examples are source examples, not prescribed universal registry values.',
  'The recipient can identify the referenced implementation specification; compliance checking is not specified as an ordered workflow.',
  ['bah-sending-messaging-endpoint','bah-receiving-messaging-endpoint']),
 ('business-processing-date','Indicate the business processing date','2.6','14–15',
  'Tell the receiver which business processing date the message refers to.',
  'Market practice or bilateral agreement should define use of this field.',
  [('Sending endpoint','Supplies BusinessProcessingDate for the receiver and sends the message.','Sending endpoint → receiving endpoint')],
  'BusinessProcessingDate may differ from CreationDate. Source examples cover after-hours processing, legal business-date differences, time zones, and forward-dated requests; no particular calendar rule is universal.',
  'The intended business processing date is communicated. Source-defined settlement or processing success is not guaranteed by this header.',
  ['bah-sending-messaging-endpoint','bah-receiving-messaging-endpoint']),
 ('copy','Send a copy of a Business Message','2.7','16',
  'Send a copy of a previously sent business message.',
  'A prior Business Message exists.',
  [('Sending endpoint','Sends the copy with CopyDuplicate=COPY and Related carrying relevant BAH elements of the original message.','Sending endpoint → receiving endpoint')],
  'No failure, cancellation or reversal branch is specified in this scenario. Copy does not itself request a settlement reversal.',
  'The receiver is informed that this is a copy and can identify the related original.',
  ['bah-sending-messaging-endpoint','bah-receiving-messaging-endpoint']),
 ('duplicate','Send a duplicate of a Business Message','2.8','17',
  'Send a duplicate of a previously sent Business Message.',
  'A prior Business Message exists; the source example describes a resend upon request.',
  [('Sending endpoint','Sends the duplicate with CopyDuplicate=DUPL and Related carrying relevant original BAH elements.','Sending endpoint → receiving endpoint')],
  'This information/confirmation duplicate scenario is separate from the possible-duplicate branch where receipt is unknown.',
  'The receiver is told that the message is a duplicate.',
  ['bah-sending-messaging-endpoint','bah-receiving-messaging-endpoint']),
 ('duplicate-of-copy','Send a duplicate of a prior copy','2.9','18',
  'Send a duplicate of a previously sent copy of a Business Message.',
  'A prior copy Business Message exists.',
  [('Sending endpoint','Uses CopyDuplicate=CODU and Related carrying relevant BAH elements of the copy Business Message.','Sending endpoint → receiving endpoint')],
  'The related message is the copy referenced by this scenario. The guide defines no settlement correction semantics for this action.',
  'The receiver is told this is a duplicate of a copy.',
  ['bah-sending-messaging-endpoint','bah-receiving-messaging-endpoint']),
 ('possible-duplicate','Resend when original receipt is uncertain','2.10','19',
  'Recover when the sender suspects that the receiver did not receive the Business Message.',
  'The sender has received no reply because of technical or other problems.',
  [('Sending endpoint','Resends the same Business Message, marks PossibleDuplicate YES, and copies relevant original header elements into Related.','Sending endpoint → receiving endpoint'),
   ('Receiving endpoint','Checks whether the original identified in Related was received.','Decision at receiving endpoint'),
   ('Receiving endpoint','If original was received, ignores this business message; if not received, treats it as the original.','Alternative branches at receiving endpoint')],
  'The received-original and missing-original branches are mutually exclusive. This is application-level resend, not network retransmission (also src-000011 pp5–6 and p15 §2.4.11).',
  'Avoid repeated business processing when the original was already received; otherwise process as original.',
  ['bah-sending-messaging-endpoint','bah-receiving-messaging-endpoint']),
 ('priority','Send with a pre-agreed priority','2.11','20',
  'Indicate processing priority within a previously agreed context.',
  'Priority meaning must be agreed for the service, market or business area.',
  [('Sending endpoint','Supplies Priority and, where needed to remove ambiguity, BusinessService and/or MarketPractice.','Sending endpoint → receiving endpoint')],
  'The guide does not define the meaning of priority values. Do not invent a universal priority ranking.',
  'The receiving application can interpret the indicated priority in the agreed context.',
  ['bah-sending-messaging-endpoint','bah-receiving-messaging-endpoint']),
 ('signed-message','Send a signed Business Message','2.12','21',
  'Send a Business Message containing the sending business entity signature.',
  'Signature must follow the W3C XML Signature specification and additional service, market-practice or business-area constraints.',
  [('Sending endpoint','Includes Signature in the BAH and sends the Business Message.','Sending endpoint → receiving endpoint')],
  'The detailed signing and verification flow is in Annex A, pp28–36. It remains separately subject to complete diagram reconstruction and review.',
  'A signed Business Message is delivered; successful signature validation is not implied merely by presence of the field.',
  ['bah-sending-messaging-endpoint','bah-receiving-messaging-endpoint']),
 ('related-message','Send a new message related to prior messages','2.13','21–23',
  'Expose the underlying business messages that triggered creation of a different business message.',
  'A process uses multiple messages, potentially different definitions, and the recipient needs the underlying context.',
  [('Business application creating the new message','Includes relevant prior BAH details in Related. CopyDuplicate and PossibleDuplicate are not used in this scenario.','Narrative names B as current creator; receiving endpoint is not safely resolved from the inconsistent table'),
   ('Receiving endpoint','Distinguishes the functions of multiple related messages using their MessageDefinitionIdentifier values.','Receives related-message context')],
  'The p22 table repeats From A / To B despite the heading and narrative identifying B as sender of Business Message B. Direction is explicitly unresolved rather than guessed. Source examples include setr.047 relating to prior setr.012 and setr.010, and camt.029 relating to camt.056 and pacs.008.',
  'The receiver can identify underlying messages and distinguish their functions. Related does not itself mean copy, duplicate, cancellation or reversal.',
  ['bah-sending-messaging-endpoint','bah-receiving-messaging-endpoint','bah-business-intermediary'])
]
flowids=['bah-'+v[0] for v in scenarios]
for rid,title,aliases,definition,actions,evidence,ident in roles:
 page='shared/reference/participants/'+rid+'.md'
 roleflows=flowids if rid.startswith('bah-') and rid not in ['bah-business-intermediary','bah-technical-forwarder'] else ['bah-business-message-exchange','bah-related-message'] if rid=='bah-business-intermediary' else ['bah-business-message-exchange'] if rid=='bah-technical-forwarder' else []
 body='## Definition and role scope\n\n'+definition+'\n\n## Responsibilities and actions\n\n'+actions+'\n\n## Identifiers\n\n'+ident+'\n\n## Relationships and applicability\n\n'
 if rid.startswith('bah-'):
  for other in ['bah-sending-messaging-endpoint','bah-receiving-messaging-endpoint','bah-business-intermediary','bah-technical-forwarder']:
   if other!=rid:body+='- '+link(page,'shared/reference/participants/'+other+'.md',other)+'.\n'
  body+='\nThe same real application or institution can occupy different roles in different exchanges. These records are scoped to BAH messaging and do not equate the roles with account owner, account servicer, bank, CSD or market infrastructure.\n\n'
 else:
  other='bfh-system-administrator' if rid=='bfh-system-user' else 'bfh-system-user'
  body+=link(page,'shared/reference/participants/'+other+'.md',other)+'. The supplied BFH context is T2S; equivalence to unrelated roles is not established.\n\n'
 body+='## Flows\n\n'+('\n'.join('- '+link(page,FLOWBASE+'/'+f[4:]+'.md',f) for f in roleflows) if roleflows else 'No separate ordered BFH business flow is defined by the cited SystemUser section.')+'\n\n## Evidence and limitations\n\n'
 body+='\n'.join('- '+src(page,sid,loc)+'.' for sid,loc in evidence)+'\n\nSource labels are scoped aliases, not identity assertions about institutions. Diagram cross-checks and version applicability of MUG scenarios remain needs-review. '+link(page,CONCEPT,'BAH and BFH context')+'.'
 save(page,title,body,document_kind='participant',participant_id=rid,aliases=aliases,source_ids=list(dict.fromkeys(s[0] for s in evidence)),source_locations=[s[1] for s in evidence],domains=['shared'],message_sets=['business-application-header'] if rid.startswith('bah-') else ['t2s-business-file-header'],message_ids=['head.001.001.04'] if rid.startswith('bah-') else ['head.002.001.01'],flows=roleflows,limitations=['Scoped functional role; no institutional equivalence inferred.','Source diagram comparison pending.'])
for ident,title,sec,pages,purpose,pre,steps,branches,outcome,participants in scenarios:
 page=FLOWBASE+'/'+ident+'.md'
 body='## Purpose, trigger and preconditions\n\n'+purpose+'\n\n'+pre+'\n\nEvidence: '+src(page,'src-000012','file/printed pages '+pages+', §'+sec)+'.\n\n## Participants\n\n'
 for rid in participants:body+='- '+link(page,'shared/reference/participants/'+rid+'.md',rid)+'.\n'
 body+='\n## Ordered activities and message direction\n\n| Step | Responsible participant | Activity or decision | Sender / receiver |\n| --- | --- | --- | --- |\n'
 for i,(who,what,direction) in enumerate(steps,1):body+='| '+str(i)+' | '+who+' | '+what+' | '+direction+' |\n'
 body+='\nAll steps derive from '+src(page,'src-000012','§'+sec+', file/printed pages '+pages)+'. The exchanged object is a Business Message with BAH (head.001 family); a particular document-message identifier is not generally specified by this scenario.\n\n## Alternatives and exceptions\n\n'+branches+'\n\n## Outcomes and postconditions\n\n'+outcome+'\n\n## Diagrams and review\n\nThe source diagrams and tables for §'+sec+' are in '+src(page,'src-000012','file/printed pages '+pages)+'. Complete source-figure classification, Mermaid reconstruction and visual comparison remain pending. No diagram-render success is claimed here.\n\nThe MUG is Version 3.0 dated 2021-11-03; its packaging example uses head.001.001.03. The supplied schema is head.001.001.04. These source scenarios are retained as guide-level business context; exact profile applicability to V04 is not silently assumed. '+link(page,CONCEPT,'Header comparison and limitations')+'.\n'
 save(page,title,body,document_kind='business-flow',flow_id='bah-'+ident,source_ids=['src-000012']+(['src-000011'] if ident=='possible-duplicate' else []),source_locations=['MUG §'+sec+', file/printed pages '+pages],source_edition='Version 3.0, 2021-11-03',domains=['shared'],message_sets=['business-application-header'],message_families=['head.001'],message_ids=[],participants=participants,limitations=['MUG-to-exact-schema-version applicability unresolved.','Source diagrams pending reconstruction and visual review.']+(['Sender/receiver inconsistency in source p22 table.'] if ident=='related-message' else []))
page=FLOWBASE+'/index.md'
save(page,'BAH usage scenarios','The guide defines these business scenarios. They share scoped functional participants and preserve the guide edition separately from the supplied V04 schema.\n\n'+'\n'.join('- '+link(page,FLOWBASE+'/'+v[0]+'.md',v[1])+' — §'+v[2]+', pp'+v[3]+'.' for v in scenarios)+'\n\nSource: '+src(page,'src-000012','§2, file/printed pages 7–23')+'.\n',document_kind='flow-index',source_ids=['src-000012'],message_sets=['business-application-header'],limitations=['Source diagram reconstruction and exact-version applicability pending.'])
body='The Business Application Header and Business File Header describe different exchange scopes. They have distinct full identifiers and namespaces and must not share a canonical message definition.\n\n| Aspect | Business Application Header | Business File Header |\n| --- | --- | --- |\n| Supplied definition | head.001.001.04 BusinessApplicationHeaderV04 | head.002.001.01 BusinessFileHeaderV01 |\n| Schema root | AppHdr | Xchg |\n| Scope | A Business Message and its sending/receiving MessagingEndpoints | A file exchange, its content and structure |\n| Core identifier | BusinessMessageIdentifier identifies the Business Message to its creator | PayloadIdentifier identifies the file delivered by the sender |\n| Payload | BAH accompanies the ISO 20022 message; the guide permits different packaging | PayloadDescription describes the exchange; zero or more Payload elements contain exchanged documents |\n| Processing context | BusinessService, MarketPractice, CreationDate, BusinessProcessingDate, copy/duplicate and related-message context | File identifier, creation timestamp, possible-duplicate flag, optional application specifics, payload type and manifest counts |\n| Supplied publication evidence | MDR Version4, March2024; separate MUG Version3.0, 2021-11-03 | MDR June2024, approved 18 June2024, supplied inside T2S archive |\n\nEvidence: '+src(CONCEPT,'src-000011','file/printed pages 4–6 §2.1 and 9–16 §2.4')+'; '+src(CONCEPT,'src-000013','target namespace urn:iso:std:iso:20022:tech:xsd:head.001.001.04, /xs:schema/xs:element[@name=\"AppHdr\"]')+'; '+src(CONCEPT,'src-000349','file/printed pages 3–8 §§1.1,2.1–2.4')+'; '+src(CONCEPT,'src-000261','target namespace urn:iso:std:iso:20022:tech:xsd:head.002.001.01, /xs:schema/xs:element[@name=\"Xchg\"]')+'.\n\n## Business identity and transport identity\n\nA Business Message is the ISO 20022 message plus its BAH. A technical forwarder does not become the BAH business sender or recipient solely by transporting it. If an intermediary actually processes the Business Message, it is recipient of the first message and sender of a different second message. The standard does not prescribe AppHdr/Document order in an envelope; the MUG calls BAH-first common best practice and also permits other packaging. '+src(CONCEPT,'src-000012','file/printed pages 3–5 §§1.3–1.5')+'.\n\n## File-header boundaries and rules\n\nThe supplied June2024 BFH publication states that head.002 is for existing implementations such as the Eurosystem and that new implementations must use the future Business File Envelope nvlp.002. This is the statement of that supplied publication; no nvlp.002 schema or current external status is established here. '+src(CONCEPT,'src-000349','file/printed pages 3–4 §§1.1,2.1')+'.\n\nThe BFH narrative gives absent PossibleDuplicateFlag the business meaning False. The supplied XSD makes the element optional and declares no default attribute. Keep that source-defined business default distinct from XSD validation defaults. The BFH SignatureEnvelope wildcard permits XML Signature namespace content with lax processing, while MDR C1 permits only the Signature root element. The Payload wildcard accepts any namespace with lax processing. '+src(CONCEPT,'src-000349','file/printed page 5 §2.3 C1, page7 §2.4.1.1.3, page8 §2.4.2')+'; '+src(CONCEPT,'src-000261','/xs:schema/xs:complexType[@name=\"PayloadData2\"], SignatureEnvelope and LaxPayload declarations')+'.\n\n## Participant and flow retrieval\n\n'
body+='- '+link(CONCEPT,FLOWBASE+'/index.md','BAH scenario index')+'.\n'
for rid,title,*_ in roles:body+='- '+link(CONCEPT,'shared/reference/participants/'+rid+'.md',title)+'.\n'
body+='\n## Known limitations\n\n- The MUG v3.0 packaging example uses head.001.001.03, while supplied MDR and XSD define head.001.001.04. Guide-level scenarios are not silently treated as an exact V04 implementation profile.\n- MUG §2.13 pp21–22 names B as sender of a newly related Business Message B, but p22 repeats a table with From A / To B. The related-message flow records that inconsistency.\n- Source figures remain subject to complete reconstruction and visual checks. No checks are claimed merely because this comparison is written.\n- '+link(CONCEPT,'tracking/issues.md#issue-000003','Direction issue issue-000003')+' and '+link(CONCEPT,'tracking/issues.md#issue-000004','applicability issue issue-000004')+' records unresolved corpus limitations.\n'
save(CONCEPT,'Business Application Header and Business File Header',body,document_kind='concept',concept_id='bah-versus-business-file-header',source_ids=['src-000011','src-000012','src-000013','src-000261','src-000349'],message_ids=['head.001.001.04','head.002.001.01'],message_families=['head.001','head.002'],message_sets=['business-application-header','t2s-business-file-header'],limitations=['MUG exact-version applicability unresolved.','Source direction inconsistency in MUG §2.13.','Figure review pending.'])
print('Created 6 scoped participants, 12 BAH flow references, 1 flow index and header comparison.')
