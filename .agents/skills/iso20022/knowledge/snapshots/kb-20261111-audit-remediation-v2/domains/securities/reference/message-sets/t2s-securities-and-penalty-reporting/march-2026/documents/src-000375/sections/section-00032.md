---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks", "3.4.1 QueryDefinition <QryDef>", "3.4.1.2 SearchCriteria <SchCrit>", "3.4.1.2.11 SettlementQuantity <SttlmQty>", "3.4.1.2.11.1 Quantity <Qty>"]
file_pages: [45]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 3.4.1.2.11.1 Quantity <Qty>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 45 to 45.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 45

```text
Definition: Total quantity of securities to be settled.
SettlementQuantity <SttlmQty> contains one of the following QuantitySearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1]  45
{Or     Unit <Unit> [1..1]  46
{Or       FromQuantity <FrQty> [1..1]  47
         Boundary <Bdry> [1..1] Quantity 47
         Included <Incl> [1..1] Indicator 47
Or       ToQuantity <ToQty> [1..1]  48
         Boundary <Bdry> [1..1] Quantity 48
         Included <Incl> [1..1] Indicator 48
Or       FromToQuantity <FrToQty> [1..1]  48
         FromQuantity <FrQty> [1..1]  48
           Boundary <Bdry> [1..1] Quantity 49
           Included <Incl> [1..1] Indicator 49
         ToQuantity <ToQty> [1..1]  49
           Boundary <Bdry> [1..1] Quantity 49
           Included <Incl> [1..1] Indicator 49
Or       EqualQuantity <EQQty> [1..1] Quantity 50
Or}       NotEqualQuantity <NEQQty> [1..1] Quantity 50
Or     FaceAmount <FaceAmt> [1..1] ± 50
Or}     AmortisedValue <AmtsdVal> [1..1] ± 50
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1]  51
     FaceAmount <FaceAmt> [1..1] ± 51
     AmortisedValue <AmtsdVal> [1..1] ± 52
3.4.1.2.11.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of financial instrument in units, original face amount or current face amount.
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 45 March 2026
```

