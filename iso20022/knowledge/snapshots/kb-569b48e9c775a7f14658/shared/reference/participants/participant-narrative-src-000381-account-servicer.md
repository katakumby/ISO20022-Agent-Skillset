---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000381-account-servicer"
title: "Account Servicer — T2S SettlementRestrictions narrative scope"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
source_labels: ["account servicer"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["t2s-settlement-restrictions"]
message_ids: ["semt.028.001.01", "semt.029.001.01", "semt.030.001.01", "semt.032.001.01", "semt.034.001.01"]
message_families: ["semt.028", "semt.029", "semt.030", "semt.032", "semt.034"]
flows: []
source_locations: [{"source_id": "src-000381", "heading": "2 semt.028.001.01 IntraPositionMovementQueryV01", "file_pages": [7], "evidence_id": "src-000381-semt.028.001.01-p7-c002"}, {"source_id": "src-000381", "heading": "3 semt.029.001.01 IntraPositionMovementQueryResponseV01", "file_pages": [57], "evidence_id": "src-000381-semt.029.001.01-p57-c002"}, {"source_id": "src-000381", "heading": "4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01", "file_pages": [87], "evidence_id": "src-000381-semt.030.001.01-p87-c002"}, {"source_id": "src-000381", "heading": "6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01", "file_pages": [134], "evidence_id": "src-000381-semt.032.001.01-p134-c002"}, {"source_id": "src-000381", "heading": "8 semt.034.001.01 IntraPositionMovementPendingReportV01", "file_pages": [169], "evidence_id": "src-000381-semt.034.001.01-p169-c002"}]
search_terms: ["account servicer"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Account Servicer — T2S SettlementRestrictions

## Definition and applicable context

This source names **account servicer** in the Functionality of the messages listed below. The record is scoped to T2S SettlementRestrictions, september-2025. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> re-send a message sent by the account owner to the account servicer (the sub-function of the message is "Duplicate")

src-000381, file p7, 2 semt.028.001.01 IntraPositionMovementQueryV01, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.

## Complete source evidence

<a id="src-000381-semt.028.001.01-p7-c002"></a>

### src-000381-semt.028.001.01-p7-c002

src-000381; file p7; 2 semt.028.001.01 IntraPositionMovementQueryV01; scope.

> re-send a message sent by the account owner to the account servicer (the sub-function of the message is "Duplicate")

<a id="src-000381-semt.029.001.01-p57-c002"></a>

### src-000381-semt.029.001.01-p57-c002

src-000381; file p57; 3 semt.029.001.01 IntraPositionMovementQueryResponseV01; scope.

> re-send a message sent by the account owner to the account servicer (the sub-function of the message is "Duplicate")

<a id="src-000381-semt.030.001.01-p87-c002"></a>

### src-000381-semt.030.001.01-p87-c002

src-000381; file p87; 4 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01; scope.

> re-send a message sent by the account owner to the account servicer (the sub-function of the message is "Duplicate")

<a id="src-000381-semt.032.001.01-p134-c002"></a>

### src-000381-semt.032.001.01-p134-c002

src-000381; file p134; 6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01; scope.

> re-send a message sent by the account owner to the account servicer (the sub-function of the message is "Duplicate")

<a id="src-000381-semt.034.001.01-p169-c002"></a>

### src-000381-semt.034.001.01-p169-c002

src-000381; file p169; 8 semt.034.001.01 IntraPositionMovementPendingReportV01; scope.

> re-send a message sent by the account owner to the account servicer (the sub-function of the message is "Duplicate")

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| semt.028.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.028.001.01/roles.md) | src-000381-semt.028.001.01-p7-c002 |
| semt.029.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.029.001.01/roles.md) | src-000381-semt.029.001.01-p57-c002 |
| semt.030.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.030.001.01/roles.md) | src-000381-semt.030.001.01-p87-c002 |
| semt.032.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.032.001.01/roles.md) | src-000381-semt.032.001.01-p134-c002 |
| semt.034.001.01 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.034.001.01/roles.md) | src-000381-semt.034.001.01-p169-c002 |


[Message-set flows](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `account servicer`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000381](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf` · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
