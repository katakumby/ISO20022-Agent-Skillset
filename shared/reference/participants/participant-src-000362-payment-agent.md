---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000362-payment-agent"
title: "Payment Agent"
source_labels: ["Payment Agent"]
role_type: "source-scoped functional participant"
source_ids: ["src-000362"]
source_editions: ["february-2025"]
source_locations: [{"source_id": "src-000362", "locator": "P96/P99/P111; images3/4"}]
message_sets: ["t2s-limit-utilisation-journal"]
message_ids: ["camt.064.001.01", "camt.065.001.01"]
flows: ["flow-src-000362-p132-query-report-process", "flow-src-000362-p137-pull-mode"]
aliases: []
limitations: ["No identifier scheme or general institution equivalence is stated in this passage."]
---





# Payment Agent

The context diagram labels PaymentAgent with FinancialInstitution; the communication diagram uses the combined source label Payment Agent/Bank on the instructing side. This supports a contextual cross-link to Payment Bank, not a universal equivalence.

Source [src-000362](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`; P96/P99/P111; images3/4.

Limit-journal source context: [Limit process actors and reporting scope](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0002.md). [flow Query Report Process](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p132-query-report-process.md).

Limit-journal source context: [Limit reporting communication roles](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0003.md). [flow Pull mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p137-pull-mode.md).
