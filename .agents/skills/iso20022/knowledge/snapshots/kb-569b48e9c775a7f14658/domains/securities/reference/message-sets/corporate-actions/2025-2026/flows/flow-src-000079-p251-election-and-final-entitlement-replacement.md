---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079", "src-000080"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p251-election-and-final-entitlement-replacement"
title: "Election and Final Entitlement Replacement"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Election, Entitlement and Reminder Scenarios", "Election and Final Entitlement Replacement"], "locator": "/w:document/w:body/w:p[251]", "paragraph_id": "P251", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Election, Entitlement and Reminder Scenarios", "Election and Final Entitlement Replacement"], "locator": "/w:document/w:body/w:p[252]", "paragraph_id": "P252", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Election, Entitlement and Reminder Scenarios", "Election and Final Entitlement Replacement"], "locator": "/w:document/w:body/w:p[253]", "paragraph_id": "P253", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Election, Entitlement and Reminder Scenarios", "Election and Final Entitlement Replacement"], "locator": "/w:document/w:body/w:p[254]", "paragraph_id": "P254", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Election, Entitlement and Reminder Scenarios", "Election and Final Entitlement Replacement"], "locator": "/w:document/w:body/w:p[255]", "paragraph_id": "P255", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Election, Entitlement and Reminder Scenarios", "Election and Final Entitlement Replacement"], "locator": "/w:document/w:body/w:p[256]", "paragraph_id": "P256", "table_id": null}, {"source_id": "src-000080", "locator": "file page 274; 5 seev.033.001.14 CorporateActionInstructionV14"}, {"source_id": "src-000080", "locator": "file page 320; 6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16"}, {"source_id": "src-000080", "locator": "file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17"}, {"source_id": "src-000080", "locator": "file page 23; 3 seev.031.001.16 CorporateActionNotificationV16"}]
participants: ["participant-src-000079-account-owner", "participant-src-000079-account-servicer"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instructions and Cancellations"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000080", "locator": "file page 274; 5 seev.033.001.14 CorporateActionInstructionV14"}, {"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instructions and Cancellations"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Confirmation, Cancellation and Reversal"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[4]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000080", "locator": "file page 320; 6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16"}, {"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Entitlements, Movement Preliminary Advice and Cancellation"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[2]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000080", "locator": "file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17"}]
message_ids: ["seev.033.001.14", "seev.034.001.16", "seev.035.001.17", "seev.031.001.16"]
message_families: ["seev.033", "seev.034", "seev.035"]
search_terms: ["Election and Final Entitlement Replacement", "Account Servicer", "Account Owner", "seev.033", "seev.034", "seev.035"]
limitations: ["The source diagram and scenario narrative were checked. Formal precondition/postcondition fields and any omitted market-specific handling are not separately defined by this scenario."]
manual_curated: true
diagram_visual_review: "pass"
---





# Election and Final Entitlement Replacement

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, triggering conditions, message direction, exceptions and outcomes are curated below from the named source scenario. Formal precondition/postcondition fields are not separately provided by this scenario.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P252** This scenario illustrates a classical sequence of corporate action messages for the election phase of a corporate action event following the announcement phase when the account owner instructs first partially and later on sends a second instruction to instruct the remaining part of the eligible balance.

**P253** Once the announcement phase is completed, the account owner may send a CorporateActionInstruction to the account servicer to instruct on one of the proposed options and for a part or all of its eligible balance.

**P254** Once the instruction has been processed by the account servicer, the account servicer sends a CorporateActionInstructionStatusAdvice to the account owner to report the status of the instruction processing. If the instruction is accepted, the account servicer may then also send a CorporateActionMovementPreliminaryAdvice containing the final entitlements and movements to the account owner.

Source diagram evidence: [fig-0026](../documents/src-000079/diagrams/fig-0026.md). Mermaid reconstruction and visual review are pending.

**P256** If the account owner then sends a second CorporateActionInstruction to the account servicer to instruct the remaining part of its eligible balance, and the instruction is accepted too, the account servicer sends a CorporateActionInstructionStatusAdvice to the account owner with a status "accepted". The account servicer then should also send a replacement CorporateActionMovementPreliminaryAdvice containing the updated final entitlement and movements to the account owner.

## Messages and alternative paths

Source-supported message family mentions: `seev.033`, `seev.034`, `seev.035`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: BusinessTransactions / Election, Entitlement and Reminder Scenarios / Election and Final Entitlement Replacement.

## Reviewed source sequence and conditions

The Account Owner first instructs partially, then instructs the remaining eligible balance. After each accepted instruction the Account Servicer reports status; after the second acceptance it should send a replacement preliminary advice with updated final entitlements and movements.

[Source sequence reconstruction](../diagrams/business-transactions/fig-0026.md).

| Ordered step | Initiator / sender | Receiver / responsible recipient | Message and source phase |
| --- | --- | --- | --- |
| 1 | Account Servicer | Account Owner | CorporateActionNotification (NEWM) — Preliminary announcement |
| 2 | Account Servicer | Account Owner | CorporateActionNotification (REPL) — Confirmed announcement |
| 3 | Account Owner | Account Servicer | CorporateActionInstruction — Partial election |
| 4 | Account Servicer | Account Owner | CorporateActionInstructionStatusAdvice |
| 5 | Account Servicer | Account Owner | CorporateActionMovementPreliminaryAdvice (NEWM) — Final entitlement |
| 6 | Account Owner | Account Servicer | CorporateActionInstruction — Remaining election |
| 7 | Account Servicer | Account Owner | CorporateActionInstructionStatusAdvice |
| 8 | Account Servicer | Account Owner | CorporateActionMovementPreliminaryAdvice (REPL) — Final entitlement |


Conditions and exceptions above come from P252-P256. This scenario does not separately enumerate formal precondition/postcondition fields; do not infer additional guarantees. P203-P204 explains the omitted intermediary chain and interchangeable functional-role capacity.

## Exact supplied message bindings

These bindings use the explicitly named message definitions in src-000080. Part 1 artwork itself uses message names, not exact version numbers.

| Source message name | Exact definition | MDR Part 2 locator |
| --- | --- | --- |
| CorporateActionInstruction | [seev.033.001.14](../../../../messages/seev.033.001.14/index.md) | src-000080 file page 274; 5 seev.033.001.14 CorporateActionInstructionV14 |
| CorporateActionInstructionStatusAdvice | [seev.034.001.16](../../../../messages/seev.034.001.16/index.md) | src-000080 file page 320; 6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 |
| CorporateActionMovementPreliminaryAdvice | [seev.035.001.17](../../../../messages/seev.035.001.17/index.md) | src-000080 file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17 |
| CorporateActionNotification | [seev.031.001.16](../../../../messages/seev.031.001.16/index.md) | src-000080 file page 23; 3 seev.031.001.16 CorporateActionNotificationV16 |

