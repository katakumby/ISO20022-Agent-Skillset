---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.40 Securities Quantity"]
file_pages: [5142]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.40 Securities Quantity

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5142 to 5142.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5142

```text
66.1.40 Securities Quantity
66.1.40.1  FinancialInstrumentQuantityChoice
Definition: Choice between formats for the quantity of security.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 5142
Or   FaceAmount <FaceAmt> [1..1] Amount 5142
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 5142
66.1.40.1.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, eg, a number of shares.
Datatype: "DecimalNumber" on page 5400
66.1.40.1.2  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, ie, the principal, of a debt
instrument.
Datatype: "ImpliedCurrencyAndAmount" on page 5270
66.1.40.1.3  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
eg, a periodic reduction of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 5270
66.1.40.2  FinancialInstrumentQuantity1
Definition: Quantity of a security.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.40.2.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, eg, a number of shares.
Datatype: "DecimalNumber" on page 5400
66.1.40.3  UnitsOrAmountOrPercentage1Choice
Definition: Choice between an amount or number of units or percentage.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5142 May 2026
```

