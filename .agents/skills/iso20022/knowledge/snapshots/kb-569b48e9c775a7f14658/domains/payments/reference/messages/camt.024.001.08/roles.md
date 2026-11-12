---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.024.001.08 participant and direction evidence"
domain: "payments"
message_id: "camt.024.001.08"
message_family: "camt.024"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.024.001.08"
source_ids: ["src-000015", "src-000037"]
message_sets: ["cash-management"]
role_labels: ["a member", "account owner", "member", "The transaction administrator", "the transaction administrator", "transaction administrator"]
search_terms: ["a member", "account owner", "member", "The transaction administrator", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-account-owner", "participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "22 camt.024.001.08 ModifyStandingOrderV08", "file_pages": [591, 603]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.024.001.08 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 3 uniquely resolved participant references.

## src-000015 — 22 camt.024.001.08 ModifyStandingOrderV08

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp591, 592; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.024.001.08-p591-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p591, scope.

- Sender: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).
- Receiver: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The ModifyStandingOrder message is sent by a member to the transaction administrator.

#### src-000015-camt.024.001.08-p591-c006-d1

Kind: sender-only; message applicability: **related-or-unspecified-message**; src-000015 file p591, usage.

- Sender: **The transaction administrator**. [The transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The transaction administrator may send a Receipt message as a reply to the Modify Standing Order request.

The phrase following “to” is the request being answered, not an identified receiving participant.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.024.001.08-p591-c001 — file p591, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Quoted above in src-000015-camt.024.001.08-p591-c001-d1.

**src-000015-camt.024.001.08-p591-c002 — file p591, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> It is used to request a change in the features of a permanent order for the transfer of funds between two accounts belonging to the same member and being held at the transaction administrator.

**src-000015-camt.024.001.08-p591-c003 — file p591, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> There should be one standing order per (direct) member and per business day.

**src-000015-camt.024.001.08-p591-c004 — file p591, usage.**

Mentioned roles: [account owner](../../../../../shared/reference/participants/participant-narrative-src-000015-account-owner.md).

> account owner (for on behalf scenario)

**src-000015-camt.024.001.08-p591-c005 — file p591, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator execute.

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> dates when the standing order begins and ceases to be effective Based on the criteria received within the ModifyStandingOrder message, the transaction administrator will execute or reject the requested modifications.

**src-000015-camt.024.001.08-p591-c006 — file p591, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator send.

Quoted above in src-000015-camt.024.001.08-p591-c006-d1.

**src-000015-camt.024.001.08-p591-c007 — file p591, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member submit.

> To verify the outcome of the request, the member may submit a GetStandingOrder message with the appropriate search criteria.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p591, usage.**

> The ModifyStandingOrder message must not be used to request a transfer of funds between accounts during the working day.

**File p591, usage.**

> The liquidity transfer messages must be used for this purpose.

**File p591, usage.**

> There is no need to have a standing order to empty the settlement account at the end of the day and transfer the funds to the current account.

**File p591, usage.**

> For liquidity savings purposes, systems will effect the necessary transfers automatically when and where relevant.

**File p591, usage.**

> The ModifyStandingOrder message first identifies the standing order to be modified and then provide the details of the new standing order.

**File p591, usage.**

> The elements that can be modified are:

**File p591, usage.**

> amount

**File p591, usage.**

> account to be credited

**File p591, usage.**

> account to be debited

**File p591, usage.**

> frequency of payment

**File p591, usage.**

> daytime or overnight processing

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
