---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.34 AssetClassCommodityFreight1Choice"]
file_pages: [308]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.34 AssetClassCommodityFreight1Choice

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 308 to 308.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 308

```text
Distillates <Dstllts> contains the following elements (see "EnergyCommodityDistillates1" on page 294
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 294
   SubProduct <SubPdct> [1..1] CodeSet 294
22.1.2.34  AssetClassCommodityFreight1Choice
Definition: Defines commodity attributes of a derivative where the type is freight.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Dry <Dry> [1..1] ± 308
Or   Wet <Wet> [1..1] ± 308
Or}   ContainerShip <CntnrShip> [1..1] ± 308
22.1.2.34.1  Dry <Dry>
Presence: [1..1]
Definition: Dry freight commodity derivative.
Dry <Dry> contains the following elements (see "FreightCommodityDry1" on page 311 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 311
   SubProduct <SubPdct> [1..1] CodeSet 311
   AdditionalSubProduct <AddtlSubPdct> [0..1] CodeSet 311
22.1.2.34.2  Wet <Wet>
Presence: [1..1]
Definition: Wet freight commodity derivative.
Wet <Wet> contains the following elements (see "FreightCommodityWet1" on page 302 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 302
   SubProduct <SubPdct> [1..1] CodeSet 303
   AdditionalSubProduct <AddtlSubPdct> [0..1] CodeSet 303
22.1.2.34.3  ContainerShip <CntnrShip>
Presence: [1..1]
Definition: Container ship freight commodity derivative.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
308 July 2025
```

