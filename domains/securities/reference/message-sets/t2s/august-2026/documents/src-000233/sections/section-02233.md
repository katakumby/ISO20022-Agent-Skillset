---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.23 AmountOrPercentageRange1"]
file_pages: [3003]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.23 AmountOrPercentageRange1

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3003 to 3003.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3003

```text
Datatype: "ISODateTime" on page 3320
82.1.19.23  AmountOrPercentageRange1
Definition: Provides constrains on a range of business values.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Operation <Opr> [0..1] CodeSet 3003
   Term <Term> [0..10]  3003
     Operator <Oprtr> [1..1] CodeSet 3003
     Value <Val> [1..1]  3004
{Or       RateValue <RateVal> [1..1] Rate 3004
Or}       AbsoluteValue <AbsVal> [1..1] Quantity 3004
82.1.19.23.1  Operation <Opr>
Presence: [0..1]
Definition: Indication of the relationship between two variables.
Datatype: "Operation1Code" on page 3265
CodeName Name Definition
TILL Till Indicates a range delimited by two
variables.
ORRR Or Indicates either of two variables is valid,
but not both.
ANDD And Indicates that only when both variables
are given, the operation is valid.
82.1.19.23.2  Term <Term>
Presence: [0..10]
Definition: Indicates one of the constraints of a range of business values.
Term <Term> contains the following Term1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Operator <Oprtr> [1..1] CodeSet 3003
   Value <Val> [1..1]  3004
{Or     RateValue <RateVal> [1..1] Rate 3004
Or}     AbsoluteValue <AbsVal> [1..1] Quantity 3004
82.1.19.23.2.1  Operator <Oprtr>
Presence: [1..1]
Definition: Provides the relationship between a variable and a fixed value.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3003 August 2026
```

