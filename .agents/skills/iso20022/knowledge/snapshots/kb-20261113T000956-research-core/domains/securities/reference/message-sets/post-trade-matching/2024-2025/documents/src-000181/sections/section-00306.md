---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.49 SecuritiesFinancing12", "7.1.19.49.27 BorrowingRate <BrrwgRate>"]
file_pages: [367]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.49.27 BorrowingRate <BrrwgRate>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 367 to 367.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 367

```text
InterestRate <IntrstRate> contains the following elements (see "Rate2" on page 517 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 517
   Rate <Rate> [1..1] Rate 517
Constraints
• SignRule
When Sign is present, rate must not be zero.
7.1.19.49.27  BorrowingRate <BrrwgRate>
Presence: [0..1]
Definition: Rate to be paid by the Borrower to the Lender for the securities borrowed.
Impacted by: C48 "SignRule"
BorrowingRate <BrrwgRate> contains the following elements (see "Rate2" on page 517 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 517
   Rate <Rate> [1..1] Rate 517
Constraints
• SignRule
When Sign is present, rate must not be zero.
7.1.19.49.28  StandardCollateralRatio <StdCollRatio>
Presence: [0..1]
Definition: Method used to calculate the standard collateral amount.
Impacted by: C48 "SignRule"
StandardCollateralRatio <StdCollRatio> contains the following elements (see "Rate2" on page 517
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 517
   Rate <Rate> [1..1] Rate 517
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 367 February 2025
```

