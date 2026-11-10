---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p327-scenario-1-mandatory-event-no-preliminary-advice"
title: "Scenario 1: Mandatory Event – No Preliminary Advice"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 1: Mandatory Event – No Preliminary Advice"], "locator": "/w:document/w:body/w:p[327]", "paragraph_id": "P327", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 1: Mandatory Event – No Preliminary Advice"], "locator": "/w:document/w:body/w:p[328]", "paragraph_id": "P328", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 1: Mandatory Event – No Preliminary Advice"], "locator": "/w:document/w:body/w:p[329]", "paragraph_id": "P329", "table_id": null}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Scenario 1: Mandatory Event – No Preliminary Advice"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Source blocks and route letters are retained without assuming exact message versions from abbreviations. Source conditions, not color alone, establish optionality and responsibility."]
manual_curated: true
issue_ids: []
---







# Scenario 1: Mandatory Event – No Preliminary Advice

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P328** This scenario illustrates, using an ISO 150022 notation, a classic business flow for mandatory corporate action events when a preliminary advice flow is not explicitly supported.

Source diagram evidence: [fig-0033](../documents/src-000079/diagrams/fig-0033.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: BusinessTransactions / Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios  / Business Scenarios / Scenario 1: Mandatory Event – No Preliminary Advice.

## Curated source routing scenario

Source scenario 1 is an legacy MT illustration of a mandatory event without explicit preliminary advice support (P327-P328). The original does not label Account Servicer or Account Owner, so reconstruction uses source-message and processing components without adding institutional boundaries.

| Ordered source step | Sender / initiating functional role | Receiver / responsible recipient | Message-block label and action |
| --- | --- | --- | --- |
| A) | Account Servicer | Account Owner: Event Management Process | MT564 / 23G::NEWM / 25D::PREC — Preliminary Announcement confirmed sent prior to Ex Date |
| B) | Account Servicer | Account Owner: Event Management Process | MT564 / 23G::REPE or REPL / 25D::COMP — Confirmed Announcement sent on Ex Date / Final Entitlement (for illustrative purposes only) |
| C) | Account Servicer | Account Owner: Payment Management Process | MT566 / 23G::NEWM / cash and/or securities movement block present — Confirmation of Payment sent on Pay Date |


Source note: No automated solution to identify MT564 as a Final Entitlement message. Manual intervention required for pre-payment reconciliation.

These examples are limited by P300 and P320-P326: preliminary advice is optional at overall-flow level; SLA-specific variations are omitted; preserve actual source colors and conditions. Formal preconditions/postconditions beyond the scenario narrative are not supplied. [Complete source reconstruction](../diagrams/routing-scenarios/fig-0033.md).
