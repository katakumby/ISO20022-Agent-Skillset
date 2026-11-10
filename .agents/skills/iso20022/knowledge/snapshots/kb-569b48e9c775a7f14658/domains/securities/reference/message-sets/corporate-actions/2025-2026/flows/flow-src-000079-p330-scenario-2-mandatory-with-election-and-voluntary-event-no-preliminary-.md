---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p330-scenario-2-mandatory-with-election-and-voluntary-event-no-preliminary-"
title: "Scenario 2: Mandatory with Election and Voluntary Event - No Preliminary Advice"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 2: Mandatory with Election and Voluntary Event - No Preliminary Advice "], "locator": "/w:document/w:body/w:p[330]", "paragraph_id": "P330", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 2: Mandatory with Election and Voluntary Event - No Preliminary Advice "], "locator": "/w:document/w:body/w:p[331]", "paragraph_id": "P331", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 2: Mandatory with Election and Voluntary Event - No Preliminary Advice "], "locator": "/w:document/w:body/w:p[332]", "paragraph_id": "P332", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 2: Mandatory with Election and Voluntary Event - No Preliminary Advice "], "locator": "/w:document/w:body/w:p[333]", "paragraph_id": "P333", "table_id": null}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Scenario 2: Mandatory with Election and Voluntary Event - No Preliminary Advice"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Source blocks and route letters are retained without assuming exact message versions from abbreviations. Source conditions, not color alone, establish optionality and responsibility.", "Exact punctuation of the small MT567 field-tag label remains uncertain in the supplied low-resolution source image; visual review requires original reconciliation."]
manual_curated: true
issue_ids: ["issue-000027"]
---







# Scenario 2: Mandatory with Election and Voluntary Event - No Preliminary Advice

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P331** This scenario illustrates, using an ISO 150022 notation, a classic business flow for mandatory corporate action events with election or voluntary corporate action events when a preliminary advice flow is not explicitly supported.

Source diagram evidence: [fig-0034](../documents/src-000079/diagrams/fig-0034.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: BusinessTransactions / Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios  / Business Scenarios / Scenario 2: Mandatory with Election and Voluntary Event - No Preliminary Advice .

## Curated source routing scenario

Source scenario 2 is an legacy MT illustration for election/voluntary events without explicit preliminary advice support (P330-P331). The source calls the response component Response Management System, not Process. The outgoing MT565 label is near the gateway without a separately drawn connecting arrow. The original punctuation in MT567 is low resolution; retain the original for exact field-tag review.

| Ordered source step | Sender / initiating functional role | Receiver / responsible recipient | Message-block label and action |
| --- | --- | --- | --- |
| A) | Account Servicer | Account Owner: Event Management Process | MT564 / 23G::NEWM / 25D::PROC//PREC — Preliminary Announcement confirmed sent prior to Ex Date |
| B) | Account Servicer | Account Owner: Event Management Process | MT564 / 23G::REPE or REPL / 25D::PROC//COMP — Confirmed Announcement sent on Ex Date (for illustrative purposes only) |
| C) | Account Owner | Account Servicer | MT565 / 23G::NEWM — New instruction |
| D) | Account Servicer | Account Owner: Response Management System | MT567 / 23G::INST / 25D::IPRC [separator unclear] PACK — Confirm of Instruction |
| E) | Account Servicer | Account Owner: Event Management Process | MT564 / 23G::REPE or REPL / 25D::PROC//COMP — Confirmed Announcement sent on Ex Date / Final Entitlement (for illustrative purposes only) |
| F) | Account Servicer | Account Owner: Payment Management Process | MT566 / 23G::NEWM / cash and/or securities movement block present — Confirmation of Payment sent on Pay Date |


Source note: No automated solution to identify MT564 as a Final Entitlement message. Manual intervention required for pre-payment reconciliation. Inbound MT567 matches with MT565.

These examples are limited by P300 and P320-P326: preliminary advice is optional at overall-flow level; SLA-specific variations are omitted; preserve actual source colors and conditions. Formal preconditions/postconditions beyond the scenario narrative are not supplied. [Complete source reconstruction](../diagrams/routing-scenarios/fig-0034.md).

Source-legibility limitation: P332/image34 does not establish whether the MT567 IPRC-to-PACK separator has one or two slash strokes. Both the unmodified original and enlarged inspection crop were reviewed; issue-000027 remains open.
