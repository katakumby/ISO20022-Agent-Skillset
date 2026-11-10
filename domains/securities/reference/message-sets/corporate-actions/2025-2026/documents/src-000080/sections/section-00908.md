---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.17 RateAndAmountFormat55Choice", "16.1.22.17.3 RateTypeAndRate <RateTpAndRate>", "16.1.22.17.3.2 Rate <Rate>"]
file_pages: [1126]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.17.3.2 Rate <Rate>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1126 to 1126.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1126

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.22.17.3.2  Rate <Rate>
Presence: [1..1]
Definition: Value expressed as a rate.
Datatype: "Percentage14Rate" on page 1247
16.1.22.18  CorporateActionRate122
Definition: Specifies rates of a corporate action.
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
16.1.22.18.1  InterestRate <IntrstRate>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1126 February 2026
```

