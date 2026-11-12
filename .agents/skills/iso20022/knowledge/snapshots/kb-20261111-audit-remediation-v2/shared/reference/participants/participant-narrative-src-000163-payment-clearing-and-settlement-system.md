---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "payments"
participant_id: "participant-narrative-src-000163-payment-clearing-and-settlement-system"
title: "Payment Clearing And Settlement System — Payments Clearing and Settlement narrative scope"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
source_labels: ["payment clearing and settlement system"]
aliases: []
role_type: "business role or institutional example in quoted Functionality context"
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.003.001.12", "pacs.008.001.14", "pacs.009.001.13", "pacs.028.001.07"]
message_families: ["pacs.003", "pacs.008", "pacs.009", "pacs.028"]
flows: []
source_locations: [{"source_id": "src-000163", "heading": "3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "file_pages": [132], "evidence_id": "src-000163-pacs.003.001.12-p132-c001"}, {"source_id": "src-000163", "heading": "6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "file_pages": [702], "evidence_id": "src-000163-pacs.008.001.14-p702-c001"}, {"source_id": "src-000163", "heading": "7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "file_pages": [830], "evidence_id": "src-000163-pacs.009.001.13-p830-c001"}, {"source_id": "src-000163", "heading": "9 pacs.028.001.07 FIToFIPaymentStatusRequestV07", "file_pages": [1049], "evidence_id": "src-000163-pacs.028.001.07-p1049-c001"}]
search_terms: ["payment clearing and settlement system"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Payment Clearing And Settlement System — Payments Clearing and Settlement

## Definition and applicable context

This source names **payment clearing and settlement system** in the Functionality of the messages listed below. The record is scoped to Payments Clearing and Settlement, March 2026. Classification: business role or institutional example in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The FinancialInstitutionToFinancialInstitutionCustomerDirectDebit message is sent by the creditor agent to the debtor agent, directly or through other agents and/or a payment clearing and settlement system.

src-000163, file p132, 3 pacs.003.001.12 FIToFICustomerDirectDebitV12, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.

## Complete source evidence

<a id="src-000163-pacs.003.001.12-p132-c001"></a>

### src-000163-pacs.003.001.12-p132-c001

src-000163; file p132; 3 pacs.003.001.12 FIToFICustomerDirectDebitV12; scope.

> The FinancialInstitutionToFinancialInstitutionCustomerDirectDebit message is sent by the creditor agent to the debtor agent, directly or through other agents and/or a payment clearing and settlement system.

<a id="src-000163-pacs.008.001.14-p702-c001"></a>

### src-000163-pacs.008.001.14-p702-c001

src-000163; file p702; 6 pacs.008.001.14 FIToFICustomerCreditTransferV14; scope.

> The FinancialInstitutionToFinancialInstitutionCustomerCreditTransfer message is sent by the debtor agent to the creditor agent, directly or through other agents and/or a payment clearing and settlement system.

<a id="src-000163-pacs.009.001.13-p830-c001"></a>

### src-000163-pacs.009.001.13-p830-c001

src-000163; file p830; 7 pacs.009.001.13 FinancialInstitutionCreditTransferV13; scope.

> The FinancialInstitutionCreditTransfer message is sent by a debtor financial institution to a creditor financial institution, directly or through other agents and/or a payment clearing and settlement system.

<a id="src-000163-pacs.028.001.07-p1049-c001"></a>

### src-000163-pacs.028.001.07-p1049-c001

src-000163; file p1049; 9 pacs.028.001.07 FIToFIPaymentStatusRequestV07; scope.

> The FinancialInstitutionToFinancialInstitutionPaymentStatusRequest message is sent by the debtor agent to the creditor agent, directly or through other agents and/or a payment clearing and settlement system.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| pacs.003.001.12 | [Exact message-role evidence](../../../domains/payments/reference/messages/pacs.003.001.12/roles.md) | src-000163-pacs.003.001.12-p132-c001 |
| pacs.008.001.14 | [Exact message-role evidence](../../../domains/payments/reference/messages/pacs.008.001.14/roles.md) | src-000163-pacs.008.001.14-p702-c001 |
| pacs.009.001.13 | [Exact message-role evidence](../../../domains/payments/reference/messages/pacs.009.001.13/roles.md) | src-000163-pacs.009.001.13-p830-c001 |
| pacs.028.001.07 | [Exact message-role evidence](../../../domains/payments/reference/messages/pacs.028.001.07/roles.md) | src-000163-pacs.028.001.07-p1049-c001 |


[Message-set flows](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `payment clearing and settlement system`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000163](../../../evidence/omitted/0b754f3040fa67a0a084bf38.md) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
