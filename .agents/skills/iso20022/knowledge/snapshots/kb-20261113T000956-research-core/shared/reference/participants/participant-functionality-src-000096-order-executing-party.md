---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["securities"]
participant_id: "participant-functionality-src-000096-order-executing-party"
title: "order executing party — Investment Funds Functionality"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
source_labels: ["order executing party"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["investment-funds"]
message_ids: ["setr.057.001.03"]
message_families: ["setr.057"]
source_locations: [{"source_id": "src-000096", "heading": "64 setr.057.001.03 OrderConfirmationStatusReportV03", "file_pages": [4283], "evidence_id": "src-000096-setr.057.001.03-p4283-c005"}, {"source_id": "src-000096", "heading": "64 setr.057.001.03 OrderConfirmationStatusReportV03", "file_pages": [4283], "evidence_id": "src-000096-setr.057.001.03-p4283-c006"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# order executing party — Investment Funds Functionality

[src-000096](../../../evidence/omitted/fffd4ab68b421d059524ec38.md)

## Definition and business context

Order-side executing function receiving OrderConfirmationStatusReport and potentially sending RequestForOrderConfirmationStatusReport. The source conditions for accepted/received versus other status values are retained.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000096-setr.057.001.03-p4283-c005

src-000096, file page 4283; 64 setr.057.001.03 OrderConfirmationStatusReportV03.

> It is likely that the OrderConfirmationStatusReport is only sent by the order instructing party to the order executing party to reject an order confirmation or to reject an order confirmation amendment, although if an intermediary party is used, the statuses sent to next party and communication problem with next party are also likely be used.

### src-000096-setr.057.001.03-p4283-c006

src-000096, file page 4283; 64 setr.057.001.03 OrderConfirmationStatusReportV03.

> The statuses confirmation accepted and confirmation received would only be used in the event the order executing party sends a RequestForOrderConfirmationStatusReport message and one of the other statuses does not apply.

## Applicable exact messages


- [setr.057.001.03](../../../domains/securities/reference/messages/setr.057.001.03/roles.md)

## Identity and unresolved scope

Source labels: order executing party. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
