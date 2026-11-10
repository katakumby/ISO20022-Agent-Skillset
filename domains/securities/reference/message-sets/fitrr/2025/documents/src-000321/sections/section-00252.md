---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.27 FertilizerCommodityDiammoniumPhosphate1"]
file_pages: [302]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.27 FertilizerCommodityDiammoniumPhosphate1

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 302 to 302.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 302

```text
Other <Othr> contains the following elements (see "AssetClassCommodityOther1" on page 295 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 295
22.1.2.27  FertilizerCommodityDiammoniumPhosphate1
Definition: Defines commodity sub-product attributes of a fertilizer derivative of type diammonium
phosphate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 302
   SubProduct <SubPdct> [1..1] CodeSet 302
22.1.2.27.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType5Code" on page 423
CodeName Name Definition
FRTL Fertilizer Commodity of type fertilizer.
22.1.2.27.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType40Code" on page 428
CodeName Name Definition
DAPH DiammoniumPhosphate Commodity of type diammonium
phosphate.
22.1.2.28  FreightCommodityWet1
Definition: Defines commodity sub-product attributes of a freight derivative of type wet.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 302
   SubProduct <SubPdct> [1..1] CodeSet 303
   AdditionalSubProduct <AddtlSubPdct> [0..1] CodeSet 303
22.1.2.28.1  BaseProduct <BasePdct>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
302 July 2025
```

