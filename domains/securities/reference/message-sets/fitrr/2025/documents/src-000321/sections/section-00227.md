---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.3 AgriculturalCommodityLiveStock1", "22.1.2.3.2 SubProduct <SubPdct>"]
file_pages: [277]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.3.2 SubProduct <SubPdct>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 277 to 277.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 277

```text
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType1Code" on page 422
CodeName Name Definition
AGRI Agricultural Commodity of type agricultural.
22.1.2.3.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType22Code" on page 425
CodeName Name Definition
LSTK Livestock Commodity of type livestock.
22.1.2.4  FreightCommodityContainerShip1
Definition: Defines commodity sub-product attributes of a freight derivative of type container ships.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 277
   SubProduct <SubPdct> [1..1] CodeSet 277
22.1.2.4.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType4Code" on page 423
CodeName Name Definition
FRGT Freight Commodity of type freight.
22.1.2.4.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType46Code" on page 429
CodeName Name Definition
CSHP ContainerShip Commodity of type container ships.
22.1.2.5  AgriculturalCommodityOilSeed1
Definition: Defines commodity sub-product attributes of an agricultural derivative of type oil seed.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
277 July 2025
```

