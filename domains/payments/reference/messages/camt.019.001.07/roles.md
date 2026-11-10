---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.019.001.07 participant and direction evidence"
domain: "payments"
message_id: "camt.019.001.07"
message_family: "camt.019"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.019.001.07"
source_ids: ["src-000015", "src-000033"]
message_sets: ["cash-management"]
role_labels: ["a member of the system", "member", "member of the system", "members", "the transaction administrator", "transaction administrator"]
search_terms: ["a member of the system", "member", "member of the system", "members", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "18 camt.019.001.07 ReturnBusinessDayInformationV07", "file_pages": [535, 557]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.019.001.07 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 3 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 18 camt.019.001.07 ReturnBusinessDayInformationV07

[src-000015](../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf); Functionality file pp535, 536; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.019.001.07-p535-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p535, scope.

- Sender: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).
- Receiver: **a member of the system**. [a member of the system](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The ReturnBusinessDayInformation message is sent by the transaction administrator to a member of the system.

#### src-000015-camt.019.001.07-p535-c002-d1

Kind: initiator; message applicability: **current-message**; src-000015 file p535, scope.

- Initiator: **the transaction administrator (push mode)**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The ReturnBusinessDayInformation message can be sent as a response to a related GetBusines DayInformation message (pull mode), or initiated by the transaction administrator (push mode).

#### src-000015-camt.019.001.07-p535-c006-d1

Kind: sender-only; message applicability: **current-message**; src-000015 file p535, usage.

- Sender: **transaction administrator**. [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The transaction administrator may also send a ReturnBusinessDayInformation message with pre- defined information at times previously agreed with the member or to warn the member about a particular problem that may have arisen and which needs attention.

Source explicitly names the sender. Scheduling, warning/preliminary usage and information content remain in the quote; no receiver is supplied by this clause.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.019.001.07-p535-c001 — file p535, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member of the system](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Quoted above in src-000015-camt.019.001.07-p535-c001-d1.

**src-000015-camt.019.001.07-p535-c002 — file p535, scope.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator initiated.

Quoted above in src-000015-camt.019.001.07-p535-c002-d1.

**src-000015-camt.019.001.07-p535-c003 — file p535, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [members](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

> The transaction administrator is in charge of providing the members with business information.

**src-000015-camt.019.001.07-p535-c004 — file p535, usage.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: member request.

> The member can request information about the static data of the system through a series of criteria, corresponding to the known information stored within the transaction administrator.

**src-000015-camt.019.001.07-p535-c005 — file p535, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator selects and reports.

Reviewed clause disposition: **source-explicit-role-action**. The actor and action are named in this sentence; the action object and conditions are retained and are not automatically the indexed message.

> Based on the criteria received within the request, the transaction administrator will select items that match the request and report them to the requester.

**src-000015-camt.019.001.07-p535-c006 — file p535, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).

Literal actions: transaction administrator send.

Reviewed clause disposition: **source-explicit-role-assertion**. The named role assertion is transcribed with its message/context scope and full source conditions; no unstated counterpart is supplied.

Quoted above in src-000015-camt.019.001.07-p535-c006-d1.

**src-000015-camt.019.001.07-p535-c007 — file p535, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The message from the transaction administrator can contain information based on the following elements:

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p535, scope.**

> It is used to provide information on different types of administrative data linked to the system.

**File p535, scope.**

> The push of information can take place either at prearranged times or as a warning or alarm when a problem has occurred.

**File p535, usage.**

> The term business day information covers all information related to the management of the system, that is, not related to the transactions or requests created in the system.

**File p535, usage.**

> The type of business information available can vary depending on the system.

**File p535, usage.**

> identification of the system

**File p535, usage.**

> status of the system and period in which this status is valid

**File p535, usage.**

> currency within the system concerned and details of the hours of availability linked to that particular currency

**File p535, usage.**

> events related to the functioning of the system and the timing of their occurrence Additional information on the generic design of the Get/Return messages can be found in the MDR Part 1 section How to Use the Cash Management Messages.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
