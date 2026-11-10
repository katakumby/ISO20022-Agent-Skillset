---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000374-account-owner"
title: "Account Owner"
source_labels: ["Account Owner"]
role_type: "functional participant role"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
source_locations: [{"source_id": "src-000374", "locator": "P171-P174/P258; Word12/25"}]
message_sets: ["t2s-securities-and-penalty-reporting"]
message_ids: ["semt.025.001.01", "semt.026.001.01", "semt.027.001.01", "semt.040.001.01", "semt.044.001.01"]
flows: ["flow-src-000374-p224-query-report-process", "flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp"]
aliases: []
limitations: ["No identifier scheme or general institution equivalence is stated in this passage."]
---









# Account Owner

Party who owns the securities account identified in the optional AccountOwner block of the Securities Account Position Response. P258 also permits account owner as a history-query search criterion. Account ownership is a functional relationship and is not equated with the query sender in every flow.

Source [src-000374](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`; P171-P174/P258; Word12/25.

Securities and penalty reporting source context: [Securities account position query and response exchange](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0001.md). [flow Securities Account Position Query and Securities Account Position Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md).

Securities and penalty reporting source context: [Securities position query activity with access and error decisions](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0010.md). [flow Securities Account Position Query and Securities Account Position Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md).

Securities and penalty reporting source context: [Reconciliation across status, penalty and settlement information](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0013.md). [flow Query Report Process](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p224-query-report-process.md).

Role category: functional participant role. Definition is source-scoped; no institution-wide functional equivalence is implied.
