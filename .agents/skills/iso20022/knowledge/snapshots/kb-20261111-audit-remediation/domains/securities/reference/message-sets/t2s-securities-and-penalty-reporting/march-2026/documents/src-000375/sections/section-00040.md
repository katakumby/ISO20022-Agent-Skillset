---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks", "3.4.1 QueryDefinition <QryDef>", "3.4.1.2 SearchCriteria <SchCrit>", "3.4.1.2.12 SettledQuantity <SttldQty>", "3.4.1.2.12.1 Quantity <Qty>"]
file_pages: [53]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 3.4.1.2.12.1 Quantity <Qty>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 53 to 53.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 53

```text
SettledQuantity <SttldQty> contains one of the following QuantitySearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1]  53
{Or     Unit <Unit> [1..1]  54
{Or       FromQuantity <FrQty> [1..1]  55
         Boundary <Bdry> [1..1] Quantity 55
         Included <Incl> [1..1] Indicator 55
Or       ToQuantity <ToQty> [1..1]  56
         Boundary <Bdry> [1..1] Quantity 56
         Included <Incl> [1..1] Indicator 56
Or       FromToQuantity <FrToQty> [1..1]  56
         FromQuantity <FrQty> [1..1]  56
           Boundary <Bdry> [1..1] Quantity 57
           Included <Incl> [1..1] Indicator 57
         ToQuantity <ToQty> [1..1]  57
           Boundary <Bdry> [1..1] Quantity 57
           Included <Incl> [1..1] Indicator 57
Or       EqualQuantity <EQQty> [1..1] Quantity 58
Or}       NotEqualQuantity <NEQQty> [1..1] Quantity 58
Or     FaceAmount <FaceAmt> [1..1] ± 58
Or}     AmortisedValue <AmtsdVal> [1..1] ± 58
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1]  59
     FaceAmount <FaceAmt> [1..1] ± 59
     AmortisedValue <AmtsdVal> [1..1] ± 60
3.4.1.2.12.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of financial instrument in units, original face amount or current face amount.
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 53 March 2026
```

