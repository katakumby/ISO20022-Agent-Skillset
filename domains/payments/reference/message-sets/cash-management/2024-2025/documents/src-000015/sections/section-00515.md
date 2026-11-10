---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["29 camt.051.001.07 LiquidityDebitTransferV07"]
file_pages: [677]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.051.001.07"]
---

# 29 camt.051.001.07 LiquidityDebitTransferV07

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 677 to 677.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 677

```text
29 camt.051.001.07
LiquidityDebitTransferV07
29.1 MessageDefinition Functionality
Scope
The LiquidityDebitTransfer message is sent by a member to the transaction administrator.
It is used to request a transfer of funds between two accounts belonging to the same member or the
same group of accounts, and being held at the transaction administrator.
Usage
At any time during the operating hours of the system, and to perform the appropriate liquidity
management, the member can request the transaction administrator to execute the transfer of funds
between two accounts that the transaction administrator maintains for the member. For instance, this
may be an action resulting from a Get/Return Account pair of messages.
The LiquidityDebitTransfer message can be used when the transactions to/from the member are
unbalanced in value for the business day, or to unlock pending transactions at the end of day.
The member can request the transfer by identifying the accounts stored at the transaction administrator:
- If the accounts involved in the requested transfer are known without doubt to the transaction
administrator, it is possible to indicate only the type of the account to be credited.
- If, on the contrary, more clarity is desired, it is possible to identify the accounts from and to which the
funds should be transferred.
Note that transfers are processed only when the balance in the account to be debited is sufficient to
pass the liquidity transfer instruction and remain positive. Based on the criteria received within the
LiquidityDebitTransfer message, the transaction administrator will execute or reject the requested
transfer.
In principle, the transaction administrator may send a Receipt message as a reply to the liquidity
transfer request. To verify the outcome of the request, the member may submit a GetTransaction or
GetAccount message with the appropriate search criteria.
Outline
The LiquidityDebitTransferV07 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. LiquidityDebitTransfer
Details of the liquidity debit transfer.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.051.001.07 LiquidityDebitTransferV07
Cash Management - Maintenance 2024 - 2025 677 February 2025
```

