---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.013.001.04 participant and direction evidence"
domain: "payments"
message_id: "camt.013.001.04"
message_family: "camt.013"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04"
source_ids: ["src-000015", "src-000027"]
message_sets: ["cash-management"]
role_labels: ["a member", "member", "members", "the transaction administrator", "transaction administrator"]
search_terms: ["a member", "member", "members", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "12 camt.013.001.04 GetMemberV04", "file_pages": [464, 475]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.013.001.04 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 12 camt.013.001.04 GetMemberV04

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp464, 465; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.013.001.04-p464-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p464, scope.

- Sender: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).
- Receiver: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The GetMember message is sent by a member to the transaction administrator.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.013.001.04-p464-c001 — file p464, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Quoted above in src-000015-camt.013.001.04-p464-c001-d1.

**src-000015-camt.013.001.04-p464-c002 — file p464, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator maintained.

> It is used to request information on static data maintained by the transaction administrator and related to the participants in the system and their membership status vis-a-vis this system.

**src-000015-camt.013.001.04-p464-c003 — file p464, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The transaction administrator is in charge of providing the members with business information.

**src-000015-camt.013.001.04-p464-c004 — file p464, usage.**

> Among other things, it can refer to information about the membership of the system.

**src-000015-camt.013.001.04-p464-c005 — file p464, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> At any time during the operating hours of the system, the member can query the transaction administrator to get information about the static data related to the members of the system.

**src-000015-camt.013.001.04-p464-c006 — file p464, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member request.

> The member can request information based on the following elements:

**src-000015-camt.013.001.04-p464-c007 — file p464, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> identification of the member within the system

**src-000015-camt.013.001.04-p464-c008 — file p464, usage.**

> membership status

**src-000015-camt.013.001.04-p464-c009 — file p464, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> type of member

**src-000015-camt.013.001.04-p464-c010 — file p464, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> contact details for the member: name, address

**src-000015-camt.013.001.04-p464-c011 — file p464, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> account number of the member

**src-000015-camt.013.001.04-p464-c012 — file p464, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> identification of contact persons for the member This message will be replied to by a ReturnMember message.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p464, usage.**

> The term business information covers all information related to the management of the system, that is, not related to the transactions entered into the system.

**File p464, usage.**

> The type of business information available can vary depending on the system.

**File p464, usage.**

> Additional information on the generic design of the Get/Return messages can be found in the MDR Part 1 section How to Use the Cash Management Messages.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
