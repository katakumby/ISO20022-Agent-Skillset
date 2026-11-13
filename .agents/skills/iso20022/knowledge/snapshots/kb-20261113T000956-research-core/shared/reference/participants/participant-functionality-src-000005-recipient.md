---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["payments"]
participant_id: "participant-functionality-src-000005-recipient"
title: "receiver — Bank-to-Customer Cash Management Functionality"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
source_labels: ["receiver"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["bank-to-customer-cash-management"]
message_ids: ["camt.052.001.14", "camt.053.001.14", "camt.054.001.14"]
message_families: ["camt.052", "camt.053", "camt.054"]
source_locations: [{"source_id": "src-000005", "heading": "2 camt.052.001.14 BankToCustomerAccountReportV14", "file_pages": [4], "evidence_id": "src-000005-camt.052.001.14-p4-c003"}, {"source_id": "src-000005", "heading": "3 camt.053.001.14 BankToCustomerStatementV14", "file_pages": [263], "evidence_id": "src-000005-camt.053.001.14-p263-c005"}, {"source_id": "src-000005", "heading": "4 camt.054.001.14 BankToCustomerDebitCreditNotificationV14", "file_pages": [523], "evidence_id": "src-000005-camt.054.001.14-p523-c003"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# receiver — Bank-to-Customer Cash Management Functionality

[src-000005](../../../evidence/omitted/4704d0f065c82a397d84d52d.md)

## Definition and business context

Generic recipient function explicitly named in this publication’s quoted message Functionality. Its precise capacity and counterparties are retained per clause rather than being inferred from the generic label.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000005-camt.052.001.14-p4-c003

src-000005, file page 4; 2 camt.052.001.14 BankToCustomerAccountReportV14.

> It is possible that the receiver of the message is not the account owner, but a party entitled by the account owner to receive the account information (also known as recipient).

### src-000005-camt.053.001.14-p263-c005

src-000005, file page 263; 3 camt.053.001.14 BankToCustomerStatementV14.

> It is possible that the receiver of the message is not the account owner, but a party entitled through arrangement with the account owner to receive the account information (also known as recipient).

### src-000005-camt.054.001.14-p523-c003

src-000005, file page 523; 4 camt.054.001.14 BankToCustomerDebitCreditNotificationV14.

> It is possible that the receiver of the message is not the account owner, but a party entitled by the account owner to receive the account information (also known as recipient).

## Applicable exact messages


- [camt.052.001.14](../../../domains/payments/reference/messages/camt.052.001.14/roles.md)
- [camt.053.001.14](../../../domains/payments/reference/messages/camt.053.001.14/roles.md)
- [camt.054.001.14](../../../domains/payments/reference/messages/camt.054.001.14/roles.md)

## Identity and unresolved scope

Source labels: receiver. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
