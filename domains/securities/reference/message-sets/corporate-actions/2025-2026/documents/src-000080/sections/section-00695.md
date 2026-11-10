---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous"]
file_pages: [886]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15 Miscellaneous

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 886 to 886.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 886

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15 Miscellaneous
16.1.15.1  RateAndAmountFormat56Choice
Definition: Choice of format between a rate or a rate type and rate or an amount or a unspecified rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 886
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 886
Or   Amount <Amt> [1..1] Amount C1 886
Or}   RateTypeAndRate <RateTpAndRate> [1..1]  887
     RateType <RateTp> [1..1]  887
{Or       Code <Cd> [1..1] CodeSet 887
Or}       Proprietary <Prtry> [1..1] ± 888
     Rate <Rate> [1..1] Rate 888
16.1.15.1.1  Rate <Rate>
Presence: [1..1]
Definition: Value expressed as a rate.
Datatype: "Percentage14Rate" on page 1247
16.1.15.1.2  NotSpecifiedRate <NotSpcfdRate>
Presence: [1..1]
Definition: Value of the rate not specified.
Datatype: "RateValueType7Code" on page 1235
CodeName Name Definition
UKWN Unknown Rate is unknown by the sender or has
not been established.
16.1.15.1.3  Amount <Amt>
Presence: [1..1]
Definition: Value is expressed as a currency and amount.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 886 February 2026
```

