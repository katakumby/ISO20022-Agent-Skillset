---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.75 RateAndAmountFormat60Choice", "16.1.15.75.4 RateTypeAndRate <RateTpAndRate>", "16.1.15.75.4.1 RateType <RateTp>", "16.1.15.75.4.1.2 Proprietary <Prtry>"]
file_pages: [1028]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.75.4.1.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1028 to 1028.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1028

```text
CodeName Name Definition
FTCA FATCATax Withholding tax related to income
subject to FATCA (Foreign Account Tax
Compliance Act).
NRAT NRATax Withholding tax related to income
subject to NRA (Non Resident Alien).
16.1.15.75.4.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of withholding tax rate.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.75.4.2  Rate <Rate>
Presence: [1..1]
Definition: Value expressed as a rate.
Datatype: "Percentage14Rate" on page 1247
16.1.15.76  InterestRateUsedForPaymentFormat11Choice
Definition: Choice between an amount or a rate or an unspecified rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1029
Or   Amount <Amt> [1..1] Amount C1 1029
Or   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  1029
     RateType <RateTp> [1..1]  1029
{Or       Code <Cd> [1..1] CodeSet 1030
Or}       Proprietary <Prtry> [1..1] ± 1030
     Amount <Amt> [1..1] Amount C1 1030
     RateStatus <RateSts> [0..1]  C52 1030
{Or       Code <Cd> [1..1] CodeSet 1031
Or}       Proprietary <Prtry> [1..1] ± 1031
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1031
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1028 February 2026
```

