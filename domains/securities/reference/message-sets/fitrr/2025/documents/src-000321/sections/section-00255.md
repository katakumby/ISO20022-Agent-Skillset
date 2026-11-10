---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.32 EnergyCommodityCoal1"]
file_pages: [305]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.32 EnergyCommodityCoal1

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 305 to 305.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 305

```text
CodeName Name Definition
UREA Urea Commodity of type urea.
22.1.2.32  EnergyCommodityCoal1
Definition: Defines commodity sub-product attributes of an energy derivative of type coal.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 305
   SubProduct <SubPdct> [1..1] CodeSet 305
22.1.2.32.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType2Code" on page 422
CodeName Name Definition
NRGY Energy Commodity of type energy.
22.1.2.32.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType24Code" on page 425
CodeName Name Definition
COAL Coal Commodity of type coal.
22.1.2.33  AssetClassCommodityEnergy1Choice
Definition: Defines commodity attributes of a derivative where the type is energy.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Electricity <Elctrcty> [1..1] ± 306
Or   NaturalGas <NtrlGas> [1..1] ± 306
Or   Oil <Oil> [1..1] ± 306
Or   Coal <Coal> [1..1] ± 306
Or   InterEnergy <IntrNrgy> [1..1] ± 307
Or   RenewableEnergy <RnwblNrgy> [1..1] ± 307
Or   LightEnd <LghtEnd> [1..1] ± 307
Or}   Distillates <Dstllts> [1..1] ± 307
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
305 July 2025
```

