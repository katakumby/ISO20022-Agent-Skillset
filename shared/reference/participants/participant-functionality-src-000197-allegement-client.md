---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["securities"]
participant_id: "participant-functionality-src-000197-allegement-client"
title: "client — Settlement and Reconciliation Functionality"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
source_labels: ["client"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["settlement-and-reconciliation"]
message_ids: ["sese.040.001.06"]
message_families: ["sese.040"]
source_locations: [{"source_id": "src-000197", "heading": "34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06", "file_pages": [1322], "evidence_id": "src-000197-sese.040.001.06-p1322-c002"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# client — Settlement and Reconciliation Functionality

[src-000197](../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf)

## Definition and business context

Client to whom an allegement may have been passed in the SecuritiesSettlementTransactionAllegementReport source clause. No equivalence with the portfolio-transfer or split-settlement client is inferred.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000197-sese.040.001.06-p1322-c002

src-000197, file page 1322; 34 sese.040.001.06 SecuritiesSettlementTransactionCounterpartyResponseV06.

> the allegement received is either rejected (that is counterparty's transaction is unknown) or accepted (i.e. either the allegement was passed to the client or the transaction is know with or without mismatches)

## Applicable exact messages


- [sese.040.001.06](../../../domains/securities/reference/messages/sese.040.001.06/roles.md)

## Identity and unresolved scope

Source labels: client. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
