---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.10 Miscellaneous", "13.1.10.4 AmountOrPercentageRange1"]
file_pages: [483]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.10.4 AmountOrPercentageRange1

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 483 to 483.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 483

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.10.4  AmountOrPercentageRange1
Definition: Provides constrains on a range of business values.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Operation <Opr> [0..1] CodeSet 483
   Term <Term> [0..10]  483
     Operator <Oprtr> [1..1] CodeSet 484
     Value <Val> [1..1]  484
{Or       RateValue <RateVal> [1..1] Rate 484
Or}       AbsoluteValue <AbsVal> [1..1] Quantity 484
13.1.10.4.1  Operation <Opr>
Presence: [0..1]
Definition: Indication of the relationship between two variables.
Datatype: "Operation1Code" on page 519
CodeName Name Definition
TILL Till Indicates a range delimited by two
variables.
ORRR Or Indicates either of two variables is valid,
but not both.
ANDD And Indicates that only when both variables
are given, the operation is valid.
13.1.10.4.2  Term <Term>
Presence: [0..10]
Definition: Indicates one of the constraints of a range of business values.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 483 March 2024
```

