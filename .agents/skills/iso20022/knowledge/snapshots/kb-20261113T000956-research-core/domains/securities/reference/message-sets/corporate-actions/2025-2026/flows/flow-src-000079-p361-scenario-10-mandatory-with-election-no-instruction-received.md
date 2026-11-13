---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p361-scenario-10-mandatory-with-election-no-instruction-received"
title: "Scenario 10: Mandatory with Election – No Instruction Received"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 10: Mandatory with Election – No Instruction Received"], "locator": "/w:document/w:body/w:p[361]", "paragraph_id": "P361", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 10: Mandatory with Election – No Instruction Received"], "locator": "/w:document/w:body/w:p[362]", "paragraph_id": "P362", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 10: Mandatory with Election – No Instruction Received"], "locator": "/w:document/w:body/w:p[363]", "paragraph_id": "P363", "table_id": null}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instructions and Cancellations"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000080", "locator": "file page 274; 5 seev.033.001.14 CorporateActionInstructionV14"}]
message_ids: []
message_families: ["seev.033"]
search_terms: ["Scenario 10: Mandatory with Election – No Instruction Received", "Account Servicer", "Account Owner", "seev.033"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Source blocks and route letters are retained without assuming exact message versions from abbreviations. Source conditions, not color alone, establish optionality and responsibility.", "Scenario10 narrative P362 conflicts with its title and figure; see issue-000026."]
manual_curated: true
issue_ids: ["issue-000026"]
---







# Scenario 10: Mandatory with Election – No Instruction Received

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P362** The account servicer announces a mandatory with election event. The account owner does provide corporate action instructions therefore (depending on the type of service provided) the account owner sends either a CA Notification with function Reminder. After the deadline the account servicer sends a CA Instruction Status Advice to advice the account owner that the default instruction has been applied to its holdings. A CA Movement Preliminary Advice is finally sent to the account owner followed by a CA Movement Confirmation.

Source diagram evidence: [fig-0042](../documents/src-000079/diagrams/fig-0042.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Source-supported message family mentions: `seev.033`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: BusinessTransactions / Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios  / Business Scenarios / Scenario 10: Mandatory with Election – No Instruction Received.

## Curated source routing scenario

P361 title and image42 show no instruction received: the Account Servicer sends a reminder, then default-action status after the deadline, preliminary advice, and payment confirmation. P362 contradicts this by saying the owner does provide instructions and sends the reminder. Both source claims remain visible under issue-000026; this reconstruction preserves the artwork direction.

| Ordered source step | Sender / initiating functional role | Receiver / responsible recipient | Message-block label and action |
| --- | --- | --- | --- |
| A) | Account Servicer | Account Owner: Event Management Process | CANO / NEWM / Confirmed-Incomplete — Preliminary Announcement confirmed sent prior to Ex Date |
| B) | Account Servicer | Account Owner: Event Management Process | CANO / REPL / Balance only or Balance & Entl / Confirmed-Complete — Confirmed Announcement sent on Ex Date (for illustrative purposes only) |
| C) | Account Servicer | Account Owner: Response Management Process | CANO / RMDR — Reminder of event details and uninstructed/instructed balance or response status sent prior to deadline |
| D) | Account Servicer | Account Owner: Response Management Process | CAIS / Processing status: Default Action — Instruction Status sent upon application of default instruction |
| E) | Account Servicer | Account Owner: Payment Management Process | CAPA / Cash and/or securities movement block present — Final Entitlement Preliminary movement advice sent upon confirm of instruction |
| F) | Account Servicer | Account Owner: Payment Management Process | CACO / NEWM / cash and/or securities movement block present — Confirm of Payment |


Deadline boundary follows C).

These examples are limited by P300 and P320-P326: preliminary advice is optional at overall-flow level; SLA-specific variations are omitted; preserve actual source colors and conditions. Formal preconditions/postconditions beyond the scenario narrative are not supplied. [Complete source reconstruction](../diagrams/routing-scenarios/fig-0042.md).
