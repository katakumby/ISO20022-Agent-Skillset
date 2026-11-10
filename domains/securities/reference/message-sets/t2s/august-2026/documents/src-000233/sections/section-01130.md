---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.2.1.4 Derivative <Deriv>", "28.4.2.2.1.4.1 Future <Futr>"]
file_pages: [1630, 1631]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.1.4.1 Future <Futr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1630 to 1631.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1630

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 1669
       EndPrice <EndPric> [0..1]  1670
         ValueType <ValTp> [0..1] CodeSet 1670
         Value <Val> [1..1] ± 1671
         PriceType <PricTp> [0..1] CodeSet 1671
       StartValue <StartVal> [0..1] Amount C1, C5 1672
       CurrentValue <CurVal> [0..1] Amount C1, C5 1672
       EndValue <EndVal> [0..1] Amount C1, C5 1673
       AdjustedQuantity <AdjstdQty> [0..1]  1673
{Or         Unit <Unit> [1..1] Quantity 1673
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1674
       ExchangeRate <XchgRate> [0..1] Rate 1674
       CapValue <CapVal> [0..1] Amount C1, C5 1674
28.4.2.2.1.4.1  Future <Futr>
Presence: [0..1]
Definition: Parameters for contracts which obligate the buyer to receive and the seller to deliver in the
future the assets specified at an agreed price.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1630 August 2026
```

## File page 1631

```text
Future <Futr> contains the following Future4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ContractSize <CtrctSz> [0..1] Rate 1632
   ExercisePrice <ExrcPric> [0..1]  1632
     ValueType <ValTp> [0..1] CodeSet 1632
     Value <Val> [1..1] ± 1633
     PriceType <PricTp> [0..1] CodeSet 1633
   FutureDate <FutrDt> [0..1] DateTime 1634
   MinimumSize <MinSz> [0..1] Amount C1, C5 1634
   UnitOfMeasure <UnitOfMeasr> [0..1]  1635
{Or     Code <Cd> [1..1] CodeSet 1635
Or}     Proprietary <Prtry> [1..1] ± 1637
   TimeUnit <TmUnit> [0..1]  1637
{Or     Code <Cd> [1..1] CodeSet 1638
Or}     Proprietary <Prtry> [1..1] ± 1638
   AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1638
     AllocationPercentage <AllcnPctg> [0..1] Rate 1640
     Quantity <Qty> [0..1]  1640
{Or       Unit <Unit> [1..1] Quantity 1640
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1640
     SettlementType <SttlmTp> [0..1]  1640
{Or       Code <Cd> [1..1] CodeSet 1641
Or}       Proprietary <Prtry> [1..1] ± 1641
     CashAmount <CshAmt> [0..1] Amount C1, C5 1641
     CashType <CshTp> [0..1] Text 1642
     Price <Pric> [0..1]  1642
       ValueType <ValTp> [0..1] CodeSet 1642
       Value <Val> [1..1] ± 1643
       PriceType <PricTp> [0..1] CodeSet 1643
     DirtyPrice <DrtyPric> [0..1]  1644
       ValueType <ValTp> [0..1] CodeSet 1644
       Value <Val> [1..1] ± 1645
       PriceType <PricTp> [0..1] CodeSet 1645
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1631 August 2026
```

