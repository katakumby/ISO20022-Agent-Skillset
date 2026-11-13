---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.101.001.02 participant and direction evidence"
domain: "payments"
message_id: "camt.101.001.02"
message_family: "camt.101"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.101.001.02"
source_ids: ["src-000015", "src-000048"]
message_sets: ["cash-management"]
role_labels: ["a member", "member", "the transaction administrator", "transaction administrator"]
search_terms: ["a member", "member", "the transaction administrator", "transaction administrator"]
participant_ids: ["participant-narrative-src-000015-member", "participant-narrative-src-000015-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "33 camt.101.001.02 CreateLimitV02", "file_pages": [745, 754]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.101.001.02 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 33 camt.101.001.02 CreateLimitV02

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp745; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.101.001.02-p745-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000015 file p745, scope.

- Sender: **a member**. [a member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md).
- Receiver: **the transaction administrator**. [the transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

> The CreateLimit message is sent by a member to the transaction administrator.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.101.001.02-p745-c001 — file p745, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Quoted above in src-000015-camt.101.001.02-p745-c001-d1.

**src-000015-camt.101.001.02-p745-c002 — file p745, scope.**

Mentioned roles: [member](../../../../../shared/reference/participants/participant-narrative-src-000015-member.md); [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator managed.

> It is used to create one or several limits set by the member and managed by the transaction administrator.

**src-000015-camt.101.001.02-p745-c003 — file p745, usage.**

Mentioned roles: [transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-transaction-administrator.md).

Literal actions: transaction administrator execute.

> Based on the criteria defined in the CreateLimit message, the transaction administrator will execute or reject the requested creation and respond with a Receipt message as a reply to the request.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
