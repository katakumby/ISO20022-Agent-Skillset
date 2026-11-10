---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "admi.005.001.02 participant and direction evidence"
domain: "shared"
message_id: "admi.005.001.02"
message_family: "admi.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:admi.005.001.02"
source_ids: ["src-000233", "src-000237", "src-000344"]
message_sets: ["t2s", "t2s-administration"]
role_labels: ["system member", "system transaction administrator"]
search_terms: ["system member", "system transaction administrator"]
participant_ids: ["participant-src-000343-system-member", "participant-src-000343-system-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "2 admi.005.001.02 ReportQueryRequestV02", "file_pages": [34, 56]}, {"source_id": "src-000344", "heading": "2 admi.005.001.02 ReportQueryRequestV02", "file_pages": [4, 26]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# admi.005.001.02 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000233 — 2 admi.005.001.02 ReportQueryRequestV02

[src-000233](../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); Functionality file pp34; publication August 2026.

### Direction and initiation clauses

#### src-000233-admi.005.001.02-p34-c001-d1

Kind: exchange-participants; message applicability: **current-message**; src-000233 file p34, scope.

- Exchange participants: **system member and system transaction administrator**. [system member](../../participants/participant-src-000343-system-member.md); [system transaction administrator](../../participants/participant-src-000343-system-transaction-administrator.md).

> The ReportQueryRequest message is exchanged between system member and system transaction administrator.

An exchange-between statement establishes participation, not sender/receiver direction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-admi.005.001.02-p34-c001 — file p34, scope.**

Mentioned roles: [system member](../../participants/participant-src-000343-system-member.md); [system transaction administrator](../../participants/participant-src-000343-system-transaction-administrator.md).

Quoted above in src-000233-admi.005.001.02-p34-c001-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p34, scope.**

> It aims at querying the latest available report data of a specific report type.

**File p34, scope.**

> A report is stored and available for query until the event occurs again report is replaced.

## src-000344 — 2 admi.005.001.02 ReportQueryRequestV02

[src-000344](../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`; Functionality file pp4; publication march-2024.

### Direction and initiation clauses

#### src-000344-admi.005.001.02-p4-c001-d1

Kind: exchange-participants; message applicability: **current-message**; src-000344 file p4, scope.

- Exchange participants: **system member and system transaction administrator**. [system member](../../participants/participant-src-000343-system-member.md); [system transaction administrator](../../participants/participant-src-000343-system-transaction-administrator.md).

> The ReportQueryRequest message is exchanged between system member and system transaction administrator.

An exchange-between statement establishes participation, not sender/receiver direction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000344-admi.005.001.02-p4-c001 — file p4, scope.**

Mentioned roles: [system member](../../participants/participant-src-000343-system-member.md); [system transaction administrator](../../participants/participant-src-000343-system-transaction-administrator.md).

Quoted above in src-000344-admi.005.001.02-p4-c001-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p4, scope.**

> It aims at querying the latest available report data of a specific report type.

**File p4, scope.**

> A report is stored and available for query until the event occurs again report is replaced.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../tracking/issues.md)
