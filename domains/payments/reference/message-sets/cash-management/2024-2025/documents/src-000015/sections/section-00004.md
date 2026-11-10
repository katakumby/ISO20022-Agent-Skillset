---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 camt.003.001.08 GetAccountV08"]
file_pages: [13, 14]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08"]
---

# 2 camt.003.001.08 GetAccountV08

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 13 to 14.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 13

```text
2 camt.003.001.08
GetAccountV08
2.1 MessageDefinition Functionality
Scope
The GetAccount message is sent by a member to the transaction administrator.
It is used to request information on the details of one or more accounts held at the transaction
administrator, including information on the balances.
Usage
At any time during the operating hours of the system, the member can query the transaction
administrator to get information about the account(s) that the transaction administrator maintains for the
member.
For example, this may be necessary in order to perform the appropriate liquidity management and the
funds transfers between accounts.
The member can request information about accounts through a series of criteria, corresponding to the
known information stored at the transaction administrator.
The query can concern one or more specific accounts, accounts of a particular identification, or a
particular type. The purpose of the query may be to obtain one or more types of balance.
The member can request information based on the following elements:
- account identification
- account type (this element can be used to refine the query when the account identification represents,
for example, a group of accounts)
- balance type (if not present, all balances are requested)
- type of counterparty: bilateral or multilateral (note that, by default, a balance is multilateral unless a
particular counterparty is specified)
- identification of the counterparty when a bilateral balance is requested
- balance value date (if not present in the GetAccount message, the ReturnAccount message will
contain the latest available balance)
This message will be answered by a ReturnAccount message.
Additional information on the generic design of the Get/Return messages can be found in the section
How to Use the Cash Management Messages.
Outline
The GetAccountV08 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 13 February 2025
```

## File page 14

```text
Common business identification for the message.
B. AccountQueryDefinition
Defines the account query criteria.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 14 February 2025
```

