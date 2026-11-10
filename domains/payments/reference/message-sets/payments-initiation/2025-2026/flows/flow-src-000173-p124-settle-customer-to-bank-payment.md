---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p124-settle-customer-to-bank-payment"
title: "Settle customer-to-bank payment"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:p[124]", "paragraph_id": "P124", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[17]", "paragraph_id": null, "table_id": "T17"}]
participants: ["participant-src-000173-debtor-agent", "participant-src-000173-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Settle customer-to-bank payment", "Debtor Agent", "Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: []
table_review: "pass"
---





# Settle customer-to-bank payment

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Credit transfer between the debit party and the credit party.

Evidence: [T17](../documents/src-000173/tables/tbl-0017.md), source row 2.

### Trigger

Execution date.

Evidence: [T17](../documents/src-000173/tables/tbl-0017.md), source row 3.

### Pre-conditions

Instructed payment is executable (all information is there to process the payment and the payment validity has been checked).

Evidence: [T17](../documents/src-000173/tables/tbl-0017.md), source row 4.

### Post-conditions

Transfer of ownership is performed between the debit party and the credit party.

Evidence: [T17](../documents/src-000173/tables/tbl-0017.md), source row 5.

### Role

Debtor agent

Evidence: [T17](../documents/src-000173/tables/tbl-0017.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Debtor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T17](../documents/src-000173/tables/tbl-0017.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx). Heading path: BusinessProcess Description / Customer-to-Bank Payment Order.

<!-- INITIATION-ACTIVITY -->
## Source-defined purpose, trigger and conditions

[T17, all rows](../documents/src-000173/tables/tbl-0017.md)

| Item | Description |
| --- | --- |
| Definition | Credit transfer between the debit party and the credit party. |
| Trigger | Execution date. |
| Pre-conditions | Instructed payment is executable (all information is there to process the payment and the payment validity has been checked). |
| Post-conditions | Transfer of ownership is performed between the debit party and the credit party. |
| Role | Debtor agent |


[Parent process and participant placement](flow-src-000173-p107-customer-to-bank-payment-order.md)

<!-- /INITIATION-ACTIVITY -->
