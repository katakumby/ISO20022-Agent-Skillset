---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.35 AssetClassCommodityPolypropylene1Choice"]
file_pages: [309]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.35 AssetClassCommodityPolypropylene1Choice

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 309 to 309.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 309

```text
ContainerShip <CntnrShip> contains the following elements (see "FreightCommodityContainerShip1"
on page 277 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 277
   SubProduct <SubPdct> [1..1] CodeSet 277
22.1.2.35  AssetClassCommodityPolypropylene1Choice
Definition: Defines commodity attributes of a derivative where the type is polypropylene.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Plastic <Plstc> [1..1]  309
     BaseProduct <BasePdct> [1..1] CodeSet 309
     SubProduct <SubPdct> [0..1] CodeSet 309
22.1.2.35.1  Plastic <Plstc>
Presence: [1..1]
Definition: Plastic commodity derivative.
Plastic <Plstc> contains the following PolypropyleneCommodityPlastic1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 309
   SubProduct <SubPdct> [0..1] CodeSet 309
22.1.2.35.1.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType9Code" on page 424
CodeName Name Definition
POLY Polypropylene Commodity of type polypropylene.
22.1.2.35.1.2  SubProduct <SubPdct>
Presence: [0..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType18Code" on page 424
CodeName Name Definition
PLST Plastic Commodity of type plastic.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
309 July 2025
```

