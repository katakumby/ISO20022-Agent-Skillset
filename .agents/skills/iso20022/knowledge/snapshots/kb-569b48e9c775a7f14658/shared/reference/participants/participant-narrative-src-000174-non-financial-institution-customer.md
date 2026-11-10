---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "payments"
participant_id: "participant-narrative-src-000174-non-financial-institution-customer"
title: "Non-Financial Institution Customer — Payments Initiation narrative scope"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
source_labels: ["non-financial institution customer"]
aliases: []
role_type: "business role or institutional example in quoted Functionality context"
message_sets: ["payments-initiation"]
message_ids: ["pain.002.001.15", "pain.007.001.13"]
message_families: ["pain.002", "pain.007"]
flows: []
source_locations: [{"source_id": "src-000174", "heading": "3 pain.002.001.15 CustomerPaymentStatusReportV15", "file_pages": [130], "evidence_id": "src-000174-pain.002.001.15-p130-c004"}, {"source_id": "src-000174", "heading": "3 pain.002.001.15 CustomerPaymentStatusReportV15", "file_pages": [130], "evidence_id": "src-000174-pain.002.001.15-p130-c005"}, {"source_id": "src-000174", "heading": "4 pain.007.001.13 CustomerPaymentReversalV13", "file_pages": [272], "evidence_id": "src-000174-pain.007.001.13-p272-c002"}]
search_terms: ["non-financial institution customer"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Non-Financial Institution Customer — Payments Initiation

## Definition and applicable context

This source names **non-financial institution customer** in the Functionality of the messages listed below. The record is scoped to Payments Initiation, March 2026. Classification: business role or institutional example in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The CustomerPaymentStatusReport message is exchanged between an agent and a non-financial institution customer to provide status information on instructions previously sent.

src-000174, file p130, 3 pain.002.001.15 CustomerPaymentStatusReportV15, usage. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| exchange_participants | The CustomerPaymentStatusReport message | current-message | exchange_participants: an agent and a non-financial institution customer ([a non-financial institution customer](participant-narrative-src-000174-non-financial-institution-customer.md)) | [src-000174-pain.002.001.15-p130-c004-d1](#src-000174-pain.002.001.15-p130-c004); file p130 |
| exchange_participants | The CustomerPaymentReversal message | current-message | exchange_participants: a non-financial institution customer and an agent ([a non-financial institution customer](participant-narrative-src-000174-non-financial-institution-customer.md)) | [src-000174-pain.007.001.13-p272-c002-d1](#src-000174-pain.007.001.13-p272-c002); file p272 |


## Complete source evidence

<a id="src-000174-pain.002.001.15-p130-c004"></a>

### src-000174-pain.002.001.15-p130-c004

src-000174; file p130; 3 pain.002.001.15 CustomerPaymentStatusReportV15; usage.

> The CustomerPaymentStatusReport message is exchanged between an agent and a non-financial institution customer to provide status information on instructions previously sent.

<a id="src-000174-pain.002.001.15-p130-c005"></a>

### src-000174-pain.002.001.15-p130-c005

src-000174; file p130; 3 pain.002.001.15 CustomerPaymentStatusReportV15; usage.

> Its usage may be governed by a bilateral or multilateral agreement between the agent and the non-financial institution customer.

<a id="src-000174-pain.007.001.13-p272-c002"></a>

### src-000174-pain.007.001.13-p272-c002

src-000174; file p272; 4 pain.007.001.13 CustomerPaymentReversalV13; usage.

> The CustomerPaymentReversal message is exchanged between a non-financial institution customer and an agent to reverse a CustomerDirectDebitInitiation message that has been settled.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| pain.002.001.15 | [Exact message-role evidence](../../../domains/payments/reference/messages/pain.002.001.15/roles.md) | src-000174-pain.002.001.15-p130-c004, src-000174-pain.002.001.15-p130-c005 |
| pain.007.001.13 | [Exact message-role evidence](../../../domains/payments/reference/messages/pain.007.001.13/roles.md) | src-000174-pain.007.001.13-p272-c002 |


[Message-set flows](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `non-financial institution customer`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000174](../../../evidence/omitted/577241d5215d98d6ed689f57.md) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
