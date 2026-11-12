---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.3 Amount", "7.1.3.3 AmountAndDirection6", "7.1.3.3.2 Sign <Sgn>"]
file_pages: [253]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.3.3.2 Sign <Sgn>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 253 to 253.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 253

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
7.1.3.3.2  Sign <Sgn>
Presence: [1..1]
Definition: Indicates that the amount value is positive or negative.
Datatype: One of the following values must be used (see "PlusOrMinusIndicator" on page 553):
• Meaning When True: Plus
• Meaning When False: Minus
7.1.4 Amount Range
7.1.4.1  ImpliedCurrencyAmountRange1Choice
Definition: Choice between ranges of values in which an amount is considered valid or a specified
amount value which has to be matched or unmatched to be valid.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromAmount <FrAmt> [1..1] ± 253
Or   ToAmount <ToAmt> [1..1] ± 254
Or   FromToAmount <FrToAmt> [1..1]  254
     FromAmount <FrAmt> [1..1] ± 254
     ToAmount <ToAmt> [1..1] ± 254
Or   EqualAmount <EQAmt> [1..1] Amount 255
Or}   NotEqualAmount <NEQAmt> [1..1] Amount 255
7.1.4.1.1  FromAmount <FrAmt>
Presence: [1..1]
Definition: Lower boundary of a range of amount values.
FromAmount <FrAmt> contains the following elements (see "AmountRangeBoundary1" on page 256
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 256
   Included <Incl> [1..1] Indicator 256
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 253 March 2026
```

