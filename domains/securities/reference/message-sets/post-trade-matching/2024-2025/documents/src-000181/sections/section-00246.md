---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.14 Revaluation3Choice", "7.1.19.14.1 Indicator <Ind>"]
file_pages: [304]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.14.1 Indicator <Ind>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 304 to 304.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 304

```text
7.1.19.14.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether the collateral position should be subject to automatic revaluation by the
account servicer.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.14.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reevaluation is determined using a data source scheme.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.15  UnderlyingRatio2
Definition: Related financial instrument into which the security can be converted.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnderlyingQuantityDenominator <UndrlygQtyDnmtr> [1..1] ± 304
   UnderlyingQuantityNumerator <UndrlygQtyNmrtr> [1..1] ± 305
   RelatedFinancialInstrumentIdentification
<RltdFinInstrmId>
[0..*] ± C13,
C14,
C19,
C20,
C26
305
7.1.19.15.1  UnderlyingQuantityDenominator <UndrlygQtyDnmtr>
Presence: [1..1]
Definition: Number of held securities for the exercise.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 304 February 2025
```

