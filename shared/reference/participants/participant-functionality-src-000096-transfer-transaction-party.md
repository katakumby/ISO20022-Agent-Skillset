---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["securities"]
participant_id: "participant-functionality-src-000096-transfer-transaction-party"
title: "any party in the transfer transaction — Investment Funds Functionality"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
source_labels: ["any party in the transfer transaction", "another party in the transfer transaction chain"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["investment-funds"]
message_ids: ["sese.009.001.09", "sese.011.001.10"]
message_families: ["sese.009", "sese.011"]
source_locations: [{"source_id": "src-000096", "heading": "32 sese.009.001.09 RequestForTransferStatusReportV09", "file_pages": [784], "evidence_id": "src-000096-sese.009.001.09-p784-c002"}, {"source_id": "src-000096", "heading": "34 sese.011.001.10 TransferInstructionStatusReportV10", "file_pages": [816], "evidence_id": "src-000096-sese.011.001.10-p816-c002"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# any party in the transfer transaction — Investment Funds Functionality

[src-000096](../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf)

## Definition and business context

Transaction-chain participant which can request or provide transfer-status information to another participant in that transfer chain. The source qualifies the availability with may also; the generic function does not assert a particular institution.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000096-sese.009.001.09-p784-c002

src-000096, file page 784; 32 sese.009.001.09 RequestForTransferStatusReportV09.

> The RequestForTransferStatusReport may also be sent by any party in the transfer transaction to another party in the transfer transaction chain to request information relevant for the settlement of a transfer transaction.

### src-000096-sese.011.001.10-p816-c002

src-000096, file page 816; 34 sese.011.001.10 TransferInstructionStatusReportV10.

> The TransferInstructionStatusReport message may also be sent by any party in the transfer transaction to another party in the transfer transaction chain to provide information relevant for the settlement of a transfer transaction.

## Applicable exact messages


- [sese.009.001.09](../../../domains/securities/reference/messages/sese.009.001.09/roles.md)
- [sese.011.001.10](../../../domains/securities/reference/messages/sese.011.001.10/roles.md)

## Identity and unresolved scope

Source labels: any party in the transfer transaction, another party in the transfer transaction chain. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
