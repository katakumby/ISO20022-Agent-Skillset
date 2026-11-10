---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p170-pending-reporting-process"
title: "Pending Reporting Process"
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[170]", "paragraph_id": "P170", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:tbl[17]", "paragraph_id": null, "table_id": "T17"}]
participants: ["participant-src-000359-executing-servicing-party"]
message_mapping_evidence: [{"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[17]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[16]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["camt.066", "camt.085"]
search_terms: ["Pending Reporting Process", "Executing/Servicing Party", "camt.066", "camt.085"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Pending Reporting Process

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The process of reporting, for a given period of time, previously sent intra-balance movement instructions with a status of pending.

Evidence: [T17](../documents/src-000359/tables/tbl-0017.md), source row 2.

### Trigger

The process is triggered by a system event (e.g. end-of-day or end of night-time cycle…).

Evidence: [T17](../documents/src-000359/tables/tbl-0017.md), source row 3.

### Pre-conditions

Static Data configuration satisfying the requirement for reporting of pending intra-balance movement instructions.

Evidence: [T17](../documents/src-000359/tables/tbl-0017.md), source row 4.

### Post-conditions

A valid Intra-Balance Movement Pending report is generated.

Evidence: [T17](../documents/src-000359/tables/tbl-0017.md), source row 5.

### Role

Executing/Servicing Party for the report / Account owner (Receiving Party) of instructions reported by the report.

Evidence: [T17](../documents/src-000359/tables/tbl-0017.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T17](../documents/src-000359/tables/tbl-0017.md).

## Messages and alternative paths

Source-supported message family mentions: `camt.066`, `camt.085`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessProcess Description / Intra-Balance Management.
