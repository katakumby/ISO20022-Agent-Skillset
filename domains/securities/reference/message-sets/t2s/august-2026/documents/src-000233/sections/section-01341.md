---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.4 Derivative <Deriv>", "32.4.3.1.1.2.4.2 Option <Optn>", "32.4.3.1.1.2.4.2.15 ContractSize <CtrctSz>"]
file_pages: [1940, 1941]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.4.2.15 ContractSize <CtrctSz>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1940 to 1941.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1940

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
32.4.3.1.1.2.4.2.15  ContractSize <CtrctSz>
Presence: [0..1]
Definition: Ratio or multiplying factor used to convert one contract into a quantity.
Datatype: "BaseOneRate" on page 3324
32.4.3.1.1.2.4.2.16  AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>
Presence: [0..*]
Definition: Provides more information about the underlying instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1940 August 2026
```

## File page 1941

```text
AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> contains the following
UnderlyingAttributes4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AllocationPercentage <AllcnPctg> [0..1] Rate 1942
   Quantity <Qty> [0..1]  1942
{Or     Unit <Unit> [1..1] Quantity 1942
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1942
   SettlementType <SttlmTp> [0..1]  1942
{Or     Code <Cd> [1..1] CodeSet 1943
Or}     Proprietary <Prtry> [1..1] ± 1943
   CashAmount <CshAmt> [0..1] Amount C1, C5 1943
   CashType <CshTp> [0..1] Text 1944
   Price <Pric> [0..1]  1944
     ValueType <ValTp> [0..1] CodeSet 1944
     Value <Val> [1..1] ± 1945
     PriceType <PricTp> [0..1] CodeSet 1945
   DirtyPrice <DrtyPric> [0..1]  1946
     ValueType <ValTp> [0..1] CodeSet 1946
     Value <Val> [1..1] ± 1947
     PriceType <PricTp> [0..1] CodeSet 1947
   EndPrice <EndPric> [0..1]  1948
     ValueType <ValTp> [0..1] CodeSet 1948
     Value <Val> [1..1] ± 1949
     PriceType <PricTp> [0..1] CodeSet 1949
   StartValue <StartVal> [0..1] Amount C1, C5 1950
   CurrentValue <CurVal> [0..1] Amount C1, C5 1950
   EndValue <EndVal> [0..1] Amount C1, C5 1951
   AdjustedQuantity <AdjstdQty> [0..1]  1951
{Or     Unit <Unit> [1..1] Quantity 1951
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1952
   ExchangeRate <XchgRate> [0..1] Rate 1952
   CapValue <CapVal> [0..1] Amount C1, C5 1952
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1941 August 2026
```

