---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.2 AssetClassCommodityIndustrialProduct1Choice"]
file_pages: [276]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.2 AssetClassCommodityIndustrialProduct1Choice

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 276 to 276.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 276

```text
CodeName Name Definition
MCEX MultiCommodityExotic Commodity of type multi commodity
exotic.
22.1.2.2  AssetClassCommodityIndustrialProduct1Choice
Definition: Defines commodity attributes of a derivative where the type is industrial product.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Construction <Cnstrctn> [1..1] ± 276
Or}   Manufacturing <Manfctg> [1..1] ± 276
22.1.2.2.1  Construction <Cnstrctn>
Presence: [1..1]
Definition: Construction related industrial product commodity derivative.
Construction <Cnstrctn> contains the following elements (see
"IndustrialProductCommodityConstruction1" on page 288 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 288
   SubProduct <SubPdct> [0..1] CodeSet 288
22.1.2.2.2  Manufacturing <Manfctg>
Presence: [1..1]
Definition: Manufacturing related industrial product commodity derivative.
Manufacturing <Manfctg> contains the following elements (see
"IndustrialProductCommodityManufacturing1" on page 322 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 322
   SubProduct <SubPdct> [0..1] CodeSet 322
22.1.2.3  AgriculturalCommodityLiveStock1
Definition: Defines commodity sub-product attributes of an agricultural derivative of type livestock.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 276
   SubProduct <SubPdct> [1..1] CodeSet 277
22.1.2.3.1  BaseProduct <BasePdct>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
276 July 2025
```

