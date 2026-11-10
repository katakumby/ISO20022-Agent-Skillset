---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11"]
file_pages: [206, 207, 208]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5 camt.006.001.11 ReturnTransactionV11

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 206 to 208.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 206

```text
5 camt.006.001.11
ReturnTransactionV11
5.1 MessageDefinition Functionality
Scope
The ReturnTransaction message is sent by the transaction administrator to a member of the system.
It is used to provide information on transactions and booked entries held at the transaction
administrator.
The Return Transaction message can be sent as a response to a related GetTransaction message (pull
mode) or initiated by the transaction administrator (push mode). The push of information can take place
either at prearranged times or as a warning or alarm when a problem has occurred.
Usage
Following normal business flows, transactions registered by the transaction administrator may be
queued for later settlement (because of insufficient funds available, because of risk or liquidity limits,
etc.). A transaction may have a series of statuses. These can be transient (such as pending or related
types) and final (such as rejected or settled).
Members of a system need to receive information about the payments queue(s) and must have the
ability to take action (that is, cancel or modify the transaction(s) to be settled). Note, however, that
actions by a member will always concern transactions in a transient status.
At any time during operating hours of the system, the member can query the transaction administrator
to get information about transactions, whatever their status.
These requests will concern either all transactions, all transactions within a particular status or a
specific transaction.
The member can request information about transactions through a series of criteria, corresponding to
the known information stored within the transaction administrator. Based on the criteria received within
the request, the transaction administrator will select items that match the request and report them to the
requester.
The transaction administrator may also send a ReturnTransaction message with pre-defined
information at times previously agreed with the member or to warn the member about a particular
problem that may have arisen and which needs attention.
The message from the transaction administrator can contain information based on the following
elements:
- provenance or destination of the payment (payment to/payment from)
- transaction reference
- transfer value date
- payment instruction reference
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 206 February 2025
```

## File page 207

```text
- payment instruction status, as registered at the transaction administrator
- instructed amount and/or currency
- interbank settlement amount and/or currency
- credit/debit indicator of the payment instruction/transaction
- message used for the payment instruction
- priority of the payment transaction
- period in which the payment instruction should be processed (processing validity time)
- instructions given, related to the processing of the transaction
- type of payment instructed
- account identification (entries booked to a specific account)
- entry amount and/or currency
- entry debit/credit indicator (if absent, all entries should be reported)
- status of the entry (pending, booked.)
- entry date and time
- currency of the account
- type of the account
- entry reference
- entry date
- transfer reason
- details related to the status of the payment instruction
An element that is particular to the Get/Return Transaction pair is the Statement Report. When a
GetTransaction message is sent requesting a statement report, the related ReturnTransaction message
will provide a pre-defined set of return criteria per transaction. The information returned contains the
following details for each transaction:
- value date
- entry date
- debit/credit code
- entry amount
- method of payment (payment instrument or message type)
- entry reference
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 207 February 2025
```

## File page 208

```text
- transaction reference
- supplementary details
Additional information on the generic design of the Get/Return messages can be found in the section
How to Use the Cash Management Messages.
Outline
The ReturnTransactionV11 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Reports on transactions.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 208 February 2025
```

