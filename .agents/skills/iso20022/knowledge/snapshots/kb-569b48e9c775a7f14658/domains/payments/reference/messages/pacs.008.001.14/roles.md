---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "pacs.008.001.14 participant and direction evidence"
domain: "payments"
message_id: "pacs.008.001.14"
message_family: "pacs.008"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14"
source_ids: ["src-000163", "src-000169"]
message_sets: ["payments-clearing-and-settlement"]
role_labels: ["agents", "creditor", "creditor agent", "customer", "debtor", "debtor agent", "financial institutions", "instructed agent", "instructing agent", "next financial institution in the payment chain", "one financial institution", "payment clearing and settlement system", "reimbursement agent", "the creditor agent", "the debtor agent", "the next financial institution in the payment chain"]
search_terms: ["agents", "creditor", "creditor agent", "customer", "debtor", "debtor agent", "financial institutions", "instructed agent", "instructing agent", "next financial institution in the payment chain", "one financial institution", "payment clearing and settlement system", "reimbursement agent", "the creditor agent", "the debtor agent", "the next financial institution in the payment chain"]
participant_ids: ["participant-functionality-src-000163-agent", "participant-functionality-src-000163-next-financial-institution", "participant-narrative-src-000163-customer", "participant-narrative-src-000163-financial-institution", "participant-narrative-src-000163-instructed-agent", "participant-narrative-src-000163-instructing-agent", "participant-narrative-src-000163-payment-clearing-and-settlement-system", "participant-narrative-src-000163-reimbursement-agent", "participant-src-000162-creditor", "participant-src-000162-creditor-agent", "participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-financial-institution"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000163", "heading": "6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "file_pages": [702, 829]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# pacs.008.001.14 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 3 direction/initiator/exchange clauses; 13 uniquely resolved participant references.

## src-000163 — 6 pacs.008.001.14 FIToFICustomerCreditTransferV14

[src-000163](../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md); Functionality file pp702; publication March 2026.

### Direction and initiation clauses

#### src-000163-pacs.008.001.14-p702-c001-d1

Kind: sender-to-receiver; message applicability: **current-message-scope-name-variant**; src-000163 file p702, scope.

- Sender: **the debtor agent**. [the debtor agent](../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md).
- Receiver: **the creditor agent, directly or through other agents and/or a payment clearing and settlement system**. [the creditor agent](../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md).

> The FinancialInstitutionToFinancialInstitutionCustomerCreditTransfer message is sent by the debtor agent to the creditor agent, directly or through other agents and/or a payment clearing and settlement system.

#### src-000163-pacs.008.001.14-p702-c003-d1

Kind: exchange-participants; message applicability: **current-message**; src-000163 file p702, usage.

- Exchange participants: **agents**. [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md).

> The FIToFICustomerCreditTransfer message is exchanged between agents and can contain one or more customer credit transfer instructions.

An exchange-between statement establishes participation, not sender/receiver direction.

#### src-000163-pacs.008.001.14-p702-c007-d1

Kind: sender-to-receiver; message applicability: **related-or-unspecified-message**; src-000163 file p702, usage.

- Sender: **one financial institution**. [one financial institution](../../../../../shared/reference/participants/participant-src-000162-financial-institution.md).
- Receiver: **the next financial institution in the payment chain**. [the next financial institution in the payment chain](../../../../../shared/reference/participants/participant-functionality-src-000163-next-financial-institution.md).

> If more than two financial institutions are involved in the payment chain and if the FIToFICustomerCreditTransfer is sent from one financial institution to the next financial institution in the payment chain, then the payment method is called the Serial method.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000163-pacs.008.001.14-p702-c001 — file p702, scope.**

Mentioned roles: [debtor agent](../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md); [creditor agent](../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md); [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md); [payment clearing and settlement system](../../../../../shared/reference/participants/participant-narrative-src-000163-payment-clearing-and-settlement-system.md).

Quoted above in src-000163-pacs.008.001.14-p702-c001-d1.

**src-000163-pacs.008.001.14-p702-c002 — file p702, scope.**

Mentioned roles: [debtor](../../../../../shared/reference/participants/participant-src-000162-debtor.md); [creditor](../../../../../shared/reference/participants/participant-src-000162-creditor.md).

> It is used to move funds from a debtor account to a creditor.

**src-000163-pacs.008.001.14-p702-c003 — file p702, usage.**

Mentioned roles: [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md); [customer](../../../../../shared/reference/participants/participant-narrative-src-000163-customer.md).

Quoted above in src-000163-pacs.008.001.14-p702-c003-d1.

**src-000163-pacs.008.001.14-p702-c004 — file p702, usage.**

Mentioned roles: [instructing agent](../../../../../shared/reference/participants/participant-narrative-src-000163-instructing-agent.md); [instructed agent](../../../../../shared/reference/participants/participant-narrative-src-000163-instructed-agent.md); [customer](../../../../../shared/reference/participants/participant-narrative-src-000163-customer.md).

> If the instructing agent and the instructed agent wish to use their direct account relationship in the currency of the transfer then the message contains both the funds for the customer transfer(s) as well as the payment details;

**src-000163-pacs.008.001.14-p702-c005 — file p702, usage.**

Mentioned roles: [instructing agent](../../../../../shared/reference/participants/participant-narrative-src-000163-instructing-agent.md); [instructed agent](../../../../../shared/reference/participants/participant-narrative-src-000163-instructed-agent.md); [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md); [customer](../../../../../shared/reference/participants/participant-narrative-src-000163-customer.md).

> If the instructing agent and the instructed agent have no direct account relationship in the currency of the transfer, or do not wish to use their account relationship, then other (reimbursement) agents will be involved to cover for the customer transfer(s).

**src-000163-pacs.008.001.14-p702-c006 — file p702, usage.**

Mentioned roles: [instructing agent](../../../../../shared/reference/participants/participant-narrative-src-000163-instructing-agent.md); [customer](../../../../../shared/reference/participants/participant-narrative-src-000163-customer.md); [reimbursement agent](../../../../../shared/reference/participants/participant-narrative-src-000163-reimbursement-agent.md).

> The FIToFICustomerCreditTransfer contains only the payment details and the instructing agent must cover the customer transfer by sending a FinancialInstitutionCreditTransfer to a reimbursement agent.

**src-000163-pacs.008.001.14-p702-c007 — file p702, usage.**

Mentioned roles: [financial institutions](../../../../../shared/reference/participants/participant-narrative-src-000163-financial-institution.md); [one financial institution](../../../../../shared/reference/participants/participant-src-000162-financial-institution.md); [next financial institution in the payment chain](../../../../../shared/reference/participants/participant-functionality-src-000163-next-financial-institution.md).

Quoted above in src-000163-pacs.008.001.14-p702-c007-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p702, usage.**

> The FIToFICustomerCreditTransfer message does not allow for grouping: a CreditTransferTransactionInformation block must be present for each credit transfer transaction.

**File p702, usage.**

> The FIToFICustomerCreditTransfer message can be used in different ways:

**File p702, usage.**

> This payment method is called the Cover method;

**File p702, usage.**

> The FIToFICustomerCreditTransfer message can be used in domestic and cross-border scenarios.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
