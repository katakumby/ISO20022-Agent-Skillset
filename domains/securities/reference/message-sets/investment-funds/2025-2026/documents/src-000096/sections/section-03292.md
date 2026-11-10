---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.20 Financial Instrument Quantity", "66.1.20.1 UnitsOrAmount1Choice", "66.1.20.1.1 Amount <Amt>"]
file_pages: [4529]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.20.1.1 Amount <Amt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4529 to 4529.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4529

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1, C13 4529
Or}   Unit <Unit> [1..1] Quantity 4529
66.1.20.1.1  Amount <Amt>
Presence: [1..1]
Definition: Currency and amount of the periodical payments.
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.20.1.2  Unit <Unit>
Presence: [1..1]
Definition: Number of units to be subscribed or withdrawn.
Datatype: "DecimalNumber" on page 5400
66.1.21 Foreign Exchange
66.1.21.1  ForeignExchangeTerms19
Definition: Provides information about the terms of the foreign exchange transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 4529
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 4530
   ExchangeRate <XchgRate> [1..1] Rate 4530
66.1.21.1.1  UnitCurrency <UnitCcy>
Presence: [1..1]
Definition: Currency in which the rate of exchange is expressed in a currency exchange. In the example
1GBP = xxxCUR, the unit currency is GBP.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4529 May 2026
```

