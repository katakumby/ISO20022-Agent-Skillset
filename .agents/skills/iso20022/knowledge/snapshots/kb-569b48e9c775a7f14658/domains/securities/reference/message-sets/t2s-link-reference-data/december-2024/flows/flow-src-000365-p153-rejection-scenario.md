---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_sets: ["t2s-link-reference-data"]
flow_id: "flow-src-000365-p153-rejection-scenario"
title: "Rejection Scenario"
source_locations: [{"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[153]", "paragraph_id": "P153", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[154]", "paragraph_id": "P154", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[155]", "paragraph_id": "P155", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[156]", "paragraph_id": "P156", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[157]", "paragraph_id": "P157", "table_id": null}]
participants: ["participant-src-000365-executing-servicing-party", "participant-src-000365-instructing-party"]
message_mapping_evidence: []
message_ids: ["reda.045.001.01", "reda.047.001.01", "reda.049.001.01", "reda.051.001.01"]
message_families: ["reda.045", "reda.049", "reda.047", "reda.051"]
search_terms: ["Rejection Scenario", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
---



# Rejection Scenario

Source context: T2S LinkReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P154** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party.

Source diagram evidence: [fig-0010](../documents/src-000365/diagrams/fig-0010.md). A canonical source reconstruction and actual review evidence are linked below.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000365](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Heading path: BusinessTransactions / Creation Process / Rejection Scenario.

## Curated source flow

The source shows the request left-to-right, an optional QUEUED advice right-to-left with a dashed line, and the final dashed REJECTED advice. The adjacent narrative says delayed processing might be reported, so QUEUED is not mandatory in every execution. Rejection can occur immediately or after dequeuing/revalidation with changed data. Multiple rejection reasons are permitted; all reasons and the queued alternative are retained in the adjacent source narrative below.

[Complete source diagram](../diagrams/curated/fig-0010.md).

### Adjacent source narrative

**P158** Reference Data Link Creation Request:

**P159** The Instructing Party sends the instruction to the Executing/Servicing Party to create a new Reference Data Link. This instruction contains information that clearly identify the party. 

**P160** Reference Data Link Status Advice:

**P161** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:


**P162** Rejected:
The instruction did not pass validation; some reasons could be:

**P163** the mandatory information is not present or incorrect,

**P164** the instruction is not a new occurrence,

**P165** the instruction has already been received and is being processed. 

**P166** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.


**P167** Queued:
The Executing/Servicing Party might inform the Instructing party that the processing of the Reference Data Link instruction has been delayed.  

**P169** Rejected after dequeuing:
After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P170** the mandatory information is not present or incorrect,

**P171** the instruction is not a new occurrence,

**P172** the instruction has already been received and is being processed. 

**P174** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000365-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).
