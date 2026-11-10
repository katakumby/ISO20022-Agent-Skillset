---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.010.001.09 participant and direction evidence"
domain: "payments"
message_id: "camt.010.001.09"
message_family: "camt.010"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.010.001.09"
source_ids: ["src-000015", "src-000024"]
message_sets: ["cash-management"]
role_labels: ["a member of the system", "member", "member of the system", "the transaction administrator", "transaction administrator"]
search_terms: ["a member of the system", "member", "member of the system", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "9 camt.010.001.09 ReturnLimitV09", "file_pages": [391, 421]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.010.001.09 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 3 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 9 camt.010.001.09 ReturnLimitV09

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp391, 392; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.010.001.09-p391-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p391, scope.

- Sender: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).
- Receiver: **a member of the system**. [a member of the system](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The ReturnLimit message is sent by the transaction administrator to a member of the system.

#### src-000015-camt.010.001.09-p391-c003-d1

Kind: initiator; message applicability: **current-message**; src-000015 file p391, scope.

- Initiator: **the transaction administrator (push mode)**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The ReturnLimit message can be sent as a response to a related GetLimit message (pull mode) or initiated by the transaction administrator (push mode).

#### src-000015-camt.010.001.09-p391-c005-d1

Kind: sender-only; message applicability: **current-message**; src-000015 file p391, usage.

- Sender: **transaction administrator**. [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The transaction administrator may also send a ReturnLimit message with pre-defined information at times previously agreed with the member or to warn the member about a particular problem that may have arisen and which needs attention.

Source explicitly names the sender. Scheduling, warning/preliminary usage and information content remain in the quote; no receiver is supplied by this clause.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.010.001.09-p391-c001 — file p391, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member of the system](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Quoted above in src-000015-camt.010.001.09-p391-c001-d1.

**src-000015-camt.010.001.09-p391-c002 — file p391, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator managed.

> It is used to provide information on the details of one or more limits set by the member (or on behalf of the member) and managed by the transaction administrator.

**src-000015-camt.010.001.09-p391-c003 — file p391, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator initiated.

Quoted above in src-000015-camt.010.001.09-p391-c003-d1.

**src-000015-camt.010.001.09-p391-c004 — file p391, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: transaction administrator manages.

> At any time during the operating hours of the system, the member can query the transaction administrator to get information about the limit(s) that the transaction administrator manages for the member.

**src-000015-camt.010.001.09-p391-c005 — file p391, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: transaction administrator send.

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000015-camt.010.001.09-p391-c005-d1.

**src-000015-camt.010.001.09-p391-c006 — file p391, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The message from the transaction administrator can contain information on the following elements:

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p391, scope.**

> The push of information can take place either at prearranged times or as a warning or alarm when a problem has occurred.

**File p391, usage.**

> type of risk and/or liquidity limit

**File p391, usage.**

> value of the limit(s) (default and/or current limit(s) for risk and/or liquidity management)

**File p391, usage.**

> identification of the system

**File p391, usage.**

> status of the limit(s) (default and/or current limit(s) for risk and/or liquidity management)

**File p391, usage.**

> point in time when the limit becomes effective

**File p391, usage.**

> identification of the counterparty Additional information on the generic design of the Get/Return messages can be found in the section How to Use the Cash Management Messages.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
