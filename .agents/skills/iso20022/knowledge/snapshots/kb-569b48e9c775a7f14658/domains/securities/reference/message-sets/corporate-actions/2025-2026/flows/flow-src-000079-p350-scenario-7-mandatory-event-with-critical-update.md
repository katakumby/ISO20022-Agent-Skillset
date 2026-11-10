---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p350-scenario-7-mandatory-event-with-critical-update"
title: "Scenario 7: Mandatory Event with Critical Update"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 7: Mandatory Event with Critical Update"], "locator": "/w:document/w:body/w:p[350]", "paragraph_id": "P350", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 7: Mandatory Event with Critical Update"], "locator": "/w:document/w:body/w:p[351]", "paragraph_id": "P351", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 7: Mandatory Event with Critical Update"], "locator": "/w:document/w:body/w:p[352]", "paragraph_id": "P352", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 7: Mandatory Event with Critical Update"], "locator": "/w:document/w:body/w:p[353]", "paragraph_id": "P353", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 7: Mandatory Event with Critical Update"], "locator": "/w:document/w:body/w:p[354]", "paragraph_id": "P354", "table_id": null}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Scenario 7: Mandatory Event with Critical Update", "Account Servicer"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Source blocks and route letters are retained without assuming exact message versions from abbreviations. Source conditions, not color alone, establish optionality and responsibility."]
manual_curated: true
issue_ids: []
---







# Scenario 7: Mandatory Event with Critical Update

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P351** The account servicer announces a mandatory event. A CA Movement Preliminary Advice is sent prior to payment date. Following this advice, a critical update is sent by the account servicer, followed by an updated CA Movement Preliminary Advice.

Source diagram evidence: [fig-0039](../documents/src-000079/diagrams/fig-0039.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: BusinessTransactions / Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios  / Business Scenarios / Scenario 7: Mandatory Event with Critical Update.

## Curated source routing scenario

P351: a critical event update after preliminary advice is followed by an updated preliminary advice. P311 recommends replacement after recalculation while cash/securities are not yet posted.

| Ordered source step | Sender / initiating functional role | Receiver / responsible recipient | Message-block label and action |
| --- | --- | --- | --- |
| A) | Account Servicer | Account Owner: Event Management Process | CANO / NEWM / Confirmed-Incomplete — Preliminary Announcement confirmed sent prior to Ex Date |
| B) | Account Servicer | Account Owner: Event Management Process | CANO / REPL / Balance only or Balance & Entl / Confirmed-Complete — Confirmed Announcement sent on Ex Date (for illustrative purposes only) |
| C) | Account Servicer | Account Owner: Payment Management Process | CAPA / Cash and/or securities movement block present — Movement Preliminary Advice sent prior to Pay Date |
| D) | Account Servicer | Account Owner: Event Management Process | CANO / REPL / Balance only or Balance & Entl / Confirmed-Complete — Replacement announcement for Critical update eg. rate change |
| E) | Account Servicer | Account Owner: Payment Management Process | CAPA / Replacement / Cash and/or securities movement block present — Replacement of the Preliminary Movement Advice sent prior to Pay Date (for illustrative purposes only) |
| F) | Account Servicer | Account Owner: Payment Management Process | CACO / NEWM / cash and/or securities movement block present — Confirmation of Payment sent on Pay Date |


These examples are limited by P300 and P320-P326: preliminary advice is optional at overall-flow level; SLA-specific variations are omitted; preserve actual source colors and conditions. Formal preconditions/postconditions beyond the scenario narrative are not supplied. [Complete source reconstruction](../diagrams/routing-scenarios/fig-0039.md).
