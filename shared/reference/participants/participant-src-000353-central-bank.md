---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000353-central-bank"
title: "CBs (source label)"
source_labels: ["CBs"]
role_type: "source-scoped functional participant"
source_ids: ["src-000353"]
source_editions: ["may-2025"]
source_locations: [{"source_id": "src-000353", "locator": "P74-P79; T2 abbreviations"}]
message_sets: ["t2s-collateral-management-reference-data"]
message_ids: ["reda.024.001.01", "reda.025.001.01", "reda.027.001.01", "reda.075.001.01", "reda.077.001.01"]
flows: ["flow-src-000353-p104-collateral-reference-data-creation", "flow-src-000353-p105-collateral-reference-data-deletion"]
aliases: []
limitations: ["No identifier scheme or general institution equivalence is stated in this passage.", "The source uses CBs in these passages; T2 separately expands NCB but does not explicitly expand CBs. No equivalence with National Central Bank is asserted."]
---





# CBs (source label)

P74-P79 names CBs as senders of collateral-value creation, eligible-securities creation/deletion and close-link creation/deletion. This scope is retained separately from the specifically defined National Central Bank business role.

Source [src-000353](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralManagementReferenceData_v2.docx`; P74-P79; P74-P79 (CBs label; T2 only separately defines NCB).

Explicit originating-message applicability (P74/P75/P77-P79): [reda.024.001.01](../../../domains/securities/reference/messages/reda.024.001.01/index.md), [reda.025.001.01](../../../domains/securities/reference/messages/reda.025.001.01/index.md), [reda.027.001.01](../../../domains/securities/reference/messages/reda.027.001.01/index.md), [reda.075.001.01](../../../domains/securities/reference/messages/reda.075.001.01/index.md), [reda.077.001.01](../../../domains/securities/reference/messages/reda.077.001.01/index.md).
