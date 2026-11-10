---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.11 AssetClassCommodityMetal1Choice", "22.1.2.11.2 Precious <Prcs>"]
file_pages: [284]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.11.2 Precious <Prcs>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 284 to 284.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 284

```text
CodeName Name Definition
STEL Steel Commodity attribute of type steel.
TINN Tin Commodity attribute of type tin.
ZINC Zinc Commodity attribute of type zinc.
OTHR Other Commodity attribute of other type.
LEAD Lead Commodity attribute of type lead.
22.1.2.11.2  Precious <Prcs>
Presence: [1..1]
Definition: Precious metal commodity derivative.
Precious <Prcs> contains the following MetalCommodityPrecious1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 284
   SubProduct <SubPdct> [1..1] CodeSet 284
   AdditionalSubProduct <AddtlSubPdct> [1..1] CodeSet 284
22.1.2.11.2.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType7Code" on page 423
CodeName Name Definition
METL Metal Commodity of type metal.
22.1.2.11.2.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType16Code" on page 424
CodeName Name Definition
PRME Precious Commodity of type precious metals.
22.1.2.11.2.3  AdditionalSubProduct <AddtlSubPdct>
Presence: [1..1]
Definition: Further subproduct type related to instruments that have a non-financial instrument or
commodity as underlying.
Datatype: "AssetClassDetailedSubProductType11Code" on page 418
CodeName Name Definition
GOLD Gold Commodity attribute of type gold.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
284 July 2025
```

