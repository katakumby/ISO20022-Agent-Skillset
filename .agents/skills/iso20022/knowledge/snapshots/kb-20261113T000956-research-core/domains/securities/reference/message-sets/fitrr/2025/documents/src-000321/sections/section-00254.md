---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.30 AssetClassCommodityOfficialEconomicStatistics1"]
file_pages: [304]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.30 AssetClassCommodityOfficialEconomicStatistics1

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 304 to 304.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 304

```text
Datatype: "AssetClassSubProductType21Code" on page 425
CodeName Name Definition
FRST Forestry Commodity of type forestry.
22.1.2.30  AssetClassCommodityOfficialEconomicStatistics1
Definition: Defines commodity attributes of a derivative where the type is official economic statistics.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 304
22.1.2.30.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType14Code" on page 422
CodeName Name Definition
OEST OfficialEconomicStatistic Commodity of type official economic
statistic.
22.1.2.31  FertilizerCommodityUrea1
Definition: Defines commodity sub-product attributes of a fertilizer derivative of type urea.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 304
   SubProduct <SubPdct> [1..1] CodeSet 304
22.1.2.31.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType5Code" on page 423
CodeName Name Definition
FRTL Fertilizer Commodity of type fertilizer.
22.1.2.31.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType43Code" on page 429
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
304 July 2025
```

