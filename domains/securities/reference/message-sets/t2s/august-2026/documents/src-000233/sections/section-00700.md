---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.1.1.3 Debt <Debt>", "28.4.2.1.1.1.3.77 PriceRange <PricRg>"]
file_pages: [1062, 1063, 1064, 1065]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.1.3.77 PriceRange <PricRg>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1062 to 1065.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1062

```text
28.4.2.1.1.1.3.77  PriceRange <PricRg>
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
28.4.2.1.1.1.4  Derivative <Deriv>
Presence: [0..1]
Definition: Choice between type of derivatives.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1062 August 2026
```

## File page 1063

```text
Derivative <Deriv> contains the following Derivative4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Future <Futr> [0..1]  1066
     ContractSize <CtrctSz> [0..1] Rate 1068
     ExercisePrice <ExrcPric> [0..1]  1068
       ValueType <ValTp> [0..1] CodeSet 1068
       Value <Val> [1..1] ± 1069
       PriceType <PricTp> [0..1] CodeSet 1069
     FutureDate <FutrDt> [0..1] DateTime 1070
     MinimumSize <MinSz> [0..1] Amount C1, C5 1070
     UnitOfMeasure <UnitOfMeasr> [0..1]  1071
{Or       Code <Cd> [1..1] CodeSet 1071
Or}       Proprietary <Prtry> [1..1] ± 1073
     TimeUnit <TmUnit> [0..1]  1073
{Or       Code <Cd> [1..1] CodeSet 1074
Or}       Proprietary <Prtry> [1..1] ± 1074
     AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1074
       AllocationPercentage <AllcnPctg> [0..1] Rate 1076
       Quantity <Qty> [0..1]  1076
{Or         Unit <Unit> [1..1] Quantity 1076
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1076
       SettlementType <SttlmTp> [0..1]  1076
{Or         Code <Cd> [1..1] CodeSet 1077
Or}         Proprietary <Prtry> [1..1] ± 1077
       CashAmount <CshAmt> [0..1] Amount C1, C5 1077
       CashType <CshTp> [0..1] Text 1078
       Price <Pric> [0..1]  1078
         ValueType <ValTp> [0..1] CodeSet 1078
         Value <Val> [1..1] ± 1079
         PriceType <PricTp> [0..1] CodeSet 1079
       DirtyPrice <DrtyPric> [0..1]  1080
         ValueType <ValTp> [0..1] CodeSet 1080
         Value <Val> [1..1] ± 1081
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1063 August 2026
```

## File page 1064

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 1081
       EndPrice <EndPric> [0..1]  1082
         ValueType <ValTp> [0..1] CodeSet 1082
         Value <Val> [1..1] ± 1083
         PriceType <PricTp> [0..1] CodeSet 1083
       StartValue <StartVal> [0..1] Amount C1, C5 1084
       CurrentValue <CurVal> [0..1] Amount C1, C5 1084
       EndValue <EndVal> [0..1] Amount C1, C5 1085
       AdjustedQuantity <AdjstdQty> [0..1]  1085
{Or         Unit <Unit> [1..1] Quantity 1085
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1086
       ExchangeRate <XchgRate> [0..1] Rate 1086
       CapValue <CapVal> [0..1] Amount C1, C5 1086
   Option <Optn> [0..1]  1086
     OptionSettlementStyle <OptnSttlmStyle> [0..1]  1090
{Or       Code <Cd> [0..*] CodeSet 1090
Or}       Proprietary <Prtry> [1..1] ± 1090
     ConversionDate <ConvsDt> [0..1] DateTime 1090
     StrikePrice <StrkPric> [0..1]  1090
       ValueType <ValTp> [0..1] CodeSet 1091
       Value <Val> [1..1] ± 1091
       PriceType <PricTp> [0..1] CodeSet 1092
     MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1092
     ConversionPeriod <ConvsPrd> [0..1]  1093
{Or       FromDateTime <FrDtTm> [1..1] DateTime 1093
Or       ToDateTime <ToDtTm> [1..1] DateTime 1093
Or}       DateTimeRange <DtTmRg> [1..1] ± 1093
     OptionStyle <OptnStyle> [0..1]  1094
{Or       Code <Cd> [1..1] CodeSet 1094
Or}       Proprietary <Prtry> [1..1] ± 1094
     OptionType <OptnTp> [0..1] ± 1094
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1064 August 2026
```

## File page 1065

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     StrikeValue <StrkVal> [0..1] Quantity 1095
     StrikeMultiplier <StrkMltplr> [0..1] Quantity 1095
     InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  1095
{Or       Code <Cd> [1..1] CodeSet 1095
Or}       Proprietary <Prtry> [1..1] ± 1095
     VersionNumber <VrsnNb> [0..1] Quantity 1096
     ExpiryLocation <XpryLctn> [0..1] Text 1096
     Standardisation <Stdstn> [0..1]  1096
{Or       Code <Cd> [1..*] CodeSet 1096
Or}       Proprietary <Prtry> [1..1] ± 1097
     TradingPartyRole <TradgPtyRole> [0..1]  1097
{Or       Code <Cd> [1..*] CodeSet 1097
Or}       Proprietary <Prtry> [1..1] ± 1097
     ContractSize <CtrctSz> [0..1] Rate 1098
     AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1098
       AllocationPercentage <AllcnPctg> [0..1] Rate 1100
       Quantity <Qty> [0..1]  1100
{Or         Unit <Unit> [1..1] Quantity 1100
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1100
       SettlementType <SttlmTp> [0..1]  1100
{Or         Code <Cd> [1..1] CodeSet 1101
Or}         Proprietary <Prtry> [1..1] ± 1101
       CashAmount <CshAmt> [0..1] Amount C1, C5 1101
       CashType <CshTp> [0..1] Text 1102
       Price <Pric> [0..1]  1102
         ValueType <ValTp> [0..1] CodeSet 1102
         Value <Val> [1..1] ± 1103
         PriceType <PricTp> [0..1] CodeSet 1103
       DirtyPrice <DrtyPric> [0..1]  1104
         ValueType <ValTp> [0..1] CodeSet 1104
         Value <Val> [1..1] ± 1105
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1065 August 2026
```

