---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.26 AssetClassCommodity3Choice", "22.1.2.26.5 Freight <Frght>"]
file_pages: [299]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.26.5 Freight <Frght>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 299 to 299.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 299

```text
22.1.2.26.5  Freight <Frght>
Presence: [1..1]
Definition: Freight commodities.
Freight <Frght> contains one of the following elements (see "AssetClassCommodityFreight1Choice"
on page 308 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Dry <Dry> [1..1] ± 308
Or   Wet <Wet> [1..1] ± 308
Or}   ContainerShip <CntnrShip> [1..1] ± 308
22.1.2.26.6  IndustrialProduct <IndstrlPdct>
Presence: [1..1]
Definition: Industrial Product commodities.
IndustrialProduct <IndstrlPdct> contains one of the following elements (see
"AssetClassCommodityIndustrialProduct1Choice" on page 276 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Construction <Cnstrctn> [1..1] ± 276
Or}   Manufacturing <Manfctg> [1..1] ± 276
22.1.2.26.7  Metal <Metl>
Presence: [1..1]
Definition: Metal commodities.
Metal <Metl> contains one of the following elements (see "AssetClassCommodityMetal1Choice" on
page 282 for details)
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
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
299 July 2025
```

