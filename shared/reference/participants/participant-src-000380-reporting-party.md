---
template: false
document_kind: "participant"
review_status: "needs-review"
participant_id: "participant-src-000380-reporting-party"
title: "Reporting Party"
source_labels: ["Reporting Party"]
aliases: []
source_ids: ["src-000380"]
source_editions: ["september-2025"]
domain: "securities"
message_sets: ["t2s-settlement-restrictions"]
role_type: "source-scoped functional label or system endpoint"
source_locations: [{"source_id": "src-000380", "locator": "P198/P307"}]
limitations: ["No identifier scheme is established by the cited role evidence.", "A data-party label is not automatically a transmitting or receiving participant."]
updated: "2026-11-09"
message_ids: ["semt.033.001.01"]
flow_ids: ["flow-src-000380-p111-transaction-cancellation-request-query-and-report", "flow-src-000380-p268-pull-mode", "flow-src-000380-p272-push-mode", "flow-src-000380-p304-securities-transaction-cancellation-request-report-semt-033"]
---

# Reporting Party

P198 and P307 scope the configured cancellation report to Securities Accounts under the Reporting Party’s scope. These sentences do not define a separate institution or establish a global alias for T2S.

[src-000380](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`; P198/P307.

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.033-START -->
[semt.033.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.033.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.033-END -->
