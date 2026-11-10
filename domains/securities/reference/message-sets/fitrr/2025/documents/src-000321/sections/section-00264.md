---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.39 AssetClassCommodityPaper1Choice", "22.1.2.39.3 Pulp <Pulp>", "22.1.2.39.3.2 SubProduct <SubPdct>"]
file_pages: [314]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.39.3.2 SubProduct <SubPdct>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 314 to 314.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 314

```text
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType8Code" on page 423
CodeName Name Definition
PAPR Paper Commodity of type paper.
22.1.2.39.3.2  SubProduct <SubPdct>
Presence: [0..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType37Code" on page 428
CodeName Name Definition
PULP Pulp Commodity of type pulp.
22.1.2.39.4  RecoveredPaper <RcvrdPpr>
Presence: [1..1]
Definition: Recovered paper commodity derivative.
RecoveredPaper <RcvrdPpr> contains the following PaperCommodityRecoveredPaper1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 314
   SubProduct <SubPdct> [0..1] CodeSet 314
22.1.2.39.4.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType8Code" on page 423
CodeName Name Definition
PAPR Paper Commodity of type paper.
22.1.2.39.4.2  SubProduct <SubPdct>
Presence: [0..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType38Code" on page 428
CodeName Name Definition
RCVP RecoveredPaper Commodity of type recovered paper.
22.1.2.40  AgriculturalCommodityPotato1
Definition: Defines commodity sub-product attributes of an agricultural derivative of type potato.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
314 July 2025
```

