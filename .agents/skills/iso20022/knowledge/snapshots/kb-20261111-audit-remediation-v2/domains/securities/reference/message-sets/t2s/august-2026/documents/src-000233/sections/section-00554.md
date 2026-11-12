---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.4 Derivative <Deriv>", "27.4.2.2.4.1 Future <Futr>", "27.4.2.2.4.1.7 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "27.4.2.2.4.1.7.12 AdjustedQuantity <AdjstdQty>", "27.4.2.2.4.1.7.12.2 FaceAmount <FaceAmt>"]
file_pages: [726, 727, 728, 729]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.4.1.7.12.2 FaceAmount <FaceAmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 726 to 729.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 726

```text
Datatype: "DecimalNumber" on page 3324
27.4.2.2.4.1.7.12.2  FaceAmount <FaceAmt>
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
27.4.2.2.4.1.7.13  ExchangeRate <XchgRate>
Presence: [0..1]
Definition: Foreign exchange rate used to compute the current value.
Datatype: "PercentageRate" on page 3325
27.4.2.2.4.1.7.14  CapValue <CapVal>
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
27.4.2.2.4.2  Option <Optn>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 726 August 2026
```

## File page 727

```text
Definition: Contracts which grant to the holder either the privilege to purchase or the privilege to sell the
assets specified at a predetermined price or formula at or within a time in the future.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 727 August 2026
```

## File page 728

```text
Option <Optn> contains the following Option15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OptionSettlementStyle <OptnSttlmStyle> [0..1]  730
{Or     Code <Cd> [0..*] CodeSet 730
Or}     Proprietary <Prtry> [1..1] ± 730
   ConversionDate <ConvsDt> [0..1] DateTime 730
   StrikePrice <StrkPric> [0..1]  730
     ValueType <ValTp> [0..1] CodeSet 731
     Value <Val> [1..1] ± 731
     PriceType <PricTp> [0..1] CodeSet 732
   MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 732
   ConversionPeriod <ConvsPrd> [0..1]  733
{Or     FromDateTime <FrDtTm> [1..1] DateTime 733
Or     ToDateTime <ToDtTm> [1..1] DateTime 733
Or}     DateTimeRange <DtTmRg> [1..1] ± 733
   OptionStyle <OptnStyle> [0..1]  734
{Or     Code <Cd> [1..1] CodeSet 734
Or}     Proprietary <Prtry> [1..1] ± 734
   OptionType <OptnTp> [0..1] ± 734
   StrikeValue <StrkVal> [0..1] Quantity 735
   StrikeMultiplier <StrkMltplr> [0..1] Quantity 735
   InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  735
{Or     Code <Cd> [1..1] CodeSet 735
Or}     Proprietary <Prtry> [1..1] ± 735
   VersionNumber <VrsnNb> [0..1] Quantity 736
   ExpiryLocation <XpryLctn> [0..1] Text 736
   Standardisation <Stdstn> [0..1]  736
{Or     Code <Cd> [1..*] CodeSet 736
Or}     Proprietary <Prtry> [1..1] ± 737
   TradingPartyRole <TradgPtyRole> [0..1]  737
{Or     Code <Cd> [1..*] CodeSet 737
Or}     Proprietary <Prtry> [1..1] ± 737
   ContractSize <CtrctSz> [0..1] Rate 738
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 728 August 2026
```

## File page 729

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  738
     AllocationPercentage <AllcnPctg> [0..1] Rate 740
     Quantity <Qty> [0..1]  740
{Or       Unit <Unit> [1..1] Quantity 740
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 740
     SettlementType <SttlmTp> [0..1]  740
{Or       Code <Cd> [1..1] CodeSet 741
Or}       Proprietary <Prtry> [1..1] ± 741
     CashAmount <CshAmt> [0..1] Amount C1, C5 741
     CashType <CshTp> [0..1] Text 742
     Price <Pric> [0..1]  742
       ValueType <ValTp> [0..1] CodeSet 742
       Value <Val> [1..1] ± 743
       PriceType <PricTp> [0..1] CodeSet 743
     DirtyPrice <DrtyPric> [0..1]  744
       ValueType <ValTp> [0..1] CodeSet 744
       Value <Val> [1..1] ± 745
       PriceType <PricTp> [0..1] CodeSet 745
     EndPrice <EndPric> [0..1]  746
       ValueType <ValTp> [0..1] CodeSet 746
       Value <Val> [1..1] ± 747
       PriceType <PricTp> [0..1] CodeSet 747
     StartValue <StartVal> [0..1] Amount C1, C5 748
     CurrentValue <CurVal> [0..1] Amount C1, C5 748
     EndValue <EndVal> [0..1] Amount C1, C5 749
     AdjustedQuantity <AdjstdQty> [0..1]  749
{Or       Unit <Unit> [1..1] Quantity 749
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 750
     ExchangeRate <XchgRate> [0..1] Rate 750
     CapValue <CapVal> [0..1] Amount C1, C5 750
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 729 August 2026
```

