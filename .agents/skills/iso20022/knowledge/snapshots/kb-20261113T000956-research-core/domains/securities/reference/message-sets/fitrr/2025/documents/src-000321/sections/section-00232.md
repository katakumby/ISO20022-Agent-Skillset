---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.10 FertilizerCommodityPotash1", "22.1.2.10.1 BaseProduct <BasePdct>"]
file_pages: [282]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.10.1 BaseProduct <BasePdct>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 282 to 282.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 282

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 282
   SubProduct <SubPdct> [1..1] CodeSet 282
22.1.2.10.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType5Code" on page 423
CodeName Name Definition
FRTL Fertilizer Commodity of type fertilizer.
22.1.2.10.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType41Code" on page 429
CodeName Name Definition
PTSH Potash Commodity of type potash.
22.1.2.11  AssetClassCommodityMetal1Choice
Definition: Defines commodity attributes of a derivative where the type is metal.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NonPrecious <NonPrcs> [1..1]  282
     BaseProduct <BasePdct> [1..1] CodeSet 283
     SubProduct <SubPdct> [1..1] CodeSet 283
     AdditionalSubProduct <AddtlSubPdct> [1..1] CodeSet 283
Or}   Precious <Prcs> [1..1]  284
     BaseProduct <BasePdct> [1..1] CodeSet 284
     SubProduct <SubPdct> [1..1] CodeSet 284
     AdditionalSubProduct <AddtlSubPdct> [1..1] CodeSet 284
22.1.2.11.1  NonPrecious <NonPrcs>
Presence: [1..1]
Definition: Non-precious metal commodity derivative.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
282 July 2025
```

