---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["payments"]
participant_id: "participant-functionality-src-000005-party-authorised-by-account-owner"
title: "party authorised by the account owner — Bank-to-Customer Cash Management Functionality"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
source_labels: ["party authorised by the account owner"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["bank-to-customer-cash-management"]
message_ids: ["camt.052.001.14", "camt.053.001.14", "camt.054.001.14"]
message_families: ["camt.052", "camt.053", "camt.054"]
source_locations: [{"source_id": "src-000005", "heading": "2 camt.052.001.14 BankToCustomerAccountReportV14", "file_pages": [4], "evidence_id": "src-000005-camt.052.001.14-p4-c001"}, {"source_id": "src-000005", "heading": "3 camt.053.001.14 BankToCustomerStatementV14", "file_pages": [263], "evidence_id": "src-000005-camt.053.001.14-p263-c001"}, {"source_id": "src-000005", "heading": "4 camt.054.001.14 BankToCustomerDebitCreditNotificationV14", "file_pages": [523], "evidence_id": "src-000005-camt.054.001.14-p523-c001"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---

# party authorised by the account owner — Bank-to-Customer Cash Management Functionality

[src-000005](../../../evidence/omitted/4704d0f065c82a397d84d52d.md)

## Definition and business context

Alternative recipient authorised by the account owner for account reports, statements or debit/credit notifications. It is distinct from the account owner and from the account servicer.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000005-camt.052.001.14-p4-c001

src-000005, file page 4; 2 camt.052.001.14 BankToCustomerAccountReportV14.

> The BankToCustomerAccountReport message is sent by the account servicer to an account owner or to a party authorised by the account owner to receive the message.

### src-000005-camt.053.001.14-p263-c001

src-000005, file page 263; 3 camt.053.001.14 BankToCustomerStatementV14.

> The BankToCustomerStatement message is sent by the account servicer to an account owner or to a party authorised by the account owner to receive the message.

### src-000005-camt.054.001.14-p523-c001

src-000005, file page 523; 4 camt.054.001.14 BankToCustomerDebitCreditNotificationV14.

> The BankToCustomerDebitCreditNotification message is sent by the account servicer to an account owner or to a party authorised by the account owner to receive the message.

## Applicable exact messages


- [camt.052.001.14](../../../domains/payments/reference/messages/camt.052.001.14/roles.md)
- [camt.053.001.14](../../../domains/payments/reference/messages/camt.053.001.14/roles.md)
- [camt.054.001.14](../../../domains/payments/reference/messages/camt.054.001.14/roles.md)

## Identity and unresolved scope

Source labels: party authorised by the account owner. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.
