---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.23 Price", "82.1.23.7 PriceRateOrAmountOrUnknown2Choice"]
file_pages: [3107]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.23.7 PriceRateOrAmountOrUnknown2Choice

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3107 to 3107.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3107

```text
82.1.23.7  PriceRateOrAmountOrUnknown2Choice
Definition: Choice of formats for the price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 3107
Or   Amount <Amt> [1..1] Amount C1 3107
Or}   UnknownIndicator <UknwnInd> [1..1] Indicator 3107
82.1.23.7.1  Rate <Rate>
Presence: [1..1]
Definition: Price expressed as a rate, that is, percentage.
Datatype: "PercentageRate" on page 3325
82.1.23.7.2  Amount <Amt>
Presence: [1..1]
Definition: Price expressed as a currency and value.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 3209
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
82.1.23.7.3  UnknownIndicator <UknwnInd>
Presence: [1..1]
Definition: Indicates whether the market price is unknown.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
82.1.23.8  TypeOfPrice28Choice
Definition: Choice of format for the type of price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3108
Or}   Proprietary <Prtry> [1..1] ± 3109
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3107 August 2026
```

