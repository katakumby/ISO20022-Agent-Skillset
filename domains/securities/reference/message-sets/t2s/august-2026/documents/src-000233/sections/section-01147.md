---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.2.1.4 Derivative <Deriv>", "28.4.2.2.1.4.1 Future <Futr>", "28.4.2.2.1.4.1.7 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "28.4.2.2.1.4.1.7.12 AdjustedQuantity <AdjstdQty>", "28.4.2.2.1.4.1.7.12.2 FaceAmount <FaceAmt>"]
file_pages: [1650, 1651, 1652, 1653]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.1.4.1.7.12.2 FaceAmount <FaceAmt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1650 to 1653.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1650

```text
Datatype: "DecimalNumber" on page 3324
28.4.2.2.1.4.1.7.12.2  FaceAmount <FaceAmt>
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
28.4.2.2.1.4.1.7.13  ExchangeRate <XchgRate>
Presence: [0..1]
Definition: Foreign exchange rate used to compute the current value.
Datatype: "PercentageRate" on page 3325
28.4.2.2.1.4.1.7.14  CapValue <CapVal>
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
28.4.2.2.1.4.2  Option <Optn>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1650 August 2026
```

## File page 1651

```text
Definition: Contracts which grant to the holder either the privilege to purchase or the privilege to sell the
assets specified at a predetermined price or formula at or within a time in the future.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1651 August 2026
```

## File page 1652

```text
Option <Optn> contains the following Option15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OptionSettlementStyle <OptnSttlmStyle> [0..1]  1654
{Or     Code <Cd> [0..*] CodeSet 1654
Or}     Proprietary <Prtry> [1..1] ± 1654
   ConversionDate <ConvsDt> [0..1] DateTime 1654
   StrikePrice <StrkPric> [0..1]  1654
     ValueType <ValTp> [0..1] CodeSet 1655
     Value <Val> [1..1] ± 1655
     PriceType <PricTp> [0..1] CodeSet 1656
   MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1656
   ConversionPeriod <ConvsPrd> [0..1]  1657
{Or     FromDateTime <FrDtTm> [1..1] DateTime 1657
Or     ToDateTime <ToDtTm> [1..1] DateTime 1657
Or}     DateTimeRange <DtTmRg> [1..1] ± 1657
   OptionStyle <OptnStyle> [0..1]  1658
{Or     Code <Cd> [1..1] CodeSet 1658
Or}     Proprietary <Prtry> [1..1] ± 1658
   OptionType <OptnTp> [0..1] ± 1658
   StrikeValue <StrkVal> [0..1] Quantity 1659
   StrikeMultiplier <StrkMltplr> [0..1] Quantity 1659
   InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  1659
{Or     Code <Cd> [1..1] CodeSet 1659
Or}     Proprietary <Prtry> [1..1] ± 1659
   VersionNumber <VrsnNb> [0..1] Quantity 1660
   ExpiryLocation <XpryLctn> [0..1] Text 1660
   Standardisation <Stdstn> [0..1]  1660
{Or     Code <Cd> [1..*] CodeSet 1660
Or}     Proprietary <Prtry> [1..1] ± 1661
   TradingPartyRole <TradgPtyRole> [0..1]  1661
{Or     Code <Cd> [1..*] CodeSet 1661
Or}     Proprietary <Prtry> [1..1] ± 1661
   ContractSize <CtrctSz> [0..1] Rate 1662
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1652 August 2026
```

## File page 1653

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1662
     AllocationPercentage <AllcnPctg> [0..1] Rate 1664
     Quantity <Qty> [0..1]  1664
{Or       Unit <Unit> [1..1] Quantity 1664
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1664
     SettlementType <SttlmTp> [0..1]  1664
{Or       Code <Cd> [1..1] CodeSet 1665
Or}       Proprietary <Prtry> [1..1] ± 1665
     CashAmount <CshAmt> [0..1] Amount C1, C5 1665
     CashType <CshTp> [0..1] Text 1666
     Price <Pric> [0..1]  1666
       ValueType <ValTp> [0..1] CodeSet 1666
       Value <Val> [1..1] ± 1667
       PriceType <PricTp> [0..1] CodeSet 1667
     DirtyPrice <DrtyPric> [0..1]  1668
       ValueType <ValTp> [0..1] CodeSet 1668
       Value <Val> [1..1] ± 1669
       PriceType <PricTp> [0..1] CodeSet 1669
     EndPrice <EndPric> [0..1]  1670
       ValueType <ValTp> [0..1] CodeSet 1670
       Value <Val> [1..1] ± 1671
       PriceType <PricTp> [0..1] CodeSet 1671
     StartValue <StartVal> [0..1] Amount C1, C5 1672
     CurrentValue <CurVal> [0..1] Amount C1, C5 1672
     EndValue <EndVal> [0..1] Amount C1, C5 1673
     AdjustedQuantity <AdjstdQty> [0..1]  1673
{Or       Unit <Unit> [1..1] Quantity 1673
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1674
     ExchangeRate <XchgRate> [0..1] Rate 1674
     CapValue <CapVal> [0..1] Amount C1, C5 1674
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1653 August 2026
```

