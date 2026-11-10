---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.2 Derivative4", "13.1.2.2.1 Future <Futr>", "13.1.2.2.1.7 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "13.1.2.2.1.7.12 AdjustedQuantity <AdjstdQty>", "13.1.2.2.1.7.12.2 FaceAmount <FaceAmt>"]
file_pages: [173, 174, 175, 176]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.2.1.7.12.2 FaceAmount <FaceAmt>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 173 to 176.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 173

```text
Datatype: "DecimalNumber" on page 532
13.1.2.2.1.7.12.2  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, ie, the principal, of a debt
instrument.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 506
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
13.1.2.2.1.7.13  ExchangeRate <XchgRate>
Presence: [0..1]
Definition: Foreign exchange rate used to compute the current value.
Datatype: "PercentageRate" on page 532
13.1.2.2.1.7.14  CapValue <CapVal>
Presence: [0..1]
Definition: Maximum notional value for a financial instrument that is capped.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 506
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
13.1.2.2.2  Option <Optn>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 173 March 2024
```

## File page 174

```text
Definition: Contracts which grant to the holder either the privilege to purchase or the privilege to sell the
assets specified at a predetermined price or formula at or within a time in the future.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 174 March 2024
```

## File page 175

```text
Option <Optn> contains the following Option15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OptionSettlementStyle <OptnSttlmStyle> [0..1]  177
{Or     Code <Cd> [0..*] CodeSet 177
Or}     Proprietary <Prtry> [1..1] ± 177
   ConversionDate <ConvsDt> [0..1] DateTime 177
   StrikePrice <StrkPric> [0..1]  177
     ValueType <ValTp> [0..1] CodeSet 178
     Value <Val> [1..1] ± 178
     PriceType <PricTp> [0..1] CodeSet 179
   MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 179
   ConversionPeriod <ConvsPrd> [0..1]  180
{Or     FromDateTime <FrDtTm> [1..1] DateTime 180
Or     ToDateTime <ToDtTm> [1..1] DateTime 180
Or}     DateTimeRange <DtTmRg> [1..1] ± 180
   OptionStyle <OptnStyle> [0..1]  181
{Or     Code <Cd> [1..1] CodeSet 181
Or}     Proprietary <Prtry> [1..1] ± 181
   OptionType <OptnTp> [0..1] ± 181
   StrikeValue <StrkVal> [0..1] Quantity 182
   StrikeMultiplier <StrkMltplr> [0..1] Quantity 182
   InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  182
{Or     Code <Cd> [1..1] CodeSet 182
Or}     Proprietary <Prtry> [1..1] ± 182
   VersionNumber <VrsnNb> [0..1] Quantity 183
   ExpiryLocation <XpryLctn> [0..1] Text 183
   Standardisation <Stdstn> [0..1]  183
{Or     Code <Cd> [1..*] CodeSet 183
Or}     Proprietary <Prtry> [1..1] ± 184
   TradingPartyRole <TradgPtyRole> [0..1]  184
{Or     Code <Cd> [1..*] CodeSet 184
Or}     Proprietary <Prtry> [1..1] ± 184
   ContractSize <CtrctSz> [0..1] Rate 185
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 175 March 2024
```

## File page 176

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  185
     AllocationPercentage <AllcnPctg> [0..1] Rate 187
     Quantity <Qty> [0..1]  187
{Or       Unit <Unit> [1..1] Quantity 187
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 187
     SettlementType <SttlmTp> [0..1]  187
{Or       Code <Cd> [1..1] CodeSet 188
Or}       Proprietary <Prtry> [1..1] ± 188
     CashAmount <CshAmt> [0..1] Amount C1, C5 188
     CashType <CshTp> [0..1] Text 189
     Price <Pric> [0..1]  189
       ValueType <ValTp> [0..1] CodeSet 189
       Value <Val> [1..1] ± 190
       PriceType <PricTp> [0..1] CodeSet 190
     DirtyPrice <DrtyPric> [0..1]  191
       ValueType <ValTp> [0..1] CodeSet 191
       Value <Val> [1..1] ± 192
       PriceType <PricTp> [0..1] CodeSet 192
     EndPrice <EndPric> [0..1]  193
       ValueType <ValTp> [0..1] CodeSet 193
       Value <Val> [1..1] ± 194
       PriceType <PricTp> [0..1] CodeSet 194
     StartValue <StartVal> [0..1] Amount C1, C5 195
     CurrentValue <CurVal> [0..1] Amount C1, C5 195
     EndValue <EndVal> [0..1] Amount C1, C5 196
     AdjustedQuantity <AdjstdQty> [0..1]  196
{Or       Unit <Unit> [1..1] Quantity 196
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 197
     ExchangeRate <XchgRate> [0..1] Rate 197
     CapValue <CapVal> [0..1] Amount C1, C5 197
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 176 March 2024
```

