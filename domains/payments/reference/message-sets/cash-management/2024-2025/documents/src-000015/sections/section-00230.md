---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 camt.008.001.11 CancelTransactionV11"]
file_pages: [347, 348]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.008.001.11"]
---

# 7 camt.008.001.11 CancelTransactionV11

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 347 to 348.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 347

```text
7 camt.008.001.11
CancelTransactionV11
7.1 MessageDefinition Functionality
Scope
The CancelTransaction message is sent by a member to the transaction administrator.
It is used to request the cancellation of one payment instruction held at the transaction administrator
and sent by the member.
Usage
Following normal business flows, transactions registered by the transaction administrator may be
queued for later settlement (because of insufficient funds available, because of risk or liquidity limits,
etc.). A transaction may have a series of statuses. These can be transient (such as pending or related
types), final (such as rejected, revoked and/or settled) or the status may even be defined as a
proprietary status.
Members of a system need to have information about the payments queue(s), and must have the ability
to take action (that is, to cancel or modify the transaction(s) to be settled). Note, however, that actions
by a member will always concern transactions in a transient status.
For this reason, at any time during the operating hours of the system, the member can request the
cancellation of a transaction that has not received a final status.
The member will submit a CancelTransaction message containing the identification of the transaction to
be cancelled.
Based on the criteria received within the CancelTransaction message, the transaction administrator will
execute or reject the requested cancellation.
The transaction administrator may send a Receipt message as a reply to the CancelTransaction
request.
To verify the outcome of the request, the member may submit a GetTransaction message with the
appropriate search criteria.
Outline
The CancelTransactionV11 MessageDefinition is composed of 5 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. PaymentIdentification
Reference to the instruction related to the payment for which information is requested.
C. CashAccount
Account to or from which a cash entry is made.
D. CancellationReason
Approved by the Payments SEG on 04 February 2025 camt.008.001.11 CancelTransactionV11
Cash Management - Maintenance 2024 - 2025 347 February 2025
```

## File page 348

```text
Provides detailed information on the cancellation reason.
E. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.008.001.11 CancelTransactionV11
Cash Management - Maintenance 2024 - 2025 348 February 2025
```

