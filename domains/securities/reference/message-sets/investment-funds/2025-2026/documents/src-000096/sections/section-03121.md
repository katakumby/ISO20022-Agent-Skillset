---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.4 Amount", "66.1.4.4 RoundingParameters1"]
file_pages: [4345]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.4.4 RoundingParameters1

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4345 to 4345.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4345

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.4.4  RoundingParameters1
Definition: Parameters applied to a fractional number.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RoundingModulus <RndgMdlus> [0..1] Quantity 4345
   RoundingDirection <RndgDrctn> [1..1] CodeSet 4345
66.1.4.4.1  RoundingModulus <RndgMdlus>
Presence: [0..1]
Definition: Float value specifying the value to which rounding is required, eg, 10 means round to a
multiple of 10 units/shares, 0.5 means round to a multiple of 0.5 units/shares.
Datatype: "DecimalNumber" on page 5400
66.1.4.4.2  RoundingDirection <RndgDrctn>
Presence: [1..1]
Definition: Rounding direction applied to fractional numbers, eg, round up.
Datatype: "RoundingDirection1Code" on page 5358
CodeName Name Definition
RDUP RoundUp Round up to the nearest whole number.
RDWN RoundDown Round down to the nearest whole
number.
STAN RoundToNearest Round up or down to the nearest whole
number.
DIST IssueFraction Do not round.
66.1.5 Balance
66.1.5.1  BalanceQuantity1Choice
Definition: Choice between formats for the balance information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 4346
Or}   QuantityAsDSS <QtyAsDSS> [1..1] ± 4346
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4345 May 2026
```

