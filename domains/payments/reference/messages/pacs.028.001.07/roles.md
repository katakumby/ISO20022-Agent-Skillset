---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "pacs.028.001.07 participant and direction evidence"
domain: "payments"
message_id: "pacs.028.001.07"
message_family: "pacs.028"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07"
source_ids: ["src-000163", "src-000172"]
message_sets: ["payments-clearing-and-settlement"]
role_labels: ["agent", "agents", "creditor agent", "debtor agent", "payment clearing and settlement system", "the creditor agent", "the debtor agent"]
search_terms: ["agent", "agents", "creditor agent", "debtor agent", "payment clearing and settlement system", "the creditor agent", "the debtor agent"]
participant_ids: ["participant-functionality-src-000163-agent", "participant-narrative-src-000163-payment-clearing-and-settlement-system", "participant-src-000162-creditor-agent", "participant-src-000162-debtor-agent"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000163", "heading": "9 pacs.028.001.07 FIToFIPaymentStatusRequestV07", "file_pages": [1049, 1160]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# pacs.028.001.07 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 4 uniquely resolved participant references.

## src-000163 — 9 pacs.028.001.07 FIToFIPaymentStatusRequestV07

[src-000163](../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf); Functionality file pp1049; publication March 2026.

### Direction and initiation clauses

#### src-000163-pacs.028.001.07-p1049-c001-d1

Kind: sender-to-receiver; message applicability: **current-message-scope-name-variant**; src-000163 file p1049, scope.

- Sender: **the debtor agent**. [the debtor agent](../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md).
- Receiver: **the creditor agent, directly or through other agents and/or a payment clearing and settlement system**. [the creditor agent](../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md).

> The FinancialInstitutionToFinancialInstitutionPaymentStatusRequest message is sent by the debtor agent to the creditor agent, directly or through other agents and/or a payment clearing and settlement system.

#### src-000163-pacs.028.001.07-p1049-c003-d1

Kind: exchange-participants; message applicability: **current-message**; src-000163 file p1049, usage.

- Exchange participants: **agents**. [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md).

> The FIToFIPaymentStatusRequest message is exchanged between agents to request status information about instructions previously sent.

An exchange-between statement establishes participation, not sender/receiver direction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000163-pacs.028.001.07-p1049-c001 — file p1049, scope.**

Mentioned roles: [debtor agent](../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md); [creditor agent](../../../../../shared/reference/participants/participant-src-000162-creditor-agent.md); [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md); [payment clearing and settlement system](../../../../../shared/reference/participants/participant-narrative-src-000163-payment-clearing-and-settlement-system.md).

Quoted above in src-000163-pacs.028.001.07-p1049-c001-d1.

**src-000163-pacs.028.001.07-p1049-c002 — file p1049, scope.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> It is used to request a FIToFIPaymentStatusReport message containing information on the status of a previously sent instruction.

**src-000163-pacs.028.001.07-p1049-c003 — file p1049, usage.**

Mentioned roles: [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md).

Quoted above in src-000163-pacs.028.001.07-p1049-c003-d1.

**src-000163-pacs.028.001.07-p1049-c004 — file p1049, usage.**

Mentioned roles: [agents](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md).

> Its usage will always be governed by a bilateral agreement between the agents.

**src-000163-pacs.028.001.07-p1049-c005 — file p1049, usage.**

Mentioned roles: [agent](../../../../../shared/reference/participants/participant-functionality-src-000163-agent.md).

> The FIToFIPaymentStatusRequest message can be used to request information about the status (such as rejection, acceptance) of a credit transfer instruction, a direct debit instruction, as well as other intra- agent instructions (for example FIToFIPaymentCancellationRequest).

**src-000163-pacs.028.001.07-p1049-c006 — file p1049, usage.**

> The FIToFIPaymentStatusRequest message refers to the original instruction(s) by means of references only or by means of references and a set of elements from the original instruction.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p1049, usage.**

> The FIToFIPaymentStatusRequest message can be used in domestic and cross-border scenarios.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
