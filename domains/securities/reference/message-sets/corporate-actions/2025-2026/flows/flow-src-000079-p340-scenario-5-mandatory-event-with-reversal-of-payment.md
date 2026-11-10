---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p340-scenario-5-mandatory-event-with-reversal-of-payment"
title: "Scenario 5: Mandatory Event with Reversal of Payment"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 5: Mandatory Event with Reversal of Payment"], "locator": "/w:document/w:body/w:p[340]", "paragraph_id": "P340", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 5: Mandatory Event with Reversal of Payment"], "locator": "/w:document/w:body/w:p[341]", "paragraph_id": "P341", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 5: Mandatory Event with Reversal of Payment"], "locator": "/w:document/w:body/w:p[342]", "paragraph_id": "P342", "table_id": null}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Scenario 5: Mandatory Event with Reversal of Payment", "Account Servicer"]
limitations: ["Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.", "Source blocks and route letters are retained without assuming exact message versions from abbreviations. Source conditions, not color alone, establish optionality and responsibility."]
manual_curated: true
issue_ids: []
---







# Scenario 5: Mandatory Event with Reversal of Payment

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P341** The account servicer announces a mandatory event. A CA Movement Preliminary Advice is sent prior to payment date. Following confirmation of the payment, a reversal needs to be made for which a CA Movement Preliminary Advice of reversal is made prior to the effective reversal of payment.

Source diagram evidence: [fig-0037](../documents/src-000079/diagrams/fig-0037.md). Mermaid reconstruction and visual review are pending.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Focused flow curation is recorded in linked diagram and narrative evidence; table review remains independent of diagram review.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: BusinessTransactions / Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios  / Business Scenarios / Scenario 5: Mandatory Event with Reversal of Payment.

## Curated source routing scenario

P341: after payment confirmation, a required reversal is pre-advised before the effective reversal. P344-P346 distinguishes reversed preliminary-advice movement directions from CARE reported directions and treats a later rebook as a new payment.

| Ordered source step | Sender / initiating functional role | Receiver / responsible recipient | Message-block label and action |
| --- | --- | --- | --- |
| A) | Account Servicer | Account Owner: Event Management Process | CANO / NEWM / Confirmed-Incomplete — Preliminary Announcement confirmed sent prior to Ex Date |
| B) | Account Servicer | Account Owner: Event Management Process | CANO / REPL / Balance only or Balance & Entl / Confirmed-Complete — Confirmed Announcement sent on Ex Date (for illustrative purposes only) |
| C) | Account Servicer | Account Owner: Payment Management Process | CAPA / Cash and/or securities movement block present — Movement Preliminary Advice sent prior to Pay Date |
| D) | Account Servicer | Account Owner: Payment Management Process | CACO / NEWM / cash and/or securities movement block present — Confirmation of Payment sent on Pay Date |
| E) | Account Servicer | Account Owner: Payment Management Process | CAPA / Reversal / Cash and/or securities movement block present — Movement Preliminary Advice of reversal sent after Pay Date |
| F) | Account Servicer | Account Owner: Payment Management Process | CARE / NEWM / cash and/or securities movement block present — Reversal of Payment |


These examples are limited by P300 and P320-P326: preliminary advice is optional at overall-flow level; SLA-specific variations are omitted; preserve actual source colors and conditions. Formal preconditions/postconditions beyond the scenario narrative are not supplied. [Complete source reconstruction](../diagrams/routing-scenarios/fig-0037.md).
