---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000180-cash-correspondent"
title: "Cash Correspondent"
source_labels: ["Cash Correspondent"]
role_type: "source-scoped business actor in flow"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
source_locations: [{"source_id": "src-000180", "locator": "P222/P223/P224; images15-17/P216/P220/P224"}]
message_sets: ["post-trade-matching"]
message_ids: ["setr.027.001.05", "setr.029.001.02", "setr.030.001.03"]
flows: ["flow-src-000180-p214-duplex-type", "flow-src-000180-p218-duplex-type-rejection-by-transfer-agent", "flow-src-000180-p222-duplex-type-rejection-by-cash-correspondent"]
aliases: []
search_terms: ["Cash Correspondent"]
limitations: ["The same narrative passages use Cash Settlement Agent while artwork labels Cash Correspondent. Both labels and their source correspondence are recorded; no general institutional equivalence is assumed.", "No identifier scheme is specified in these source passages."]
---







# Cash Correspondent

## Definition and context

The diagram participant that receives a forwarded confirmation after the Transfer Agent response in the duplex flow and can send a confirmation response; the rejection scenario is explicitly titled Rejection by Cash Correspondent.

## Responsibilities and relationships

Receives a forwarded confirmation; returns a response; may reject trade details and receive a forwarded cancellation.

The same narrative passages use Cash Settlement Agent while artwork labels Cash Correspondent. Both labels and their source correspondence are recorded; no general institutional equivalence is assumed.

Source: [src-000180](../../../raw-input/post_trade_matching/ISO20022_MDRPart1_PostTradeMatching_2024_2025_v2.docx); P222/P223/P224; images15-17/P216/P220/P224. No identifier scheme is specified.

Post-trade matching scenario: [Duplex Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p214-duplex-type.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0018.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Duplex Type Rejection by Transfer Agent](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p218-duplex-type-rejection-by-transfer-agent.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0019.md). The source identifies this participant as an inactive lifeline or narrative alternative in this scenario.

Post-trade matching scenario: [Duplex Type Rejection by Cash Correspondent](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p222-duplex-type-rejection-by-cash-correspondent.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0020.md). The source diagram shows this participant as sender/receiver in the ordered exchange.
