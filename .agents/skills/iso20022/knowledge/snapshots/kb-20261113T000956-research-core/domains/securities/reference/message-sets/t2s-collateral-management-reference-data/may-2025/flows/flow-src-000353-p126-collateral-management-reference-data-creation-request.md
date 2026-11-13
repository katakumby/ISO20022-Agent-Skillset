---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000353"]
source_editions: ["may-2025"]
message_sets: ["t2s-collateral-management-reference-data"]
flow_id: "flow-src-000353-p126-collateral-management-reference-data-creation-request"
title: "Collateral Management Reference Data Creation Request"
source_locations: [{"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data creation", "Confirmation Scenario", "Collateral Management Reference Data Creation Request"], "locator": "/w:document/w:body/w:p[126]", "paragraph_id": "P126", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data creation", "Confirmation Scenario", "Collateral Management Reference Data Creation Request"], "locator": "/w:document/w:body/w:p[127]", "paragraph_id": "P127", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data creation", "Confirmation Scenario", "Collateral Management Reference Data Creation Request"], "locator": "/w:document/w:body/w:p[128]", "paragraph_id": "P128", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data creation", "Confirmation Scenario", "Collateral Management Reference Data Creation Request"], "locator": "/w:document/w:body/w:p[129]", "paragraph_id": "P129", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data creation", "Confirmation Scenario", "Collateral Management Reference Data Creation Request"], "locator": "/w:document/w:body/w:p[130]", "paragraph_id": "P130", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data creation", "Confirmation Scenario", "Collateral Management Reference Data Creation Request"], "locator": "/w:document/w:body/w:p[131]", "paragraph_id": "P131", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data creation", "Confirmation Scenario", "Collateral Management Reference Data Creation Request"], "locator": "/w:document/w:body/w:p[132]", "paragraph_id": "P132", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data creation", "Confirmation Scenario", "Collateral Management Reference Data Creation Request"], "locator": "/w:document/w:body/w:p[133]", "paragraph_id": "P133", "table_id": null}]
participants: ["participant-src-000353-executing-servicing-party", "participant-src-000353-instructing-party"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Collateral Management Reference Data Creation Request", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Collateral Management Reference Data Creation Request

Source context: T2S CollateralManagementReferenceData. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000353-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000353-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P127** The Instructing Party sends the instruction to the Executing/Servicing Party to create a new:

**P128** - Security Valuation

**P129** - Auto-Collateralisation Eligibility Link

**P130** - Close Link

**P131** - Eligible Counterpart CSD

**P132** when there is a gap in the Security Valuations or in the Auto-Collateralisation Eligibility Links or in the Close Links or in the Eligible Counterpart CSDs coverage at the Executing/Servicing Party. This instruction contains information that clearly identify the Security Valuation or the Auto-Collateralisation Eligibility Link or the Close Link or the Eligible Counterpart CSD.

**P133** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the Completed status: the Executing/Servicing Party informs the Instructing party that the Collateral Reference Data creation instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the Collateral Reference Data that has been processed.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000353](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralManagementReferenceData_v2.docx`. Heading path: BusinessTransactions / Collateral Reference Data creation / Confirmation Scenario / Collateral Management Reference Data Creation Request.
