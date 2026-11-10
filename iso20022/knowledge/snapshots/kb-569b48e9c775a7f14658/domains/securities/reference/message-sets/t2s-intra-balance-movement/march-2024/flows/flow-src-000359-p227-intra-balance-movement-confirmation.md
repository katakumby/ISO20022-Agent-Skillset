---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
flow_id: "flow-src-000359-p227-intra-balance-movement-confirmation"
title: "IntraBalance Movement Confirmation"
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Creation Process ", "In external scenario"], "locator": "/w:document/w:body/w:p[227]", "paragraph_id": "P227", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Creation Process ", "In external scenario"], "locator": "/w:document/w:body/w:p[228]", "paragraph_id": "P228", "table_id": null}, {"source_id": "src-000359", "heading_path": ["BusinessTransactions", "Creation Process ", "In external scenario"], "locator": "/w:document/w:body/w:p[229]", "paragraph_id": "P229", "table_id": null}]
participants: ["participant-src-000359-servicing-executing-party", "participant-src-000359-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000359", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[19]", "paragraph_id": null, "table_id": "T4"}]
message_ids: []
message_families: ["camt.068"]
search_terms: ["IntraBalance Movement Confirmation", "Servicing/Executing Party", "Instructing Party", "camt.068"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# IntraBalance Movement Confirmation

Source context: T2S IntraBalanceMovement. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Servicing/Executing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-servicing-executing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000359-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P228** The Servicing/Executing Party informs the Instructing Party that the Intra-balance movement has been successfully processed either in full mode or in partials. The Servicing/Executing Party presents to the Instructing Party the unique reference number assigned that identifies the restriction.

## Messages and alternative paths

Source-supported message family mentions: `camt.068`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000359](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Heading path: BusinessTransactions / Creation Process  / In external scenario.
