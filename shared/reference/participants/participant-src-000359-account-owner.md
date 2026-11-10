---
template: false
document_kind: "participant"
review_status: "needs-review"
participant_id: "participant-src-000359-account-owner"
title: "Account owner"
source_labels: ["Account owner"]
aliases: []
source_ids: ["src-000359"]
source_editions: ["march-2024"]
domain: "securities"
message_sets: ["t2s-intra-balance-movement"]
role_type: "source-scoped actor label; no broader equivalence asserted"
source_locations: [{"source_id": "src-000359", "paragraph_id": "P159", "heading_path": ["BusinessProcess Description", "Intra-Balance Management"]}]
limitations: ["Identifier schemes are not specified in the cited role evidence. Institutional examples and functional roles are not equated."]
updated: "2026-11-09"
flow_ids: ["flow-src-000359-p151-intra-balance-management", "flow-src-000359-p189-external-scenario", "flow-src-000359-p193-internal-scenario", "flow-src-000359-p197-intra-balance-movement-modification-cancellation-process", "flow-src-000359-p200-push-mode", "flow-src-000359-p204-pull-mode", "flow-src-000359-p208-intra-balance-movement-pending-posting-report-process", "flow-src-000359-p219-in-external-scenario", "flow-src-000359-p230-in-internal-scenario", "flow-src-000359-p238-modification-and-cancellation-process", "flow-src-000359-p256-requesting-an-intra-balance-cancellation-query", "flow-src-000359-p269-requesting-an-intra-balance-modification-query", "flow-src-000359-p282-producing-an-intra-balance-modification-cancellation-report-at-a-busin", "flow-src-000359-p298-intra-balance-movement-pending-posting-report-process"]
---





























# Account owner

Contextual role in T9/T10/T13/T16 receiving status/confirmation or requesting query, explicitly parenthesized Instructing Party there; T17/T18 instead parenthesize Receiving Party. This is a relationship role, not a particular institution.

[src-000359](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`; src-000359 P159.

## Responsibilities and relationships

The linked flows below retain the source-specific actions and counterparties. No identifier scheme or unprinted alias is inferred.

<!-- INTRABALANCE-FIG-2-START -->
[Intra-balance management in its business context](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p151-intra-balance-management.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0002.md)
<!-- INTRABALANCE-FIG-2-END -->

<!-- INTRABALANCE-FIG-10-START -->
[External intra-balance movement activity](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p189-external-scenario.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0010.md)
<!-- INTRABALANCE-FIG-10-END -->

<!-- INTRABALANCE-FIG-11-START -->
[Internal intra-balance movement activity](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p193-internal-scenario.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0011.md)
<!-- INTRABALANCE-FIG-11-END -->

<!-- INTRABALANCE-FIG-12-START -->
[Modification and cancellation activity](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p197-intra-balance-movement-modification-cancellation-process.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0012.md)
<!-- INTRABALANCE-FIG-12-END -->

<!-- INTRABALANCE-FIG-13-START -->
[Push modification and cancellation reporting activity](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p200-push-mode.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0013.md)
<!-- INTRABALANCE-FIG-13-END -->

<!-- INTRABALANCE-FIG-14-START -->
[Pull modification and cancellation reporting activity](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p204-pull-mode.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0014.md)
<!-- INTRABALANCE-FIG-14-END -->

<!-- INTRABALANCE-FIG-15-START -->
[Pending and posting reporting activity](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p208-intra-balance-movement-pending-posting-report-process.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0015.md)
<!-- INTRABALANCE-FIG-15-END -->

<!-- INTRABALANCE-FIG-17-START -->
[External cash settlement restriction creation](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p219-in-external-scenario.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0017.md)
<!-- INTRABALANCE-FIG-17-END -->

<!-- INTRABALANCE-FIG-18-START -->
[Internal cash settlement restriction creation](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p230-in-internal-scenario.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0018.md)
<!-- INTRABALANCE-FIG-18-END -->

<!-- INTRABALANCE-FIG-19-START -->
[Modification and cancellation transaction exchange](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p238-modification-and-cancellation-process.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0019.md)
<!-- INTRABALANCE-FIG-19-END -->

<!-- INTRABALANCE-FIG-20-START -->
[Cancellation query and report exchange](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p256-requesting-an-intra-balance-cancellation-query.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0020.md)
<!-- INTRABALANCE-FIG-20-END -->

<!-- INTRABALANCE-FIG-21-START -->
[Modification query and report exchange](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p269-requesting-an-intra-balance-modification-query.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0021.md)
<!-- INTRABALANCE-FIG-21-END -->

<!-- INTRABALANCE-FIG-22-START -->
[Event-triggered cancellation and modification reporting](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p282-producing-an-intra-balance-modification-cancellation-report-at-a-busin.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0022.md)
<!-- INTRABALANCE-FIG-22-END -->

<!-- INTRABALANCE-FIG-23-START -->
[Pending and posting report exchange](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p298-intra-balance-movement-pending-posting-report-process.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0023.md)
<!-- INTRABALANCE-FIG-23-END -->
