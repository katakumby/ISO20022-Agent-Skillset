---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.49 SecuritiesFinancing12", "7.1.19.49.29 DividendRatio <DvddRatio>"]
file_pages: [368]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.49.29 DividendRatio <DvddRatio>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 368 to 368.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 368

```text
Constraints
• SignRule
When Sign is present, rate must not be zero.
7.1.19.49.29  DividendRatio <DvddRatio>
Presence: [0..1]
Definition: Percentage of earnings paid to shareholders in dividends.
Impacted by: C48 "SignRule"
DividendRatio <DvddRatio> contains the following elements (see "Rate2" on page 517 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 517
   Rate <Rate> [1..1] Rate 517
Constraints
• SignRule
When Sign is present, rate must not be zero.
7.1.19.49.30  NumberOfDaysLendingBorrowing <NbOfDaysLndgBrrwg>
Presence: [0..1]
Definition: Number of days the securities are lent or borrowed where the contract has an agreed closing
date.
NumberOfDaysLendingBorrowing <NbOfDaysLndgBrrwg> contains one of the following elements
(see "Number24Choice" on page 322 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NumberIdentification <NbId> [1..1] Text 322
Or}   Proprietary <Prtry> [1..1] ± 322
7.1.19.49.31  StandardCollateralAmount <StdCollAmt>
Presence: [0..1]
Definition: Specifies the standard collateral amount.
StandardCollateralAmount <StdCollAmt> contains the following elements (see
"AmountAndDirection5" on page 227 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C9 227
   CreditDebit <CdtDbt> [0..1] CodeSet 228
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 368 February 2025
```

