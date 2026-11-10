---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000353"]
source_editions: ["may-2025"]
message_sets: ["t2s-collateral-management-reference-data"]
flow_id: "flow-src-000353-p104-collateral-reference-data-creation"
title: "Collateral Reference Data creation"
source_locations: [{"source_id": "src-000353", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:p[104]", "paragraph_id": "P104", "table_id": null}, {"source_id": "src-000353", "heading_path": ["BusinessProcess Description"], "locator": "/w:document/w:body/w:tbl[8]", "paragraph_id": null, "table_id": "T8"}]
participants: ["participant-src-000353-central-bank", "participant-src-000353-executing-servicing-party", "participant-src-000353-instructing-party", "participant-src-000353-party-authorised-by-central-bank-or-payment-bank", "participant-src-000353-party-authorised-by-csd"]
message_mapping_evidence: []
message_ids: ["reda.024.001.01", "reda.025.001.01", "reda.026.001.01", "reda.027.001.01", "reda.028.001.01", "reda.044.001.01"]
message_families: ["reda.024", "reda.025", "reda.026", "reda.027", "reda.028", "reda.044"]
search_terms: ["Collateral Reference Data creation", "Executing / Servicing Party", "Instructing Party"]
limitations: ["Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Diagram review and table-cell review have separate evidence."]
manual_curated: true
---











# Collateral Reference Data creation

Source context: T2S CollateralManagementReferenceData. This reference preserves the source-defined segment and its evidence.

## Purpose, trigger and conditions

### Definition

When an Instructing Party would like to create:
• a specific Securities Valuation
• a specific Auto-Collateralisation Eligibility Link
• a specific Close Link
• a specific Eligible Counterpart CSD
that is not yet supported by the Executing/Servicing Party, an Instructing Party asks the Executing/Servicing Party to create: 
• the Securities Valuation
• the Auto-Collateralisation Eligibility Link
• the Close Link
• the Eligible Counterpart CSD
in its system.

Evidence: [T8](../documents/src-000353/tables/tbl-0008.md), source row 2.

### Trigger

The process is triggered when the Instructing Party sends:
• a Create Securities Valuation message;
• a Create Auto-Collateralisation Eligibility Link message;
• a Create Close Link message;
• a Create Eligible Counterpart CSD message.

Evidence: [T8](../documents/src-000353/tables/tbl-0008.md), source row 3.

### Pre-conditions

The Instructing Party is known by the Executing/Servicing Party system. 
The Instructing Party identified a gap in: 
• the Securities Valuations
• the Auto-Collateralisation Eligibility Links
• the Close Links
• the Eligible Counterpart CSDs
coverage of the Executing/Servicing Party. 
The Instructing Party needs this: 
• Securities Valuation 
• Auto-Collateralisation Eligibility Link
• Close Link
• Eligible Counterpart CSD
to be set-up at the Executing /Servicing Party to perform its activities.

Evidence: [T8](../documents/src-000353/tables/tbl-0008.md), source row 4.

### Post-conditions

The acknowledgement of the processing of the creation request.

Evidence: [T8](../documents/src-000353/tables/tbl-0008.md), source row 5.

### Role

Instructing Party

Evidence: [T8](../documents/src-000353/tables/tbl-0008.md), source row 6.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Executing / Servicing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000353-executing-servicing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Instructing Party | [Participant](../../../../../../../shared/reference/participants/participant-src-000353-instructing-party.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

Source table [T8](../documents/src-000353/tables/tbl-0008.md).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000353](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralManagementReferenceData_v2.docx`. Heading path: BusinessProcess Description.

## Curated source flow

The source start branches into six maintenance activities: four creations (securities valuation, auto-collateralisation eligibility link, close link and eligible counterpart CSD) and two deletions (close link and auto-collateralisation eligibility link). All lead to the same end. No exclusive-choice or parallel bar is drawn. T8/T9 require the instructing party to be known and to identify the required coverage change; acknowledgement of processing is the stated postcondition. Their creation/deletion conditions remain separate.

[Complete source diagram](../diagrams/curated/fig-0002.md).

Scoped participants: [instructing party](../../../../../../../shared/reference/participants/participant-src-000353-instructing-party.md), [executing servicing party](../../../../../../../shared/reference/participants/participant-src-000353-executing-servicing-party.md).

Exact confirmed bindings for this process: [reda.024.001.01](../../../../messages/reda.024.001.01/index.md), [reda.025.001.01](../../../../messages/reda.025.001.01/index.md), [reda.026.001.01](../../../../messages/reda.026.001.01/index.md), [reda.027.001.01](../../../../messages/reda.027.001.01/index.md), [reda.028.001.01](../../../../messages/reda.028.001.01/index.md), [reda.044.001.01](../../../../messages/reda.044.001.01/index.md). Source response family044 in deletion sequences remains disputed under issue-000043.

Narrative authorised sender: [Central Bank](../../../../../../../shared/reference/participants/participant-src-000353-central-bank.md); P74/P75/P77-P79. Only the message applicability listed in that participant record is established.

Narrative authorised sender: [Party authorised by a central bank or payment bank](../../../../../../../shared/reference/participants/participant-src-000353-party-authorised-by-central-bank-or-payment-bank.md); P75/P78. Only the message applicability listed in that participant record is established.

Narrative authorised sender: [Party authorised by a CSD](../../../../../../../shared/reference/participants/participant-src-000353-party-authorised-by-csd.md); P76. Only the message applicability listed in that participant record is established.
