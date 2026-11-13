---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000180-institutional-investor"
title: "Institutional Investor"
source_labels: ["Institutional Investor"]
role_type: "source-scoped business actor in flow"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
source_locations: [{"source_id": "src-000180", "locator": "P154/P204/P209; image13/P205; image14/P210"}]
message_sets: ["post-trade-matching"]
message_ids: ["setr.027.001.05", "setr.029.001.02", "setr.030.001.03"]
flows: ["flow-src-000180-p153-own-account-trade-type", "flow-src-000180-p203-own-account-trade-type", "flow-src-000180-p208-own-account-trade-type-cancellation"]
aliases: []
search_terms: ["Institutional Investor"]
limitations: ["The source notes an analogous Underwriter/Issuer Agent flow; this is an alternative pair of actors, not an assertion that Institutional Investor and Issuer Agent are equivalent.", "No identifier scheme is specified in these source passages."]
---







# Institutional Investor

## Definition and context

The own-account-trade participant to which the CMU forwards the executing broker confirmation and from which an affirmation or disaffirmation is received.

## Responsibilities and relationships

Compares confirmation details with its own trade details; affirms when agreed, or disaffirms irreconcilable details.

The source notes an analogous Underwriter/Issuer Agent flow; this is an alternative pair of actors, not an assertion that Institutional Investor and Issuer Agent are equivalent.

Source: [src-000180](../../../evidence/omitted/620693d01e301c06503cea9a.md); P154/P204/P209; image13/P205; image14/P210. No identifier scheme is specified.

Post-trade matching scenario: [Own Account Trade Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p203-own-account-trade-type.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0016.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Own Account Trade Type Cancellation](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p208-own-account-trade-type-cancellation.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0017.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Source context: [Own-account local matching activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0008.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p153-own-account-trade-type.md).
