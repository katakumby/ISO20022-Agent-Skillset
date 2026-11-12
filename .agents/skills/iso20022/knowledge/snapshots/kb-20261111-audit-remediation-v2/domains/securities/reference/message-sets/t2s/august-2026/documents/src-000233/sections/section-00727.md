---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.1.1.4 Derivative <Deriv>", "28.4.2.1.1.1.4.2 Option <Optn>", "28.4.2.1.1.1.4.2.15 ContractSize <CtrctSz>"]
file_pages: [1098, 1099]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.1.4.2.15 ContractSize <CtrctSz>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1098 to 1099.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1098

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
28.4.2.1.1.1.4.2.15  ContractSize <CtrctSz>
Presence: [0..1]
Definition: Ratio or multiplying factor used to convert one contract into a quantity.
Datatype: "BaseOneRate" on page 3324
28.4.2.1.1.1.4.2.16  AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>
Presence: [0..*]
Definition: Provides more information about the underlying instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1098 August 2026
```

## File page 1099

```text
AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> contains the following
UnderlyingAttributes4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AllocationPercentage <AllcnPctg> [0..1] Rate 1100
   Quantity <Qty> [0..1]  1100
{Or     Unit <Unit> [1..1] Quantity 1100
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1100
   SettlementType <SttlmTp> [0..1]  1100
{Or     Code <Cd> [1..1] CodeSet 1101
Or}     Proprietary <Prtry> [1..1] ± 1101
   CashAmount <CshAmt> [0..1] Amount C1, C5 1101
   CashType <CshTp> [0..1] Text 1102
   Price <Pric> [0..1]  1102
     ValueType <ValTp> [0..1] CodeSet 1102
     Value <Val> [1..1] ± 1103
     PriceType <PricTp> [0..1] CodeSet 1103
   DirtyPrice <DrtyPric> [0..1]  1104
     ValueType <ValTp> [0..1] CodeSet 1104
     Value <Val> [1..1] ± 1105
     PriceType <PricTp> [0..1] CodeSet 1105
   EndPrice <EndPric> [0..1]  1106
     ValueType <ValTp> [0..1] CodeSet 1106
     Value <Val> [1..1] ± 1107
     PriceType <PricTp> [0..1] CodeSet 1107
   StartValue <StartVal> [0..1] Amount C1, C5 1108
   CurrentValue <CurVal> [0..1] Amount C1, C5 1108
   EndValue <EndVal> [0..1] Amount C1, C5 1109
   AdjustedQuantity <AdjstdQty> [0..1]  1109
{Or     Unit <Unit> [1..1] Quantity 1109
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1110
   ExchangeRate <XchgRate> [0..1] Rate 1110
   CapValue <CapVal> [0..1] Amount C1, C5 1110
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1099 August 2026
```

