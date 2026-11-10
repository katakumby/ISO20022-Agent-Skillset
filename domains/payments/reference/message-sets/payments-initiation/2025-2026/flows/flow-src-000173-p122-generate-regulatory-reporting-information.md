---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p122-generate-regulatory-reporting-information"
title: "Generate Regulatory Reporting Information"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:p[122]", "paragraph_id": "P122", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[15]", "paragraph_id": null, "table_id": "T15"}]
participants: ["participant-src-000173-debtor-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Generate Regulatory Reporting Information", "Debtor Agent"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: ["issue-000044"]
table_review: "pass"
---





# Generate Regulatory Reporting Information

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Information from the payment transaction necessary to meet regulatory reporting requirements (for example, balance of payments reporting, reporting on money-laundering issues, etc.).

Evidence: [T15](../documents/src-000173/tables/tbl-0015.md), source row 2.

### Trigger

There are regulatory reporting requirements.

Evidence: [T15](../documents/src-000173/tables/tbl-0015.md), source row 3.

### Pre-conditions

The payment meets regulatory reporting criteria.

Evidence: [T15](../documents/src-000173/tables/tbl-0015.md), source row 4.

### Post-conditions

Information for the regulatory reporting has been extracted based in the information in the payment.

Evidence: [T15](../documents/src-000173/tables/tbl-0015.md), source row 5.

### Role

Debtor agent

Evidence: [T15](../documents/src-000173/tables/tbl-0015.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Debtor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T15](../documents/src-000173/tables/tbl-0015.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx). Heading path: BusinessProcess Description / Customer-to-Bank Payment Order.

<!-- INITIATION-ACTIVITY -->
## Source-defined purpose, trigger and conditions

[T15, all rows](../documents/src-000173/tables/tbl-0015.md)

| Item | Description |
| --- | --- |
| Definition | Information from the payment transaction necessary to meet regulatory reporting requirements (for example, balance of payments reporting, reporting on money-laundering issues, etc.). |
| Trigger | There are regulatory reporting requirements. |
| Pre-conditions | The payment meets regulatory reporting criteria. |
| Post-conditions | Information for the regulatory reporting has been extracted based in the information in the payment. |
| Role | Debtor agent |


[Parent process and participant placement](flow-src-000173-p107-customer-to-bank-payment-order.md)

Literal Role cell/figure or definition discrepancy remains issue-000044; no participant is silently substituted.
<!-- /INITIATION-ACTIVITY -->
