---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "payments"
participant_id: "participant-narrative-src-000163-next-party-in-the-payment-chain"
title: "Next Party In The Payment Chain — Payments Clearing and Settlement narrative scope"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
source_labels: ["next party in the payment chain"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.007.001.14"]
message_families: ["pacs.007"]
flows: []
source_locations: [{"source_id": "src-000163", "heading": "5 pacs.007.001.14 FIToFIPaymentReversalV14", "file_pages": [562], "evidence_id": "src-000163-pacs.007.001.14-p562-c001"}]
search_terms: ["next party in the payment chain"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Next Party In The Payment Chain — Payments Clearing and Settlement

## Definition and applicable context

This source names **next party in the payment chain** in the Functionality of the messages listed below. The record is scoped to Payments Clearing and Settlement, March 2026. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The FinancialInstitutionToFinancialInstitutionPaymentReversal message is sent by an agent to the next party in the payment chain.

src-000163, file p562, 5 pacs.007.001.14 FIToFIPaymentReversalV14, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| receiver | The FinancialInstitutionToFinancialInstitutionPaymentReversal message | current-message-scope-name-variant | sender: an agent; receiver: the next party in the payment chain ([the next party in the payment chain](participant-narrative-src-000163-next-party-in-the-payment-chain.md)) | [src-000163-pacs.007.001.14-p562-c001-d1](#src-000163-pacs.007.001.14-p562-c001); file p562 |


## Complete source evidence

<a id="src-000163-pacs.007.001.14-p562-c001"></a>

### src-000163-pacs.007.001.14-p562-c001

src-000163; file p562; 5 pacs.007.001.14 FIToFIPaymentReversalV14; scope.

> The FinancialInstitutionToFinancialInstitutionPaymentReversal message is sent by an agent to the next party in the payment chain.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| pacs.007.001.14 | [Exact message-role evidence](../../../domains/payments/reference/messages/pacs.007.001.14/roles.md) | src-000163-pacs.007.001.14-p562-c001 |


[Message-set flows](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `next party in the payment chain`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000163](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
