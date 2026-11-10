---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks", "3.4.1 QueryDefinition <QryDef>", "3.4.1.2 SearchCriteria <SchCrit>", "3.4.1.2.12 SettledQuantity <SttldQty>", "3.4.1.2.12.1 Quantity <Qty>", "3.4.1.2.12.1.1 Unit <Unit>", "3.4.1.2.12.1.1.2 ToQuantity <ToQty>"]
file_pages: [56]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 3.4.1.2.12.1.1.2 ToQuantity <ToQty>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 56 to 56.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 56

```text
• Meaning When True: Yes
• Meaning When False: No
3.4.1.2.12.1.1.2  ToQuantity <ToQty>
Presence: [1..1]
Definition: Upper boundary of a range of quantity values.
ToQuantity <ToQty> contains the following QuantityRangeBoundary1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Boundary <Bdry> [1..1] Quantity 56
   Included <Incl> [1..1] Indicator 56
3.4.1.2.12.1.1.2.1  Boundary <Bdry>
Presence: [1..1]
Definition: Quantity value of the range limit.
Datatype: "DecimalNumber" on page 554
3.4.1.2.12.1.1.2.2  Included <Incl>
Presence: [1..1]
Definition: Indicates whether the boundary quantity is included in the range of quantity values.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
• Meaning When True: Yes
• Meaning When False: No
3.4.1.2.12.1.1.3  FromToQuantity <FrToQty>
Presence: [1..1]
Definition: Range of valid quantity values.
FromToQuantity <FrToQty> contains the following FromToQuantityRange1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromQuantity <FrQty> [1..1]  56
     Boundary <Bdry> [1..1] Quantity 57
     Included <Incl> [1..1] Indicator 57
   ToQuantity <ToQty> [1..1]  57
     Boundary <Bdry> [1..1] Quantity 57
     Included <Incl> [1..1] Indicator 57
3.4.1.2.12.1.1.3.1  FromQuantity <FrQty>
Presence: [1..1]
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 56 March 2026
```

