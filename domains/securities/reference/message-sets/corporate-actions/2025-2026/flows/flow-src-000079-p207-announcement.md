---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079", "src-000080"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p207-announcement"
title: "Announcement"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement"], "locator": "/w:document/w:body/w:p[207]", "paragraph_id": "P207", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement"], "locator": "/w:document/w:body/w:p[208]", "paragraph_id": "P208", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement"], "locator": "/w:document/w:body/w:p[209]", "paragraph_id": "P209", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement"], "locator": "/w:document/w:body/w:p[210]", "paragraph_id": "P210", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement"], "locator": "/w:document/w:body/w:p[211]", "paragraph_id": "P211", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement"], "locator": "/w:document/w:body/w:p[212]", "paragraph_id": "P212", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement"], "locator": "/w:document/w:body/w:p[213]", "paragraph_id": "P213", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement"], "locator": "/w:document/w:body/w:p[214]", "paragraph_id": "P214", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement"], "locator": "/w:document/w:body/w:p[215]", "paragraph_id": "P215", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Announcement ", "Announcement"], "locator": "/w:document/w:body/w:p[216]", "paragraph_id": "P216", "table_id": null}, {"source_id": "src-000080", "locator": "file page 266; 4 seev.032.001.09 CorporateActionEventProcessingStatusAdviceV09"}, {"source_id": "src-000080", "locator": "file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17"}, {"source_id": "src-000080", "locator": "file page 23; 3 seev.031.001.16 CorporateActionNotificationV16"}]
participants: ["participant-src-000079-account-owner", "participant-src-000079-account-servicer"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Notifications/Announcements and Cancellation"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000080", "locator": "file page 23; 3 seev.031.001.16 CorporateActionNotificationV16"}, {"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Entitlements, Movement Preliminary Advice and Cancellation"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[2]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000080", "locator": "file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17"}, {"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Confirmation, Cancellation and Reversal"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[3]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000080", "locator": "file page 266; 4 seev.032.001.09 CorporateActionEventProcessingStatusAdviceV09"}]
message_ids: ["seev.032.001.09", "seev.035.001.17", "seev.031.001.16"]
message_families: ["seev.031", "seev.032", "seev.035"]
search_terms: ["Announcement", "Account Servicer", "Account Owner", "seev.031", "seev.032", "seev.035"]
limitations: ["The source diagram and scenario narrative were checked. Formal precondition/postcondition fields and any omitted market-specific handling are not separately defined by this scenario."]
manual_curated: true
diagram_visual_review: "pass"
---





# Announcement

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, triggering conditions, message direction, exceptions and outcomes are curated below from the named source scenario. Formal precondition/postcondition fields are not separately provided by this scenario.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P208** This scenario illustrates a classical sequence of corporate action messages for the announcement phase of a corporate action event. However, depending on the type of corporate action event and on its processing evolution during its life cycle, not all messages illustrated here will necessarily be sent.

**P209** The account servicer sends a new CorporateActionNotification to the account owner as a preliminary announcement of a corporate action event concerning a security in which the account owner has holdings on its account. As the event details communicated to the account Servicer are updated or modified, the account servicer may send other replacement CorporateActionNotification messages indicating each time the processing status of the event.

Source diagram evidence: [fig-0020](../documents/src-000079/diagrams/fig-0020.md). Mermaid reconstruction and visual review are pending.

**P211** Once the information about the corporate action event is complete and confirmed, the account servicer sends a replacement CorporateActionNotification to the account owner as a confirmed announcement indicating the status is complete and confirmed.

**P212** If appropriate for the corporate action event, the account servicer may send a replacement CorporateActionNotification containing the information on the event stage reached in the corporate action event life cycle.

**P213** For corporate action events having an entitlement date (for example, stock dividend), the account servicer sends on entitlement date an entitlement CorporateActionMovemmentPreliminaryAdvice containing the eligible balance and possibly resulting securities and/or cash movements to the account servicer.

**P214** For corporate action events that have an entitlement date and that do not require an election phase (for example, mandatory events without options), once the entitlement date is reached, the account servicer may send a CorporateActionMovementPreliminaryAdvice containing the final entitlements and movements to the account owner.

**P215** In the case of plain vanilla predictable events such as an interest payment, a preliminary announcement and a confirmed announcement are not always necessary and therefore the related CorporateActionNotification messages may not necessarily be sent by the account servicer. The account servicer might directly send a final entitlement CorporateActionMovementPreliminaryAdvice message to the account owner as a first message concerning this type of corporate action event (see also section 2 about election, entitlement and reminder).

**P216** Should a corporate action event processing not be fully completed by the announced payment date, the account servicer may send a CorporateActionEventProcessingStatusAdvice to the account owner to inform about the processing status and optionally, the reason for this status.

## Messages and alternative paths

Source-supported message family mentions: `seev.031`, `seev.032`, `seev.035`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: BusinessTransactions / Announcement  / Announcement.

## Reviewed source sequence and conditions

The illustrated messages are conditional on the event and its life cycle, not all mandatory. Updated event details may cause replacements; final entitlement may be the first message for predictable events. Processing status advice may be sent when completion is delayed beyond the payment date. Source P213 contains an apparent recipient/message-name inconsistency; the drawing and adjacent P214 show Account Servicer to Account Owner.

[Source sequence reconstruction](../diagrams/business-transactions/fig-0020.md).

| Ordered step | Initiator / sender | Receiver / responsible recipient | Message and source phase |
| --- | --- | --- | --- |
| 1 | Account Servicer | Account Owner | CorporateActionNotification (NEWM) — Preliminary announcement |
| 2 | Account Servicer | Account Owner | CorporateActionNotification (REPL) — Confirmed announcement |
| 3 | Account Servicer | Account Owner | CorporateActionNotification (REPL + Event stage) |
| 4 | Account Servicer | Account Owner | CorporateActionNotification (REPL + Eligible balance) — Entitlement |
| 5 | Account Servicer | Account Owner | CorporateActionMovementPreliminaryAdvice (NEWM) — Final entitlement (eg. Mandatory events) |
| 6 | Account Servicer | Account Owner | CorporateActionEventProcessingStatusAdvice (Status pending) |


Conditions and exceptions above come from P208-P216. This scenario does not separately enumerate formal precondition/postcondition fields; do not infer additional guarantees. P203-P204 explains the omitted intermediary chain and interchangeable functional-role capacity.

## Exact supplied message bindings

These bindings use the explicitly named message definitions in src-000080. Part 1 artwork itself uses message names, not exact version numbers.

| Source message name | Exact definition | MDR Part 2 locator |
| --- | --- | --- |
| CorporateActionEventProcessingStatusAdvice | [seev.032.001.09](../../../../messages/seev.032.001.09/index.md) | src-000080 file page 266; 4 seev.032.001.09 CorporateActionEventProcessingStatusAdviceV09 |
| CorporateActionMovementPreliminaryAdvice | [seev.035.001.17](../../../../messages/seev.035.001.17/index.md) | src-000080 file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17 |
| CorporateActionNotification | [seev.031.001.16](../../../../messages/seev.031.001.16/index.md) | src-000080 file page 23; 3 seev.031.001.16 CorporateActionNotificationV16 |

