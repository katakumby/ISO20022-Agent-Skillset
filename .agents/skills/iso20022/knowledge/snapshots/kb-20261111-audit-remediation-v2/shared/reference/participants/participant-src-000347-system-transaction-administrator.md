---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000347-system-transaction-administrator"
title: "System Transaction Administrator"
source_labels: ["System Transaction Administrator"]
role_type: "source-scoped operational participant"
source_ids: ["src-000347"]
source_editions: ["december-2025"]
source_locations: [{"source_id": "src-000347", "locator": "P117; image7/P119; T10"}]
message_sets: ["t2s-billing"]
message_ids: ["camt.076.001.01", "camt.077.001.01"]
flows: ["flow-src-000347-p116-query-billing-information", "flow-src-000347-p129-positive-scenario", "flow-src-000347-p142-negative-scenario"]
aliases: []
limitations: ["No identifier scheme is assigned to this role in the cited passage. Contextual functional-role correspondences do not identify a particular institution."]
---







# System Transaction Administrator

The query activity participant identified with the executing party by P117.

## Responsibilities and relationships

Validates the request, checks permissions, searches billing data, extracts requested information and delivers cumulative or itemised data. Validation, permission or data-availability failure leads to error generation.

Source [src-000347](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v2.docx`; P117; image7/P119; T10.

Billing source context: [Query billing information activity](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0007.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p116-query-billing-information.md).

Billing source context: [Successful billing information query](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0009.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p129-positive-scenario.md).

Billing source context: [Rejected billing information query](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/diagrams/curated/fig-0010.md). [Reusable flow](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/flows/flow-src-000347-p142-negative-scenario.md).
