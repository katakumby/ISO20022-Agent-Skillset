---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["21 camt.023.001.07 BackupPaymentV07"]
file_pages: [577, 578]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.023.001.07"]
---

# 21 camt.023.001.07 BackupPaymentV07

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 577 to 578.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 577

```text
21 camt.023.001.07
BackupPaymentV07
21.1 MessageDefinition Functionality
Scope
The BackupPayment message is sent by a member to the transaction administrator.
It is used to request a liquidity transfer from the member to another participant in the system when the
user is in recovery mode.
Usage
Under very specific circumstances, the transaction administrator can accept direct input of transactions
as part of its cash management functionalities. This possibility is available only when a declared
incident has been reported to the transaction administrator This could be the case, for example, when
the internal systems of the member are having problems sending out payments or when the continuity
of the whole system is put at risk.
The purpose of the BackupPayment message is to prevent the consequences of a specific failure
affecting not only the member experiencing problems but also its counterparties. Members can
therefore input transactions directly in order to ensure the stability of the system and smooth
exchanges.
At any time during the operating hours of the system, and under the agreed circumstances, the member
can request a backup payment to be effected.
The member can request the transfer by identifying the following elements:
- party (account owner) that will receive the funds
- the financial institution that will receive the funds on behalf of the account owner
Based on the criteria received within the BackupPayment message, the transaction administrator will
execute or reject the requested funds transfer.
The transaction administrator may send a Receipt message as a reply to the BackupPayment request.
To verify the outcome of the request, the member may submit a GetTransaction or GetAccount
message with the appropriate search criteria.
Outline
The BackupPaymentV07 MessageDefinition is composed of 8 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. OriginalMessageIdentification
Identifies the original message identification.
This was formerly the PaymentInstructionReference.
Approved by the Payments SEG on 04 February 2025 camt.023.001.07 BackupPaymentV07
Cash Management - Maintenance 2024 - 2025 577 February 2025
```

## File page 578

```text
C. InstructionInformation
Provides details on the execution and type of payment contained in the instruction.
D. TransferredAmount
Quantity of cash that the transaction administrator transfers from one account to another.
E. Creditor
Party that receives an amount of money from the debtor.
F. CreditorAgent
Financial institution that receives the payment transaction on behalf of an account owner, or other
nominated party, and credits the account.
G. DebtorAgent
Financial institution that receives the payment transaction from the account owner, or other
authorised party, and processes the instruction.
H. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.023.001.07 BackupPaymentV07
Cash Management - Maintenance 2024 - 2025 578 February 2025
```

