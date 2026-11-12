---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.23 AssetClassCommodityOther1"]
file_pages: [295]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.23 AssetClassCommodityOther1

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 295 to 295.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 295

```text
CodeName Name Definition
DIST Distillates Commodity of type distillates.
22.1.2.23  AssetClassCommodityOther1
Definition: Defines commodity attributes of a derivative where the type is other.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 295
22.1.2.23.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType15Code" on page 422
CodeName Name Definition
OTHR Other Commodity of other type.
22.1.2.24  EnvironmentalCommodityCarbonRelated1
Definition: Defines commodity sub-product attributes of an environmental derivative of type carbon
related.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 295
   SubProduct <SubPdct> [1..1] CodeSet 295
22.1.2.24.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType3Code" on page 423
CodeName Name Definition
ENVR Environmental Commodity of type environmental.
22.1.2.24.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType29Code" on page 426
CodeName Name Definition
CRBR CarbonRelated Commodity of type carbon related.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
295 July 2025
```

