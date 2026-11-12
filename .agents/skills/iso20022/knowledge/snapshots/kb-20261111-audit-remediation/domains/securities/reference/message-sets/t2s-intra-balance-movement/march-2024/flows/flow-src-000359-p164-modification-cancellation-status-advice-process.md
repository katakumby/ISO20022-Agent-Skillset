---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p164-modification-cancellation-status-advice-process"
title: "Modification/Cancellation Status Advice Process"
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[164]", "paragraph_id": "P164", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:tbl[13]", "paragraph_id": null, "table_id": "T13"}]
participants: ["participant-src-000359-executing-servicing-party", "participant-src-000359-instructing-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Modification/Cancellation Status Advice Process", "Executing/Servicing Party", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Modification/Cancellation Status Advice Process

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The process of informing the current status of a liquidity restriction modification or cancellation request.

Evidence: [T13](../documents/src-000359/tables/tbl-0013.md), source row 2.

### Trigger

The process is triggered by market infrastructure when the status changes.

Evidence: [T13](../documents/src-000359/tables/tbl-0013.md), source row 3.

### Pre-conditions

Existence of a liquidity restriction modification or cancellation request as received within a market infrastructure.

Evidence: [T13](../documents/src-000359/tables/tbl-0013.md), source row 4.

### Post-conditions

A status change is generated.

Evidence: [T13](../documents/src-000359/tables/tbl-0013.md), source row 5.

### Role

Account owner (Instructing party) - for the receipt of the Status Advice.
Executing/Servicing Party - for the sending of the Status Advice.

Evidence: [T13](../documents/src-000359/tables/tbl-0013.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T13](../documents/src-000359/tables/tbl-0013.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessProcess Description / Intra-Balance Management.
