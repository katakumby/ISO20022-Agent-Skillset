---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p166-movement-reporting-process"
title: "Movement Reporting Process"
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[166]", "paragraph_id": "P166", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:tbl[15]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[167]", "paragraph_id": "P167", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[168]", "paragraph_id": "P168", "table_id": null}]
participants: ["participant-src-000359-executing-servicing-party"]
message_mapping_evidence: [{"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[9]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[10]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["camt.078", "camt.079"]
search_terms: ["Movement Reporting Process", "Executing/Servicing Party", "camt.078", "camt.079"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Movement Reporting Process

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The process of responding, to a received cash movement query.

Evidence: [T15](../documents/src-000359/tables/tbl-0015.md), source row 2.

### Trigger

The process is triggered by a system event (e.g. end-of-day or end of night-time cycle…).

Evidence: [T15](../documents/src-000359/tables/tbl-0015.md), source row 3.

### Pre-conditions

Receipt of an incoming query.

Evidence: [T15](../documents/src-000359/tables/tbl-0015.md), source row 4.

### Post-conditions

A valid Intra-Balance Movement Query Response is generated containing either a business report or operational error.

Evidence: [T15](../documents/src-000359/tables/tbl-0015.md), source row 5.

### Role

Executing/Servicing Party for the response.

Evidence: [T15](../documents/src-000359/tables/tbl-0015.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T15](../documents/src-000359/tables/tbl-0015.md).

## Messages and alternative paths

Source-supported message family mentions: `camt.078`, `camt.079`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessProcess Description / Intra-Balance Management.
