---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_sets: ["t2s-link-reference-data"]
flow_id: "flow-src-000365-p139-confirmation-scenario"
title: "Confirmation Scenario"
source_locations: [{"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[139]", "paragraph_id": "P139", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[140]", "paragraph_id": "P140", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[141]", "paragraph_id": "P141", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[142]", "paragraph_id": "P142", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[143]", "paragraph_id": "P143", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Creation Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[144]", "paragraph_id": "P144", "table_id": null}]
participants: ["participant-src-000365-executing-servicing-party", "participant-src-000365-instructing-party"]
message_mapping_evidence: []
message_ids: ["reda.045.001.01", "reda.047.001.01", "reda.049.001.01", "reda.051.001.01"]
message_families: ["reda.045", "reda.049", "reda.047", "reda.051"]
search_terms: ["Confirmation Scenario", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
---



# Confirmation Scenario

Source context: T2S LinkReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P140** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing Party.

Source diagram evidence: [fig-0009](../documents/src-000365/diagrams/fig-0009.md). A canonical source reconstruction and actual review evidence are linked below.

**P144** Reference Data Link Creation Request

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000365](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Heading path: BusinessTransactions / Creation Process / Confirmation Scenario.

## Curated source flow

The source shows the request left-to-right, an optional QUEUED advice right-to-left with a dashed line, and the final solid COMPLETED advice. The adjacent narrative says delayed processing might be reported, so QUEUED is not mandatory in every execution. Successful processing returns identification of the link.

[Complete source diagram](../diagrams/curated/fig-0009.md).

### Adjacent source narrative

**P144** Reference Data Link Creation Request

**P145** The Instructing Party sends the instruction to the Executing/Servicing Party to create a new Reference Data Link.  This instruction contains information that clearly identify the Reference Data Link.

**P146** Reference Data Link Status Advice

**P147** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:

**P149** Queued

The Executing/Servicing Party might inform the Instructing party that the processing of the Create Reference Data Link instruction has been delayed.

**P151** Completed

The Executing/Servicing Party informs the Instructing party that the Create Reference Data Link instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the Reference Data Link that has been processed.

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000365-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).
