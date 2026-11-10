---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079", "src-000080"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p217-announcement-and-cancellation-of-event"
title: "Announcement and Cancellation of Event"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement and Cancellation of Event"], "locator": "/w:document/w:body/w:p[217]", "paragraph_id": "P217", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement and Cancellation of Event"], "locator": "/w:document/w:body/w:p[218]", "paragraph_id": "P218", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement and Cancellation of Event"], "locator": "/w:document/w:body/w:p[219]", "paragraph_id": "P219", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement and Cancellation of Event"], "locator": "/w:document/w:body/w:p[220]", "paragraph_id": "P220", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement and Cancellation of Event"], "locator": "/w:document/w:body/w:p[221]", "paragraph_id": "P221", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement and Cancellation of Event"], "locator": "/w:document/w:body/w:p[222]", "paragraph_id": "P222", "table_id": null}, {"source_id": "src-000080", "locator": "file page 701; 11 seev.039.001.13 CorporateActionCancellationAdviceV13"}, {"source_id": "src-000080", "locator": "file page 23; 3 seev.031.001.16 CorporateActionNotificationV16"}]
participants: ["participant-src-000079-account-owner", "participant-src-000079-account-servicer", "participant-src-000079-issuer"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Notifications/Announcements and Cancellation"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000080", "locator": "file page 23; 3 seev.031.001.16 CorporateActionNotificationV16"}, {"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Notifications/Announcements and Cancellation"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[3]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000080", "locator": "file page 701; 11 seev.039.001.13 CorporateActionCancellationAdviceV13"}, {"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Entitlements, Movement Preliminary Advice and Cancellation"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[2]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000080", "locator": "file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17"}]
message_ids: ["seev.039.001.13", "seev.031.001.16"]
message_families: ["seev.031", "seev.035", "seev.039"]
search_terms: ["Announcement and Cancellation of Event", "Account Servicer", "Account Owner", "Issuer", "seev.031", "seev.035", "seev.039"]
limitations: ["The source diagram and scenario narrative were checked. Formal precondition/postcondition fields and any omitted market-specific handling are not separately defined by this scenario."]
manual_curated: true
diagram_visual_review: "pass"
---





# Announcement and Cancellation of Event

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, triggering conditions, message direction, exceptions and outcomes are curated below from the named source scenario. Formal precondition/postcondition fields are not separately provided by this scenario.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Issuer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-issuer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P218** This scenario illustrates a classical sequence of corporate action messages when a corporate action event is withdrawn by the issuer after having been previously announced through the chain of intermediaries and possibly to the end investor.

**P219** The account servicer sends a CorporateActionNotification to the account owner as an announcement of a corporate action event concerning a security in which the account owner has holdings on its account.

**P220** Once the account servicer has been informed that the corporate action event is withdrawn by the Issuer, the account servicer sends a CorporateActionCancellationAdvice to the account owner with the cancellation reason indicating a withdrawal of the event.

**P221** A corporate action event may be withdrawn by the Issuer at any moment during its life cycle. It is possible that CorporateActionCancellationAdvice is sent after several replacement CorporateActionNotification or CorporateActionMovementPreliminaryAdvice messages have been sent or even after the election phase of an event.

Source diagram evidence: [fig-0021](../documents/src-000079/diagrams/fig-0021.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `seev.031`, `seev.035`, `seev.039`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: BusinessTransactions / Announcement  / Announcement and Cancellation of Event.

## Reviewed source sequence and conditions

Trigger: the issuer withdraws a previously announced event. The Account Servicer sends withdrawal advice to the Account Owner. Withdrawal can occur at any point, after replacements, preliminary advice, or election. Issuer and intermediary chain appear in the narrative but are intentionally abstracted out of the two-role artwork.

[Source sequence reconstruction](../diagrams/business-transactions/fig-0021.md).

| Ordered step | Initiator / sender | Receiver / responsible recipient | Message and source phase |
| --- | --- | --- | --- |
| 1 | Account Servicer | Account Owner | CorporateActionNotification |
| 2 | Account Servicer | Account Owner | CorporateActionCancellationAdvice (WITH) — Event cancellation |


Conditions and exceptions above come from P218-P221. This scenario does not separately enumerate formal precondition/postcondition fields; do not infer additional guarantees. P203-P204 explains the omitted intermediary chain and interchangeable functional-role capacity.

## Exact supplied message bindings

These bindings use the explicitly named message definitions in src-000080. Part 1 artwork itself uses message names, not exact version numbers.

| Source message name | Exact definition | MDR Part 2 locator |
| --- | --- | --- |
| CorporateActionCancellationAdvice | [seev.039.001.13](../../../../messages/seev.039.001.13/index.md) | src-000080 file page 701; 11 seev.039.001.13 CorporateActionCancellationAdviceV13 |
| CorporateActionNotification | [seev.031.001.16](../../../../messages/seev.031.001.16/index.md) | src-000080 file page 23; 3 seev.031.001.16 CorporateActionNotificationV16 |


The [Issuer](../../../../../../../shared/reference/participants/participant-src-000079-issuer.md) triggers the withdrawal or changed event details in the narrative. The two-role source sequence intentionally omits this upstream actor.
