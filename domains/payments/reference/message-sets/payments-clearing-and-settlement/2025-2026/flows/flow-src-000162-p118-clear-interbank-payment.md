---
template: false
document_kind: "business-activity"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p118-clear-interbank-payment"
title: "Clear Interbank Payment"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Credit Transfer"], "locator": "/w:document/w:body/w:p[118]", "paragraph_id": "P118", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[13]", "paragraph_id": null, "table_id": "T13"}]
participants: ["participant-src-000162-payment-clearing-agent", "participant-src-000162-financial-institution", "participant-src-000162-clearing-system"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Clear Interbank Payment", "Payment Clearing Agent", "Financial Institution", "Clearing System"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
table_review: "pass: exact cells, merges, complete Word table context"
---





# Clear Interbank Payment

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Preparation of the payment information by the payment clearing agent for the next clearing agent in the interbank chain. This process of preparing payment information can be divided into the sub-processes 'Sort payment' and 'prepare onward interbank payment'.

Evidence: [T13](../documents/src-000162/tables/tbl-0013.md), source row 2.

### Trigger

Payment execution date is reached.

Evidence: [T13](../documents/src-000162/tables/tbl-0013.md), source row 3.

### Pre-conditions

Payment is accepted.

Evidence: [T13](../documents/src-000162/tables/tbl-0013.md), source row 4.

### Post-conditions

Next clearing agent is determined.

Evidence: [T13](../documents/src-000162/tables/tbl-0013.md), source row 5.

### Role

Clearing system or financial institution

Evidence: [T13](../documents/src-000162/tables/tbl-0013.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Payment Clearing Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-payment-clearing-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Financial Institution | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Clearing System | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-clearing-system.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T13](../documents/src-000162/tables/tbl-0013.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Heading path: BusinessProcess Description / Credit Transfer.

<!-- CLEARING-ACTIVITY -->
## Complete source activity conditions

[T13, all rows](../documents/src-000162/tables/tbl-0013.md)

| Item | Description |
| --- | --- |
| Definition | Preparation of the payment information by the payment clearing agent for the next clearing agent in the interbank chain. This process of preparing payment information can be divided into the sub-processes 'Sort payment' and 'prepare onward interbank payment'. |
| Trigger | Payment execution date is reached. |
| Pre-conditions | Payment is accepted. |
| Post-conditions | Next clearing agent is determined. |
| Role | Clearing system or financial institution |


[Parent process and participant context](flow-src-000162-p111-credit-transfer.md)
<!-- /CLEARING-ACTIVITY -->

## Completed table review

[All48 source tables: exact cells, merged cells and Word-page visual evidence](../../../../../../../tracking/reviews/payments-clearing-tables.json). The cited source activities retain their explicit definitions, conditions, roles and outcomes.
