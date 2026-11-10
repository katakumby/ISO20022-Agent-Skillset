---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.36 AgriculturalCommodityOliveOil1"]
file_pages: [310]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.36 AgriculturalCommodityOliveOil1

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 310 to 310.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 310

```text
22.1.2.36  AgriculturalCommodityOliveOil1
Definition: Defines commodity sub-product attributes of an agricultural derivative of type olive oil.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 310
   SubProduct <SubPdct> [1..1] CodeSet 310
   AdditionalSubProduct <AddtlSubPdct> [0..1] CodeSet 310
22.1.2.36.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType1Code" on page 422
CodeName Name Definition
AGRI Agricultural Commodity of type agricultural.
22.1.2.36.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType3Code" on page 428
CodeName Name Definition
OOLI OliveOil Commodity of type olive oil.
22.1.2.36.3  AdditionalSubProduct <AddtlSubPdct>
Presence: [0..1]
Definition: Further subproduct type related to instruments that have a non-financial instrument or
commodity as underlying.
Datatype: "AssetClassDetailedSubProductType4Code" on page 419
CodeName Name Definition
LAMP Lampante Commodity attribute of type lampante.
22.1.2.37  AssetClassCommodityInflation1
Definition: Defines commodity attributes of a derivative where the type is inflation.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 310
22.1.2.37.1  BaseProduct <BasePdct>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
310 July 2025
```

