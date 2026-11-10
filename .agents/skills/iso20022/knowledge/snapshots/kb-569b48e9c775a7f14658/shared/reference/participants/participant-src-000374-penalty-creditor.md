---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000374-penalty-creditor"
title: "Penalty Creditor"
source_labels: ["Penalty Creditor"]
role_type: "functional penalty-creditor role"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
source_locations: [{"source_id": "src-000374", "locator": "T12 row2; P181/P277-P279; Word13/23/25-26"}]
message_sets: ["t2s-securities-and-penalty-reporting"]
message_ids: ["semt.025.001.01", "semt.026.001.01", "semt.027.001.01", "semt.040.001.01", "semt.044.001.01"]
flows: ["flow-src-000374-p224-query-report-process", "flow-src-000374-p243-securities-transaction-penalties-report"]
aliases: []
limitations: ["No identifier scheme or general institution equivalence is stated in this passage."]
---









# Penalty Creditor

Creditor is one of the reporting criteria for previously calculated cash penalties. The report can identify parties credited with penalties; this record is scoped to penalty reporting.

Source [src-000374](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`; T12 row2; P181/P277-P279; Word13/23/25-26.

Securities and penalty reporting source context: [Penalty reporting in settlement instruction context](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0003.md). [flow Securities Transaction Penalties Report](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p243-securities-transaction-penalties-report.md).

Securities and penalty reporting source context: [Scheduled cash-penalty reporting activity](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0012.md). [flow Securities Transaction Penalties Report](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p243-securities-transaction-penalties-report.md).

Securities and penalty reporting source context: [Reconciliation across status, penalty and settlement information](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0013.md). [flow Query Report Process](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p224-query-report-process.md).

Role category: functional penalty-creditor role. Definition is source-scoped; no institution-wide functional equivalence is implied.
