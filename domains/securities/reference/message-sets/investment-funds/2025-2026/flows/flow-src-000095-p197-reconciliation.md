---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p197-reconciliation"
title: "Reconciliation"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[197]", "paragraph_id": "P197", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[198]", "paragraph_id": "P198", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[33]", "paragraph_id": null, "table_id": "T33"}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Reconciliation"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Reconciliation

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Records (shares and cash) and account details on the books of a party are compared/matched and brought into conformity with the records and account details on the books of another party, through the identification of discrepancies, determination of the correct value for any item where a discrepancy exists, and modification of the books of one or both parties to result in the correct value enabling full reconciliation of both parties.
Custody reporting
Accounting reporting
Transactions reporting
Transparency of holdings reporting: provides transparency and the breakdown structure of the underlying holdings through a chain of custodians of one or several financial instruments.

Evidence: [T33](../documents/src-000095/tables/tbl-0033.md), source row 2.

### Trigger

time period as defined in SLA
time period as defined by regulator
on request
completion of any transaction that affects account balances
corporate event

Evidence: [T33](../documents/src-000095/tables/tbl-0033.md), source row 3.

### Pre-conditions

both parties involved maintain records for an account that is recognisably the same account
both parties agree on the reconciliation process

Evidence: [T33](../documents/src-000095/tables/tbl-0033.md), source row 4.

### Post-conditions

parties agree (verbally, in writing) as to account details and balances, otherwise repeat process
reconciliation is completed

Evidence: [T33](../documents/src-000095/tables/tbl-0033.md), source row 5.

### Role

Account servicer, account servicer

Evidence: [T33](../documents/src-000095/tables/tbl-0033.md), source row 6.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

Source diagram evidence: [fig-0004](../documents/src-000095/diagrams/fig-0004.md). Mermaid reconstruction and visual review are pending.

Source table [T33](../documents/src-000095/tables/tbl-0033.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Heading path: BusinessProcess Description.
