---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
participant_id: "participant-src-000095-distributor"
title: "Distributor"
source_labels: ["Distributor"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000095", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[19]/w:tr[8]", "paragraph_id": null, "table_id": "T19"}]
flows: []
process_sections: ["flow-src-000095-p348-fund-reference-data-reporting", "flow-src-000095-p360-order-and-confirmation", "flow-src-000095-p415-order-instruction-status-reporting", "flow-src-000095-p504-order-cancellation-and-status", "flow-src-000095-p592-order-confirmation-status-reporting", "flow-src-000095-p612-order-confirmation-amendment", "flow-src-000095-p670-order-confirmation-cancellation", "flow-src-000095-p726-order-confirmation-status-request"]
message_ids: []
message_families: ["reda.004", "setr.016", "setr.017", "setr.057", "setr.058"]
search_terms: ["Distributor", "reda.004", "setr.016", "setr.017", "setr.057", "setr.058"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000095-p351-fund-reference-data-report-solicited-requested", "flow-src-000095-p356-fund-reference-data-report-unsolicited", "flow-src-000095-p368-direct", "flow-src-000095-p374-intermediary", "flow-src-000095-p381-bulk", "flow-src-000095-p388-direct", "flow-src-000095-p394-intermediary", "flow-src-000095-p400-bulk", "flow-src-000095-p407-direct", "flow-src-000095-p411-intermediary", "flow-src-000095-p425-direct", "flow-src-000095-p429-intermediary", "flow-src-000095-p436-bulk", "flow-src-000095-p445-direct", "flow-src-000095-p449-intermediary", "flow-src-000095-p456-bulk", "flow-src-000095-p465-direct", "flow-src-000095-p469-intermediary", "flow-src-000095-p476-request-status-of-subscription", "flow-src-000095-p481-request-status-of-redemption", "flow-src-000095-p486-request-status-of-switch", "flow-src-000095-p515-request-and-status-direct", "flow-src-000095-p519-request-and-status-intermediary", "flow-src-000095-p524-request-and-status-bulk"]
---





















































# Distributor

Business context: Investment Funds. Source classification: business role.

## Definition

Party that act as a wholesaler of funds.

Evidence: [T19](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0019.md), source row 8.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Instructing Party](participant-src-000095-instructing-party.md) | [T20](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0020.md) row 9, column 2 |
| Can play the functional participant role in this source context | [Intermediary](participant-src-000095-intermediary.md) | [T20](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0020.md) row 9, column 3 |
| Can play the functional participant role in this source context | [Executing Party](participant-src-000095-executing-party.md) | [T20](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0020.md) row 9, column 4 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Fund Reference Data Reporting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p348-fund-reference-data-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order and Confirmation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p360-order-and-confirmation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Instruction Status Reporting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p415-order-instruction-status-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Cancellation and Status](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p504-order-cancellation-and-status.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Confirmation Status Reporting](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p592-order-confirmation-status-reporting.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Confirmation Amendment](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p612-order-confirmation-amendment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Confirmation Cancellation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p670-order-confirmation-cancellation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Order Confirmation Status Request](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p726-order-confirmation-status-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `reda.004`, `setr.016`, `setr.017`, `setr.057`, `setr.058`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Distributor`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000095](../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md).

<!-- FUNDS-CURATED-FLOW-0075-START -->
[Redemption cancellation — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p534-request-and-status-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0075.md)
<!-- FUNDS-CURATED-FLOW-0075-END -->

<!-- FUNDS-CURATED-FLOW-0076-START -->
[Redemption cancellation — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p539-request-and-status-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0076.md)
<!-- FUNDS-CURATED-FLOW-0076-END -->

<!-- FUNDS-CURATED-FLOW-0077-START -->
[Redemption cancellation — bulk and reinstruction](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p544-request-and-status-bulk.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0077.md)
<!-- FUNDS-CURATED-FLOW-0077-END -->

<!-- FUNDS-CURATED-FLOW-0078-START -->
[Switch cancellation — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p554-request-and-status-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0078.md)
<!-- FUNDS-CURATED-FLOW-0078-END -->

<!-- FUNDS-CURATED-FLOW-0079-START -->
[Switch cancellation — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p558-request-and-status-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0079.md)
<!-- FUNDS-CURATED-FLOW-0079-END -->

<!-- FUNDS-CURATED-FLOW-0084-START -->
[Subscription confirmation rejected by instructing party](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p597-subscription.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0084.md)
<!-- FUNDS-CURATED-FLOW-0084-END -->

<!-- FUNDS-CURATED-FLOW-0085-START -->
[Redemption confirmation rejected by instructing party](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p602-redemption.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0085.md)
<!-- FUNDS-CURATED-FLOW-0085-END -->

<!-- FUNDS-CURATED-FLOW-0086-START -->
[Switch confirmation rejected by instructing party](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p607-switch.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0086.md)
<!-- FUNDS-CURATED-FLOW-0086-END -->

<!-- FUNDS-CURATED-FLOW-0087-START -->
[Subscription confirmation amendment — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p619-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0087.md)
<!-- FUNDS-CURATED-FLOW-0087-END -->

<!-- FUNDS-CURATED-FLOW-0088-START -->
[Subscription confirmation amendment — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p624-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0088.md)
<!-- FUNDS-CURATED-FLOW-0088-END -->

<!-- FUNDS-CURATED-FLOW-0089-START -->
[Subscription confirmation amendment — bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p630-bulk.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0089.md)
<!-- FUNDS-CURATED-FLOW-0089-END -->

<!-- FUNDS-CURATED-FLOW-0090-START -->
[Redemption confirmation amendment — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p639-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0090.md)
<!-- FUNDS-CURATED-FLOW-0090-END -->

<!-- FUNDS-CURATED-FLOW-0091-START -->
[Redemption confirmation amendment — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p644-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0091.md)
<!-- FUNDS-CURATED-FLOW-0091-END -->

<!-- FUNDS-CURATED-FLOW-0092-START -->
[Redemption confirmation amendment — bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p650-bulk.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0092.md)
<!-- FUNDS-CURATED-FLOW-0092-END -->

<!-- FUNDS-CURATED-FLOW-0093-START -->
[Switch confirmation amendment — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p659-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0093.md)
<!-- FUNDS-CURATED-FLOW-0093-END -->

<!-- FUNDS-CURATED-FLOW-0094-START -->
[Switch confirmation amendment — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p664-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0094.md)
<!-- FUNDS-CURATED-FLOW-0094-END -->

<!-- FUNDS-CURATED-FLOW-0095-START -->
[Subscription confirmation cancellation — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p677-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0095.md)
<!-- FUNDS-CURATED-FLOW-0095-END -->

<!-- FUNDS-CURATED-FLOW-0096-START -->
[Subscription confirmation cancellation — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p682-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0096.md)
<!-- FUNDS-CURATED-FLOW-0096-END -->

<!-- FUNDS-CURATED-FLOW-0097-START -->
[Subscription confirmation cancellation — bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p687-bulk.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0097.md)
<!-- FUNDS-CURATED-FLOW-0097-END -->

<!-- FUNDS-CURATED-FLOW-0098-START -->
[Redemption confirmation cancellation — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p696-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0098.md)
<!-- FUNDS-CURATED-FLOW-0098-END -->

<!-- FUNDS-CURATED-FLOW-0099-START -->
[Redemption confirmation cancellation — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p701-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0099.md)
<!-- FUNDS-CURATED-FLOW-0099-END -->

<!-- FUNDS-CURATED-FLOW-0100-START -->
[Redemption confirmation cancellation — bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p707-bulk.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0100.md)
<!-- FUNDS-CURATED-FLOW-0100-END -->

<!-- FUNDS-CURATED-FLOW-0101-START -->
[Switch confirmation cancellation — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p716-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0101.md)
<!-- FUNDS-CURATED-FLOW-0101-END -->

<!-- FUNDS-CURATED-FLOW-0102-START -->
[Switch confirmation cancellation — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p720-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0102.md)
<!-- FUNDS-CURATED-FLOW-0102-END -->

<!-- FUNDS-CURATED-FLOW-0103-START -->
[Subscription amended-confirmation status query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p731-subscription.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0103.md)
<!-- FUNDS-CURATED-FLOW-0103-END -->

<!-- FUNDS-CURATED-FLOW-0104-START -->
[Redemption amended-confirmation status query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p738-redemption.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0104.md)
<!-- FUNDS-CURATED-FLOW-0104-END -->

<!-- FUNDS-CURATED-FLOW-0105-START -->
[Switch amended-confirmation status query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p745-switch.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0105.md)
<!-- FUNDS-CURATED-FLOW-0105-END -->

<!-- FUNDS-PROCESS-fig-0001 -->
[Investment Funds communication scope](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0001.md)
<!-- /FUNDS-PROCESS-fig-0001 -->

<!-- FUNDS-PROCESS-fig-0002 -->
[Business roles and functional participants](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0002.md)
<!-- /FUNDS-PROCESS-fig-0002 -->

<!-- FUNDS-EARLY-FLOW-356 -->
[Fund Reference Data Reporting / Fund Reference Data Report – Unsolicited](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p356-fund-reference-data-report-unsolicited.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-356 -->

<!-- FUNDS-EARLY-FLOW-351 -->
[Fund Reference Data Reporting / Fund Reference Data Report – Solicited (requested)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p351-fund-reference-data-report-solicited-requested.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-351 -->

<!-- FUNDS-EARLY-FLOW-368 -->
[Order and Confirmation / Subscription  / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p368-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-368 -->

<!-- FUNDS-EARLY-FLOW-374 -->
[Order and Confirmation / Subscription  / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p374-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-374 -->

<!-- FUNDS-EARLY-FLOW-381 -->
[Order and Confirmation / Subscription  / Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p381-bulk.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-381 -->

<!-- FUNDS-EARLY-FLOW-388 -->
[Order and Confirmation / Redemption / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p388-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-388 -->

<!-- FUNDS-EARLY-FLOW-394 -->
[Order and Confirmation / Redemption / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p394-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-394 -->

<!-- FUNDS-EARLY-FLOW-400 -->
[Order and Confirmation / Redemption / Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p400-bulk.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-400 -->

<!-- FUNDS-EARLY-FLOW-407 -->
[Order and Confirmation / Switch  / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p407-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-407 -->

<!-- FUNDS-EARLY-FLOW-411 -->
[Order and Confirmation / Switch  / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p411-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-411 -->

<!-- FUNDS-EARLY-FLOW-425 -->
[Order Instruction Status Reporting / Subscription / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p425-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-425 -->

<!-- FUNDS-EARLY-FLOW-445 -->
[Order Instruction Status Reporting / Redemption / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p445-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-445 -->

<!-- FUNDS-EARLY-FLOW-465 -->
[Order Instruction Status Reporting / Switch / Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p465-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-465 -->

<!-- FUNDS-EARLY-FLOW-429 -->
[Order Instruction Status Reporting / Subscription / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p429-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-429 -->

<!-- FUNDS-EARLY-FLOW-449 -->
[Order Instruction Status Reporting / Redemption / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p449-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-449 -->

<!-- FUNDS-EARLY-FLOW-469 -->
[Order Instruction Status Reporting / Switch / Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p469-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-469 -->

<!-- FUNDS-EARLY-FLOW-436 -->
[Order Instruction Status Reporting / Subscription / Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p436-bulk.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-436 -->

<!-- FUNDS-EARLY-FLOW-456 -->
[Order Instruction Status Reporting / Redemption / Bulk](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p456-bulk.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-456 -->

<!-- FUNDS-EARLY-FLOW-476 -->
[Order Instruction Status Reporting / Order Instruction Status Request / Request Status of Subscription ](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p476-request-status-of-subscription.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-476 -->

<!-- FUNDS-EARLY-FLOW-481 -->
[Order Instruction Status Reporting / Order Instruction Status Request / Request Status of Redemption ](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p481-request-status-of-redemption.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-481 -->

<!-- FUNDS-EARLY-FLOW-486 -->
[Order Instruction Status Reporting / Order Instruction Status Request / Request Status of Switch](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p486-request-status-of-switch.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-486 -->

<!-- FUNDS-EARLY-FLOW-515 -->
[Order Cancellation and Status  / Subscription  / Request and Status - Direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p515-request-and-status-direct.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-515 -->

<!-- FUNDS-EARLY-FLOW-519 -->
[Order Cancellation and Status  / Subscription  / Request and Status - Intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p519-request-and-status-intermediary.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-519 -->

<!-- FUNDS-EARLY-FLOW-524 -->
[Order Cancellation and Status  / Subscription  / Request and Status - Bulk ](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p524-request-and-status-bulk.md) — narrative participant example; not drawn separately.
<!-- /FUNDS-EARLY-FLOW-524 -->
