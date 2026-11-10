---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.007.001.10 participant and direction evidence"
domain: "payments"
message_id: "camt.007.001.10"
message_family: "camt.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10"
source_ids: ["src-000015", "src-000021"]
message_sets: ["cash-management"]
role_labels: ["a member", "member", "Members of a system", "The transaction administrator", "the transaction administrator", "transaction administrator"]
search_terms: ["a member", "member", "Members of a system", "The transaction administrator", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "6 camt.007.001.10 ModifyTransactionV10", "file_pages": [326, 346]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.007.001.10 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 6 camt.007.001.10 ModifyTransactionV10

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp326, 327; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.007.001.10-p326-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p326, scope.

- Sender: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).
- Receiver: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The ModifyTransaction message is sent by a member to the transaction administrator.

#### src-000015-camt.007.001.10-p326-c012-d1

Kind: sender-only; message applicability: **related-or-unspecified-message**; src-000015 file p326, usage.

- Sender: **The transaction administrator**. [The transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The transaction administrator may send a Receipt message as a reply to the ModifyTransaction request.

The phrase following “to” is the request being answered, not an identified receiving participant.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.007.001.10-p326-c001 — file p326, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Quoted above in src-000015-camt.007.001.10-p326-c001-d1.

**src-000015-camt.007.001.10-p326-c002 — file p326, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> It is used to request one modification in one payment instruction held at the transaction administrator and sent by the member, debiting or crediting its account at the transaction administrator.

**src-000015-camt.007.001.10-p326-c003 — file p326, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> Following normal business flows, transactions registered by the transaction administrator may be queued for later settlement (because of insufficient funds available, or because of risk or liquidity limits, etc.).

**src-000015-camt.007.001.10-p326-c004 — file p326, usage.**

Mentioned roles: [Members of a system](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> Members of a system need to have information about the payments queue(s) and must have the ability to take action (that is, to cancel or modify the transaction(s) to be settled).

**src-000015-camt.007.001.10-p326-c005 — file p326, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> Note, however, that actions by a member will always concern transactions in a transient status.

**src-000015-camt.007.001.10-p326-c006 — file p326, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member request.

> For this reason, at any time during the operating hours of the system, the member can request modifications to the features of transient transactions.

**src-000015-camt.007.001.10-p326-c007 — file p326, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member submit.

> The member will submit a message requesting modifications in one or more of the following criteria:

**src-000015-camt.007.001.10-p326-c008 — file p326, usage.**

> instruction given, related to the processing of the transaction

**src-000015-camt.007.001.10-p326-c009 — file p326, usage.**

> type of payment instructed

**src-000015-camt.007.001.10-p326-c010 — file p326, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> priority of payment period in which the payment instruction should be processed (processing validity time) The ModifyTransaction message will contain the new values that the member wants to see applied to the features of the transaction identified in the message.

**src-000015-camt.007.001.10-p326-c011 — file p326, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator execute.

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> Based on the criteria received within the ModifyTransaction message, the transaction administrator will execute or reject the requested modifications.

**src-000015-camt.007.001.10-p326-c012 — file p326, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator send.

Quoted above in src-000015-camt.007.001.10-p326-c012-d1.

**src-000015-camt.007.001.10-p326-c013 — file p326, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member submit.

> To verify the outcome of the request, the member may submit a GetTransaction message with the appropriate search criteria.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p326, usage.**

> A transaction may have a series of statuses.

**File p326, usage.**

> These can be transient (such as pending or related types) and final (such as rejected, revoked and/or settled).

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
