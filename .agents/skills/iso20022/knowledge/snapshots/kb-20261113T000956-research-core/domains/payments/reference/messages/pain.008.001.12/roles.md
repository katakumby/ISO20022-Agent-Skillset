---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "pain.008.001.12 participant and direction evidence"
domain: "payments"
message_id: "pain.008.001.12"
message_family: "pain.008"
namespace: "urn:iso:std:iso:20022:tech:xsd:pain.008.001.12"
source_ids: ["src-000174", "src-000179"]
message_sets: ["payments-initiation"]
role_labels: ["a forwarding agent", "account servicer", "corporate", "creditor", "creditor agent", "debtor", "financial institution", "forwarding agent", "initiating party", "payments factory", "the creditor agent", "the forwarding agent", "the initiating party"]
search_terms: ["a forwarding agent", "account servicer", "corporate", "creditor", "creditor agent", "debtor", "financial institution", "forwarding agent", "initiating party", "payments factory", "the creditor agent", "the forwarding agent", "the initiating party"]
participant_ids: ["participant-narrative-src-000174-corporate", "participant-narrative-src-000174-payments-factory", "participant-src-000173-account-servicer", "participant-src-000173-creditor", "participant-src-000173-creditor-agent", "participant-src-000173-debtor", "participant-src-000173-financial-institution", "participant-src-000173-forwarding-agent", "participant-src-000173-initiating-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000174", "heading": "5 pain.008.001.12 CustomerDirectDebitInitiationV12", "file_pages": [403, 526]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# pain.008.001.12 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 5 direction/initiator/exchange clauses; 9 uniquely resolved participant references.

## src-000174 — 5 pain.008.001.12 CustomerDirectDebitInitiationV12

[src-000174](../../../../../evidence/omitted/577241d5215d98d6ed689f57.md); Functionality file pp403; publication March 2026.

### Direction and initiation clauses

#### src-000174-pain.008.001.12-p403-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000174 file p403, scope.

- Sender: **the initiating party**. [the initiating party](../../../../../shared/reference/participants/participant-src-000173-initiating-party.md).
- Receiver: **the forwarding agent or creditor agent**. [the forwarding agent](../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md); [creditor agent](../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md).

> The CustomerDirectDebitInitiation message is sent by the initiating party to the forwarding agent or creditor agent.

#### src-000174-pain.008.001.12-p403-c004-d1

Kind: receiver-only; message applicability: **current-message**; src-000174 file p403, usage.

- Receiver: **the creditor agent**. [the creditor agent](../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md).

> In a direct scenario, the message is sent directly to the creditor agent.

Sender is not supplied by this clause; pronouns or scenario context are not expanded.

#### src-000174-pain.008.001.12-p403-c006-d1

Kind: receiver-only; message applicability: **current-message**; src-000174 file p403, usage.

- Receiver: **a forwarding agent**. [a forwarding agent](../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md).

> In a relay scenario, the message is sent to a forwarding agent.

Sender is not supplied by this clause; pronouns or scenario context are not expanded.

#### src-000174-pain.008.001.12-p403-c008-d1

Kind: receiver-only; message applicability: **current-message**; src-000174 file p403, usage.

- Receiver: **the creditor agent**. [the creditor agent](../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md).

> It will forward the CustomerDirectDebitInitiation message to the creditor agent.

Sender is a pronoun/reference in this clause; it is retained in the quote and is not resolved automatically.

#### src-000174-pain.008.001.12-p403-c009-d1

Kind: sender-only; message applicability: **current-message**; src-000174 file p403, usage.

- Sender: **initiating party**. [initiating party](../../../../../shared/reference/participants/participant-src-000173-initiating-party.md).

> The message can also be used by an initiating party that has authority to send the message on behalf of the creditor.

Conditional authorized use: the initiating party has authority to send on behalf of the creditor. The principal is not thereby equated with the functional sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000174-pain.008.001.12-p403-c001 — file p403, scope.**

Mentioned roles: [initiating party](../../../../../shared/reference/participants/participant-src-000173-initiating-party.md); [forwarding agent](../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md); [creditor agent](../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md).

Quoted above in src-000174-pain.008.001.12-p403-c001-d1.

**src-000174-pain.008.001.12-p403-c002 — file p403, scope.**

Mentioned roles: [debtor](../../../../../shared/reference/participants/participant-src-000173-debtor.md); [creditor](../../../../../shared/reference/participants/participant-src-000173-creditor.md).

> It is used to request single or bulk collection(s) of funds from one or various debtor's account(s) for a creditor.

**src-000174-pain.008.001.12-p403-c003 — file p403, usage.**

> The CustomerDirectDebitInitiation message can contain one or more direct debit instructions.

**src-000174-pain.008.001.12-p403-c004 — file p403, usage.**

Mentioned roles: [creditor agent](../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md).

Quoted above in src-000174-pain.008.001.12-p403-c004-d1.

**src-000174-pain.008.001.12-p403-c005 — file p403, usage.**

Mentioned roles: [creditor agent](../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md); [account servicer](../../../../../shared/reference/participants/participant-src-000173-account-servicer.md); [creditor](../../../../../shared/reference/participants/participant-src-000173-creditor.md).

> The creditor agent is the account servicer of the creditor.

**src-000174-pain.008.001.12-p403-c006 — file p403, usage.**

Mentioned roles: [forwarding agent](../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md).

Quoted above in src-000174-pain.008.001.12-p403-c006-d1.

**src-000174-pain.008.001.12-p403-c007 — file p403, usage.**

Mentioned roles: [forwarding agent](../../../../../shared/reference/participants/participant-src-000173-forwarding-agent.md); [financial institution](../../../../../shared/reference/participants/participant-src-000173-financial-institution.md).

Literal actions: forwarding agent acts.

> The forwarding agent acts as a concentrating financial institution.

**src-000174-pain.008.001.12-p403-c008 — file p403, usage.**

Mentioned roles: [creditor agent](../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md).

Quoted above in src-000174-pain.008.001.12-p403-c008-d1.

**src-000174-pain.008.001.12-p403-c009 — file p403, usage.**

Mentioned roles: [initiating party](../../../../../shared/reference/participants/participant-src-000173-initiating-party.md); [creditor](../../../../../shared/reference/participants/participant-src-000173-creditor.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000174-pain.008.001.12-p403-c009-d1.

**src-000174-pain.008.001.12-p403-c010 — file p403, usage.**

Mentioned roles: [payments factory](../../../../../shared/reference/participants/participant-narrative-src-000174-payments-factory.md); [corporate](../../../../../shared/reference/participants/participant-narrative-src-000174-corporate.md).

> This caters for example for the scenario of a payments factory initiating all payments on behalf of a large corporate.

**src-000174-pain.008.001.12-p403-c011 — file p403, usage.**

Mentioned roles: [creditor agent](../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md).

> The CustomerDirectDebitInitiation message must not be used by the creditor agent to execute the direct debit instruction(s).

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p403, usage.**

> The message can be used in a direct or a relay scenario:

**File p403, usage.**

> The CustomerDirectDebitInitiation message can be used in domestic and cross-border scenarios.

**File p403, usage.**

> The CustomerDirectDebitInitiation may or may not contain mandate related information, i.e. extracts from a mandate, such as MandateIdentification or DateOfSignature.

**File p403, usage.**

> The CustomerDirectDebitInitiation message must not be considered as a mandate.

**File p403, usage.**

> The FIToFICustomerDirectDebit message must be used instead.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
