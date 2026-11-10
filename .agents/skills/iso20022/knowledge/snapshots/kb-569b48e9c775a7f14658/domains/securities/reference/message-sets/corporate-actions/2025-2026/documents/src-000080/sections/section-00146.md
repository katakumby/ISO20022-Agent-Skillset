---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.25 CashMovementDetails <CshMvmntDtls>", "3.4.11.25.8 PriceCalculationMethod <PricClctnMtd>", "3.4.11.25.8.1 Code <Cd>"]
file_pages: [208]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.25.8.1 Code <Cd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 208 to 208.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 208

```text
3.4.11.25.8.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the method applied for the calculation of the price.
Datatype: "PriceCalculationMethod1Code" on page 1230
CodeName Name Definition
VWAP VolumeWeightedAveragePrice The price is based on a volume-
weighted average price which is a ratio
of the cumulative share price to the
cumulative volume traded over a given
time period.
NAVF FinalAssetValue Final asset value at the liquidation of the
fund.
MIMP MidMarketPrice Price at a certain amount of time prior to
the date it is announced.
NAVA NetAssetValue Net value of an investment fund's assets
less its liabilities, divided by the number
of shares outstanding.
AVCL AverageClosingPrice Price of the asset at close of a given
day.
3.4.11.25.8.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification to specify the method applied for the calculation of the price.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
3.4.11.25.9  CountryOfIncomeSource <CtryOfIncmSrc>
Presence: [0..1]
Definition: Indicates the country from which the income originates.
Impacted by: C17 "Country"
Datatype: "CountryCode" on page 1205
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 208 February 2026
```

