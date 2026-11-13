---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.1 UnmatchedReason32Choice", "7.1.28.1.2 Proprietary <Prtry>"]
file_pages: [585]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.1.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 585 to 585.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 585

```text
CodeName Name Definition
OLID ClientOrderLinkIdentification ClientOrderLinkIdentification does not
match.
TRSA ClosingSettlementAmount Closing settlement amount does not
match.
TRTE TypeOfFinancingClosing Type of financing closing does not
match.
BOIA BorrowingInterestAmount Borrowing interest amount does not
match.
OPLI OpeningLegIdentification OpeningLegIdentification does not
match.
TRTR TradeTransactionType Trade transaction type does not match.
LWCO LendingWithCollateral LendingWithCollateral does not match.
INTT InterestType Interest type does not match.
CUFC CurrentFactor Current factor does not match.
LTME LendingTransactionMethod Lending transaction method does not
match.
ENFC EndFactor End factor does not match.
CLSE ClearingSegment Counterparty's instruction is for
settlement through clearing segment,
your instruction is not, or vice versa.
7.1.28.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has an unmatched status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.28.2  BorrowingReason2Choice
Definition: Choice of format for the borrowing reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 585
Or}   Proprietary <Prtry> [1..1] ± 586
7.1.28.2.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 585 February 2025
```

