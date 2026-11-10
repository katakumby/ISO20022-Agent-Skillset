---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.6 EnergyCommodityLightEnd1", "22.1.2.6.1 BaseProduct <BasePdct>"]
file_pages: [279]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.6.1 BaseProduct <BasePdct>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 279 to 279.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 279

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 279
   SubProduct <SubPdct> [1..1] CodeSet 279
22.1.2.6.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType2Code" on page 422
CodeName Name Definition
NRGY Energy Commodity of type energy.
22.1.2.6.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType27Code" on page 426
CodeName Name Definition
LGHT LightEnds Commodity of type light ends.
22.1.2.7  AgriculturalCommodityGrain1
Definition: Defines commodity sub-product attributes of an agricultural derivative of type grain.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 279
   SubProduct <SubPdct> [1..1] CodeSet 279
   AdditionalSubProduct <AddtlSubPdct> [0..1] CodeSet 280
22.1.2.7.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType1Code" on page 422
CodeName Name Definition
AGRI Agricultural Commodity of type agricultural.
22.1.2.7.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
279 July 2025
```

