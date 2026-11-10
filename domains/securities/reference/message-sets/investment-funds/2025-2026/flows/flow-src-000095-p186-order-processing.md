---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p186-order-processing"
title: "Order Processing"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[186]", "paragraph_id": "P186", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[22]", "paragraph_id": null, "table_id": "T22"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-intermediary"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Order Processing", "Instructing Party", "Intermediary"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Order Processing

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

An investor places an instruction to subscribe to, redeem from, transfer or switch between units in one or more funds.

Evidence: [T22](../documents/src-000095/tables/tbl-0022.md), source row 2.

### Trigger

investor/intermediary decision
corporate action event
standing instruction, for example, saving plans or saving schemes

Evidence: [T22](../documents/src-000095/tables/tbl-0022.md), source row 3.

### Pre-conditions

valid account exists
fund exists
credit limit exists (for subscription), if required
for switch or redemption, the units in the account are settled/created
order respects the terms set out in the prospectus
instructing party is validated and verified

Evidence: [T22](../documents/src-000095/tables/tbl-0022.md), source row 4.

### Post-conditions

Valid instruction is generated

Evidence: [T22](../documents/src-000095/tables/tbl-0022.md), source row 5.

### Role

Instructing party

Evidence: [T22](../documents/src-000095/tables/tbl-0022.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Intermediary | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T22](../documents/src-000095/tables/tbl-0022.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Heading path: BusinessProcess Description.
