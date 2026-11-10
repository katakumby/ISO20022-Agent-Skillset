---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "payments"
participant_id: "participant-narrative-src-000163-financial-institution"
title: "Financial Institution — Payments Clearing and Settlement narrative scope"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
source_labels: ["financial institutions"]
aliases: []
role_type: "business role or institutional example in quoted Functionality context"
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14", "pacs.009.001.13", "pacs.010.001.06"]
message_families: ["pacs.008", "pacs.009", "pacs.010"]
flows: []
source_locations: [{"source_id": "src-000163", "heading": "6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "file_pages": [702], "evidence_id": "src-000163-pacs.008.001.14-p702-c007"}, {"source_id": "src-000163", "heading": "7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "file_pages": [830], "evidence_id": "src-000163-pacs.009.001.13-p830-c002"}, {"source_id": "src-000163", "heading": "7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "file_pages": [830], "evidence_id": "src-000163-pacs.009.001.13-p830-c003"}, {"source_id": "src-000163", "heading": "8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "file_pages": [1016], "evidence_id": "src-000163-pacs.010.001.06-p1016-c002"}]
search_terms: ["financial institution", "financial institutions"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Financial Institution — Payments Clearing and Settlement

## Definition and applicable context

This source names **financial institution** in the Functionality of the messages listed below. The record is scoped to Payments Clearing and Settlement, March 2026. Classification: business role or institutional example in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> If more than two financial institutions are involved in the payment chain and if the FIToFICustomerCreditTransfer is sent from one financial institution to the next financial institution in the payment chain, then the payment method is called the Serial method.

src-000163, file p702, 6 pacs.008.001.14 FIToFICustomerCreditTransferV14, usage. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.

## Complete source evidence

<a id="src-000163-pacs.008.001.14-p702-c007"></a>

### src-000163-pacs.008.001.14-p702-c007

src-000163; file p702; 6 pacs.008.001.14 FIToFICustomerCreditTransferV14; usage.

> If more than two financial institutions are involved in the payment chain and if the FIToFICustomerCreditTransfer is sent from one financial institution to the next financial institution in the payment chain, then the payment method is called the Serial method.

<a id="src-000163-pacs.009.001.13-p830-c002"></a>

### src-000163-pacs.009.001.13-p830-c002

src-000163; file p830; 7 pacs.009.001.13 FinancialInstitutionCreditTransferV13; scope.

> It is used to move funds from a debtor account to a creditor, where both debtor and creditor are financial institutions.

<a id="src-000163-pacs.009.001.13-p830-c003"></a>

### src-000163-pacs.009.001.13-p830-c003

src-000163; file p830; 7 pacs.009.001.13 FinancialInstitutionCreditTransferV13; usage.

> The FinancialInstitutionCreditTransfer message is exchanged between agents and can contain one or more credit transfer instructions where debtor and creditor are both financial institutions.

<a id="src-000163-pacs.010.001.06-p1016-c002"></a>

### src-000163-pacs.010.001.06-p1016-c002

src-000163; file p1016; 8 pacs.010.001.06 FinancialInstitutionDirectDebitV06; scope.

> It is used to instruct the DebtorAgent to move funds from one or more debtor(s) account(s) to one or more creditor(s), where both debtor and creditor are financial institutions.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| pacs.008.001.14 | [Exact message-role evidence](../../../domains/payments/reference/messages/pacs.008.001.14/roles.md) | src-000163-pacs.008.001.14-p702-c007 |
| pacs.009.001.13 | [Exact message-role evidence](../../../domains/payments/reference/messages/pacs.009.001.13/roles.md) | src-000163-pacs.009.001.13-p830-c002, src-000163-pacs.009.001.13-p830-c003 |
| pacs.010.001.06 | [Exact message-role evidence](../../../domains/payments/reference/messages/pacs.010.001.06/roles.md) | src-000163-pacs.010.001.06-p1016-c002 |


[Message-set flows](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `financial institutions`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000163](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
