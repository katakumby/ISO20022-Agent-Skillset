---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.5 AgriculturalCommodityOilSeed1", "22.1.2.5.1 BaseProduct <BasePdct>"]
file_pages: [278]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.5.1 BaseProduct <BasePdct>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 278 to 278.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 278

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 278
   SubProduct <SubPdct> [1..1] CodeSet 278
   AdditionalSubProduct <AddtlSubPdct> [1..1] CodeSet 278
22.1.2.5.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType1Code" on page 422
CodeName Name Definition
AGRI Agricultural Commodity of type agricultural.
22.1.2.5.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType1Code" on page 425
CodeName Name Definition
GROS GrainOilSeeds Commodity of type grain oil seeds.
22.1.2.5.3  AdditionalSubProduct <AddtlSubPdct>
Presence: [1..1]
Definition: Further subproduct type related to instruments that have a non-financial instrument or
commodity as underlying.
Datatype: "AssetClassDetailedSubProductType1Code" on page 419
CodeName Name Definition
FWHT FeedWheat Commodity attribute of type feed wheat.
SOYB Soybeans Commodity attribute of type soybeans.
RPSD Rapeseed Commodity attribute of type rapeseed.
OTHR Other Commodity attribute of other type.
CORN Maize Commodity attribute of type maize.
RICE Rice Commodity attribute of type rice.
22.1.2.6  EnergyCommodityLightEnd1
Definition: Defines commodity sub-product attributes of an energy derivative of type light end.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
278 July 2025
```

