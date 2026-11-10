---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.4 Amount Range"]
file_pages: [394]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.4 Amount Range

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 394 to 394.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 394

```text
17.1.4 Amount Range
17.1.4.1  ImpliedCurrencyAmountRange1Choice
Definition: Choice between ranges of values in which an amount is considered valid or a specified
amount value which has to be matched or unmatched to be valid.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromAmount <FrAmt> [1..1] ± 394
Or   ToAmount <ToAmt> [1..1] ± 394
Or   FromToAmount <FrToAmt> [1..1]  394
     FromAmount <FrAmt> [1..1] ± 395
     ToAmount <ToAmt> [1..1] ± 395
Or   EqualAmount <EQAmt> [1..1] Amount 395
Or}   NotEqualAmount <NEQAmt> [1..1] Amount 395
17.1.4.1.1  FromAmount <FrAmt>
Presence: [1..1]
Definition: Lower boundary of a range of amount values.
FromAmount <FrAmt> contains the following elements (see "AmountRangeBoundary1" on page 395
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 396
   Included <Incl> [1..1] Indicator 396
17.1.4.1.2  ToAmount <ToAmt>
Presence: [1..1]
Definition: Upper boundary of a range of amount values.
ToAmount <ToAmt> contains the following elements (see "AmountRangeBoundary1" on page 395 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 396
   Included <Incl> [1..1] Indicator 396
17.1.4.1.3  FromToAmount <FrToAmt>
Presence: [1..1]
Definition: Range of valid amount values.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
394 March 2024
```

