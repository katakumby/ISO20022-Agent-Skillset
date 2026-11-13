---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.22 PriceDetails <PricDtls>"]
file_pages: [163]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.22 PriceDetails <PricDtls>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 163 to 163.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 163

```text
Definition: Acceptable price increment used for submitting a bid.
BidInterval <BidIntrvl> contains one of the following elements (see "RateAndAmountFormat58Choice"
on page 1121 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1122
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1122
Or   Amount <Amt> [1..1] Amount C1 1122
Or}   IndexPoints <IndxPts> [1..1] Quantity 1122
3.4.11.22  PriceDetails <PricDtls>
Presence: [0..1]
Definition: Provides information about the prices related to a corporate action option.
PriceDetails <PricDtls> contains the following CorporateActionPrice87 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 163
   OverSubscriptionDepositPrice <OverSbcptDpstPric> [0..1] ± 164
   MaximumCashToInstruct <MaxCshToInst> [0..1] ± 164
   MinimumCashToInstruct <MinCshToInst> [0..1] ± 164
   MinimumMultipleCashToInstruct <MinMltplCshToInst> [0..1] ± 165
   MaximumPrice <MaxPric> [0..1] ± 165
   MinimumPrice <MinPric> [0..1] ± 165
   FirstBidIncrementPrice <FrstBidIncrmtPric> [0..1] ± 166
   LastBidIncrementPrice <LastBidIncrmtPric> [0..1] ± 166
3.4.11.22.1  CashInLieuOfSharePrice <CshInLieuOfShrPric>
Presence: [0..1]
Definition: Cash disbursement in lieu of equities; usually in lieu of fractional quantity.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 163 February 2026
```

