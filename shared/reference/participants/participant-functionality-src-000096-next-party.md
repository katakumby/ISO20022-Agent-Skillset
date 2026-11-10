---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["securities"]
participant_id: "participant-functionality-src-000096-next-party"
title: "next party — Investment Funds Functionality"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
source_labels: ["next party"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["investment-funds"]
message_ids: ["sese.010.001.07", "setr.016.001.05", "setr.057.001.03"]
message_families: ["sese.010", "setr.016", "setr.057"]
source_locations: [{"source_id": "src-000096", "heading": "33 sese.010.001.07 TransferCancellationStatusReportV07", "file_pages": [809], "evidence_id": "src-000096-sese.010.001.07-p809-c005"}, {"source_id": "src-000096", "heading": "56 setr.016.001.05 OrderInstructionStatusReportV05", "file_pages": [4109], "evidence_id": "src-000096-setr.016.001.05-p4109-c003"}, {"source_id": "src-000096", "heading": "56 setr.016.001.05 OrderInstructionStatusReportV05", "file_pages": [4109], "evidence_id": "src-000096-setr.016.001.05-p4109-c005"}, {"source_id": "src-000096", "heading": "64 setr.057.001.03 OrderConfirmationStatusReportV03", "file_pages": [4283], "evidence_id": "src-000096-setr.057.001.03-p4283-c002"}, {"source_id": "src-000096", "heading": "64 setr.057.001.03 OrderConfirmationStatusReportV03", "file_pages": [4283], "evidence_id": "src-000096-setr.057.001.03-p4283-c003"}, {"source_id": "src-000096", "heading": "64 setr.057.001.03 OrderConfirmationStatusReportV03", "file_pages": [4283], "evidence_id": "src-000096-setr.057.001.03-p4283-c005"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# next party — Investment Funds Functionality

[src-000096](../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf)

## Definition and business context

Next participant in the source-described transfer or order-processing chain. Each exact message context retains its direction, onward-transmission state and communication-problem conditions; this label does not fix one institution across those chains.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000096-sese.010.001.07-p809-c005

src-000096, file page 809; 33 sese.010.001.07 TransferCancellationStatusReportV07.

> the transfer cancellation has been sent to the next party, or,

### src-000096-setr.016.001.05-p4109-c003

src-000096, file page 4109; 56 setr.016.001.05 OrderInstructionStatusReportV05.

> a sent to next party status, or,

### src-000096-setr.016.001.05-p4109-c005

src-000096, file page 4109; 56 setr.016.001.05 OrderInstructionStatusReportV05.

> a communication problem with next party status, or, Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05 Investment Funds - Maintenance 2025 - 2026 4109 May 2026

### src-000096-setr.057.001.03-p4283-c002

src-000096, file page 4283; 64 setr.057.001.03 OrderConfirmationStatusReportV03.

> sent to next party, or,

### src-000096-setr.057.001.03-p4283-c003

src-000096, file page 4283; 64 setr.057.001.03 OrderConfirmationStatusReportV03.

> communication problem with next party, or,

### src-000096-setr.057.001.03-p4283-c005

src-000096, file page 4283; 64 setr.057.001.03 OrderConfirmationStatusReportV03.

> It is likely that the OrderConfirmationStatusReport is only sent by the order instructing party to the order executing party to reject an order confirmation or to reject an order confirmation amendment, although if an intermediary party is used, the statuses sent to next party and communication problem with next party are also likely be used.

## Applicable exact messages


- [sese.010.001.07](../../../domains/securities/reference/messages/sese.010.001.07/roles.md)
- [setr.016.001.05](../../../domains/securities/reference/messages/setr.016.001.05/roles.md)
- [setr.057.001.03](../../../domains/securities/reference/messages/setr.057.001.03/roles.md)

## Identity and unresolved scope

Source labels: next party. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
