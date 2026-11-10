---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.23 AmountOrPercentageRange1", "82.1.19.23.2 Term <Term>", "82.1.19.23.2.2 Value <Val>"]
file_pages: [3004]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.23.2.2 Value <Val>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3004 to 3004.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3004

```text
Datatype: "Operator1Code" on page 3265
CodeName Name Definition
SMAL SmallerThan Smaller than.
SMEQ SmallerOrEqualTo Smaller or equal to.
GREA GreaterThan Greater than.
GREQ GreaterOrEqualTo Greater or equal to.
EQAL EqualTo Equal to.
82.1.19.23.2.2  Value <Val>
Presence: [1..1]
Definition: Indicates the value.
Value <Val> contains one of the following RateOrAbsoluteValue1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   RateValue <RateVal> [1..1] Rate 3004
Or}   AbsoluteValue <AbsVal> [1..1] Quantity 3004
82.1.19.23.2.2.1  RateValue <RateVal>
Presence: [1..1]
Definition: A rate expressed as a percentage.
Datatype: "PercentageRate" on page 3325
82.1.19.23.2.2.2  AbsoluteValue <AbsVal>
Presence: [1..1]
Definition: Absolute value determined with a number.
Datatype: "Number" on page 3324
82.1.19.24  RateAndAmountFormat1Choice
Definition: Choice of format between rate, amount and not specified.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 3004
Or   Amount <Amt> [1..1] Amount C1, C4 3005
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1]  3005
{Or     Code <Cd> [1..1] CodeSet 3005
Or}     Proprietary <Prtry> [1..1] ± 3005
82.1.19.24.1  Rate <Rate>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3004 August 2026
```

