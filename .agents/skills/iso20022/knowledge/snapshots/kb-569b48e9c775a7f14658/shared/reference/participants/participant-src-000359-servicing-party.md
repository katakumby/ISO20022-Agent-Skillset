---
template: false
document_kind: "participant"
review_status: "needs-review"
participant_id: "participant-src-000359-servicing-party"
title: "Servicing Party"
source_labels: ["Servicing Party"]
aliases: []
source_ids: ["src-000359"]
source_editions: ["march-2024"]
domain: "securities"
message_sets: ["t2s-intra-balance-movement"]
role_type: "source-scoped actor label; no broader equivalence asserted"
source_locations: [{"source_id": "src-000359", "paragraph_id": "P258", "heading_path": ["BusinessTransactions", "Intra-Balance Movement Modification/Cancellation Query and Report Process", "Requesting an Intra Balance Cancellation Query"]}]
limitations: ["Identifier schemes are not specified in the cited role evidence. Institutional examples and functional roles are not equated."]
updated: "2026-11-09"
flow_ids: ["flow-src-000359-p200-push-mode", "flow-src-000359-p204-pull-mode", "flow-src-000359-p256-requesting-an-intra-balance-cancellation-query", "flow-src-000359-p269-requesting-an-intra-balance-modification-query", "flow-src-000359-p282-producing-an-intra-balance-modification-cancellation-report-at-a-busin"]
---











# Servicing Party

The source transaction and query/report activity label for the party receiving cancellation/modification queries and sending reports or request status to the Instructing Party. Source label variants Servicing/Executing Party and Executing/Servicing Party are retained as separate records; no global equivalence is inferred.

[src-000359](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`; src-000359 P258.

## Responsibilities and relationships

The linked flows below retain the source-specific actions and counterparties. No identifier scheme or unprinted alias is inferred.

<!-- INTRABALANCE-FIG-13-START -->
[Push modification and cancellation reporting activity](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p200-push-mode.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0013.md)
<!-- INTRABALANCE-FIG-13-END -->

<!-- INTRABALANCE-FIG-14-START -->
[Pull modification and cancellation reporting activity](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p204-pull-mode.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0014.md)
<!-- INTRABALANCE-FIG-14-END -->

<!-- INTRABALANCE-FIG-20-START -->
[Cancellation query and report exchange](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p256-requesting-an-intra-balance-cancellation-query.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0020.md)
<!-- INTRABALANCE-FIG-20-END -->

<!-- INTRABALANCE-FIG-21-START -->
[Modification query and report exchange](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p269-requesting-an-intra-balance-modification-query.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0021.md)
<!-- INTRABALANCE-FIG-21-END -->

<!-- INTRABALANCE-FIG-22-START -->
[Event-triggered cancellation and modification reporting](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p282-producing-an-intra-balance-modification-cancellation-report-at-a-busin.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0022.md)
<!-- INTRABALANCE-FIG-22-END -->
