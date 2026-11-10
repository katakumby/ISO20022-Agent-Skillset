---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.4 Derivative <Deriv>", "32.4.3.1.1.2.4.1 Future <Futr>", "32.4.3.1.1.2.4.1.1 ContractSize <CtrctSz>"]
file_pages: [1910]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.4.1.1 ContractSize <CtrctSz>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1910 to 1910.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1910

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     EndPrice <EndPric> [0..1]  1924
       ValueType <ValTp> [0..1] CodeSet 1924
       Value <Val> [1..1] ± 1925
       PriceType <PricTp> [0..1] CodeSet 1925
     StartValue <StartVal> [0..1] Amount C1, C5 1926
     CurrentValue <CurVal> [0..1] Amount C1, C5 1926
     EndValue <EndVal> [0..1] Amount C1, C5 1927
     AdjustedQuantity <AdjstdQty> [0..1]  1927
{Or       Unit <Unit> [1..1] Quantity 1927
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1928
     ExchangeRate <XchgRate> [0..1] Rate 1928
     CapValue <CapVal> [0..1] Amount C1, C5 1928
32.4.3.1.1.2.4.1.1  ContractSize <CtrctSz>
Presence: [0..1]
Definition: Ratio or multiplying factor used to convert one contract into a quantity.
Datatype: "BaseOneRate" on page 3324
32.4.3.1.1.2.4.1.2  ExercisePrice <ExrcPric>
Presence: [0..1]
Definition: Predetermined price at which the holder of a Future will have to buy or sell the underlying
instrument.
ExercisePrice <ExrcPric> contains the following Price8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValueType <ValTp> [0..1] CodeSet 1910
   Value <Val> [1..1] ± 1911
   PriceType <PricTp> [0..1] CodeSet 1911
32.4.3.1.1.2.4.1.2.1  ValueType <ValTp>
Presence: [0..1]
Definition: Type of value in which the price is expressed.
Datatype: "PriceValueType3Code" on page 3281
CodeName Name Definition
DISC Discount Price expressed as a number of
percentage points below par, for
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1910 August 2026
```

