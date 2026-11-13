---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.7 AgriculturalCommodityGrain1", "22.1.2.7.3 AdditionalSubProduct <AddtlSubPdct>"]
file_pages: [280]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.7.3 AdditionalSubProduct <AddtlSubPdct>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 280 to 280.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 280

```text
Datatype: "AssetClassSubProductType5Code" on page 430
CodeName Name Definition
GRIN Grain Commodity of type grain.
22.1.2.7.3  AdditionalSubProduct <AddtlSubPdct>
Presence: [0..1]
Definition: Further subproduct type related to instruments that have a non-financial instrument or
commodity as underlying.
Datatype: "AssetClassDetailedSubProductType15Code" on page 419
CodeName Name Definition
MWHT MillingWheat Commodity attribute of type milled
wheat.
22.1.2.8  FertilizerCommodityAmmonia1
Definition: Defines commodity sub-product attributes of a fertilizer derivative of type ammonia.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 280
   SubProduct <SubPdct> [1..1] CodeSet 280
22.1.2.8.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType5Code" on page 423
CodeName Name Definition
FRTL Fertilizer Commodity of type fertilizer.
22.1.2.8.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType39Code" on page 428
CodeName Name Definition
AMMO Ammonia Commodity of type ammonia.
22.1.2.9  EnergyCommodityElectricity1
Definition: Defines commodity sub-product attributes of an energy derivative of type electricity.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
280 July 2025
```

