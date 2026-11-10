---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [3]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14", "camt.053.001.14", "camt.054.001.14", "camt.060.001.07"]
---

# 1 Message Set Overview

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 3 to 3.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3

```text
1 Message Set Overview
Introduction
This document describes the Bank-to-Customer Cash Management message set. It includes the new
version of the MessageDefinitions that have been added as part of the maintenance cycle 2025-2026
(See MCR #277) and approved by the Payments Standards Evaluation Group on 12 January 2026.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
camt.052.001.14
BankToCustomerAccountReportV14
The BankToCustomerAccountReport message is sent
by the account servicer to an account owner or to a
party authorised by the account owner to receive the
message. It can be used to inform the account owner,
or authorised party, of the entries reported to the
account, and/or to provide the owner with balance
information on the account at a given point in time.
camt.053.001.14
BankToCustomerStatementV14
The BankToCustomerStatement message is sent by
the account servicer to an account owner or to a party
authorised by the account owner to receive the
message. It is used to inform the account owner, or
authorised party, of the entries booked to the account,
and to provide the owner with balance information on
the account at a given point in time.
camt.054.001.14
BankToCustomerDebitCreditNotificationV14
The BankToCustomerDebitCreditNotification message
is sent by the account servicer to an account owner or
to a party authorised by the account owner to receive
the message. It can be used to inform the account
owner, or authorised party, of single or multiple debit
and/or credit entries reported to the account.
camt.060.001.07
AccountReportingRequestV07
The AccountReportingRequest message is sent by the
account owner, either directly or through a forwarding
agent, to one of its account servicing institutions. It is
used to ask the account servicing institution to send a
report on the account owner's account in a
BankToCustomerAccountReport (camt.052), a
BankToCustomerStatement (camt.053) or a
BankToCustomerDebitCreditNotification (camt.054).
Approved by the Payments SEG on 12 January 2026 Message Set Overview
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
3 March 2026
```

