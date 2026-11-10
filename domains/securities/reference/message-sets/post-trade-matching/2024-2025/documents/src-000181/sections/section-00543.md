---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.24 CreditDebitCode"]
file_pages: [623]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.24 CreditDebitCode

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 623 to 623.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 623

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.2.2.24  CreditDebitCode
Definition: Specifies if an operation is an increase or a decrease.
Type: CodeSet
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
7.2.2.25  DateType2Code
Definition: Specifies when date is open.
Type: CodeSet
CodeName Name Definition
OPEN Open Open-dated, which indicates that the
date has not been established.
7.2.2.26  DateType3Code
Definition: Specifies a type of date.
Type: CodeSet
CodeName Name Definition
VARI Various Partial trades have occurred over a
period of two or more days.
7.2.2.27  DeliveryReceiptType2Code
Definition: Specifies how the transaction is to be settled.
Type: CodeSet
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
7.2.2.28  DeliveryType2Code
Definition: Describes the delivery or custody arrangement for the underlying securities.
Type: CodeSet
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 623 February 2025
```

