---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks", "3.4.1 QueryDefinition <QryDef>", "3.4.1.2 SearchCriteria <SchCrit>", "3.4.1.2.11 SettlementQuantity <SttlmQty>", "3.4.1.2.11.1 Quantity <Qty>", "3.4.1.2.11.1.1 Unit <Unit>", "3.4.1.2.11.1.1.4 EqualQuantity <EQQty>"]
file_pages: [50]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 3.4.1.2.11.1.1.4 EqualQuantity <EQQty>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 50 to 50.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 50

```text
3.4.1.2.11.1.1.4  EqualQuantity <EQQty>
Presence: [1..1]
Definition: Exact value a quantity must match to be considered valid.
Datatype: "DecimalNumber" on page 554
3.4.1.2.11.1.1.5  NotEqualQuantity <NEQQty>
Presence: [1..1]
Definition: Value that a quantity must not match to be considered valid.
Datatype: "DecimalNumber" on page 554
3.4.1.2.11.1.2  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, that is the principal, of a
debt instrument.
FaceAmount <FaceAmt> contains one of the following elements (see
"ImpliedCurrencyAmountRange1Choice" on page 253 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromAmount <FrAmt> [1..1] ± 253
Or   ToAmount <ToAmt> [1..1] ± 254
Or   FromToAmount <FrToAmt> [1..1]  254
     FromAmount <FrAmt> [1..1] ± 254
     ToAmount <ToAmt> [1..1] ± 254
Or   EqualAmount <EQAmt> [1..1] Amount 255
Or}   NotEqualAmount <NEQAmt> [1..1] Amount 255
3.4.1.2.11.1.3  AmortisedValue <AmtsdVal>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the current amortised face amount of a bond,
for example, a periodic reduction/increase of a bond's principal amount.
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 50 March 2026
```

