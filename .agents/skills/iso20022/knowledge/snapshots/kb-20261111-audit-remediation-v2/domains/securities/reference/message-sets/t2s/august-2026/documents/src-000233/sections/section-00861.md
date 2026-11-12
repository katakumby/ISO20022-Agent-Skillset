---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.2.1.4 Derivative <Deriv>", "28.4.2.1.2.1.4.1 Future <Futr>", "28.4.2.1.2.1.4.1.7 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "28.4.2.1.2.1.4.1.7.12 AdjustedQuantity <AdjstdQty>", "28.4.2.1.2.1.4.1.7.12.2 FaceAmount <FaceAmt>"]
file_pages: [1274, 1275, 1276, 1277]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.1.4.1.7.12.2 FaceAmount <FaceAmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1274 to 1277.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1274

```text
Datatype: "DecimalNumber" on page 3324
28.4.2.1.2.1.4.1.7.12.2  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, ie, the principal, of a debt
instrument.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
28.4.2.1.2.1.4.1.7.13  ExchangeRate <XchgRate>
Presence: [0..1]
Definition: Foreign exchange rate used to compute the current value.
Datatype: "PercentageRate" on page 3325
28.4.2.1.2.1.4.1.7.14  CapValue <CapVal>
Presence: [0..1]
Definition: Maximum notional value for a financial instrument that is capped.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
28.4.2.1.2.1.4.2  Option <Optn>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1274 August 2026
```

## File page 1275

```text
Definition: Contracts which grant to the holder either the privilege to purchase or the privilege to sell the
assets specified at a predetermined price or formula at or within a time in the future.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1275 August 2026
```

## File page 1276

```text
Option <Optn> contains the following Option15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OptionSettlementStyle <OptnSttlmStyle> [0..1]  1278
{Or     Code <Cd> [0..*] CodeSet 1278
Or}     Proprietary <Prtry> [1..1] ± 1278
   ConversionDate <ConvsDt> [0..1] DateTime 1278
   StrikePrice <StrkPric> [0..1]  1278
     ValueType <ValTp> [0..1] CodeSet 1279
     Value <Val> [1..1] ± 1279
     PriceType <PricTp> [0..1] CodeSet 1280
   MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1280
   ConversionPeriod <ConvsPrd> [0..1]  1281
{Or     FromDateTime <FrDtTm> [1..1] DateTime 1281
Or     ToDateTime <ToDtTm> [1..1] DateTime 1281
Or}     DateTimeRange <DtTmRg> [1..1] ± 1281
   OptionStyle <OptnStyle> [0..1]  1282
{Or     Code <Cd> [1..1] CodeSet 1282
Or}     Proprietary <Prtry> [1..1] ± 1282
   OptionType <OptnTp> [0..1] ± 1282
   StrikeValue <StrkVal> [0..1] Quantity 1283
   StrikeMultiplier <StrkMltplr> [0..1] Quantity 1283
   InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  1283
{Or     Code <Cd> [1..1] CodeSet 1283
Or}     Proprietary <Prtry> [1..1] ± 1283
   VersionNumber <VrsnNb> [0..1] Quantity 1284
   ExpiryLocation <XpryLctn> [0..1] Text 1284
   Standardisation <Stdstn> [0..1]  1284
{Or     Code <Cd> [1..*] CodeSet 1284
Or}     Proprietary <Prtry> [1..1] ± 1285
   TradingPartyRole <TradgPtyRole> [0..1]  1285
{Or     Code <Cd> [1..*] CodeSet 1285
Or}     Proprietary <Prtry> [1..1] ± 1285
   ContractSize <CtrctSz> [0..1] Rate 1286
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1276 August 2026
```

## File page 1277

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1286
     AllocationPercentage <AllcnPctg> [0..1] Rate 1288
     Quantity <Qty> [0..1]  1288
{Or       Unit <Unit> [1..1] Quantity 1288
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1288
     SettlementType <SttlmTp> [0..1]  1288
{Or       Code <Cd> [1..1] CodeSet 1289
Or}       Proprietary <Prtry> [1..1] ± 1289
     CashAmount <CshAmt> [0..1] Amount C1, C5 1289
     CashType <CshTp> [0..1] Text 1290
     Price <Pric> [0..1]  1290
       ValueType <ValTp> [0..1] CodeSet 1290
       Value <Val> [1..1] ± 1291
       PriceType <PricTp> [0..1] CodeSet 1291
     DirtyPrice <DrtyPric> [0..1]  1292
       ValueType <ValTp> [0..1] CodeSet 1292
       Value <Val> [1..1] ± 1293
       PriceType <PricTp> [0..1] CodeSet 1293
     EndPrice <EndPric> [0..1]  1294
       ValueType <ValTp> [0..1] CodeSet 1294
       Value <Val> [1..1] ± 1295
       PriceType <PricTp> [0..1] CodeSet 1295
     StartValue <StartVal> [0..1] Amount C1, C5 1296
     CurrentValue <CurVal> [0..1] Amount C1, C5 1296
     EndValue <EndVal> [0..1] Amount C1, C5 1297
     AdjustedQuantity <AdjstdQty> [0..1]  1297
{Or       Unit <Unit> [1..1] Quantity 1297
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1298
     ExchangeRate <XchgRate> [0..1] Rate 1298
     CapValue <CapVal> [0..1] Amount C1, C5 1298
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1277 August 2026
```

