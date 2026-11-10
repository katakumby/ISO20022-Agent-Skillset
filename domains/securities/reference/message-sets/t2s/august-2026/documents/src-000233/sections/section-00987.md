---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.3.1.4 Derivative <Deriv>", "28.4.2.1.3.1.4.1 Future <Futr>"]
file_pages: [1442, 1443]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.1.4.1 Future <Futr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1442 to 1443.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1442

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 1481
       EndPrice <EndPric> [0..1]  1482
         ValueType <ValTp> [0..1] CodeSet 1482
         Value <Val> [1..1] ± 1483
         PriceType <PricTp> [0..1] CodeSet 1483
       StartValue <StartVal> [0..1] Amount C1, C5 1484
       CurrentValue <CurVal> [0..1] Amount C1, C5 1484
       EndValue <EndVal> [0..1] Amount C1, C5 1485
       AdjustedQuantity <AdjstdQty> [0..1]  1485
{Or         Unit <Unit> [1..1] Quantity 1485
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1486
       ExchangeRate <XchgRate> [0..1] Rate 1486
       CapValue <CapVal> [0..1] Amount C1, C5 1486
28.4.2.1.3.1.4.1  Future <Futr>
Presence: [0..1]
Definition: Parameters for contracts which obligate the buyer to receive and the seller to deliver in the
future the assets specified at an agreed price.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1442 August 2026
```

## File page 1443

```text
Future <Futr> contains the following Future4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ContractSize <CtrctSz> [0..1] Rate 1444
   ExercisePrice <ExrcPric> [0..1]  1444
     ValueType <ValTp> [0..1] CodeSet 1444
     Value <Val> [1..1] ± 1445
     PriceType <PricTp> [0..1] CodeSet 1445
   FutureDate <FutrDt> [0..1] DateTime 1446
   MinimumSize <MinSz> [0..1] Amount C1, C5 1446
   UnitOfMeasure <UnitOfMeasr> [0..1]  1447
{Or     Code <Cd> [1..1] CodeSet 1447
Or}     Proprietary <Prtry> [1..1] ± 1449
   TimeUnit <TmUnit> [0..1]  1449
{Or     Code <Cd> [1..1] CodeSet 1450
Or}     Proprietary <Prtry> [1..1] ± 1450
   AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1450
     AllocationPercentage <AllcnPctg> [0..1] Rate 1452
     Quantity <Qty> [0..1]  1452
{Or       Unit <Unit> [1..1] Quantity 1452
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1452
     SettlementType <SttlmTp> [0..1]  1452
{Or       Code <Cd> [1..1] CodeSet 1453
Or}       Proprietary <Prtry> [1..1] ± 1453
     CashAmount <CshAmt> [0..1] Amount C1, C5 1453
     CashType <CshTp> [0..1] Text 1454
     Price <Pric> [0..1]  1454
       ValueType <ValTp> [0..1] CodeSet 1454
       Value <Val> [1..1] ± 1455
       PriceType <PricTp> [0..1] CodeSet 1455
     DirtyPrice <DrtyPric> [0..1]  1456
       ValueType <ValTp> [0..1] CodeSet 1456
       Value <Val> [1..1] ± 1457
       PriceType <PricTp> [0..1] CodeSet 1457
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1443 August 2026
```

