---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "payments"
participant_id: "participant-narrative-src-000163-receiver-of-the-payment"
title: "Receiver Of The Payment — Payments Clearing and Settlement narrative scope"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
source_labels: ["receiver of the payment"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.002.001.16"]
message_families: ["pacs.002"]
flows: []
source_locations: [{"source_id": "src-000163", "heading": "2 pacs.002.001.16 FIToFIPaymentStatusReportV16", "file_pages": [6], "evidence_id": "src-000163-pacs.002.001.16-p6-c008"}]
search_terms: ["receiver of the payment"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Receiver Of The Payment — Payments Clearing and Settlement

## Definition and applicable context

This source names **receiver of the payment** in the Functionality of the messages listed below. The record is scoped to Payments Clearing and Settlement, March 2026. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The FIToFIPaymentStatusReport may also be sent to the receiver of the payment in a real time payment scenario, as both sides of the transactions must be informed of the status of the transaction (for example either the beneficiary is credited, or the transaction is rejected).

src-000163, file p6, 2 pacs.002.001.16 FIToFIPaymentStatusReportV16, usage. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.

## Complete source evidence

<a id="src-000163-pacs.002.001.16-p6-c008"></a>

### src-000163-pacs.002.001.16-p6-c008

src-000163; file p6; 2 pacs.002.001.16 FIToFIPaymentStatusReportV16; usage.

> The FIToFIPaymentStatusReport may also be sent to the receiver of the payment in a real time payment scenario, as both sides of the transactions must be informed of the status of the transaction (for example either the beneficiary is credited, or the transaction is rejected).

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| pacs.002.001.16 | [Exact message-role evidence](../../../domains/payments/reference/messages/pacs.002.001.16/roles.md) | src-000163-pacs.002.001.16-p6-c008 |


[Message-set flows](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `receiver of the payment`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000163](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
