---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.19 EnergyCommodityRenewableEnergy1"]
file_pages: [291]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.19 EnergyCommodityRenewableEnergy1

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 291 to 291.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 291

```text
22.1.2.19  EnergyCommodityRenewableEnergy1
Definition: Defines commodity sub-product attributes of an energy derivative of type renewable energy.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 291
   SubProduct <SubPdct> [1..1] CodeSet 291
22.1.2.19.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType2Code" on page 422
CodeName Name Definition
NRGY Energy Commodity of type energy.
22.1.2.19.2  SubProduct <SubPdct>
Presence: [1..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType28Code" on page 426
CodeName Name Definition
RNNG RenewableEnergy Commodity of type renewable energy.
22.1.2.20  AssetClassCommodityEnvironmental1Choice
Definition: Defines commodity attributes of a derivative where the type is environmental.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Emissions <Emssns> [1..1] ± 291
Or   Weather <Wthr> [1..1] ± 292
Or}   CarbonRelated <CrbnRltd> [1..1] ± 292
22.1.2.20.1  Emissions <Emssns>
Presence: [1..1]
Definition: Emissions environmental commodity derivative.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
291 July 2025
```

