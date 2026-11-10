---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.6 FinancialInstrumentAttributes <FinInstrmAttrbts>", "3.4.6.47 MinimumNominalQuantity <MinNmnlQty>"]
file_pages: [76]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.6.47 MinimumNominalQuantity <MinNmnlQty>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 76 to 76.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 76

```text
TaxableIncomePerShare <TaxblIncmPerShr> contains the following elements (see "Price14" on
page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
3.4.6.47  MinimumNominalQuantity <MinNmnlQty>
Presence: [0..1]
Definition: Indicates the minimum tradable quantity of a security.
MinimumNominalQuantity <MinNmnlQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 272 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 273
Or   FaceAmount <FaceAmt> [1..1] Amount 273
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 273
3.4.6.48  MinimumExercisableQuantity <MinExrcblQty>
Presence: [0..1]
Definition: Minimum quantity of financial instrument or lot of rights/warrants that must be exercised.
MinimumExercisableQuantity <MinExrcblQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 272 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 273
Or   FaceAmount <FaceAmt> [1..1] Amount 273
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 273
3.4.6.49  MinimumExercisableMultipleQuantity <MinExrcblMltplQty>
Presence: [0..1]
Definition: Minimum multiple quantity of financial instrument or lot of rights/warrants that must be
exercised.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 76 February 2025
```

