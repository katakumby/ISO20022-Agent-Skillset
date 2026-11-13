---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000180-issuer-agent"
title: "Issuer Agent"
source_labels: ["Issuer Agent"]
role_type: "source-scoped business actor in flow"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
source_locations: [{"source_id": "src-000180", "locator": "image13/P205 and image14/P210, note below sequence; activity image5/P155 label"}]
message_sets: ["post-trade-matching"]
message_ids: []
flows: ["flow-src-000180-p153-own-account-trade-type", "flow-src-000180-p203-own-account-trade-type", "flow-src-000180-p208-own-account-trade-type-cancellation"]
aliases: []
search_terms: ["Issuer Agent"]
limitations: ["Kept distinct from Institutional Investor and Underwriter; the source supplies an analogous flow, not an identity equivalence.", "No identifier scheme is specified in these source passages."]
---







# Issuer Agent

## Definition and context

An actor named in the source note as an alternative recipient in an analogous flow with an Underwriter. A standalone definition is not supplied in these passages.

## Responsibilities and relationships

Participates in the alternative Underwriter-to-Issuer-Agent confirmation flow identified by the source figure note.

Kept distinct from Institutional Investor and Underwriter; the source supplies an analogous flow, not an identity equivalence.

Source: [src-000180](../../../evidence/omitted/620693d01e301c06503cea9a.md); image13/P205 and image14/P210, note below sequence; activity image5/P155 label. No identifier scheme is specified.

Post-trade matching scenario: [Own Account Trade Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p203-own-account-trade-type.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0016.md). The source identifies this participant as an inactive lifeline or narrative alternative in this scenario.

Post-trade matching scenario: [Own Account Trade Type Cancellation](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p208-own-account-trade-type-cancellation.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0017.md). The source identifies this participant as an inactive lifeline or narrative alternative in this scenario.

Source context: [Own-account local matching activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0008.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p153-own-account-trade-type.md).
