---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p121-assess-customer-to-bank-payment-risk"
title: "Assess Customer-to-Bank-Payment Risk"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:p[121]", "paragraph_id": "P121", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Payment Order"], "locator": "/w:document/w:body/w:tbl[14]", "paragraph_id": null, "table_id": "T14"}]
participants: ["participant-src-000173-creditor-agent", "participant-src-000173-debtor-agent"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Assess Customer-to-Bank-Payment Risk", "Creditor Agent", "Debtor Agent"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: []
table_review: "pass"
---





# Assess Customer-to-Bank-Payment Risk

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Necessary risk checks in order to execute and process the payment further. It can be 'assess static risk', for example, checking of embargo, and 'assess dynamic risk' (check sufficient cash on account, cover received, etc.).

Evidence: [T14](../documents/src-000173/tables/tbl-0014.md), source row 2.

### Trigger

The payment has been validated and risk criteria have been established.

Evidence: [T14](../documents/src-000173/tables/tbl-0014.md), source row 3.

### Pre-conditions

Receipt of payment order, positive authorisation and validation check.

Evidence: [T14](../documents/src-000173/tables/tbl-0014.md), source row 4.

### Post-conditions

The payment or is executable (all information is there to process the payment and the payment risk assessment had been checked).

Evidence: [T14](../documents/src-000173/tables/tbl-0014.md), source row 5.

### Role

Debtor agent or creditor agent

Evidence: [T14](../documents/src-000173/tables/tbl-0014.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Creditor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T14](../documents/src-000173/tables/tbl-0014.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Heading path: BusinessProcess Description / Customer-to-Bank Payment Order.

<!-- INITIATION-ACTIVITY -->
## Source-defined purpose, trigger and conditions

[T14, all rows](../documents/src-000173/tables/tbl-0014.md)

| Item | Description |
| --- | --- |
| Definition | Necessary risk checks in order to execute and process the payment further. It can be 'assess static risk', for example, checking of embargo, and 'assess dynamic risk' (check sufficient cash on account, cover received, etc.). |
| Trigger | The payment has been validated and risk criteria have been established. |
| Pre-conditions | Receipt of payment order, positive authorisation and validation check. |
| Post-conditions | The payment or is executable (all information is there to process the payment and the payment risk assessment had been checked). |
| Role | Debtor agent or creditor agent |


[Parent process and participant placement](flow-src-000173-p107-customer-to-bank-payment-order.md)

<!-- /INITIATION-ACTIVITY -->
