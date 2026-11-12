---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.2.1.4 Derivative <Deriv>", "28.4.2.2.1.4.2 Option <Optn>", "28.4.2.2.1.4.2.15 ContractSize <CtrctSz>"]
file_pages: [1662, 1663]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.1.4.2.15 ContractSize <CtrctSz>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1662 to 1663.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1662

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
28.4.2.2.1.4.2.15  ContractSize <CtrctSz>
Presence: [0..1]
Definition: Ratio or multiplying factor used to convert one contract into a quantity.
Datatype: "BaseOneRate" on page 3324
28.4.2.2.1.4.2.16  AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>
Presence: [0..*]
Definition: Provides more information about the underlying instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1662 August 2026
```

## File page 1663

```text
AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> contains the following
UnderlyingAttributes4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AllocationPercentage <AllcnPctg> [0..1] Rate 1664
   Quantity <Qty> [0..1]  1664
{Or     Unit <Unit> [1..1] Quantity 1664
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1664
   SettlementType <SttlmTp> [0..1]  1664
{Or     Code <Cd> [1..1] CodeSet 1665
Or}     Proprietary <Prtry> [1..1] ± 1665
   CashAmount <CshAmt> [0..1] Amount C1, C5 1665
   CashType <CshTp> [0..1] Text 1666
   Price <Pric> [0..1]  1666
     ValueType <ValTp> [0..1] CodeSet 1666
     Value <Val> [1..1] ± 1667
     PriceType <PricTp> [0..1] CodeSet 1667
   DirtyPrice <DrtyPric> [0..1]  1668
     ValueType <ValTp> [0..1] CodeSet 1668
     Value <Val> [1..1] ± 1669
     PriceType <PricTp> [0..1] CodeSet 1669
   EndPrice <EndPric> [0..1]  1670
     ValueType <ValTp> [0..1] CodeSet 1670
     Value <Val> [1..1] ± 1671
     PriceType <PricTp> [0..1] CodeSet 1671
   StartValue <StartVal> [0..1] Amount C1, C5 1672
   CurrentValue <CurVal> [0..1] Amount C1, C5 1672
   EndValue <EndVal> [0..1] Amount C1, C5 1673
   AdjustedQuantity <AdjstdQty> [0..1]  1673
{Or     Unit <Unit> [1..1] Quantity 1673
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1674
   ExchangeRate <XchgRate> [0..1] Rate 1674
   CapValue <CapVal> [0..1] Amount C1, C5 1674
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1663 August 2026
```

