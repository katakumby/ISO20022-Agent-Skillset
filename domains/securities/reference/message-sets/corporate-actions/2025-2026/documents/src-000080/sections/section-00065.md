---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.4 PriceDetails <PricDtls>"]
file_pages: [111]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.4 PriceDetails <PricDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 111 to 111.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 111

```text
RateAndAmountDetails <RateAndAmtDtls> contains the following elements (see
"CorporateActionRate122" on page 1126 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InterestRate <IntrstRate> [0..1] ± 1126
   PercentageSought <PctgSght> [0..1] ± 1127
   RelatedIndex <RltdIndx> [0..1] ± 1127
   Spread <Sprd> [0..1] ± 1127
   BidInterval <BidIntrvl> [0..1] ± 1128
   PreviousFactor <PrvsFctr> [0..1] ± 1128
   NextFactor <NxtFctr> [0..1] ± 1128
   ReinvestmentDiscountRateToMarket
<RinvstmtDscntRateToMkt>
[0..1] ± 1128
   InterestShortfall <IntrstShrtfll> [0..1] ± 1129
   RealisedLoss <RealsdLoss> [0..1] ± 1129
   DeclaredRate <DclrdRate> [0..1] ± 1129
   IndexFactor <IndxFctr> [0..1] ± 1130
Constraints
• DeclaredRateRule
DeclaredRate may only be used if the dividend or interest declared by the issuer is actually paid in a
different currency than the declared one or if the dividend or the interest event makes it possible to
elect amongst multiple currency options.
3.4.10.4  PriceDetails <PricDtls>
Presence: [0..1]
Definition: Provides information about the prices related to a corporate action event.
PriceDetails <PricDtls> contains the following CorporateActionPrice85 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MaximumPrice <MaxPric> [0..1] ± 111
   MinimumPrice <MinPric> [0..1] ± 112
   FirstBidIncrementPrice <FrstBidIncrmtPric> [0..1] ± 112
   LastBidIncrementPrice <LastBidIncrmtPric> [0..1] ± 113
3.4.10.4.1  MaximumPrice <MaxPric>
Presence: [0..1]
Definition: Maximum or cap price at which a holder can bid, for example, on a Dutch auction offer.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 111 February 2026
```

