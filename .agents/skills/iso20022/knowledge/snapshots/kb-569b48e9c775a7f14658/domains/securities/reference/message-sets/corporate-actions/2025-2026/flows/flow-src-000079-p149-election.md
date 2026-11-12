---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p149-election"
title: "Election"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[149]", "paragraph_id": "P149", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[14]", "paragraph_id": null, "table_id": "T14"}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instructions and Cancellations"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000080", "locator": "file page 274; 5 seev.033.001.14 CorporateActionInstructionV14"}]
message_ids: []
message_families: ["seev.033"]
search_terms: ["Election", "Account Servicer", "Account Owner", "seev.033"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Election

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The process of providing the account servicer with instructions on how the account owner wishes to proceed with the corporate action event. The account owner can request the cancellation of a previously sent corporate action instruction.

Evidence: [T14](../documents/src-000079/tables/tbl-0014.md), source row 2.

### Trigger

account owner has been advised of corporate action event details with sufficient details to respond 
account owner has a standing instruction at the account servicer
account servicer instruction deadline, the default option can trigger the process.

Evidence: [T14](../documents/src-000079/tables/tbl-0014.md), source row 3.

### Pre-conditions

Corporate action event is voluntary or mandatory with options and is not withdrawn

Evidence: [T14](../documents/src-000079/tables/tbl-0014.md), source row 4.

### Post-conditions

Account servicer has the necessary details and instructions to carry out processing and transactions relating to the corporate action event

Evidence: [T14](../documents/src-000079/tables/tbl-0014.md), source row 5.

### Role

Account owner

Evidence: [T14](../documents/src-000079/tables/tbl-0014.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T14](../documents/src-000079/tables/tbl-0014.md).

## Messages and alternative paths

Source-supported message family mentions: `seev.033`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: BusinessProcess Description.
