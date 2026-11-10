---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.28 FreightCommodityWet1", "22.1.2.28.2 SubProduct <SubPdct>"]
file_pages: [303]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.28.2 SubProduct <SubPdct>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 303 to 303.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 303

```text
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType4Code" on page 423
CodeName Name Definition
FRGT Freight Commodity of type freight.
22.1.2.28.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType32Code" on page 427
CodeName Name Definition
WETF Wet Commodity of type wet freight.
22.1.2.28.3  AdditionalSubProduct <AddtlSubPdct>
Presence: [0..1]
Definition: Further subproduct type related to instruments that have a non-financial instrument or
commodity as underlying.
Datatype: "AssetClassDetailedSubProductType12Code" on page 418
CodeName Name Definition
TNKR Tanker Commodity attribute of type tanker.
22.1.2.29  AgriculturalCommodityForestry1
Definition: Defines commodity sub-product attributes of an agricultural derivative of type forestry.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 303
   SubProduct <SubPdct> [1..1] CodeSet 303
22.1.2.29.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType1Code" on page 422
CodeName Name Definition
AGRI Agricultural Commodity of type agricultural.
22.1.2.29.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
303 July 2025
```

