---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["2 semt.028.001.01 IntraPositionMovementQueryV01", "2.4 Message Building Blocks", "2.4.1 QueryDefinition <QryDef>", "2.4.1.2 SearchCriteria <SchCrit>", "2.4.1.2.8 SettlementQuantity <SttlmQty>", "2.4.1.2.8.1 Quantity <Qty>", "2.4.1.2.8.1.1 Unit <Unit>", "2.4.1.2.8.1.1.1 FromQuantity <FrQty>"]
file_pages: [34]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 2.4.1.2.8.1.1.1 FromQuantity <FrQty>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 34 to 34.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 34

```text
Unit <Unit> contains one of the following QuantityRange1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromQuantity <FrQty> [1..1]  34
     Boundary <Bdry> [1..1] Quantity 34
     Included <Incl> [1..1] Indicator 34
Or   ToQuantity <ToQty> [1..1]  35
     Boundary <Bdry> [1..1] Quantity 35
     Included <Incl> [1..1] Indicator 35
Or   FromToQuantity <FrToQty> [1..1]  35
     FromQuantity <FrQty> [1..1]  35
       Boundary <Bdry> [1..1] Quantity 36
       Included <Incl> [1..1] Indicator 36
     ToQuantity <ToQty> [1..1]  36
       Boundary <Bdry> [1..1] Quantity 36
       Included <Incl> [1..1] Indicator 36
Or   EqualQuantity <EQQty> [1..1] Quantity 37
Or}   NotEqualQuantity <NEQQty> [1..1] Quantity 37
2.4.1.2.8.1.1.1  FromQuantity <FrQty>
Presence: [1..1]
Definition: Lower boundary of a range of quantity values.
FromQuantity <FrQty> contains the following QuantityRangeBoundary1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Boundary <Bdry> [1..1] Quantity 34
   Included <Incl> [1..1] Indicator 34
2.4.1.2.8.1.1.1.1  Boundary <Bdry>
Presence: [1..1]
Definition: Quantity value of the range limit.
Datatype: "DecimalNumber" on page 342
2.4.1.2.8.1.1.1.2  Included <Incl>
Presence: [1..1]
Definition: Indicates whether the boundary quantity is included in the range of quantity values.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 342):
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 34 September 2025
```

