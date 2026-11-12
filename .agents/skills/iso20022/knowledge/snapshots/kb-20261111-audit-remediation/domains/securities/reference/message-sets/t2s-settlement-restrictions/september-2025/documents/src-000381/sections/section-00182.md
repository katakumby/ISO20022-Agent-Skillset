---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.10 Financial Instrument Quantity", "9.1.10.1 FinancialInstrumentQuantity1Choice", "9.1.10.1.1 Unit <Unit>"]
file_pages: [221]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.10.1.1 Unit <Unit>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 221 to 221.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 221

```text
9.1.10.1.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, for example, a number of shares.
Datatype: "DecimalNumber" on page 342
9.1.10.1.2  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, that is, the principal, of a
debt instrument.
Datatype: "ImpliedCurrencyAndAmount" on page 313
9.1.10.1.3  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Datatype: "ImpliedCurrencyAndAmount" on page 313
9.1.10.2  Quantity6Choice
Definition: Choice of format for the quantity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 221
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 221
9.1.10.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of financial instrument in units, original face amount or current face amount.
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantity1Choice" on
page 220 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 221
Or   FaceAmount <FaceAmt> [1..1] Amount 221
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 221
9.1.10.2.2  OriginalAndCurrentFace <OrgnlAndCurFace>
Presence: [1..1]
Definition: Original and current value of an asset-back instrument.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 221 September 2025
```

