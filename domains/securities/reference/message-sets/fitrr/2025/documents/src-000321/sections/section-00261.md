---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.38 FreightCommodityDry1"]
file_pages: [311]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.38 FreightCommodityDry1

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 311 to 311.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 311

```text
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType12Code" on page 422
CodeName Name Definition
INFL Inflation Commodity of type inflation.
22.1.2.38  FreightCommodityDry1
Definition: Defines commodity sub-product attributes of a freight derivative of type dry.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 311
   SubProduct <SubPdct> [1..1] CodeSet 311
   AdditionalSubProduct <AddtlSubPdct> [0..1] CodeSet 311
22.1.2.38.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType4Code" on page 423
CodeName Name Definition
FRGT Freight Commodity of type freight.
22.1.2.38.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType31Code" on page 427
CodeName Name Definition
DRYF Dry Commodity of type dry freight.
22.1.2.38.3  AdditionalSubProduct <AddtlSubPdct>
Presence: [0..1]
Definition: Further subproduct type related to instruments that have a non-financial instrument or
commodity as underlying.
Datatype: "AssetClassDetailedSubProductType14Code" on page 418
CodeName Name Definition
DBCR DryBulkCarrier Commodity attribute of type dry bulk
carrier.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
311 July 2025
```

