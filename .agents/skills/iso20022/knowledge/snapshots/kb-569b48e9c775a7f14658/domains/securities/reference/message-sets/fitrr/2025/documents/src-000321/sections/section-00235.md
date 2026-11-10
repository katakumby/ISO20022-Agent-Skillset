---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.12 AgriculturalCommodityDairy1"]
file_pages: [285]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.12 AgriculturalCommodityDairy1

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 285 to 285.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 285

```text
CodeName Name Definition
OTHR Other Commodity attribute of other type.
PLDM Palladium Commodity attribute of type palladium.
PTNM Platinum Commodity attribute of type platinum.
SLVR Silver Commodity attribute of type silver.
22.1.2.12  AgriculturalCommodityDairy1
Definition: Defines commodity sub-product attributes of an agricultural derivative of type dairy.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 285
   SubProduct <SubPdct> [1..1] CodeSet 285
22.1.2.12.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType1Code" on page 422
CodeName Name Definition
AGRI Agricultural Commodity of type agricultural.
22.1.2.12.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType20Code" on page 425
CodeName Name Definition
DIRY Dairy Commodity of type dairy.
22.1.2.13  AgriculturalCommoditySoft1
Definition: Defines commodity sub-product attributes of an agricultural derivative of type soft.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 285
   SubProduct <SubPdct> [1..1] CodeSet 286
   AdditionalSubProduct <AddtlSubPdct> [1..1] CodeSet 286
22.1.2.13.1  BaseProduct <BasePdct>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
285 July 2025
```

