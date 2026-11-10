---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.23 CashMovementDetails <CshMvmntDtls>", "7.4.13.23.14 PriceDetails <PricDtls>"]
file_pages: [523]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.23.14 PriceDetails <PricDtls>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 523 to 523.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 523

```text
DeemedRate <DmdRate> contains one of the following elements (see
"RateAndAmountFormat61Choice" on page 1115 for details)
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
7.4.13.23.14  PriceDetails <PricDtls>
Presence: [0..1]
Definition: Provides information about the prices related to a corporate action option.
Impacted by: C30 "GenericCashPricePerProductGuideline"
PriceDetails <PricDtls> contains the following PriceDetails38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 524
   GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 524
   CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 525
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 523 February 2026
```

