---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.4 Balance", "35.1.4.2 BalanceAmounts1", "35.1.4.2.3 BookValue <BookVal>"]
file_pages: [1411]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.4.2.3 BookValue <BookVal>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1411 to 1411.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1411

```text
PreviousHoldingValue <PrvsHldgVal> contains the following elements (see "AmountAndDirection6"
on page 1361 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1362
   Sign <Sgn> [1..1] Indicator 1362
35.1.4.2.3  BookValue <BookVal>
Presence: [0..1]
Definition: Value of a financial instrument, as booked/acquired in an account. It may be used to
establish capital gain tax liability.
BookValue <BookVal> contains the following elements (see "AmountAndDirection6" on page 1361 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1362
   Sign <Sgn> [1..1] Indicator 1362
35.1.4.2.4  UnrealisedGainLoss <UrlsdGnLoss>
Presence: [0..1]
Definition: Difference between holding value and the book value.
UnrealisedGainLoss <UrlsdGnLoss> contains the following elements (see "AmountAndDirection6" on
page 1361 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1362
   Sign <Sgn> [1..1] Indicator 1362
35.1.4.2.5  AccruedInterestAmount <AcrdIntrstAmt>
Presence: [0..1]
Definition: Interest amount that has accrued in between coupon payment periods.
AccruedInterestAmount <AcrdIntrstAmt> contains the following elements (see
"AmountAndDirection6" on page 1361 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1362
   Sign <Sgn> [1..1] Indicator 1362
35.1.4.3  SubBalanceType11Choice
Definition: Choice of format for the sub-balance.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1411 March 2026
```

