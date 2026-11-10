---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p190-payment-execution-pay-in-arrears"
title: "Payment Execution - Pay In Arrears"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[190]", "paragraph_id": "P190", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[26]", "paragraph_id": null, "table_id": "T26"}]
participants: ["participant-src-000095-intermediary", "participant-src-000095-paying-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Payment Execution - Pay In Arrears", "Intermediary", "Paying Agent"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Payment Execution - Pay In Arrears

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

After execution of the subscription the investor or intermediary pays the payable amount applied or the fund collects the cash money into the investor's account with fund and then deducts the consideration from investor's account on settlement day, returning any excess cash to the investor or collects any additional cash required.

Evidence: [T26](../documents/src-000095/tables/tbl-0026.md), source row 2.

### Trigger

confirmation of the deal execution
payment instruction

Evidence: [T26](../documents/src-000095/tables/tbl-0026.md), source row 3.

### Pre-conditions

Execution is completed.

Evidence: [T26](../documents/src-000095/tables/tbl-0026.md), source row 4.

### Post-conditions

cash is applied to the deal
deal is fully settled
settlement and registration of the units is completed, if not already done

Evidence: [T26](../documents/src-000095/tables/tbl-0026.md), source row 5.

### Role

Paying agent

Evidence: [T26](../documents/src-000095/tables/tbl-0026.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Intermediary | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Paying Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-paying-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T26](../documents/src-000095/tables/tbl-0026.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Heading path: BusinessProcess Description.
