---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.4 Derivative <Deriv>", "32.4.3.1.1.2.4.1 Future <Futr>", "32.4.3.1.1.2.4.1.7 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "32.4.3.1.1.2.4.1.7.12 AdjustedQuantity <AdjstdQty>", "32.4.3.1.1.2.4.1.7.12.2 FaceAmount <FaceAmt>"]
file_pages: [1928, 1929, 1930, 1931]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.4.1.7.12.2 FaceAmount <FaceAmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1928 to 1931.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1928

```text
Datatype: "DecimalNumber" on page 3324
32.4.3.1.1.2.4.1.7.12.2  FaceAmount <FaceAmt>
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
32.4.3.1.1.2.4.1.7.13  ExchangeRate <XchgRate>
Presence: [0..1]
Definition: Foreign exchange rate used to compute the current value.
Datatype: "PercentageRate" on page 3325
32.4.3.1.1.2.4.1.7.14  CapValue <CapVal>
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
32.4.3.1.1.2.4.2  Option <Optn>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1928 August 2026
```

## File page 1929

```text
Definition: Contracts which grant to the holder either the privilege to purchase or the privilege to sell the
assets specified at a predetermined price or formula at or within a time in the future.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1929 August 2026
```

## File page 1930

```text
Option <Optn> contains the following Option15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OptionSettlementStyle <OptnSttlmStyle> [0..1]  1932
{Or     Code <Cd> [0..*] CodeSet 1932
Or}     Proprietary <Prtry> [1..1] ± 1932
   ConversionDate <ConvsDt> [0..1] DateTime 1932
   StrikePrice <StrkPric> [0..1]  1932
     ValueType <ValTp> [0..1] CodeSet 1933
     Value <Val> [1..1] ± 1933
     PriceType <PricTp> [0..1] CodeSet 1934
   MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1934
   ConversionPeriod <ConvsPrd> [0..1]  1935
{Or     FromDateTime <FrDtTm> [1..1] DateTime 1935
Or     ToDateTime <ToDtTm> [1..1] DateTime 1935
Or}     DateTimeRange <DtTmRg> [1..1] ± 1935
   OptionStyle <OptnStyle> [0..1]  1936
{Or     Code <Cd> [1..1] CodeSet 1936
Or}     Proprietary <Prtry> [1..1] ± 1936
   OptionType <OptnTp> [0..1] ± 1936
   StrikeValue <StrkVal> [0..1] Quantity 1937
   StrikeMultiplier <StrkMltplr> [0..1] Quantity 1937
   InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  1937
{Or     Code <Cd> [1..1] CodeSet 1937
Or}     Proprietary <Prtry> [1..1] ± 1937
   VersionNumber <VrsnNb> [0..1] Quantity 1938
   ExpiryLocation <XpryLctn> [0..1] Text 1938
   Standardisation <Stdstn> [0..1]  1938
{Or     Code <Cd> [1..*] CodeSet 1938
Or}     Proprietary <Prtry> [1..1] ± 1939
   TradingPartyRole <TradgPtyRole> [0..1]  1939
{Or     Code <Cd> [1..*] CodeSet 1939
Or}     Proprietary <Prtry> [1..1] ± 1939
   ContractSize <CtrctSz> [0..1] Rate 1940
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1930 August 2026
```

## File page 1931

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1940
     AllocationPercentage <AllcnPctg> [0..1] Rate 1942
     Quantity <Qty> [0..1]  1942
{Or       Unit <Unit> [1..1] Quantity 1942
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1942
     SettlementType <SttlmTp> [0..1]  1942
{Or       Code <Cd> [1..1] CodeSet 1943
Or}       Proprietary <Prtry> [1..1] ± 1943
     CashAmount <CshAmt> [0..1] Amount C1, C5 1943
     CashType <CshTp> [0..1] Text 1944
     Price <Pric> [0..1]  1944
       ValueType <ValTp> [0..1] CodeSet 1944
       Value <Val> [1..1] ± 1945
       PriceType <PricTp> [0..1] CodeSet 1945
     DirtyPrice <DrtyPric> [0..1]  1946
       ValueType <ValTp> [0..1] CodeSet 1946
       Value <Val> [1..1] ± 1947
       PriceType <PricTp> [0..1] CodeSet 1947
     EndPrice <EndPric> [0..1]  1948
       ValueType <ValTp> [0..1] CodeSet 1948
       Value <Val> [1..1] ± 1949
       PriceType <PricTp> [0..1] CodeSet 1949
     StartValue <StartVal> [0..1] Amount C1, C5 1950
     CurrentValue <CurVal> [0..1] Amount C1, C5 1950
     EndValue <EndVal> [0..1] Amount C1, C5 1951
     AdjustedQuantity <AdjstdQty> [0..1]  1951
{Or       Unit <Unit> [1..1] Quantity 1951
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1952
     ExchangeRate <XchgRate> [0..1] Rate 1952
     CapValue <CapVal> [0..1] Amount C1, C5 1952
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1931 August 2026
```

