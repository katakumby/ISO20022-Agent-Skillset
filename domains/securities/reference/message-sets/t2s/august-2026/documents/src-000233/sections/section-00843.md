---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.2.1.3 Debt <Debt>", "28.4.2.1.2.1.3.77 PriceRange <PricRg>"]
file_pages: [1250, 1251, 1252, 1253]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.1.3.77 PriceRange <PricRg>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1250 to 1253.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1250

```text
28.4.2.1.2.1.3.77  PriceRange <PricRg>
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
28.4.2.1.2.1.4  Derivative <Deriv>
Presence: [0..1]
Definition: Choice between type of derivatives.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1250 August 2026
```

## File page 1251

```text
Derivative <Deriv> contains the following Derivative4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Future <Futr> [0..1]  1254
     ContractSize <CtrctSz> [0..1] Rate 1256
     ExercisePrice <ExrcPric> [0..1]  1256
       ValueType <ValTp> [0..1] CodeSet 1256
       Value <Val> [1..1] ± 1257
       PriceType <PricTp> [0..1] CodeSet 1257
     FutureDate <FutrDt> [0..1] DateTime 1258
     MinimumSize <MinSz> [0..1] Amount C1, C5 1258
     UnitOfMeasure <UnitOfMeasr> [0..1]  1259
{Or       Code <Cd> [1..1] CodeSet 1259
Or}       Proprietary <Prtry> [1..1] ± 1261
     TimeUnit <TmUnit> [0..1]  1261
{Or       Code <Cd> [1..1] CodeSet 1262
Or}       Proprietary <Prtry> [1..1] ± 1262
     AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1262
       AllocationPercentage <AllcnPctg> [0..1] Rate 1264
       Quantity <Qty> [0..1]  1264
{Or         Unit <Unit> [1..1] Quantity 1264
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1264
       SettlementType <SttlmTp> [0..1]  1264
{Or         Code <Cd> [1..1] CodeSet 1265
Or}         Proprietary <Prtry> [1..1] ± 1265
       CashAmount <CshAmt> [0..1] Amount C1, C5 1265
       CashType <CshTp> [0..1] Text 1266
       Price <Pric> [0..1]  1266
         ValueType <ValTp> [0..1] CodeSet 1266
         Value <Val> [1..1] ± 1267
         PriceType <PricTp> [0..1] CodeSet 1267
       DirtyPrice <DrtyPric> [0..1]  1268
         ValueType <ValTp> [0..1] CodeSet 1268
         Value <Val> [1..1] ± 1269
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1251 August 2026
```

## File page 1252

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 1269
       EndPrice <EndPric> [0..1]  1270
         ValueType <ValTp> [0..1] CodeSet 1270
         Value <Val> [1..1] ± 1271
         PriceType <PricTp> [0..1] CodeSet 1271
       StartValue <StartVal> [0..1] Amount C1, C5 1272
       CurrentValue <CurVal> [0..1] Amount C1, C5 1272
       EndValue <EndVal> [0..1] Amount C1, C5 1273
       AdjustedQuantity <AdjstdQty> [0..1]  1273
{Or         Unit <Unit> [1..1] Quantity 1273
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1274
       ExchangeRate <XchgRate> [0..1] Rate 1274
       CapValue <CapVal> [0..1] Amount C1, C5 1274
   Option <Optn> [0..1]  1274
     OptionSettlementStyle <OptnSttlmStyle> [0..1]  1278
{Or       Code <Cd> [0..*] CodeSet 1278
Or}       Proprietary <Prtry> [1..1] ± 1278
     ConversionDate <ConvsDt> [0..1] DateTime 1278
     StrikePrice <StrkPric> [0..1]  1278
       ValueType <ValTp> [0..1] CodeSet 1279
       Value <Val> [1..1] ± 1279
       PriceType <PricTp> [0..1] CodeSet 1280
     MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1280
     ConversionPeriod <ConvsPrd> [0..1]  1281
{Or       FromDateTime <FrDtTm> [1..1] DateTime 1281
Or       ToDateTime <ToDtTm> [1..1] DateTime 1281
Or}       DateTimeRange <DtTmRg> [1..1] ± 1281
     OptionStyle <OptnStyle> [0..1]  1282
{Or       Code <Cd> [1..1] CodeSet 1282
Or}       Proprietary <Prtry> [1..1] ± 1282
     OptionType <OptnTp> [0..1] ± 1282
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1252 August 2026
```

## File page 1253

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     StrikeValue <StrkVal> [0..1] Quantity 1283
     StrikeMultiplier <StrkMltplr> [0..1] Quantity 1283
     InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  1283
{Or       Code <Cd> [1..1] CodeSet 1283
Or}       Proprietary <Prtry> [1..1] ± 1283
     VersionNumber <VrsnNb> [0..1] Quantity 1284
     ExpiryLocation <XpryLctn> [0..1] Text 1284
     Standardisation <Stdstn> [0..1]  1284
{Or       Code <Cd> [1..*] CodeSet 1284
Or}       Proprietary <Prtry> [1..1] ± 1285
     TradingPartyRole <TradgPtyRole> [0..1]  1285
{Or       Code <Cd> [1..*] CodeSet 1285
Or}       Proprietary <Prtry> [1..1] ± 1285
     ContractSize <CtrctSz> [0..1] Rate 1286
     AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1286
       AllocationPercentage <AllcnPctg> [0..1] Rate 1288
       Quantity <Qty> [0..1]  1288
{Or         Unit <Unit> [1..1] Quantity 1288
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1288
       SettlementType <SttlmTp> [0..1]  1288
{Or         Code <Cd> [1..1] CodeSet 1289
Or}         Proprietary <Prtry> [1..1] ± 1289
       CashAmount <CshAmt> [0..1] Amount C1, C5 1289
       CashType <CshTp> [0..1] Text 1290
       Price <Pric> [0..1]  1290
         ValueType <ValTp> [0..1] CodeSet 1290
         Value <Val> [1..1] ± 1291
         PriceType <PricTp> [0..1] CodeSet 1291
       DirtyPrice <DrtyPric> [0..1]  1292
         ValueType <ValTp> [0..1] CodeSet 1292
         Value <Val> [1..1] ± 1293
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1253 August 2026
```

