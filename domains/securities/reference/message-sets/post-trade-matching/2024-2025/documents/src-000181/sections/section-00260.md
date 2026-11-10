---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.28 QuantityOrAmount2Choice"]
file_pages: [318]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.28 QuantityOrAmount2Choice

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 318 to 318.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 318

```text
7.1.19.28  QuantityOrAmount2Choice
Definition: Choice between a quantity expressed in units, face amount or amortised amount and a
quantity expressed as an amount.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 318
Or}   Amount <Amt> [1..1] Amount C1, C9 318
7.1.19.28.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity is expressed in units, face amount or amortised amount.
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantity1Choice" on
page 272 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 273
Or   FaceAmount <FaceAmt> [1..1] Amount 273
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 273
7.1.19.28.2  Amount <Amt>
Presence: [1..1]
Definition: Quantity is expressed as an amount.
Impacted by: C1 "ActiveCurrency", C9 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 611
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
7.1.19.29  BusinessProcessType2Choice
Definition: Choice between a code or a data source scheme to determine the business process type.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 318 February 2025
```

