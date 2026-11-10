---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.1 Equity3", "13.1.2.1.5 VotingRightsPerShare <VtngRghtsPerShr>"]
file_pages: [149, 150, 151, 152]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.1.5 VotingRightsPerShare <VtngRghtsPerShr>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 149 to 152.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 149

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
13.1.2.1.5  VotingRightsPerShare <VtngRghtsPerShr>
Presence: [0..1]
Definition: Number of voting rights per share.
Datatype: "Number" on page 532
13.1.2.2  Derivative4
Definition: Represents different types of derivative.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 149 March 2024
```

## File page 150

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Future <Futr> [0..1]  153
     ContractSize <CtrctSz> [0..1] Rate 155
     ExercisePrice <ExrcPric> [0..1]  155
       ValueType <ValTp> [0..1] CodeSet 155
       Value <Val> [1..1] ± 156
       PriceType <PricTp> [0..1] CodeSet 156
     FutureDate <FutrDt> [0..1] DateTime 157
     MinimumSize <MinSz> [0..1] Amount C1, C5 157
     UnitOfMeasure <UnitOfMeasr> [0..1]  158
{Or       Code <Cd> [1..1] CodeSet 158
Or}       Proprietary <Prtry> [1..1] ± 160
     TimeUnit <TmUnit> [0..1]  160
{Or       Code <Cd> [1..1] CodeSet 161
Or}       Proprietary <Prtry> [1..1] ± 161
     AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  161
       AllocationPercentage <AllcnPctg> [0..1] Rate 163
       Quantity <Qty> [0..1]  163
{Or         Unit <Unit> [1..1] Quantity 163
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 163
       SettlementType <SttlmTp> [0..1]  163
{Or         Code <Cd> [1..1] CodeSet 164
Or}         Proprietary <Prtry> [1..1] ± 164
       CashAmount <CshAmt> [0..1] Amount C1, C5 164
       CashType <CshTp> [0..1] Text 165
       Price <Pric> [0..1]  165
         ValueType <ValTp> [0..1] CodeSet 165
         Value <Val> [1..1] ± 166
         PriceType <PricTp> [0..1] CodeSet 166
       DirtyPrice <DrtyPric> [0..1]  167
         ValueType <ValTp> [0..1] CodeSet 167
         Value <Val> [1..1] ± 168
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 150 March 2024
```

## File page 151

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 168
       EndPrice <EndPric> [0..1]  169
         ValueType <ValTp> [0..1] CodeSet 169
         Value <Val> [1..1] ± 170
         PriceType <PricTp> [0..1] CodeSet 170
       StartValue <StartVal> [0..1] Amount C1, C5 171
       CurrentValue <CurVal> [0..1] Amount C1, C5 171
       EndValue <EndVal> [0..1] Amount C1, C5 172
       AdjustedQuantity <AdjstdQty> [0..1]  172
{Or         Unit <Unit> [1..1] Quantity 172
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 173
       ExchangeRate <XchgRate> [0..1] Rate 173
       CapValue <CapVal> [0..1] Amount C1, C5 173
   Option <Optn> [0..1]  173
     OptionSettlementStyle <OptnSttlmStyle> [0..1]  177
{Or       Code <Cd> [0..*] CodeSet 177
Or}       Proprietary <Prtry> [1..1] ± 177
     ConversionDate <ConvsDt> [0..1] DateTime 177
     StrikePrice <StrkPric> [0..1]  177
       ValueType <ValTp> [0..1] CodeSet 178
       Value <Val> [1..1] ± 178
       PriceType <PricTp> [0..1] CodeSet 179
     MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 179
     ConversionPeriod <ConvsPrd> [0..1]  180
{Or       FromDateTime <FrDtTm> [1..1] DateTime 180
Or       ToDateTime <ToDtTm> [1..1] DateTime 180
Or}       DateTimeRange <DtTmRg> [1..1] ± 180
     OptionStyle <OptnStyle> [0..1]  181
{Or       Code <Cd> [1..1] CodeSet 181
Or}       Proprietary <Prtry> [1..1] ± 181
     OptionType <OptnTp> [0..1] ± 181
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 151 March 2024
```

## File page 152

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     StrikeValue <StrkVal> [0..1] Quantity 182
     StrikeMultiplier <StrkMltplr> [0..1] Quantity 182
     InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  182
{Or       Code <Cd> [1..1] CodeSet 182
Or}       Proprietary <Prtry> [1..1] ± 182
     VersionNumber <VrsnNb> [0..1] Quantity 183
     ExpiryLocation <XpryLctn> [0..1] Text 183
     Standardisation <Stdstn> [0..1]  183
{Or       Code <Cd> [1..*] CodeSet 183
Or}       Proprietary <Prtry> [1..1] ± 184
     TradingPartyRole <TradgPtyRole> [0..1]  184
{Or       Code <Cd> [1..*] CodeSet 184
Or}       Proprietary <Prtry> [1..1] ± 184
     ContractSize <CtrctSz> [0..1] Rate 185
     AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  185
       AllocationPercentage <AllcnPctg> [0..1] Rate 187
       Quantity <Qty> [0..1]  187
{Or         Unit <Unit> [1..1] Quantity 187
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 187
       SettlementType <SttlmTp> [0..1]  187
{Or         Code <Cd> [1..1] CodeSet 188
Or}         Proprietary <Prtry> [1..1] ± 188
       CashAmount <CshAmt> [0..1] Amount C1, C5 188
       CashType <CshTp> [0..1] Text 189
       Price <Pric> [0..1]  189
         ValueType <ValTp> [0..1] CodeSet 189
         Value <Val> [1..1] ± 190
         PriceType <PricTp> [0..1] CodeSet 190
       DirtyPrice <DrtyPric> [0..1]  191
         ValueType <ValTp> [0..1] CodeSet 191
         Value <Val> [1..1] ± 192
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 152 March 2024
```

