---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.9 Currency Exchange", "7.1.9.1 ForeignExchangeTerms18", "7.1.9.1.1 UnitCurrency <UnitCcy>"]
file_pages: [260]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.9.1.1 UnitCurrency <UnitCcy>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 260 to 260.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 260

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 260
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 260
   ExchangeRate <XchgRate> [1..1] Rate 260
   ConvertedAmount <ConvtdAmt> [1..1] Amount C1, C9 261
7.1.9.1.1  UnitCurrency <UnitCcy>
Presence: [1..1]
Definition: Currency in which the rate of exchange is expressed in a currency exchange. In the example
1GBP = xxxCUR, the unit currency is GBP.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 613
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
7.1.9.1.2  QuotedCurrency <QtdCcy>
Presence: [1..1]
Definition: Currency into which the base currency is converted, in a currency exchange.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 613
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
7.1.9.1.3  ExchangeRate <XchgRate>
Presence: [1..1]
Definition: Factor used for the conversion of an amount from one currency into another. This reflects the
price at which one currency was bought with another currency.
Usage: ExchangeRate expresses the ratio between UnitCurrency and QuotedCurrency (ExchangeRate
= UnitCurrency/QuotedCurrency).
Datatype: "BaseOneRate" on page 666
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 260 February 2025
```

