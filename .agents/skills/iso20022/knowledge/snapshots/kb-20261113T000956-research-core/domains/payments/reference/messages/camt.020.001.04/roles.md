---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.020.001.04 participant and direction evidence"
domain: "payments"
message_id: "camt.020.001.04"
message_family: "camt.020"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04"
source_ids: ["src-000015", "src-000034"]
message_sets: ["cash-management"]
role_labels: ["a member", "member", "members", "the members", "The transaction administrator", "the transaction administrator", "transaction administrator"]
search_terms: ["a member", "member", "members", "the members", "The transaction administrator", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "19 camt.020.001.04 GetGeneralBusinessInformationV04", "file_pages": [558, 567]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.020.001.04 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 3 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 19 camt.020.001.04 GetGeneralBusinessInformationV04

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp558, 559; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.020.001.04-p558-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p558, scope.

- Sender: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).
- Receiver: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The GetGeneralBusinessInformation message is sent by a member to the transaction administrator.

#### src-000015-camt.020.001.04-p558-c002-d1

Kind: sender-to-receiver; message applicability: **related-previous-broadcast-message**; src-000015 file p558, scope.

- Sender: **transaction administrator**. [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).
- Receiver: **members**. [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> It is used to request information on a broadcast-type message previously sent by the transaction administrator to all or some of the members, giving information related to the processing business.

All or some members receive the earlier broadcast-type message; this is not the GetGeneralBusinessInformation query direction.

#### src-000015-camt.020.001.04-p558-c003-d1

Kind: sender-to-receiver; message applicability: **related-or-unspecified-message**; src-000015 file p558, usage.

- Sender: **The transaction administrator**. [The transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).
- Receiver: **the members, which may request further action from them**. [the members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The transaction administrator can send general business information messages to the members, which may request further action from them.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.020.001.04-p558-c001 — file p558, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Quoted above in src-000015-camt.020.001.04-p558-c001-d1.

**src-000015-camt.020.001.04-p558-c002 — file p558, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000015-camt.020.001.04-p558-c002-d1.

**src-000015-camt.020.001.04-p558-c003 — file p558, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: transaction administrator send.

Quoted above in src-000015-camt.020.001.04-p558-c003-d1.

**src-000015-camt.020.001.04-p558-c004 — file p558, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> non-solicited reports are pushed by the transaction administrator to the (selected) members together with a reference, a qualifier and a subject line

**src-000015-camt.020.001.04-p558-c005 — file p558, usage.**

Mentioned roles: [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> upon request from the members (pull mode), the transaction administrator delivers the full text/content of the message back to the user The Get General Business Information message is used in this second context.

**src-000015-camt.020.001.04-p558-c006 — file p558, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Reviewed clause disposition: **actor-or-condition-context**. The sentence describes actors, responsibilities, source/target data, prohibitions or conditions. Existing literal actions and the complete quote remain available; sending/receiving a different object or a negative assertion is not converted into an unconditional current-message direction.

> At any time during the operating hours of the system, the member can query the transaction administrator to get information about a report of general business information previously sent.

**src-000015-camt.020.001.04-p558-c007 — file p558, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member request.

> The member can request information based on the following elements:

**src-000015-camt.020.001.04-p558-c008 — file p558, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> priority of the report previously sent, and indication of its format.

**src-000015-camt.020.001.04-p558-c009 — file p558, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> This enumeration has to be agreed upon by the transaction administrator and the members of the system.)

**src-000015-camt.020.001.04-p558-c010 — file p558, usage.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> details of the previously sent message This message will be replied to by a ReturnGeneralBusinessInformation message.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p558, usage.**

> General business information can contain either static data announcing foreseen events affecting the system operations, or dynamic data warning or notifying about unexpected events.

**File p558, usage.**

> This type of information can be transmitted in either of the two following ways:

**File p558, usage.**

> reference of the report previously delivered

**File p558, usage.**

> subject of the report previously delivered, detailing the purpose and content of the message

**File p558, usage.**

> (Note that if the format is indicated, the subject refers to a set of pre-agreed texts.

**File p558, usage.**

> Additional information on the generic design of the Get/Return messages can be found in the section How to Use the Cash Management Messages.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
