---
template: false
document_kind: "business-activity"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p128-process-reject"
title: "Process Reject"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Direct Debit"], "locator": "/w:document/w:body/w:p[128]", "paragraph_id": "P128", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Direct Debit"], "locator": "/w:document/w:body/w:tbl[20]", "paragraph_id": null, "table_id": "T20"}]
participants: ["participant-src-000162-financial-institution"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Process Reject", "Financial Institution"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
table_review: "pass: exact cells, merges, complete Word table context"
---





# Process Reject

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Reconciles reject with the original direct debit instructions and identifies the reason for rejection.  If the reject results from a formatting error, correct the data and resubmit for processing.

Evidence: [T20](../documents/src-000162/tables/tbl-0020.md), source row 2.

### Trigger

Reconciliation of the reject.

Evidence: [T20](../documents/src-000162/tables/tbl-0020.md), source row 3.

### Pre-conditions

Reject received.

Evidence: [T20](../documents/src-000162/tables/tbl-0020.md), source row 4.

### Post-conditions

Reconciled reject.

Evidence: [T20](../documents/src-000162/tables/tbl-0020.md), source row 5.

### Role

Financial institution

Evidence: [T20](../documents/src-000162/tables/tbl-0020.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Financial Institution | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T20](../documents/src-000162/tables/tbl-0020.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Heading path: BusinessProcess Description / Direct Debit.

<!-- CLEARING-ACTIVITY -->
## Complete source activity conditions

[T20, all rows](../documents/src-000162/tables/tbl-0020.md)

| Item | Description |
| --- | --- |
| Definition | Reconciles reject with the original direct debit instructions and identifies the reason for rejection.  If the reject results from a formatting error, correct the data and resubmit for processing. |
| Trigger | Reconciliation of the reject. |
| Pre-conditions | Reject received. |
| Post-conditions | Reconciled reject. |
| Role | Financial institution |


[Parent process and participant context](flow-src-000162-p124-direct-debit.md)
<!-- /CLEARING-ACTIVITY -->

## Completed table review

[All48 source tables: exact cells, merged cells and Word-page visual evidence](../../../../../../../tracking/reviews/payments-clearing-tables.json). The cited source activities retain their explicit definitions, conditions, roles and outcomes.
