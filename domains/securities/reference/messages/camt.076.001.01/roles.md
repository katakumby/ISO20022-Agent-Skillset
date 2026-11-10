---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.076.001.01 participant and direction evidence"
domain: "securities"
message_id: "camt.076.001.01"
message_family: "camt.076"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.076.001.01"
source_ids: ["src-000233", "src-000249", "src-000346"]
message_sets: ["t2s", "t2s-billing"]
role_labels: ["system member", "system transaction administrator", "the system member", "the system transaction administrator"]
search_terms: ["system member", "system transaction administrator", "the system member", "the system transaction administrator"]
participant_ids: ["participant-narrative-src-000346-system-member", "participant-narrative-src-000346-system-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "14 camt.076.001.01 BillingReportRequestV01", "file_pages": [233, 239]}, {"source_id": "src-000346", "heading": "2 camt.076.001.01 BillingReportRequestV01", "file_pages": [4, 10]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.076.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000233 — 14 camt.076.001.01 BillingReportRequestV01

[src-000233](../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf); Functionality file pp233; publication August 2026.

### Direction and initiation clauses

#### src-000233-camt.076.001.01-p233-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000233 file p233, scope.

- Sender: **the system member**. [the system member](../../../../../shared/reference/participants/participant-narrative-src-000346-system-member.md).
- Receiver: **the system transaction administrator**. [the system transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000346-system-transaction-administrator.md).

> The BillingReportRequest message is sent by the system member to the system transaction administrator to request cumulative or itemised billing data.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-camt.076.001.01-p233-c001 — file p233, scope.**

Mentioned roles: [system member](../../../../../shared/reference/participants/participant-narrative-src-000346-system-member.md); [system transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000346-system-transaction-administrator.md).

Quoted above in src-000233-camt.076.001.01-p233-c001-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p233, scope.**

> The billing data may be cumulative information or aggregated information on the level of a single securities or a dedicated cash account within a given period for each service item.

## src-000346 — 2 camt.076.001.01 BillingReportRequestV01

[src-000346](../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`; Functionality file pp4; publication december-2025.

### Direction and initiation clauses

#### src-000346-camt.076.001.01-p4-c001-d1

Kind: sender-to-receiver; message applicability: **current-message**; src-000346 file p4, scope.

- Sender: **the system member**. [the system member](../../../../../shared/reference/participants/participant-narrative-src-000346-system-member.md).
- Receiver: **the system transaction administrator**. [the system transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000346-system-transaction-administrator.md).

> The BillingReportRequest message is sent by the system member to the system transaction administrator to request cumulative or itemised billing data.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000346-camt.076.001.01-p4-c001 — file p4, scope.**

Mentioned roles: [system member](../../../../../shared/reference/participants/participant-narrative-src-000346-system-member.md); [system transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000346-system-transaction-administrator.md).

Quoted above in src-000346-camt.076.001.01-p4-c001-d1.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p4, scope.**

> The billing data may be cumulative information or aggregated information on the level of a single securities or a dedicated cash account within a given period for each service item.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
