---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079", "src-000080"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p265-confirmation"
title: "Confirmation"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Confirmation and Reversal", "Confirmation"], "locator": "/w:document/w:body/w:p[265]", "paragraph_id": "P265", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Confirmation and Reversal", "Confirmation"], "locator": "/w:document/w:body/w:p[266]", "paragraph_id": "P266", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Confirmation and Reversal", "Confirmation"], "locator": "/w:document/w:body/w:p[267]", "paragraph_id": "P267", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Confirmation and Reversal", "Confirmation"], "locator": "/w:document/w:body/w:p[268]", "paragraph_id": "P268", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Confirmation and Reversal", "Confirmation"], "locator": "/w:document/w:body/w:p[269]", "paragraph_id": "P269", "table_id": null}, {"source_id": "src-000080", "locator": "file page 274; 5 seev.033.001.14 CorporateActionInstructionV14"}, {"source_id": "src-000080", "locator": "file page 320; 6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16"}, {"source_id": "src-000080", "locator": "file page 540; 8 seev.036.001.17 CorporateActionMovementConfirmationV17"}, {"source_id": "src-000080", "locator": "file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17"}, {"source_id": "src-000080", "locator": "file page 23; 3 seev.031.001.16 CorporateActionNotificationV16"}]
participants: ["participant-src-000079-account-owner", "participant-src-000079-account-servicer"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Entitlements, Movement Preliminary Advice and Cancellation"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[2]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000080", "locator": "file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17"}]
message_ids: ["seev.033.001.14", "seev.034.001.16", "seev.036.001.17", "seev.035.001.17", "seev.031.001.16"]
message_families: ["seev.035"]
search_terms: ["Confirmation", "Account Servicer", "Account Owner", "seev.035"]
limitations: ["The source diagram and scenario narrative were checked. Formal precondition/postcondition fields and any omitted market-specific handling are not separately defined by this scenario."]
manual_curated: true
diagram_visual_review: "pass"
---





# Confirmation

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, triggering conditions, message direction, exceptions and outcomes are curated below from the named source scenario. Formal precondition/postcondition fields are not separately provided by this scenario.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P266** This scenario illustrates a classical sequence of corporate action messages for the confirmation phase of a corporate action event following the announcement and election phases.

Source diagram evidence: [fig-0028](../documents/src-000079/diagrams/fig-0028.md). Mermaid reconstruction and visual review are pending.

**P269** Once the announcement phase and the election phase (in the cases of elective corporate action events) are completed, the account servicer may send a CorporateActionMovementPreliminaryAdvice containing the final entitlements and movements to the account owner so as to pre-advise him about the upcoming securities and/or cash movements. The account servicer must also send a CorporateActionConfirmation to the account owner to confirm that the cash and/or securities have been credited and/or debited from/to its account.

## Messages and alternative paths

Source-supported message family mentions: `seev.035`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: BusinessTransactions / Confirmation and Reversal / Confirmation.

## Reviewed source sequence and conditions

For elective events, confirmation follows election; for non-elective events it follows announcement/final entitlement. The Account Servicer may pre-advise movements and must confirm effected cash/securities credits or debits. The drawing uses CorporateActionMovementConfirmation; P269 shortens its name to CorporateActionConfirmation.

[Source sequence reconstruction](../diagrams/business-transactions/fig-0028.md).

| Ordered step | Initiator / sender | Receiver / responsible recipient | Message and source phase |
| --- | --- | --- | --- |
| 1 | Account Servicer | Account Owner | CorporateActionNotification (NEWM) — Preliminary announcement |
| 2 | Account Servicer | Account Owner | CorporateActionNotification (REPL) — Confirmed announcement |
| 3 | Account Owner | Account Servicer | CorporateActionInstruction |
| 4 | Account Servicer | Account Owner | CorporateActionInstructionStatusAdvice |
| 5 | Account Servicer | Account Owner | CorporateActionMovementPreliminaryAdvice (NEWM) — Final entitlement |
| 6 | Account Servicer | Account Owner | CorporateActionMovementConfirmation |


Conditions and exceptions above come from P263-P269. This scenario does not separately enumerate formal precondition/postcondition fields; do not infer additional guarantees. P203-P204 explains the omitted intermediary chain and interchangeable functional-role capacity.

## Exact supplied message bindings

These bindings use the explicitly named message definitions in src-000080. Part 1 artwork itself uses message names, not exact version numbers.

| Source message name | Exact definition | MDR Part 2 locator |
| --- | --- | --- |
| CorporateActionInstruction | [seev.033.001.14](../../../../messages/seev.033.001.14/index.md) | src-000080 file page 274; 5 seev.033.001.14 CorporateActionInstructionV14 |
| CorporateActionInstructionStatusAdvice | [seev.034.001.16](../../../../messages/seev.034.001.16/index.md) | src-000080 file page 320; 6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16 |
| CorporateActionMovementConfirmation | [seev.036.001.17](../../../../messages/seev.036.001.17/index.md) | src-000080 file page 540; 8 seev.036.001.17 CorporateActionMovementConfirmationV17 |
| CorporateActionMovementPreliminaryAdvice | [seev.035.001.17](../../../../messages/seev.035.001.17/index.md) | src-000080 file page 360; 7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17 |
| CorporateActionNotification | [seev.031.001.16](../../../../messages/seev.031.001.16/index.md) | src-000080 file page 23; 3 seev.031.001.16 CorporateActionNotificationV16 |

