---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000347-settlement-infrastructure"
title: "Settlement Infrastructure"
source_labels: ["Settlement Infrastructure"]
role_type: "source-scoped operational participant"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
source_locations: [{"source_id": "src-000347", "locator": "P122; image8/P124; T11"}]
message_sets: ["t2s-billing"]
message_ids: ["camt.077.001.01"]
flows: ["flow-src-000347-p121-billing-report", "flow-src-000347-p156-billing-report"]
aliases: []
limitations: ["No identifier scheme is assigned to this role in the cited passage. Contextual functional-role correspondences do not identify a particular institution."]
---





# Settlement Infrastructure

The billing report activity participant identified with the executing party by P122.

## Responsibilities and relationships

Checks billing event, generates invoice data, delivers and stores cumulative invoices, or generates/delivers invoice cancellation when invoice processing is cancelled.

Source [src-000347](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`; P122; image8/P124; T11.

Billing source context: [Billing report activity](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0008.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p121-billing-report.md).

Billing source context: [Billing report push sequence](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0011.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p156-billing-report.md).
