---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.4 Amount Range", "37.1.4.7 ImpliedCurrencyAmountRange1Choice", "37.1.4.7.2 ToAmount <ToAmt>"]
file_pages: [795]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.4.7.2 ToAmount <ToAmt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 795 to 795.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 795

```text
37.1.4.7.2  ToAmount <ToAmt>
Presence: [1..1]
Definition: Upper boundary of a range of amount values.
ToAmount <ToAmt> contains the following elements (see "AmountRangeBoundary1" on page 793 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 794
   Included <Incl> [1..1] Indicator 794
37.1.4.7.3  FromToAmount <FrToAmt>
Presence: [1..1]
Definition: Range of valid amount values.
FromToAmount <FrToAmt> contains the following FromToAmountRange1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromAmount <FrAmt> [1..1] ± 795
   ToAmount <ToAmt> [1..1] ± 795
37.1.4.7.3.1  FromAmount <FrAmt>
Presence: [1..1]
Definition: Lower boundary of a range of amount values.
FromAmount <FrAmt> contains the following elements (see "AmountRangeBoundary1" on page 793
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 794
   Included <Incl> [1..1] Indicator 794
37.1.4.7.3.2  ToAmount <ToAmt>
Presence: [1..1]
Definition: Upper boundary of a range of amount values.
ToAmount <ToAmt> contains the following elements (see "AmountRangeBoundary1" on page 793 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 794
   Included <Incl> [1..1] Indicator 794
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 795 February 2025
```

