---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "colr.001.001.02 participant and direction evidence"
domain: "securities"
message_id: "colr.001.001.02"
message_family: "colr.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:colr.001.001.02"
source_ids: ["src-000233", "src-000259", "src-000357"]
message_sets: ["t2s", "t2s-collateral-reporting"]
role_labels: ["a system member", "directly connected party", "system member", "system transaction administrator", "the system transaction administrator"]
search_terms: ["a system member", "directly connected party", "system member", "system transaction administrator", "the system transaction administrator"]
participant_ids: ["participant-narrative-src-000357-directly-connected-party", "participant-src-000356-system-member", "participant-src-000356-system-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "24 colr.001.001.02 CollateralValueQueryV02", "file_pages": [578, 589]}, {"source_id": "src-000357", "heading": "2 colr.001.001.02 CollateralValueQueryV02", "file_pages": [4, 15]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# colr.001.001.02 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 3 uniquely resolved participant references.

## src-000233 — 24 colr.001.001.02 CollateralValueQueryV02

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp578; publication August 2026.

### Direction and initiation clauses

#### src-000233-colr.001.001.02-p578-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p578, scope.

- Sender: **a system member (such as a directly connected party)**. [a system member](../../../../../shared/reference/participants/participant-src-000356-system-member.md).
- Receiver: **the system transaction administrator**. [the system transaction administrator](../../../../../shared/reference/participants/participant-src-000356-system-transaction-administrator.md).

> The CollateralValueQuery message is sent by a system member (such as a directly connected party) to the system transaction administrator to query the current available value of securities for auto collateralisation for one specific or several cash accounts.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-colr.001.001.02-p578-c001 — file p578, scope.**

Mentioned roles: [system member](../../../../../shared/reference/participants/participant-src-000356-system-member.md); [directly connected party](../../../../../shared/reference/participants/participant-narrative-src-000357-directly-connected-party.md); [system transaction administrator](../../../../../shared/reference/participants/participant-src-000356-system-transaction-administrator.md).

Quoted above in src-000233-colr.001.001.02-p578-c001-d1.

## src-000357 — 2 colr.001.001.02 CollateralValueQueryV02

[src-000357](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`; Functionality file pp4; publication march-2024.

### Direction and initiation clauses

#### src-000357-colr.001.001.02-p4-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000357 file p4, scope.

- Sender: **a system member (such as a directly connected party)**. [a system member](../../../../../shared/reference/participants/participant-src-000356-system-member.md).
- Receiver: **the system transaction administrator**. [the system transaction administrator](../../../../../shared/reference/participants/participant-src-000356-system-transaction-administrator.md).

> The CollateralValueQuery message is sent by a system member (such as a directly connected party) to the system transaction administrator to query the current available value of securities for auto collateralisation for one specific or several cash accounts.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000357-colr.001.001.02-p4-c001 — file p4, scope.**

Mentioned roles: [system member](../../../../../shared/reference/participants/participant-src-000356-system-member.md); [directly connected party](../../../../../shared/reference/participants/participant-narrative-src-000357-directly-connected-party.md); [system transaction administrator](../../../../../shared/reference/participants/participant-src-000356-system-transaction-administrator.md).

Quoted above in src-000357-colr.001.001.02-p4-c001-d1.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
