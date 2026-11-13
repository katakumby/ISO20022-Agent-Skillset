---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p189-payment-execution-advance-pay-in"
title: "Payment Execution - Advance Pay In"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[189]", "paragraph_id": "P189", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[25]", "paragraph_id": null, "table_id": "T25"}]
participants: ["participant-src-000095-transfer-agent", "participant-src-000095-intermediary", "participant-src-000095-paying-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Payment Execution - Advance Pay In", "Transfer Agent", "Intermediary", "Paying Agent"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Payment Execution - Advance Pay In

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The investor or intermediary pays or the paying agent/transfer agent collects a cash amount prior to execution. The transfer agent invests the consideration in the investor's account, returning any excess cash to the investor or collecting any additional cash required.

Evidence: [T25](../documents/src-000095/tables/tbl-0025.md), source row 2.

### Trigger

investor decides to invest
payment and instruction are posted

Evidence: [T25](../documents/src-000095/tables/tbl-0025.md), source row 3.

### Pre-conditions

Identification of the account. For a savings plan or direct debit pay-ins: 
completed application form
agreed bank mandate
signed authorisation

Evidence: [T25](../documents/src-000095/tables/tbl-0025.md), source row 4.

### Post-conditions

payment is received
cash is cleared
cash is rejected if not identified
money laundering checks are negative

Evidence: [T25](../documents/src-000095/tables/tbl-0025.md), source row 5.

### Role

Paying agent

Evidence: [T25](../documents/src-000095/tables/tbl-0025.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Intermediary | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Paying Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-paying-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T25](../documents/src-000095/tables/tbl-0025.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Heading path: BusinessProcess Description.
