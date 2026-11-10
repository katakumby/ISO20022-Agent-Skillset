---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.1.1.4 Derivative <Deriv>", "28.4.2.1.1.1.4.1 Future <Futr>"]
file_pages: [1066, 1067]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.1.4.1 Future <Futr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1066 to 1067.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1066

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 1105
       EndPrice <EndPric> [0..1]  1106
         ValueType <ValTp> [0..1] CodeSet 1106
         Value <Val> [1..1] ± 1107
         PriceType <PricTp> [0..1] CodeSet 1107
       StartValue <StartVal> [0..1] Amount C1, C5 1108
       CurrentValue <CurVal> [0..1] Amount C1, C5 1108
       EndValue <EndVal> [0..1] Amount C1, C5 1109
       AdjustedQuantity <AdjstdQty> [0..1]  1109
{Or         Unit <Unit> [1..1] Quantity 1109
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1110
       ExchangeRate <XchgRate> [0..1] Rate 1110
       CapValue <CapVal> [0..1] Amount C1, C5 1110
28.4.2.1.1.1.4.1  Future <Futr>
Presence: [0..1]
Definition: Parameters for contracts which obligate the buyer to receive and the seller to deliver in the
future the assets specified at an agreed price.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1066 August 2026
```

## File page 1067

```text
Future <Futr> contains the following Future4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ContractSize <CtrctSz> [0..1] Rate 1068
   ExercisePrice <ExrcPric> [0..1]  1068
     ValueType <ValTp> [0..1] CodeSet 1068
     Value <Val> [1..1] ± 1069
     PriceType <PricTp> [0..1] CodeSet 1069
   FutureDate <FutrDt> [0..1] DateTime 1070
   MinimumSize <MinSz> [0..1] Amount C1, C5 1070
   UnitOfMeasure <UnitOfMeasr> [0..1]  1071
{Or     Code <Cd> [1..1] CodeSet 1071
Or}     Proprietary <Prtry> [1..1] ± 1073
   TimeUnit <TmUnit> [0..1]  1073
{Or     Code <Cd> [1..1] CodeSet 1074
Or}     Proprietary <Prtry> [1..1] ± 1074
   AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1074
     AllocationPercentage <AllcnPctg> [0..1] Rate 1076
     Quantity <Qty> [0..1]  1076
{Or       Unit <Unit> [1..1] Quantity 1076
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1076
     SettlementType <SttlmTp> [0..1]  1076
{Or       Code <Cd> [1..1] CodeSet 1077
Or}       Proprietary <Prtry> [1..1] ± 1077
     CashAmount <CshAmt> [0..1] Amount C1, C5 1077
     CashType <CshTp> [0..1] Text 1078
     Price <Pric> [0..1]  1078
       ValueType <ValTp> [0..1] CodeSet 1078
       Value <Val> [1..1] ± 1079
       PriceType <PricTp> [0..1] CodeSet 1079
     DirtyPrice <DrtyPric> [0..1]  1080
       ValueType <ValTp> [0..1] CodeSet 1080
       Value <Val> [1..1] ± 1081
       PriceType <PricTp> [0..1] CodeSet 1081
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1067 August 2026
```

