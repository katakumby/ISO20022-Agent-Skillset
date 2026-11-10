---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.10 RateAndAmountFormat62Choice", "16.1.22.10.4 RateTypeAndRate <RateTpAndRate>", "16.1.22.10.4.2 Rate <Rate>"]
file_pages: [1115]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.10.4.2 Rate <Rate>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1115 to 1115.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1115

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.22.10.4.2  Rate <Rate>
Presence: [1..1]
Definition: Value expressed as a rate.
Datatype: "Percentage14Rate" on page 1247
16.1.22.11  RateAndAmountFormat61Choice
Definition: Choice of format between a rate or a deemed rate type and rate or an amount or a
unspecified rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1115
Or   Amount <Amt> [1..1] Amount C1 1116
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1116
Or   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  1116
     RateType <RateTp> [1..1]  1116
{Or       Code <Cd> [1..1] CodeSet 1117
Or}       Proprietary <Prtry> [1..1] ± 1117
     Amount <Amt> [1..1] Amount C1 1117
     RateStatus <RateSts> [0..1]  C52 1118
{Or       Code <Cd> [1..1] CodeSet 1118
Or}       Proprietary <Prtry> [1..1] ± 1118
Or}   RateTypeAndRate <RateTpAndRate> [1..1]  1119
     RateType <RateTp> [1..1]  1119
{Or       Code <Cd> [1..1] CodeSet 1119
Or}       Proprietary <Prtry> [1..1] ± 1119
     Rate <Rate> [1..1] Rate 1120
16.1.22.11.1  Rate <Rate>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1115 February 2026
```

