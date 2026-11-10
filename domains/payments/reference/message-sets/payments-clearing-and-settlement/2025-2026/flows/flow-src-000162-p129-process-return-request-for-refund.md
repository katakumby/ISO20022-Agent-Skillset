---
template: false
document_kind: "business-activity"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p129-process-return-request-for-refund"
title: "Process Return/Request for Refund"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Direct Debit"], "locator": "/w:document/w:body/w:p[129]", "paragraph_id": "P129", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Direct Debit"], "locator": "/w:document/w:body/w:tbl[21]", "paragraph_id": null, "table_id": "T21"}]
participants: ["participant-src-000162-financial-institution", "participant-src-000162-creditor", "participant-src-000162-debtor", "participant-src-000162-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Process Return/Request for Refund", "Financial Institution", "Creditor", "Debtor", "Party"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
table_review: "pass: exact cells, merges, complete Word table context"
---





# Process Return/Request for Refund

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Returns are individual debits that have reached the debtor’s agent and have been settled at the inter-bank level, but the debtor’s agent is then unable to make the collection for one of a number of reasons, for example, account closed, no funds, customer dead, etc. 
The debtor has the unconditional right during "n" days after a debit to instruct its bank to revoke the debit. Following that instruction the debtor's account is credited by its bank and the debit is returned electronically through the clearing process to the creditor’s agent.

Evidence: [T21](../documents/src-000162/tables/tbl-0021.md), source row 2.

### Trigger

Return of a direct debit / request for refund.

Evidence: [T21](../documents/src-000162/tables/tbl-0021.md), source row 3.

### Pre-conditions

Settled direct debit instruction subject for return / refund.

Evidence: [T21](../documents/src-000162/tables/tbl-0021.md), source row 4.

### Post-conditions

Returned direct debit instruction / requested refund.

Evidence: [T21](../documents/src-000162/tables/tbl-0021.md), source row 5.

### Role

Financial institution or party

Evidence: [T21](../documents/src-000162/tables/tbl-0021.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Financial Institution | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Creditor | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T21](../documents/src-000162/tables/tbl-0021.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Heading path: BusinessProcess Description / Direct Debit.

<!-- CLEARING-ACTIVITY -->
## Complete source activity conditions

[T21, all rows](../documents/src-000162/tables/tbl-0021.md)

| Item | Description |
| --- | --- |
| Definition | Returns are individual debits that have reached the debtor’s agent and have been settled at the inter-bank level, but the debtor’s agent is then unable to make the collection for one of a number of reasons, for example, account closed, no funds, customer dead, etc. <br>The debtor has the unconditional right during "n" days after a debit to instruct its bank to revoke the debit. Following that instruction the debtor's account is credited by its bank and the debit is returned electronically through the clearing process to the creditor’s agent. |
| Trigger | Return of a direct debit / request for refund. |
| Pre-conditions | Settled direct debit instruction subject for return / refund. |
| Post-conditions | Returned direct debit instruction / requested refund. |
| Role | Financial institution or party |


[Parent process and participant context](flow-src-000162-p124-direct-debit.md)
<!-- /CLEARING-ACTIVITY -->

## Completed table review

[All48 source tables: exact cells, merged cells and Word-page visual evidence](../../../../../../../tracking/reviews/payments-clearing-tables.json). The cited source activities retain their explicit definitions, conditions, roles and outcomes.
