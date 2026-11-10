---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11"]
file_pages: [98, 99]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4 camt.005.001.11 GetTransactionV11

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 98 to 99.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 98

```text
4 camt.005.001.11
GetTransactionV11
4.1 MessageDefinition Functionality
Scope
The GetTransaction message is sent by a member to the transaction administrator.
It is used to request information about payment instructions held at the transaction administrator.
Payment instructions are either sent by the member, debiting or crediting its account at the transaction
administrator or received by the transaction administrator, crediting or debiting the member's account.
Usage
Following normal business flows, transactions registered by the transaction administrator may be
queued for later settlement (because of insufficient funds available, or because of risk or liquidity limits,
etc.). A transaction may have a series of statuses. These can be transient (such as pending or related
types) and final (such as rejected, revoked and/or settled).
Members of a system need to have information about the payments queue(s) and must have the ability
to take action (that is, to cancel or modify the transaction(s) to be settled). Note, however, that actions
by a member will always concern transactions in a transient status.
At any time during the operating hours of the system, the member can query the transaction
administrator to get information about transactions, whatever their status.
These requests will concern either all transactions, all transactions with a particular status or a specific
transaction.
The member can request information about transactions through a series of criteria, corresponding to
the known information stored at the transaction administrator, based on the following elements:
- provenance or destination of the payment (payment to/payment from)
- transaction reference
- transfer value date
- payment instruction reference
- payment instruction status, as registered at the transaction administrator
- instructed amount and/or currency
- interbank settlement amount and/or currency
- credit/debit indicator of the payment instruction/transaction
- SWIFT FIN payment message used for the payment instruction
- priority of the payment transaction
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 98 February 2025
```

## File page 99

```text
- period in which the payment instruction should be processed (processing validity time)
- instructions given, related to the processing of the transaction
- type of payment instructed
- account identification (entries booked to a specific account)
- entry amount and/or currency
- entry debit/credit indicator (if absent, all entries should be reported).
Outline
The GetTransactionV11 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. TransactionQueryDefinition
Defines the transaction query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 99 February 2025
```

