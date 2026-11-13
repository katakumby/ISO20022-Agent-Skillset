---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.13 AgriculturalCommoditySoft1", "22.1.2.13.2 SubProduct <SubPdct>"]
file_pages: [286]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.13.2 SubProduct <SubPdct>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 286 to 286.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 286

```text
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType1Code" on page 422
CodeName Name Definition
AGRI Agricultural Commodity of type agricultural.
22.1.2.13.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType2Code" on page 426
CodeName Name Definition
SOFT Softs Commodity of type softs.
22.1.2.13.3  AdditionalSubProduct <AddtlSubPdct>
Presence: [1..1]
Definition: Further subproduct type related to instruments that have a non-financial instrument or
commodity as underlying.
Datatype: "AssetClassDetailedSubProductType2Code" on page 419
CodeName Name Definition
ROBU RobustaCoffee Commodity attribute of type robusta
coffee.
CCOA Cocoa Commodity attribute of type cocoa.
BRWN RawSugar Commodity attribute of type raw sugar.
WHSG WhiteSugar Commodity attribute of type white sugar.
OTHR Other Commodity attribute of other type.
22.1.2.14  AssetClassCommodityOtherC102Choice
Definition: Defines commodity attributes of a derivative where the type is other C10.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Deliverable <Dlvrbl> [1..1]  286
     BaseProduct <BasePdct> [1..1] CodeSet 287
     SubProduct <SubPdct> [0..1] CodeSet 287
Or}   NonDeliverable <NonDlvrbl> [1..1]  287
     BaseProduct <BasePdct> [1..1] CodeSet 287
     SubProduct <SubPdct> [0..1] CodeSet 288
22.1.2.14.1  Deliverable <Dlvrbl>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
286 July 2025
```

