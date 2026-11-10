---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.025.001.09 participant and direction evidence"
domain: "payments"
message_id: "camt.025.001.09"
message_family: "camt.025"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.025.001.09"
source_ids: ["src-000015", "src-000038"]
message_sets: ["cash-management"]
role_labels: ["a message recipient", "message recipient", "message sender", "the message sender"]
search_terms: ["a message recipient", "message recipient", "message sender", "the message sender"]
participant_ids: ["participant-functionality-src-000015-recipient", "participant-functionality-src-000015-sender"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "23 camt.025.001.09 ReceiptV09", "file_pages": [604, 623]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.025.001.09 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 23 camt.025.001.09 ReceiptV09

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp604; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.025.001.09-p604-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p604, scope.

- Sender: **a message recipient**. [a message recipient](../../../../../shared/reference/participants/participant-functionality-src-000015-recipient.md).
- Receiver: **the message sender**. [the message sender](../../../../../shared/reference/participants/participant-functionality-src-000015-sender.md).

> The Receipt message is sent by a message recipient to the message sender.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.025.001.09-p604-c001 — file p604, scope.**

Mentioned roles: [message recipient](../../../../../shared/reference/participants/participant-functionality-src-000015-recipient.md); [message sender](../../../../../shared/reference/participants/participant-functionality-src-000015-sender.md).

Quoted above in src-000015-camt.025.001.09-p604-c001-d1.

**src-000015-camt.025.001.09-p604-c002 — file p604, scope.**

Reviewed clause disposition: **usage-condition-or-related-message-context**. The sentence supplies purpose, response linkage, timing, content, status or a condition. It does not independently identify an additional complete current-message sender/receiver direction. Its full literal wording remains available.

> It is sent to acknowledge the receipt of one or multiple messages sent previously.

**src-000015-camt.025.001.09-p604-c003 — file p604, usage.**

Mentioned roles: [message sender](../../../../../shared/reference/participants/participant-functionality-src-000015-sender.md).

> This may happen, for instance, when an action is requested from the message sender (a deletion, modification or cancellation).

**src-000015-camt.025.001.09-p604-c004 — file p604, usage.**

Mentioned roles: [message sender](../../../../../shared/reference/participants/participant-functionality-src-000015-sender.md).

> The message sender will first acknowledge the request (with a Receipt message) and then execute it.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p604, scope.**

> The Receipt message is an application receipt acknowledgement and conveys information about the processing of the original message(s).

**File p604, usage.**

> The Receipt message is used when the exchange of messages takes place in an asynchronous manner.

**File p604, usage.**

> The message can contain information based on the following elements: reference of the message(s) it acknowledges, the status code (optional) and further explanation:

**File p604, usage.**

> reference of the message it acknowledges

**File p604, usage.**

> potentially, a status code and status reason information.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
