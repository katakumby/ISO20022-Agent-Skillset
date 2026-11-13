---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.4 Amount Range", "82.1.4.1 ImpliedCurrencyAmountRange1Choice", "82.1.4.1.3 FromToAmount <FrToAmt>"]
file_pages: [2843]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.4.1.3 FromToAmount <FrToAmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2843 to 2843.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2843

```text
ToAmount <ToAmt> contains the following elements (see "AmountRangeBoundary1" on page 2845
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 2845
   Included <Incl> [1..1] Indicator 2845
82.1.4.1.3  FromToAmount <FrToAmt>
Presence: [1..1]
Definition: Range of valid amount values.
FromToAmount <FrToAmt> contains the following FromToAmountRange1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromAmount <FrAmt> [1..1] ± 2843
   ToAmount <ToAmt> [1..1] ± 2843
82.1.4.1.3.1  FromAmount <FrAmt>
Presence: [1..1]
Definition: Lower boundary of a range of amount values.
FromAmount <FrAmt> contains the following elements (see "AmountRangeBoundary1" on page 2845
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 2845
   Included <Incl> [1..1] Indicator 2845
82.1.4.1.3.2  ToAmount <ToAmt>
Presence: [1..1]
Definition: Upper boundary of a range of amount values.
ToAmount <ToAmt> contains the following elements (see "AmountRangeBoundary1" on page 2845
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 2845
   Included <Incl> [1..1] Indicator 2845
82.1.4.1.4  EqualAmount <EQAmt>
Presence: [1..1]
Definition: Exact value an amount must match to be considered valid.
Datatype: "ImpliedCurrencyAndAmount" on page 3210
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2843 August 2026
```

