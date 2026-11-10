---
template: false
document_kind: "business-flow"
review_status: "needs-review"
manual_curated: true
domain: "securities"
flow_id: "flow-corporate-actions-market-claims-tax-refunds"
title: "Market claim, compensation and tax refund preliminary advice"
source_ids: ["src-000079"]
message_sets: ["corporate-actions"]
source_locations: [{"source_id": "src-000079", "locator": "BusinessTransactions / Movement Preliminary Advice - Detailed Usage in Typical CA Business Scenarios / Scenario 13; P371-P397; image45.emf-image48.emf"}]
participants: ["participant-src-000079-account-servicer", "participant-src-000079-account-owner"]
limitations: ["The source drawings do not define formal triggers, preconditions, postconditions, exact message versions or reason for acronym CAPA versus CAFE in table T6."]
source_editions: ["February 2026"]
---

# Market claim, compensation and tax refund preliminary advice

Source src-000079, Scenario 13 P371-P397. Four diagram variants specify the communication and internal routing for these contexts; no additional triggering conditions are inferred.

## Source routing variants

The Account Servicer initiates each pictured communication. The Account Owner receives it through its Message Gateway and routes it to its Payment Management Process. These are internal processing entities, not extra institutional actors. Each context shows either A) initial CAPA then B) replacement CAPA and D) CACO confirmation, or A) initial CAPA then B) CAPC cancellation. The source does not show a movement reversal in the cancellation variants. CAPA/CAPC/CACO labels and the missing C) path lettering are retained exactly; no unsupported acronym equivalence is asserted.

- [fig-0045](../diagrams/claims-tax/fig-0045.md)
- [fig-0046](../diagrams/claims-tax/fig-0046.md)
- [fig-0047](../diagrams/claims-tax/fig-0047.md)
- [fig-0048](../diagrams/claims-tax/fig-0048.md)
