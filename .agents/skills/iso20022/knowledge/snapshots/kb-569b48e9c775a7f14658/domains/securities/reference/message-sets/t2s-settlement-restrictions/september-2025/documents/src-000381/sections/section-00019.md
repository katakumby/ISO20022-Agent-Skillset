---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["2 semt.028.001.01 IntraPositionMovementQueryV01", "2.4 Message Building Blocks", "2.4.1 QueryDefinition <QryDef>", "2.4.1.2 SearchCriteria <SchCrit>", "2.4.1.2.8 SettlementQuantity <SttlmQty>", "2.4.1.2.8.1 Quantity <Qty>", "2.4.1.2.8.1.1 Unit <Unit>"]
file_pages: [33]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 2.4.1.2.8.1.1 Unit <Unit>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 33 to 33.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 33

```text
Quantity <Qty> contains one of the following FinancialInstrumentQuantitySearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1]  33
{Or     FromQuantity <FrQty> [1..1]  34
       Boundary <Bdry> [1..1] Quantity 34
       Included <Incl> [1..1] Indicator 34
Or     ToQuantity <ToQty> [1..1]  35
       Boundary <Bdry> [1..1] Quantity 35
       Included <Incl> [1..1] Indicator 35
Or     FromToQuantity <FrToQty> [1..1]  35
       FromQuantity <FrQty> [1..1]  35
         Boundary <Bdry> [1..1] Quantity 36
         Included <Incl> [1..1] Indicator 36
       ToQuantity <ToQty> [1..1]  36
         Boundary <Bdry> [1..1] Quantity 36
         Included <Incl> [1..1] Indicator 36
Or     EqualQuantity <EQQty> [1..1] Quantity 37
Or}     NotEqualQuantity <NEQQty> [1..1] Quantity 37
Or   FaceAmount <FaceAmt> [1..1] ± 37
Or}   AmortisedValue <AmtsdVal> [1..1] ± 37
2.4.1.2.8.1.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, for example a number of shares.
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 33 September 2025
```

