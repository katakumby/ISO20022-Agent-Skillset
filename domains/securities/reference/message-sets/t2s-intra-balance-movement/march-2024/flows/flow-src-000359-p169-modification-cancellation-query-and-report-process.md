---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p169-modification-cancellation-query-and-report-process"
title: "Modification/Cancellation Query and Report Process"
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[169]", "paragraph_id": "P169", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:tbl[16]", "paragraph_id": null, "table_id": "T16"}]
participants: ["participant-src-000359-executing-servicing-party", "participant-src-000359-instructing-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Modification/Cancellation Query and Report Process", "Executing/Servicing Party", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Modification/Cancellation Query and Report Process

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The Instructing Party asks the Servicing Party a response to a query concerning a previously sent intra-balance movement cancellation instruction/modification.

Evidence: [T16](../documents/src-000359/tables/tbl-0016.md), source row 2.

### Trigger

The process is triggered either by the system at the end-of-date event or by the receipt of a query request. 

Evidence: [T16](../documents/src-000359/tables/tbl-0016.md), source row 3.

### Pre-conditions

Existence of an intra-balance cancellation instruction/modification.

Evidence: [T16](../documents/src-000359/tables/tbl-0016.md), source row 4.

### Post-conditions

The acknowledgement of the processing of the query and the generation of a valid intra-balance movement cancellation/modification report.

Evidence: [T16](../documents/src-000359/tables/tbl-0016.md), source row 5.

### Role

Account owner (Instructing Party) for the Query.
Executing/Servicing Party for the Report.

Evidence: [T16](../documents/src-000359/tables/tbl-0016.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T16](../documents/src-000359/tables/tbl-0016.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessProcess Description / Intra-Balance Management.
