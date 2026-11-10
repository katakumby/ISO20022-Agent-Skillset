---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.23 Rate", "7.1.23.3 Rate2"]
file_pages: [517]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.23.3 Rate2

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 517 to 517.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 517

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.23.3  Rate2
Definition: Set of elements qualifying the interest rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 517
   Rate <Rate> [1..1] Rate 517
Constraints
• SignRule
When Sign is present, rate must not be zero.
7.1.23.3.1  Sign <Sgn>
Presence: [0..1]
Definition: Indicates the sign of the rate.
Datatype: One of the following values must be used (see "PlusOrMinusIndicator" on page 665):
• Meaning When True: Plus
• Meaning When False: Minus
7.1.23.3.2  Rate <Rate>
Presence: [1..1]
Definition: Percentage charged for the use of an amount of money, usually expressed at an annual rate.
The interest rate is the ratio of the amount of interest paid during a certain period of time compared to
the principal amount of the interest bearing financial instrument.
Datatype: "PercentageRate" on page 667
7.1.24 Rating
7.1.24.1  Rating1
Definition: Assessment of securities credit and investment risk.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 517 February 2025
```

