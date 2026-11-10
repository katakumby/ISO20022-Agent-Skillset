---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p188-payment-execution"
title: "Payment Execution"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[188]", "paragraph_id": "P188", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[24]", "paragraph_id": null, "table_id": "T24"}]
participants: ["participant-src-000095-intermediary", "participant-src-000095-paying-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Payment Execution", "Intermediary", "Paying Agent"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Payment Execution

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The investor or the intermediary pays for the fund units or the appointed agent collects a cash subscription into the investor's account (possibly prior to execution) and then deducts the consideration from the investor's account on settlement day, returning any excess cash to the investor or collecting any additional cash required.

Evidence: [T24](../documents/src-000095/tables/tbl-0024.md), source row 2.

### Trigger

Deal confirmation

Evidence: [T24](../documents/src-000095/tables/tbl-0024.md), source row 3.

### Pre-conditions

confirmation that the deal was executed
value date of the payment is defined

Evidence: [T24](../documents/src-000095/tables/tbl-0024.md), source row 4.

### Post-conditions

Depends on the type of payment method

Evidence: [T24](../documents/src-000095/tables/tbl-0024.md), source row 5.

### Role

Paying agent

Evidence: [T24](../documents/src-000095/tables/tbl-0024.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Intermediary | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Paying Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-paying-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T24](../documents/src-000095/tables/tbl-0024.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Heading path: BusinessProcess Description.
