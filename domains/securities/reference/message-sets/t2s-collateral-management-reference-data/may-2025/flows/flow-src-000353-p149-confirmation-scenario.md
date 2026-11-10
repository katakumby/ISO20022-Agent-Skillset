---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000353"]
source_editions: ["may-2025"]
message_sets: ["t2s-collateral-management-reference-data"]
flow_id: "flow-src-000353-p149-confirmation-scenario"
title: "Confirmation Scenario"
source_locations: [{"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data deletion", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[149]", "paragraph_id": "P149", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data deletion", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[150]", "paragraph_id": "P150", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data deletion", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[151]", "paragraph_id": "P151", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data deletion", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[152]", "paragraph_id": "P152", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data deletion", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[153]", "paragraph_id": "P153", "table_id": null}]
participants: ["participant-src-000353-executing-servicing-party", "participant-src-000353-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000353", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Collateral Management Reference Data "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000353", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Collateral Management Reference Data "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[7]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.028.001.01", "reda.075.001.01", "reda.077.001.01"]
message_families: ["reda.075", "reda.077", "reda.028"]
search_terms: ["Confirmation Scenario", "Executing / Servicing Party", "Instructing Party", "reda.028", "reda.044", "reda.075", "reda.077"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
issue_ids: ["issue-000043"]
disputed_message_ids: ["reda.044.001.01"]
---





# Confirmation Scenario

Source context: T2S CollateralManagementReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000353-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000353-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P150** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing Party.

**P152** Deletion ProcessCollateral Data Status Advice/Eligible Counterpart CSD Status Advice (reda.028/reda.044): COMPLETEDAuto-Collateralisation Eligibility Link/Close Link Delete Request (reda.075, reda.077)Deletion ProcessCollateral Data Status Advice/Eligible Counterpart CSD Status Advice (reda.028/reda.044): COMPLETEDAuto-Collateralisation Eligibility Link/Close Link Delete Request (reda.075, reda.077)

Source diagram evidence: [fig-0011](../documents/src-000353/diagrams/fig-0011.md). A canonical source reconstruction and actual review evidence are linked below.

## Messages and alternative paths

Source-supported message family mentions: `reda.028`, `reda.044`, `reda.075`, `reda.077`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000353](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralManagementReferenceData_v2.docx`. Heading path: BusinessTransactions / Collateral Reference Data deletion / Confirmation Scenario.

## Curated source flow

The Instructing Party sends a deletion instruction for an existing auto-collateralisation eligibility link or close link. The Executing/Servicing Party returns COMPLETED and identifies the reference data processed. Request items are alternatives within the combined source label, not a requirement to send all request messages. The source response label includes reda.044, but P80 associates deletion075/077 with reda.028 while P82 associates reda.044 with creation026. The original label is retained under issue-000043; reda.044 is recorded as a disputed source assertion rather than a confirmed deletion-response mapping.

[Complete source diagram](../diagrams/curated/fig-0011.md).

### Adjacent source narrative

**P155** The Instructing Party sends the instruction to the Executing/Servicing Party to delete an already created:

**P156** - Auto-Collateralisation Eligibility Link

**P157** - Close Link

**P158** when there is a gap in the Auto-Collateralisation Eligibility Links or in the Close Links coverage at the Executing/Servicing Party. This instruction contains information that clearly identify the or the Auto-Collateralisation Eligibility Link or the Close Link.

**P159** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the Completed status: the Executing/Servicing Party informs the Instructing party that the Collateral Reference Data deletion instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the Collateral Reference Data that has been processed.

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000353-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000353-executing-servicing-party.md).
