---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p187-order-execution"
title: "Order Execution"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[187]", "paragraph_id": "P187", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[23]", "paragraph_id": null, "table_id": "T23"}]
participants: ["participant-src-000095-executing-party", "participant-src-000095-transfer-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Order Execution", "Executing Party", "Transfer Agent"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Order Execution

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The transfer agent books and executes an instruction to buy, sell, transfer or switch between units in one or more funds.

Evidence: [T23](../documents/src-000095/tables/tbl-0023.md), source row 2.

### Trigger

trade date and cut-off time of the fund is reached
instruction has been accepted by the fund company
instruction has been processed by the transfer agent

Evidence: [T23](../documents/src-000095/tables/tbl-0023.md), source row 3.

### Pre-conditions

valid instruction is received. 
quantities and amounts associated with the instruction have been calculated

Evidence: [T23](../documents/src-000095/tables/tbl-0023.md), source row 4.

### Post-conditions

quantities and amounts resulting from the execution of the instruction have been calculated
units are issued or redeemed
execution details are confirmed

Evidence: [T23](../documents/src-000095/tables/tbl-0023.md), source row 5.

### Role

Executing party

Evidence: [T23](../documents/src-000095/tables/tbl-0023.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T23](../documents/src-000095/tables/tbl-0023.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Heading path: BusinessProcess Description.
