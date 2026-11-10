---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.13 Financial Instrument Quantity"]
file_pages: [342]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.13 Financial Instrument Quantity

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 342 to 342.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 342

```text
7.1.13 Financial Instrument Quantity
7.1.13.1  FinancialInstrumentQuantity1Choice
Definition: Choice between formats for the quantity of security.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 342
Or   FaceAmount <FaceAmt> [1..1] Amount 342
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 342
7.1.13.1.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, for example, a number of shares.
Datatype: "DecimalNumber" on page 554
7.1.13.1.2  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, that is, the principal, of a
debt instrument.
Datatype: "ImpliedCurrencyAndAmount" on page 491
7.1.13.1.3  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 491
7.1.13.2  Quantity6Choice
Definition: Choice of format for the quantity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 342
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 343
7.1.13.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of financial instrument in units, original face amount or current face amount.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 342 March 2026
```

