---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p343-cafe-and-caco-movements-usage-guidelines"
title: "CAFE and CACO Movements usage guidelines"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 5: Mandatory Event with Reversal of Payment"], "locator": "/w:document/w:body/w:p[343]", "paragraph_id": "P343", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 5: Mandatory Event with Reversal of Payment"], "locator": "/w:document/w:body/w:p[344]", "paragraph_id": "P344", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 5: Mandatory Event with Reversal of Payment"], "locator": "/w:document/w:body/w:p[345]", "paragraph_id": "P345", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Business Scenarios", "Scenario 5: Mandatory Event with Reversal of Payment"], "locator": "/w:document/w:body/w:p[346]", "paragraph_id": "P346", "table_id": null}]
participants: ["participant-src-000079-account-servicer"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["CAFE and CACO Movements usage guidelines", "Account Servicer"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# CAFE and CACO Movements usage guidelines

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

| Source role | Canonical scoped record | Evidence interpretation |
| --- | --- | --- |
| Account Servicer | [Participant](../../../../../../../shared/reference/participants/participant-src-000079-account-servicer.md) | Mentioned in this segment; use the activity/narrative evidence for actions and message direction |

## Ordered activities and source narrative

**P344** Movements reported within the CA movement preliminary advice reversal (CAFE reversal) message will be opposite to those reported into the referred CA confirmation message (CACO) i.e. credit of cash and/or securities will become debits and inversely.

**P345** Movements reported within the CA Reversal (CARE) message will be identical to the movements reported into the referred CA confirmation message (CACO).

**P346** If a rebook follows a reversal, it is recommended that the rebook be considered a new payment. Therefore, subject to the pre-advice process if it meets the criteria agreed upon between the account servicer and the account provider.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../evidence/omitted/2628a9d179f54e089e8f29f3.md). Heading path: BusinessTransactions / Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios  / Business Scenarios / Scenario 5: Mandatory Event with Reversal of Payment.
