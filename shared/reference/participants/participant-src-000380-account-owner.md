---
template: false
document_kind: "participant"
review_status: "needs-review"
participant_id: "participant-src-000380-account-owner"
title: "Account Owner"
source_labels: ["Account Owner"]
aliases: []
source_ids: ["src-000380"]
source_editions: ["september-2025"]
domain: "securities"
message_sets: ["t2s-settlement-restrictions"]
role_type: "source-scoped functional label or system endpoint"
source_locations: [{"source_id": "src-000380", "locator": "P153/P181/P209/P223–P224"}]
limitations: ["No identifier scheme is established by the cited role evidence.", "A data-party label is not automatically a transmitting or receiving participant."]
updated: "2026-11-09"
message_ids: ["semt.029.001.01", "semt.031.001.01", "semt.033.001.01", "semt.034.001.01"]
flow_ids: ["flow-src-000380-p101-settlement-condition-modification-request-query-and-report", "flow-src-000380-p111-transaction-cancellation-request-query-and-report", "flow-src-000380-p259-pull-mode", "flow-src-000380-p263-push-mode", "flow-src-000380-p268-pull-mode", "flow-src-000380-p272-push-mode", "flow-src-000380-p285-intra-position-movement-query-response-semt-029", "flow-src-000380-p293-securities-settlement-conditions-modification-request-report-semt-031", "flow-src-000380-p304-securities-transaction-cancellation-request-report-semt-033", "flow-src-000380-p308-intra-position-movement-pending-report-semt-034", "flow-src-000380-p91-intra-position-movement-query-response-and-pending-report"]
---

# Account Owner

Party that owns the account to or from which an entry is made in the pending report (P224). Other report rules distinguish a report-level Account Owner from the owner nested under an individual movement, modification or cancellation. Presence in data is not proof of sender/receiver responsibility.

[src-000380](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`; P153/P181/P209/P223–P224.





<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.029-START -->
[semt.029.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.029.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.029-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.031-START -->
[semt.031.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.031.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.031-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.033-START -->
[semt.033.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.033.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.033-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.034-START -->
[semt.034.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.034.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.034-END -->
