---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p364-scenario-11-voluntary-event-cancel-and-rebook-instruction"
title: "Scenario 11: Voluntary Event – Cancel and Rebook Instruction"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 11: Voluntary Event – Cancel and Rebook Instruction"], "locator": "/w:document/w:body/w:p[364]", "paragraph_id": "P364", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 11: Voluntary Event – Cancel and Rebook Instruction"], "locator": "/w:document/w:body/w:p[365]", "paragraph_id": "P365", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 11: Voluntary Event – Cancel and Rebook Instruction"], "locator": "/w:document/w:body/w:p[366]", "paragraph_id": "P366", "table_id": null}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instructions and Cancellations"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000080", "locator": "file page 274; 5 seev.033.001.14 CorporateActionInstructionV14"}]
message_ids: []
message_families: ["seev.033"]
search_terms: ["Scenario 11: Voluntary Event – Cancel and Rebook Instruction", "Account Servicer", "Account Owner", "seev.033"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Source blocks and route letters are retained without assuming exact message versions from abbreviations. Source conditions, not color alone, establish optionality and responsibility."]
manual_curated: true
issue_ids: []
---







# Scenario 11: Voluntary Event – Cancel and Rebook Instruction

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P365** The account servicer announces a voluntary event. The account servicer sends a CA Movement Preliminary Advice message to the account owner following the receipt of its corporate action instruction. The account owner cancels its corporate action instruction. The account servicer then cancels the sent CA Movement Preliminary Advice message and sends a new CA Movement Preliminary Advice message following the receipt of the new corporate action instruction from the account owner.

Source diagram evidence: [fig-0043](../documents/src-000079/diagrams/fig-0043.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `seev.033`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: BusinessTransactions / Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios  / Business Scenarios / Scenario 11: Voluntary Event – Cancel and Rebook Instruction.

## Curated source routing scenario

P365: voluntary-event instruction is cancelled and rebooked. The servicer cancels prior preliminary advice and sends new preliminary advice after the new instruction. The source J) CAIS block is black-bordered with orange message arrows, retained as separate observed attributes.

| Ordered source step | Sender / initiating functional role | Receiver / responsible recipient | Message-block label and action |
| --- | --- | --- | --- |
| A) | Account Servicer | Account Owner: Event Management Process | CANO / NEWM / Confirmed-Incomplete — Preliminary Announcement confirmed sent prior to Ex Date |
| B) | Account Servicer | Account Owner: Event Management Process | CANO / REPL / Balance only or Balance & Entl / Confirmed-Complete — Confirmed Announcement sent on Ex Date (for illustrative purposes only) |
| C) | Account Owner | Account Servicer | CAIN — New instruction |
| D) | Account Servicer | Account Owner: Response Management Process | CAIS / Accepted instruction — Instruction status |
| E) | Account Servicer | Account Owner: Payment Management Process | CAPA / Cash and/or securities movement block present — Final Entitlement Preliminary movement advice sent upon confirm of instruction |
| F) | Account Owner | Account Servicer | CAIC — Instruction Cancellation Request |
| G) | Account Servicer | Account Owner: Response Management Process | CACS / Accepted cancellation request — Instruction status |
| H) | Account Servicer | Account Owner: Payment Management Process | CAPC / Cancellation of CAPA — Movement Preliminary Advice cancellation |
| I) | Account Owner | Account Servicer | CAIN — New instruction |
| J) | Account Servicer | Account Owner: Response Management Process | CAIS / Accepted instruction — instruction Status |
| K) | Account Servicer | Account Owner: Payment Management Process | CAPA / Cash and/or securities movement block present — Final Entitlement Preliminary movement advice sent upon confirm of instruction |
| L) | Account Servicer | Account Owner: Payment Management Process | CACO / NEWM / cash and/or securities movement block present — Confirm of Payment |


Deadline boundary follows J).

Source note: The source Deadline label has a small upward blue pointer toward the preceding J) status; the deadline boundary remains between J) and K). No extra business message is inferred.

These examples are limited by P300 and P320-P326: preliminary advice is optional at overall-flow level; SLA-specific variations are omitted; preserve actual source colors and conditions. Formal preconditions/postconditions beyond the scenario narrative are not supplied. [Complete source reconstruction](../diagrams/routing-scenarios/fig-0043.md).
