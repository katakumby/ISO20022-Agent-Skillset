---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079", "src-000080"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p229-final-entitlement-replacement-scenario"
title: "Final Entitlement Replacement Scenario"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Final Entitlement Replacement Scenario"], "locator": "/w:document/w:body/w:p[229]", "paragraph_id": "P229", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Final Entitlement Replacement Scenario"], "locator": "/w:document/w:body/w:p[230]", "paragraph_id": "P230", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Final Entitlement Replacement Scenario"], "locator": "/w:document/w:body/w:p[231]", "paragraph_id": "P231", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Final Entitlement Replacement Scenario"], "locator": "/w:document/w:body/w:p[232]", "paragraph_id": "P232", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Final Entitlement Replacement Scenario"], "locator": "/w:document/w:body/w:p[233]", "paragraph_id": "P233", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Final Entitlement Replacement Scenario"], "locator": "/w:document/w:body/w:p[234]", "paragraph_id": "P234", "table_id": null}, {"source_id": "src-000080", "locator": "file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17"}, {"source_id": "src-000080", "locator": "file page 23; 3 seev.031.001.16 CorporateActionNotificationV16"}]
participants: ["participant-src-000079-account-owner", "participant-src-000079-account-servicer", "participant-src-000079-issuer"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Notifications/Announcements and Cancellation"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000080", "locator": "file page 23; 3 seev.031.001.16 CorporateActionNotificationV16"}, {"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Entitlements, Movement Preliminary Advice and Cancellation"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[2]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000080", "locator": "file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17"}]
message_ids: ["seev.035.001.17", "seev.031.001.16"]
message_families: ["seev.031", "seev.035"]
search_terms: ["Final Entitlement Replacement Scenario", "Account Servicer", "Account Owner", "Issuer", "seev.031", "seev.035"]
limitations: ["The source diagram and scenario narrative were checked. Formal precondition/postcondition fields and any omitted market-specific handling are not separately defined by this scenario."]
manual_curated: true
diagram_visual_review: "pass"
---





# Final Entitlement Replacement Scenario

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, triggering conditions, message direction, exceptions and outcomes are curated below from the named source scenario. Formal precondition/postcondition fields are not separately provided by this scenario.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Issuer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-issuer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P230** This scenario illustrates a case where a replacement of a final entitlement takes place. 

**P231** In the case of a mandatory corporate action event, after the sending of one or more preliminary announcement and of a confirmed announcement, the account servicer may send a new CorporateActionMovementPreliminaryAdvice containing the final entitlements and movements to the account owner.

Source diagram evidence: [fig-0023](../documents/src-000079/diagrams/fig-0023.md). Mermaid reconstruction and visual review are pending.

**P233** After this, if one or more information element in the corporate action event details are modified by the issuer and may affect the eligible balance and/or the movements details, the account servicer sends a replacement CorporateActionNotification with the updated information as a second confirmed announcement.

**P234** Following this, the account servicer also sends a replacement CorporateActionMovementPreliminaryAdvice to the account owner to confirm the updated entitlements and movements.

## Messages and alternative paths

Source-supported message family mentions: `seev.031`, `seev.035`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: BusinessTransactions / Announcement  / Final Entitlement Replacement Scenario.

## Reviewed source sequence and conditions

For a mandatory event, issuer changes affecting eligible balances or movement details after a final-entitlement advice trigger an updated confirmed notification and replacement preliminary advice. The Issuer is in the narrative but is not a third actor in the source sequence.

[Source sequence reconstruction](../diagrams/business-transactions/fig-0023.md).

| Ordered step | Initiator / sender | Receiver / responsible recipient | Message and source phase |
| --- | --- | --- | --- |
| 1 | Account Servicer | Account Owner | CorporateActionNotification (NEWM) — Preliminary announcement |
| 2 | Account Servicer | Account Owner | CorporateActionNotification (REPL) — Confirmed announcement |
| 3 | Account Servicer | Account Owner | CorporateActionMovementPreliminaryAdvice (NEWM) — Final entitlement (eg. Mandatory events) |
| 4 | Account Servicer | Account Owner | CorporateActionNotification (REPL) — Confirmed announcement with change |
| 5 | Account Servicer | Account Owner | CorporateActionMovementPreliminaryAdvice (REPL) — Final entitlement (eg. Mandatory events) |


Conditions and exceptions above come from P230-P234. This scenario does not separately enumerate formal precondition/postcondition fields; do not infer additional guarantees. P203-P204 explains the omitted intermediary chain and interchangeable functional-role capacity.

## Exact supplied message bindings

These bindings use the explicitly named message definitions in src-000080. Part 1 artwork itself uses message names, not exact version numbers.

| Source message name | Exact definition | MDR Part 2 locator |
| --- | --- | --- |
| CorporateActionMovementPreliminaryAdvice | [seev.035.001.17](../../../../messages/seev.035.001.17/index.md) | src-000080 file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17 |
| CorporateActionNotification | [seev.031.001.16](../../../../messages/seev.031.001.16/index.md) | src-000080 file page 23; 3 seev.031.001.16 CorporateActionNotificationV16 |


The [Issuer](../../../../../../../shared/reference/participants/participant-src-000079-issuer.md) triggers the withdrawal or changed event details in the narrative. The two-role source sequence intentionally omits this upstream actor.
