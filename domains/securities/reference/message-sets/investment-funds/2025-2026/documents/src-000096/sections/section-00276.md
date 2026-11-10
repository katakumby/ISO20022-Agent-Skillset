---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["19 semt.003.001.02 AccountingStatementOfHoldingsV02"]
file_pages: [387, 388]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.02"]
---

# 19 semt.003.001.02 AccountingStatementOfHoldingsV02

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 387 to 388.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 387

```text
19 semt.003.001.02
AccountingStatementOfHoldingsV02
19.1 MessageDefinition Functionality
Scope
An account servicer, for example, a transfer agent sends the AccountStatementOfHoldings message to
the account owner, for example, a fund manager or an account owner's designated agent to provide
detailed holdings of the portfolio at a specified moment in time.
The message provides, at a moment in time, valuations of the portfolio together with details of each
financial instrument holding.
The message can be sent either audited or un-audited and may be provided on a trade date or
settlement date basis.
Usage
The AccountingStatementOfHoldings message is used to provide valuation detail for each financial
instrument held in a portfolio. The message should be sent at a frequency agreed bi-laterally between
the account servicer and the account owner.
This message can only be used to list the holdings of a single (master) account. However, it is possible
to break down these holdings into one or several sub-accounts. Therefore, the message can be used to
either specify holdings at
- the main account level, or,
- the sub-account level.
This message can be used to report where the financial instruments are safe-kept, physically or
notionally. If a security is held in more than one safekeeping place, this can also be indicated.
The AccountingStatementOfHoldings message should not be used for trading purposes.
Outline
The AccountingStatementOfHoldingsV02 MessageDefinition is composed of 10
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies a message from a business application standpoint.
B. PreviousReference
Reference to a linked message that was previously sent.
C. RelatedReference
Reference to a linked message that was previously received.
D. MessagePagination
Pagination of the message.
Approved by the Securities SEG on 27 January 2026 semt.003.001.02
AccountingStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 387 May 2026
```

## File page 388

```text
E. StatementGeneralDetails
General information related to the accounting statement of holdings.
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
Approved by the Securities SEG on 27 January 2026 semt.003.001.02
AccountingStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 388 May 2026
```

