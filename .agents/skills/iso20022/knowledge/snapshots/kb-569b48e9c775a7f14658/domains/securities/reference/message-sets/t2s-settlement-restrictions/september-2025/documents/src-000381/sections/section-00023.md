---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["2 semt.028.001.01 IntraPositionMovementQueryV01", "2.4 Message Building Blocks", "2.4.1 QueryDefinition <QryDef>", "2.4.1.2 SearchCriteria <SchCrit>", "2.4.1.2.8 SettlementQuantity <SttlmQty>", "2.4.1.2.8.1 Quantity <Qty>", "2.4.1.2.8.1.1 Unit <Unit>", "2.4.1.2.8.1.1.4 EqualQuantity <EQQty>"]
file_pages: [37]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 2.4.1.2.8.1.1.4 EqualQuantity <EQQty>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 37 to 37.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 37

```text
2.4.1.2.8.1.1.4  EqualQuantity <EQQty>
Presence: [1..1]
Definition: Exact value a quantity must match to be considered valid.
Datatype: "DecimalNumber" on page 342
2.4.1.2.8.1.1.5  NotEqualQuantity <NEQQty>
Presence: [1..1]
Definition: Value that a quantity must not match to be considered valid.
Datatype: "DecimalNumber" on page 342
2.4.1.2.8.1.2  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, that is the principal, of a
debt instrument.
FaceAmount <FaceAmt> contains one of the following elements (see
"ImpliedCurrencyAmountRange1Choice" on page 195 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromAmount <FrAmt> [1..1] ± 195
Or   ToAmount <ToAmt> [1..1] ± 195
Or   FromToAmount <FrToAmt> [1..1]  196
     FromAmount <FrAmt> [1..1] ± 196
     ToAmount <ToAmt> [1..1] ± 196
Or   EqualAmount <EQAmt> [1..1] Amount 196
Or}   NotEqualAmount <NEQAmt> [1..1] Amount 197
2.4.1.2.8.1.3  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 37 September 2025
```

