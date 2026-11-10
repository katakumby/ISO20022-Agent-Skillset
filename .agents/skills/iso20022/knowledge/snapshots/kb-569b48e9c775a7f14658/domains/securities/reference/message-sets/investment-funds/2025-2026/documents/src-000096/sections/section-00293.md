---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02"]
file_pages: [408, 409]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.006.001.02"]
---

# 22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 408 to 409.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 408

```text
22 semt.006.001.02
StatementOfInvestmentFundTransactionsV02
22.1 MessageDefinition Functionality
Scope
An account servicer, for example, a transfer agent sends the StatementOfInvestmentFundTransactions
message to the account owner, for example, an investment manager or its authorised representative to
provide detailed transactions (increases and decreases) of holdings which occurred during a specified
period of time.
Usage
The StatementOfInvestmentFundTransactions message is used to list the holdings transactions of a
single (master) account or several sub-accounts.
This message should be used at a frequency agreed bi-laterally between the account servicer and the
account owner.
This message must not be used in place of confirmation messages.
Outline
The StatementOfInvestmentFundTransactionsV02 MessageDefinition is composed of 9
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies a message from a business application standpoint.
B. PreviousReference
Reference to a linked message that was previously sent.
C. RelatedReference
Reference to a linked message that was previously received.
D. MessagePagination
Pagination of the message.
E. StatementGeneralDetails
General information related to the investment fund statement of transactions.
F. InvestmentAccountDetails
Information related to an investment account.
G. TransactionOnAccount
Creation/cancellation of investment units on the books of the fund or its designated agent, as a
result of executing an investment fund order.
H. SubAccountDetails
The sub-account of the safekeeping or investment account.
Approved by the Securities SEG on 27 January 2026 semt.006.001.02
StatementOfInvestmentFundTransactionsV02
Investment Funds - Maintenance 2025 - 2026 408 May 2026
```

## File page 409

```text
I. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 semt.006.001.02
StatementOfInvestmentFundTransactionsV02
Investment Funds - Maintenance 2025 - 2026 409 May 2026
```

