---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.23 Price", "82.1.23.1 Price7", "82.1.23.1.2 Value <Val>"]
file_pages: [3102]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.23.1.2 Value <Val>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3102 to 3102.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3102

```text
Type <Tp> contains one of the following elements (see "YieldedOrValueType1Choice" on page 3025
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Yielded <Yldd> [1..1] Indicator 3025
Or}   ValueType <ValTp> [1..1] CodeSet 3025
82.1.23.1.2  Value <Val>
Presence: [1..1]
Definition: Value of the price, for example, as a currency and value.
Value <Val> contains one of the following elements (see "PriceRateOrAmount3Choice" on page 3102
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 3102
Or}   Amount <Amt> [1..1] Amount C1 3102
82.1.23.2  PriceRateOrAmount3Choice
Definition: Choice of formats for the price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 3102
Or}   Amount <Amt> [1..1] Amount C1 3102
82.1.23.2.1  Rate <Rate>
Presence: [1..1]
Definition: Price expressed as a rate, that is percentage.
Datatype: "PercentageRate" on page 3325
82.1.23.2.2  Amount <Amt>
Presence: [1..1]
Definition: Price expressed as a currency and value.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 3209
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3102 August 2026
```

