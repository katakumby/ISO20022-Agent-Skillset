---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.071.001.05 participant and direction evidence"
domain: "payments"
message_id: "camt.071.001.05"
message_family: "camt.071"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.071.001.05"
source_ids: ["src-000015", "src-000047"]
message_sets: ["cash-management"]
role_labels: ["system member", "system transaction administrator", "the system member"]
search_terms: ["system member", "system transaction administrator", "the system member"]
participant_ids: ["participant-narrative-src-000015-system-transaction-administrator", "participant-src-000014-system-member"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000015", "heading": "32 camt.071.001.05 DeleteStandingOrderV05", "file_pages": [738, 744]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.071.001.05 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 1 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000015 — 32 camt.071.001.05 DeleteStandingOrderV05

[src-000015](../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md); Functionality file pp738; publication February 2025.

### Direction and initiation clauses

#### src-000015-camt.071.001.05-p738-c001-d1

Kind: sender-only; message applicability: **current-message**; src-000015 file p738, scope.

- Sender: **the system member**. [the system member](../../../../../shared/reference/participants/participant-src-000014-system-member.md).

> The DeleteStandingOrder message is sent by the system member to delete one or more standing orders within the static data held by the system transaction administrator.

The clause supplies the sender and a purpose introduced by “to”; it does not explicitly name a receiver.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000015-camt.071.001.05-p738-c001 — file p738, scope.**

Mentioned roles: [system member](../../../../../shared/reference/participants/participant-src-000014-system-member.md); [system transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000015-system-transaction-administrator.md).

Literal actions: system transaction administrator held.

Quoted above in src-000015-camt.071.001.05-p738-c001-d1.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
