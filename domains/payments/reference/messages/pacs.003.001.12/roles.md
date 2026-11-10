---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "pacs.003.001.12 participant and direction evidence"
domain: "payments"
message_id: "pacs.003.001.12"
message_family: "pacs.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12"
source_ids: ["src-000163", "src-000166"]
message_sets: ["payments-clearing-and-settlement"]
role_labels: ["agents", "creditor", "creditor agent", "customer", "debtor", "debtor agent", "payment clearing and settlement system", "the creditor agent", "the debtor agent"]
search_terms: ["agents", "creditor", "creditor agent", "customer", "debtor", "debtor agent", "payment clearing and settlement system", "the creditor agent", "the debtor agent"]
participant_ids: ["participant-functionality-src-000163-agent", "participant-narrative-src-000163-customer", "participant-narrative-src-000163-payment-clearing-and-settlement-system", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000163", "heading": "3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "file_pages": [132, 245]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# pacs.003.001.12 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 7 uniquely resolved participant references.

## src-000163 — 3 pacs.003.001.12 FIToFICustomerDirectDebitV12

[src-000163](../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf); Functionality file pp132; publication March 2026.

### Direction and initiation clauses

#### src-000163-pacs.003.001.12-p132-c001-d1

Kind: sender-to-receiver; message applicability: **current-message-scope-name-variant**; src-000163 file p132, scope.

- Sender: **the creditor agent**. [the creditor agent](../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md).
- Receiver: **the debtor agent, directly or through other agents and/or a payment clearing and settlement system**. [the debtor agent](../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md).

> The FinancialInstitutionToFinancialInstitutionCustomerDirectDebit message is sent by the creditor agent to the debtor agent, directly or through other agents and/or a payment clearing and settlement system.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000163-pacs.003.001.12-p132-c001 — file p132, scope.**

Mentioned roles: [creditor agent](../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md); [debtor agent](../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md); [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md); [payment clearing and settlement system](../../../../../shared/reference/participants/participant-narrative-src-000163-payment-clearing-and-settlement-system.md).

Quoted above in src-000163-pacs.003.001.12-p132-c001-d1.

**src-000163-pacs.003.001.12-p132-c002 — file p132, scope.**

Mentioned roles: [debtor](../../../../../shared/reference/participants/participant-src-000162-debtor.md); [creditor](../../../../../shared/reference/participants/participant-src-000162-creditor.md).

> It is used to collect funds from a debtor account for a creditor.

**src-000163-pacs.003.001.12-p132-c003 — file p132, usage.**

Mentioned roles: [customer](../../../../../shared/reference/participants/participant-narrative-src-000163-customer.md).

> The FItoFICustomerDirectDebit message can contain one or more customer direct debit instructions.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p132, usage.**

> The FIToFICustomerDirectDebit message does not allow for grouping.

**File p132, usage.**

> The FItoFICustomerDirectDebit message may or may not contain mandate related information, that is extracts from a mandate, such as the MandateIdentification or DateOfSignature.

**File p132, usage.**

> The FIToFICustomerDirectDebit message must not be considered as a mandate.

**File p132, usage.**

> The FItoFICustomerDirectDebit message can be used in domestic and cross-border scenarios.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
