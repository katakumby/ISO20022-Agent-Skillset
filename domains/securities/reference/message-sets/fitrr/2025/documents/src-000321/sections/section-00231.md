---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.9 EnergyCommodityElectricity1", "22.1.2.9.1 BaseProduct <BasePdct>"]
file_pages: [281]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.9.1 BaseProduct <BasePdct>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 281 to 281.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 281

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 281
   SubProduct <SubPdct> [1..1] CodeSet 281
   AdditionalSubProduct <AddtlSubPdct> [1..1] CodeSet 281
22.1.2.9.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType2Code" on page 422
CodeName Name Definition
NRGY Energy Commodity of type energy.
22.1.2.9.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType6Code" on page 430
CodeName Name Definition
ELEC Electricity Commodity of type electricity.
22.1.2.9.3  AdditionalSubProduct <AddtlSubPdct>
Presence: [1..1]
Definition: Further subproduct type related to instruments that have a non-financial instrument or
commodity as underlying.
Datatype: "AssetClassDetailedSubProductType5Code" on page 420
CodeName Name Definition
BSLD BaseLoad Commodity attribute of type base load.
FITR FinancialTransmissionRights Commodity attribute of type financial
transmission rights.
PKLD PeakLoad Commodity attribute of type peak load.
OFFP OffPeak Commodity attribute of type off-peak.
OTHR Other Commodity attribute of other type.
22.1.2.10  FertilizerCommodityPotash1
Definition: Defines commodity sub-product attributes of a fertilizer derivative of type potash.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
281 July 2025
```

