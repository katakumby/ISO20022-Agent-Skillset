---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000353"]
source_editions: ["may-2025"]
message_sets: ["t2s-collateral-management-reference-data"]
flow_id: "flow-src-000353-p160-rejection-scenario"
title: "Rejection Scenario"
source_locations: [{"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data deletion", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[160]", "paragraph_id": "P160", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data deletion", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[161]", "paragraph_id": "P161", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data deletion", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[162]", "paragraph_id": "P162", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data deletion", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[163]", "paragraph_id": "P163", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data deletion", "Rejection Scenario"], "locator": "/w:document/w:body/w:p[164]", "paragraph_id": "P164", "table_id": null}]
participants: ["participant-src-000353-executing-servicing-party", "participant-src-000353-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000353", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Collateral Management Reference Data "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000353", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Collateral Management Reference Data "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[7]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.028.001.01", "reda.075.001.01", "reda.077.001.01"]
message_families: ["reda.075", "reda.077", "reda.028"]
search_terms: ["Rejection Scenario", "Executing / Servicing Party", "Instructing Party", "reda.028", "reda.044", "reda.075", "reda.077"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
issue_ids: ["issue-000043"]
disputed_message_ids: ["reda.044.001.01"]
---





# Rejection Scenario

Source context: T2S CollateralManagementReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000353-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000353-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P161** Applies when the instruction sent by the Instructing Party is rejected by the Executing/Servicing Party.

**P163** Deletion ProcessCollateral Data Status Advice/Eligible Counterpart CSD Status Advice (reda.028/reda.044): REJECTEDAuto-Collateralisation Eligibility Link/Close Link Delete Request (reda.075, reda.077)Deletion ProcessCollateral Data Status Advice/Eligible Counterpart CSD Status Advice (reda.028/reda.044): REJECTEDAuto-Collateralisation Eligibility Link/Close Link Delete Request (reda.075, reda.077)

Source diagram evidence: [fig-0012](../documents/src-000353/diagrams/fig-0012.md). A canonical source reconstruction and actual review evidence are linked below.

## Messages and alternative paths

Source-supported message family mentions: `reda.028`, `reda.044`, `reda.075`, `reda.077`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000353](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralManagementReferenceData_v2.docx`. Heading path: BusinessTransactions / Collateral Reference Data deletion / Rejection Scenario.

## Curated source flow

The Instructing Party sends a deletion instruction for an existing auto-collateralisation eligibility link or close link. The Executing/Servicing Party returns REJECTED and identifies the reference data rejected. Request items are alternatives within the combined source label, not a requirement to send all request messages. The source response label includes reda.044, but P80 associates deletion075/077 with reda.028 while P82 associates reda.044 with creation026. The original label is retained under issue-000043; reda.044 is recorded as a disputed source assertion rather than a confirmed deletion-response mapping.

[Complete source diagram](../diagrams/curated/fig-0012.md).

### Adjacent source narrative

**P166** The Instructing Party sends the instruction to the Executing/Servicing Party to delete an already created:

**P167** - Auto-Collateralisation Eligibility Link

**P168** - Close Link

**P169** when there is a gap in the Auto-Collateralisation Eligibility Links or in the Close Links coverage at the Executing/Servicing Party. This instruction contains information that clearly identify the or the Auto-Collateralisation Eligibility Link or the Close Link.

**P170** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the Rejected status: the Executing/Servicing Party informs the Instructing party that the Collateral Reference Data deletion instruction has been rejected. The Executing/Servicing Party present to the Instructing Party the identification of the Collateral Reference Data that has been rejected.

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000353-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000353-executing-servicing-party.md).
