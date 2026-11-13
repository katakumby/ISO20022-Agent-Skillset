---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["2 semt.028.001.01 IntraPositionMovementQueryV01", "2.4 Message Building Blocks", "2.4.1 QueryDefinition <QryDef>", "2.4.1.2 SearchCriteria <SchCrit>", "2.4.1.2.9 SettledQuantity <SttldQty>", "2.4.1.2.9.1 Quantity <Qty>"]
file_pages: [40]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 2.4.1.2.9.1 Quantity <Qty>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 40 to 40.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 40

```text
SettledQuantity <SttldQty> contains one of the following QuantitySearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1]  40
{Or     Unit <Unit> [1..1]  41
{Or       FromQuantity <FrQty> [1..1]  42
         Boundary <Bdry> [1..1] Quantity 42
         Included <Incl> [1..1] Indicator 42
Or       ToQuantity <ToQty> [1..1]  43
         Boundary <Bdry> [1..1] Quantity 43
         Included <Incl> [1..1] Indicator 43
Or       FromToQuantity <FrToQty> [1..1]  43
         FromQuantity <FrQty> [1..1]  43
           Boundary <Bdry> [1..1] Quantity 44
           Included <Incl> [1..1] Indicator 44
         ToQuantity <ToQty> [1..1]  44
           Boundary <Bdry> [1..1] Quantity 44
           Included <Incl> [1..1] Indicator 44
Or       EqualQuantity <EQQty> [1..1] Quantity 45
Or}       NotEqualQuantity <NEQQty> [1..1] Quantity 45
Or     FaceAmount <FaceAmt> [1..1] ± 45
Or}     AmortisedValue <AmtsdVal> [1..1] ± 45
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1]  46
     FaceAmount <FaceAmt> [1..1] ± 46
     AmortisedValue <AmtsdVal> [1..1] ± 47
2.4.1.2.9.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of financial instrument in units, original face amount or current face amount.
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 40 September 2025
```

