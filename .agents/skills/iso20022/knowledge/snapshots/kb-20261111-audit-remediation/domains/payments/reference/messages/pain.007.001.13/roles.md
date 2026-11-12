---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "pain.007.001.13 participant and direction evidence"
domain: "payments"
message_id: "pain.007.001.13"
message_family: "pain.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:pain.007.001.13"
source_ids: ["src-000174", "src-000178"]
message_sets: ["payments-initiation"]
role_labels: ["a non-financial institution customer", "agent", "an agent", "debtor", "initiating party", "next party in the payment chain", "non-financial institution customer", "the initiating party", "the next party in the payment chain"]
search_terms: ["a non-financial institution customer", "agent", "an agent", "debtor", "initiating party", "next party in the payment chain", "non-financial institution customer", "the initiating party", "the next party in the payment chain"]
participant_ids: ["participant-functionality-src-000174-agent", "participant-narrative-src-000174-next-party-in-the-payment-chain", "participant-narrative-src-000174-non-financial-institution-customer", "participant-src-000173-debtor", "participant-src-000173-initiating-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000174", "heading": "4 pain.007.001.13 CustomerPaymentReversalV13", "file_pages": [272, 402]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# pain.007.001.13 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 5 uniquely resolved participant references.

## src-000174 — 4 pain.007.001.13 CustomerPaymentReversalV13

[src-000174](../../../../../evidence/omitted/577241d5215d98d6ed689f57.md); Functionality file pp272; publication March 2026.

### Direction and initiation clauses

#### src-000174-pain.007.001.13-p272-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000174 file p272, scope.

- Sender: **the initiating party**. [the initiating party](../../../../../shared/reference/participants/participant-src-000173-initiating-party.md).
- Receiver: **the next party in the payment chain**. [the next party in the payment chain](../../../../../shared/reference/participants/participant-narrative-src-000174-next-party-in-the-payment-chain.md).

> The CustomerPaymentReversal message is sent by the initiating party to the next party in the payment chain.

#### src-000174-pain.007.001.13-p272-c002-d1

Kind: exchange-participants; message applicability: **current-message**; src-000174 file p272, usage.

- Exchange participants: **a non-financial institution customer and an agent**. [a non-financial institution customer](../../../../../shared/reference/participants/participant-narrative-src-000174-non-financial-institution-customer.md); [an agent](../../../../../shared/reference/participants/participant-functionality-src-000174-agent.md).

> The CustomerPaymentReversal message is exchanged between a non-financial institution customer and an agent to reverse a CustomerDirectDebitInitiation message that has been settled.

An exchange-between statement establishes participation, not sender/receiver direction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000174-pain.007.001.13-p272-c001 — file p272, scope.**

Mentioned roles: [initiating party](../../../../../shared/reference/participants/participant-src-000173-initiating-party.md); [next party in the payment chain](../../../../../shared/reference/participants/participant-narrative-src-000174-next-party-in-the-payment-chain.md).

Quoted above in src-000174-pain.007.001.13-p272-c001-d1.

**src-000174-pain.007.001.13-p272-c002 — file p272, usage.**

Mentioned roles: [non-financial institution customer](../../../../../shared/reference/participants/participant-narrative-src-000174-non-financial-institution-customer.md); [agent](../../../../../shared/reference/participants/participant-functionality-src-000174-agent.md).

Quoted above in src-000174-pain.007.001.13-p272-c002-d1.

**src-000174-pain.007.001.13-p272-c003 — file p272, usage.**

Mentioned roles: [debtor](../../../../../shared/reference/participants/participant-src-000173-debtor.md).

> The result will be a credit on the debtor account.

**src-000174-pain.007.001.13-p272-c004 — file p272, usage.**

> The CustomerPaymentReversal message refers to the original CustomerDirectDebitInitiation message by means of references only or by means of references and a set of elements from the original instruction.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p272, scope.**

> It is used to reverse a payment previously executed.

**File p272, usage.**

> The CustomerPaymentReversal message can be used in domestic and cross-border scenarios.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
