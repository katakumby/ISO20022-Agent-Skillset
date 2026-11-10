---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.023.001.07 participant and direction evidence"
domain: "payments"
message_id: "camt.023.001.07"
message_family: "camt.023"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.023.001.07"
source_ids: ["src-000015", "src-000036"]
message_sets: ["cash-management"]
role_labels: ["a member", "account owner", "financial institution", "member", "Members", "The transaction administrator", "the transaction administrator", "transaction administrator"]
search_terms: ["a member", "account owner", "financial institution", "member", "Members", "The transaction administrator", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-account-owner", "participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator", "participant-src-000014-financial-institution"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "21 camt.023.001.07 BackupPaymentV07", "file_pages": [577, 590]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.023.001.07 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 4 uniquely resolved participant references.

## src-000015 — 21 camt.023.001.07 BackupPaymentV07

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); Functionality file pp577, 578; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.023.001.07-p577-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p577, scope.

- Sender: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).
- Receiver: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The BackupPayment message is sent by a member to the transaction administrator.

#### src-000015-camt.023.001.07-p577-c011-d1

Kind: sender-only; message applicability: **related-or-unspecified-message**; src-000015 file p577, usage.

- Sender: **The transaction administrator**. [The transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The transaction administrator may send a Receipt message as a reply to the BackupPayment request.

The phrase following “to” is the request being answered, not an identified receiving participant.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.023.001.07-p577-c001 — file p577, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Quoted above in src-000015-camt.023.001.07-p577-c001-d1.

**src-000015-camt.023.001.07-p577-c002 — file p577, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> It is used to request a liquidity transfer from the member to another participant in the system when the user is in recovery mode.

**src-000015-camt.023.001.07-p577-c003 — file p577, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> Under very specific circumstances, the transaction administrator can accept direct input of transactions as part of its cash management functionalities.

**src-000015-camt.023.001.07-p577-c004 — file p577, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> This possibility is available only when a declared incident has been reported to the transaction administrator This could be the case, for example, when the internal systems of the member are having problems sending out payments or when the continuity of the whole system is put at risk.

**src-000015-camt.023.001.07-p577-c005 — file p577, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The purpose of the BackupPayment message is to prevent the consequences of a specific failure affecting not only the member experiencing problems but also its counterparties.

**src-000015-camt.023.001.07-p577-c006 — file p577, usage.**

Mentioned roles: [Members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> Members can therefore input transactions directly in order to ensure the stability of the system and smooth exchanges.

**src-000015-camt.023.001.07-p577-c007 — file p577, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member request.

> At any time during the operating hours of the system, and under the agreed circumstances, the member can request a backup payment to be effected.

**src-000015-camt.023.001.07-p577-c008 — file p577, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member request.

> The member can request the transfer by identifying the following elements:

**src-000015-camt.023.001.07-p577-c009 — file p577, usage.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/participant-narrative-src-000015-account-owner.md).

Literal actions: account owner will receive.

Reviewed clause disposition: **source-explicit-role-action**. The actor and action are named in this sentence; the action object and conditions are retained and are not automatically the indexed message.

> party (account owner) that will receive the funds

**src-000015-camt.023.001.07-p577-c010 — file p577, usage.**

Mentioned roles: [financial institution](../../../../../shared/reference/participants/participant-src-000014-financial-institution.md); [account owner](../../../../../shared/reference/participants/participant-narrative-src-000015-account-owner.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator execute.

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> the financial institution that will receive the funds on behalf of the account owner Based on the criteria received within the BackupPayment message, the transaction administrator will execute or reject the requested funds transfer.

**src-000015-camt.023.001.07-p577-c011 — file p577, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator send.

Quoted above in src-000015-camt.023.001.07-p577-c011-d1.

**src-000015-camt.023.001.07-p577-c012 — file p577, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member submit.

> To verify the outcome of the request, the member may submit a GetTransaction or GetAccount message with the appropriate search criteria.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
