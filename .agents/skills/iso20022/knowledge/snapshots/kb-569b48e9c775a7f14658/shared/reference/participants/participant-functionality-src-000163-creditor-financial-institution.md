---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["payments"]
participant_id: "participant-functionality-src-000163-creditor-financial-institution"
title: "creditor financial institution — Payments Clearing and Settlement Functionality"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
source_labels: ["creditor financial institution"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.009.001.13"]
message_families: ["pacs.009"]
source_locations: [{"source_id": "src-000163", "heading": "7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "file_pages": [830], "evidence_id": "src-000163-pacs.009.001.13-p830-c001"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# creditor financial institution — Payments Clearing and Settlement Functionality

[src-000163](../../../evidence/omitted/0b754f3040fa67a0a084bf38.md)

## Definition and business context

Creditor-side institution receiving FinancialInstitutionCreditTransfer, with the direct or intermediary route retained. Its role is scoped to the quoted payment relationship.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000163-pacs.009.001.13-p830-c001

src-000163, file page 830; 7 pacs.009.001.13 FinancialInstitutionCreditTransferV13.

> The FinancialInstitutionCreditTransfer message is sent by a debtor financial institution to a creditor financial institution, directly or through other agents and/or a payment clearing and settlement system.

## Applicable exact messages


- [pacs.009.001.13](../../../domains/payments/reference/messages/pacs.009.001.13/roles.md)

## Identity and unresolved scope

Source labels: creditor financial institution. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
