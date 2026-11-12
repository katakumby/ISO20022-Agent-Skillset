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
participant_id: "participant-src-000095-end-client"
title: "End Client"
source_labels: ["End Client"]
role_type: "Narrative-only recipient in stock-transfer context"
aliases: []
source_locations: [{"source_id": "src-000095", "locator": "T43 rows7–8; P225 figure15"}, {"source_id": "src-000095", "locator": "T43 rows6–8; figure15"}]
flow_ids: ["flow-src-000095-p221-stock-transfers-single-leg-transfer"]
message_ids: []
limitations: ["Scoped to the supplied Investment Funds source; same-name roles in other publications are not merged.", "No identifier scheme is specified in the cited evidence."]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative/table/figure labels inspected; no independent institutional equivalence inferred."}
---



# End Client

[src-000095](../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md)

## Definition and context

Client informed of a transfer by the transferor bank or transferee bank. This source scope does not establish a distinct institution type or equate the client with every investor/account owner. (T43 rows7–8; P225 figure15)

Source classification: Narrative-only recipient in stock-transfer context. A functional role varies with the relationship; institutional examples do not fix the role for every process.

## Responsibilities and actions

Receives transfer information from the relevant bank after the transfer agent sends transfer confirmations. The figure includes Inform End Client actions but no separate End Client lane. (T43 rows6–8; figure15)

## Relationships

- [transferor s bank executing party](participant-src-000095-transferor-s-bank-executing-party.md)
- [transferee s bank executing party](participant-src-000095-transferee-s-bank-executing-party.md)

## Flows and messages

- [flow-src-000095-p221-stock-transfers-single-leg-transfer](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p221-stock-transfers-single-leg-transfer.md)

Message names in the cited source identify business exchanges; exact definitions are resolved through the message-set index.

## Identification and limitations

- Scoped to the supplied Investment Funds source; same-name roles in other publications are not merged.
- No identifier scheme is specified in the cited evidence.

<!-- FUNDS-CURATED-FLOW-0117-START -->
[Two-owner asset transfer — SLT market practice](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p828-two-account-owners-direct-slt-market-practice.md) · [Source diagram and exact message directions](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0117.md)
<!-- FUNDS-CURATED-FLOW-0117-END -->

<!-- FUNDS-PROCESS-fig-0015 -->
[Transfer Flow — Single Leg (from transfer agent perspective)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0015.md) · [Flow responsibilities](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p221-stock-transfers-single-leg-transfer.md)
<!-- /FUNDS-PROCESS-fig-0015 -->
