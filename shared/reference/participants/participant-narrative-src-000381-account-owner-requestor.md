---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000381-account-owner-requestor"
title: "Account Owner/Requestor — T2S SettlementRestrictions narrative scope"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
source_labels: ["account owner/requestor"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["t2s-settlement-restrictions"]
message_ids: ["semt.028.001.01", "semt.029.001.01", "semt.031.001.01", "semt.033.001.01"]
message_families: ["semt.028", "semt.029", "semt.031", "semt.033"]
flows: []
source_locations: [{"source_id": "src-000381", "heading": "2 semt.028.001.01 IntraPositionMovementQueryV01", "file_pages": [7], "evidence_id": "src-000381-semt.028.001.01-p7-c001"}, {"source_id": "src-000381", "heading": "3 semt.029.001.01 IntraPositionMovementQueryResponseV01", "file_pages": [57], "evidence_id": "src-000381-semt.029.001.01-p57-c001"}, {"source_id": "src-000381", "heading": "5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "file_pages": [97], "evidence_id": "src-000381-semt.031.001.01-p97-c001"}, {"source_id": "src-000381", "heading": "7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "file_pages": [145], "evidence_id": "src-000381-semt.033.001.01-p145-c001"}]
search_terms: ["account owner/requestor"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Account Owner/Requestor — T2S SettlementRestrictions

## Definition and applicable context

This source names **account owner/requestor** in the Functionality of the messages listed below. The record is scoped to T2S SettlementRestrictions, september-2025. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The IntraPositionMovementQuery message is sent from an account owner/requestor to a settlement infrastructure to query intra-position movement instructions, along with their current status, based on a set of search criteria.

src-000381, file p7, 2 semt.028.001.01 IntraPositionMovementQueryV01, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| sender | The IntraPositionMovementQuery message | current-message | sender: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000381-account-owner-requestor.md)); receiver: a settlement infrastructure ([a settlement infrastructure](participant-src-000380-settlement-infrastructure.md)) | [src-000381-semt.028.001.01-p7-c001-d1](#src-000381-semt.028.001.01-p7-c001); file p7 |
| receiver | The IntraPositionMovementQueryResponse message | current-message | sender: a settlement infrastructure ([a settlement infrastructure](participant-src-000380-settlement-infrastructure.md)); receiver: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000381-account-owner-requestor.md)) | [src-000381-semt.029.001.01-p57-c001-d1](#src-000381-semt.029.001.01-p57-c001); file p57 |
| receiver | The SecuritiesSettlementConditionsModificationRequestReport message | current-message | sender: a settlement infrastructure ([a settlement infrastructure](participant-src-000380-settlement-infrastructure.md)); receiver: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000381-account-owner-requestor.md)) | [src-000381-semt.031.001.01-p97-c001-d1](#src-000381-semt.031.001.01-p97-c001); file p97 |
| receiver | The SecuritiesTransactionCancellationRequestReport message | current-message | sender: a settlement infrastructure ([a settlement infrastructure](participant-src-000380-settlement-infrastructure.md)); receiver: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000381-account-owner-requestor.md)) | [src-000381-semt.033.001.01-p145-c001-d1](#src-000381-semt.033.001.01-p145-c001); file p145 |


## Complete source evidence

<a id="src-000381-semt.028.001.01-p7-c001"></a>

### src-000381-semt.028.001.01-p7-c001

src-000381; file p7; 2 semt.028.001.01 IntraPositionMovementQueryV01; scope.

> The IntraPositionMovementQuery message is sent from an account owner/requestor to a settlement infrastructure to query intra-position movement instructions, along with their current status, based on a set of search criteria.

<a id="src-000381-semt.029.001.01-p57-c001"></a>

### src-000381-semt.029.001.01-p57-c001

src-000381; file p57; 3 semt.029.001.01 IntraPositionMovementQueryResponseV01; scope.

> The IntraPositionMovementQueryResponse message is sent from a settlement infrastructure to an account owner/requestor to provide all intra-position movement instructions satisfying the selection criteria, as defined within the query, returning current attributes and latest status.

<a id="src-000381-semt.031.001.01-p97-c001"></a>

### src-000381-semt.031.001.01-p97-c001

src-000381; file p97; 5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01; scope.

> The SecuritiesSettlementConditionsModificationRequestReport message is sent from a settlement infrastructure to an account owner/requestor to provide full details or current status values of the settlement or intra-position movement modification request(s), as defined within the query.

<a id="src-000381-semt.033.001.01-p145-c001"></a>

### src-000381-semt.033.001.01-p145-c001

src-000381; file p145; 7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01; scope.

> The SecuritiesTransactionCancellationRequestReport message is sent from a settlement infrastructure to an account owner/requestor to provide full details or current status values of settlement or the intra- position movement cancellation request(s), as defined within the query.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| semt.028.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.028.001.01/roles.md) | src-000381-semt.028.001.01-p7-c001 |
| semt.029.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.029.001.01/roles.md) | src-000381-semt.029.001.01-p57-c001 |
| semt.031.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.031.001.01/roles.md) | src-000381-semt.031.001.01-p97-c001 |
| semt.033.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.033.001.01/roles.md) | src-000381-semt.033.001.01-p145-c001 |


[Message-set flows](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `account owner/requestor`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000381](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf` · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
