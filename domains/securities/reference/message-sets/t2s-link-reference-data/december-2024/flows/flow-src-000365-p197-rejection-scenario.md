---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_sets: ["t2s-link-reference-data"]
flow_id: "flow-src-000365-p197-rejection-scenario"
title: "Rejection Scenario"
source_locations: [{"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[197]", "paragraph_id": "P197", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[198]", "paragraph_id": "P198", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[199]", "paragraph_id": "P199", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[200]", "paragraph_id": "P200", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[201]", "paragraph_id": "P201", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[202]", "paragraph_id": "P202", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[203]", "paragraph_id": "P203", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[204]", "paragraph_id": "P204", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[205]", "paragraph_id": "P205", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[206]", "paragraph_id": "P206", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[207]", "paragraph_id": "P207", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[208]", "paragraph_id": "P208", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[209]", "paragraph_id": "P209", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[210]", "paragraph_id": "P210", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[211]", "paragraph_id": "P211", "table_id": null}]
participants: ["participant-src-000365-csd", "participant-src-000365-executing-servicing-party", "participant-src-000365-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000365", "heading_path": ["Scope and Functionality", "Scope", "Groups", "Link Creation and Maintenance"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000365", "heading_path": ["Scope and Functionality", "Scope", "Groups", "Link Creation and Maintenance"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[7]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.046.001.01", "reda.047.001.01", "reda.050.001.01", "reda.051.001.01"]
message_families: ["reda.046", "reda.050", "reda.047", "reda.051"]
search_terms: ["Rejection Scenario", "Executing / Servicing Party", "Instructing Party", "CSD", "reda.046", "reda.047", "reda.050", "reda.051"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
issue_ids: ["issue-000049"]
---





# Rejection Scenario

Source context: T2S LinkReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CSD | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-csd.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P198** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party

**P200** Security CSD Link/Account Link Maintenance Request (reda.046/reda.050)Modification processSecurity CSD Link/Account Link Status Advice (reda.047/reda.051): QUEUEDSecurity CSD Link/Account Link Status Advice (reda.047/reda.051): REJECTEDSecurity CSD Link/Account Link Maintenance Request (reda.046/reda.050)Modification processSecurity CSD Link/Account Link Status Advice (reda.047/reda.051): QUEUEDSecurity CSD Link/Account Link Status Advice (reda.047/reda.051): REJECTED

Source diagram evidence: [fig-0012](../documents/src-000365/diagrams/fig-0012.md). A canonical source reconstruction and actual review evidence are linked below.

## Messages and alternative paths

Source-supported message family mentions: `reda.046`, `reda.047`, `reda.050`, `reda.051`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000365](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Heading path: BusinessTransactions / Modification Process / Rejection Scenario.

## Curated source flow

The source shows the request left-to-right, an optional QUEUED advice right-to-left with a dashed line, and the final dashed REJECTED advice. The adjacent narrative says delayed processing might be reported, so QUEUED is not mandatory in every execution. Rejection can occur immediately or after dequeuing/revalidation with changed data. Multiple rejection reasons are permitted; all reasons and the queued alternative are retained in the adjacent source narrative below. Both source actor boxes literally say Instructing Party (Word20/21, images11/12). The narrative identifies the receiving/responding role as Executing/Servicing Party. This reconstruction preserves the literal artwork; narrative message directions are maintained separately, and issue-000049 remains unresolved. No second institution identity is invented from the duplicate label.

[Complete source diagram](../diagrams/curated/fig-0012.md).

### Adjacent source narrative

**P212** Reference Data Link Maintenance Request

**P213** The Instructing Party sends an instruction to the Executing/Servicing Party to modify reference data for a link. 

**P214** Reference Data Link Status Advice

**P215** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:


**P216** Rejected:
The instruction did not pass validation; some reasons could be:

**P217** the mandatory information is not present or incorrect,

**P218** the data cannot be updated,

**P219** the instruction has already been received and is being processed. 

**P220** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.


**P221** Queued:
The Executing/Servicing Party might inform the Instructing party that the processing of the Modify Reference Data Link instruction has been delayed.

**P223** Rejected:
After the re-validation of the instruction, with the new set of data the current instruction did not pass validation, some reasons could be:

**P224** the mandatory information is not present or incorrect,

**P225** the data cannot be updated,

**P226** the instruction has already been received and is being processed. 

**P227** This instruction contains information that identifies the status and the reasons why the instruction is rejected. It is possible to have more than one reason for this status.

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000365-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).

Source direction qualification: narrative P178/P191/P193/P198/P213/P215 gives the receiving/responding role as Executing/Servicing Party; the two source drawings incorrectly duplicate the Instructing Party label. Both claims are retained under issue-000049.
