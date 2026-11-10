---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks", "3.4.1 QueryDefinition <QryDef>", "3.4.1.2 SearchCriteria <SchCrit>", "3.4.1.2.12 SettledQuantity <SttldQty>", "3.4.1.2.12.1 Quantity <Qty>", "3.4.1.2.12.1.1 Unit <Unit>", "3.4.1.2.12.1.1.1 FromQuantity <FrQty>"]
file_pages: [55]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 3.4.1.2.12.1.1.1 FromQuantity <FrQty>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 55 to 55.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 55

```text
Unit <Unit> contains one of the following QuantityRange1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromQuantity <FrQty> [1..1]  55
     Boundary <Bdry> [1..1] Quantity 55
     Included <Incl> [1..1] Indicator 55
Or   ToQuantity <ToQty> [1..1]  56
     Boundary <Bdry> [1..1] Quantity 56
     Included <Incl> [1..1] Indicator 56
Or   FromToQuantity <FrToQty> [1..1]  56
     FromQuantity <FrQty> [1..1]  56
       Boundary <Bdry> [1..1] Quantity 57
       Included <Incl> [1..1] Indicator 57
     ToQuantity <ToQty> [1..1]  57
       Boundary <Bdry> [1..1] Quantity 57
       Included <Incl> [1..1] Indicator 57
Or   EqualQuantity <EQQty> [1..1] Quantity 58
Or}   NotEqualQuantity <NEQQty> [1..1] Quantity 58
3.4.1.2.12.1.1.1  FromQuantity <FrQty>
Presence: [1..1]
Definition: Lower boundary of a range of quantity values.
FromQuantity <FrQty> contains the following QuantityRangeBoundary1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Boundary <Bdry> [1..1] Quantity 55
   Included <Incl> [1..1] Indicator 55
3.4.1.2.12.1.1.1.1  Boundary <Bdry>
Presence: [1..1]
Definition: Quantity value of the range limit.
Datatype: "DecimalNumber" on page 554
3.4.1.2.12.1.1.1.2  Included <Incl>
Presence: [1..1]
Definition: Indicates whether the boundary quantity is included in the range of quantity values.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 55 March 2026
```

