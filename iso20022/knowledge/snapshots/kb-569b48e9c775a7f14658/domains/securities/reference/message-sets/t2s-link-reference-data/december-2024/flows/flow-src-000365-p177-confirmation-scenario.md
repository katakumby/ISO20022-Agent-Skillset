---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000365"]
source_editions: ["december-2024"]
message_sets: ["t2s-link-reference-data"]
flow_id: "flow-src-000365-p177-confirmation-scenario"
title: "Confirmation Scenario"
source_locations: [{"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[177]", "paragraph_id": "P177", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[178]", "paragraph_id": "P178", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[179]", "paragraph_id": "P179", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[180]", "paragraph_id": "P180", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[181]", "paragraph_id": "P181", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[182]", "paragraph_id": "P182", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[183]", "paragraph_id": "P183", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[184]", "paragraph_id": "P184", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[185]", "paragraph_id": "P185", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[186]", "paragraph_id": "P186", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[187]", "paragraph_id": "P187", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[188]", "paragraph_id": "P188", "table_id": null}, {"source_id": "src-000365", "heading_path": ["BusinessTransactions", "Modification Process", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[189]", "paragraph_id": "P189", "table_id": null}]
participants: ["participant-src-000365-csd", "participant-src-000365-executing-servicing-party", "participant-src-000365-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000365", "heading_path": ["Scope and Functionality", "Scope", "Groups", "Link Creation and Maintenance"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000365", "heading_path": ["Scope and Functionality", "Scope", "Groups", "Link Creation and Maintenance"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[7]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.046.001.01", "reda.047.001.01", "reda.050.001.01", "reda.051.001.01"]
message_families: ["reda.046", "reda.050", "reda.047", "reda.051"]
search_terms: ["Confirmation Scenario", "Executing / Servicing Party", "Instructing Party", "CSD", "reda.046", "reda.047", "reda.050", "reda.051"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
issue_ids: ["issue-000049"]
---





# Confirmation Scenario

Source context: T2S LinkReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| CSD | [Participant](../../../../../../../shared/reference/participants/participant-src-000365-csd.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P178** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing party

**P179** Security CSD Link/Account Link Maintenance Request (reda.046/reda.050)Modification processSecurity CSD Link/Account Link Status Advice (reda.047/reda.051): QUEUEDSecurity CSD Link/Account Link Status Advice (reda.047/reda.051): COMPLETEDSecurity CSD Link/Account Link Maintenance Request (reda.046/reda.050)Modification processSecurity CSD Link/Account Link Status Advice (reda.047/reda.051): QUEUEDSecurity CSD Link/Account Link Status Advice (reda.047/reda.051): COMPLETED

Source diagram evidence: [fig-0011](../documents/src-000365/diagrams/fig-0011.md). A canonical source reconstruction and actual review evidence are linked below.

## Messages and alternative paths

Source-supported message family mentions: `reda.046`, `reda.047`, `reda.050`, `reda.051`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000365](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`. Heading path: BusinessTransactions / Modification Process / Confirmation Scenario.

## Curated source flow

The source shows the request left-to-right, an optional QUEUED advice right-to-left with a dashed line, and the final solid COMPLETED advice. The adjacent narrative says delayed processing might be reported, so QUEUED is not mandatory in every execution. Successful processing returns identification of the link. Both source actor boxes literally say Instructing Party (Word20/21, images11/12). The narrative identifies the receiving/responding role as Executing/Servicing Party. This reconstruction preserves the literal artwork; narrative message directions are maintained separately, and issue-000049 remains unresolved. No second institution identity is invented from the duplicate label.

[Complete source diagram](../diagrams/curated/fig-0011.md).

### Adjacent source narrative

**P190** Reference Data Link Maintenance Request

**P191** The Instructing Party sends an instruction to the Executing/Servicing Party to modify data for a Reference Data Link. This instruction contains information that uniquely identify the Reference Data Link. 

**P192** Reference Data Link Status Advice

**P193** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the following statuses:


**P194** Queued:
The Executing/Servicing Party might inform the Instructing party that the processing of the Modify Reference Data Link instruction has been delayed.


**P195** Completed:
The Executing/Servicing Party informs the Instructing party that the Modify Reference Data Link instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the Reference Data Link that has been processed.

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000365-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000365-executing-servicing-party.md).

Source direction qualification: narrative P178/P191/P193/P198/P213/P215 gives the receiving/responding role as Executing/Servicing Party; the two source drawings incorrectly duplicate the Instructing Party label. Both claims are retained under issue-000049.
