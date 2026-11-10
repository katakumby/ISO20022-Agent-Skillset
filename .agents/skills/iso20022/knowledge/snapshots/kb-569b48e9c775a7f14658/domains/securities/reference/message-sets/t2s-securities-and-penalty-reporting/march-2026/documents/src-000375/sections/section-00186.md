---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.4 Amount Range", "7.1.4.1 ImpliedCurrencyAmountRange1Choice", "7.1.4.1.2 ToAmount <ToAmt>"]
file_pages: [254]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.4.1.2 ToAmount <ToAmt>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 254 to 254.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 254

```text
7.1.4.1.2  ToAmount <ToAmt>
Presence: [1..1]
Definition: Upper boundary of a range of amount values.
ToAmount <ToAmt> contains the following elements (see "AmountRangeBoundary1" on page 256 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 256
   Included <Incl> [1..1] Indicator 256
7.1.4.1.3  FromToAmount <FrToAmt>
Presence: [1..1]
Definition: Range of valid amount values.
FromToAmount <FrToAmt> contains the following FromToAmountRange1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromAmount <FrAmt> [1..1] ± 254
   ToAmount <ToAmt> [1..1] ± 254
7.1.4.1.3.1  FromAmount <FrAmt>
Presence: [1..1]
Definition: Lower boundary of a range of amount values.
FromAmount <FrAmt> contains the following elements (see "AmountRangeBoundary1" on page 256
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 256
   Included <Incl> [1..1] Indicator 256
7.1.4.1.3.2  ToAmount <ToAmt>
Presence: [1..1]
Definition: Upper boundary of a range of amount values.
ToAmount <ToAmt> contains the following elements (see "AmountRangeBoundary1" on page 256 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 256
   Included <Incl> [1..1] Indicator 256
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 254 March 2026
```

