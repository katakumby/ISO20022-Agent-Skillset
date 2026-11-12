---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p279-intra-balance-movement-modification-report"
title: "IntraBalance Movement Modification Report"
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Modification/Cancellation Query and Report Process", "Requesting an Intra Balance Modification Query"], "locator": "/w:document/w:body/w:p[279]", "paragraph_id": "P279", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Modification/Cancellation Query and Report Process", "Requesting an Intra Balance Modification Query"], "locator": "/w:document/w:body/w:p[280]", "paragraph_id": "P280", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Modification/Cancellation Query and Report Process", "Requesting an Intra Balance Modification Query"], "locator": "/w:document/w:body/w:p[281]", "paragraph_id": "P281", "table_id": null}]
participants: ["participant-src-000359-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[12]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["camt.081"]
search_terms: ["IntraBalance Movement Modification Report", "Instructing Party", "camt.081"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# IntraBalance Movement Modification Report

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P280** The Servicing party sends to the Instructing party the response of the query with the full details of the Intra-Balance Movement Modification Instruction/s that fulfilled the selection criteria.

## Messages and alternative paths

Source-supported message family mentions: `camt.081`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessTransactions / Intra-Balance Movement Modification/Cancellation Query and Report Process / Requesting an Intra Balance Modification Query.
