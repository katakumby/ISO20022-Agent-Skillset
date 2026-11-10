---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p191-payment-execution-pay-out-arrears"
title: "Payment Execution - Pay Out Arrears"
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[191]", "paragraph_id": "P191", "table_id": null}, {"source_id": "src-000095", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[27]", "paragraph_id": null, "table_id": "T27"}]
participants: ["participant-src-000095-transfer-agent", "participant-src-000095-intermediary", "participant-src-000095-paying-agent", "participant-src-000095-custodian"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Payment Execution - Pay Out Arrears", "Transfer Agent", "Intermediary", "Paying Agent", "Custodian"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Payment Execution - Pay Out Arrears

Source context: Investment Funds. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The transfer agent, custodian or paying agent pays out cash to the investor or its intermediary.

Evidence: [T27](../documents/src-000095/tables/tbl-0027.md), source row 2.

### Trigger

maturity of the fund
dividend payment
redemption
excess of an advanced payment
periodical withdrawals
commission has to be paid

Evidence: [T27](../documents/src-000095/tables/tbl-0027.md), source row 3.

### Pre-conditions

fund owes money to the investor
credit balance needs to be paid

Evidence: [T27](../documents/src-000095/tables/tbl-0027.md), source row 4.

### Post-conditions

Balance to be paid is closed

Evidence: [T27](../documents/src-000095/tables/tbl-0027.md), source row 5.

### Role

Paying agent

Evidence: [T27](../documents/src-000095/tables/tbl-0027.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Transfer Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Intermediary | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Paying Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-paying-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Custodian | [Participant](../../../../../../../shared/reference/participants/participant-src-000095-custodian.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T27](../documents/src-000095/tables/tbl-0027.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000095](../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Heading path: BusinessProcess Description.
