---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.15 UnderlyingRatio2", "7.1.19.15.2 UnderlyingQuantityNumerator <UndrlygQtyNmrtr>"]
file_pages: [305]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.15.2 UnderlyingQuantityNumerator <UndrlygQtyNmrtr>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 305 to 305.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 305

```text
UnderlyingQuantityDenominator <UndrlygQtyDnmtr> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 272 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 273
Or   FaceAmount <FaceAmt> [1..1] Amount 273
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 273
7.1.19.15.2  UnderlyingQuantityNumerator <UndrlygQtyNmrtr>
Presence: [1..1]
Definition: Number of related securities for the exercise.
UnderlyingQuantityNumerator <UndrlygQtyNmrtr> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 272 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 273
Or   FaceAmount <FaceAmt> [1..1] Amount 273
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 273
7.1.19.15.3  RelatedFinancialInstrumentIdentification <RltdFinInstrmId>
Presence: [0..*]
Definition: Related security into which the security can be converted.
Impacted by: C13 "DescriptionPresenceRule", C14 "DescriptionUsageRule", C19 "ISINGuideline", C20
"ISINPresenceRule", C26 "OtherIdentificationPresenceRule"
RelatedFinancialInstrumentIdentification <RltdFinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 270 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 271
   OtherIdentification <OthrId> [0..*]  271
     Identification <Id> [1..1] Text 271
     Suffix <Sfx> [0..1] Text 271
     Type <Tp> [1..1] ± 271
   Description <Desc> [0..1] Text 271
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 305 February 2025
```

