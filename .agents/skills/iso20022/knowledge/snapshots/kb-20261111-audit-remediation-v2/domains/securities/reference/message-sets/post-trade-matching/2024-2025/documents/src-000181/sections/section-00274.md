---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.38 RateOrName1Choice", "7.1.19.38.1 Rate <Rate>"]
file_pages: [332]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.38.1 Rate <Rate>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 332 to 332.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 332

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] ± C48 332
Or}   RateName <RateNm> [1..1] ± 332
7.1.19.38.1  Rate <Rate>
Presence: [1..1]
Definition: Pricing expressed as a rate.
Impacted by: C48 "SignRule"
Rate <Rate> contains the following elements (see "Rate2" on page 517 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 517
   Rate <Rate> [1..1] Rate 517
Constraints
• SignRule
When Sign is present, rate must not be zero.
7.1.19.38.2  RateName <RateNm>
Presence: [1..1]
Definition: Pricing expressed as a rate name.
RateName <RateNm> contains the following elements (see "RateName1" on page 515 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [0..1] Text 516
   RateName <RateNm> [1..1] Text 516
7.1.19.39  RepurchaseType22Choice
Definition: Choice of format for the repurchase transaction type information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 332
Or}   Proprietary <Prtry> [1..1] ± 333
7.1.19.39.1  Code <Cd>
Presence: [1..1]
Definition: Type of securities financing transaction process expressed as an ISO 20022 code.
Datatype: "RepurchaseType9Code" on page 644
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 332 February 2025
```

