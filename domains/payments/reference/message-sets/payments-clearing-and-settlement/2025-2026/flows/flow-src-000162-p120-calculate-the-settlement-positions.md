---
template: false
document_kind: "business-activity"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p120-calculate-the-settlement-positions"
title: "Calculate the Settlement Positions"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Credit Transfer"], "locator": "/w:document/w:body/w:p[120]", "paragraph_id": "P120", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[15]", "paragraph_id": null, "table_id": "T15"}]
participants: ["participant-src-000162-financial-institution", "participant-src-000162-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Calculate the Settlement Positions", "Financial Institution", "Party"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
table_review: "pass: exact cells, merges, complete Word table context"
---





# Calculate the Settlement Positions

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Clearing agent applies the payment amount to the debit party and credit party's clearing positions. For multiple payments, it is equivalent to calculate the sub-settlement positions. The calculation may be done continuously or at certain times through bilateral netting. The settlement may be delegated to a third party.

Evidence: [T15](../documents/src-000162/tables/tbl-0015.md), source row 2.

### Trigger

Payment has been accepted.

Evidence: [T15](../documents/src-000162/tables/tbl-0015.md), source row 3.

### Pre-conditions

Payment is executable.

Evidence: [T15](../documents/src-000162/tables/tbl-0015.md), source row 4.

### Post-conditions

Payment amount is applied to the debit and credit party.

Evidence: [T15](../documents/src-000162/tables/tbl-0015.md), source row 5.

### Role

Financial institution

Evidence: [T15](../documents/src-000162/tables/tbl-0015.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Financial Institution | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T15](../documents/src-000162/tables/tbl-0015.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Heading path: BusinessProcess Description / Credit Transfer.

<!-- CLEARING-ACTIVITY -->
## Complete source activity conditions

[T15, all rows](../documents/src-000162/tables/tbl-0015.md)

| Item | Description |
| --- | --- |
| Definition | Clearing agent applies the payment amount to the debit party and credit party's clearing positions. For multiple payments, it is equivalent to calculate the sub-settlement positions. The calculation may be done continuously or at certain times through bilateral netting. The settlement may be delegated to a third party. |
| Trigger | Payment has been accepted. |
| Pre-conditions | Payment is executable. |
| Post-conditions | Payment amount is applied to the debit and credit party. |
| Role | Financial institution |


[Parent process and participant context](flow-src-000162-p111-credit-transfer.md)
<!-- /CLEARING-ACTIVITY -->

## Completed table review

[All48 source tables: exact cells, merged cells and Word-page visual evidence](../../../../../../../tracking/reviews/payments-clearing-tables.json). The cited source activities retain their explicit definitions, conditions, roles and outcomes.
