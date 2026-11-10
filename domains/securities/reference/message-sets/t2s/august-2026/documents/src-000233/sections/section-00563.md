---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.4 Derivative <Deriv>", "27.4.2.2.4.2 Option <Optn>", "27.4.2.2.4.2.15 ContractSize <CtrctSz>"]
file_pages: [738, 739]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.4.2.15 ContractSize <CtrctSz>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 738 to 739.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 738

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
27.4.2.2.4.2.15  ContractSize <CtrctSz>
Presence: [0..1]
Definition: Ratio or multiplying factor used to convert one contract into a quantity.
Datatype: "BaseOneRate" on page 3324
27.4.2.2.4.2.16  AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>
Presence: [0..*]
Definition: Provides more information about the underlying instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 738 August 2026
```

## File page 739

```text
AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> contains the following
UnderlyingAttributes4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AllocationPercentage <AllcnPctg> [0..1] Rate 740
   Quantity <Qty> [0..1]  740
{Or     Unit <Unit> [1..1] Quantity 740
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 740
   SettlementType <SttlmTp> [0..1]  740
{Or     Code <Cd> [1..1] CodeSet 741
Or}     Proprietary <Prtry> [1..1] ± 741
   CashAmount <CshAmt> [0..1] Amount C1, C5 741
   CashType <CshTp> [0..1] Text 742
   Price <Pric> [0..1]  742
     ValueType <ValTp> [0..1] CodeSet 742
     Value <Val> [1..1] ± 743
     PriceType <PricTp> [0..1] CodeSet 743
   DirtyPrice <DrtyPric> [0..1]  744
     ValueType <ValTp> [0..1] CodeSet 744
     Value <Val> [1..1] ± 745
     PriceType <PricTp> [0..1] CodeSet 745
   EndPrice <EndPric> [0..1]  746
     ValueType <ValTp> [0..1] CodeSet 746
     Value <Val> [1..1] ± 747
     PriceType <PricTp> [0..1] CodeSet 747
   StartValue <StartVal> [0..1] Amount C1, C5 748
   CurrentValue <CurVal> [0..1] Amount C1, C5 748
   EndValue <EndVal> [0..1] Amount C1, C5 749
   AdjustedQuantity <AdjstdQty> [0..1]  749
{Or     Unit <Unit> [1..1] Quantity 749
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 750
   ExchangeRate <XchgRate> [0..1] Rate 750
   CapValue <CapVal> [0..1] Amount C1, C5 750
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 739 August 2026
```

