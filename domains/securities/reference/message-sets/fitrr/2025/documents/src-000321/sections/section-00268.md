---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.43 FertilizerCommodityUreaAndAmmoniumNitrate1", "22.1.2.43.2 SubProduct <SubPdct>"]
file_pages: [318]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.43.2 SubProduct <SubPdct>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 318 to 318.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 318

```text
22.1.2.43.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType44Code" on page 429
CodeName Name Definition
UAAN UreaAndAmmoniumNitrite Commodity of type urea and ammonium
nitrite.
22.1.2.44  AssetClassCommodityAgricultural1Choice
Definition: Defines commodity attributes of a derivative where the type is agricultural.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   GrainOilSeed <GrnOilSeed> [1..1] ± 318
Or   Soft <Soft> [1..1] ± 318
Or   Potato <Ptt> [1..1] ± 319
Or   OliveOil <OlvOil> [1..1] ± 319
Or   Dairy <Dairy> [1..1] ± 319
Or   Forestry <Frstry> [1..1] ± 319
Or   Seafood <Sfd> [1..1] ± 320
Or   LiveStock <LiveStock> [1..1] ± 320
Or}   Grain <Grn> [1..1] ± 320
22.1.2.44.1  GrainOilSeed <GrnOilSeed>
Presence: [1..1]
Definition: Grain oil seed agricultural commodity derivative.
GrainOilSeed <GrnOilSeed> contains the following elements (see "AgriculturalCommodityOilSeed1"
on page 277 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 278
   SubProduct <SubPdct> [1..1] CodeSet 278
   AdditionalSubProduct <AddtlSubPdct> [1..1] CodeSet 278
22.1.2.44.2  Soft <Soft>
Presence: [1..1]
Definition: Soft agricultural commodity derivative.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
318 July 2025
```

