---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.3.1.4 Derivative <Deriv>", "28.4.2.1.3.1.4.1 Future <Futr>", "28.4.2.1.3.1.4.1.7 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "28.4.2.1.3.1.4.1.7.12 AdjustedQuantity <AdjstdQty>", "28.4.2.1.3.1.4.1.7.12.2 FaceAmount <FaceAmt>"]
file_pages: [1462, 1463, 1464, 1465]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.1.4.1.7.12.2 FaceAmount <FaceAmt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1462 to 1465.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1462

```text
Datatype: "DecimalNumber" on page 3324
28.4.2.1.3.1.4.1.7.12.2  FaceAmount <FaceAmt>
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
28.4.2.1.3.1.4.1.7.13  ExchangeRate <XchgRate>
Presence: [0..1]
Definition: Foreign exchange rate used to compute the current value.
Datatype: "PercentageRate" on page 3325
28.4.2.1.3.1.4.1.7.14  CapValue <CapVal>
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
28.4.2.1.3.1.4.2  Option <Optn>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1462 August 2026
```

## File page 1463

```text
Definition: Contracts which grant to the holder either the privilege to purchase or the privilege to sell the
assets specified at a predetermined price or formula at or within a time in the future.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1463 August 2026
```

## File page 1464

```text
Option <Optn> contains the following Option15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OptionSettlementStyle <OptnSttlmStyle> [0..1]  1466
{Or     Code <Cd> [0..*] CodeSet 1466
Or}     Proprietary <Prtry> [1..1] ± 1466
   ConversionDate <ConvsDt> [0..1] DateTime 1466
   StrikePrice <StrkPric> [0..1]  1466
     ValueType <ValTp> [0..1] CodeSet 1467
     Value <Val> [1..1] ± 1467
     PriceType <PricTp> [0..1] CodeSet 1468
   MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1468
   ConversionPeriod <ConvsPrd> [0..1]  1469
{Or     FromDateTime <FrDtTm> [1..1] DateTime 1469
Or     ToDateTime <ToDtTm> [1..1] DateTime 1469
Or}     DateTimeRange <DtTmRg> [1..1] ± 1469
   OptionStyle <OptnStyle> [0..1]  1470
{Or     Code <Cd> [1..1] CodeSet 1470
Or}     Proprietary <Prtry> [1..1] ± 1470
   OptionType <OptnTp> [0..1] ± 1470
   StrikeValue <StrkVal> [0..1] Quantity 1471
   StrikeMultiplier <StrkMltplr> [0..1] Quantity 1471
   InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  1471
{Or     Code <Cd> [1..1] CodeSet 1471
Or}     Proprietary <Prtry> [1..1] ± 1471
   VersionNumber <VrsnNb> [0..1] Quantity 1472
   ExpiryLocation <XpryLctn> [0..1] Text 1472
   Standardisation <Stdstn> [0..1]  1472
{Or     Code <Cd> [1..*] CodeSet 1472
Or}     Proprietary <Prtry> [1..1] ± 1473
   TradingPartyRole <TradgPtyRole> [0..1]  1473
{Or     Code <Cd> [1..*] CodeSet 1473
Or}     Proprietary <Prtry> [1..1] ± 1473
   ContractSize <CtrctSz> [0..1] Rate 1474
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1464 August 2026
```

## File page 1465

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1474
     AllocationPercentage <AllcnPctg> [0..1] Rate 1476
     Quantity <Qty> [0..1]  1476
{Or       Unit <Unit> [1..1] Quantity 1476
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1476
     SettlementType <SttlmTp> [0..1]  1476
{Or       Code <Cd> [1..1] CodeSet 1477
Or}       Proprietary <Prtry> [1..1] ± 1477
     CashAmount <CshAmt> [0..1] Amount C1, C5 1477
     CashType <CshTp> [0..1] Text 1478
     Price <Pric> [0..1]  1478
       ValueType <ValTp> [0..1] CodeSet 1478
       Value <Val> [1..1] ± 1479
       PriceType <PricTp> [0..1] CodeSet 1479
     DirtyPrice <DrtyPric> [0..1]  1480
       ValueType <ValTp> [0..1] CodeSet 1480
       Value <Val> [1..1] ± 1481
       PriceType <PricTp> [0..1] CodeSet 1481
     EndPrice <EndPric> [0..1]  1482
       ValueType <ValTp> [0..1] CodeSet 1482
       Value <Val> [1..1] ± 1483
       PriceType <PricTp> [0..1] CodeSet 1483
     StartValue <StartVal> [0..1] Amount C1, C5 1484
     CurrentValue <CurVal> [0..1] Amount C1, C5 1484
     EndValue <EndVal> [0..1] Amount C1, C5 1485
     AdjustedQuantity <AdjstdQty> [0..1]  1485
{Or       Unit <Unit> [1..1] Quantity 1485
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1486
     ExchangeRate <XchgRate> [0..1] Rate 1486
     CapValue <CapVal> [0..1] Amount C1, C5 1486
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1465 August 2026
```

