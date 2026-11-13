---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.4 Amount Range"]
file_pages: [812]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.4 Amount Range

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 812 to 812.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 812

```text
6.1.4 Amount Range
6.1.4.1  ImpliedCurrencyAmountRange1Choice
Definition: Choice between ranges of values in which an amount is considered valid or a specified
amount value which has to be matched or unmatched to be valid.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromAmount <FrAmt> [1..1] ± 812
Or   ToAmount <ToAmt> [1..1] ± 812
Or   FromToAmount <FrToAmt> [1..1]  812
     FromAmount <FrAmt> [1..1] ± 813
     ToAmount <ToAmt> [1..1] ± 813
Or   EqualAmount <EQAmt> [1..1] Amount 813
Or}   NotEqualAmount <NEQAmt> [1..1] Amount 813
6.1.4.1.1  FromAmount <FrAmt>
Presence: [1..1]
Definition: Lower boundary of a range of amount values.
FromAmount <FrAmt> contains the following elements (see "AmountRangeBoundary1" on page 815
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 815
   Included <Incl> [1..1] Indicator 815
6.1.4.1.2  ToAmount <ToAmt>
Presence: [1..1]
Definition: Upper boundary of a range of amount values.
ToAmount <ToAmt> contains the following elements (see "AmountRangeBoundary1" on page 815
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 815
   Included <Incl> [1..1] Indicator 815
6.1.4.1.3  FromToAmount <FrToAmt>
Presence: [1..1]
Definition: Range of valid amount values.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
812 March 2026
```

