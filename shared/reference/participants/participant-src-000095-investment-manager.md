---
template: false
document_kind: "participant"
review_status: "reviewed"
manual_curated: true
domain: "shared"
domains: ["securities"]
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
participant_id: "participant-src-000095-investment-manager"
title: "Investment manager"
source_labels: ["Investment manager"]
role_type: "Institutional source example"
aliases: []
source_locations: [{"source_id": "src-000095", "locator": "P109 figure1"}, {"source_id": "src-000095", "locator": "P109 figure1"}]
flow_ids: ["flow-src-000095-p368-direct", "flow-src-000095-p374-intermediary", "flow-src-000095-p381-bulk", "flow-src-000095-p388-direct", "flow-src-000095-p394-intermediary", "flow-src-000095-p400-bulk", "flow-src-000095-p407-direct", "flow-src-000095-p411-intermediary", "flow-src-000095-p425-direct", "flow-src-000095-p429-intermediary", "flow-src-000095-p436-bulk", "flow-src-000095-p445-direct", "flow-src-000095-p449-intermediary", "flow-src-000095-p456-bulk", "flow-src-000095-p465-direct", "flow-src-000095-p469-intermediary", "flow-src-000095-p476-request-status-of-subscription", "flow-src-000095-p481-request-status-of-redemption", "flow-src-000095-p486-request-status-of-switch", "flow-src-000095-p515-request-and-status-direct", "flow-src-000095-p519-request-and-status-intermediary", "flow-src-000095-p524-request-and-status-bulk"]
message_ids: []
limitations: ["Scoped to the supplied Investment Funds source; same-name roles in other publications are not merged.", "No identifier scheme is specified in the cited evidence."]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative/table/figure labels inspected; no independent institutional equivalence inferred."}
---















































# Investment manager

[src-000095](../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx)

## Definition and context

Participant named Investment manager in the communication-scope figure. This label is not automatically equated to the separately defined Fund Manager. (P109 figure1)

Source classification: Institutional source example. A functional role varies with the relationship; institutional examples do not fix the role for every process.

## Responsibilities and actions

Receives FundCashForecast from the Transfer Agent/Fund Administrator endpoint. (P109 figure1)

## Relationships

- [fund administrator](participant-src-000095-fund-administrator.md)
- [transfer agent](participant-src-000095-transfer-agent.md)

## Flows and messages



Message names in the cited source identify business exchanges; exact definitions are resolved through the message-set index.

## Identification and limitations

- Scoped to the supplied Investment Funds source; same-name roles in other publications are not merged.
- No identifier scheme is specified in the cited evidence.

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

<!-- FUNDS-CURATED-FLOW-0114-START -->
[Own-account asset transfer — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p811-own-account-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0114.md)
<!-- FUNDS-CURATED-FLOW-0114-END -->

<!-- FUNDS-CURATED-FLOW-0115-START -->
[Two-owner asset transfer — direct double leg](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p816-two-account-owners-direct-double-leg.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0115.md)
<!-- FUNDS-CURATED-FLOW-0115-END -->

<!-- FUNDS-CURATED-FLOW-0116-START -->
[Two-owner asset transfer — direct single leg](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p822-two-account-owners-direct-single-leg.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0116.md)
<!-- FUNDS-CURATED-FLOW-0116-END -->

<!-- FUNDS-CURATED-FLOW-0117-START -->
[Two-owner asset transfer — SLT market practice](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p828-two-account-owners-direct-slt-market-practice.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0117.md)
<!-- FUNDS-CURATED-FLOW-0117-END -->

<!-- FUNDS-CURATED-FLOW-0118-START -->
[Two-owner asset transfer — intermediary double leg](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p837-two-account-owners-intermediary-double-leg.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0118.md)
<!-- FUNDS-CURATED-FLOW-0118-END -->

<!-- FUNDS-CURATED-FLOW-0119-START -->
[Transfer-out confirmation reversal](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p843-transfer-out-reversal.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0119.md)
<!-- FUNDS-CURATED-FLOW-0119-END -->

<!-- FUNDS-CURATED-FLOW-0120-START -->
[Transfer-in confirmation reversal](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p848-transfer-in-reversal.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0120.md)
<!-- FUNDS-CURATED-FLOW-0120-END -->

<!-- FUNDS-CURATED-FLOW-0121-START -->
[Transfer-out instruction cancellation request](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p853-transfer-out-cancellation.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0121.md)
<!-- FUNDS-CURATED-FLOW-0121-END -->

<!-- FUNDS-CURATED-FLOW-0122-START -->
[Transfer-in instruction cancellation request](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p857-transfer-in-cancellation.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0122.md)
<!-- FUNDS-CURATED-FLOW-0122-END -->

<!-- FUNDS-CURATED-FLOW-0123-START -->
[Transfer instruction status query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p867-request-for-status.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0123.md)
<!-- FUNDS-CURATED-FLOW-0123-END -->

<!-- FUNDS-CURATED-FLOW-0124-START -->
[Transfer instruction status query rejected](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p871-request-for-status-rejection.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0124.md)
<!-- FUNDS-CURATED-FLOW-0124-END -->

<!-- FUNDS-CURATED-FLOW-0125-START -->
[Unsolicited transfer instruction status — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p876-status-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0125.md)
<!-- FUNDS-CURATED-FLOW-0125-END -->

<!-- FUNDS-CURATED-FLOW-0126-START -->
[Unsolicited transfer instruction status — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p881-status-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0126.md)
<!-- FUNDS-CURATED-FLOW-0126-END -->

<!-- FUNDS-CURATED-FLOW-0127-START -->
[Transfer cancellation status query — direct](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p886-cancellation-status-direct.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0127.md)
<!-- FUNDS-CURATED-FLOW-0127-END -->

<!-- FUNDS-CURATED-FLOW-0128-START -->
[Transfer cancellation status query — intermediary](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p893-transfer-cancellation-status-intermediary.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0128.md)
<!-- FUNDS-CURATED-FLOW-0128-END -->

<!-- FUNDS-CURATED-FLOW-0132-START -->
[Accounting holdings statement](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p920-accounting-statement-of-holdings.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0132.md)
<!-- FUNDS-CURATED-FLOW-0132-END -->

<!-- FUNDS-CURATED-FLOW-0133-START -->
[Accounting holdings statement query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p923-accounting-statement-of-holdings-request.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0133.md)
<!-- FUNDS-CURATED-FLOW-0133-END -->

<!-- FUNDS-CURATED-FLOW-0134-START -->
[Accounting holdings statement cancellation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p926-accounting-statement-of-holdings-cancellation.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0134.md)
<!-- FUNDS-CURATED-FLOW-0134-END -->

<!-- FUNDS-CURATED-FLOW-0135-START -->
[Custody holdings statement](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p930-custody-statement-of-holdings.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0135.md)
<!-- FUNDS-CURATED-FLOW-0135-END -->

<!-- FUNDS-CURATED-FLOW-0136-START -->
[Custody holdings statement query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p933-custody-statement-of-holdings-request.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0136.md)
<!-- FUNDS-CURATED-FLOW-0136-END -->

<!-- FUNDS-CURATED-FLOW-0137-START -->
[Custody holdings statement cancellation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p936-custody-statement-of-holdings-cancellation.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0137.md)
<!-- FUNDS-CURATED-FLOW-0137-END -->

<!-- FUNDS-CURATED-FLOW-0138-START -->
[Transparency holdings statement aggregation and status](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p940-transparency-of-holdings-statement.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0138.md)
<!-- FUNDS-CURATED-FLOW-0138-END -->

<!-- FUNDS-CURATED-FLOW-0139-START -->
[Investment fund transaction statement](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p945-statement-of-investment-fund-transactions.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0139.md)
<!-- FUNDS-CURATED-FLOW-0139-END -->

<!-- FUNDS-CURATED-FLOW-0140-START -->
[Investment fund transaction statement query](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p948-statement-of-investment-fund-transactions-request.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0140.md)
<!-- FUNDS-CURATED-FLOW-0140-END -->

<!-- FUNDS-CURATED-FLOW-0141-START -->
[Investment fund transaction statement cancellation](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p951-statement-of-investment-fund-transactions-cancellation.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0141.md)
<!-- FUNDS-CURATED-FLOW-0141-END -->

<!-- FUNDS-PROCESS-fig-0001 -->
[Investment Funds communication scope](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0001.md)
<!-- /FUNDS-PROCESS-fig-0001 -->

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
