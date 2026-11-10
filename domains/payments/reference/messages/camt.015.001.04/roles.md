---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.015.001.04 participant and direction evidence"
domain: "payments"
message_id: "camt.015.001.04"
message_family: "camt.015"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04"
source_ids: ["src-000015", "src-000029"]
message_sets: ["cash-management"]
role_labels: ["a member", "Member", "member", "members", "the transaction administrator", "transaction administrator"]
search_terms: ["a member", "Member", "member", "members", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "14 camt.015.001.04 ModifyMemberV04", "file_pages": [495, 504]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.015.001.04 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 14 camt.015.001.04 ModifyMemberV04

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); Functionality file pp495, 496; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.015.001.04-p495-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p495, scope.

- Sender: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).
- Receiver: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The ModifyMember message is sent by a member to the transaction administrator.

#### src-000015-camt.015.001.04-p495-c010-d1

Kind: sender-only; message applicability: **related-or-unspecified-message**; src-000015 file p495, usage.

- Sender: **In principle, the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> In principle, the transaction administrator may send a Receipt message as a reply to the ModifyMember request.

The phrase following “to” is the request being answered, not an identified receiving participant.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.015.001.04-p495-c001 — file p495, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Quoted above in src-000015-camt.015.001.04-p495-c001-d1.

**src-000015-camt.015.001.04-p495-c002 — file p495, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator maintains.

> It is used to request modifications to the static data related to the profile of a member that the transaction administrator maintains.

**src-000015-camt.015.001.04-p495-c003 — file p495, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The transaction administrator is in charge of providing the members with business information.

**src-000015-camt.015.001.04-p495-c004 — file p495, usage.**

> Among other things, it can, refer to information about the membership of the system.

**src-000015-camt.015.001.04-p495-c005 — file p495, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member request.

> At any time during the operating hours of the system, the member can request the transaction administrator to modify the information it maintains about the member.

**src-000015-camt.015.001.04-p495-c006 — file p495, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member submit.

> The member will submit a message requesting modifications in one or more of the following criteria:

**src-000015-camt.015.001.04-p495-c007 — file p495, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> identification of the member

**src-000015-camt.015.001.04-p495-c008 — file p495, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> contact information for the member organization: postal address, e-mail address, telephone or fax number

**src-000015-camt.015.001.04-p495-c009 — file p495, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [Member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator execute.

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> identification of contact persons for the member, their role and/or details (postal address, e-mail address, telephone or fax number) Based on the criteria received within the Modify Member message, the transaction administrator will execute or reject the requested modifications.

**src-000015-camt.015.001.04-p495-c010 — file p495, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator send.

Quoted above in src-000015-camt.015.001.04-p495-c010-d1.

**src-000015-camt.015.001.04-p495-c011 — file p495, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member submit.

> To verify the outcome of the request, the member may submit a GetMember message with the appropriate search criteria.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p495, usage.**

> The term business information covers all information related to the management of the system, that is, not related to the transactions entered into the system.

**File p495, usage.**

> The type of business information available can vary depending on the system.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
