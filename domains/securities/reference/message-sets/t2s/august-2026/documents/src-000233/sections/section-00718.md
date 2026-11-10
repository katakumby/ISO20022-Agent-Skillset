---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.1.1.4 Derivative <Deriv>", "28.4.2.1.1.1.4.1 Future <Futr>", "28.4.2.1.1.1.4.1.7 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "28.4.2.1.1.1.4.1.7.12 AdjustedQuantity <AdjstdQty>", "28.4.2.1.1.1.4.1.7.12.2 FaceAmount <FaceAmt>"]
file_pages: [1086, 1087, 1088, 1089]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.1.4.1.7.12.2 FaceAmount <FaceAmt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1086 to 1089.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1086

```text
Datatype: "DecimalNumber" on page 3324
28.4.2.1.1.1.4.1.7.12.2  FaceAmount <FaceAmt>
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
28.4.2.1.1.1.4.1.7.13  ExchangeRate <XchgRate>
Presence: [0..1]
Definition: Foreign exchange rate used to compute the current value.
Datatype: "PercentageRate" on page 3325
28.4.2.1.1.1.4.1.7.14  CapValue <CapVal>
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
28.4.2.1.1.1.4.2  Option <Optn>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1086 August 2026
```

## File page 1087

```text
Definition: Contracts which grant to the holder either the privilege to purchase or the privilege to sell the
assets specified at a predetermined price or formula at or within a time in the future.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1087 August 2026
```

## File page 1088

```text
Option <Optn> contains the following Option15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OptionSettlementStyle <OptnSttlmStyle> [0..1]  1090
{Or     Code <Cd> [0..*] CodeSet 1090
Or}     Proprietary <Prtry> [1..1] ± 1090
   ConversionDate <ConvsDt> [0..1] DateTime 1090
   StrikePrice <StrkPric> [0..1]  1090
     ValueType <ValTp> [0..1] CodeSet 1091
     Value <Val> [1..1] ± 1091
     PriceType <PricTp> [0..1] CodeSet 1092
   MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1092
   ConversionPeriod <ConvsPrd> [0..1]  1093
{Or     FromDateTime <FrDtTm> [1..1] DateTime 1093
Or     ToDateTime <ToDtTm> [1..1] DateTime 1093
Or}     DateTimeRange <DtTmRg> [1..1] ± 1093
   OptionStyle <OptnStyle> [0..1]  1094
{Or     Code <Cd> [1..1] CodeSet 1094
Or}     Proprietary <Prtry> [1..1] ± 1094
   OptionType <OptnTp> [0..1] ± 1094
   StrikeValue <StrkVal> [0..1] Quantity 1095
   StrikeMultiplier <StrkMltplr> [0..1] Quantity 1095
   InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  1095
{Or     Code <Cd> [1..1] CodeSet 1095
Or}     Proprietary <Prtry> [1..1] ± 1095
   VersionNumber <VrsnNb> [0..1] Quantity 1096
   ExpiryLocation <XpryLctn> [0..1] Text 1096
   Standardisation <Stdstn> [0..1]  1096
{Or     Code <Cd> [1..*] CodeSet 1096
Or}     Proprietary <Prtry> [1..1] ± 1097
   TradingPartyRole <TradgPtyRole> [0..1]  1097
{Or     Code <Cd> [1..*] CodeSet 1097
Or}     Proprietary <Prtry> [1..1] ± 1097
   ContractSize <CtrctSz> [0..1] Rate 1098
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1088 August 2026
```

## File page 1089

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1098
     AllocationPercentage <AllcnPctg> [0..1] Rate 1100
     Quantity <Qty> [0..1]  1100
{Or       Unit <Unit> [1..1] Quantity 1100
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1100
     SettlementType <SttlmTp> [0..1]  1100
{Or       Code <Cd> [1..1] CodeSet 1101
Or}       Proprietary <Prtry> [1..1] ± 1101
     CashAmount <CshAmt> [0..1] Amount C1, C5 1101
     CashType <CshTp> [0..1] Text 1102
     Price <Pric> [0..1]  1102
       ValueType <ValTp> [0..1] CodeSet 1102
       Value <Val> [1..1] ± 1103
       PriceType <PricTp> [0..1] CodeSet 1103
     DirtyPrice <DrtyPric> [0..1]  1104
       ValueType <ValTp> [0..1] CodeSet 1104
       Value <Val> [1..1] ± 1105
       PriceType <PricTp> [0..1] CodeSet 1105
     EndPrice <EndPric> [0..1]  1106
       ValueType <ValTp> [0..1] CodeSet 1106
       Value <Val> [1..1] ± 1107
       PriceType <PricTp> [0..1] CodeSet 1107
     StartValue <StartVal> [0..1] Amount C1, C5 1108
     CurrentValue <CurVal> [0..1] Amount C1, C5 1108
     EndValue <EndVal> [0..1] Amount C1, C5 1109
     AdjustedQuantity <AdjstdQty> [0..1]  1109
{Or       Unit <Unit> [1..1] Quantity 1109
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1110
     ExchangeRate <XchgRate> [0..1] Rate 1110
     CapValue <CapVal> [0..1] Amount C1, C5 1110
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1089 August 2026
```

