---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.3.1.3 Debt <Debt>", "28.4.2.1.3.1.3.77 PriceRange <PricRg>"]
file_pages: [1438, 1439, 1440, 1441]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.1.3.77 PriceRange <PricRg>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1438 to 1441.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1438

```text
28.4.2.1.3.1.3.77  PriceRange <PricRg>
Presence: [0..1]
Definition: Indicates a search criterion used when looking to buy a bond within a particular price range.
PriceRange <PricRg> contains the following elements (see "AmountOrPercentageRange1" on
page 3003 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Operation <Opr> [0..1] CodeSet 3003
   Term <Term> [0..10]  3003
     Operator <Oprtr> [1..1] CodeSet 3003
     Value <Val> [1..1]  3004
{Or       RateValue <RateVal> [1..1] Rate 3004
Or}       AbsoluteValue <AbsVal> [1..1] Quantity 3004
28.4.2.1.3.1.4  Derivative <Deriv>
Presence: [0..1]
Definition: Choice between type of derivatives.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1438 August 2026
```

## File page 1439

```text
Derivative <Deriv> contains the following Derivative4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Future <Futr> [0..1]  1442
     ContractSize <CtrctSz> [0..1] Rate 1444
     ExercisePrice <ExrcPric> [0..1]  1444
       ValueType <ValTp> [0..1] CodeSet 1444
       Value <Val> [1..1] ± 1445
       PriceType <PricTp> [0..1] CodeSet 1445
     FutureDate <FutrDt> [0..1] DateTime 1446
     MinimumSize <MinSz> [0..1] Amount C1, C5 1446
     UnitOfMeasure <UnitOfMeasr> [0..1]  1447
{Or       Code <Cd> [1..1] CodeSet 1447
Or}       Proprietary <Prtry> [1..1] ± 1449
     TimeUnit <TmUnit> [0..1]  1449
{Or       Code <Cd> [1..1] CodeSet 1450
Or}       Proprietary <Prtry> [1..1] ± 1450
     AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1450
       AllocationPercentage <AllcnPctg> [0..1] Rate 1452
       Quantity <Qty> [0..1]  1452
{Or         Unit <Unit> [1..1] Quantity 1452
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1452
       SettlementType <SttlmTp> [0..1]  1452
{Or         Code <Cd> [1..1] CodeSet 1453
Or}         Proprietary <Prtry> [1..1] ± 1453
       CashAmount <CshAmt> [0..1] Amount C1, C5 1453
       CashType <CshTp> [0..1] Text 1454
       Price <Pric> [0..1]  1454
         ValueType <ValTp> [0..1] CodeSet 1454
         Value <Val> [1..1] ± 1455
         PriceType <PricTp> [0..1] CodeSet 1455
       DirtyPrice <DrtyPric> [0..1]  1456
         ValueType <ValTp> [0..1] CodeSet 1456
         Value <Val> [1..1] ± 1457
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1439 August 2026
```

## File page 1440

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 1457
       EndPrice <EndPric> [0..1]  1458
         ValueType <ValTp> [0..1] CodeSet 1458
         Value <Val> [1..1] ± 1459
         PriceType <PricTp> [0..1] CodeSet 1459
       StartValue <StartVal> [0..1] Amount C1, C5 1460
       CurrentValue <CurVal> [0..1] Amount C1, C5 1460
       EndValue <EndVal> [0..1] Amount C1, C5 1461
       AdjustedQuantity <AdjstdQty> [0..1]  1461
{Or         Unit <Unit> [1..1] Quantity 1461
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1462
       ExchangeRate <XchgRate> [0..1] Rate 1462
       CapValue <CapVal> [0..1] Amount C1, C5 1462
   Option <Optn> [0..1]  1462
     OptionSettlementStyle <OptnSttlmStyle> [0..1]  1466
{Or       Code <Cd> [0..*] CodeSet 1466
Or}       Proprietary <Prtry> [1..1] ± 1466
     ConversionDate <ConvsDt> [0..1] DateTime 1466
     StrikePrice <StrkPric> [0..1]  1466
       ValueType <ValTp> [0..1] CodeSet 1467
       Value <Val> [1..1] ± 1467
       PriceType <PricTp> [0..1] CodeSet 1468
     MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1468
     ConversionPeriod <ConvsPrd> [0..1]  1469
{Or       FromDateTime <FrDtTm> [1..1] DateTime 1469
Or       ToDateTime <ToDtTm> [1..1] DateTime 1469
Or}       DateTimeRange <DtTmRg> [1..1] ± 1469
     OptionStyle <OptnStyle> [0..1]  1470
{Or       Code <Cd> [1..1] CodeSet 1470
Or}       Proprietary <Prtry> [1..1] ± 1470
     OptionType <OptnTp> [0..1] ± 1470
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1440 August 2026
```

## File page 1441

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     StrikeValue <StrkVal> [0..1] Quantity 1471
     StrikeMultiplier <StrkMltplr> [0..1] Quantity 1471
     InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  1471
{Or       Code <Cd> [1..1] CodeSet 1471
Or}       Proprietary <Prtry> [1..1] ± 1471
     VersionNumber <VrsnNb> [0..1] Quantity 1472
     ExpiryLocation <XpryLctn> [0..1] Text 1472
     Standardisation <Stdstn> [0..1]  1472
{Or       Code <Cd> [1..*] CodeSet 1472
Or}       Proprietary <Prtry> [1..1] ± 1473
     TradingPartyRole <TradgPtyRole> [0..1]  1473
{Or       Code <Cd> [1..*] CodeSet 1473
Or}       Proprietary <Prtry> [1..1] ± 1473
     ContractSize <CtrctSz> [0..1] Rate 1474
     AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1474
       AllocationPercentage <AllcnPctg> [0..1] Rate 1476
       Quantity <Qty> [0..1]  1476
{Or         Unit <Unit> [1..1] Quantity 1476
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1476
       SettlementType <SttlmTp> [0..1]  1476
{Or         Code <Cd> [1..1] CodeSet 1477
Or}         Proprietary <Prtry> [1..1] ± 1477
       CashAmount <CshAmt> [0..1] Amount C1, C5 1477
       CashType <CshTp> [0..1] Text 1478
       Price <Pric> [0..1]  1478
         ValueType <ValTp> [0..1] CodeSet 1478
         Value <Val> [1..1] ± 1479
         PriceType <PricTp> [0..1] CodeSet 1479
       DirtyPrice <DrtyPric> [0..1]  1480
         ValueType <ValTp> [0..1] CodeSet 1480
         Value <Val> [1..1] ± 1481
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1441 August 2026
```

