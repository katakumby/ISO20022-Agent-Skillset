---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000369-executing-party"
title: "Executing Party — T2S PartyReferenceData narrative scope"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
source_labels: ["executing party"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["t2s-party-reference-data"]
message_ids: ["reda.014.001.02", "reda.015.001.01", "reda.016.001.01", "reda.017.001.02", "reda.022.001.02", "reda.031.001.01", "reda.041.001.02", "reda.042.001.01", "reda.043.001.02"]
message_families: ["reda.014", "reda.015", "reda.016", "reda.017", "reda.022", "reda.031", "reda.041", "reda.042", "reda.043"]
flows: []
source_locations: [{"source_id": "src-000369", "heading": "2 reda.014.001.02 PartyCreationRequestV02", "file_pages": [6], "evidence_id": "src-000369-reda.014.001.02-p6-c001"}, {"source_id": "src-000369", "heading": "3 reda.015.001.01 PartyQueryV01", "file_pages": [18], "evidence_id": "src-000369-reda.015.001.01-p18-c001"}, {"source_id": "src-000369", "heading": "4 reda.016.001.01 PartyStatusAdviceV01", "file_pages": [35], "evidence_id": "src-000369-reda.016.001.01-p35-c001"}, {"source_id": "src-000369", "heading": "5 reda.017.001.02 PartyReportV02", "file_pages": [41], "evidence_id": "src-000369-reda.017.001.02-p41-c001"}, {"source_id": "src-000369", "heading": "6 reda.022.001.02 PartyModificationRequestV02", "file_pages": [61], "evidence_id": "src-000369-reda.022.001.02-p61-c001"}, {"source_id": "src-000369", "heading": "7 reda.031.001.01 PartyDeletionRequestV01", "file_pages": [76], "evidence_id": "src-000369-reda.031.001.01-p76-c001"}, {"source_id": "src-000369", "heading": "8 reda.041.001.02 PartyActivityAdviceV02", "file_pages": [79], "evidence_id": "src-000369-reda.041.001.02-p79-c001"}, {"source_id": "src-000369", "heading": "9 reda.042.001.01 PartyAuditTrailQueryV01", "file_pages": [111], "evidence_id": "src-000369-reda.042.001.01-p111-c001"}, {"source_id": "src-000369", "heading": "10 reda.043.001.02 PartyAuditTrailReportV02", "file_pages": [115], "evidence_id": "src-000369-reda.043.001.02-p115-c001"}]
search_terms: ["executing party"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Executing Party — T2S PartyReferenceData

## Definition and applicable context

This source names **executing party** in the Functionality of the messages listed below. The record is scoped to T2S PartyReferenceData, march-2024. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The PartyCreationRequest message is sent by an instructing party to the executing party to request for the creation of party reference data for a new party in the executing system.

src-000369, file p6, 2 reda.014.001.02 PartyCreationRequestV02, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| receiver | The PartyCreationRequest message | current-message | sender: an instructing party ([an instructing party](participant-src-000368-instructing-party.md)); receiver: the executing party ([the executing party](participant-narrative-src-000369-executing-party.md)) | [src-000369-reda.014.001.02-p6-c001-d1](#src-000369-reda.014.001.02-p6-c001); file p6 |
| receiver | The PartyQuery message | current-message | sender: a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange ([a central securities depository](participant-narrative-src-000369-central-securities-depository.md); [a central securities depository participant](participant-narrative-src-000369-central-securities-depository-participant.md); [a central counter party](participant-narrative-src-000369-central-counter-party.md); [a stock exchange](participant-narrative-src-000369-stock-exchange.md)); receiver: the executing party ([the executing party](participant-narrative-src-000369-executing-party.md)) | [src-000369-reda.015.001.01-p18-c001-d1](#src-000369-reda.015.001.01-p18-c001); file p18 |
| sender | The PartyStatusAdvice message | current-message | sender: the executing party ([the executing party](participant-narrative-src-000369-executing-party.md)); receiver: the instructing party ([the instructing party](participant-src-000368-instructing-party.md)) | [src-000369-reda.016.001.01-p35-c001-d1](#src-000369-reda.016.001.01-p35-c001); file p35 |
| sender | The PartyReport message | current-message | sender: the executing party ([the executing party](participant-narrative-src-000369-executing-party.md)); receiver: a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange ([a central securities depository](participant-narrative-src-000369-central-securities-depository.md); [a central securities depository participant](participant-narrative-src-000369-central-securities-depository-participant.md); [a central counter party](participant-narrative-src-000369-central-counter-party.md); [a stock exchange](participant-narrative-src-000369-stock-exchange.md)) | [src-000369-reda.017.001.02-p41-c001-d1](#src-000369-reda.017.001.02-p41-c001); file p41 |
| receiver | The PartyModificationRequest message | current-message | sender: the instructing party ([the instructing party](participant-src-000368-instructing-party.md)); receiver: the executing party ([the executing party](participant-narrative-src-000369-executing-party.md)) | [src-000369-reda.022.001.02-p61-c001-d1](#src-000369-reda.022.001.02-p61-c001); file p61 |
| receiver | The PartyDeletionRequest message | current-message | sender: the instructing party ([the instructing party](participant-src-000368-instructing-party.md)); receiver: the executing party ([the executing party](participant-narrative-src-000369-executing-party.md)) | [src-000369-reda.031.001.01-p76-c001-d1](#src-000369-reda.031.001.01-p76-c001); file p76 |
| sender | The PartyActivityReport message | current-message-scope-name-variant | sender: the executing party ([the executing party](participant-narrative-src-000369-executing-party.md)); receiver: an instructing party ([an instructing party](participant-src-000368-instructing-party.md)) | [src-000369-reda.041.001.02-p79-c001-d1](#src-000369-reda.041.001.02-p79-c001); file p79 |
| receiver | The PartyAuditTrailQuery message | current-message | sender: an instructing party ([an instructing party](participant-src-000368-instructing-party.md)); receiver: the executing party ([the executing party](participant-narrative-src-000369-executing-party.md)) | [src-000369-reda.042.001.01-p111-c001-d1](#src-000369-reda.042.001.01-p111-c001); file p111 |
| sender | The PartyAuditTrailReport message | current-message | sender: the executing party ([the executing party](participant-narrative-src-000369-executing-party.md)); receiver: an instructing party ([an instructing party](participant-src-000368-instructing-party.md)) | [src-000369-reda.043.001.02-p115-c001-d1](#src-000369-reda.043.001.02-p115-c001); file p115 |


## Complete source evidence

<a id="src-000369-reda.014.001.02-p6-c001"></a>

### src-000369-reda.014.001.02-p6-c001

src-000369; file p6; 2 reda.014.001.02 PartyCreationRequestV02; scope.

> The PartyCreationRequest message is sent by an instructing party to the executing party to request for the creation of party reference data for a new party in the executing system.

<a id="src-000369-reda.015.001.01-p18-c001"></a>

### src-000369-reda.015.001.01-p18-c001

src-000369; file p18; 3 reda.015.001.01 PartyQueryV01; scope.

> The PartyQuery message is sent by a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange to the executing party to query for the party reference data of a party defined in the system.

<a id="src-000369-reda.016.001.01-p35-c001"></a>

### src-000369-reda.016.001.01-p35-c001

src-000369; file p35; 4 reda.016.001.01 PartyStatusAdviceV01; scope.

> The PartyStatusAdvice message is sent by the executing party to the instructing party to provide details about the processing of a request on party reference data (create or update).

<a id="src-000369-reda.017.001.02-p41-c001"></a>

### src-000369-reda.017.001.02-p41-c001

src-000369; file p41; 5 reda.017.001.02 PartyReportV02; scope.

> The PartyReport message is sent by the executing party to a central securities depository, a national central bank, a central securities depository participant, a central counter party, a payment bank, a trading party or a stock exchange to provide detailed information on the requested party reference data of the party defined in the system.

<a id="src-000369-reda.022.001.02-p61-c001"></a>

### src-000369-reda.022.001.02-p61-c001

src-000369; file p61; 6 reda.022.001.02 PartyModificationRequestV02; scope.

> The PartyModificationRequest message is sent by the instructing party to the executing party to request for an update of the party reference data of a party defined in the executing system.

<a id="src-000369-reda.031.001.01-p76-c001"></a>

### src-000369-reda.031.001.01-p76-c001

src-000369; file p76; 7 reda.031.001.01 PartyDeletionRequestV01; scope.

> The PartyDeletionRequest message is sent by the instructing party to the executing party to request a deletion of a party defined in the executing system.

<a id="src-000369-reda.041.001.02-p79-c001"></a>

### src-000369-reda.041.001.02-p79-c001

src-000369; file p79; 8 reda.041.001.02 PartyActivityAdviceV02; scope.

> The PartyActivityReport message is sent by the executing party to an instructing party containing information about changes on party reference data.

<a id="src-000369-reda.042.001.01-p111-c001"></a>

### src-000369-reda.042.001.01-p111-c001

src-000369; file p111; 9 reda.042.001.01 PartyAuditTrailQueryV01; scope.

> The PartyAuditTrailQuery message is sent by an instructing party to the executing party to query for the party audit trail recorded in the system.

<a id="src-000369-reda.043.001.02-p115-c001"></a>

### src-000369-reda.043.001.02-p115-c001

src-000369; file p115; 10 reda.043.001.02 PartyAuditTrailReportV02; scope.

> The PartyAuditTrailReport message is sent by the executing party to an instructing party to provide detailed information on the requested party audit trail recorded in the system.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| reda.014.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.014.001.02/roles.md) | src-000369-reda.014.001.02-p6-c001 |
| reda.015.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.015.001.01/roles.md) | src-000369-reda.015.001.01-p18-c001 |
| reda.016.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.016.001.01/roles.md) | src-000369-reda.016.001.01-p35-c001 |
| reda.017.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.017.001.02/roles.md) | src-000369-reda.017.001.02-p41-c001 |
| reda.022.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.022.001.02/roles.md) | src-000369-reda.022.001.02-p61-c001 |
| reda.031.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.031.001.01/roles.md) | src-000369-reda.031.001.01-p76-c001 |
| reda.041.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.041.001.02/roles.md) | src-000369-reda.041.001.02-p79-c001 |
| reda.042.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.042.001.01/roles.md) | src-000369-reda.042.001.01-p111-c001 |
| reda.043.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.043.001.02/roles.md) | src-000369-reda.043.001.02-p115-c001 |


[Message-set flows](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `executing party`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000369](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf` · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
