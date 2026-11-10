---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "payments"
participant_id: "participant-narrative-src-000174-instructed-agent"
title: "Instructed Agent — Payments Initiation narrative scope"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
source_labels: ["instructed agent"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["payments-initiation"]
message_ids: ["pain.002.001.15"]
message_families: ["pain.002"]
flows: []
source_locations: [{"source_id": "src-000174", "heading": "3 pain.002.001.15 CustomerPaymentStatusReportV15", "file_pages": [130], "evidence_id": "src-000174-pain.002.001.15-p130-c001"}]
search_terms: ["instructed agent"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Instructed Agent — Payments Initiation

## Definition and applicable context

This source names **instructed agent** in the Functionality of the messages listed below. The record is scoped to Payments Initiation, March 2026. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The CustomerPaymentStatusReport message is sent by an instructed agent to the previous party in the payment chain.

src-000174, file p130, 3 pain.002.001.15 CustomerPaymentStatusReportV15, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| sender | The CustomerPaymentStatusReport message | current-message | sender: an instructed agent ([an instructed agent](participant-narrative-src-000174-instructed-agent.md)); receiver: the previous party in the payment chain ([the previous party in the payment chain](participant-narrative-src-000174-previous-party-in-the-payment-chain.md)) | [src-000174-pain.002.001.15-p130-c001-d1](#src-000174-pain.002.001.15-p130-c001); file p130 |


## Complete source evidence

<a id="src-000174-pain.002.001.15-p130-c001"></a>

### src-000174-pain.002.001.15-p130-c001

src-000174; file p130; 3 pain.002.001.15 CustomerPaymentStatusReportV15; scope.

> The CustomerPaymentStatusReport message is sent by an instructed agent to the previous party in the payment chain.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| pain.002.001.15 | [Exact message-role evidence](../../../domains/payments/reference/messages/pain.002.001.15/roles.md) | src-000174-pain.002.001.15-p130-c001 |


[Message-set flows](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `instructed agent`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000174](../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
