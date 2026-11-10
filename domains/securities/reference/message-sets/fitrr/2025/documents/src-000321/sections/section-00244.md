---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.21 AssetClassCommodityFertilizer1Choice", "22.1.2.21.5 Urea <Urea>"]
file_pages: [294]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.21.5 Urea <Urea>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 294 to 294.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 294

```text
22.1.2.21.5  Urea <Urea>
Presence: [1..1]
Definition: Urea fertilizer commodity derivative.
Urea <Urea> contains the following elements (see "FertilizerCommodityUrea1" on page 304 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 304
   SubProduct <SubPdct> [1..1] CodeSet 304
22.1.2.21.6  UreaAndAmmoniumNitrate <UreaAndAmmnmNtrt>
Presence: [1..1]
Definition: Urea and ammonium nitrate fertilizer commodity derivative.
UreaAndAmmoniumNitrate <UreaAndAmmnmNtrt> contains the following elements (see
"FertilizerCommodityUreaAndAmmoniumNitrate1" on page 317 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 317
   SubProduct <SubPdct> [1..1] CodeSet 318
22.1.2.22  EnergyCommodityDistillates1
Definition: Defines commodity sub-product attributes of an energy derivative of type distillates.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 294
   SubProduct <SubPdct> [1..1] CodeSet 294
22.1.2.22.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType2Code" on page 422
CodeName Name Definition
NRGY Energy Commodity of type energy.
22.1.2.22.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType25Code" on page 426
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
294 July 2025
```

