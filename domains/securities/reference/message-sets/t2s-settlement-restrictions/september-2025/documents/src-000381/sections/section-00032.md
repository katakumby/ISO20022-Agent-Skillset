---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["2 semt.028.001.01 IntraPositionMovementQueryV01", "2.4 Message Building Blocks", "2.4.1 QueryDefinition <QryDef>", "2.4.1.2 SearchCriteria <SchCrit>", "2.4.1.2.9 SettledQuantity <SttldQty>", "2.4.1.2.9.2 OriginalAndCurrentFace <OrgnlAndCurFace>"]
file_pages: [46]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 2.4.1.2.9.2 OriginalAndCurrentFace <OrgnlAndCurFace>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 46 to 46.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 46

```text
AmortisedValue <AmtsdVal> contains one of the following elements (see
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
2.4.1.2.9.2  OriginalAndCurrentFace <OrgnlAndCurFace>
Presence: [1..1]
Definition: Original and current value of an asset-back instrument.
OriginalAndCurrentFace <OrgnlAndCurFace> contains the following
FinancialInstrumentQuantitySearch2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FaceAmount <FaceAmt> [1..1] ± 46
   AmortisedValue <AmtsdVal> [1..1] ± 47
2.4.1.2.9.2.1  FaceAmount <FaceAmt>
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
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 46 September 2025
```

