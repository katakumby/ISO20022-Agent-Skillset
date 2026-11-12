---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.49 SecuritiesFinancing12", "7.1.19.49.32 AccruedInterestTax <AcrdIntrstTax>"]
file_pages: [369]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.49.32 AccruedInterestTax <AcrdIntrstTax>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 369 to 369.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 369

```text
7.1.19.49.32  AccruedInterestTax <AcrdIntrstTax>
Presence: [0..1]
Definition: Interest rate tax that has been accrued in between coupon payment periods.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.19.49.33  EndNumberOfDaysAccrued <EndNbOfDaysAcrd>
Presence: [0..1]
Definition: Number of days accrued at the instant of closing trade.
Impacted by: C25 "NumberRule"
Datatype: "Max3Number" on page 666
Constraints
• NumberRule
If Number is negative, then Sign must be present.
7.1.19.49.34  EndFactor <EndFctr>
Presence: [0..1]
Definition: End ratio of principal outstanding to the original balance.
Datatype: "BaseOneRate" on page 666
7.1.19.49.35  SecuritiesLendingType <SctiesLndgTp>
Presence: [0..1]
Definition: Type of securities lending.
SecuritiesLendingType <SctiesLndgTp> contains one of the following elements (see
"SecuritiesLendingType2Choice" on page 333 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 333
Or}   Proprietary <Prtry> [1..1] ± 334
7.1.19.49.36  Reversible <Rvsbl>
Presence: [0..1]
Definition: Indicates the possibility to terminate the securitiesc lending contract either by the borrower or
lender before the expiration date.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 369 February 2025
```

