---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "pacs.009.001.13 participant and direction evidence"
domain: "payments"
message_id: "pacs.009.001.13"
message_family: "pacs.009"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13"
source_ids: ["src-000163", "src-000170"]
message_sets: ["payments-clearing-and-settlement"]
role_labels: ["a creditor financial institution", "a debtor financial institution", "agents", "creditor", "creditor financial institution", "debtor", "debtor financial institution", "financial institutions", "payment clearing and settlement system"]
search_terms: ["a creditor financial institution", "a debtor financial institution", "agents", "creditor", "creditor financial institution", "debtor", "debtor financial institution", "financial institutions", "payment clearing and settlement system"]
participant_ids: ["participant-functionality-src-000163-agent", "participant-functionality-src-000163-creditor-financial-institution", "participant-functionality-src-000163-debtor-financial-institution", "participant-narrative-src-000163-financial-institution", "participant-narrative-src-000163-payment-clearing-and-settlement-system", "participant-src-000162-creditor", "participant-src-000162-debtor"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000163", "heading": "7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "file_pages": [830, 1015]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# pacs.009.001.13 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 7 uniquely resolved participant references.

## src-000163 — 7 pacs.009.001.13 FinancialInstitutionCreditTransferV13

[src-000163](../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf); Functionality file pp830; publication March 2026.

### Direction and initiation clauses

#### src-000163-pacs.009.001.13-p830-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000163 file p830, scope.

- Sender: **a debtor financial institution**. [a debtor financial institution](../../../../../shared/reference/participants/participant-functionality-src-000163-debtor-financial-institution.md).
- Receiver: **a creditor financial institution, directly or through other agents and/or a payment clearing and settlement system**. [a creditor financial institution](../../../../../shared/reference/participants/participant-functionality-src-000163-creditor-financial-institution.md).

> The FinancialInstitutionCreditTransfer message is sent by a debtor financial institution to a creditor financial institution, directly or through other agents and/or a payment clearing and settlement system.

#### src-000163-pacs.009.001.13-p830-c003-d1

Kind: exchange-participants; message applicability: **current-message**; src-000163 file p830, usage.

- Exchange participants: **agents**. [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md).

> The FinancialInstitutionCreditTransfer message is exchanged between agents and can contain one or more credit transfer instructions where debtor and creditor are both financial institutions.

An exchange-between statement establishes participation, not sender/receiver direction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000163-pacs.009.001.13-p830-c001 — file p830, scope.**

Mentioned roles: [debtor financial institution](../../../../../shared/reference/participants/participant-functionality-src-000163-debtor-financial-institution.md); [creditor financial institution](../../../../../shared/reference/participants/participant-functionality-src-000163-creditor-financial-institution.md); [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md); [payment clearing and settlement system](../../../../../shared/reference/participants/participant-narrative-src-000163-payment-clearing-and-settlement-system.md).

Quoted above in src-000163-pacs.009.001.13-p830-c001-d1.

**src-000163-pacs.009.001.13-p830-c002 — file p830, scope.**

Mentioned roles: [debtor](../../../../../shared/reference/participants/participant-src-000162-debtor.md); [creditor](../../../../../shared/reference/participants/participant-src-000162-creditor.md); [debtor](../../../../../shared/reference/participants/participant-src-000162-debtor.md); [creditor](../../../../../shared/reference/participants/participant-src-000162-creditor.md); [financial institutions](../../../../../shared/reference/participants/participant-narrative-src-000163-financial-institution.md).

> It is used to move funds from a debtor account to a creditor, where both debtor and creditor are financial institutions.

**src-000163-pacs.009.001.13-p830-c003 — file p830, usage.**

Mentioned roles: [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md); [debtor](../../../../../shared/reference/participants/participant-src-000162-debtor.md); [creditor](../../../../../shared/reference/participants/participant-src-000162-creditor.md); [financial institutions](../../../../../shared/reference/participants/participant-narrative-src-000163-financial-institution.md).

Quoted above in src-000163-pacs.009.001.13-p830-c003-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p830, usage.**

> The FinancialInstitutionCreditTransfer message does not allow for grouping: a CreditTransferTransactionInformation block must be present for each credit transfer transaction.

**File p830, usage.**

> The FinancialInstitutionCreditTransfer message can be used in domestic and cross-border scenarios.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
