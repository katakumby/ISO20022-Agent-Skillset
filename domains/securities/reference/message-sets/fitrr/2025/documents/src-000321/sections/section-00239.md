---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.16 EnergyCommodityInterEnergy1", "22.1.2.16.2 SubProduct <SubPdct>"]
file_pages: [289]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.16.2 SubProduct <SubPdct>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 289 to 289.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 289

```text
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType2Code" on page 422
CodeName Name Definition
NRGY Energy Commodity of type energy.
22.1.2.16.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType26Code" on page 426
CodeName Name Definition
INRG InterEnergy Commodity of type inter energy.
22.1.2.17  EnvironmentalCommodityWeather1
Definition: Defines commodity sub-product attributes of an environmental derivative of type weather.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 289
   SubProduct <SubPdct> [1..1] CodeSet 289
22.1.2.17.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType3Code" on page 423
CodeName Name Definition
ENVR Environmental Commodity of type environmental.
22.1.2.17.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType30Code" on page 427
CodeName Name Definition
WTHR Weather Commodity of type weather.
22.1.2.18  EnvironmentalCommodityEmission1
Definition: Defines commodity sub-product attributes of an environmental derivative of type emission.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
289 July 2025
```

