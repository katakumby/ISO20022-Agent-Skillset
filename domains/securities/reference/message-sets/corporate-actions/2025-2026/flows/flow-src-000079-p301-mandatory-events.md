---
template: false
document_kind: "source-process-section"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_sets: ["corporate-actions"]
flow_id: "flow-src-000079-p301-mandatory-events"
title: "Mandatory Events"
source_locations: [{"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Usage Rules", "Mandatory Events"], "locator": "/w:document/w:body/w:p[301]", "paragraph_id": "P301", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Usage Rules", "Mandatory Events"], "locator": "/w:document/w:body/w:p[302]", "paragraph_id": "P302", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Usage Rules", "Mandatory Events"], "locator": "/w:document/w:body/w:p[303]", "paragraph_id": "P303", "table_id": null}, {"source_id": "src-000079", "heading_path": ["BusinessTransactions", "Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios ", "Usage Rules", "Mandatory Events"], "locator": "/w:document/w:body/w:p[304]", "paragraph_id": "P304", "table_id": null}]
participants: []
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Mandatory Events"]
limitations: ["Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.", "Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.", "Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors."]
---

# Mandatory Events

Source context: Corporate Actions. This reference preserves the source-defined segment and its evidence.

Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.

## Participants

No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.

## Ordered activities and source narrative

**P302** The CA Movement Preliminary Advice can be sent for credit/debit of cash and/or securities. It would be triggered prior to the payment date of the event and may or may not follow an ISO 20022 CA Notification message. 

**P303** Some common examples of cases where the CA Movement Preliminary Advice would be used include Mandatory Income as well as Mandatory Capital events such as: Cash Dividends, Interest Payments, Maturity Payments / Final Redemptions, Partial Redemptions, CMO Payments, Stock Dividends, Stock Splits/Reverse Splits, Return of Capital, Merger (the list is not exhaustive).

**P304** CA Movement Preliminary advice can be sent as a stand-alone message (i.e. not linked to a CA Notification) only in the case of predictable events (Interest payment, maturity payment, …).

## Messages and alternative paths

Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.

## Limitations and provenance

- Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.
- Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.
- Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.

Original: [src-000079](../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Heading path: BusinessTransactions / Movement Preliminary Advice – Detailed Usage in Typical CA Business Scenarios  / Usage Rules / Mandatory Events.
