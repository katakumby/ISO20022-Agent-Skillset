---
template: false
document_kind: "message-roles"
review_status: "needs-review"
title: "semt.044.001.01 participant and direction evidence"
domain: "securities"
message_id: "semt.044.001.01"
message_family: "semt.044"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.044.001.01"
source_ids: ["src-000233", "src-000319", "src-000375"]
message_sets: ["t2s", "t2s-securities-and-penalty-reporting"]
role_labels: ["CSD participant", "Executing/Servicing Party", "instructing party", "the Executing/Servicing Party", "the instructing party"]
search_terms: ["CSD participant", "Executing/Servicing Party", "instructing party", "the Executing/Servicing Party", "the instructing party"]
participant_ids: ["participant-src-000374-csd-participant", "participant-src-000374-executing-servicing-party", "participant-src-000374-instructing-party"]
role_extraction_status: "role-evidence-extracted-needs-review"
source_locations: [{"source_id": "src-000233", "heading": "81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "file_pages": [2761, 2827]}, {"source_id": "src-000375", "heading": "6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "file_pages": [179, 245]}]
limitations: ["Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.", "Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.", "Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.", "Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope."]
updated: "2026-11-09"
---

# semt.044.001.01 participants and message directions

This page retrieves literal role statements from the **exact message definition**. Sender, receiver and initiator are separate assertions. Institutional examples, intermediaries, copies, conditional paths and negative statements remain in their source context. Automatic extraction is not a completed semantic review.

Coverage: **role-evidence-extracted-needs-review**. 2 direction/initiator/exchange clauses; 3 uniquely resolved participant references.

## src-000233 — 81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01

[src-000233](../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md); Functionality file pp2761; publication August 2026.

### Direction and initiation clauses

#### src-000233-semt.044.001.01-p2761-c001-d1

Kind: sender-to-receiver; message applicability: **current-message-scope-name-variant**; src-000233 file p2761, scope.

- Sender: **the Executing/Servicing Party**. [the Executing/Servicing Party](../../../../../shared/reference/participants/participant-src-000374-executing-servicing-party.md).
- Receiver: **the instructing party**. [the instructing party](../../../../../shared/reference/participants/participant-src-000374-instructing-party.md).

> The SecuritiesTransactionPenaltiesReport V01 message is sent by the Executing/Servicing Party to the instructing party to inform about the cash penalties:

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000233-semt.044.001.01-p2761-c001 — file p2761, scope.**

Mentioned roles: [Executing/Servicing Party](../../../../../shared/reference/participants/participant-src-000374-executing-servicing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000374-instructing-party.md).

Quoted above in src-000233-semt.044.001.01-p2761-c001-d1.

**src-000233-semt.044.001.01-p2761-c002 — file p2761, scope.**

Mentioned roles: [CSD participant](../../../../../shared/reference/participants/participant-src-000374-csd-participant.md); [CSD participant](../../../../../shared/reference/participants/participant-src-000374-csd-participant.md).

> For example, in case of a CSD, the information shall include the cash penalties that are either imposed or credited to all of its participants and the CSD itself; in case of a CSD participant, the information shall include the cash penalties that are either imposed or credited to the CSD participant itself.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p2761, scope.**

> Newly computed cash penalties.

**File p2761, scope.**

> Modified penalties: to inform about the modifications occurred in existing cash penalties since the previous reporting.

**File p2761, scope.**

> Aggregated amounts of cash penalties: to inform about the aggregated amounts of the cash penalties computed for the business days of a given period, for example the previous month.

## src-000375 — 6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01

[src-000375](../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`; Functionality file pp179; publication march-2026.

### Direction and initiation clauses

#### src-000375-semt.044.001.01-p179-c001-d1

Kind: sender-to-receiver; message applicability: **current-message-scope-name-variant**; src-000375 file p179, scope.

- Sender: **the Executing/Servicing Party**. [the Executing/Servicing Party](../../../../../shared/reference/participants/participant-src-000374-executing-servicing-party.md).
- Receiver: **the instructing party**. [the instructing party](../../../../../shared/reference/participants/participant-src-000374-instructing-party.md).

> The SecuritiesTransactionPenaltiesReport V01 message is sent by the Executing/Servicing Party to the instructing party to inform about the cash penalties:

### Additional role mentions, actions and scenario context

These are narrative mentions and literal action clauses, not additional assumed senders or receivers. The quoted text determines whether a role is an example, intermediary, recipient of a copy, excluded party, or conditional participant.

**src-000375-semt.044.001.01-p179-c001 — file p179, scope.**

Mentioned roles: [Executing/Servicing Party](../../../../../shared/reference/participants/participant-src-000374-executing-servicing-party.md); [instructing party](../../../../../shared/reference/participants/participant-src-000374-instructing-party.md).

Quoted above in src-000375-semt.044.001.01-p179-c001-d1.

**src-000375-semt.044.001.01-p179-c002 — file p179, scope.**

Mentioned roles: [CSD participant](../../../../../shared/reference/participants/participant-src-000374-csd-participant.md); [CSD participant](../../../../../shared/reference/participants/participant-src-000374-csd-participant.md).

> For example, in case of a CSD, the information shall include the cash penalties that are either imposed or credited to all of its participants and the CSD itself; in case of a CSD participant, the information shall include the cash penalties that are either imposed or credited to the CSD participant itself.

### Remaining Functionality narrative

These source sentences were not classified as role clauses. They remain available for checking missed roles, conditions, outcomes and usage restrictions.

**File p179, scope.**

> Newly computed cash penalties.

**File p179, scope.**

> Modified penalties: to inform about the modifications occurred in existing cash penalties since the previous reporting.

**File p179, scope.**

> Aggregated amounts of cash penalties: to inform about the aggregated amounts of the cash penalties computed for the business days of a given period, for example the previous month.

## Limitations and navigation

- Lexical extraction is incomplete for pronouns, implied roles, complex conditions and unrecognised narrative constructions; no unchecked assertion is marked reviewed.
- Only exact definition headings are matched. A missing or pending MDR definition is not evidence of absent business roles.
- Sender is not assumed to be initiator. Functional participant roles are not equated with institutional examples.
- Different publication statements remain distinct. Same-name participants are linked only by explicit labels within source/publication scope.

[Canonical message](index.md) · [Full Functionality and detailed MDR evidence](mdr-evidence.md) · [Issue register](../../../../../tracking/issues.md)
