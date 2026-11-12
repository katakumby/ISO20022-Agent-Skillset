---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "payments"
participant_id: "participant-narrative-src-000174-beneficiary"
title: "Beneficiary — Payments Initiation narrative scope"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
source_labels: ["beneficiary"]
aliases: []
role_type: "business role or institutional example in quoted Functionality context"
message_sets: ["payments-initiation"]
message_ids: ["pain.002.001.15"]
message_families: ["pain.002"]
flows: []
source_locations: [{"source_id": "src-000174", "heading": "3 pain.002.001.15 CustomerPaymentStatusReportV15", "file_pages": [130], "evidence_id": "src-000174-pain.002.001.15-p130-c008"}]
search_terms: ["beneficiary"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Beneficiary — Payments Initiation

## Definition and applicable context

This source names **beneficiary** in the Functionality of the messages listed below. The record is scoped to Payments Initiation, March 2026. Classification: business role or institutional example in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The CustomerPaymentStatusReport may also be sent to the receiver of the payment in a real time payment scenario, as both sides of the transactions must be informed of the status of the transaction (that is either the beneficiary is credited, or the transaction is rejected).

src-000174, file p130, 3 pain.002.001.15 CustomerPaymentStatusReportV15, usage. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.

## Complete source evidence

<a id="src-000174-pain.002.001.15-p130-c008"></a>

### src-000174-pain.002.001.15-p130-c008

src-000174; file p130; 3 pain.002.001.15 CustomerPaymentStatusReportV15; usage.

> The CustomerPaymentStatusReport may also be sent to the receiver of the payment in a real time payment scenario, as both sides of the transactions must be informed of the status of the transaction (that is either the beneficiary is credited, or the transaction is rejected).

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| pain.002.001.15 | [Exact message-role evidence](../../../domains/payments/reference/messages/pain.002.001.15/roles.md) | src-000174-pain.002.001.15-p130-c008 |


[Message-set flows](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `beneficiary`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000174](../../../evidence/omitted/577241d5215d98d6ed689f57.md) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
