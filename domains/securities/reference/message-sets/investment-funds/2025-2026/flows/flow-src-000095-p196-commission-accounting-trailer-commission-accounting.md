---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p196-commission-accounting-trailer-commission-accounting"
title: "Commission Accounting / Trailer Commission Accounting"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[196]", "paragraph_id": "P196", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[32]", "paragraph_id": null, "table_id": "T32"}]
participants: ["participant-src-000095-fund-accountant", "participant-src-000095-transfer-agent", "participant-src-000095-intermediary"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Commission Accounting / Trailer Commission Accounting", "Fund Accountant", "Transfer Agent", "Intermediary"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Commission Accounting / Trailer Commission Accounting

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Identification and calculation of rebate of management fee based on the holdings position level of the investor accounts with the intermediary and/or based on a lot of transactions linked to a specific intermediary.

Evidence: [T32](../documents/src-000095/tables/tbl-0032.md), source row 2.

### Trigger

upon request
calendar date is reached
SLA dependent

Evidence: [T32](../documents/src-000095/tables/tbl-0032.md), source row 3.

### Pre-conditions

assets/accounts linked to an intermediary
fee structure is known

Evidence: [T32](../documents/src-000095/tables/tbl-0032.md), source row 4.

### Post-conditions

commission payment or accruals are to be initiated on a holding level
commission details are created at the level of the intermediary

Evidence: [T32](../documents/src-000095/tables/tbl-0032.md), source row 5.

### Role

Fund accountant/transfer agent

Evidence: [T32](../documents/src-000095/tables/tbl-0032.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Fund Accountant | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-fund-accountant.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Intermediary | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T32](../documents/src-000095/tables/tbl-0032.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Heading path: BusinessProcess Description.
