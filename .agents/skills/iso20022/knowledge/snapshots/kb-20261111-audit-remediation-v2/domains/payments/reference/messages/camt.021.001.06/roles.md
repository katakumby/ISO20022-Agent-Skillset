---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.021.001.06 participant and direction evidence"
domain: "payments"
message_id: "camt.021.001.06"
message_family: "camt.021"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06"
source_ids: ["src-000015", "src-000035"]
message_sets: ["cash-management"]
role_labels: ["a member of the system", "member of the system", "members", "the members", "The transaction administrator", "the transaction administrator", "transaction administrator"]
search_terms: ["a member of the system", "member of the system", "members", "the members", "The transaction administrator", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "20 camt.021.001.06 ReturnGeneralBusinessInformationV06", "file_pages": [568, 576]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.021.001.06 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 3 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 20 camt.021.001.06 ReturnGeneralBusinessInformationV06

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp568, 569; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.021.001.06-p568-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p568, scope.

- Sender: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).
- Receiver: **a member of the system**. [a member of the system](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The ReturnGeneralBusinessInformation message is sent by the transaction administrator to a member of the system.

#### src-000015-camt.021.001.06-p568-c003-d1

Kind: initiator; message applicability: **current-message**; src-000015 file p568, scope.

- Initiator: **the transaction administrator (push mode)**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The Return General Business Information message can be sent as a response to a related GetGeneralBusinessInformation message (pull mode) or initiated by the transaction administrator (push mode).

#### src-000015-camt.021.001.06-p568-c004-d1

Kind: sender-to-receiver; message applicability: **related-or-unspecified-message**; src-000015 file p568, usage.

- Sender: **The transaction administrator**. [The transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).
- Receiver: **the members, which may request further action from them**. [the members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The transaction administrator can send general business information messages to the members, which may request further action from them.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.021.001.06-p568-c001 — file p568, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member of the system](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Quoted above in src-000015-camt.021.001.06-p568-c001-d1.

**src-000015-camt.021.001.06-p568-c002 — file p568, scope.**

Mentioned roles: [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> It is used to provide some or all of the members with information related to the processing of the system.

**src-000015-camt.021.001.06-p568-c003 — file p568, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator initiated.

Quoted above in src-000015-camt.021.001.06-p568-c003-d1.

**src-000015-camt.021.001.06-p568-c004 — file p568, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: transaction administrator send.

Quoted above in src-000015-camt.021.001.06-p568-c004-d1.

**src-000015-camt.021.001.06-p568-c005 — file p568, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> non-solicited reports are pushed by the transaction administrator to the (selected) members together with a reference, a qualifier and a subject line

**src-000015-camt.021.001.06-p568-c006 — file p568, usage.**

Mentioned roles: [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> upon request from the members (pull mode), the transaction administrator delivers the full text/content of the message back to the user In either case, the message from the transaction administrator can contain information based on the following elements:

**src-000015-camt.021.001.06-p568-c007 — file p568, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> This enumeration has to be agreed upon by the transaction administrator and the members of the system).

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p568, scope.**

> The push of information can take place either at prearranged times or as a warning or alarm when a problem has occurred.

**File p568, usage.**

> General business information can contain either static data announcing foreseen events affecting the system operations, or dynamic data warning or notifying about unexpected events.

**File p568, usage.**

> This type of information can be transmitted in either of the two following ways:

**File p568, usage.**

> subject of the report detailing the purpose and content of the message

**File p568, usage.**

> details of the report

**File p568, usage.**

> indication of the priority of the report and of its format.

**File p568, usage.**

> (Note that if the format is indicated, the subject refers to a set of pre-agreed texts.

**File p568, usage.**

> Additional information on the generic design of the Get/Return messages can be found in the MDR Part 1 section How to Use the Cash Management Messages.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
