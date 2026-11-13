---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
flow_id: "flow-src-000368-p144-query-query-response-process"
title: "Query/Query Response process"
source_locations: [{"source_id": "src-000368", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Query/Query Response process"], "locator": "/w:document/w:body/w:p[144]", "paragraph_id": "P144", "table_id": null}, {"source_id": "src-000368", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Query/Query Response process"], "locator": "/w:document/w:body/w:p[145]", "paragraph_id": "P145", "table_id": null}, {"source_id": "src-000368", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Query/Query Response process"], "locator": "/w:document/w:body/w:p[146]", "paragraph_id": "P146", "table_id": null}, {"source_id": "src-000368", "heading_path": ["Description of BusinessActivities", "Party Reference Data", "Query/Query Response process"], "locator": "/w:document/w:body/w:tbl[17]", "paragraph_id": null, "table_id": "T17"}]
participants: ["participant-src-000368-executing-servicing-party", "participant-src-000368-instructing-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Query/Query Response process", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Query/Query Response process

Source context: T2S PartyReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000368-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000368-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source diagram evidence: [fig-0010](../documents/src-000368/diagrams/fig-0010.md). Mermaid reconstruction and visual review are pending.

Source table [T17](../documents/src-000368/tables/tbl-0017.md).

| Source column 1 | Source column 2 | Source column 3 |
| --- | --- | --- |
| Step | Description | Initiator |
| Instruction | Instructing Party instructs Executing/Servicing Party to run a query or Audit Trail Query. | Instructing Party |
| Process Query | Executing/Servicing Party processes the request.<br>In case the processing of the query takes too much time or cannot give any positive response, the Executing/Servicing Party sends an error message back to the Instructing Party with the error code and the related explanation. | Executing/Servicing Party |
| Response | Executing/Services Party sends the response to the Instructing Party according to query results. | Executing/Servicing Party |
| Monitor process | Instructing Party monitors the status of the instruction. | Instructing Party |

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000368](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Heading path: Description of BusinessActivities / Party Reference Data / Query/Query Response process.
