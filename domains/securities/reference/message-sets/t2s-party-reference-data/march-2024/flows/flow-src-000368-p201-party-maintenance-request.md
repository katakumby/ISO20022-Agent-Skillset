---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_sets: ["t2s-party-reference-data"]
flow_id: "flow-src-000368-p201-party-maintenance-request"
title: "Party Maintenance Request"
source_locations: [{"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[201]", "paragraph_id": "P201", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[202]", "paragraph_id": "P202", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[203]", "paragraph_id": "P203", "table_id": null}, {"source_id": "src-000368", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[204]", "paragraph_id": "P204", "table_id": null}]
participants: ["participant-src-000368-executing-servicing-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Party Maintenance Request", "Executing / Servicing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Party Maintenance Request

Source context: T2S PartyReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000368-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P202** The Instruction Party sends an instruction to the Executing/Servicing Party to modify data for a Party. This instruction contains information that uniquely identify the Party. 

**P203** In this instruction, the Instruction Party can also send to the Executing/Servicing Party the request to block/unblock a Party for settlement. 

**P204** In this case, this instruction contains details of the restriction like the restriction type and timeframe.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000368](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Heading path: BusinessTransactions / Modification Process / Confirmation Scenario.
