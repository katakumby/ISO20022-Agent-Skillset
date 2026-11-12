---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.49 SecuritiesFinancing12", "7.1.19.49.8 StockLoanMargin <StockLnMrgn>"]
file_pages: [362]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.49.8 StockLoanMargin <StockLnMrgn>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 362 to 362.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 362

```text
Constraints
• SignRule
When Sign is present, rate must not be zero.
7.1.19.49.8  StockLoanMargin <StockLnMrgn>
Presence: [0..1]
Definition: Percentage mark-up on a loan consideration used to reflect the lender's risk.
Impacted by: C48 "SignRule"
StockLoanMargin <StockLnMrgn> contains the following elements (see "Rate2" on page 517 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 517
   Rate <Rate> [1..1] Rate 517
Constraints
• SignRule
When Sign is present, rate must not be zero.
7.1.19.49.9  SecuritiesHaircut <SctiesHrcut>
Presence: [0..1]
Definition: Haircut or valuation factor on the security expressed as a percentage.
Impacted by: C48 "SignRule"
SecuritiesHaircut <SctiesHrcut> contains the following elements (see "Rate2" on page 517 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 517
   Rate <Rate> [1..1] Rate 517
Constraints
• SignRule
When Sign is present, rate must not be zero.
7.1.19.49.10  PricingRate <PricgRate>
Presence: [0..1]
Definition: Interest rate to be paid on the transaction amount, as agreed between the counterparties.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 362 February 2025
```

