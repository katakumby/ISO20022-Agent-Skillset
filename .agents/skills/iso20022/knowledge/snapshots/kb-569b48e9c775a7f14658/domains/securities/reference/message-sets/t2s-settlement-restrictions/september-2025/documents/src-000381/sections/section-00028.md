---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["2 semt.028.001.01 IntraPositionMovementQueryV01", "2.4 Message Building Blocks", "2.4.1 QueryDefinition <QryDef>", "2.4.1.2 SearchCriteria <SchCrit>", "2.4.1.2.9 SettledQuantity <SttldQty>", "2.4.1.2.9.1 Quantity <Qty>", "2.4.1.2.9.1.1 Unit <Unit>", "2.4.1.2.9.1.1.1 FromQuantity <FrQty>"]
file_pages: [42]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 2.4.1.2.9.1.1.1 FromQuantity <FrQty>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 42 to 42.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 42

```text
Unit <Unit> contains one of the following QuantityRange1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromQuantity <FrQty> [1..1]  42
     Boundary <Bdry> [1..1] Quantity 42
     Included <Incl> [1..1] Indicator 42
Or   ToQuantity <ToQty> [1..1]  43
     Boundary <Bdry> [1..1] Quantity 43
     Included <Incl> [1..1] Indicator 43
Or   FromToQuantity <FrToQty> [1..1]  43
     FromQuantity <FrQty> [1..1]  43
       Boundary <Bdry> [1..1] Quantity 44
       Included <Incl> [1..1] Indicator 44
     ToQuantity <ToQty> [1..1]  44
       Boundary <Bdry> [1..1] Quantity 44
       Included <Incl> [1..1] Indicator 44
Or   EqualQuantity <EQQty> [1..1] Quantity 45
Or}   NotEqualQuantity <NEQQty> [1..1] Quantity 45
2.4.1.2.9.1.1.1  FromQuantity <FrQty>
Presence: [1..1]
Definition: Lower boundary of a range of quantity values.
FromQuantity <FrQty> contains the following QuantityRangeBoundary1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Boundary <Bdry> [1..1] Quantity 42
   Included <Incl> [1..1] Indicator 42
2.4.1.2.9.1.1.1.1  Boundary <Bdry>
Presence: [1..1]
Definition: Quantity value of the range limit.
Datatype: "DecimalNumber" on page 342
2.4.1.2.9.1.1.1.2  Included <Incl>
Presence: [1..1]
Definition: Indicates whether the boundary quantity is included in the range of quantity values.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 342):
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 42 September 2025
```

