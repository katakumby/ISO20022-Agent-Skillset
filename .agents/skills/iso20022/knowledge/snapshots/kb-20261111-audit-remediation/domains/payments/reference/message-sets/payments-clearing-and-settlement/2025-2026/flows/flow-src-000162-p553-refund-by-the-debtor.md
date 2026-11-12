---
template: false
document_kind: "business-flow"
review_status: "reviewed"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
flow_id: "flow-src-000162-p553-refund-by-the-debtor"
title: "Refund by the Debtor"
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "PaymentReturn with Direct Debit", "Refund by the Debtor"], "locator": "/w:document/w:body/w:p[553]", "paragraph_id": "P553", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "PaymentReturn with Direct Debit", "Refund by the Debtor"], "locator": "/w:document/w:body/w:p[554]", "paragraph_id": "P554", "table_id": null}, {"source_id": "src-000162", "heading_path": ["BusinessTransactions", "Direct Debit", "PaymentReturn with Direct Debit", "Refund by the Debtor"], "locator": "/w:document/w:body/w:p[555]", "paragraph_id": "P555", "table_id": null}]
participants: ["participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-clearing-and-settlement-agent"]
message_mapping_evidence: [{"source_id": "src-000162", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Related Messages"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}]
message_ids: []
message_families: ["pacs.004"]
search_terms: ["Refund by the Debtor", "Settlement Agent", "Debtor agent", "Debtor", "pacs.004"]
limitations: ["Refund request is non-automated and outside ISO message scope in P537/P555."]
manual_curated: true
participant_ids: ["participant-src-000162-debtor", "participant-src-000162-debtor-agent", "participant-src-000162-clearing-and-settlement-agent"]
related_diagrams: ["domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/diagrams/clearing/fig-0041.md"]
---

# Debtor refund request

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md); P537–538, P553–555.

Debtor requests refund from debtor agent, assumed non-automated (phone/fax) in this source. This triggers the PaymentReturn route, carrying a code indicating debtor-requested refund. No separate formal pre/postcondition is supplied beyond this trigger and return outcome.

[Complete return/refund flow, participant responsibilities and literal sequence](flow-src-000162-p539-payment-return-initiated-by-debtor-agent.md)
