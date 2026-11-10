---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_sets: ["t2s-settlement-restrictions"]
participant_id: "participant-src-000380-central-securities-depositories-csd"
title: "Central Securities Depositories (CSD)"
source_labels: ["Central Securities Depositories (CSD)"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000380", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[3]", "paragraph_id": null, "table_id": "T6"}]
flows: []
process_sections: []
message_ids: ["semt.028.001.01", "semt.029.001.01", "semt.030.001.01", "semt.031.001.01", "semt.032.001.01", "semt.033.001.01", "semt.034.001.01"]
message_families: []
search_terms: ["Central Securities Depositories (CSD)"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000380-p101-settlement-condition-modification-request-query-and-report", "flow-src-000380-p111-transaction-cancellation-request-query-and-report", "flow-src-000380-p259-pull-mode", "flow-src-000380-p263-push-mode", "flow-src-000380-p268-pull-mode", "flow-src-000380-p272-push-mode", "flow-src-000380-p282-intra-position-movement-query-semt-028", "flow-src-000380-p285-intra-position-movement-query-response-semt-029", "flow-src-000380-p289-securities-settlement-conditions-modification-request-query-semt-030", "flow-src-000380-p293-securities-settlement-conditions-modification-request-report-semt-031", "flow-src-000380-p299-securities-transaction-cancellation-request-query-semt-032", "flow-src-000380-p304-securities-transaction-cancellation-request-report-semt-033", "flow-src-000380-p308-intra-position-movement-pending-report-semt-034", "flow-src-000380-p91-intra-position-movement-query-response-and-pending-report"]
---





























# Central Securities Depositories (CSD)

Business context: T2S SettlementRestrictions. Source classification: business role.

## Definition

An infrastructure that, holds or controls, the holding of physical or dematerialised financial instruments belonging to all, or a large portion of, the investors in a securities market. This affects the centralised transfer of ownership of such securities by entries on its books and records.

Evidence: [T6](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0006.md), source row 3.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Instructing Party](participant-src-000380-instructing-party.md) | [T7](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/documents/src-000380/tables/tbl-0007.md) row 3, column 2 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Central Securities Depositories (CSD)`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000380](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`.








<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.028-START -->
[semt.028.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.028.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.028-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.029-START -->
[semt.029.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.029.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.029-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.030-START -->
[semt.030.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.030.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.030-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.031-START -->
[semt.031.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.031.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.031-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.032-START -->
[semt.032.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.032.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.032-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.033-START -->
[semt.033.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.033.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.033-END -->

<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.034-START -->
[semt.034.001.01 — role involvement and message direction](../../../domains/securities/reference/messages/semt.034.001.01/business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-MESSAGE-semt.034-END -->
