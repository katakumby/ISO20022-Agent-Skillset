---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.2 Derivative4", "13.1.2.2.2 Option <Optn>", "13.1.2.2.2.15 ContractSize <CtrctSz>"]
file_pages: [185, 186]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.2.2.15 ContractSize <CtrctSz>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 185 to 186.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 185

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.2.2.2.15  ContractSize <CtrctSz>
Presence: [0..1]
Definition: Ratio or multiplying factor used to convert one contract into a quantity.
Datatype: "BaseOneRate" on page 532
13.1.2.2.2.16  AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>
Presence: [0..*]
Definition: Provides more information about the underlying instrument.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 185 March 2024
```

## File page 186

```text
AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> contains the following
UnderlyingAttributes4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AllocationPercentage <AllcnPctg> [0..1] Rate 187
   Quantity <Qty> [0..1]  187
{Or     Unit <Unit> [1..1] Quantity 187
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 187
   SettlementType <SttlmTp> [0..1]  187
{Or     Code <Cd> [1..1] CodeSet 188
Or}     Proprietary <Prtry> [1..1] ± 188
   CashAmount <CshAmt> [0..1] Amount C1, C5 188
   CashType <CshTp> [0..1] Text 189
   Price <Pric> [0..1]  189
     ValueType <ValTp> [0..1] CodeSet 189
     Value <Val> [1..1] ± 190
     PriceType <PricTp> [0..1] CodeSet 190
   DirtyPrice <DrtyPric> [0..1]  191
     ValueType <ValTp> [0..1] CodeSet 191
     Value <Val> [1..1] ± 192
     PriceType <PricTp> [0..1] CodeSet 192
   EndPrice <EndPric> [0..1]  193
     ValueType <ValTp> [0..1] CodeSet 193
     Value <Val> [1..1] ± 194
     PriceType <PricTp> [0..1] CodeSet 194
   StartValue <StartVal> [0..1] Amount C1, C5 195
   CurrentValue <CurVal> [0..1] Amount C1, C5 195
   EndValue <EndVal> [0..1] Amount C1, C5 196
   AdjustedQuantity <AdjstdQty> [0..1]  196
{Or     Unit <Unit> [1..1] Quantity 196
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 197
   ExchangeRate <XchgRate> [0..1] Rate 197
   CapValue <CapVal> [0..1] Amount C1, C5 197
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 186 March 2024
```

