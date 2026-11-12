---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p161-modification-process"
title: "Modification Process"
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[161]", "paragraph_id": "P161", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:tbl[11]", "paragraph_id": null, "table_id": "T11"}]
participants: ["participant-src-000359-executing-servicing-party", "participant-src-000359-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[17]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["camt.066"]
search_terms: ["Modification Process", "Executing/Servicing Party", "Instructing Party", "camt.066"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Modification Process

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The process to request the modification of process indicators or other information as concerns a previously sent intra-balance movement instruction.

Evidence: [T11](../documents/src-000359/tables/tbl-0011.md), source row 2.

### Trigger

The process is triggered by an instructing party decision to alter an intra-balance movement instruction.

Evidence: [T11](../documents/src-000359/tables/tbl-0011.md), source row 3.

### Pre-conditions

Existence of a liquidity restriction instruction.

Evidence: [T11](../documents/src-000359/tables/tbl-0011.md), source row 4.

### Post-conditions

A valid liquidity restriction modification request is generated.

Evidence: [T11](../documents/src-000359/tables/tbl-0011.md), source row 5.

### Role

Instructing Party - for the modification request.
Executing/Servicing Party - for the receipt of the modification request.

Evidence: [T11](../documents/src-000359/tables/tbl-0011.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T11](../documents/src-000359/tables/tbl-0011.md).

## Messages and alternative paths

Source-supported message family mentions: `camt.066`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessProcess Description / Intra-Balance Management.
