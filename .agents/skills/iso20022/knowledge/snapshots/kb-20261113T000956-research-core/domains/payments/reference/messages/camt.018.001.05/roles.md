---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.018.001.05 participant and direction evidence"
domain: "payments"
message_id: "camt.018.001.05"
message_family: "camt.018"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.018.001.05"
source_ids: ["src-000015", "src-000032"]
message_sets: ["cash-management"]
role_labels: ["a member", "member", "members", "the transaction administrator", "transaction administrator"]
search_terms: ["a member", "member", "members", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "17 camt.018.001.05 GetBusinessDayInformationV05", "file_pages": [522, 534]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.018.001.05 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 17 camt.018.001.05 GetBusinessDayInformationV05

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp522; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.018.001.05-p522-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p522, scope.

- Sender: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).
- Receiver: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The GetBusinessDayInformation message is sent by a member to the transaction administrator.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.018.001.05-p522-c001 — file p522, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Quoted above in src-000015-camt.018.001.05-p522-c001-d1.

**src-000015-camt.018.001.05-p522-c002 — file p522, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The transaction administrator is in charge of providing the members with business information.

**src-000015-camt.018.001.05-p522-c003 — file p522, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> At any time during the operating hours of the system, the member can query the transaction administrator to get information about the static data of the system.

**src-000015-camt.018.001.05-p522-c004 — file p522, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: member request.

> The member can request information based on the following elements:

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p522, scope.**

> It is used to request information on different types of administrative data linked to the system.

**File p522, usage.**

> The term business day information covers all information related to the management of the system, not related to the transactions created in the system.

**File p522, usage.**

> The type of business day information available can vary depending on the system.

**File p522, usage.**

> identification of the system

**File p522, usage.**

> currency within the system concerned

**File p522, usage.**

> status of the system

**File p522, usage.**

> period of availability of a given currency linked to the system concerned (in case the system handles more than one currency)

**File p522, usage.**

> closure information (dates when the system will be inactive and reasons for this inactivity)

**File p522, usage.**

> event indicator (types of event and precise timing of their occurrence within the system concerned) This message will be replied to by a ReturnBusinessDayInformation message.

**File p522, usage.**

> Additional information on the generic design of the Get/Return messages can be found in the section How to Use the Cash Management Messages.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
