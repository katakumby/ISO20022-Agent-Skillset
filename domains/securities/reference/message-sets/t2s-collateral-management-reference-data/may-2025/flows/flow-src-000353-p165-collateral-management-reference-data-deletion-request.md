---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000353"]
source_editions: ["may-2025"]
message_sets: ["t2s-collateral-management-reference-data"]
flow_id: "flow-src-000353-p165-collateral-management-reference-data-deletion-request"
title: "Collateral Management Reference Data Deletion Request"
source_locations: [{"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data deletion", "Rejection Scenario", "Collateral Management Reference Data Deletion Request"], "locator": "/w:document/w:body/w:p[165]", "paragraph_id": "P165", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data deletion", "Rejection Scenario", "Collateral Management Reference Data Deletion Request"], "locator": "/w:document/w:body/w:p[166]", "paragraph_id": "P166", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data deletion", "Rejection Scenario", "Collateral Management Reference Data Deletion Request"], "locator": "/w:document/w:body/w:p[167]", "paragraph_id": "P167", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data deletion", "Rejection Scenario", "Collateral Management Reference Data Deletion Request"], "locator": "/w:document/w:body/w:p[168]", "paragraph_id": "P168", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data deletion", "Rejection Scenario", "Collateral Management Reference Data Deletion Request"], "locator": "/w:document/w:body/w:p[169]", "paragraph_id": "P169", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data deletion", "Rejection Scenario", "Collateral Management Reference Data Deletion Request"], "locator": "/w:document/w:body/w:p[170]", "paragraph_id": "P170", "table_id": null}]
participants: ["participant-src-000353-executing-servicing-party", "participant-src-000353-instructing-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Collateral Management Reference Data Deletion Request", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Collateral Management Reference Data Deletion Request

Source context: T2S CollateralManagementReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000353-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000353-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P166** The Instructing Party sends the instruction to the Executing/Servicing Party to delete an already created:

**P167** - Auto-Collateralisation Eligibility Link

**P168** - Close Link

**P169** when there is a gap in the Auto-Collateralisation Eligibility Links or in the Close Links coverage at the Executing/Servicing Party. This instruction contains information that clearly identify the or the Auto-Collateralisation Eligibility Link or the Close Link.

**P170** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the Rejected status: the Executing/Servicing Party informs the Instructing party that the Collateral Reference Data deletion instruction has been rejected. The Executing/Servicing Party present to the Instructing Party the identification of the Collateral Reference Data that has been rejected.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000353](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralManagementReferenceData_v2.docx`. Heading path: BusinessTransactions / Collateral Reference Data deletion / Rejection Scenario / Collateral Management Reference Data Deletion Request.
