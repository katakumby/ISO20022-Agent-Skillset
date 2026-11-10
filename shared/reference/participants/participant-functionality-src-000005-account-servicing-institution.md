---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "shared"
domains: ["payments"]
participant_id: "participant-functionality-src-000005-account-servicing-institution"
title: "account servicing institutions — Bank-to-Customer Cash Management Functionality"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
source_labels: ["account servicing institution", "account servicing institutions", "one of its account servicing institutions"]
aliases: []
role_type: "functional participant explicitly named in message Functionality"
message_sets: ["bank-to-customer-cash-management"]
message_ids: ["camt.060.001.07"]
message_families: ["camt.060"]
source_locations: [{"source_id": "src-000005", "heading": "5 camt.060.001.07 AccountReportingRequestV07", "file_pages": [781], "evidence_id": "src-000005-camt.060.001.07-p781-c001"}, {"source_id": "src-000005", "heading": "5 camt.060.001.07 AccountReportingRequestV07", "file_pages": [781], "evidence_id": "src-000005-camt.060.001.07-p781-c002"}]
identifier_schemes: []
limitations: ["Meaning is scoped to these exact quoted message contexts; a generic role label does not identify one institution across messages.", "A separate formal business-role definition or identifier scheme is not supplied in these Functionality clauses.", "Mention in an example, routing clause or alternative is not automatically an independent sender or receiver."]
---





# account servicing institutions — Bank-to-Customer Cash Management Functionality

[src-000005](../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf)

## Definition and business context

Recipient institution for AccountReportingRequest, selected from the account owner’s servicing institutions. The quoted direct or forwarding-agent route remains explicit.

This record collects the literal role within this publication. It does not equate that function with a particular institution or with a differently scoped role having the same name.

## Responsibilities, actions and relationships

The complete evidence below preserves who acts, the counterparties, alternatives and conditions. Only explicit clauses establish directions; quoted examples remain examples.

### src-000005-camt.060.001.07-p781-c001

src-000005, file page 781; 5 camt.060.001.07 AccountReportingRequestV07.

> The AccountReportingRequest message is sent by the account owner, either directly or through a forwarding agent, to one of its account servicing institutions.

## Applicable exact messages


- [camt.060.001.07](../../../domains/payments/reference/messages/camt.060.001.07/roles.md)

## Identity and unresolved scope

Source labels: account servicing institutions. No identifier scheme or institution equivalence is inferred. The quoted clauses define the available actions; no absent duty, flow or business condition is invented.

<!-- FUNCTIONALITY-ALIASES-src-000005 -->
## Additional literal publication labels

Singular and qualified plural source phrases refer to the servicing institution addressed by AccountReportingRequest.

| Source label | Source context |
| --- | --- |
| account servicing institution | src-000005-camt.060.001.07-p781-c002 |
| one of its account servicing institutions | src-000005-camt.060.001.07-p781-c001 |


> The AccountReportingRequest message is sent by the account owner, either directly or through a forwarding agent, to one of its account servicing institutions.

src-000005, file pages781; 5 camt.060.001.07 AccountReportingRequestV07.

> It is used to ask the account servicing institution to send a report on the account owner's account in a BankToCustomerAccountReport (camt.052), a BankToCustomerStatement (camt.053) or a BankToCustomerDebitCreditNotification (camt.054).

src-000005, file pages781; 5 camt.060.001.07 AccountReportingRequestV07.

<!-- /FUNCTIONALITY-ALIASES-src-000005 -->
