---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000347-operator"
title: "Operator"
source_labels: ["Operator"]
role_type: "source-scoped operational participant"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
source_locations: [{"source_id": "src-000347", "locator": "P166-P168"}]
message_sets: ["t2s-billing"]
message_ids: ["camt.077.001.01"]
flows: ["flow-src-000347-p121-billing-report", "flow-src-000347-p156-billing-report"]
aliases: []
limitations: ["No identifier scheme is assigned to this role in the cited passage. Contextual functional-role correspondences do not identify a particular institution."]
---





# Operator

The narrative participant that has submitted an invoice cancellation request before the cancellation-status report is generated.

## Responsibilities and relationships

Submits the prior cancellation request; cancellation status is reported after its processing. The source does not draw this participant in the typical report sequence or identify the cancellation-request message.

Source [src-000347](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`; P166-P168.

Billing source context: [Billing report activity](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0008.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p121-billing-report.md).

Billing source context: [Billing report push sequence](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0011.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p156-billing-report.md).
