---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.14 AssetClassCommodityOtherC102Choice", "22.1.2.14.1 Deliverable <Dlvrbl>", "22.1.2.14.1.1 BaseProduct <BasePdct>"]
file_pages: [287]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.14.1.1 BaseProduct <BasePdct>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 287 to 287.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 287

```text
Definition: Other C10 deliverable commodity derivative.
Deliverable <Dlvrbl> contains the following OtherC10CommodityDeliverable2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 287
   SubProduct <SubPdct> [0..1] CodeSet 287
22.1.2.14.1.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType11Code" on page 421
CodeName Name Definition
OTHC OtherC10 Commodity of other type C10.
22.1.2.14.1.2  SubProduct <SubPdct>
Presence: [0..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType47Code" on page 430
CodeName Name Definition
DLVR Deliverable Commodity of type deliverable.
22.1.2.14.2  NonDeliverable <NonDlvrbl>
Presence: [1..1]
Definition: Other C10 non-deliverable commodity derivative.
NonDeliverable <NonDlvrbl> contains the following OtherC10CommodityNonDeliverable2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 287
   SubProduct <SubPdct> [0..1] CodeSet 288
22.1.2.14.2.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType11Code" on page 421
CodeName Name Definition
OTHC OtherC10 Commodity of other type C10.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
287 July 2025
```

