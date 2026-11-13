---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.005.001.11 participant and direction evidence"
domain: "payments"
message_id: "camt.005.001.11"
message_family: "camt.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11"
source_ids: ["src-000015", "src-000019"]
message_sets: ["cash-management"]
role_labels: ["a member", "member", "Members of a system", "the transaction administrator", "transaction administrator"]
search_terms: ["a member", "member", "Members of a system", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "4 camt.005.001.11 GetTransactionV11", "file_pages": [98, 205]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.005.001.11 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 3 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 4 camt.005.001.11 GetTransactionV11

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp98, 99; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.005.001.11-p98-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p98, scope.

- Sender: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).
- Receiver: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The GetTransaction message is sent by a member to the transaction administrator.

#### src-000015-camt.005.001.11-p98-c003-d1

Kind: sender-only; message applicability: **related-payment-instructions**; src-000015 file p98, scope.

- Sender: **member**. [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> Payment instructions are either sent by the member, debiting or crediting its account at the transaction administrator or received by the transaction administrator, crediting or debiting the member's account.

The source discusses payment instructions, not the indexed GetTransaction query.

#### src-000015-camt.005.001.11-p98-c003-d2

Kind: receiver-only; message applicability: **related-payment-instructions**; src-000015 file p98, scope.

- Receiver: **transaction administrator**. [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> Payment instructions are either sent by the member, debiting or crediting its account at the transaction administrator or received by the transaction administrator, crediting or debiting the member's account.

The source alternative describes receipt of payment instructions. It does not supply the sender of that alternative or the query direction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.005.001.11-p98-c001 — file p98, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Quoted above in src-000015-camt.005.001.11-p98-c001-d1.

**src-000015-camt.005.001.11-p98-c002 — file p98, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> It is used to request information about payment instructions held at the transaction administrator.

**src-000015-camt.005.001.11-p98-c003 — file p98, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: transaction administrator received.

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000015-camt.005.001.11-p98-c003-d1, src-000015-camt.005.001.11-p98-c003-d2.

**src-000015-camt.005.001.11-p98-c004 — file p98, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> Following normal business flows, transactions registered by the transaction administrator may be queued for later settlement (because of insufficient funds available, or because of risk or liquidity limits, etc.).

**src-000015-camt.005.001.11-p98-c005 — file p98, usage.**

Mentioned roles: [Members of a system](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> Members of a system need to have information about the payments queue(s) and must have the ability to take action (that is, to cancel or modify the transaction(s) to be settled).

**src-000015-camt.005.001.11-p98-c006 — file p98, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> Note, however, that actions by a member will always concern transactions in a transient status.

**src-000015-camt.005.001.11-p98-c007 — file p98, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> At any time during the operating hours of the system, the member can query the transaction administrator to get information about transactions, whatever their status.

**src-000015-camt.005.001.11-p98-c008 — file p98, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: member request.

> The member can request information about transactions through a series of criteria, corresponding to the known information stored at the transaction administrator, based on the following elements:

**src-000015-camt.005.001.11-p98-c009 — file p98, usage.**

> payment instruction reference

**src-000015-camt.005.001.11-p98-c010 — file p98, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> payment instruction status, as registered at the transaction administrator

**src-000015-camt.005.001.11-p98-c011 — file p98, usage.**

> instructed amount and/or currency

**src-000015-camt.005.001.11-p98-c012 — file p98, usage.**

> credit/debit indicator of the payment instruction/transaction

**src-000015-camt.005.001.11-p98-c013 — file p98, usage.**

> SWIFT FIN payment message used for the payment instruction

**src-000015-camt.005.001.11-p98-c014 — file p99, usage.**

> period in which the payment instruction should be processed (processing validity time)

**src-000015-camt.005.001.11-p98-c015 — file p99, usage.**

> instructions given, related to the processing of the transaction

**src-000015-camt.005.001.11-p98-c016 — file p99, usage.**

> type of payment instructed

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p98, usage.**

> A transaction may have a series of statuses.

**File p98, usage.**

> These can be transient (such as pending or related types) and final (such as rejected, revoked and/or settled).

**File p98, usage.**

> These requests will concern either all transactions, all transactions with a particular status or a specific transaction.

**File p98, usage.**

> provenance or destination of the payment (payment to/payment from)

**File p98, usage.**

> transaction reference

**File p98, usage.**

> transfer value date

**File p98, usage.**

> interbank settlement amount and/or currency

**File p98, usage.**

> priority of the payment transaction Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11 Cash Management - Maintenance 2024 - 2025 98 February 2025

**File p99, usage.**

> account identification (entries booked to a specific account)

**File p99, usage.**

> entry amount and/or currency

**File p99, usage.**

> entry debit/credit indicator (if absent, all entries should be reported).

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
