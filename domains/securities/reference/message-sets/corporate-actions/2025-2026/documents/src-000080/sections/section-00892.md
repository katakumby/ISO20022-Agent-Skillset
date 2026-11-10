---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.9 InterestRateUsedForPaymentFormat12Choice", "16.1.22.9.3 RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts>", "16.1.22.9.3.3 RateStatus <RateSts>", "16.1.22.9.3.3.2 Proprietary <Prtry>"]
file_pages: [1110]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.9.3.3.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1110 to 1110.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1110

```text
Datatype: "RateStatus1Code" on page 1234
CodeName Name Definition
ACTU ActualRate Rate is actual.
INDI IndicativeRate Rate is indicative.
16.1.22.9.3.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the status of the rate.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.22.10  RateAndAmountFormat62Choice
Definition: Choice of format between a rate or a deemed rate type and rate or an amount or a
unspecified rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1111
Or   Amount <Amt> [1..1] Amount C1 1111
Or   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  1111
     RateType <RateTp> [1..1]  1111
{Or       Code <Cd> [1..1] CodeSet 1112
Or}       Proprietary <Prtry> [1..1] ± 1112
     Amount <Amt> [1..1] Amount C1 1112
     RateStatus <RateSts> [0..1]  C52 1113
{Or       Code <Cd> [1..1] CodeSet 1113
Or}       Proprietary <Prtry> [1..1] ± 1113
Or}   RateTypeAndRate <RateTpAndRate> [1..1]  1113
     RateType <RateTp> [1..1]  1114
{Or       Code <Cd> [1..1] CodeSet 1114
Or}       Proprietary <Prtry> [1..1] ± 1114
     Rate <Rate> [1..1] Rate 1115
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1110 February 2026
```

