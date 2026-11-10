---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079", "src-000080"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p282-instruction-reporting"
title: "Instruction Reporting"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Instruction Reporting "], "locator": "/w:document/w:body/w:p[282]", "paragraph_id": "P282", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Instruction Reporting "], "locator": "/w:document/w:body/w:p[283]", "paragraph_id": "P283", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Instruction Reporting "], "locator": "/w:document/w:body/w:p[284]", "paragraph_id": "P284", "table_id": null}, {"source_id": "src-000080", "locator": "file page 757; 14 seev.042.001.14 CorporateActionInstructionStatementReportV14"}]
participants: ["participant-src-000079-account-owner", "participant-src-000079-account-servicer"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instructions and Cancellations"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000080", "locator": "file page 274; 5 seev.033.001.14 CorporateActionInstructionV14"}, {"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instructions and Cancellations"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[6]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000080", "locator": "file page 757; 14 seev.042.001.14 CorporateActionInstructionStatementReportV14"}]
message_ids: ["seev.042.001.14"]
message_families: ["seev.033", "seev.042"]
search_terms: ["Instruction Reporting", "Account Servicer", "Account Owner", "seev.033", "seev.042"]
limitations: ["The source diagram and scenario narrative were checked. Formal precondition/postcondition fields and any omitted market-specific handling are not separately defined by this scenario."]
manual_curated: true
diagram_visual_review: "pass"
---





# Instruction Reporting

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, triggering conditions, message direction, exceptions and outcomes are curated below from the named source scenario. Formal precondition/postcondition fields are not separately provided by this scenario.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P283** The account servicer may send a CorporateActionInstructionStatementReport to the account owner at any time to report about the instructed, uninstructed and other balances for one or more corporate action events at a safekeeping account level or to report about the instructed, uninstructed and other balances for one corporate action event but for one or several safekeeping accounts in which the account owner has holdings.

Source diagram evidence: [fig-0031](../documents/src-000079/diagrams/fig-0031.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `seev.033`, `seev.042`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: BusinessTransactions / Instruction Reporting .

## Reviewed source sequence and conditions

The Account Servicer may report instructed, uninstructed and other balances at any time: for one or more events at a safekeeping account, or one event across one or several safekeeping accounts where the Account Owner has holdings.

[Source sequence reconstruction](../diagrams/business-transactions/fig-0031.md).

| Ordered step | Initiator / sender | Receiver / responsible recipient | Message and source phase |
| --- | --- | --- | --- |
| 1 | Account Servicer | Account Owner | CorporateActionInstructionStatementReport |


Conditions and exceptions above come from P283. This scenario does not separately enumerate formal precondition/postcondition fields; do not infer additional guarantees. P203-P204 explains the omitted intermediary chain and interchangeable functional-role capacity.

## Exact supplied message bindings

These bindings use the explicitly named message definitions in src-000080. Part 1 artwork itself uses message names, not exact version numbers.

| Source message name | Exact definition | MDR Part 2 locator |
| --- | --- | --- |
| CorporateActionInstructionStatementReport | [seev.042.001.14](../../../../messages/seev.042.001.14/index.md) | src-000080 file page 757; 14 seev.042.001.14 CorporateActionInstructionStatementReportV14 |

