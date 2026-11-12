---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.14 AssetClassCommodityOtherC102Choice", "22.1.2.14.2 NonDeliverable <NonDlvrbl>", "22.1.2.14.2.2 SubProduct <SubPdct>"]
file_pages: [288]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.14.2.2 SubProduct <SubPdct>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 288 to 288.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 288

```text
22.1.2.14.2.2  SubProduct <SubPdct>
Presence: [0..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType48Code" on page 430
CodeName Name Definition
NDLV NonDeliverable Commodity of type non deliverable.
22.1.2.15  IndustrialProductCommodityConstruction1
Definition: Defines commodity sub-product attributes of an industrial product derivative of type
construction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 288
   SubProduct <SubPdct> [0..1] CodeSet 288
22.1.2.15.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType6Code" on page 423
CodeName Name Definition
INDP IndustrialProduct Commodity of type industrial product.
22.1.2.15.2  SubProduct <SubPdct>
Presence: [0..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType33Code" on page 427
CodeName Name Definition
CSTR Construction Commodity of type construction.
22.1.2.16  EnergyCommodityInterEnergy1
Definition: Defines commodity sub-product attributes of an energy derivative of type inter energy.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 288
   SubProduct <SubPdct> [1..1] CodeSet 289
22.1.2.16.1  BaseProduct <BasePdct>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
288 July 2025
```

