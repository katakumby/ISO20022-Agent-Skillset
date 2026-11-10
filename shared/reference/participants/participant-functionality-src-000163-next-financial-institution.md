---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["payments"]
participant_id: "participant-functionality-src-000163-next-financial-institution"
title: "next financial institution in the payment chain — Payments Clearing and Settlement Functionality"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
source_labels: ["next financial institution in the payment chain"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14"]
message_families: ["pacs.008"]
source_locations: [{"source_id": "src-000163", "heading": "6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "file_pages": [702], "evidence_id": "src-000163-pacs.008.001.14-p702-c007"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# next financial institution in the payment chain — Payments Clearing and Settlement Functionality

[src-000163](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf)

## Definition and business context

The next financial institution addressed by the preceding financial institution in the source description of the Serial payment method, under the explicit condition that more than two financial institutions are involved.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000163-pacs.008.001.14-p702-c007

src-000163, file page 702; 6 pacs.008.001.14 FIToFICustomerCreditTransferV14.

> If more than two financial institutions are involved in the payment chain and if the FIToFICustomerCreditTransfer is sent from one financial institution to the next financial institution in the payment chain, then the payment method is called the Serial method.

## Applicable exact messages


- [pacs.008.001.14](../../../domains/payments/reference/messages/pacs.008.001.14/roles.md)

## Identity and unresolved scope

Source labels: next financial institution in the payment chain. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
