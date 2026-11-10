---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "secl.009.001.03 participant and direction evidence"
domain: "securities"
message_id: "secl.009.001.03"
message_family: "secl.009"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.009.001.03"
source_ids: ["src-000053", "src-000063"]
message_sets: ["ccp-clearing"]
role_labels: ["central counterparty (CCP)", "clearing member", "the central counterparty", "the clearing member"]
search_terms: ["central counterparty (CCP)", "clearing member", "the central counterparty", "the clearing member"]
participant_ids: ["participant-src-000052-central-counterparty", "participant-src-000052-individual-or-general-clearing-member"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000053", "heading": "10 MX secl.009.001.03 BuyInConfirmationV03", "file_pages": [294, 315]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# secl.009.001.03 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000053 — 10 MX secl.009.001.03 BuyInConfirmationV03

[src-000053](../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md); Functionality file pp294; publication March 2026; Standards MX November 2026 release.

### Direction and initiation clauses

#### src-000053-secl.009.001.03-p294-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000053 file p294, scope.

- Sender: **the central counterparty (CCP)**. [the central counterparty](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).
- Receiver: **the clearing member**. [the clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

> The Buy In Confirmation message is sent by the central counterparty (CCP) to the clearing member to confirm the details of the transaction resulting from the buy in.

#### src-000053-secl.009.001.03-p294-c002-d1

Kind: sender-only; message applicability: **current-message**; src-000053 file p294, usage.

- Sender: **the central counterparty (CCP)**. [the central counterparty](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).

> The Buy In Confirmation message is sent by the central counterparty (CCP) to confirm the details of the buy in transaction.

The clause supplies the sender and a purpose introduced by “to”; it does not explicitly name a receiver.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000053-secl.009.001.03-p294-c001 — file p294, scope.**

Mentioned roles: [central counterparty (CCP)](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md); [clearing member](../../../../../shared/reference/participants/participant-src-000052-individual-or-general-clearing-member.md).

Quoted above in src-000053-secl.009.001.03-p294-c001-d1.

**src-000053-secl.009.001.03-p294-c002 — file p294, usage.**

Mentioned roles: [central counterparty (CCP)](../../../../../shared/reference/participants/participant-src-000052-central-counterparty.md).

Quoted above in src-000053-secl.009.001.03-p294-c002-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p294, scope.**

> The message definition is intended for use with the ISO 20022 Business Application Header.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
