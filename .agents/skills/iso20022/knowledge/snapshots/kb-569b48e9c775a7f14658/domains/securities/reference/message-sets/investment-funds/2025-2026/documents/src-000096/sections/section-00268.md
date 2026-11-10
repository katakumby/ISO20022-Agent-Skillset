---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["18 semt.002.001.02 CustodyStatementOfHoldingsV02"]
file_pages: [375, 376]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.02"]
---

# 18 semt.002.001.02 CustodyStatementOfHoldingsV02

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 375 to 376.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 375

```text
18 semt.002.001.02
CustodyStatementOfHoldingsV02
18.1 MessageDefinition Functionality
Scope
An account servicer, for example, a transfer agent sends the CustodyStatementOfHoldings message to
the account owner, for example, a fund manager or an account owner's designated agent to provide
detailed holdings of the portfolio at a specified moment in time.
The message provides, at a moment in time, the quantity and identification of the financial instruments
that the account servicer holds for the account owner. The message can also include availability and
the location of holdings to facilitate trading and minimise settlement issues.
The message reports all information per financial instrument, ie, when a financial instrument is held at
multiple places of safekeeping, the total holdings for all locations can be provided.
Usage
The CustodyStatementOfHoldings message is used to provide detailed quantity and availability
information for financial instrument holdings of a portfolio. The message should be sent at a frequency
agreed bi-laterally between the account servicer and the account owner.
This message can be also be used to report where the financial instruments are safe-kept, physically or
notionally. If a security is held in more than one safekeeping place, this can also be indicated.
This message can reflect all outstanding holding information or may only contain changes since the
previously sent statement.
The CustodyStatementOfHoldings message can only be used to list the holdings of a single (master)
account. However, it is possible to break down these holdings into one or several sub-accounts.
Therefore, this message can be used to either specify holdings at
- the main account level, or,
- the sub-account level.
Outline
The CustodyStatementOfHoldingsV02 MessageDefinition is composed of 10 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies a message from a business application standpoint.
B. PreviousReference
Reference to a linked message that was previously sent.
C. RelatedReference
Reference to a linked message that was previously received.
D. MessagePagination
Pagination of the message.
Approved by the Securities SEG on 27 January 2026 semt.002.001.02 CustodyStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 375 May 2026
```

## File page 376

```text
E. StatementGeneralDetails
General information related to the custody statement of holdings.
F. AccountDetails
The safekeeping or investment account.
G. BalanceForAccount
Net position of a segregated holding, in a single security, within the overall position held in a
securities account.
H. SubAccountDetails
The sub-account of the safekeeping or investment account.
I. TotalValues
Value of total holdings reported.
J. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 semt.002.001.02 CustodyStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 376 May 2026
```

