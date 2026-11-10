---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000354-executing-party"
title: "Executing Party — T2S CollateralManagementReferenceData narrative scope"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
source_labels: ["executing party"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["t2s-collateral-management-reference-data"]
message_ids: ["reda.024.001.01", "reda.025.001.01", "reda.026.001.01", "reda.027.001.01", "reda.028.001.01", "reda.044.001.01", "reda.075.001.01", "reda.077.001.01"]
message_families: ["reda.024", "reda.025", "reda.026", "reda.027", "reda.028", "reda.044", "reda.075", "reda.077"]
flows: []
source_locations: [{"source_id": "src-000354", "heading": "2 reda.024.001.01 CollateralValueCreationRequestV01", "file_pages": [6], "evidence_id": "src-000354-reda.024.001.01-p6-c001"}, {"source_id": "src-000354", "heading": "3 reda.025.001.01 EligibleSecuritiesCreationRequestV01", "file_pages": [16], "evidence_id": "src-000354-reda.025.001.01-p16-c001"}, {"source_id": "src-000354", "heading": "4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01", "file_pages": [22], "evidence_id": "src-000354-reda.026.001.01-p22-c001"}, {"source_id": "src-000354", "heading": "5 reda.027.001.01 CloseLinkCreationRequestV01", "file_pages": [30], "evidence_id": "src-000354-reda.027.001.01-p30-c001"}, {"source_id": "src-000354", "heading": "6 reda.028.001.01 CollateralDataStatusAdviceV01", "file_pages": [36], "evidence_id": "src-000354-reda.028.001.01-p36-c001"}, {"source_id": "src-000354", "heading": "7 reda.044.001.01 EligibleCounterpartCSDStatusAdviceV01", "file_pages": [46], "evidence_id": "src-000354-reda.044.001.01-p46-c001"}, {"source_id": "src-000354", "heading": "8 reda.075.001.01 EligibleSecuritiesDeletionRequestV01", "file_pages": [51], "evidence_id": "src-000354-reda.075.001.01-p51-c001"}, {"source_id": "src-000354", "heading": "9 reda.077.001.01 CloseLinkDeletionRequestV01", "file_pages": [57], "evidence_id": "src-000354-reda.077.001.01-p57-c001"}]
search_terms: ["executing party"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Executing Party — T2S CollateralManagementReferenceData

## Definition and applicable context

This source names **executing party** in the Functionality of the messages listed below. The record is scoped to T2S CollateralManagementReferenceData, may-2025. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The CollateralValueCreationRequest message is sent by the instructing party to the executing party to request for the creation of a collateral value in the executing system collateral management reference data.

src-000354, file p6, 2 reda.024.001.01 CollateralValueCreationRequestV01, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| receiver | The CollateralValueCreationRequest message | current-message | sender: the instructing party ([the instructing party](participant-src-000353-instructing-party.md)); receiver: the executing party ([the executing party](participant-narrative-src-000354-executing-party.md)) | [src-000354-reda.024.001.01-p6-c001-d1](#src-000354-reda.024.001.01-p6-c001); file p6 |
| exchange_participants | The EligibleSecuritiesCreationRequest message | current-message | exchange_participants: an instructing party and the executing party ([an instructing party](participant-src-000353-instructing-party.md); [the executing party](participant-narrative-src-000354-executing-party.md)) | [src-000354-reda.025.001.01-p16-c001-d1](#src-000354-reda.025.001.01-p16-c001); file p16 |
| receiver | The EligibleCounterpartCSDCreationRequest message | current-message | sender: an instructing party ([an instructing party](participant-src-000353-instructing-party.md)); receiver: the executing party ([the executing party](participant-narrative-src-000354-executing-party.md)) | [src-000354-reda.026.001.01-p22-c001-d1](#src-000354-reda.026.001.01-p22-c001); file p22 |
| receiver | The CloseLinkCreationRequest message | current-message | sender: an instructing party ([an instructing party](participant-src-000353-instructing-party.md)); receiver: the executing party ([the executing party](participant-narrative-src-000354-executing-party.md)) | [src-000354-reda.027.001.01-p30-c001-d1](#src-000354-reda.027.001.01-p30-c001); file p30 |
| sender | The CollateralDataStatusAdvice message | current-message | sender: the executing party ([the executing party](participant-narrative-src-000354-executing-party.md)); receiver: an instructing party (the requestor) ([an instructing party](participant-src-000353-instructing-party.md)) | [src-000354-reda.028.001.01-p36-c001-d1](#src-000354-reda.028.001.01-p36-c001); file p36 |
| sender | The EligibleCounterpartCSDStatusAdvice message | current-message | sender: the executing party ([the executing party](participant-narrative-src-000354-executing-party.md)); receiver: an instructing party (the requestor) ([an instructing party](participant-src-000353-instructing-party.md)) | [src-000354-reda.044.001.01-p46-c001-d1](#src-000354-reda.044.001.01-p46-c001); file p46 |
| exchange_participants | The EligibleSecuritiesDeletionRequest message | current-message | exchange_participants: an instructing party and the executing party ([an instructing party](participant-src-000353-instructing-party.md); [the executing party](participant-narrative-src-000354-executing-party.md)) | [src-000354-reda.075.001.01-p51-c001-d1](#src-000354-reda.075.001.01-p51-c001); file p51 |
| receiver | The CloseLinkDeletionRequest message | current-message | sender: an instructing party ([an instructing party](participant-src-000353-instructing-party.md)); receiver: the executing party ([the executing party](participant-narrative-src-000354-executing-party.md)) | [src-000354-reda.077.001.01-p57-c001-d1](#src-000354-reda.077.001.01-p57-c001); file p57 |


## Complete source evidence

<a id="src-000354-reda.024.001.01-p6-c001"></a>

### src-000354-reda.024.001.01-p6-c001

src-000354; file p6; 2 reda.024.001.01 CollateralValueCreationRequestV01; scope.

> The CollateralValueCreationRequest message is sent by the instructing party to the executing party to request for the creation of a collateral value in the executing system collateral management reference data.

<a id="src-000354-reda.025.001.01-p16-c001"></a>

### src-000354-reda.025.001.01-p16-c001

src-000354; file p16; 3 reda.025.001.01 EligibleSecuritiesCreationRequestV01; scope.

> The EligibleSecuritiesCreationRequest message is exchanged between an instructing party and the executing party to request for the creation of an eligible securities in the executing system collateral management reference data.

<a id="src-000354-reda.026.001.01-p22-c001"></a>

### src-000354-reda.026.001.01-p22-c001

src-000354; file p22; 4 reda.026.001.01 EligibleCounterpartCSDCreationRequestV01; scope.

> The EligibleCounterpartCSDCreationRequest message is sent by an instructing party to the executing party to request for the creation of an eligible counterpart CSD in the executing system collateral management reference data.

<a id="src-000354-reda.027.001.01-p30-c001"></a>

### src-000354-reda.027.001.01-p30-c001

src-000354; file p30; 5 reda.027.001.01 CloseLinkCreationRequestV01; scope.

> The CloseLinkCreationRequest message is sent by an instructing party to the executing party to request for the creation of a close link in the executing system collateral management reference data.

<a id="src-000354-reda.028.001.01-p36-c001"></a>

### src-000354-reda.028.001.01-p36-c001

src-000354; file p36; 6 reda.028.001.01 CollateralDataStatusAdviceV01; scope.

> The CollateralDataStatusAdvice message is sent by the executing party to an instructing party (the requestor) to provide information of a request on collateral management reference data.

<a id="src-000354-reda.044.001.01-p46-c001"></a>

### src-000354-reda.044.001.01-p46-c001

src-000354; file p46; 7 reda.044.001.01 EligibleCounterpartCSDStatusAdviceV01; scope.

> The EligibleCounterpartCSDStatusAdvice message is sent by the executing party to an instructing party (the requestor) to provide information for a request on eligible counterpart CSD reference data.

<a id="src-000354-reda.075.001.01-p51-c001"></a>

### src-000354-reda.075.001.01-p51-c001

src-000354; file p51; 8 reda.075.001.01 EligibleSecuritiesDeletionRequestV01; scope.

> The EligibleSecuritiesDeletionRequest message is exchanged between an instructing party and the executing party to request for the deletion of an eligible securities in the executing system collateral management reference data.

<a id="src-000354-reda.077.001.01-p57-c001"></a>

### src-000354-reda.077.001.01-p57-c001

src-000354; file p57; 9 reda.077.001.01 CloseLinkDeletionRequestV01; scope.

> The CloseLinkDeletionRequest message is sent by an instructing party to the executing party to request for the deletion of a close link in the executing system collateral management reference data.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| reda.024.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.024.001.01/roles.md) | src-000354-reda.024.001.01-p6-c001 |
| reda.025.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.025.001.01/roles.md) | src-000354-reda.025.001.01-p16-c001 |
| reda.026.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.026.001.01/roles.md) | src-000354-reda.026.001.01-p22-c001 |
| reda.027.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.027.001.01/roles.md) | src-000354-reda.027.001.01-p30-c001 |
| reda.028.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.028.001.01/roles.md) | src-000354-reda.028.001.01-p36-c001 |
| reda.044.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.044.001.01/roles.md) | src-000354-reda.044.001.01-p46-c001 |
| reda.075.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.075.001.01/roles.md) | src-000354-reda.075.001.01-p51-c001 |
| reda.077.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.077.001.01/roles.md) | src-000354-reda.077.001.01-p57-c001 |


[Message-set flows](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `executing party`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000354](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf` · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
