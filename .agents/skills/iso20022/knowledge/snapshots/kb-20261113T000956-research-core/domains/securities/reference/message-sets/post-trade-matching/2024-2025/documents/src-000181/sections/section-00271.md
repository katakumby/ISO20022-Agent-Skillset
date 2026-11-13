---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.35 FutureOrOptionDetails3", "7.1.19.35.16 Rating <Ratg>"]
file_pages: [329]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.35.16 Rating <Ratg>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 329 to 329.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 329

```text
Ratio <Ratio> contains the following elements (see "UnderlyingRatio2" on page 304 for details)
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
7.1.19.35.16  Rating <Ratg>
Presence: [0..*]
Definition: Rating(s) of the security.
Rating <Ratg> contains the following elements (see "Rating1" on page 517 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RatingScheme <RatgSchme> [1..1] Text 518
   ValueDate <ValDt> [1..1] DateTime 518
   ValueIdentification <ValId> [1..1] IdentifierSet 518
7.1.19.35.17  IssuePrice <IssePric>
Presence: [0..1]
Definition: Initial issue price of a financial instrument.
IssuePrice <IssePric> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
7.1.19.35.18  OptionRights <OptnRghts>
Presence: [0..1]
Definition: Rights to exercise the privilege to purchase or to sell the assets specified at a predetermined
price or formula at or within a time in the future.
OptionRights <OptnRghts> contains one of the following elements (see "OptionRight2Choice" on
page 382 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 382
Or}   Proprietary <Prtry> [1..1] ± 383
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 329 February 2025
```

