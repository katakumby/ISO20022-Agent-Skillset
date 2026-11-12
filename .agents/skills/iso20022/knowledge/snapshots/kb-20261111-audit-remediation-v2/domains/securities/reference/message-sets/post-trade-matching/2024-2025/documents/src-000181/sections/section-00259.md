---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.27 AmountOrPercentageRange1", "7.1.19.27.2 Term <Term>", "7.1.19.27.2.1 Operator <Oprtr>"]
file_pages: [317]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.27.2.1 Operator <Oprtr>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 317 to 317.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 317

```text
Definition: Indicates one of the constraints of a range of business values.
Term <Term> contains the following Term1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Operator <Oprtr> [1..1] CodeSet 317
   Value <Val> [1..1]  317
{Or     RateValue <RateVal> [1..1] Rate 317
Or}     AbsoluteValue <AbsVal> [1..1] Quantity 317
7.1.19.27.2.1  Operator <Oprtr>
Presence: [1..1]
Definition: Provides the relationship between a variable and a fixed value.
Datatype: "Operator1Code" on page 636
CodeName Name Definition
SMAL SmallerThan Smaller than.
SMEQ SmallerOrEqualTo Smaller or equal to.
GREA GreaterThan Greater than.
GREQ GreaterOrEqualTo Greater or equal to.
EQAL EqualTo Equal to.
7.1.19.27.2.2  Value <Val>
Presence: [1..1]
Definition: Indicates the value.
Value <Val> contains one of the following RateOrAbsoluteValue1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   RateValue <RateVal> [1..1] Rate 317
Or}   AbsoluteValue <AbsVal> [1..1] Quantity 317
7.1.19.27.2.2.1  RateValue <RateVal>
Presence: [1..1]
Definition: A rate expressed as a percentage.
Datatype: "PercentageRate" on page 667
7.1.19.27.2.2.2  AbsoluteValue <AbsVal>
Presence: [1..1]
Definition: Absolute value determined with a number.
Datatype: "Number" on page 666
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 317 February 2025
```

