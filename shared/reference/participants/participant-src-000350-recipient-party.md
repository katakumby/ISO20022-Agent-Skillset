---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000350-recipient-party"
title: "Recipient Party"
source_labels: ["Recipient Party"]
role_type: "source-scoped functional participant"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
source_locations: [{"source_id": "src-000350", "locator": "T10 rows2-5; P95/P164; image8/P137 and image10/P162"}]
message_sets: ["t2s-cash-account-query-and-report"]
message_ids: ["acmt.025.001.02", "acmt.026.001.02", "reda.038.001.01", "reda.039.001.01", "reda.040.001.01"]
flows: ["flow-src-000350-p123-account-query-list", "flow-src-000350-p124-cash-account-audit-trail-query", "flow-src-000350-p125-cash-account-activity-advice", "flow-src-000350-p135-cash-account-activity-advice-process", "flow-src-000350-p161-cash-account-activity-advice-process"]
aliases: []
limitations: ["No identifier scheme or general institution equivalence is stated in this passage."]
---







# Recipient Party

T10 names this functional recipient of the automatically generated Cash Account Activity Advice. A standing instruction must be in place at the Executing/Servicing Party. The activity and sequence use Instructing Party for the receiving lane; the two contextual labels are linked without assuming equivalence outside this flow.

Source [src-000350](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart1_Target2Securities_CashAccountQueryAndReport_v2.docx`; T10 rows2-5; P95/P164; image8/P137 and image10/P162.

Cash-account source context: [Cash account query, report and advice overview](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/diagrams/curated/fig-0002.md). [flow Account Query List](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p123-account-query-list.md), [flow Cash Account Audit Trail Query](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p124-cash-account-audit-trail-query.md), [flow Cash Account Activity Advice](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p125-cash-account-activity-advice.md).

Cash-account source context: [Cash account activity advice activity](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/diagrams/curated/fig-0008.md). [flow Cash Account Activity Advice process](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p135-cash-account-activity-advice-process.md).

Cash-account source context: [Cash account activity advice push sequence](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/diagrams/curated/fig-0011.md). [flow Cash Account Activity Advice Process](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/flows/flow-src-000350-p161-cash-account-activity-advice-process.md).
