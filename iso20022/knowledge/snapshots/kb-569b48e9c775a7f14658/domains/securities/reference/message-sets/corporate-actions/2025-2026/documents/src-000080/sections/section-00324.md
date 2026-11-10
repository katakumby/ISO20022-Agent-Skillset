---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.19 RateAndAmountDetails <RateAndAmtDtls>", "7.4.13.19.2 GrossDistributionRate <GrssDstrbtnRate>"]
file_pages: [444]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.19.2 GrossDistributionRate <GrssDstrbtnRate>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 444 to 444.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 444

```text
AdditionalTax <AddtlTax> contains one of the following elements (see
"RateAndAmountFormat57Choice" on page 1123 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1123
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1123
Or}   Amount <Amt> [1..1] Amount C1 1123
7.4.13.19.2  GrossDistributionRate <GrssDstrbtnRate>
Presence: [0..*]
Definition: Distribution rate before tax has been deducted.
GrossDistributionRate <GrssDstrbtnRate> contains one of the following elements (see
"GrossDividendRateFormat36Choice" on page 949 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 949
Or   AmountAndRateStatus <AmtAndRateSts> [1..1]  950
     Amount <Amt> [1..1] Amount C1 950
     RateStatus <RateSts> [1..1] CodeSet 950
Or   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  950
     RateType <RateTp> [1..1]  951
{Or       Code <Cd> [1..1] CodeSet 951
Or}       Proprietary <Prtry> [1..1] ± 952
     Amount <Amt> [1..1] Amount C1 952
     RateStatus <RateSts> [0..1]  C52 952
{Or       Code <Cd> [1..1] CodeSet 953
Or}       Proprietary <Prtry> [1..1] ± 953
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 953
7.4.13.19.3  NetDistributionRate <NetDstrbtnRate>
Presence: [0..*]
Definition: Distribution rate after tax has been deducted.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 444 February 2026
```

