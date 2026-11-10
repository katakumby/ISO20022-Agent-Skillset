---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000375-account-owner-requestor"
title: "Account Owner/Requestor — T2S SecuritiesAndPenaltyReporting narrative scope"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
source_labels: ["account owner/requestor"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["t2s-securities-and-penalty-reporting"]
message_ids: ["semt.026.001.01", "semt.027.001.01"]
message_families: ["semt.026", "semt.027"]
flows: []
source_locations: [{"source_id": "src-000375", "heading": "3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "file_pages": [13], "evidence_id": "src-000375-semt.026.001.01-p13-c001"}, {"source_id": "src-000375", "heading": "4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "file_pages": [77], "evidence_id": "src-000375-semt.027.001.01-p77-c001"}]
search_terms: ["account owner/requestor"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Account Owner/Requestor — T2S SecuritiesAndPenaltyReporting

## Definition and applicable context

This source names **account owner/requestor** in the Functionality of the messages listed below. The record is scoped to T2S SecuritiesAndPenaltyReporting, march-2026. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The SecuritiesSettlementInstructionQuery message is sent from an account owner/requestor to a settlement infrastructure.

src-000375, file p13, 3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| sender | The SecuritiesSettlementInstructionQuery message | current-message-scope-name-variant | sender: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000375-account-owner-requestor.md)); receiver: a settlement infrastructure ([a settlement infrastructure](participant-src-000374-settlement-infrastructure.md)) | [src-000375-semt.026.001.01-p13-c001-d1](#src-000375-semt.026.001.01-p13-c001); file p13 |
| receiver | The SecuritiesSettlementResponse message | current-message-scope-name-variant | sender: a settlement infrastructure ([a settlement infrastructure](participant-src-000374-settlement-infrastructure.md)); receiver: an account owner/requestor ([an account owner/requestor](participant-narrative-src-000375-account-owner-requestor.md)) | [src-000375-semt.027.001.01-p77-c001-d1](#src-000375-semt.027.001.01-p77-c001); file p77 |


## Complete source evidence

<a id="src-000375-semt.026.001.01-p13-c001"></a>

### src-000375-semt.026.001.01-p13-c001

src-000375; file p13; 3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01; scope.

> The SecuritiesSettlementInstructionQuery message is sent from an account owner/requestor to a settlement infrastructure.

<a id="src-000375-semt.027.001.01-p77-c001"></a>

### src-000375-semt.027.001.01-p77-c001

src-000375; file p77; 4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01; scope.

> The SecuritiesSettlementResponse message is sent from a settlement infrastructure to an account owner/requestor to provide the details of the securities settlement instructions, as selected in the search criteria defined in the request.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| semt.026.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.026.001.01/roles.md) | src-000375-semt.026.001.01-p13-c001 |
| semt.027.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.027.001.01/roles.md) | src-000375-semt.027.001.01-p77-c001 |


[Message-set flows](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `account owner/requestor`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000375](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf` · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
