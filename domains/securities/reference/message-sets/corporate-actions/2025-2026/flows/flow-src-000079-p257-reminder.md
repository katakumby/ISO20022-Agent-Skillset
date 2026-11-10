---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079", "src-000080"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p257-reminder"
title: "Reminder"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Election, Entitlement and Reminder Scenarios", "Reminder"], "locator": "/w:document/w:body/w:p[257]", "paragraph_id": "P257", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Election, Entitlement and Reminder Scenarios", "Reminder"], "locator": "/w:document/w:body/w:p[258]", "paragraph_id": "P258", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Election, Entitlement and Reminder Scenarios", "Reminder"], "locator": "/w:document/w:body/w:p[259]", "paragraph_id": "P259", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Election, Entitlement and Reminder Scenarios", "Reminder"], "locator": "/w:document/w:body/w:p[260]", "paragraph_id": "P260", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Election, Entitlement and Reminder Scenarios", "Reminder"], "locator": "/w:document/w:body/w:p[261]", "paragraph_id": "P261", "table_id": null}, {"source_id": "src-000080", "locator": "file page 274; 5 seev.033.001.14 CorporateActionInstructionV14"}, {"source_id": "src-000080", "locator": "file page 320; 6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16"}, {"source_id": "src-000080", "locator": "file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17"}, {"source_id": "src-000080", "locator": "file page 23; 3 seev.031.001.16 CorporateActionNotificationV16"}]
participants: ["participant-src-000079-account-owner", "participant-src-000079-account-servicer"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Notifications/Announcements and Cancellation"], "locator": "/w:document/w:body/w:tbl[4]/w:tr[2]", "paragraph_id": null, "table_id": "T4"}, {"source_id": "src-000080", "locator": "file page 23; 3 seev.031.001.16 CorporateActionNotificationV16"}, {"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instructions and Cancellations"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000080", "locator": "file page 274; 5 seev.033.001.14 CorporateActionInstructionV14"}]
message_ids: ["seev.033.001.14", "seev.034.001.16", "seev.035.001.17", "seev.031.001.16"]
message_families: ["seev.031", "seev.033"]
search_terms: ["Reminder", "Account Servicer", "Account Owner", "seev.031", "seev.033"]
limitations: ["The source diagram and scenario narrative were checked. Formal precondition/postcondition fields and any omitted market-specific handling are not separately defined by this scenario."]
manual_curated: true
diagram_visual_review: "pass"
---





# Reminder

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, triggering conditions, message direction, exceptions and outcomes are curated below from the named source scenario. Formal precondition/postcondition fields are not separately provided by this scenario.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P258** This scenario illustrates a classical sequence of corporate action messages for the election phase of a corporate action event following the announcement phase when the account servicer reminds the account owner that it may instruct on the proposed options of the concerned corporate action event.

**P259** Once the announcement phase is completed, and the account owner has not yet instructed for any of the option for its eligible balance whilst the instruction deadline set by the account servicer is approaching, the account servicer may send a reminder CorporateActionNotification to the account owner to remind him about the corporate action event details, its eligible balance and proposed options.

**P260** The account owner may then send to the account servicer its instruction within the CorporateActionInstruction so that the election process can continue until completion.

Source diagram evidence: [fig-0027](../documents/src-000079/diagrams/fig-0027.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `seev.031`, `seev.033`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: BusinessTransactions / Election, Entitlement and Reminder Scenarios / Reminder.

## Reviewed source sequence and conditions

When the instruction deadline approaches and the Account Owner has not instructed, the Account Servicer may remind it of event details, eligible balance and options. The owner may then instruct and the election process continues.

[Source sequence reconstruction](../diagrams/business-transactions/fig-0027.md).

| Ordered step | Initiator / sender | Receiver / responsible recipient | Message and source phase |
| --- | --- | --- | --- |
| 1 | Account Servicer | Account Owner | CorporateActionNotification (NEWM) — Preliminary announcement |
| 2 | Account Servicer | Account Owner | CorporateActionNotification (REPL) — Confirmed announcement |
| 3 | Account Servicer | Account Owner | CorporateActionNotification (RMDR) |
| 4 | Account Owner | Account Servicer | CorporateActionInstruction |
| 5 | Account Servicer | Account Owner | CorporateActionInstructionStatusAdvice |
| 6 | Account Servicer | Account Owner | CorporateActionMovementPreliminaryAdvice (NEWM) — Final entitlement |


Conditions and exceptions above come from P258-P260. This scenario does not separately enumerate formal precondition/postcondition fields; do not infer additional guarantees. P203-P204 explains the omitted intermediary chain and interchangeable functional-role capacity.

## Exact supplied message bindings

These bindings use the explicitly named message definitions in src-000080. Part 1 artwork itself uses message names, not exact version numbers.

| Source message name | Exact definition | MDR Part 2 locator |
| --- | --- | --- |
| CorporateActionInstruction | [seev.033.001.14](../../../../messages/seev.033.001.14/index.md) | src-000080 file page 274; 5 seev.033.001.14 CorporateActionInstructionV14 |
| CorporateActionInstructionStatusAdvice | [seev.034.001.16](../../../../messages/seev.034.001.16/index.md) | src-000080 file page 320; 6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 |
| CorporateActionMovementPreliminaryAdvice | [seev.035.001.17](../../../../messages/seev.035.001.17/index.md) | src-000080 file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17 |
| CorporateActionNotification | [seev.031.001.16](../../../../messages/seev.031.001.16/index.md) | src-000080 file page 23; 3 seev.031.001.16 CorporateActionNotificationV16 |

