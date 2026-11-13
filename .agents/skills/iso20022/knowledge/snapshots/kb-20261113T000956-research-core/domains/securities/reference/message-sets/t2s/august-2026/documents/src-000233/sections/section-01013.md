---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.3.1.4 Derivative <Deriv>", "28.4.2.1.3.1.4.2 Option <Optn>", "28.4.2.1.3.1.4.2.15 ContractSize <CtrctSz>"]
file_pages: [1474, 1475]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.1.4.2.15 ContractSize <CtrctSz>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1474 to 1475.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1474

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
28.4.2.1.3.1.4.2.15  ContractSize <CtrctSz>
Presence: [0..1]
Definition: Ratio or multiplying factor used to convert one contract into a quantity.
Datatype: "BaseOneRate" on page 3324
28.4.2.1.3.1.4.2.16  AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>
Presence: [0..*]
Definition: Provides more information about the underlying instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1474 August 2026
```

## File page 1475

```text
AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> contains the following
UnderlyingAttributes4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AllocationPercentage <AllcnPctg> [0..1] Rate 1476
   Quantity <Qty> [0..1]  1476
{Or     Unit <Unit> [1..1] Quantity 1476
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1476
   SettlementType <SttlmTp> [0..1]  1476
{Or     Code <Cd> [1..1] CodeSet 1477
Or}     Proprietary <Prtry> [1..1] ± 1477
   CashAmount <CshAmt> [0..1] Amount C1, C5 1477
   CashType <CshTp> [0..1] Text 1478
   Price <Pric> [0..1]  1478
     ValueType <ValTp> [0..1] CodeSet 1478
     Value <Val> [1..1] ± 1479
     PriceType <PricTp> [0..1] CodeSet 1479
   DirtyPrice <DrtyPric> [0..1]  1480
     ValueType <ValTp> [0..1] CodeSet 1480
     Value <Val> [1..1] ± 1481
     PriceType <PricTp> [0..1] CodeSet 1481
   EndPrice <EndPric> [0..1]  1482
     ValueType <ValTp> [0..1] CodeSet 1482
     Value <Val> [1..1] ± 1483
     PriceType <PricTp> [0..1] CodeSet 1483
   StartValue <StartVal> [0..1] Amount C1, C5 1484
   CurrentValue <CurVal> [0..1] Amount C1, C5 1484
   EndValue <EndVal> [0..1] Amount C1, C5 1485
   AdjustedQuantity <AdjstdQty> [0..1]  1485
{Or     Unit <Unit> [1..1] Quantity 1485
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1486
   ExchangeRate <XchgRate> [0..1] Rate 1486
   CapValue <CapVal> [0..1] Amount C1, C5 1486
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1475 August 2026
```

