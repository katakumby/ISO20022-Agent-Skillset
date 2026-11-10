---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000347-system-member"
title: "System Member"
source_labels: ["System Member"]
role_type: "source-scoped operational participant"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
source_locations: [{"source_id": "src-000347", "locator": "T8; P117/image7/P119; P122/image8/P124"}]
message_sets: ["t2s-billing"]
message_ids: ["camt.076.001.01", "camt.077.001.01"]
flows: ["flow-src-000347-p110-billing-report", "flow-src-000347-p116-query-billing-information", "flow-src-000347-p121-billing-report", "flow-src-000347-p129-positive-scenario", "flow-src-000347-p142-negative-scenario", "flow-src-000347-p156-billing-report"]
aliases: []
limitations: ["No identifier scheme is assigned to this role in the cited passage. Contextual functional-role correspondences do not identify a particular institution."]
---













# System Member

The billing-data requester and invoice/report recipient in the billing activities. P117 and P122 explicitly identify this participant with the Instructing Party within those flows.

## Responsibilities and relationships

Requests cumulative or itemised data; handles errors and returned data; receives cumulative invoice or invoice cancellation. T8 allows inquiry of generated invoices regardless of cancelled/not-confirmed status; the Billing Reference (Invoice Number) distinct search criterion can ensure active confirmed data.

Source [src-000347](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`; T8; P117/image7/P119; P122/image8/P124.

Billing source context: [Billing process overview](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0002.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p110-billing-report.md).

Billing source context: [Query billing information activity](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0007.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p116-query-billing-information.md).

Billing source context: [Billing report activity](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0008.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p121-billing-report.md).

Billing source context: [Successful billing information query](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0009.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p129-positive-scenario.md).

Billing source context: [Rejected billing information query](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0010.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p142-negative-scenario.md).

Billing source context: [Billing report push sequence](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0011.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p156-billing-report.md).
