---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.25 AgriculturalCommoditySeafood1"]
file_pages: [296]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.25 AgriculturalCommoditySeafood1

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 296 to 296.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 296

```text
22.1.2.25  AgriculturalCommoditySeafood1
Definition: Defines commodity sub-product attributes of an agricultural derivative of type seafood.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 296
   SubProduct <SubPdct> [1..1] CodeSet 296
22.1.2.25.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType1Code" on page 422
CodeName Name Definition
AGRI Agricultural Commodity of type agricultural.
22.1.2.25.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType23Code" on page 425
CodeName Name Definition
SEAF Seafood Commodity of type seafood.
22.1.2.26  AssetClassCommodity3Choice
Definition: Choice to define commodity specific attributes of a derivative.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
296 July 2025
```

