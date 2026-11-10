---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.2 SearchCriteria <SchCrit>", "71.4.1.2.12 SettledQuantity <SttldQty>", "71.4.1.2.12.1 Quantity <Qty>", "71.4.1.2.12.1.1 Unit <Unit>", "71.4.1.2.12.1.1.4 EqualQuantity <EQQty>"]
file_pages: [2454]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.2.12.1.1.4 EqualQuantity <EQQty>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2454 to 2454.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2454

```text
71.4.1.2.12.1.1.4  EqualQuantity <EQQty>
Presence: [1..1]
Definition: Exact value a quantity must match to be considered valid.
Datatype: "DecimalNumber" on page 3324
71.4.1.2.12.1.1.5  NotEqualQuantity <NEQQty>
Presence: [1..1]
Definition: Value that a quantity must not match to be considered valid.
Datatype: "DecimalNumber" on page 3324
71.4.1.2.12.1.2  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, that is the principal, of a
debt instrument.
FaceAmount <FaceAmt> contains one of the following elements (see
"ImpliedCurrencyAmountRange1Choice" on page 2842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromAmount <FrAmt> [1..1] ± 2842
Or   ToAmount <ToAmt> [1..1] ± 2842
Or   FromToAmount <FrToAmt> [1..1]  2843
     FromAmount <FrAmt> [1..1] ± 2843
     ToAmount <ToAmt> [1..1] ± 2843
Or   EqualAmount <EQAmt> [1..1] Amount 2843
Or}   NotEqualAmount <NEQAmt> [1..1] Amount 2844
71.4.1.2.12.1.3  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2454 August 2026
```

