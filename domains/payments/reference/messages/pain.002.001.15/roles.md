---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "pain.002.001.15 participant and direction evidence"
domain: "payments"
message_id: "pain.002.001.15"
message_family: "pain.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:pain.002.001.15"
source_ids: ["src-000174", "src-000177"]
message_sets: ["payments-initiation"]
role_labels: ["a non-financial institution customer", "agent", "an agent", "an instructed agent", "beneficiary", "customer", "instructed agent", "non-financial institution customer", "previous party in the payment chain", "receiver of the payment", "the previous party in the payment chain"]
search_terms: ["a non-financial institution customer", "agent", "an agent", "an instructed agent", "beneficiary", "customer", "instructed agent", "non-financial institution customer", "previous party in the payment chain", "receiver of the payment", "the previous party in the payment chain"]
participant_ids: ["participant-functionality-src-000174-agent", "participant-narrative-src-000174-beneficiary", "participant-narrative-src-000174-customer", "participant-narrative-src-000174-instructed-agent", "participant-narrative-src-000174-non-financial-institution-customer", "participant-narrative-src-000174-previous-party-in-the-payment-chain", "participant-narrative-src-000174-receiver-of-the-payment"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000174", "heading": "3 pain.002.001.15 CustomerPaymentStatusReportV15", "file_pages": [130, 271]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# pain.002.001.15 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 3 direction/initiator/exchange clauses; 7 uniquely resolved participant references.

## src-000174 — 3 pain.002.001.15 CustomerPaymentStatusReportV15

[src-000174](../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf); Functionality file pp130; publication March 2026.

### Direction and initiation clauses

#### src-000174-pain.002.001.15-p130-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000174 file p130, scope.

- Sender: **an instructed agent**. [an instructed agent](../../../../../shared/reference/participants/participant-narrative-src-000174-instructed-agent.md).
- Receiver: **the previous party in the payment chain**. [the previous party in the payment chain](../../../../../shared/reference/participants/participant-narrative-src-000174-previous-party-in-the-payment-chain.md).

> The CustomerPaymentStatusReport message is sent by an instructed agent to the previous party in the payment chain.

#### src-000174-pain.002.001.15-p130-c004-d1

Kind: exchange-participants; message applicability: **current-message**; src-000174 file p130, usage.

- Exchange participants: **an agent and a non-financial institution customer**. [an agent](../../../../../shared/reference/participants/participant-functionality-src-000174-agent.md); [a non-financial institution customer](../../../../../shared/reference/participants/participant-narrative-src-000174-non-financial-institution-customer.md).

> The CustomerPaymentStatusReport message is exchanged between an agent and a non-financial institution customer to provide status information on instructions previously sent.

An exchange-between statement establishes participation, not sender/receiver direction.

#### src-000174-pain.002.001.15-p130-c008-d1

Kind: receiver-only; message applicability: **current-message**; src-000174 file p130, usage.

- Receiver: **receiver of the payment**. [receiver of the payment](../../../../../shared/reference/participants/participant-narrative-src-000174-receiver-of-the-payment.md).

> The CustomerPaymentStatusReport may also be sent to the receiver of the payment in a real time payment scenario, as both sides of the transactions must be informed of the status of the transaction (that is either the beneficiary is credited, or the transaction is rejected).

Additional conditional receiver in a real-time payment scenario; both transaction sides must be informed. The full credited/rejected alternatives remain in the quote.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000174-pain.002.001.15-p130-c001 — file p130, scope.**

Mentioned roles: [instructed agent](../../../../../shared/reference/participants/participant-narrative-src-000174-instructed-agent.md); [previous party in the payment chain](../../../../../shared/reference/participants/participant-narrative-src-000174-previous-party-in-the-payment-chain.md).

Quoted above in src-000174-pain.002.001.15-p130-c001-d1.

**src-000174-pain.002.001.15-p130-c002 — file p130, scope.**

> It is used to inform this party about the positive or negative status of an instruction (either single or file).

**src-000174-pain.002.001.15-p130-c003 — file p130, scope.**

> It is also used to report on a pending instruction.

**src-000174-pain.002.001.15-p130-c004 — file p130, usage.**

Mentioned roles: [agent](../../../../../shared/reference/participants/participant-functionality-src-000174-agent.md); [non-financial institution customer](../../../../../shared/reference/participants/participant-narrative-src-000174-non-financial-institution-customer.md).

Quoted above in src-000174-pain.002.001.15-p130-c004-d1.

**src-000174-pain.002.001.15-p130-c005 — file p130, usage.**

Mentioned roles: [agent](../../../../../shared/reference/participants/participant-functionality-src-000174-agent.md); [non-financial institution customer](../../../../../shared/reference/participants/participant-narrative-src-000174-non-financial-institution-customer.md).

> Its usage may be governed by a bilateral or multilateral agreement between the agent and the non-financial institution customer.

**src-000174-pain.002.001.15-p130-c006 — file p130, usage.**

Mentioned roles: [customer](../../../../../shared/reference/participants/participant-narrative-src-000174-customer.md).

> The CustomerPaymentStatusReport message can be used to provide information about the status (for example a rejection, an acceptance) of the initiation of a credit transfer, a direct debit, as well as on the initiation of other customer instructions.

**src-000174-pain.002.001.15-p130-c007 — file p130, usage.**

> The CustomerPaymentStatusReport message refers to the original instruction(s) by means of references only or by means of references and a set of elements from the original instruction.

**src-000174-pain.002.001.15-p130-c008 — file p130, usage.**

Mentioned roles: [receiver of the payment](../../../../../shared/reference/participants/participant-narrative-src-000174-receiver-of-the-payment.md); [beneficiary](../../../../../shared/reference/participants/participant-narrative-src-000174-beneficiary.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000174-pain.002.001.15-p130-c008-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p130, usage.**

> The CustomerPaymentStatusReport message can be used in domestic and cross-border scenarios.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
