---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000374-t2s-actor"
title: "T2S Actor"
source_labels: ["T2S Actor"]
role_type: "source contextual actor umbrella"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
source_locations: [{"source_id": "src-000374", "locator": "P56/P158-P164/P277-P279; Word6/12/25-26"}]
message_sets: ["t2s-securities-and-penalty-reporting"]
message_ids: ["semt.025.001.01", "semt.040.001.01", "semt.044.001.01"]
flows: ["flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp", "flow-src-000374-p243-securities-transaction-penalties-report"]
aliases: []
limitations: ["No identifier scheme or general institution equivalence is stated in this passage."]
---











# T2S Actor

Contextual platform actor addressed by position queries and penalties reports. For penalties, P277 specifies CSDs or CSD participants, with data scope and External CSD treatment in P278-P279. The label remains broader than any one institution type.

Source [src-000374](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`; P56/P158-P164/P277-P279; Word6/12/25-26.

Securities and penalty reporting source context: [Securities account position query and response exchange](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0001.md). [flow Securities Account Position Query and Securities Account Position Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md).

Securities and penalty reporting source context: [Penalty reporting in settlement instruction context](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0003.md). [flow Securities Transaction Penalties Report](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p243-securities-transaction-penalties-report.md).

Securities and penalty reporting source context: [Securities position query activity with access and error decisions](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0010.md). [flow Securities Account Position Query and Securities Account Position Response](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p232-securities-account-position-query-and-securities-account-position-resp.md).

Securities and penalty reporting source context: [Scheduled cash-penalty reporting activity](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/diagrams/curated/fig-0012.md). [flow Securities Transaction Penalties Report](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/flows/flow-src-000374-p243-securities-transaction-penalties-report.md).

Role category: source contextual actor umbrella. Definition is source-scoped; no institution-wide functional equivalence is implied.
