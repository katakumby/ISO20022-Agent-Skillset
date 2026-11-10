---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.4 Amount Range", "37.1.4.6 AmountRangeBoundary1", "37.1.4.6.1 BoundaryAmount <BdryAmt>"]
file_pages: [794]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.4.6.1 BoundaryAmount <BdryAmt>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 794 to 794.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 794

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 794
   Included <Incl> [1..1] Indicator 794
37.1.4.6.1  BoundaryAmount <BdryAmt>
Presence: [1..1]
Definition: Amount value of the range limit.
Datatype: "ImpliedCurrencyAndAmount" on page 848
37.1.4.6.2  Included <Incl>
Presence: [1..1]
Definition: Indicates whether the boundary amount is included in the range of amount values.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 886):
• Meaning When True: Yes
• Meaning When False: No
37.1.4.7  ImpliedCurrencyAmountRange1Choice
Definition: Choice between ranges of values in which an amount is considered valid or a specified
amount value which has to be matched or unmatched to be valid.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromAmount <FrAmt> [1..1] ± 794
Or   ToAmount <ToAmt> [1..1] ± 795
Or   FromToAmount <FrToAmt> [1..1]  795
     FromAmount <FrAmt> [1..1] ± 795
     ToAmount <ToAmt> [1..1] ± 795
Or   EqualAmount <EQAmt> [1..1] Amount 796
Or}   NotEqualAmount <NEQAmt> [1..1] Amount 796
37.1.4.7.1  FromAmount <FrAmt>
Presence: [1..1]
Definition: Lower boundary of a range of amount values.
FromAmount <FrAmt> contains the following elements (see "AmountRangeBoundary1" on page 793
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 794
   Included <Incl> [1..1] Indicator 794
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 794 February 2025
```

