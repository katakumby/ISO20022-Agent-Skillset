---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.9 Currency Exchange", "7.1.9.1 ForeignExchangeTerms18", "7.1.9.1.4 ConvertedAmount <ConvtdAmt>"]
file_pages: [261]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.9.1.4 ConvertedAmount <ConvtdAmt>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 261 to 261.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 261

```text
7.1.9.1.4  ConvertedAmount <ConvtdAmt>
Presence: [1..1]
Definition: Amount following a foreign exchange conversion.
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
7.1.10 Date Period
7.1.10.1  DateTimePeriod2
Definition: Time span defined by a start date and time, and an end date and time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 261
   ToDateTime <ToDtTm> [0..1] DateTime 261
7.1.10.1.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODateTime" on page 662
7.1.10.1.2  ToDateTime <ToDtTm>
Presence: [0..1]
Definition: Date and time at which the range ends.
Datatype: "ISODateTime" on page 662
7.1.11 Date Time
7.1.11.1  TradeDate8Choice
Definition: Choice of format for the trade date.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 261 February 2025
```

