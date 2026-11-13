---
template: false
document_kind: "business-activity"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p127-process-direct-debit"
title: "Process direct debit"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Direct Debit"], "locator": "/w:document/w:body/w:p[127]", "paragraph_id": "P127", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessProcess Description", "Direct Debit"], "locator": "/w:document/w:body/w:tbl[19]", "paragraph_id": null, "table_id": "T19"}]
participants: ["participant-src-000162-financial-institution", "participant-src-000162-clearing-system", "participant-src-000162-creditor", "participant-src-000162-debtor"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Instruction Messages"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[5]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["pacs.010"]
search_terms: ["Process direct debit", "Financial Institution", "Clearing System", "Creditor", "Debtor", "pacs.010"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
manual_curated: true
table_review: "pass: exact cells, merges, complete Word table context"
---





# Process direct debit

Source context: Payments Clearing and Settlement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The creditor’s agent (or creditor if it is a financial institution direct debit) sends the message to the clearing system in line with the clearing cycle.
The clearing system forwards the message to the debtor’s agent immediately for information purposes only and processes the direct debit in accordance with the settlement cycle, to initiate the debit to the debtor's account.

Evidence: [T19](../documents/src-000162/tables/tbl-0019.md), source row 2.

### Trigger

Release of direct debit instructions to the  instructed agent.

Evidence: [T19](../documents/src-000162/tables/tbl-0019.md), source row 3.

### Pre-conditions

Direct debit instructions received and successfully validated.

Evidence: [T19](../documents/src-000162/tables/tbl-0019.md), source row 4.

### Post-conditions

Forwarded direct debit instructions.

Evidence: [T19](../documents/src-000162/tables/tbl-0019.md), source row 5.

### Role

Financial institution / clearing system

Evidence: [T19](../documents/src-000162/tables/tbl-0019.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Financial Institution | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-financial-institution.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Clearing System | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-clearing-system.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Creditor | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-creditor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Debtor | [Participant](../../../../../../../shared/reference/participants/participant-src-000162-debtor.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T19](../documents/src-000162/tables/tbl-0019.md).

## Messages and alternative paths

Source-supported message family mentions: `pacs.010`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Heading path: BusinessProcess Description / Direct Debit.

<!-- CLEARING-ACTIVITY -->
## Complete source activity conditions

[T19, all rows](../documents/src-000162/tables/tbl-0019.md)

| Item | Description |
| --- | --- |
| Definition | The creditor’s agent (or creditor if it is a financial institution direct debit) sends the message to the clearing system in line with the clearing cycle.<br>The clearing system forwards the message to the debtor’s agent immediately for information purposes only and processes the direct debit in accordance with the settlement cycle, to initiate the debit to the debtor's account. |
| Trigger | Release of direct debit instructions to the  instructed agent. |
| Pre-conditions | Direct debit instructions received and successfully validated. |
| Post-conditions | Forwarded direct debit instructions. |
| Role | Financial institution / clearing system |


[Parent process and participant context](flow-src-000162-p124-direct-debit.md)
<!-- /CLEARING-ACTIVITY -->

## Completed table review

[All48 source tables: exact cells, merged cells and Word-page visual evidence](../../../../../../../evidence/archived/fa67d8621c20bf64aa62336b.md). The cited source activities retain their explicit definitions, conditions, roles and outcomes.
