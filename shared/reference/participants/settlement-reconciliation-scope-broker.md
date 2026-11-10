---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
participant_id: "participant-settlement-reconciliation-scope-broker"
title: "Broker"
domains: ["securities"]
domain: "securities"
message_sets: ["settlement-and-reconciliation"]
source_ids: ["src-000196"]
source_labels: ["Broker"]
aliases: []
source_locations: [{"source_id": "src-000196", "paragraph_id": "P145", "figure_id": "fig-0001", "heading_path": ["Scope and Functionality", "Scope"], "xml_path": "/w:document/w:body/w:p[145]"}]
role_kind: "illustrative institution/business participant; figure-scoped"
message_ids: []
flow_ids: ["flow-settlement-reconciliation-instruction-confirmation", "flow-settlement-reconciliation-transaction-generation", "flow-settlement-reconciliation-allegement"]
limitations: ["The supplied picture is the scope of this record. It gives no formal institution definition or identifier scheme.", "No equivalence with another same-named participant in a different collection is asserted."]
updated: "2026-11-09"
source_editions: ["March 2026"]
---

# Broker

The Broker in this illustration sends a receipt/delivery instruction to its local agent and receives the depicted status/processing advice, settlement confirmation, generated transaction advice and allegement.

[src-000196](../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx); Scope, settlement communication illustration, P145 / fig-0001.

[Communication graph, unchanged source artwork and visual review](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0001.md)

## Context and relationships

The source illustrates business participants using institutional pictograms. Its account-owner/account-servicer labels apply to the specific depicted relationship. They do not make an institutional category identical to a functional account role. No source-supported alias or identifier scheme is stated in this picture.

## Related flows

- [instruction confirmation](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/instruction-confirmation.md)
- [transaction generation](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/transaction-generation.md)
- [allegement](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/flows/allegement.md)

<!-- SOURCE196-DIAGRAM-1-START -->
[Settlement communication scope and account relationships](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities/fig-0001.md) — src-000196 direct-body paragraph P145.
<!-- SOURCE196-DIAGRAM-1-END -->
