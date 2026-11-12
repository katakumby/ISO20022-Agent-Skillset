---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.2 Derivative4", "13.1.2.2.1 Future <Futr>", "13.1.2.2.1.1 ContractSize <CtrctSz>"]
file_pages: [155]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.2.1.1 ContractSize <CtrctSz>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 155 to 155.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 155

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     EndPrice <EndPric> [0..1]  169
       ValueType <ValTp> [0..1] CodeSet 169
       Value <Val> [1..1] ± 170
       PriceType <PricTp> [0..1] CodeSet 170
     StartValue <StartVal> [0..1] Amount C1, C5 171
     CurrentValue <CurVal> [0..1] Amount C1, C5 171
     EndValue <EndVal> [0..1] Amount C1, C5 172
     AdjustedQuantity <AdjstdQty> [0..1]  172
{Or       Unit <Unit> [1..1] Quantity 172
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 173
     ExchangeRate <XchgRate> [0..1] Rate 173
     CapValue <CapVal> [0..1] Amount C1, C5 173
13.1.2.2.1.1  ContractSize <CtrctSz>
Presence: [0..1]
Definition: Ratio or multiplying factor used to convert one contract into a quantity.
Datatype: "BaseOneRate" on page 532
13.1.2.2.1.2  ExercisePrice <ExrcPric>
Presence: [0..1]
Definition: Predetermined price at which the holder of a Future will have to buy or sell the underlying
instrument.
ExercisePrice <ExrcPric> contains the following Price8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValueType <ValTp> [0..1] CodeSet 155
   Value <Val> [1..1] ± 156
   PriceType <PricTp> [0..1] CodeSet 156
13.1.2.2.1.2.1  ValueType <ValTp>
Presence: [0..1]
Definition: Type of value in which the price is expressed.
Datatype: "PriceValueType3Code" on page 521
CodeName Name Definition
DISC Discount Price expressed as a number of
percentage points below par, for
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 155 March 2024
```

