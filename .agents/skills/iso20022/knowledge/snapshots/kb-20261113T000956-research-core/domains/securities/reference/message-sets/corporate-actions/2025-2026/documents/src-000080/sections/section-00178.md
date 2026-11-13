---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.25 CashMovementDetails <CshMvmntDtls>", "3.4.11.25.15 PriceDetails <PricDtls>"]
file_pages: [243]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.25.15 PriceDetails <PricDtls>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 243 to 243.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 243

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
3.4.11.25.15  PriceDetails <PricDtls>
Presence: [0..1]
Definition: Provides information about the prices related to a corporate action option.
Impacted by: C42 "GenericCashPricePerProductGuideline"
PriceDetails <PricDtls> contains the following PriceDetails38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 244
   GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 244
   CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 245
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 243 February 2026
```

