---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.014.001.05 participant and direction evidence"
domain: "payments"
message_id: "camt.014.001.05"
message_family: "camt.014"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.014.001.05"
source_ids: ["src-000015", "src-000028"]
message_sets: ["cash-management"]
role_labels: ["a member of the system", "Member", "member", "member of the system", "members", "the transaction administrator", "transaction administrator"]
search_terms: ["a member of the system", "Member", "member", "member of the system", "members", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "13 camt.014.001.05 ReturnMemberV05", "file_pages": [476, 494]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.014.001.05 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 3 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 13 camt.014.001.05 ReturnMemberV05

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp476, 477; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.014.001.05-p476-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p476, scope.

- Sender: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).
- Receiver: **a member of the system**. [a member of the system](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The ReturnMember message is sent by the transaction administrator to a member of the system.

#### src-000015-camt.014.001.05-p476-c003-d1

Kind: initiator; message applicability: **current-message**; src-000015 file p476, scope.

- Initiator: **the transaction administrator (push mode)**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The ReturnMember message can be sent as a response to a related GetMember message (pull mode) or initiated by the transaction administrator (push mode).

#### src-000015-camt.014.001.05-p476-c008-d1

Kind: sender-only; message applicability: **current-message**; src-000015 file p476, usage.

- Sender: **transaction administrator**. [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The transaction administrator may also send a Return Member message with pre-defined information at times previously agreed with the member or to warn the member about a particular problem that may have arisen and which needs the member(s) attention.

Source explicitly names the sender. Scheduling, warning/preliminary usage and information content remain in the quote; no receiver is supplied by this clause.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.014.001.05-p476-c001 — file p476, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member of the system](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Quoted above in src-000015-camt.014.001.05-p476-c001-d1.

**src-000015-camt.014.001.05-p476-c002 — file p476, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator maintained.

> It is used to provide information on static data maintained by the transaction administrator and related to the participants in the system and their membership status vis-a-vis this system.

**src-000015-camt.014.001.05-p476-c003 — file p476, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator initiated.

Quoted above in src-000015-camt.014.001.05-p476-c003-d1.

**src-000015-camt.014.001.05-p476-c004 — file p476, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The transaction administrator is in charge of providing the members with business information.

**src-000015-camt.014.001.05-p476-c005 — file p476, usage.**

> Among other things, it can refer to information about the membership of the system.

**src-000015-camt.014.001.05-p476-c006 — file p476, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: member request.

> The member can request information about the members of the system through a series of criteria, corresponding to the known information stored within the transaction administrator.

**src-000015-camt.014.001.05-p476-c007 — file p476, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> Based on the criteria received within the request, the transaction administrator will select items that will match with the request and report them to the requestor.

**src-000015-camt.014.001.05-p476-c008 — file p476, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [Member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: transaction administrator send.

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000015-camt.014.001.05-p476-c008-d1.

**src-000015-camt.014.001.05-p476-c009 — file p476, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The message from the transaction administrator can contain information based on the following elements:

**src-000015-camt.014.001.05-p476-c010 — file p476, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> identification of the member within the system

**src-000015-camt.014.001.05-p476-c011 — file p476, usage.**

> membership status

**src-000015-camt.014.001.05-p476-c012 — file p476, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> type of member

**src-000015-camt.014.001.05-p476-c013 — file p476, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> contact details for the member: name, address

**src-000015-camt.014.001.05-p476-c014 — file p476, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> identification of the member's account

**src-000015-camt.014.001.05-p476-c015 — file p476, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> identification of contact persons for the member, their role and details.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p476, scope.**

> The push of information can take place either at prearranged times or as a warning or alarm when a problem has occurred.

**File p476, usage.**

> The term business information covers all information related to the management of the system, that is, not related to the transactions entered into in the system.

**File p476, usage.**

> The type of business information available can vary depending on the system.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
