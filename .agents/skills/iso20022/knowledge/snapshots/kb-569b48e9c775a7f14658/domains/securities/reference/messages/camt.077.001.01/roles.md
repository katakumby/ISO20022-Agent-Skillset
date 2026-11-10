---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "camt.077.001.01 participant and direction evidence"
domain: "securities"
message_id: "camt.077.001.01"
message_family: "camt.077"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.077.001.01"
source_ids: ["src-000233", "src-000250", "src-000346"]
message_sets: ["t2s", "t2s-billing"]
role_labels: ["a system member", "system member", "system transaction administrator", "the system transaction administrator"]
search_terms: ["a system member", "system member", "system transaction administrator", "the system transaction administrator"]
participant_ids: ["participant-narrative-src-000346-system-member", "participant-narrative-src-000346-system-transaction-administrator"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "15 camt.077.001.01 BillingReportV01", "file_pages": [240, 340]}, {"source_id": "src-000346", "heading": "3 camt.077.001.01 BillingReportV01", "file_pages": [11, 111]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# camt.077.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 2 uniquely resolved participant references.

## src-000233 — 15 camt.077.001.01 BillingReportV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp240; publication August 2026.

### Direction and initiation clauses

#### src-000233-camt.077.001.01-p240-c001-d1

Kind: exchange-participants; message applicability: **current-message**; src-000233 file p240, scope.

- Exchange participants: **the system transaction administrator and a system member**. [the system transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000346-system-transaction-administrator.md); [a system member](../../../../../shared/reference/participants/participant-narrative-src-000346-system-member.md).

> The BillingReport message is exchanged between the system transaction administrator and a system member.

An exchange-between statement establishes participation, not sender/receiver direction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-camt.077.001.01-p240-c001 — file p240, scope.**

Mentioned roles: [system transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000346-system-transaction-administrator.md); [system member](../../../../../shared/reference/participants/participant-narrative-src-000346-system-member.md).

Quoted above in src-000233-camt.077.001.01-p240-c001-d1.

**src-000233-camt.077.001.01-p240-c002 — file p240, scope.**

Mentioned roles: [system member](../../../../../shared/reference/participants/participant-narrative-src-000346-system-member.md).

> Cumulative Billing Data Query Response: The BillingReport message is also used to inform the system member about details backing an invoice.

**src-000233-camt.077.001.01-p240-c003 — file p240, scope.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> This can be sent via cumulative billing data or itemised billing data as response to an invoice query message.

**src-000233-camt.077.001.01-p240-c004 — file p240, scope.**

Mentioned roles: [system member](../../../../../shared/reference/participants/participant-narrative-src-000346-system-member.md).

> Itemised Billing Data Query Response: The BillingReport message is also used to inform the system member about details backing an invoice.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p240, scope.**

> It aims at providing the invoice or invoice cancellation and informing about data providing cumulative or itemised details backing an invoice.

**File p240, scope.**

> BillingReport is used for the following usages:

**File p240, scope.**

> Invoice The Cumulative Invoice will consist of the following:

**File p240, scope.**

> Sum of the total number of units per service item for each CSD or CB;

**File p240, scope.**

> Sum of the amounts based on the total number of units per service item for each CSD or CB;

**File p240, scope.**

> Cancellation status of the invoice data.

**File p240, scope.**

> Invoice Cancellation

**File p240, scope.**

> This can be via cumulative billing data or itemised billing data as response to an invoice query message.

## src-000346 — 3 camt.077.001.01 BillingReportV01

[src-000346](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`; Functionality file pp11; publication december-2025.

### Direction and initiation clauses

#### src-000346-camt.077.001.01-p11-c001-d1

Kind: exchange-participants; message applicability: **current-message**; src-000346 file p11, scope.

- Exchange participants: **the system transaction administrator and a system member**. [the system transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000346-system-transaction-administrator.md); [a system member](../../../../../shared/reference/participants/participant-narrative-src-000346-system-member.md).

> The BillingReport message is exchanged between the system transaction administrator and a system member.

An exchange-between statement establishes participation, not sender/receiver direction.

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000346-camt.077.001.01-p11-c001 — file p11, scope.**

Mentioned roles: [system transaction administrator](../../../../../shared/reference/participants/participant-narrative-src-000346-system-transaction-administrator.md); [system member](../../../../../shared/reference/participants/participant-narrative-src-000346-system-member.md).

Quoted above in src-000346-camt.077.001.01-p11-c001-d1.

**src-000346-camt.077.001.01-p11-c002 — file p11, scope.**

Mentioned roles: [system member](../../../../../shared/reference/participants/participant-narrative-src-000346-system-member.md).

> Cumulative Billing Data Query Response: The BillingReport message is also used to inform the system member about details backing an invoice.

**src-000346-camt.077.001.01-p11-c003 — file p11, scope.**

Reviewed clause disposition: **message-purpose-status-or-condition**. Literal purpose, timing, message status, option-list introduction or related-message condition; no additional named current-message sender/receiver pair is asserted. All source wording is retained.

> This can be sent via cumulative billing data or itemised billing data as response to an invoice query message.

**src-000346-camt.077.001.01-p11-c004 — file p11, scope.**

Mentioned roles: [system member](../../../../../shared/reference/participants/participant-narrative-src-000346-system-member.md).

> Itemised Billing Data Query Response: The BillingReport message is also used to inform the system member about details backing an invoice.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p11, scope.**

> It aims at providing the invoice or invoice cancellation and informing about data providing cumulative or itemised details backing an invoice.

**File p11, scope.**

> BillingReport is used for the following usages:

**File p11, scope.**

> Invoice The Cumulative Invoice will consist of the following:

**File p11, scope.**

> Sum of the total number of units per service item for each CSD or CB;

**File p11, scope.**

> Sum of the amounts based on the total number of units per service item for each CSD or CB;

**File p11, scope.**

> Cancellation status of the invoice data.

**File p11, scope.**

> Invoice Cancellation

**File p11, scope.**

> This can be via cumulative billing data or itemised billing data as response to an invoice query message.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
