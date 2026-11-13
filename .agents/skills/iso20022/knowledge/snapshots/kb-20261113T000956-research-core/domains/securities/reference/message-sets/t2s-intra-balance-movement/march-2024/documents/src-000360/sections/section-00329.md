---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.4 Amount Range", "17.1.4.1 ImpliedCurrencyAmountRange1Choice", "17.1.4.1.3 FromToAmount <FrToAmt>", "17.1.4.1.3.1 FromAmount <FrAmt>"]
file_pages: [395]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.4.1.3.1 FromAmount <FrAmt>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 395 to 395.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 395

```text
FromToAmount <FrToAmt> contains the following FromToAmountRange1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromAmount <FrAmt> [1..1] ± 395
   ToAmount <ToAmt> [1..1] ± 395
17.1.4.1.3.1  FromAmount <FrAmt>
Presence: [1..1]
Definition: Lower boundary of a range of amount values.
FromAmount <FrAmt> contains the following elements (see "AmountRangeBoundary1" on page 395
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 396
   Included <Incl> [1..1] Indicator 396
17.1.4.1.3.2  ToAmount <ToAmt>
Presence: [1..1]
Definition: Upper boundary of a range of amount values.
ToAmount <ToAmt> contains the following elements (see "AmountRangeBoundary1" on page 395 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 396
   Included <Incl> [1..1] Indicator 396
17.1.4.1.4  EqualAmount <EQAmt>
Presence: [1..1]
Definition: Exact value an amount must match to be considered valid.
Datatype: "ImpliedCurrencyAndAmount" on page 474
17.1.4.1.5  NotEqualAmount <NEQAmt>
Presence: [1..1]
Definition: Value that an amount must not match to be considered valid.
Datatype: "ImpliedCurrencyAndAmount" on page 474
17.1.4.2  AmountRangeBoundary1
Definition: Limit for an amount range.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
395 March 2024
```

