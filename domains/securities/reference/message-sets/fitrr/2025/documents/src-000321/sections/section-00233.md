---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.11 AssetClassCommodityMetal1Choice", "22.1.2.11.1 NonPrecious <NonPrcs>", "22.1.2.11.1.1 BaseProduct <BasePdct>"]
file_pages: [283]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.11.1.1 BaseProduct <BasePdct>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 283 to 283.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 283

```text
NonPrecious <NonPrcs> contains the following MetalCommodityNonPrecious1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 283
   SubProduct <SubPdct> [1..1] CodeSet 283
   AdditionalSubProduct <AddtlSubPdct> [1..1] CodeSet 283
22.1.2.11.1.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType7Code" on page 423
CodeName Name Definition
METL Metal Commodity of type metal.
22.1.2.11.1.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType15Code" on page 424
CodeName Name Definition
NPRM NonPrecious Commodity of type non precious metals.
22.1.2.11.1.3  AdditionalSubProduct <AddtlSubPdct>
Presence: [1..1]
Definition: Further subproduct type related to instruments that have a non-financial instrument or
commodity as underlying.
Datatype: "AssetClassDetailedSubProductType10Code" on page 417
CodeName Name Definition
ALUM Aluminium Commodity attribute of type aluminium.
ALUA AluminiumAlloy Commodity attribute of type aluminium
alloy.
CBLT Cobalt Commodity attribute of type cobalt.
COPR Copper Commodity attribute of type copper.
IRON IronOre Commodity attribute of type iron ore.
MOLY Molybdenum Commodity attribute of type
molybdenum.
NASC NASAAC Commodity attribute of type NASAAC
(North American Special Aluminum Alloy
Contract).
NICK Nickel Commodity attribute of type nickel.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
283 July 2025
```

