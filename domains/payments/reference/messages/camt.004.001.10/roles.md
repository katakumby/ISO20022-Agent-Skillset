---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.004.001.10 participant and direction evidence"
domain: "payments"
message_id: "camt.004.001.10"
message_family: "camt.004"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.004.001.10"
source_ids: ["src-000015", "src-000018"]
message_sets: ["cash-management"]
role_labels: ["a member", "member", "the transaction administrator", "transaction administrator"]
search_terms: ["a member", "member", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "3 camt.004.001.10 ReturnAccountV10", "file_pages": [48, 97]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.004.001.10 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 3 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 3 camt.004.001.10 ReturnAccountV10

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); Functionality file pp48, 49; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.004.001.10-p48-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p48, scope.

- Sender: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).
- Receiver: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The ReturnAccount message is sent by the transaction administrator to a member.

#### src-000015-camt.004.001.10-p48-c003-d1

Kind: initiator; message applicability: **current-message**; src-000015 file p48, scope.

- Initiator: **the transaction administrator (push mode)**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The Return Account message can be sent as a response to a related GetAccount message (pull mode) or initiated by the transaction administrator (push mode).

#### src-000015-camt.004.001.10-p48-c006-d1

Kind: sender-only; message applicability: **current-message**; src-000015 file p48, usage.

- Sender: **transaction administrator**. [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The transaction administrator may also send a ReturnAccount message with pre-defined information, at times previously agreed with the member, or to warn the member about a particular problem that may have arisen and which needs attention.

Source explicitly names the sender. Scheduling, warning/preliminary usage and information content remain in the quote; no receiver is supplied by this clause.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.004.001.10-p48-c001 — file p48, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Quoted above in src-000015-camt.004.001.10-p48-c001-d1.

**src-000015-camt.004.001.10-p48-c002 — file p48, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> It is used to provide information on the details of one or more accounts held at the transaction administrator, including information on the balances.

**src-000015-camt.004.001.10-p48-c003 — file p48, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator initiated.

Quoted above in src-000015-camt.004.001.10-p48-c003-d1.

**src-000015-camt.004.001.10-p48-c004 — file p48, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: transaction administrator maintains.

> At any time during the operating hours of the system, the member can query the transaction administrator to get information about the account(s) that the transaction administrator maintains for the member.

**src-000015-camt.004.001.10-p48-c005 — file p48, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: member request.

> The member can request information about accounts through a series of criteria, corresponding to the known information stored at the transaction administrator.

**src-000015-camt.004.001.10-p48-c006 — file p48, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: transaction administrator send.

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000015-camt.004.001.10-p48-c006-d1.

**src-000015-camt.004.001.10-p48-c007 — file p48, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The message from the transaction administrator can contain information based on the following elements:

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p48, scope.**

> The push of information can take place either at prearranged times or as a warning or alarm when a problem has occurred.

**File p48, usage.**

> For example, this may be necessary in order to perform the appropriate liquidity management and the necessary funds transfers between accounts.

**File p48, usage.**

> The query can concern one or more specific accounts, accounts of a particular identification, or a particular type.

**File p48, usage.**

> The purpose of the query may be to obtain one or more types of balance.

**File p48, usage.**

> account identification

**File p48, usage.**

> account name

**File p48, usage.**

> account type (this is used when the account identification represents, for example, a group of accounts)

**File p48, usage.**

> currency of the account (this is used for example when the account identification represents a group of account in various currencies, or when it is a multi-currency account with one single identifier)

**File p48, usage.**

> type of balance (if not present in the GetAccount message, all balances will be reported)

**File p48, usage.**

> bilateral or multilateral limits

**File p48, usage.**

> related counterparty (when the limit or balance is bilateral) Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10 Cash Management - Maintenance 2024 - 2025 48 February 2025

**File p49, usage.**

> balance value date (if not present in the GetAccount message, the ReturnAccount message will contain the latest available balance)

**File p49, usage.**

> number of payments to the additional account information on the generic design of the Get/Return messages can be found in the section How to Use the Cash Management Messages.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
