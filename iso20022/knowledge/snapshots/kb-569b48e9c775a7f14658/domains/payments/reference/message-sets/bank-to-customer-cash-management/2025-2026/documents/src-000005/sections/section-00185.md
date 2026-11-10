---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14"]
file_pages: [263]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3 camt.053.001.14 BankToCustomerStatementV14

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 263 to 263.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 263

```text
3 camt.053.001.14
BankToCustomerStatementV14
3.1 MessageDefinition Functionality
Scope
The BankToCustomerStatement message is sent by the account servicer to an account owner or to a
party authorised by the account owner to receive the message. It is used to inform the account owner,
or authorised party, of the entries booked to the account, and to provide the owner with balance
information on the account at a given point in time.
Usage
The BankToCustomerStatement message can contain reports for more than one account. It provides
information for cash management and/or reconciliation.
It contains information on booked entries only.
It can include underlying details of transactions that have been included in the entry.
The message is exchanged as defined between the account servicer and the account owner. It
provides information on items that have been booked to the account and also balance information.
Depending on services and schedule agreed between banks and their customers, statements may be
generated and exchanged accordingly, for example for intraday or prior day periods.
It is possible that the receiver of the message is not the account owner, but a party entitled through
arrangement with the account owner to receive the account information (also known as recipient).
Outline
The BankToCustomerStatementV14 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. GroupHeader
Common information for the message.
B. Statement
Reports on booked entries and balances for a cash account.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
263 March 2026
```

