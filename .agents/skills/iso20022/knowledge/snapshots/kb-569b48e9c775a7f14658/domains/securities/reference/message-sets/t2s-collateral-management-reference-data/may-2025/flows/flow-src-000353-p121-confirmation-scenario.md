---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000353"]
source_editions: ["may-2025"]
message_sets: ["t2s-collateral-management-reference-data"]
flow_id: "flow-src-000353-p121-confirmation-scenario"
title: "Confirmation Scenario"
source_locations: [{"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data creation", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[121]", "paragraph_id": "P121", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data creation", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[122]", "paragraph_id": "P122", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data creation", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[123]", "paragraph_id": "P123", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data creation", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[124]", "paragraph_id": "P124", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessTransactions", "Collateral Reference Data creation", "Confirmation Scenario"], "locator": "/w:document/w:body/w:p[125]", "paragraph_id": "P125", "table_id": null}]
participants: ["participant-src-000353-executing-servicing-party", "participant-src-000353-instructing-party"]
message_mapping_evidence: [{"source_id": "src-000353", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Collateral Management Reference Data "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[6]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000353", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Collateral Management Reference Data "], "locator": "/w:document/w:body/w:tbl[4]/w:tr[7]", "paragraph_id": null, "table_id": "T4"}]
message_ids: ["reda.024.001.01", "reda.025.001.01", "reda.026.001.01", "reda.027.001.01", "reda.028.001.01", "reda.044.001.01"]
message_families: ["reda.024", "reda.025", "reda.026", "reda.027", "reda.028", "reda.044"]
search_terms: ["Confirmation Scenario", "Executing / Servicing Party", "Instructing Party", "reda.024", "reda.025", "reda.026", "reda.027", "reda.028", "reda.044"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
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

**P122** Applies when the instruction sent by the Instructing Party is processed and confirmed by the Executing/Servicing Party.

**P124** Creation ProcessCollateral Data Status Advice/Eligible Counterpart CSD Status Advice (reda.028/reda.044): COMPLETEDSecurity Valuation/Auto-Collateralisation Eligibility Link/Close Link/Eligible Counterpart CSD Create Request (reda.024, reda.025, reda.027, reda.026)Creation ProcessCollateral Data Status Advice/Eligible Counterpart CSD Status Advice (reda.028/reda.044): COMPLETEDSecurity Valuation/Auto-Collateralisation Eligibility Link/Close Link/Eligible Counterpart CSD Create Request (reda.024, reda.025, reda.027, reda.026)

Source diagram evidence: [fig-0009](../documents/src-000353/diagrams/fig-0009.md). A canonical source reconstruction and actual review evidence are linked below.

## Messages and alternative paths

Source-supported message family mentions: `reda.024`, `reda.025`, `reda.026`, `reda.027`, `reda.028`, `reda.044`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000353](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralManagementReferenceData_v2.docx`. Heading path: BusinessTransactions / Collateral Reference Data creation / Confirmation Scenario.

## Curated source flow

The Instructing Party sends a creation instruction for a security valuation, auto-collateralisation eligibility link, close link or eligible counterpart CSD. The Executing/Servicing Party returns COMPLETED and identifies the reference data processed. Request items are alternatives within the combined source label, not a requirement to send all request messages. P80 explicitly associates requests024/025/027 with status028; P82 associates request026 with status044. The combined artwork label does not mean every creation request receives both status messages.

[Complete source diagram](../diagrams/curated/fig-0009.md).

### Adjacent source narrative

**P127** The Instructing Party sends the instruction to the Executing/Servicing Party to create a new:

**P128** - Security Valuation

**P129** - Auto-Collateralisation Eligibility Link

**P130** - Close Link

**P131** - Eligible Counterpart CSD

**P132** when there is a gap in the Security Valuations or in the Auto-Collateralisation Eligibility Links or in the Close Links or in the Eligible Counterpart CSDs coverage at the Executing/Servicing Party. This instruction contains information that clearly identify the Security Valuation or the Auto-Collateralisation Eligibility Link or the Close Link or the Eligible Counterpart CSD.

**P133** The Executing/Servicing Party informs the Instructing Party about the lifecycle of its instruction with the Completed status: the Executing/Servicing Party informs the Instructing party that the Collateral Reference Data creation instruction has been successfully processed. The Executing/Servicing Party present to the Instructing Party the identification of the Collateral Reference Data that has been processed.

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000353-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000353-executing-servicing-party.md).
