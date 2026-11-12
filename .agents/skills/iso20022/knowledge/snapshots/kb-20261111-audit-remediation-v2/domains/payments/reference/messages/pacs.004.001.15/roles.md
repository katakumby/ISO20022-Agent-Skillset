---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "pacs.004.001.15 participant and direction evidence"
domain: "payments"
message_id: "pacs.004.001.15"
message_family: "pacs.004"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15"
source_ids: ["src-000163", "src-000167"]
message_sets: ["payments-clearing-and-settlement"]
role_labels: ["agent", "agents", "an agent", "Non-financial institution customers", "non-financial institution customers", "previous agent in the payment chain", "the previous agent in the payment chain"]
search_terms: ["agent", "agents", "an agent", "Non-financial institution customers", "non-financial institution customers", "previous agent in the payment chain", "the previous agent in the payment chain"]
participant_ids: ["participant-functionality-src-000163-agent", "participant-narrative-src-000163-non-financial-institution-customer", "participant-narrative-src-000163-previous-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000163", "heading": "4 pacs.004.001.15 PaymentReturnV15", "file_pages": [246, 561]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# pacs.004.001.15 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 3 uniquely resolved participant references.

## src-000163 — 4 pacs.004.001.15 PaymentReturnV15

[src-000163](../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md); Functionality file pp246; publication March 2026.

### Direction and initiation clauses

#### src-000163-pacs.004.001.15-p246-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000163 file p246, scope.

- Sender: **an agent**. [an agent](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md).
- Receiver: **the previous agent in the payment chain**. [the previous agent in the payment chain](../../../../../shared/reference/participants/participant-narrative-src-000163-previous-agent.md).

> The PaymentReturn message is sent by an agent to the previous agent in the payment chain to undo a payment previously settled.

#### src-000163-pacs.004.001.15-p246-c002-d1

Kind: exchange-participants; message applicability: **current-message**; src-000163 file p246, usage.

- Exchange participants: **agents**. [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md).

> The PaymentReturn message is exchanged between agents to return funds after settlement of credit transfer instructions (that is FIToFICustomerCreditTransfer message and FinancialInstitutionCreditTransfer message) or direct debit instructions (FIToFICustomerDirectDebit message).

An exchange-between statement establishes participation, not sender/receiver direction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000163-pacs.004.001.15-p246-c001 — file p246, scope.**

Mentioned roles: [agent](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md); [previous agent in the payment chain](../../../../../shared/reference/participants/participant-narrative-src-000163-previous-agent.md).

Quoted above in src-000163-pacs.004.001.15-p246-c001-d1.

**src-000163-pacs.004.001.15-p246-c002 — file p246, usage.**

Mentioned roles: [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md).

Quoted above in src-000163-pacs.004.001.15-p246-c002-d1.

**src-000163-pacs.004.001.15-p246-c003 — file p246, usage.**

Mentioned roles: [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md); [non-financial institution customers](../../../../../shared/reference/participants/participant-narrative-src-000163-non-financial-institution-customer.md).

> The PaymentReturn message should not be used between agents and non-financial institution customers.

**src-000163-pacs.004.001.15-p246-c004 — file p246, usage.**

Mentioned roles: [Non-financial institution customers](../../../../../shared/reference/participants/participant-narrative-src-000163-non-financial-institution-customer.md).

> Non-financial institution customers will be informed about a debit or a credit on their account(s) through a BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/BankToCustomerStatement message ('statement').

**src-000163-pacs.004.001.15-p246-c005 — file p246, usage.**

> The PaymentReturn message can be used to return single instructions or multiple instructions from one or different files.

**src-000163-pacs.004.001.15-p246-c006 — file p246, usage.**

> The PaymentReturn message refers to the original instruction(s) by means of references only or by means of references and a set of elements from the original instruction.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p246, usage.**

> The PaymentReturn message can be used in domestic and cross-border scenarios.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
