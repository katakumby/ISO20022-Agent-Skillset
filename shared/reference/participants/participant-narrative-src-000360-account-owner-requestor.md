---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000360-account-owner-requestor"
title: "Account Owner/Requestor — T2S IntraBalanceMovement narrative scope"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
source_labels: ["account owner/requestor"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["t2s-intra-balance-movement"]
message_ids: ["camt.066.001.02", "camt.067.001.02", "camt.068.001.02", "camt.072.001.02", "camt.073.001.02", "camt.074.001.02", "camt.075.001.02", "camt.078.001.02", "camt.079.001.02", "camt.080.001.02", "camt.081.001.02", "camt.082.001.02", "camt.083.001.02", "camt.084.001.02"]
message_families: ["camt.066", "camt.067", "camt.068", "camt.072", "camt.073", "camt.074", "camt.075", "camt.078", "camt.079", "camt.080", "camt.081", "camt.082", "camt.083", "camt.084"]
flows: []
source_locations: [{"source_id": "src-000360", "heading": "2 camt.066.001.02 IntraBalanceMovementInstructionV02", "file_pages": [10], "evidence_id": "src-000360-camt.066.001.02-p10-c001"}, {"source_id": "src-000360", "heading": "3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02", "file_pages": [31], "evidence_id": "src-000360-camt.067.001.02-p31-c001"}, {"source_id": "src-000360", "heading": "4 camt.068.001.02 IntraBalanceMovementConfirmationV02", "file_pages": [50], "evidence_id": "src-000360-camt.068.001.02-p50-c001"}, {"source_id": "src-000360", "heading": "5 camt.072.001.02 IntraBalanceMovementModificationRequestV02", "file_pages": [66], "evidence_id": "src-000360-camt.072.001.02-p66-c001"}, {"source_id": "src-000360", "heading": "6 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02", "file_pages": [90], "evidence_id": "src-000360-camt.073.001.02-p90-c001"}, {"source_id": "src-000360", "heading": "7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02", "file_pages": [115], "evidence_id": "src-000360-camt.074.001.02-p115-c001"}, {"source_id": "src-000360", "heading": "8 camt.075.001.02 IntraBalanceMovementCancellationRequestStatusAdviceV02", "file_pages": [132], "evidence_id": "src-000360-camt.075.001.02-p132-c001"}, {"source_id": "src-000360", "heading": "9 camt.078.001.02 IntraBalanceMovementQueryV02", "file_pages": [150], "evidence_id": "src-000360-camt.078.001.02-p150-c001"}, {"source_id": "src-000360", "heading": "10 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "file_pages": [190], "evidence_id": "src-000360-camt.079.001.02-p190-c001"}, {"source_id": "src-000360", "heading": "11 camt.080.001.02 IntraBalanceMovementModificationQueryV02", "file_pages": [232], "evidence_id": "src-000360-camt.080.001.02-p232-c001"}, {"source_id": "src-000360", "heading": "12 camt.081.001.02 IntraBalanceMovementModificationReportV02", "file_pages": [245], "evidence_id": "src-000360-camt.081.001.02-p245-c001"}, {"source_id": "src-000360", "heading": "13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02", "file_pages": [286], "evidence_id": "src-000360-camt.082.001.02-p286-c001"}, {"source_id": "src-000360", "heading": "14 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "file_pages": [300], "evidence_id": "src-000360-camt.083.001.02-p300-c001"}, {"source_id": "src-000360", "heading": "15 camt.084.001.02 IntraBalanceMovementPostingReportV02", "file_pages": [331], "evidence_id": "src-000360-camt.084.001.02-p331-c001"}]
search_terms: ["account owner/requestor"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Account Owner/Requestor — T2S IntraBalanceMovement

## Definition and applicable context

This source names **account owner/requestor** in the Functionality of the messages listed below. The record is scoped to T2S IntraBalanceMovement, march-2024. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The IntraBalanceMovementInstruction message is sent from an account owner/requestor to a settlement infrastructure to instruct the movement of an amount of money within its holdings from one sub-balance to another.

src-000360, file p10, 2 camt.066.001.02 IntraBalanceMovementInstructionV02, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| sender | The IntraBalanceMovementInstruction message | current-message | sender: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000360-account-owner-requestor.md)); receiver: a settlement infrastructure ([a settlement infrastructure](participant-src-000359-settlement-infrastructure.md)) | [src-000360-camt.066.001.02-p10-c001-d1](#src-000360-camt.066.001.02-p10-c001); file p10 |
| receiver | The IntraBalanceMovementStatusAdvice message | current-message | sender: a settlement infrastructure ([a settlement infrastructure](participant-src-000359-settlement-infrastructure.md)); receiver: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000360-account-owner-requestor.md)) | [src-000360-camt.067.001.02-p31-c001-d1](#src-000360-camt.067.001.02-p31-c001); file p31 |
| receiver | The IntraBalanceMovementConfirmation message | current-message | sender: a settlement infrastructure ([a settlement infrastructure](participant-src-000359-settlement-infrastructure.md)); receiver: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000360-account-owner-requestor.md)) | [src-000360-camt.068.001.02-p50-c001-d1](#src-000360-camt.068.001.02-p50-c001); file p50 |
| sender | The IntraBalanceMovementModificationRequest message | current-message | sender: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000360-account-owner-requestor.md)); receiver: a settlement infrastructure ([a settlement infrastructure](participant-src-000359-settlement-infrastructure.md)) | [src-000360-camt.072.001.02-p66-c001-d1](#src-000360-camt.072.001.02-p66-c001); file p66 |
| receiver | The IntraBalanceMovementModificationRequestStatusAdvice message | current-message | sender: a settlement infrastructure ([a settlement infrastructure](participant-src-000359-settlement-infrastructure.md)); receiver: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000360-account-owner-requestor.md)) | [src-000360-camt.073.001.02-p90-c001-d1](#src-000360-camt.073.001.02-p90-c001); file p90 |
| sender | The IntraBalanceMovementCancellationRequest message | current-message | sender: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000360-account-owner-requestor.md)); receiver: a settlement infrastructure ([a settlement infrastructure](participant-src-000359-settlement-infrastructure.md)) | [src-000360-camt.074.001.02-p115-c001-d1](#src-000360-camt.074.001.02-p115-c001); file p115 |
| receiver | The IntraBalanceMovementCancellationRequestStatusAdvice message | current-message | sender: a settlement infrastructure ([a settlement infrastructure](participant-src-000359-settlement-infrastructure.md)); receiver: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000360-account-owner-requestor.md)) | [src-000360-camt.075.001.02-p132-c001-d1](#src-000360-camt.075.001.02-p132-c001); file p132 |
| sender | The IntraBalanceMovementQuery message | current-message | sender: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000360-account-owner-requestor.md)); receiver: a settlement infrastructure ([a settlement infrastructure](participant-src-000359-settlement-infrastructure.md)) | [src-000360-camt.078.001.02-p150-c001-d1](#src-000360-camt.078.001.02-p150-c001); file p150 |
| receiver | The IntraBalanceMovementQueryResponse message | current-message | sender: a settlement infrastructure ([a settlement infrastructure](participant-src-000359-settlement-infrastructure.md)); receiver: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000360-account-owner-requestor.md)) | [src-000360-camt.079.001.02-p190-c001-d1](#src-000360-camt.079.001.02-p190-c001); file p190 |
| sender | The IntraBalanceMovementModificationQuery message | current-message | sender: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000360-account-owner-requestor.md)); receiver: a settlement infrastructure ([a settlement infrastructure](participant-src-000359-settlement-infrastructure.md)) | [src-000360-camt.080.001.02-p232-c001-d1](#src-000360-camt.080.001.02-p232-c001); file p232 |
| receiver | The IntraBalanceMovementModificationReport message | current-message | sender: a settlement infrastructure ([a settlement infrastructure](participant-src-000359-settlement-infrastructure.md)); receiver: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000360-account-owner-requestor.md)) | [src-000360-camt.081.001.02-p245-c001-d1](#src-000360-camt.081.001.02-p245-c001); file p245 |
| sender | The IntraBalanceMovementCancellationQuery message | current-message | sender: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000360-account-owner-requestor.md)); receiver: a settlement infrastructure ([a settlement infrastructure](participant-src-000359-settlement-infrastructure.md)) | [src-000360-camt.082.001.02-p286-c001-d1](#src-000360-camt.082.001.02-p286-c001); file p286 |
| receiver | The IntraBalanceMovementCancellationReport message | current-message | sender: a settlement infrastructure ([a settlement infrastructure](participant-src-000359-settlement-infrastructure.md)); receiver: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000360-account-owner-requestor.md)) | [src-000360-camt.083.001.02-p300-c001-d1](#src-000360-camt.083.001.02-p300-c001); file p300 |
| receiver | This IntraBalanceMovementPostingReport message | current-message | sender: a settlement infrastructure ([a settlement infrastructure](participant-src-000359-settlement-infrastructure.md)); receiver: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000360-account-owner-requestor.md)) | [src-000360-camt.084.001.02-p331-c001-d1](#src-000360-camt.084.001.02-p331-c001); file p331 |


## Complete source evidence

<a id="src-000360-camt.066.001.02-p10-c001"></a>

### src-000360-camt.066.001.02-p10-c001

src-000360; file p10; 2 camt.066.001.02 IntraBalanceMovementInstructionV02; scope.

> The IntraBalanceMovementInstruction message is sent from an account owner/requestor to a settlement infrastructure to instruct the movement of an amount of money within its holdings from one sub-balance to another.

<a id="src-000360-camt.067.001.02-p31-c001"></a>

### src-000360-camt.067.001.02-p31-c001

src-000360; file p31; 3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02; scope.

> The IntraBalanceMovementStatusAdvice message is sent from a settlement infrastructure to an account owner/requestor to advise the status of an intra-balance movement instruction previously sent by the account owner/requestor.

<a id="src-000360-camt.068.001.02-p50-c001"></a>

### src-000360-camt.068.001.02-p50-c001

src-000360; file p50; 4 camt.068.001.02 IntraBalanceMovementConfirmationV02; scope.

> The IntraBalanceMovementConfirmation message is sent from a settlement infrastructure to an account owner/requestor to confirm the movement of an amount of money within its holdings from one sub- balance to another.

<a id="src-000360-camt.072.001.02-p66-c001"></a>

### src-000360-camt.072.001.02-p66-c001

src-000360; file p66; 5 camt.072.001.02 IntraBalanceMovementModificationRequestV02; scope.

> The IntraBalanceMovementModificationRequest message is sent from an account owner/requestor to a settlement infrastructure to request the modification of a processing indicator on a previously sent IntraBalanceMovementInstruction message.

<a id="src-000360-camt.073.001.02-p90-c001"></a>

### src-000360-camt.073.001.02-p90-c001

src-000360; file p90; 6 camt.073.001.02 IntraBalanceMovementModificationRequestStatusAdviceV02; scope.

> The IntraBalanceMovementModificationRequestStatusAdvice message is sent from a settlement infrastructure to an account owner/requestor to advise the status of an intra-balance movement modification request previously sent by the account owner/requestor.

<a id="src-000360-camt.074.001.02-p115-c001"></a>

### src-000360-camt.074.001.02-p115-c001

src-000360; file p115; 7 camt.074.001.02 IntraBalanceMovementCancellationRequestV02; scope.

> The IntraBalanceMovementCancellationRequest message is sent from an account owner/requestor to a settlement infrastructure to request the cancellation of a previously sent IntraBalanceMovementInstruction message.

<a id="src-000360-camt.075.001.02-p132-c001"></a>

### src-000360-camt.075.001.02-p132-c001

src-000360; file p132; 8 camt.075.001.02 IntraBalanceMovementCancellationRequestStatusAdviceV02; scope.

> The IntraBalanceMovementCancellationRequestStatusAdvice message is sent from a settlement infrastructure to an account owner/requestor to advise the status of an intra-balance movement cancellation request previously sent by the account owner/requestor.

<a id="src-000360-camt.078.001.02-p150-c001"></a>

### src-000360-camt.078.001.02-p150-c001

src-000360; file p150; 9 camt.078.001.02 IntraBalanceMovementQueryV02; scope.

> The IntraBalanceMovementQuery message is sent from an account owner/requestor to a settlement infrastructure to query intra-balance movement instructions, along with their current status, based on a set of search criteria.

<a id="src-000360-camt.079.001.02-p190-c001"></a>

### src-000360-camt.079.001.02-p190-c001

src-000360; file p190; 10 camt.079.001.02 IntraBalanceMovementQueryResponseV02; scope.

> The IntraBalanceMovementQueryResponse message is sent from a settlement infrastructure to an account owner/requestor to provide all intra-balance movement instructions satisfying the selection criteria, as defined within the query, returning current attributes and latest status.

<a id="src-000360-camt.080.001.02-p232-c001"></a>

### src-000360-camt.080.001.02-p232-c001

src-000360; file p232; 11 camt.080.001.02 IntraBalanceMovementModificationQueryV02; scope.

> The IntraBalanceMovementModificationQuery message is sent from an account owner/requestor to a settlement infrastructure to query for the status of intra-balance movement modification instruction(s) based on a set of search criteria or business attributes.

<a id="src-000360-camt.081.001.02-p245-c001"></a>

### src-000360-camt.081.001.02-p245-c001

src-000360; file p245; 12 camt.081.001.02 IntraBalanceMovementModificationReportV02; scope.

> The IntraBalanceMovementModificationReport message is sent from a settlement infrastructure to an account owner/requestor to provide full details or current status values of the intra-balance movement modification request(s), as defined within the query.

<a id="src-000360-camt.082.001.02-p286-c001"></a>

### src-000360-camt.082.001.02-p286-c001

src-000360; file p286; 13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02; scope.

> The IntraBalanceMovementCancellationQuery message is sent from an account owner/requestor to a settlement infrastructure to query for the status of intra-balance movement cancellation instruction(s) based on a set of search criteria or business attributes.

<a id="src-000360-camt.083.001.02-p300-c001"></a>

### src-000360-camt.083.001.02-p300-c001

src-000360; file p300; 14 camt.083.001.02 IntraBalanceMovementCancellationReportV02; scope.

> The IntraBalanceMovementCancellationReport message is sent from a settlement infrastructure to an account owner/requestor to provide full details or current status values of the intra-balance movement cancellation request(s), as defined within the query.

<a id="src-000360-camt.084.001.02-p331-c001"></a>

### src-000360-camt.084.001.02-p331-c001

src-000360; file p331; 15 camt.084.001.02 IntraBalanceMovementPostingReportV02; scope.

> This IntraBalanceMovementPostingReport message is sent from a settlement infrastructure to an account owner/requestor to report the intra-balance movement instructions, previously sent by the account owner, that have a settled status.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| camt.066.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.066.001.02/roles.md) | src-000360-camt.066.001.02-p10-c001 |
| camt.067.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.067.001.02/roles.md) | src-000360-camt.067.001.02-p31-c001 |
| camt.068.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.068.001.02/roles.md) | src-000360-camt.068.001.02-p50-c001 |
| camt.072.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.072.001.02/roles.md) | src-000360-camt.072.001.02-p66-c001 |
| camt.073.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.073.001.02/roles.md) | src-000360-camt.073.001.02-p90-c001 |
| camt.074.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.074.001.02/roles.md) | src-000360-camt.074.001.02-p115-c001 |
| camt.075.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.075.001.02/roles.md) | src-000360-camt.075.001.02-p132-c001 |
| camt.078.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.078.001.02/roles.md) | src-000360-camt.078.001.02-p150-c001 |
| camt.079.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.079.001.02/roles.md) | src-000360-camt.079.001.02-p190-c001 |
| camt.080.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.080.001.02/roles.md) | src-000360-camt.080.001.02-p232-c001 |
| camt.081.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.081.001.02/roles.md) | src-000360-camt.081.001.02-p245-c001 |
| camt.082.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.082.001.02/roles.md) | src-000360-camt.082.001.02-p286-c001 |
| camt.083.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.083.001.02/roles.md) | src-000360-camt.083.001.02-p300-c001 |
| camt.084.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/camt.084.001.02/roles.md) | src-000360-camt.084.001.02-p331-c001 |


[Message-set flows](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `account owner/requestor`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000360](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf` · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
