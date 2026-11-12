---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p367-scenario-12-voluntary-event-partial-election"
title: "Scenario 12: Voluntary Event – Partial Election"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 12: Voluntary Event – Partial Election"], "locator": "/w:document/w:body/w:p[367]", "paragraph_id": "P367", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 12: Voluntary Event – Partial Election"], "locator": "/w:document/w:body/w:p[368]", "paragraph_id": "P368", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 12: Voluntary Event – Partial Election"], "locator": "/w:document/w:body/w:p[369]", "paragraph_id": "P369", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 12: Voluntary Event – Partial Election"], "locator": "/w:document/w:body/w:p[370]", "paragraph_id": "P370", "table_id": null}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: [{"source_id": "src-000079", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Instructions and Cancellations"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000080", "locator": "file page 274; 5 seev.033.001.14 CorporateActionInstructionV14"}]
message_ids: []
message_families: ["seev.033"]
search_terms: ["Scenario 12: Voluntary Event – Partial Election", "Account Servicer", "Account Owner", "seev.033"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Source blocks and route letters are retained without assuming exact message versions from abbreviations. Source conditions, not color alone, establish optionality and responsibility."]
manual_curated: true
issue_ids: []
---







# Scenario 12: Voluntary Event – Partial Election

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |
| Account Owner | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-owner.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P368** The account servicer announces a voluntary event for which two consecutive partial corporate action instructions are received from the account owner. The account servicer sends a CA Movement Preliminary Advice following each corporate action instruction received.

Source diagram evidence: [fig-0044](../documents/src-000079/diagrams/fig-0044.md). Mermaid reconstruction and visual review are pending.

**P370** Regarding split elections between options, it is understood that since one CA Confirmation is sent per elected option, a separate CA Movement Preliminary Advice message will be sent for each option elected.


## Messages and alternative paths

Source-supported message family mentions: `seev.033`. Full versions are retained only when explicitly present: none established in this segment.

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: BusinessTransactions / Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios  / Business Scenarios / Scenario 12: Voluntary Event – Partial Election.

## Curated source routing scenario

P368: two consecutive partial instructions are received, with preliminary advice after each. P370: when splitting elections between options, a separate preliminary advice is sent for each elected option, consistent with a separate confirmation per option.

| Ordered source step | Sender / initiating functional role | Receiver / responsible recipient | Message-block label and action |
| --- | --- | --- | --- |
| A) | Account Servicer | Account Owner: Event Management Process | CANO / NEWM / Confirmed-Incomplete — Preliminary Announcement confirmed sent prior to Ex Date |
| B) | Account Servicer | Account Owner: Event Management Process | CANO / REPL / Balance only or Balance & Entl / Confirmed-Complete — Confirmed Announcement sent on Ex Date (for illustrative purposes only) |
| C) | Account Owner | Account Servicer | CAIN / Partial election — New instruction |
| D) | Account Servicer | Account Owner: Response Management Process | CAIS / Accepted instruction — Instruction status |
| E) | Account Servicer | Account Owner: Payment Management Process | CAPA / Cash and/or securities movement block present — Final Entitlement Preliminary movement advice sent upon confirm of instruction |
| F) | Account Owner | Account Servicer | CAIN / remaining election (same option) — New instruction |
| G) | Account Servicer | Account Owner: Response Management Process | CAIS / Accepted instruction — instruction status |
| H) | Account Servicer | Account Owner: Payment Management Process | CAPA / Replacement / Cash and/or securities movement block present — Replacement of the Preliminary Movement Advice sent prior to Pay Date |
| I) | Account Servicer | Account Owner: Payment Management Process | CACO / NEWM / cash and/or securities movement block present — Confirm of Payment |


Deadline boundary follows G).

These examples are limited by P300 and P320-P326: preliminary advice is optional at overall-flow level; SLA-specific variations are omitted; preserve actual source colors and conditions. Formal preconditions/postconditions beyond the scenario narrative are not supplied. [Complete source reconstruction](../diagrams/routing-scenarios/fig-0044.md).
