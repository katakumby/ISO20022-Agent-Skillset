---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.49 SecuritiesFinancing12", "7.1.19.49.15 AccruedInterestPercentage <AcrdIntrstPctg>"]
file_pages: [364]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.49.15 AccruedInterestPercentage <AcrdIntrstPctg>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 364 to 364.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 364

```text
AccruedInterestAmount <AcrdIntrstAmt> contains the following elements (see
"AmountAndDirection5" on page 227 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C9 227
   CreditDebit <CdtDbt> [0..1] CodeSet 228
7.1.19.49.15  AccruedInterestPercentage <AcrdIntrstPctg>
Presence: [0..1]
Definition: Interest rate that has been accrued in between coupon payment periods.
Datatype: "PercentageRate" on page 667
7.1.19.49.16  ForfeitAmount <FrftAmt>
Presence: [0..1]
Definition: Fixed amount of money that has to be paid (instead of interest) in the case of a recall or at
the closing date.
ForfeitAmount <FrftAmt> contains the following elements (see "AmountAndDirection5" on page 227
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C9 227
   CreditDebit <CdtDbt> [0..1] CodeSet 228
7.1.19.49.17  PremiumAmount <PrmAmt>
Presence: [0..1]
Definition: Difference between the amount of money of the first leg and the amount of the second leg of
the transaction.
PremiumAmount <PrmAmt> contains the following elements (see "AmountAndDirection5" on
page 227 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C9 227
   CreditDebit <CdtDbt> [0..1] CodeSet 228
7.1.19.49.18  ClosingAmountPerPiecesOfCollateral <ClsgAmtPerPcsOfColl>
Presence: [0..1]
Definition: Amount of money to be settled per piece of collateral to close the transaction.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 364 February 2025
```

