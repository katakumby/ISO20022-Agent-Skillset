---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.4 Amount Range", "6.1.4.1 ImpliedCurrencyAmountRange1Choice", "6.1.4.1.3 FromToAmount <FrToAmt>", "6.1.4.1.3.1 FromAmount <FrAmt>"]
file_pages: [813]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.4.1.3.1 FromAmount <FrAmt>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 813 to 813.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 813

```text
FromToAmount <FrToAmt> contains the following FromToAmountRange1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromAmount <FrAmt> [1..1] ± 813
   ToAmount <ToAmt> [1..1] ± 813
6.1.4.1.3.1  FromAmount <FrAmt>
Presence: [1..1]
Definition: Lower boundary of a range of amount values.
FromAmount <FrAmt> contains the following elements (see "AmountRangeBoundary1" on page 815
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 815
   Included <Incl> [1..1] Indicator 815
6.1.4.1.3.2  ToAmount <ToAmt>
Presence: [1..1]
Definition: Upper boundary of a range of amount values.
ToAmount <ToAmt> contains the following elements (see "AmountRangeBoundary1" on page 815
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 815
   Included <Incl> [1..1] Indicator 815
6.1.4.1.4  EqualAmount <EQAmt>
Presence: [1..1]
Definition: Exact value an amount must match to be considered valid.
Datatype: "ImpliedCurrencyAndAmount" on page 886
6.1.4.1.5  NotEqualAmount <NEQAmt>
Presence: [1..1]
Definition: Value that an amount must not match to be considered valid.
Datatype: "ImpliedCurrencyAndAmount" on page 886
6.1.4.2  ActiveOrHistoricCurrencyAndAmountRange2
Definition: Range of amount values.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
813 March 2026
```

