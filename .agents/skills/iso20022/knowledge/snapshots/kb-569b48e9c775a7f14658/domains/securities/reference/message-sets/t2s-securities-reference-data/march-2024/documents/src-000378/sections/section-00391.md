---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.10 Miscellaneous", "13.1.10.4 AmountOrPercentageRange1", "13.1.10.4.2 Term <Term>", "13.1.10.4.2.1 Operator <Oprtr>"]
file_pages: [484]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.10.4.2.1 Operator <Oprtr>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 484 to 484.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 484

```text
Term <Term> contains the following Term1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Operator <Oprtr> [1..1] CodeSet 484
   Value <Val> [1..1]  484
{Or     RateValue <RateVal> [1..1] Rate 484
Or}     AbsoluteValue <AbsVal> [1..1] Quantity 484
13.1.10.4.2.1  Operator <Oprtr>
Presence: [1..1]
Definition: Provides the relationship between a variable and a fixed value.
Datatype: "Operator1Code" on page 519
CodeName Name Definition
SMAL SmallerThan Smaller than.
SMEQ SmallerOrEqualTo Smaller or equal to.
GREA GreaterThan Greater than.
GREQ GreaterOrEqualTo Greater or equal to.
EQAL EqualTo Equal to.
13.1.10.4.2.2  Value <Val>
Presence: [1..1]
Definition: Indicates the value.
Value <Val> contains one of the following RateOrAbsoluteValue1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   RateValue <RateVal> [1..1] Rate 484
Or}   AbsoluteValue <AbsVal> [1..1] Quantity 484
13.1.10.4.2.2.1  RateValue <RateVal>
Presence: [1..1]
Definition: A rate expressed as a percentage.
Datatype: "PercentageRate" on page 532
13.1.10.4.2.2.2  AbsoluteValue <AbsVal>
Presence: [1..1]
Definition: Absolute value determined with a number.
Datatype: "Number" on page 532
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 484 March 2024
```

