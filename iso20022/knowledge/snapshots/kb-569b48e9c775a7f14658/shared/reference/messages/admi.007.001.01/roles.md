---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "admi.007.001.01 participant and direction evidence"
domain: "shared"
message_id: "admi.007.001.01"
message_family: "admi.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:admi.007.001.01"
source_ids: ["src-000233", "src-000239", "src-000344"]
message_sets: ["t2s", "t2s-administration"]
role_labels: ["a member of the system", "member of the system", "the transaction administrator", "transaction administrator"]
search_terms: ["a member of the system", "member of the system", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000344-member", "participant-narrative-src-000344-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "4 admi.007.001.01 ReceiptAcknowledgementV01", "file_pages": [62, 67]}, {"source_id": "src-000344", "heading": "4 admi.007.001.01 ReceiptAcknowledgementV01", "file_pages": [32, 37]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# admi.007.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 4 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000233 — 4 admi.007.001.01 ReceiptAcknowledgementV01

[src-000233](../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp62; publication August 2026.

### Direction and initiation clauses

#### src-000233-admi.007.001.01-p62-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p62, scope.

- Sender: **the transaction administrator**. [the transaction administrator](../../participants/participant-narrative-src-000344-transaction-administrator.md).
- Receiver: **a member of the system and vice versa**. [a member of the system](../../participants/participant-narrative-src-000344-member.md).

> The ReceiptAcknowledgement message is sent by the transaction administrator to a member of the system and vice versa.

#### src-000233-admi.007.001.01-p62-c001-d2

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p62, scope.

- Sender: **a member of the system and vice versa**. [a member of the system](../../participants/participant-narrative-src-000344-member.md).
- Receiver: **the transaction administrator**. [the transaction administrator](../../participants/participant-narrative-src-000344-transaction-administrator.md).

> The ReceiptAcknowledgement message is sent by the transaction administrator to a member of the system and vice versa.

The source explicitly adds “and vice versa”; the two directed claims retain this reciprocal usage.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-admi.007.001.01-p62-c001 — file p62, scope.**

Mentioned roles: [transaction administrator](../../participants/participant-narrative-src-000344-transaction-administrator.md); [member of the system](../../participants/participant-narrative-src-000344-member.md).

Quoted above in src-000233-admi.007.001.01-p62-c001-d1, src-000233-admi.007.001.01-p62-c001-d2.

**src-000233-admi.007.001.01-p62-c002 — file p62, scope.**

Reviewed clause disposition: **usage-condition-or-related-message-context**. The sentence supplies purpose, response linkage, timing, content, status or a condition. It does not independently identify an additional complete current-message sender/receiver direction. Its full literal wording remains available.

> It is sent to acknowledge the receipt of one or multiple messages sent previously.

**src-000233-admi.007.001.01-p62-c003 — file p62, scope.**

> In case of 2) the ReceiptAcknowledgement can be used as a Generic error message, which provides information about the status (e.g. rejection, acceptance) of an instruction.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p62, scope.**

> The Acknowledgement message is 1) an application receipt acknowledgement and 2) conveys information about the processing of the original message(s).

## src-000344 — 4 admi.007.001.01 ReceiptAcknowledgementV01

[src-000344](../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`; Functionality file pp32; publication march-2024.

### Direction and initiation clauses

#### src-000344-admi.007.001.01-p32-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000344 file p32, scope.

- Sender: **the transaction administrator**. [the transaction administrator](../../participants/participant-narrative-src-000344-transaction-administrator.md).
- Receiver: **a member of the system and vice versa**. [a member of the system](../../participants/participant-narrative-src-000344-member.md).

> The ReceiptAcknowledgement message is sent by the transaction administrator to a member of the system and vice versa.

#### src-000344-admi.007.001.01-p32-c001-d2

Kind: sender-to-receiver; message applicability: **current-message**; src-000344 file p32, scope.

- Sender: **a member of the system and vice versa**. [a member of the system](../../participants/participant-narrative-src-000344-member.md).
- Receiver: **the transaction administrator**. [the transaction administrator](../../participants/participant-narrative-src-000344-transaction-administrator.md).

> The ReceiptAcknowledgement message is sent by the transaction administrator to a member of the system and vice versa.

The source explicitly adds “and vice versa”; the two directed claims retain this reciprocal usage.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000344-admi.007.001.01-p32-c001 — file p32, scope.**

Mentioned roles: [transaction administrator](../../participants/participant-narrative-src-000344-transaction-administrator.md); [member of the system](../../participants/participant-narrative-src-000344-member.md).

Quoted above in src-000344-admi.007.001.01-p32-c001-d1, src-000344-admi.007.001.01-p32-c001-d2.

**src-000344-admi.007.001.01-p32-c002 — file p32, scope.**

Reviewed clause disposition: **usage-condition-or-related-message-context**. The sentence supplies purpose, response linkage, timing, content, status or a condition. It does not independently identify an additional complete current-message sender/receiver direction. Its full literal wording remains available.

> It is sent to acknowledge the receipt of one or multiple messages sent previously.

**src-000344-admi.007.001.01-p32-c003 — file p32, scope.**

> In case of 2) the ReceiptAcknowledgement can be used as a Generic error message, which provides information about the status (e.g. rejection, acceptance) of an instruction.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p32, scope.**

> The Acknowledgement message is 1) an application receipt acknowledgement and 2) conveys information about the processing of the original message(s).

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../tracking/issues.md)
