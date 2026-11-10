---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "payments"
domains: ["payments"]
participant_id: "participant-src-000004-final-agent"
title: "Final Agent"
source_labels: ["Final Agent"]
role_type: "functional participant role"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
source_locations: [{"source_id": "src-000004", "locator": "P110; Word12"}]
message_sets: ["bank-to-customer-cash-management"]
message_ids: []
flows: ["flow-src-000004-p101-report", "flow-src-000004-p104-reconcile", "flow-src-000004-p107-report-on-payment-transaction", "flow-src-000004-p109-report-on-payment-transaction-status"]
aliases: []
limitations: ["No identifier scheme or general institution equivalence is stated in this passage."]
---





# Final Agent

The final agent registers the payment in the creditor account; the source describes conveying that status through preceding agents or investigation from the first/forwarding agent.

Source [src-000004](../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart1_BankToCustomerCashManagement_2025_2026_v2.docx); P110; Word12.

Bank-to-customer source context: [Reporting business-process actor overview](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/diagrams/curated/fig-0002.md). [flow Report](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p101-report.md), [flow Reconcile](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p104-reconcile.md), [flow Report on Payment Transaction](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p107-report-on-payment-transaction.md), [flow Report on Payment Transaction Status](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/flows/flow-src-000004-p109-report-on-payment-transaction-status.md).
