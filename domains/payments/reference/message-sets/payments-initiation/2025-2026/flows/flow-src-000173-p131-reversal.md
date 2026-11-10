---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
flow_id: "flow-src-000173-p131-reversal"
title: "Reversal"
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Direct Debit"], "locator": "/w:document/w:body/w:p[131]", "paragraph_id": "P131", "table_id": null}, {"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Direct Debit"], "locator": "/w:document/w:body/w:tbl[21]", "paragraph_id": null, "table_id": "T21"}, {"source_id": "src-000173", "heading_path": ["BusinessProcess Description", "Customer-to-Bank Direct Debit"], "locator": "/w:document/w:body/w:p[132]", "paragraph_id": "P132", "table_id": null}]
participants: ["participant-src-000173-creditor-agent", "participant-src-000173-creditor", "participant-src-000173-debtor"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Reversal", "Creditor Agent", "Creditor", "Debtor"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
issue_ids: ["issue-000044"]
table_review: "pass"
---





# Reversal

Source context: Payments Initiation. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

Creditor identifies the original instruction (or a file of instructions) and generates an offsetting transaction in favour of the debtor under quotation of the reversal reason.

Evidence: [T21](../documents/src-000173/tables/tbl-0021.md), source row 2.

### Trigger

Trigger: reversal of the instruction.

Evidence: [T21](../documents/src-000173/tables/tbl-0021.md), source row 3.

### Pre-conditions

Settled instruction subject to reversal (collected in error).

Evidence: [T21](../documents/src-000173/tables/tbl-0021.md), source row 4.

### Post-conditions

Reversed instruction.

Evidence: [T21](../documents/src-000173/tables/tbl-0021.md), source row 5.

### Role

Creditor agent

Evidence: [T21](../documents/src-000173/tables/tbl-0021.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Creditor Agent | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-creditor-agent.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Creditor | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-creditor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000173-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T21](../documents/src-000173/tables/tbl-0021.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000173](../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx). Heading path: BusinessProcess Description / Customer-to-Bank Direct Debit.

<!-- INITIATION-ACTIVITY -->
## Source-defined purpose, trigger and conditions

[T21, all rows](../documents/src-000173/tables/tbl-0021.md)

| Item | Description |
| --- | --- |
| Definition | Creditor identifies the original instruction (or a file of instructions) and generates an offsetting transaction in favour of the debtor under quotation of the reversal reason. |
| Trigger | Trigger: reversal of the instruction. |
| Pre-conditions | Settled instruction subject to reversal (collected in error). |
| Post-conditions | Reversed instruction. |
| Role | Creditor agent |


[Parent process and participant placement](flow-src-000173-p125-customer-to-bank-direct-debit.md)

Literal Role cell/figure or definition discrepancy remains issue-000044; no participant is silently substituted.
<!-- /INITIATION-ACTIVITY -->
