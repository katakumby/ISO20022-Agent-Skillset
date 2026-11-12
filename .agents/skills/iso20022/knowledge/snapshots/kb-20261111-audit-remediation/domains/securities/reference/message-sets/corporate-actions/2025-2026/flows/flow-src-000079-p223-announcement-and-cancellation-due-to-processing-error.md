---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079", "src-000080"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p223-announcement-and-cancellation-due-to-processing-error"
title: "Announcement and Cancellation due to Processing Error"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement and Cancellation due to Processing Error"], "locator": "/w:document/w:body/w:p[223]", "paragraph_id": "P223", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement and Cancellation due to Processing Error"], "locator": "/w:document/w:body/w:p[224]", "paragraph_id": "P224", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement and Cancellation due to Processing Error"], "locator": "/w:document/w:body/w:p[225]", "paragraph_id": "P225", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement and Cancellation due to Processing Error"], "locator": "/w:document/w:body/w:p[226]", "paragraph_id": "P226", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement and Cancellation due to Processing Error"], "locator": "/w:document/w:body/w:p[227]", "paragraph_id": "P227", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement and Cancellation due to Processing Error"], "locator": "/w:document/w:body/w:p[228]", "paragraph_id": "P228", "table_id": null}, {"source_id": "src-000080", "locator": "file page 701; 11 seev.039.001.13 CorporateActionCancellationAdviceV13"}, {"source_id": "src-000080", "locator": "file page 23; 3 seev.031.001.16 CorporateActionNotificationV16"}]
participants: ["participant-src-000079-account-owner", "participant-src-000079-account-servicer"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Notifications/Announcements and Cancellation"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000080", "locator": "file page 23; 3 seev.031.001.16 CorporateActionNotificationV16"}, {"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Notifications/Announcements and Cancellation"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000080", "locator": "file page 701; 11 seev.039.001.13 CorporateActionCancellationAdviceV13"}, {"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Entitlements, Movement Preliminary Advice and Cancellation"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[2]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000080", "locator": "file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17"}]
message_ids: ["seev.039.001.13", "seev.031.001.16"]
message_families: ["seev.031", "seev.035", "seev.039"]
search_terms: ["Announcement and Cancellation due to Processing Error", "Account Servicer", "Account Owner", "seev.031", "seev.035", "seev.039"]
limitations: ["The source diagram and scenario narrative were checked. Formal precondition/postcondition fields and any omitted market-specific handling are not separately defined by this scenario."]
manual_curated: true
diagram_visual_review: "pass"
---





# Announcement and Cancellation due to Processing Error

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, triggering conditions, message direction, exceptions and outcomes are curated below from the named source scenario. Formal precondition/postcondition fields are not separately provided by this scenario.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P224** This scenario illustrates a classical sequence of corporate action messages when a corporate action event is cancelled by the account servicer after having been previously but erroneously announced to the account owner. This might happen when the account servicer sends announcement messages to the account owner whilst for instance it has no holdings in the security concerned by the corporate action event announced. 

**P225** The account servicer sends a new CorporateActionNotification to the account owner as a preliminary announcement of a corporate action event concerning a security in which the account owner has for instance no holdings on its account.

**P226** Once the account servicer notices that the account owner should not have been informed about this corporate action event, the account servicer sends a CorporateActionCancellationAdvice to the account owner with the cancellation reason indicating a processing error.

**P227** Note also that it is likely that a CorporateActionCancellationAdvice is sent only after several replacement CorporateActionNotification or a CorporateActionMovementPreliminaryAdvice have been sent, should the account servicer not notice its mistake immediately.

Source diagram evidence: [fig-0022](../documents/src-000079/diagrams/fig-0022.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `seev.031`, `seev.035`, `seev.039`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: BusinessTransactions / Announcement  / Announcement and Cancellation due to Processing Error.

## Reviewed source sequence and conditions

Trigger: the Account Servicer discovers that a previous announcement to the Account Owner was erroneous, for example because the owner has no holdings in the security. The cancellation reason is processing error. Detection can follow multiple replacement notifications or preliminary advice; the two-arrow illustration is a minimal path.

[Source sequence reconstruction](../diagrams/business-transactions/fig-0022.md).

| Ordered step | Initiator / sender | Receiver / responsible recipient | Message and source phase |
| --- | --- | --- | --- |
| 1 | Account Servicer | Account Owner | CorporateActionNotification (NEWM) — Preliminary announcement |
| 2 | Account Servicer | Account Owner | CorporateActionCancellationAdvice (PROC) — Cancellation due to processing error |


Conditions and exceptions above come from P224-P227. This scenario does not separately enumerate formal precondition/postcondition fields; do not infer additional guarantees. P203-P204 explains the omitted intermediary chain and interchangeable functional-role capacity.

## Exact supplied message bindings

These bindings use the explicitly named message definitions in src-000080. Part 1 artwork itself uses message names, not exact version numbers.

| Source message name | Exact definition | MDR Part 2 locator |
| --- | --- | --- |
| CorporateActionCancellationAdvice | [seev.039.001.13](../../../../messages/seev.039.001.13/index.md) | src-000080 file page 701; 11 seev.039.001.13 CorporateActionCancellationAdviceV13 |
| CorporateActionNotification | [seev.031.001.16](../../../../messages/seev.031.001.16/index.md) | src-000080 file page 23; 3 seev.031.001.16 CorporateActionNotificationV16 |

