---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p158-movement-process"
title: "Movement Process"
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[158]", "paragraph_id": "P158", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:tbl[8]", "paragraph_id": null, "table_id": "T8"}]
participants: ["participant-src-000359-executing-servicing-party", "participant-src-000359-instructing-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Movement Process", "Executing/Servicing Party", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Movement Process

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The process of enabling the movement of liquidity between sub-balances within the holdings of an account owner in order to proceed with a liquidity restriction.

Evidence: [T8](../documents/src-000359/tables/tbl-0008.md), source row 2.

### Trigger

The process is triggered by an instructing party decision or a market infrastructure generated instruction resulting in an intra-balance movement.

Evidence: [T8](../documents/src-000359/tables/tbl-0008.md), source row 3.

### Pre-conditions

Existence of sub-balances on a cash account held within a market infrastructure.

Evidence: [T8](../documents/src-000359/tables/tbl-0008.md), source row 4.

### Post-conditions

A valid liquidity restriction is generated.

Evidence: [T8](../documents/src-000359/tables/tbl-0008.md), source row 5.

### Role

Instructing party for the movement instruction.
Executing/Servicing Party for the receipt of the movement instruction.

Evidence: [T8](../documents/src-000359/tables/tbl-0008.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing/Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T8](../documents/src-000359/tables/tbl-0008.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessProcess Description / Intra-Balance Management.
