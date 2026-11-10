---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.34 Price", "66.1.34.6 PriceRateOrAmountOrUnknownChoice"]
file_pages: [5117]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.34.6 PriceRateOrAmountOrUnknownChoice

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5117 to 5117.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5117

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.34.6  PriceRateOrAmountOrUnknownChoice
Definition: Choice of formats for the price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 5117
Or   Amount <Amt> [1..1] Amount C2 5117
Or}   UnknownIndicator <UknwnInd> [1..1] Indicator 5117
66.1.34.6.1  Rate <Rate>
Presence: [1..1]
Definition: Price expressed as a rate, ie, percentage.
Datatype: "PercentageRate" on page 5401
66.1.34.6.2  Amount <Amt>
Presence: [1..1]
Definition: Price expressed as a currency and value.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
66.1.34.6.3  UnknownIndicator <UknwnInd>
Presence: [1..1]
Definition: Indicates whether the market price is unknown.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5117 May 2026
```

