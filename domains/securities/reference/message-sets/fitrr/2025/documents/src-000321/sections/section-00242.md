---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.20 AssetClassCommodityEnvironmental1Choice", "22.1.2.20.2 Weather <Wthr>"]
file_pages: [292]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.20.2 Weather <Wthr>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 292 to 292.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 292

```text
Emissions <Emssns> contains the following elements (see "EnvironmentalCommodityEmission1" on
page 289 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 290
   SubProduct <SubPdct> [1..1] CodeSet 290
   AdditionalSubProduct <AddtlSubPdct> [0..1] CodeSet 290
22.1.2.20.2  Weather <Wthr>
Presence: [1..1]
Definition: Weather environmental commodity derivative.
Weather <Wthr> contains the following elements (see "EnvironmentalCommodityWeather1" on
page 289 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 289
   SubProduct <SubPdct> [1..1] CodeSet 289
22.1.2.20.3  CarbonRelated <CrbnRltd>
Presence: [1..1]
Definition: Carbon related environmental commodity derivative.
CarbonRelated <CrbnRltd> contains the following elements (see
"EnvironmentalCommodityCarbonRelated1" on page 295 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 295
   SubProduct <SubPdct> [1..1] CodeSet 295
22.1.2.21  AssetClassCommodityFertilizer1Choice
Definition: Defines commodity attributes of a derivative where the type is fertilizer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Ammonia <Ammn> [1..1] ± 293
Or   DiammoniumPhosphate <DmmnmPhspht> [1..1] ± 293
Or   Potash <Ptsh> [1..1] ± 293
Or   Sulphur <Slphr> [1..1] ± 293
Or   Urea <Urea> [1..1] ± 294
Or}   UreaAndAmmoniumNitrate <UreaAndAmmnmNtrt> [1..1] ± 294
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
292 July 2025
```

