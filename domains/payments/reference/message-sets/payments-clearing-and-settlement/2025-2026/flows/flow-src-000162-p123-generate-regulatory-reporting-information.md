---
template: false
document_kind: "business-activity"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p123-generate-regulatory-reporting-information"
title: "Generate Regulatory Reporting Information"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Credit Transfer"], "locator": "/w:document/w:body/w:p[123]", "paragraph_id": "P123", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[18]", "paragraph_id": null, "table_id": "T18"}]
participants: ["participant-src-000162-financial-institution", "participant-src-000162-debtor-agent", "participant-src-000162-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Generate Regulatory Reporting Information", "Financial Institution", "Debtor agent", "Party"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
table_review: "pass: exact cells, merges, complete Word table context"
---





# Generate Regulatory Reporting Information

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Forwarding party or debtor agent selects the information from the payment transaction necessary to meet regulatory reporting requirements, if necessary, for example, balance of payments reporting, reporting on money-laundering issues.

Evidence: [T18](../documents/src-000162/tables/tbl-0018.md), source row 2.

### Trigger

Payment meets the regulatory reporting criteria.

Evidence: [T18](../documents/src-000162/tables/tbl-0018.md), source row 3.

### Pre-conditions

There are regulatory reporting requirements.

Evidence: [T18](../documents/src-000162/tables/tbl-0018.md), source row 4.

### Post-conditions

Information for the regulatory reporting has been extracted based on information in the payment.

Evidence: [T18](../documents/src-000162/tables/tbl-0018.md), source row 5.

### Role

Financial institution

Evidence: [T18](../documents/src-000162/tables/tbl-0018.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Financial Institution | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T18](../documents/src-000162/tables/tbl-0018.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Heading path: BusinessProcess Description / Credit Transfer.

<!-- CLEARING-ACTIVITY -->
## Complete source activity conditions

[T18, all rows](../documents/src-000162/tables/tbl-0018.md)

| Item | Description |
| --- | --- |
| Definition | Forwarding party or debtor agent selects the information from the payment transaction necessary to meet regulatory reporting requirements, if necessary, for example, balance of payments reporting, reporting on money-laundering issues. |
| Trigger | Payment meets the regulatory reporting criteria. |
| Pre-conditions | There are regulatory reporting requirements. |
| Post-conditions | Information for the regulatory reporting has been extracted based on information in the payment. |
| Role | Financial institution |


[Parent process and participant context](flow-src-000162-p111-credit-transfer.md)
<!-- /CLEARING-ACTIVITY -->

## Completed table review

[All48 source tables: exact cells, merged cells and Word-page visual evidence](../../../../../../../tracking/reviews/payments-clearing-tables.json). The cited source activities retain their explicit definitions, conditions, roles and outcomes.
