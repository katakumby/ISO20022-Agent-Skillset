---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "pain.001.001.13 participant and direction evidence"
domain: "payments"
message_id: "pain.001.001.13"
message_family: "pain.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:pain.001.001.13"
source_ids: ["src-000174", "src-000176"]
message_sets: ["payments-initiation"]
role_labels: ["a forwarding agent", "account servicer", "corporate", "creditor", "customer", "debtor", "debtor agent", "financial institution", "forwarding agent", "initiating party", "payments factory", "the debtor agent", "the forwarding agent", "the initiating party"]
search_terms: ["a forwarding agent", "account servicer", "corporate", "creditor", "customer", "debtor", "debtor agent", "financial institution", "forwarding agent", "initiating party", "payments factory", "the debtor agent", "the forwarding agent", "the initiating party"]
participant_ids: ["participant-narrative-src-000174-corporate", "participant-narrative-src-000174-customer", "participant-narrative-src-000174-payments-factory", "participant-src-000173-account-servicer", "participant-src-000173-creditor", "participant-src-000173-debtor", "participant-src-000173-debtor-agent", "participant-src-000173-financial-institution", "participant-src-000173-forwarding-agent", "participant-src-000173-initiating-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000174", "heading": "2 pain.001.001.13 CustomerCreditTransferInitiationV13", "file_pages": [4, 129]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# pain.001.001.13 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 5 direction/initiator/exchange clauses; 10 uniquely resolved participant references.

## src-000174 — 2 pain.001.001.13 CustomerCreditTransferInitiationV13

[src-000174](../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf); Functionality file pp4, 5; publication March 2026.

### Direction and initiation clauses

#### src-000174-pain.001.001.13-p4-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000174 file p4, scope.

- Sender: **the initiating party**. [the initiating party](../../../../../shared/reference/participants/participant-src-000173-initiating-party.md).
- Receiver: **the forwarding agent or debtor agent**. [the forwarding agent](../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md); [debtor agent](../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md).

> The CustomerCreditTransferInitiation message is sent by the initiating party to the forwarding agent or debtor agent.

#### src-000174-pain.001.001.13-p4-c006-d1

Kind: receiver-only; message applicability: **current-message**; src-000174 file p4, usage.

- Receiver: **the debtor agent**. [the debtor agent](../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md).

> In a direct scenario, the message is sent directly to the debtor agent.

Sender is not supplied by this clause; pronouns or scenario context are not expanded.

#### src-000174-pain.001.001.13-p4-c008-d1

Kind: receiver-only; message applicability: **current-message**; src-000174 file p4, usage.

- Receiver: **a forwarding agent**. [a forwarding agent](../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md).

> In a relay scenario, the message is sent to a forwarding agent.

Sender is not supplied by this clause; pronouns or scenario context are not expanded.

#### src-000174-pain.001.001.13-p4-c010-d1

Kind: receiver-only; message applicability: **current-message**; src-000174 file p4, usage.

- Receiver: **the debtor agent**. [the debtor agent](../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md).

> It will forward the CustomerCreditTransferInitiation message to the debtor agent.

Sender is a pronoun/reference in this clause; it is retained in the quote and is not resolved automatically.

#### src-000174-pain.001.001.13-p4-c011-d1

Kind: sender-only; message applicability: **current-message**; src-000174 file p4, usage.

- Sender: **initiating party**. [initiating party](../../../../../shared/reference/participants/participant-src-000173-initiating-party.md).

> The message can also be used by an initiating party that has authority to send the message on behalf of the debtor.

Conditional authorized use: the initiating party has authority to send on behalf of the debtor. The principal is not thereby equated with the functional sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000174-pain.001.001.13-p4-c001 — file p4, scope.**

Mentioned roles: [initiating party](../../../../../shared/reference/participants/participant-src-000173-initiating-party.md); [forwarding agent](../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md); [debtor agent](../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md).

Quoted above in src-000174-pain.001.001.13-p4-c001-d1.

**src-000174-pain.001.001.13-p4-c002 — file p4, scope.**

Mentioned roles: [debtor](../../../../../shared/reference/participants/participant-src-000173-debtor.md); [creditor](../../../../../shared/reference/participants/participant-src-000173-creditor.md).

> It is used to request movement of funds from the debtor account to a creditor.

**src-000174-pain.001.001.13-p4-c003 — file p4, usage.**

Mentioned roles: [customer](../../../../../shared/reference/participants/participant-narrative-src-000174-customer.md).

> The CustomerCreditTransferInitiation message can contain one or more customer credit transfer instructions.

**src-000174-pain.001.001.13-p4-c004 — file p4, usage.**

Mentioned roles: [debtor agent](../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md); [financial institution](../../../../../shared/reference/participants/participant-src-000173-financial-institution.md).

> Payment transactions that result in book transfers at the debtor agent or payments to another financial institution;

**src-000174-pain.001.001.13-p4-c005 — file p4, usage.**

Mentioned roles: [creditor](../../../../../shared/reference/participants/participant-src-000173-creditor.md).

> Payment transactions that result in an electronic cash transfer to the creditor account or in the emission of a cheque.

**src-000174-pain.001.001.13-p4-c006 — file p4, usage.**

Mentioned roles: [debtor agent](../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md).

Quoted above in src-000174-pain.001.001.13-p4-c006-d1.

**src-000174-pain.001.001.13-p4-c007 — file p4, usage.**

Mentioned roles: [debtor agent](../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md); [account servicer](../../../../../shared/reference/participants/participant-src-000173-account-servicer.md); [debtor](../../../../../shared/reference/participants/participant-src-000173-debtor.md).

> The debtor agent is the account servicer of the debtor.

**src-000174-pain.001.001.13-p4-c008 — file p4, usage.**

Mentioned roles: [forwarding agent](../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md).

Quoted above in src-000174-pain.001.001.13-p4-c008-d1.

**src-000174-pain.001.001.13-p4-c009 — file p4, usage.**

Mentioned roles: [forwarding agent](../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md); [financial institution](../../../../../shared/reference/participants/participant-src-000173-financial-institution.md).

Literal actions: forwarding agent acts.

> The forwarding agent acts as a concentrating financial institution.

**src-000174-pain.001.001.13-p4-c010 — file p4, usage.**

Mentioned roles: [debtor agent](../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md).

Quoted above in src-000174-pain.001.001.13-p4-c010-d1.

**src-000174-pain.001.001.13-p4-c011 — file p4, usage.**

Mentioned roles: [initiating party](../../../../../shared/reference/participants/participant-src-000173-initiating-party.md); [debtor](../../../../../shared/reference/participants/participant-src-000173-debtor.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000174-pain.001.001.13-p4-c011-d1.

**src-000174-pain.001.001.13-p4-c012 — file p4, usage.**

Mentioned roles: [payments factory](../../../../../shared/reference/participants/participant-narrative-src-000174-payments-factory.md); [corporate](../../../../../shared/reference/participants/participant-narrative-src-000174-corporate.md).

> This caters for example for the scenario of a payments factory initiating all payments on behalf of a large corporate.

**src-000174-pain.001.001.13-p4-c013 — file p4, usage.**

Mentioned roles: [debtor agent](../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md).

> The CustomerCreditTransferInitiation message must not be used by the debtor agent to execute the credit transfer instruction(s).

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p4, usage.**

> The CustomerCreditTransferInitiation message is used to exchange:

**File p4, usage.**

> One or more instances of a credit transfer initiation;

**File p4, usage.**

> The message can be used in a direct or a relay scenario:

**File p4, usage.**

> The CustomerCreditTransferInitiation message can be used in domestic and cross-border scenarios.

**File p4, usage.**

> The FIToFICustomerCreditTransfer message must be used instead.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
