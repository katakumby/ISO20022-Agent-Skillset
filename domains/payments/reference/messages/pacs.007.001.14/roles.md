---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "pacs.007.001.14 participant and direction evidence"
domain: "payments"
message_id: "pacs.007.001.14"
message_family: "pacs.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14"
source_ids: ["src-000163", "src-000168"]
message_sets: ["payments-clearing-and-settlement"]
role_labels: ["agent", "agents", "an agent", "creditor", "debtor", "next party in the payment chain", "the next party in the payment chain"]
search_terms: ["agent", "agents", "an agent", "creditor", "debtor", "next party in the payment chain", "the next party in the payment chain"]
participant_ids: ["participant-functionality-src-000163-agent", "participant-narrative-src-000163-next-party-in-the-payment-chain", "participant-src-000162-creditor", "participant-src-000162-debtor"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000163", "heading": "5 pacs.007.001.14 FIToFIPaymentReversalV14", "file_pages": [562, 701]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# pacs.007.001.14 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 4 uniquely resolved participant references.

## src-000163 — 5 pacs.007.001.14 FIToFIPaymentReversalV14

[src-000163](../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf); Functionality file pp562; publication March 2026.

### Direction and initiation clauses

#### src-000163-pacs.007.001.14-p562-c001-d1

Kind: sender-to-receiver; message applicability: **current-message-scope-name-variant**; src-000163 file p562, scope.

- Sender: **an agent**. [an agent](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md).
- Receiver: **the next party in the payment chain**. [the next party in the payment chain](../../../../../shared/reference/participants/participant-narrative-src-000163-next-party-in-the-payment-chain.md).

> The FinancialInstitutionToFinancialInstitutionPaymentReversal message is sent by an agent to the next party in the payment chain.

#### src-000163-pacs.007.001.14-p562-c002-d1

Kind: exchange-participants; message applicability: **current-message**; src-000163 file p562, usage.

- Exchange participants: **agents**. [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md).

> The FIToFIPaymentReversal message is exchanged between agents to reverse a payment message that has been settled.

An exchange-between statement establishes participation, not sender/receiver direction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000163-pacs.007.001.14-p562-c001 — file p562, scope.**

Mentioned roles: [agent](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md); [next party in the payment chain](../../../../../shared/reference/participants/participant-narrative-src-000163-next-party-in-the-payment-chain.md).

Quoted above in src-000163-pacs.007.001.14-p562-c001-d1.

**src-000163-pacs.007.001.14-p562-c002 — file p562, usage.**

Mentioned roles: [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md).

Quoted above in src-000163-pacs.007.001.14-p562-c002-d1.

**src-000163-pacs.007.001.14-p562-c003 — file p562, usage.**

Mentioned roles: [debtor](../../../../../shared/reference/participants/participant-src-000162-debtor.md); [creditor](../../../../../shared/reference/participants/participant-src-000162-creditor.md).

> The result will be a credit on the debtor account (when the reversed payment was a direct debit) or a debit on the creditor account (when the reversed payment was a credit transfer).

**src-000163-pacs.007.001.14-p562-c004 — file p562, usage.**

> The FIToFIPaymentReversal message refers to the original payment message by means of references only or by means of references and a set of elements from the original instruction.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p562, scope.**

> It is used to reverse a payment previously executed.

**File p562, usage.**

> The FIToFIPaymentReversal message may or may not be the follow-up of a payment message.

**File p562, usage.**

> The FIToFIPaymentReversal message can be used in domestic and cross-border scenarios.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
