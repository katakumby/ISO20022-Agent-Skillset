---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.012.001.08 participant and direction evidence"
domain: "payments"
message_id: "camt.012.001.08"
message_family: "camt.012"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.012.001.08"
source_ids: ["src-000015", "src-000026"]
message_sets: ["cash-management"]
role_labels: ["a member", "member", "The transaction administrator", "the transaction administrator", "transaction administrator"]
search_terms: ["a member", "member", "The transaction administrator", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "11 camt.012.001.08 DeleteLimitV08", "file_pages": [450, 463]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.012.001.08 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 11 camt.012.001.08 DeleteLimitV08

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp450; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.012.001.08-p450-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p450, scope.

- Sender: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).
- Receiver: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The DeleteLimit message is sent by a member to the transaction administrator.

#### src-000015-camt.012.001.08-p450-c005-d1

Kind: sender-only; message applicability: **related-or-unspecified-message**; src-000015 file p450, usage.

- Sender: **The transaction administrator**. [The transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The transaction administrator may send a Receipt message as a reply to the DeleteLimit request.

The phrase following “to” is the request being answered, not an identified receiving participant.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.012.001.08-p450-c001 — file p450, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Quoted above in src-000015-camt.012.001.08-p450-c001-d1.

**src-000015-camt.012.001.08-p450-c002 — file p450, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator managed.

> It is used to request the deletion of one particular, several or all limits set by the member and managed by the transaction administrator.

**src-000015-camt.012.001.08-p450-c003 — file p450, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member submit.

> The member will submit a DeleteLimit message identifying which limit(s) it wants to delete (current limit risk/liquidity limit concepts have been merged) based on following criteria:

**src-000015-camt.012.001.08-p450-c004 — file p450, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator execute.

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> identification of the counterparty (bilateral limit) Based on the criteria received within the DeleteLimit message, the transaction administrator will execute or reject the requested modifications.

**src-000015-camt.012.001.08-p450-c005 — file p450, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator send.

Quoted above in src-000015-camt.012.001.08-p450-c005-d1.

**src-000015-camt.012.001.08-p450-c006 — file p450, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member submit.

> To verify the outcome of the request, the member may submit a GetLimit message with the appropriate search criteria.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p450, scope.**

> The DeleteLimit message may delete several types of current limits (risk or liquidity management limit), based on a multiple requests.

**File p450, usage.**

> type of limit(s) (current/default)

**File p450, usage.**

> value of the limit(s) (default and/or current limit(s))

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
