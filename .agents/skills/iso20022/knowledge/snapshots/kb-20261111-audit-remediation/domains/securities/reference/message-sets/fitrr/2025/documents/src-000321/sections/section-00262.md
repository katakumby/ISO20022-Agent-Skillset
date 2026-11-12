---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.2 Commodity", "22.1.2.39 AssetClassCommodityPaper1Choice"]
file_pages: [312]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.2.39 AssetClassCommodityPaper1Choice

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 312 to 312.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 312

```text
22.1.2.39  AssetClassCommodityPaper1Choice
Definition: Defines commodity attributes of a derivative where the type is paper.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ContainerBoard <CntnrBrd> [1..1]  312
     BaseProduct <BasePdct> [1..1] CodeSet 312
     SubProduct <SubPdct> [0..1] CodeSet 312
Or   Newsprint <Nwsprnt> [1..1]  313
     BaseProduct <BasePdct> [1..1] CodeSet 313
     SubProduct <SubPdct> [0..1] CodeSet 313
Or   Pulp <Pulp> [1..1]  313
     BaseProduct <BasePdct> [1..1] CodeSet 313
     SubProduct <SubPdct> [0..1] CodeSet 314
Or}   RecoveredPaper <RcvrdPpr> [1..1]  314
     BaseProduct <BasePdct> [1..1] CodeSet 314
     SubProduct <SubPdct> [0..1] CodeSet 314
22.1.2.39.1  ContainerBoard <CntnrBrd>
Presence: [1..1]
Definition: Container board commodity derivative.
ContainerBoard <CntnrBrd> contains the following PaperCommodityContainerBoard1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BaseProduct <BasePdct> [1..1] CodeSet 312
   SubProduct <SubPdct> [0..1] CodeSet 312
22.1.2.39.1.1  BaseProduct <BasePdct>
Presence: [1..1]
Definition: Base product for the underlying asset class as specified in the classification of commodities
derivatives table.
Datatype: "AssetClassProductType8Code" on page 423
CodeName Name Definition
PAPR Paper Commodity of type paper.
22.1.2.39.1.2  SubProduct <SubPdct>
Presence: [0..1]
Definition: Sub-product for the underlying asset class.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
312 July 2025
```

