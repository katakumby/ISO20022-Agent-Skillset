---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "payments"
participant_id: "participant-narrative-src-000163-non-financial-institution-customer"
title: "Non-Financial Institution Customer — Payments Clearing and Settlement narrative scope"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
source_labels: ["Non-financial institution customers", "non-financial institution customers"]
aliases: []
role_type: "business role or institutional example in quoted Functionality context"
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.004.001.15"]
message_families: ["pacs.004"]
flows: []
source_locations: [{"source_id": "src-000163", "heading": "4 pacs.004.001.15 PaymentReturnV15", "file_pages": [246], "evidence_id": "src-000163-pacs.004.001.15-p246-c003"}, {"source_id": "src-000163", "heading": "4 pacs.004.001.15 PaymentReturnV15", "file_pages": [246], "evidence_id": "src-000163-pacs.004.001.15-p246-c004"}]
search_terms: ["Non-financial institution customers", "non-financial institution customer", "non-financial institution customers"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Non-Financial Institution Customer — Payments Clearing and Settlement

## Definition and applicable context

This source names **non-financial institution customer** in the Functionality of the messages listed below. The record is scoped to Payments Clearing and Settlement, March 2026. Classification: business role or institutional example in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The PaymentReturn message should not be used between agents and non-financial institution customers.

src-000163, file p246, 4 pacs.004.001.15 PaymentReturnV15, usage. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.

## Complete source evidence

<a id="src-000163-pacs.004.001.15-p246-c003"></a>

### src-000163-pacs.004.001.15-p246-c003

src-000163; file p246; 4 pacs.004.001.15 PaymentReturnV15; usage.

> The PaymentReturn message should not be used between agents and non-financial institution customers.

<a id="src-000163-pacs.004.001.15-p246-c004"></a>

### src-000163-pacs.004.001.15-p246-c004

src-000163; file p246; 4 pacs.004.001.15 PaymentReturnV15; usage.

> Non-financial institution customers will be informed about a debit or a credit on their account(s) through a BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/BankToCustomerStatement message ('statement').

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| pacs.004.001.15 | [Exact message-role evidence](../../../domains/payments/reference/messages/pacs.004.001.15/roles.md) | src-000163-pacs.004.001.15-p246-c003, src-000163-pacs.004.001.15-p246-c004 |


[Message-set flows](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `Non-financial institution customers`, `non-financial institution customers`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000163](../../../evidence/omitted/0b754f3040fa67a0a084bf38.md) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
