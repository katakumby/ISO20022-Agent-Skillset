---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.011.001.08 participant and direction evidence"
domain: "payments"
message_id: "camt.011.001.08"
message_family: "camt.011"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.011.001.08"
source_ids: ["src-000015", "src-000025"]
message_sets: ["cash-management"]
role_labels: ["a member", "member", "The transaction administrator", "the transaction administrator", "transaction administrator"]
search_terms: ["a member", "member", "The transaction administrator", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "10 camt.011.001.08 ModifyLimitV08", "file_pages": [422, 449]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.011.001.08 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 10 camt.011.001.08 ModifyLimitV08

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp422; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.011.001.08-p422-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p422, scope.

- Sender: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).
- Receiver: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The ModifyLimit message is sent by a member to the transaction administrator.

#### src-000015-camt.011.001.08-p422-c007-d1

Kind: sender-only; message applicability: **related-or-unspecified-message**; src-000015 file p422, usage.

- Sender: **The transaction administrator**. [The transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The transaction administrator may send a Receipt message as a reply to the ModifyLimit request.

The phrase following “to” is the request being answered, not an identified receiving participant.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.011.001.08-p422-c001 — file p422, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Quoted above in src-000015-camt.011.001.08-p422-c001-d1.

**src-000015-camt.011.001.08-p422-c002 — file p422, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator managed.

> It is used to request modifications in the details of one particular, several or all limits set by the member and managed by the transaction administrator.

**src-000015-camt.011.001.08-p422-c003 — file p422, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member request.

> At any time during the operating hours of the system, the member can request modifications in the limits it has set.

**src-000015-camt.011.001.08-p422-c004 — file p422, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> For example, the reason may be to unlock the payments queue regarding a particular member, or following a risk management decision issued after an exceptional event has occurred.

**src-000015-camt.011.001.08-p422-c005 — file p422, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member submit.

> The member will submit a message requesting modifications in one or more of the following criteria:

**src-000015-camt.011.001.08-p422-c006 — file p422, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator execute.

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> point in time when the limit becomes effective Based on the criteria received within the ModifyLimit message, the transaction administrator will execute or reject the requested modification.

**src-000015-camt.011.001.08-p422-c007 — file p422, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator send.

Quoted above in src-000015-camt.011.001.08-p422-c007-d1.

**src-000015-camt.011.001.08-p422-c008 — file p422, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member submit.

> To verify the outcome of the request, the member may submit a GetLimit message with the appropriate search criteria.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p422, scope.**

> Each ModifyLimit message can alter only one type of limit (current or default).

**File p422, usage.**

> type of limit (current/default)

**File p422, usage.**

> identification of the system

**File p422, usage.**

> identification of the counterparty

**File p422, usage.**

> value of the limit(s) (default and/or current limit(s))

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
