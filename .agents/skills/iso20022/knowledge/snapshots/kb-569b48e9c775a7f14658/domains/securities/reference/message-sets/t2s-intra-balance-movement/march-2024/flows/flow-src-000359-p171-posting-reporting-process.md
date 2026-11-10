---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p171-posting-reporting-process"
title: "Posting Reporting Process"
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[171]", "paragraph_id": "P171", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:tbl[18]", "paragraph_id": null, "table_id": "T18"}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[172]", "paragraph_id": "P172", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[173]", "paragraph_id": "P173", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[174]", "paragraph_id": "P174", "table_id": null}]
participants: ["participant-src-000359-executing-servicing-party"]
message_mapping_evidence: [{"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[17]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[15]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["camt.066", "camt.084"]
search_terms: ["Posting Reporting Process", "Executing/Servicing Party", "camt.066", "camt.084"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Posting Reporting Process

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The process of reporting, for a given period of time, previously sent intra-balance movement instructions with a status of settled.

Evidence: [T18](../documents/src-000359/tables/tbl-0018.md), source row 2.

### Trigger

The process is triggered by a system event (e.g. end-of-day or end of night-time cycle…).

Evidence: [T18](../documents/src-000359/tables/tbl-0018.md), source row 3.

### Pre-conditions

Static Data configuration satisfying the requirement for reporting of settled intra-balance movement instructions.

Evidence: [T18](../documents/src-000359/tables/tbl-0018.md), source row 4.

### Post-conditions

A valid Intra-Balance Movement Posting report is generated.

Evidence: [T18](../documents/src-000359/tables/tbl-0018.md), source row 5.

### Role

Executing/Servicing Party for the report / Account owner (Receiving Party) of instructions reported by the report.

Evidence: [T18](../documents/src-000359/tables/tbl-0018.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T18](../documents/src-000359/tables/tbl-0018.md).

## Messages and alternative paths

Source-supported message family mentions: `camt.066`, `camt.084`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessProcess Description / Intra-Balance Management.
