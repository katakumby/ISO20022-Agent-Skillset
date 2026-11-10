---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.047.001.08 participant and direction evidence"
domain: "payments"
message_id: "camt.047.001.08"
message_family: "camt.047"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.047.001.08"
source_ids: ["src-000015", "src-000040"]
message_sets: ["cash-management"]
role_labels: ["a member", "member", "the member", "The transaction administrator", "the transaction administrator", "transaction administrator"]
search_terms: ["a member", "member", "the member", "The transaction administrator", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "25 camt.047.001.08 ReturnReservationV08", "file_pages": [636, 653]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.047.001.08 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 3 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 25 camt.047.001.08 ReturnReservationV08

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); Functionality file pp636; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.047.001.08-p636-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p636, scope.

- Sender: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).
- Receiver: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The ReturnReservation message is sent by the transaction administrator to a member.

#### src-000015-camt.047.001.08-p636-c003-d1

Kind: initiator; message applicability: **current-message**; src-000015 file p636, scope.

- Initiator: **the transaction administrator (push mode)**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The ReturnReservation message can be sent as a response to a related Get Reservation message (pull mode) or initiated by the transaction administrator (push mode).

#### src-000015-camt.047.001.08-p636-c005-d1

Kind: sender-to-receiver; message applicability: **related-or-unspecified-message**; src-000015 file p636, usage.

- Sender: **The transaction administrator**. [The transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).
- Receiver: **the member**. [the member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The transaction administrator will send reservations information to the member based on the following elements:

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.047.001.08-p636-c001 — file p636, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Quoted above in src-000015-camt.047.001.08-p636-c001-d1.

**src-000015-camt.047.001.08-p636-c002 — file p636, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator managed.

> It is used to provide information on the details of one or more reservation facilities set by the member and managed by the transaction administrator.

**src-000015-camt.047.001.08-p636-c003 — file p636, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator initiated.

Quoted above in src-000015-camt.047.001.08-p636-c003-d1.

**src-000015-camt.047.001.08-p636-c004 — file p636, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: transaction administrator manages.

> At any time during the operating hours of the system, the member can query the transaction administrator to get information about the reservations facilities that the transaction administrator manages for the member.

**src-000015-camt.047.001.08-p636-c005 — file p636, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: transaction administrator send.

Quoted above in src-000015-camt.047.001.08-p636-c005-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p636, scope.**

> The push of information can take place either at prearranged times or as a warning or alarm when a problem has occurred.

**File p636, usage.**

> identification of the system

**File p636, usage.**

> identification of the account

**File p636, usage.**

> status of the reservation (default and/or current )

**File p636, usage.**

> type of reservation.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
