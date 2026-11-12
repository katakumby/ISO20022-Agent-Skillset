---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.39 AssetClassCommodityPaper1Choice", "22.1.2.39.2 Newsprint <Nwsprnt>"]
file_pages: [313]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.39.2 Newsprint <Nwsprnt>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 313 to 313.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 313

```text
Datatype: "AssetClassSubProductType35Code" on page 427
CodeName Name Definition
CBRD Containerboard Commodity of type containerboard.
22.1.2.39.2  Newsprint <Nwsprnt>
Presence: [1..1]
Definition: Newsprint commodity derivative.
Newsprint <Nwsprnt> contains the following PaperCommodityNewsprint1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 313
   SubProduct <SubPdct> [0..1] CodeSet 313
22.1.2.39.2.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType8Code" on page 423
CodeName Name Definition
PAPR Paper Commodity of type paper.
22.1.2.39.2.2  SubProduct <SubPdct>
Presence: [0..1]
Definition: Sub-product for the underlying asset class.
Datatype: "AssetClassSubProductType36Code" on page 428
CodeName Name Definition
NSPT Newsprint Commodity of type newsprint.
22.1.2.39.3  Pulp <Pulp>
Presence: [1..1]
Definition: Pulp commodity derivative.
Pulp <Pulp> contains the following PaperCommodityPulp1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 313
   SubProduct <SubPdct> [0..1] CodeSet 314
22.1.2.39.3.1  BaseProduct <BasePdct>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
313 July 2025
```

