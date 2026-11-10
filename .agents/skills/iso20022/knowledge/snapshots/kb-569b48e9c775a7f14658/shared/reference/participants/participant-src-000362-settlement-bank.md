---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000362-settlement-bank"
title: "Settlement Bank"
source_labels: ["Settlement Bank"]
role_type: "source-scoped functional participant"
source_ids: ["src-000362"]
source_editions: ["february-2025"]
source_locations: [{"source_id": "src-000362", "locator": "P51/P53; word/media/image2.png"}]
message_sets: ["t2s-limit-utilisation-journal"]
message_ids: ["camt.064.001.01", "camt.065.001.01"]
flows: ["flow-src-000362-p137-pull-mode"]
aliases: []
limitations: ["No identifier scheme or general institution equivalence is stated in this passage."]
---



# Settlement Bank

A query-capable class named by P51 and scope image2; the detailed T6 role table instead defines Payment Bank. Preserve the separate source label without inferring that every settlement bank is a payment bank.

Source [src-000362](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`; P51/P53; word/media/image2.png.

Limit-journal source context: [Limit-utilisation journal scope exchange](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/diagrams/curated/fig-0001.md). [flow Pull mode](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/flows/flow-src-000362-p137-pull-mode.md).
