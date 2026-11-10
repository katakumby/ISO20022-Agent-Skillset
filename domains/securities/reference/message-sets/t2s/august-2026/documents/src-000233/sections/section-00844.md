---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.2.1.4 Derivative <Deriv>", "28.4.2.1.2.1.4.1 Future <Futr>"]
file_pages: [1254, 1255]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.1.4.1 Future <Futr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1254 to 1255.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1254

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 1293
       EndPrice <EndPric> [0..1]  1294
         ValueType <ValTp> [0..1] CodeSet 1294
         Value <Val> [1..1] ± 1295
         PriceType <PricTp> [0..1] CodeSet 1295
       StartValue <StartVal> [0..1] Amount C1, C5 1296
       CurrentValue <CurVal> [0..1] Amount C1, C5 1296
       EndValue <EndVal> [0..1] Amount C1, C5 1297
       AdjustedQuantity <AdjstdQty> [0..1]  1297
{Or         Unit <Unit> [1..1] Quantity 1297
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1298
       ExchangeRate <XchgRate> [0..1] Rate 1298
       CapValue <CapVal> [0..1] Amount C1, C5 1298
28.4.2.1.2.1.4.1  Future <Futr>
Presence: [0..1]
Definition: Parameters for contracts which obligate the buyer to receive and the seller to deliver in the
future the assets specified at an agreed price.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1254 August 2026
```

## File page 1255

```text
Future <Futr> contains the following Future4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ContractSize <CtrctSz> [0..1] Rate 1256
   ExercisePrice <ExrcPric> [0..1]  1256
     ValueType <ValTp> [0..1] CodeSet 1256
     Value <Val> [1..1] ± 1257
     PriceType <PricTp> [0..1] CodeSet 1257
   FutureDate <FutrDt> [0..1] DateTime 1258
   MinimumSize <MinSz> [0..1] Amount C1, C5 1258
   UnitOfMeasure <UnitOfMeasr> [0..1]  1259
{Or     Code <Cd> [1..1] CodeSet 1259
Or}     Proprietary <Prtry> [1..1] ± 1261
   TimeUnit <TmUnit> [0..1]  1261
{Or     Code <Cd> [1..1] CodeSet 1262
Or}     Proprietary <Prtry> [1..1] ± 1262
   AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1262
     AllocationPercentage <AllcnPctg> [0..1] Rate 1264
     Quantity <Qty> [0..1]  1264
{Or       Unit <Unit> [1..1] Quantity 1264
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1264
     SettlementType <SttlmTp> [0..1]  1264
{Or       Code <Cd> [1..1] CodeSet 1265
Or}       Proprietary <Prtry> [1..1] ± 1265
     CashAmount <CshAmt> [0..1] Amount C1, C5 1265
     CashType <CshTp> [0..1] Text 1266
     Price <Pric> [0..1]  1266
       ValueType <ValTp> [0..1] CodeSet 1266
       Value <Val> [1..1] ± 1267
       PriceType <PricTp> [0..1] CodeSet 1267
     DirtyPrice <DrtyPric> [0..1]  1268
       ValueType <ValTp> [0..1] CodeSet 1268
       Value <Val> [1..1] ± 1269
       PriceType <PricTp> [0..1] CodeSet 1269
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1255 August 2026
```

