---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.046.001.08 participant and direction evidence"
domain: "payments"
message_id: "camt.046.001.08"
message_family: "camt.046"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.046.001.08"
source_ids: ["src-000015", "src-000039"]
message_sets: ["cash-management"]
role_labels: ["a member", "member", "the transaction administrator", "transaction administrator"]
search_terms: ["a member", "member", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "24 camt.046.001.08 GetReservationV08", "file_pages": [624, 635]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.046.001.08 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 24 camt.046.001.08 GetReservationV08

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp624; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.046.001.08-p624-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p624, scope.

- Sender: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).
- Receiver: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The GetReservation message is sent by a member to the transaction administrator.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.046.001.08-p624-c001 — file p624, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Quoted above in src-000015-camt.046.001.08-p624-c001-d1.

**src-000015-camt.046.001.08-p624-c002 — file p624, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator managed.

> It is used to request information on the details of one or more reservation facilities set by the member and managed by the transaction administrator.

**src-000015-camt.046.001.08-p624-c003 — file p624, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member request.

> The member can request reservations information based on the following elements:

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p624, usage.**

> identification of the system;

**File p624, usage.**

> identification of the account;

**File p624, usage.**

> status of the reservation (default and/or current);

**File p624, usage.**

> type of reservation.

**File p624, usage.**

> This message will be replied to by a ReturnReservation message.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
