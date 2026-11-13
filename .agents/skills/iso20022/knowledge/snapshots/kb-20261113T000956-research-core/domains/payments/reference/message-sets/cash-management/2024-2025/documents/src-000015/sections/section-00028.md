---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10"]
file_pages: [48, 49]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3 camt.004.001.10 ReturnAccountV10

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 48 to 49.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 48

```text
3 camt.004.001.10
ReturnAccountV10
3.1 MessageDefinition Functionality
Scope
The ReturnAccount message is sent by the transaction administrator to a member.
It is used to provide information on the details of one or more accounts held at the transaction
administrator, including information on the balances.
The Return Account message can be sent as a response to a related GetAccount message (pull mode)
or initiated by the transaction administrator (push mode). The push of information can take place either
at prearranged times or as a warning or alarm when a problem has occurred.
Usage
At any time during the operating hours of the system, the member can query the transaction
administrator to get information about the account(s) that the transaction administrator maintains for the
member.
For example, this may be necessary in order to perform the appropriate liquidity management and the
necessary funds transfers between accounts.
The member can request information about accounts through a series of criteria, corresponding to the
known information stored at the transaction administrator.
The query can concern one or more specific accounts, accounts of a particular identification, or a
particular type. The purpose of the query may be to obtain one or more types of balance.
The transaction administrator may also send a ReturnAccount message with pre-defined information, at
times previously agreed with the member, or to warn the member about a particular problem that may
have arisen and which needs attention.
The message from the transaction administrator can contain information based on the following
elements:
- account identification
- account name
- account type (this is used when the account identification represents, for example, a group of
accounts)
- currency of the account (this is used for example when the account identification represents a group of
account in various currencies, or when it is a multi-currency account with one single identifier)
- type of balance (if not present in the GetAccount message, all balances will be reported)
- bilateral or multilateral limits
- related counterparty (when the limit or balance is bilateral)
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 48 February 2025
```

## File page 49

```text
- balance value date (if not present in the GetAccount message, the ReturnAccount message will
contain the latest available balance)
- number of payments to the additional account information on the generic design of the Get/Return
messages can be found in the section How to Use the Cash Management Messages.
Outline
The ReturnAccountV10 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Common business identification for the message.
B. ReportOrError
Reports on accounts.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 49 February 2025
```

