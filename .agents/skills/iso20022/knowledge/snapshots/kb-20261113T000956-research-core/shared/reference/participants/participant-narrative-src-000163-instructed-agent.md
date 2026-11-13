---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "payments"
participant_id: "participant-narrative-src-000163-instructed-agent"
title: "Instructed Agent — Payments Clearing and Settlement narrative scope"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
source_labels: ["instructed agent"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.002.001.16", "pacs.008.001.14"]
message_families: ["pacs.002", "pacs.008"]
flows: []
source_locations: [{"source_id": "src-000163", "heading": "2 pacs.002.001.16 FIToFIPaymentStatusReportV16", "file_pages": [6], "evidence_id": "src-000163-pacs.002.001.16-p6-c001"}, {"source_id": "src-000163", "heading": "6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "file_pages": [702], "evidence_id": "src-000163-pacs.008.001.14-p702-c004"}, {"source_id": "src-000163", "heading": "6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "file_pages": [702], "evidence_id": "src-000163-pacs.008.001.14-p702-c005"}]
search_terms: ["instructed agent"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Instructed Agent — Payments Clearing and Settlement

## Definition and applicable context

This source names **instructed agent** in the Functionality of the messages listed below. The record is scoped to Payments Clearing and Settlement, March 2026. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The FIToFIPaymentStatusReport message is sent by an instructed agent to the previous party in the payment chain.

src-000163, file p6, 2 pacs.002.001.16 FIToFIPaymentStatusReportV16, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| sender | The FIToFIPaymentStatusReport message | current-message | sender: an instructed agent ([an instructed agent](participant-narrative-src-000163-instructed-agent.md)); receiver: the previous party in the payment chain ([the previous party in the payment chain](participant-narrative-src-000163-previous-party-in-the-payment-chain.md)) | [src-000163-pacs.002.001.16-p6-c001-d1](#src-000163-pacs.002.001.16-p6-c001); file p6 |


## Complete source evidence

<a id="src-000163-pacs.002.001.16-p6-c001"></a>

### src-000163-pacs.002.001.16-p6-c001

src-000163; file p6; 2 pacs.002.001.16 FIToFIPaymentStatusReportV16; scope.

> The FIToFIPaymentStatusReport message is sent by an instructed agent to the previous party in the payment chain.

<a id="src-000163-pacs.008.001.14-p702-c004"></a>

### src-000163-pacs.008.001.14-p702-c004

src-000163; file p702; 6 pacs.008.001.14 FIToFICustomerCreditTransferV14; usage.

> If the instructing agent and the instructed agent wish to use their direct account relationship in the currency of the transfer then the message contains both the funds for the customer transfer(s) as well as the payment details;

<a id="src-000163-pacs.008.001.14-p702-c005"></a>

### src-000163-pacs.008.001.14-p702-c005

src-000163; file p702; 6 pacs.008.001.14 FIToFICustomerCreditTransferV14; usage.

> If the instructing agent and the instructed agent have no direct account relationship in the currency of the transfer, or do not wish to use their account relationship, then other (reimbursement) agents will be involved to cover for the customer transfer(s).

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| pacs.002.001.16 | [Exact message-role evidence](../../../domains/payments/reference/messages/pacs.002.001.16/roles.md) | src-000163-pacs.002.001.16-p6-c001 |
| pacs.008.001.14 | [Exact message-role evidence](../../../domains/payments/reference/messages/pacs.008.001.14/roles.md) | src-000163-pacs.008.001.14-p702-c004, src-000163-pacs.008.001.14-p702-c005 |


[Message-set flows](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `instructed agent`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000163](../../../evidence/omitted/0b754f3040fa67a0a084bf38.md) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
