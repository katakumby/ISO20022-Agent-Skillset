---
template: false
document_kind: "participant"
manual_curated: true
review_status: "needs-review"
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000353-party-authorised-by-central-bank-or-payment-bank"
title: "Party authorised by CBs or payment banks"
source_labels: ["any party authorised by them"]
role_type: "source-scoped functional participant"
source_ids: ["src-000353"]
source_editions: ["may-2025"]
source_locations: [{"source_id": "src-000353", "locator": "P75/P78"}]
message_sets: ["t2s-collateral-management-reference-data"]
message_ids: ["reda.025.001.01", "reda.075.001.01"]
flows: ["flow-src-000353-p104-collateral-reference-data-creation", "flow-src-000353-p105-collateral-reference-data-deletion"]
aliases: []
limitations: ["No identifier scheme or general institution equivalence is stated in this passage.", "The source uses CBs in these passages; T2 separately expands NCB but does not explicitly expand CBs. No equivalence with National Central Bank is asserted."]
---





# Party authorised by CBs or payment banks

A delegated actor expressly permitted in P75/P78 to send eligible-securities creation or deletion requests. Authorisation by a CB/payment-bank is the source relationship; no particular institution is identified.

Source [src-000353](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralManagementReferenceData_v2.docx`; P75/P78.

Explicit originating-message applicability (P75/P78): [reda.025.001.01](../../../domains/securities/reference/messages/reda.025.001.01/index.md), [reda.075.001.01](../../../domains/securities/reference/messages/reda.075.001.01/index.md).
