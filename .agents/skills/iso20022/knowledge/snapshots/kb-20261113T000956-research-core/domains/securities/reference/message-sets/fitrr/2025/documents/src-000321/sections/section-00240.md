---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.18 EnvironmentalCommodityEmission1", "22.1.2.18.1 BaseProduct <BasePdct>"]
file_pages: [290]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.18.1 BaseProduct <BasePdct>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 290 to 290.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 290

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 290
   SubProduct <SubPdct> [1..1] CodeSet 290
   AdditionalSubProduct <AddtlSubPdct> [0..1] CodeSet 290
22.1.2.18.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType3Code" on page 423
CodeName Name Definition
ENVR Environmental Commodity of type environmental.
22.1.2.18.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType10Code" on page 424
CodeName Name Definition
EMIS Emission Commodity of type emission.
22.1.2.18.3  AdditionalSubProduct <AddtlSubPdct>
Presence: [0..1]
Definition: Further subproduct type related to instruments that have a non-financial instrument or
commodity as underlying.
Datatype: "AssetClassDetailedSubProductType8Code" on page 421
CodeName Name Definition
CERE CER Commodity attribute of type emissions
allowance CER (Certified Emission
Reduction).
ERUE ERU Commodity attribute of type emissions
allowance ERU (European Reduction
Unit).
EUAE EUA Commodity attribute of type emissions
allowance EUA (European Union
Allowance).
EUAA EUAA Commodity attribute of type emissions
allowance EUAA (European Union
Aviation Allowance).
OTHR Other Commodity attribute of other type.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
290 July 2025
```

