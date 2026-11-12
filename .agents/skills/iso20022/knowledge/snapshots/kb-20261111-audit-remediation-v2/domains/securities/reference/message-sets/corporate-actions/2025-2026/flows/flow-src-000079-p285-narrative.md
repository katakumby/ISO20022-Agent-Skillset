---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079", "src-000080"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p285-narrative"
title: "Narrative"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Narrative"], "locator": "/w:document/w:body/w:p[285]", "paragraph_id": "P285", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Narrative"], "locator": "/w:document/w:body/w:p[286]", "paragraph_id": "P286", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Narrative"], "locator": "/w:document/w:body/w:p[287]", "paragraph_id": "P287", "table_id": null}, {"source_id": "src-000080", "locator": "file page 692; 10 seev.038.001.09 CorporateActionNarrativeV09"}]
participants: ["participant-src-000079-account-owner", "participant-src-000079-account-servicer"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Notifications/Announcements and Cancellation"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[4]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000080", "locator": "file page 692; 10 seev.038.001.09 CorporateActionNarrativeV09"}]
message_ids: ["seev.038.001.09"]
message_families: ["seev.038"]
search_terms: ["Narrative", "Account Servicer", "Account Owner", "seev.038"]
limitations: ["The source diagram and scenario narrative were checked. Formal precondition/postcondition fields and any omitted market-specific handling are not separately defined by this scenario."]
manual_curated: true
diagram_visual_review: "pass"
---





# Narrative

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, triggering conditions, message direction, exceptions and outcomes are curated below from the named source scenario. Formal precondition/postcondition fields are not separately provided by this scenario.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P286** The account owner or the account servicer may send the CorporateActionNarrative message to provide specific narrative information for taxation conditions, registration details, confirmation of holdings transfer and other ancillary processes.

Source diagram evidence: [fig-0032](../documents/src-000079/diagrams/fig-0032.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `seev.038`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: BusinessTransactions / Narrative.

## Reviewed source sequence and conditions

Either functional participant may provide narrative information for taxation conditions, registration details, confirmation of holdings transfer and ancillary processes. The two directions shown do not establish a request-response dependency or mandatory ordering between otherwise independent narrative messages.

[Source sequence reconstruction](../diagrams/business-transactions/fig-0032.md).

| Ordered step | Initiator / sender | Receiver / responsible recipient | Message and source phase |
| --- | --- | --- | --- |
| 1 | Account Servicer | Account Owner | CorporateActionNarrative |
| 2 | Account Owner | Account Servicer | CorporateActionNarrative |


Conditions and exceptions above come from P286. This scenario does not separately enumerate formal precondition/postcondition fields; do not infer additional guarantees. P203-P204 explains the omitted intermediary chain and interchangeable functional-role capacity.

## Exact supplied message bindings

These bindings use the explicitly named message definitions in src-000080. Part 1 artwork itself uses message names, not exact version numbers.

| Source message name | Exact definition | MDR Part 2 locator |
| --- | --- | --- |
| CorporateActionNarrative | [seev.038.001.09](../../../../messages/seev.038.001.09/index.md) | src-000080 file page 692; 10 seev.038.001.09 CorporateActionNarrativeV09 |

