---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p165-movement-querying-process"
title: "Movement Querying Process"
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:p[165]", "paragraph_id": "P165", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"], "locator": "/w:document/w:body/w:tbl[14]", "paragraph_id": null, "table_id": "T14"}]
participants: ["participant-src-000359-instructing-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Movement Querying Process", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Movement Querying Process

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

The process of enabling the reconciliation of cash movements through the querying of available and necessary data using defined selection criteria.

Evidence: [T14](../documents/src-000359/tables/tbl-0014.md), source row 2.

### Trigger

The process is triggered by reconciliation processing (e.g. missing instructions or system errors) resulting in the sending of a query request by the Instructing Party.

Evidence: [T14](../documents/src-000359/tables/tbl-0014.md), source row 3.

### Pre-conditions

Instructing Party must hold necessary privileges within the Static Data configuration.

Evidence: [T14](../documents/src-000359/tables/tbl-0014.md), source row 4.

### Post-conditions

None.

Evidence: [T14](../documents/src-000359/tables/tbl-0014.md), source row 5.

### Role

Instructing Party for the Query. 

Evidence: [T14](../documents/src-000359/tables/tbl-0014.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T14](../documents/src-000359/tables/tbl-0014.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessProcess Description / Intra-Balance Management.
