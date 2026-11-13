---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.45 EnergyCommodityNaturalGas1"]
file_pages: [321]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.45 EnergyCommodityNaturalGas1

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 321 to 321.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 321

```text
22.1.2.45  EnergyCommodityNaturalGas1
Definition: Defines commodity sub-product attributes of an energy derivative of type natural gas.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 321
   SubProduct <SubPdct> [1..1] CodeSet 321
   AdditionalSubProduct <AddtlSubPdct> [0..1] CodeSet 321
22.1.2.45.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType2Code" on page 422
CodeName Name Definition
NRGY Energy Commodity of type energy.
22.1.2.45.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType7Code" on page 430
CodeName Name Definition
NGAS NaturalGas Commodity of type natural gas.
22.1.2.45.3  AdditionalSubProduct <AddtlSubPdct>
Presence: [0..1]
Definition: Further subproduct type related to instruments that have a non-financial instrument or
commodity as underlying.
Datatype: "AssetClassDetailedSubProductType6Code" on page 420
CodeName Name Definition
GASP GasPool Commodity attribute of type GASPOOL.
LNGG LNG Commodity attribute of type liquid natural
gas.
NCGG NCG Commodity attribute of type NCG
(NetConnect Germany).
TTFG TTF Commodity attribute of type TTF (Dutch
Title Transfer Facility).
NBPG NBP Commodity attribute of type NBP
(National Balancing Point).
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
321 July 2025
```

