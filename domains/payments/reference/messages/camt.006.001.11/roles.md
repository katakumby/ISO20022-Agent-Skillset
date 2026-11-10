---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.006.001.11 participant and direction evidence"
domain: "payments"
message_id: "camt.006.001.11"
message_family: "camt.006"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.006.001.11"
source_ids: ["src-000015", "src-000020"]
message_sets: ["cash-management"]
role_labels: ["a member of the system", "member", "member of the system", "Members of a system", "the transaction administrator", "transaction administrator"]
search_terms: ["a member of the system", "member", "member of the system", "Members of a system", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "5 camt.006.001.11 ReturnTransactionV11", "file_pages": [206, 325]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.006.001.11 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 3 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 5 camt.006.001.11 ReturnTransactionV11

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); Functionality file pp206, 207, 208; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.006.001.11-p206-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p206, scope.

- Sender: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).
- Receiver: **a member of the system**. [a member of the system](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The ReturnTransaction message is sent by the transaction administrator to a member of the system.

#### src-000015-camt.006.001.11-p206-c003-d1

Kind: initiator; message applicability: **current-message**; src-000015 file p206, scope.

- Initiator: **the transaction administrator (push mode)**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The Return Transaction message can be sent as a response to a related GetTransaction message (pull mode) or initiated by the transaction administrator (push mode).

#### src-000015-camt.006.001.11-p206-c010-d1

Kind: sender-only; message applicability: **current-message**; src-000015 file p206, usage.

- Sender: **transaction administrator**. [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The transaction administrator may also send a ReturnTransaction message with pre-defined information at times previously agreed with the member or to warn the member about a particular problem that may have arisen and which needs attention.

Source explicitly names the sender. Scheduling, warning/preliminary usage and information content remain in the quote; no receiver is supplied by this clause.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.006.001.11-p206-c001 — file p206, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member of the system](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Quoted above in src-000015-camt.006.001.11-p206-c001-d1.

**src-000015-camt.006.001.11-p206-c002 — file p206, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> It is used to provide information on transactions and booked entries held at the transaction administrator.

**src-000015-camt.006.001.11-p206-c003 — file p206, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator initiated.

Quoted above in src-000015-camt.006.001.11-p206-c003-d1.

**src-000015-camt.006.001.11-p206-c004 — file p206, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> Following normal business flows, transactions registered by the transaction administrator may be queued for later settlement (because of insufficient funds available, because of risk or liquidity limits, etc.).

**src-000015-camt.006.001.11-p206-c005 — file p206, usage.**

Mentioned roles: [Members of a system](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: Members of a system need to receive.

Reviewed clause disposition: **source-explicit-role-action**. The actor and action are named in this sentence; the action object and conditions are retained and are not automatically the indexed message.

> Members of a system need to receive information about the payments queue(s) and must have the ability to take action (that is, cancel or modify the transaction(s) to be settled).

**src-000015-camt.006.001.11-p206-c006 — file p206, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> Note, however, that actions by a member will always concern transactions in a transient status.

**src-000015-camt.006.001.11-p206-c007 — file p206, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> At any time during operating hours of the system, the member can query the transaction administrator to get information about transactions, whatever their status.

**src-000015-camt.006.001.11-p206-c008 — file p206, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: member request.

> The member can request information about transactions through a series of criteria, corresponding to the known information stored within the transaction administrator.

**src-000015-camt.006.001.11-p206-c009 — file p206, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator selects and reports.

Reviewed clause disposition: **source-explicit-role-action**. The actor and action are named in this sentence; the action object and conditions are retained and are not automatically the indexed message.

> Based on the criteria received within the request, the transaction administrator will select items that match the request and report them to the requester.

**src-000015-camt.006.001.11-p206-c010 — file p206, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: transaction administrator send.

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000015-camt.006.001.11-p206-c010-d1.

**src-000015-camt.006.001.11-p206-c011 — file p206, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The message from the transaction administrator can contain information based on the following elements:

**src-000015-camt.006.001.11-p206-c012 — file p206, usage.**

> payment instruction reference Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11 Cash Management - Maintenance 2024 - 2025 206 February 2025

**src-000015-camt.006.001.11-p206-c013 — file p207, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> payment instruction status, as registered at the transaction administrator

**src-000015-camt.006.001.11-p206-c014 — file p207, usage.**

> instructed amount and/or currency

**src-000015-camt.006.001.11-p206-c015 — file p207, usage.**

> credit/debit indicator of the payment instruction/transaction

**src-000015-camt.006.001.11-p206-c016 — file p207, usage.**

> message used for the payment instruction

**src-000015-camt.006.001.11-p206-c017 — file p207, usage.**

> period in which the payment instruction should be processed (processing validity time)

**src-000015-camt.006.001.11-p206-c018 — file p207, usage.**

> instructions given, related to the processing of the transaction

**src-000015-camt.006.001.11-p206-c019 — file p207, usage.**

> type of payment instructed

**src-000015-camt.006.001.11-p206-c020 — file p207, usage.**

> details related to the status of the payment instruction An element that is particular to the Get/Return Transaction pair is the Statement Report.

**src-000015-camt.006.001.11-p206-c021 — file p207, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> When a GetTransaction message is sent requesting a statement report, the related ReturnTransaction message will provide a pre-defined set of return criteria per transaction.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p206, scope.**

> The push of information can take place either at prearranged times or as a warning or alarm when a problem has occurred.

**File p206, usage.**

> A transaction may have a series of statuses.

**File p206, usage.**

> These can be transient (such as pending or related types) and final (such as rejected or settled).

**File p206, usage.**

> These requests will concern either all transactions, all transactions within a particular status or a specific transaction.

**File p206, usage.**

> provenance or destination of the payment (payment to/payment from)

**File p206, usage.**

> transaction reference

**File p206, usage.**

> transfer value date

**File p207, usage.**

> interbank settlement amount and/or currency

**File p207, usage.**

> priority of the payment transaction

**File p207, usage.**

> account identification (entries booked to a specific account)

**File p207, usage.**

> entry amount and/or currency

**File p207, usage.**

> entry debit/credit indicator (if absent, all entries should be reported)

**File p207, usage.**

> status of the entry (pending, booked.)

**File p207, usage.**

> entry date and time

**File p207, usage.**

> currency of the account

**File p207, usage.**

> type of the account

**File p207, usage.**

> entry reference

**File p207, usage.**

> entry date

**File p207, usage.**

> transfer reason

**File p207, usage.**

> The information returned contains the following details for each transaction:

**File p207, usage.**

> value date

**File p207, usage.**

> entry date

**File p207, usage.**

> debit/credit code

**File p207, usage.**

> entry amount

**File p207, usage.**

> method of payment (payment instrument or message type)

**File p207, usage.**

> entry reference Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11 Cash Management - Maintenance 2024 - 2025 207 February 2025

**File p208, usage.**

> transaction reference

**File p208, usage.**

> supplementary details Additional information on the generic design of the Get/Return messages can be found in the section How to Use the Cash Management Messages.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
