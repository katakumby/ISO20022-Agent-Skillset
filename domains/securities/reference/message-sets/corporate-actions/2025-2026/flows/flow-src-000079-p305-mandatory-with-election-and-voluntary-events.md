---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p305-mandatory-with-election-and-voluntary-events"
title: "Mandatory with Election and Voluntary Events"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Usage Rules", "Mandatory with Election and Voluntary Events"], "locator": "/w:document/w:body/w:p[305]", "paragraph_id": "P305", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Usage Rules", "Mandatory with Election and Voluntary Events"], "locator": "/w:document/w:body/w:p[306]", "paragraph_id": "P306", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Usage Rules", "Mandatory with Election and Voluntary Events"], "locator": "/w:document/w:body/w:p[307]", "paragraph_id": "P307", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Usage Rules", "Mandatory with Election and Voluntary Events"], "locator": "/w:document/w:body/w:p[308]", "paragraph_id": "P308", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Usage Rules", "Mandatory with Election and Voluntary Events"], "locator": "/w:document/w:body/w:p[309]", "paragraph_id": "P309", "table_id": null}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Mandatory with Election and Voluntary Events"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Mandatory with Election and Voluntary Events

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P306** ISO 20022 CA Movement Preliminary Advice can be sent as the communication method for Final Entitlement replacing the CA Notification message for this purpose. The CA Movement Preliminary Advice for Mandatory with Election and Voluntary events can be sent for credit/debit of cash and/or securities upon confirmation of the instruction. This is consistent with the current market practice of final entitlement.

**P307** The Movement Preliminary Advice is formatted with all the movements associated with the option, even though more than one final confirmation of payment message may have to be sent depending on posting dates. 

**P308** For instance, in the case of a Rights Issue where the Exercise option is elected, the Movement Preliminary Advice will identify the following movements; Cash Debit Movement, Share Credit Movement, and Share Debit Movement. 

**P309** However, several final payment confirmations (in an ISO 20022 CA Confirmation messages) may have to be sent as the payment dates may be different for each movement.

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: BusinessTransactions / Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios  / Usage Rules / Mandatory with Election and Voluntary Events.
