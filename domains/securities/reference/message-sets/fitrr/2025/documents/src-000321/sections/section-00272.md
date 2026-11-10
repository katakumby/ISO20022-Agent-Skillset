---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.46 IndustrialProductCommodityManufacturing1"]
file_pages: [322]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.46 IndustrialProductCommodityManufacturing1

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 322 to 322.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 322

```text
22.1.2.46  IndustrialProductCommodityManufacturing1
Definition: Defines commodity sub-product attributes of an industrial product derivative of type
manufacturing.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 322
   SubProduct <SubPdct> [0..1] CodeSet 322
22.1.2.46.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType6Code" on page 423
CodeName Name Definition
INDP IndustrialProduct Commodity of type industrial product.
22.1.2.46.2  SubProduct <SubPdct>
Presence: [0..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType34Code" on page 427
CodeName Name Definition
MFTG Manufacturing Commodity of type manufacturing.
22.1.3 Date Period
22.1.3.1  Period4Choice
Definition: Choice between date and date-time for the specification of a period.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 322
Or   FromDate <FrDt> [1..1] Date 323
Or   ToDate <ToDt> [1..1] Date 323
Or}   FromDateToDate <FrDtToDt> [1..1] ± 323
22.1.3.1.1  Date <Dt>
Presence: [1..1]
Definition: Date period is limited to a single date.
Datatype: "ISODate" on page 449
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
322 July 2025
```

