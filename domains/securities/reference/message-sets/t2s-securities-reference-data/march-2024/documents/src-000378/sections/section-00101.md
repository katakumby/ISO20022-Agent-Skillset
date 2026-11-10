---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.2 Derivative4", "13.1.2.2.1 Future <Futr>"]
file_pages: [153, 154]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.2.1 Future <Futr>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 153 to 154.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 153

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 192
       EndPrice <EndPric> [0..1]  193
         ValueType <ValTp> [0..1] CodeSet 193
         Value <Val> [1..1] ± 194
         PriceType <PricTp> [0..1] CodeSet 194
       StartValue <StartVal> [0..1] Amount C1, C5 195
       CurrentValue <CurVal> [0..1] Amount C1, C5 195
       EndValue <EndVal> [0..1] Amount C1, C5 196
       AdjustedQuantity <AdjstdQty> [0..1]  196
{Or         Unit <Unit> [1..1] Quantity 196
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 197
       ExchangeRate <XchgRate> [0..1] Rate 197
       CapValue <CapVal> [0..1] Amount C1, C5 197
13.1.2.2.1  Future <Futr>
Presence: [0..1]
Definition: Parameters for contracts which obligate the buyer to receive and the seller to deliver in the
future the assets specified at an agreed price.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 153 March 2024
```

## File page 154

```text
Future <Futr> contains the following Future4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ContractSize <CtrctSz> [0..1] Rate 155
   ExercisePrice <ExrcPric> [0..1]  155
     ValueType <ValTp> [0..1] CodeSet 155
     Value <Val> [1..1] ± 156
     PriceType <PricTp> [0..1] CodeSet 156
   FutureDate <FutrDt> [0..1] DateTime 157
   MinimumSize <MinSz> [0..1] Amount C1, C5 157
   UnitOfMeasure <UnitOfMeasr> [0..1]  158
{Or     Code <Cd> [1..1] CodeSet 158
Or}     Proprietary <Prtry> [1..1] ± 160
   TimeUnit <TmUnit> [0..1]  160
{Or     Code <Cd> [1..1] CodeSet 161
Or}     Proprietary <Prtry> [1..1] ± 161
   AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  161
     AllocationPercentage <AllcnPctg> [0..1] Rate 163
     Quantity <Qty> [0..1]  163
{Or       Unit <Unit> [1..1] Quantity 163
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 163
     SettlementType <SttlmTp> [0..1]  163
{Or       Code <Cd> [1..1] CodeSet 164
Or}       Proprietary <Prtry> [1..1] ± 164
     CashAmount <CshAmt> [0..1] Amount C1, C5 164
     CashType <CshTp> [0..1] Text 165
     Price <Pric> [0..1]  165
       ValueType <ValTp> [0..1] CodeSet 165
       Value <Val> [1..1] ± 166
       PriceType <PricTp> [0..1] CodeSet 166
     DirtyPrice <DrtyPric> [0..1]  167
       ValueType <ValTp> [0..1] CodeSet 167
       Value <Val> [1..1] ± 168
       PriceType <PricTp> [0..1] CodeSet 168
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 154 March 2024
```

