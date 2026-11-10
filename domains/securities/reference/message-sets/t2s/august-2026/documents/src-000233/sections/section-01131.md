---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.2.1.4 Derivative <Deriv>", "28.4.2.2.1.4.1 Future <Futr>", "28.4.2.2.1.4.1.1 ContractSize <CtrctSz>"]
file_pages: [1632]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.1.4.1.1 ContractSize <CtrctSz>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1632 to 1632.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1632

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     EndPrice <EndPric> [0..1]  1646
       ValueType <ValTp> [0..1] CodeSet 1646
       Value <Val> [1..1] ± 1647
       PriceType <PricTp> [0..1] CodeSet 1647
     StartValue <StartVal> [0..1] Amount C1, C5 1648
     CurrentValue <CurVal> [0..1] Amount C1, C5 1648
     EndValue <EndVal> [0..1] Amount C1, C5 1649
     AdjustedQuantity <AdjstdQty> [0..1]  1649
{Or       Unit <Unit> [1..1] Quantity 1649
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1650
     ExchangeRate <XchgRate> [0..1] Rate 1650
     CapValue <CapVal> [0..1] Amount C1, C5 1650
28.4.2.2.1.4.1.1  ContractSize <CtrctSz>
Presence: [0..1]
Definition: Ratio or multiplying factor used to convert one contract into a quantity.
Datatype: "BaseOneRate" on page 3324
28.4.2.2.1.4.1.2  ExercisePrice <ExrcPric>
Presence: [0..1]
Definition: Predetermined price at which the holder of a Future will have to buy or sell the underlying
instrument.
ExercisePrice <ExrcPric> contains the following Price8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValueType <ValTp> [0..1] CodeSet 1632
   Value <Val> [1..1] ± 1633
   PriceType <PricTp> [0..1] CodeSet 1633
28.4.2.2.1.4.1.2.1  ValueType <ValTp>
Presence: [0..1]
Definition: Type of value in which the price is expressed.
Datatype: "PriceValueType3Code" on page 3281
CodeName Name Definition
DISC Discount Price expressed as a number of
percentage points below par, for
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1632 August 2026
```

