---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.42 EnergyCommodityOil1"]
file_pages: [316]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.42 EnergyCommodityOil1

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 316 to 316.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 316

```text
CodeName Name Definition
SLPH Sulphur Commodity of type sulphur.
22.1.2.42  EnergyCommodityOil1
Definition: Defines commodity sub-product attributes of an energy derivative of type oil.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 316
   SubProduct <SubPdct> [1..1] CodeSet 316
   AdditionalSubProduct <AddtlSubPdct> [0..1] CodeSet 316
22.1.2.42.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType2Code" on page 422
CodeName Name Definition
NRGY Energy Commodity of type energy.
22.1.2.42.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType8Code" on page 430
CodeName Name Definition
OILP Oil Commodity of type oil.
22.1.2.42.3  AdditionalSubProduct <AddtlSubPdct>
Presence: [0..1]
Definition: Further subproduct type related to instruments that have a non-financial instrument or
commodity as underlying.
Datatype: "AssetClassDetailedSubProductType7Code" on page 420
CodeName Name Definition
BAKK Bakken Commodity attribute of type bakken.
BDSL Biodiesel Commodity attribute of type biodiesel.
BRNT Brent Commodity attribute of type Brent.
BRNX BrentNX Commodity attribute of type Brent NX
(New Expiry).
CNDA Canadian Commodity attribute of type canadian.
COND Condensate Commodity attribute of type condensate.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
316 July 2025
```

