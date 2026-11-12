---
template: false
document_kind: "business-activity"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p130-process-reversal"
title: "Process Reversal"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Direct Debit"], "locator": "/w:document/w:body/w:p[130]", "paragraph_id": "P130", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Direct Debit"], "locator": "/w:document/w:body/w:tbl[22]", "paragraph_id": null, "table_id": "T22"}, {"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Direct Debit"], "locator": "/w:document/w:body/w:p[131]", "paragraph_id": "P131", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Direct Debit"], "locator": "/w:document/w:body/w:p[132]", "paragraph_id": "P132", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Direct Debit"], "locator": "/w:document/w:body/w:p[133]", "paragraph_id": "P133", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Direct Debit"], "locator": "/w:document/w:body/w:p[134]", "paragraph_id": "P134", "table_id": null}]
participants: ["participant-src-000162-financial-institution", "participant-src-000162-debtor"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Process Reversal", "Financial Institution", "Debtor"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
table_review: "pass: exact cells, merges, complete Word table context"
---





# Process Reversal

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The direct debit reversal will contain sufficient information which allows the debtor’s agent to identify it as a "reversal' of a particular direct debit. The debtor’s agent will credit debtor's account under quotation of the original direct debit reference and the reason for reversal.  

Evidence: [T22](../documents/src-000162/tables/tbl-0022.md), source row 2.

### Trigger

Accounting and reporting of the direct debit reversal instruction

Evidence: [T22](../documents/src-000162/tables/tbl-0022.md), source row 3.

### Pre-conditions

Direct debit reversal received and successfully validated

Evidence: [T22](../documents/src-000162/tables/tbl-0022.md), source row 4.

### Post-conditions

Reversed direct debit instruction

Evidence: [T22](../documents/src-000162/tables/tbl-0022.md), source row 5.

### Role

Financial institution

Evidence: [T22](../documents/src-000162/tables/tbl-0022.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Financial Institution | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T22](../documents/src-000162/tables/tbl-0022.md).

**P131** The process cancellation/revocation is out of scope.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Heading path: BusinessProcess Description / Direct Debit.

<!-- CLEARING-ACTIVITY -->
## Complete source activity conditions

[T22, all rows](../documents/src-000162/tables/tbl-0022.md)

| Item | Description |
| --- | --- |
| Definition | The direct debit reversal will contain sufficient information which allows the debtor’s agent to identify it as a "reversal' of a particular direct debit. The debtor’s agent will credit debtor's account under quotation of the original direct debit reference and the reason for reversal.   |
| Trigger | Accounting and reporting of the direct debit reversal instruction |
| Pre-conditions | Direct debit reversal received and successfully validated |
| Post-conditions | Reversed direct debit instruction |
| Role | Financial institution |


[Parent process and participant context](flow-src-000162-p124-direct-debit.md)
<!-- /CLEARING-ACTIVITY -->

## Completed table review

[All48 source tables: exact cells, merged cells and Word-page visual evidence](../../../../../../../tracking/reviews/payments-clearing-tables.json). The cited source activities retain their explicit definitions, conditions, roles and outcomes.
