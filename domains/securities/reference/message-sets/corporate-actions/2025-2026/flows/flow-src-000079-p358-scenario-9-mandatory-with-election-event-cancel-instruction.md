---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p358-scenario-9-mandatory-with-election-event-cancel-instruction"
title: "Scenario 9: Mandatory with Election Event - Cancel Instruction"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 9: Mandatory with Election Event - Cancel Instruction"], "locator": "/w:document/w:body/w:p[358]", "paragraph_id": "P358", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 9: Mandatory with Election Event - Cancel Instruction"], "locator": "/w:document/w:body/w:p[359]", "paragraph_id": "P359", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 9: Mandatory with Election Event - Cancel Instruction"], "locator": "/w:document/w:body/w:p[360]", "paragraph_id": "P360", "table_id": null}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instructions and Cancellations"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000080", "locator": "file page 274; 5 seev.033.001.14 CorporateActionInstructionV14"}]
message_ids: []
message_families: ["seev.033"]
search_terms: ["Scenario 9: Mandatory with Election Event - Cancel Instruction", "Account Servicer", "Account Owner", "seev.033"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Source blocks and route letters are retained without assuming exact message versions from abbreviations. Source conditions, not color alone, establish optionality and responsibility."]
manual_curated: true
issue_ids: []
---







# Scenario 9: Mandatory with Election Event - Cancel Instruction

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P359** The account servicer announces a mandatory with election or a voluntary event. A CA Movement Preliminary Advice is sent to the account owner after receipt of its corporate action instruction. The account owner subsequently cancels its corporate action instruction. The acceptance of the corporate action instruction cancellation by the account servicer is followed by the sending of a CA Movement Preliminary Advice Cancellation Advice. After the instruction deadline, a CA Movement Preliminary Advice is sent to the account owner followed by a CA Movement Confirmation.

Source diagram evidence: [fig-0041](../documents/src-000079/diagrams/fig-0041.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `seev.033`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: BusinessTransactions / Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios  / Business Scenarios / Scenario 9: Mandatory with Election Event - Cancel Instruction.

## Curated source routing scenario

P359: an accepted instruction cancellation causes cancellation of the earlier preliminary advice. After the instruction deadline, new preliminary advice is followed by confirmation. Source default-action status and replacement-final-entitlement labels are preserved.

| Ordered source step | Sender / initiating functional role | Receiver / responsible recipient | Message-block label and action |
| --- | --- | --- | --- |
| A) | Account Servicer | Account Owner: Event Management Process | CANO / NEWM / Confirmed-Incomplete — Preliminary Announcement confirmed sent prior to Ex Date |
| B) | Account Servicer | Account Owner: Event Management Process | CANO / REPL / Balance only or Balance & Entl / Confirmed-Complete — Confirmed Announcement sent on Ex Date (for illustrative purposes only) |
| C) | Account Owner | Account Servicer | CAIN — New instruction |
| D) | Account Servicer | Account Owner: Response Management Process | CAIS / Accepted instruction — Confirm of Instruction |
| E) | Account Servicer | Account Owner: Payment Management Process | CAPA / Cash and/or securities movement block present — Final Entitlement Preliminary movement advice sent upon confirm of instruction |
| F) | Account Owner | Account Servicer | CAIC — Instruction Cancellation Request |
| G) | Account Servicer | Account Owner: Response Management Process | CACS / Accepted cancellation request — Instruction status |
| H) | Account Servicer | Account Owner: Payment Management Process | CAPC / Cancellation of CAPA — Movement Preliminary Advice cancellation |
| I) | Account Servicer | Account Owner: Response Management Process | CAIS / Processing status: Default Action — Instruction Status sent upon application of default instruction |
| J) | Account Servicer | Account Owner: Payment Management Process | CAPA / Cash and/or securities movement block present — Replacement Final Entitlement Preliminary movement advice sent upon confirm of instruction |
| K) | Account Servicer | Account Owner: Payment Management Process | CACO / NEWM / cash and/or securities movement block present — Confirm of Payment |


Deadline boundary follows H).

These examples are limited by P300 and P320-P326: preliminary advice is optional at overall-flow level; SLA-specific variations are omitted; preserve actual source colors and conditions. Formal preconditions/postconditions beyond the scenario narrative are not supplied. [Complete source reconstruction](../diagrams/routing-scenarios/fig-0041.md).
