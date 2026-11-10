---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.4 Derivative <Deriv>", "27.4.2.2.4.1 Future <Futr>"]
file_pages: [706, 707]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.4.1 Future <Futr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 706 to 707.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 706

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 745
       EndPrice <EndPric> [0..1]  746
         ValueType <ValTp> [0..1] CodeSet 746
         Value <Val> [1..1] ± 747
         PriceType <PricTp> [0..1] CodeSet 747
       StartValue <StartVal> [0..1] Amount C1, C5 748
       CurrentValue <CurVal> [0..1] Amount C1, C5 748
       EndValue <EndVal> [0..1] Amount C1, C5 749
       AdjustedQuantity <AdjstdQty> [0..1]  749
{Or         Unit <Unit> [1..1] Quantity 749
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 750
       ExchangeRate <XchgRate> [0..1] Rate 750
       CapValue <CapVal> [0..1] Amount C1, C5 750
27.4.2.2.4.1  Future <Futr>
Presence: [0..1]
Definition: Parameters for contracts which obligate the buyer to receive and the seller to deliver in the
future the assets specified at an agreed price.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 706 August 2026
```

## File page 707

```text
Future <Futr> contains the following Future4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ContractSize <CtrctSz> [0..1] Rate 708
   ExercisePrice <ExrcPric> [0..1]  708
     ValueType <ValTp> [0..1] CodeSet 708
     Value <Val> [1..1] ± 709
     PriceType <PricTp> [0..1] CodeSet 709
   FutureDate <FutrDt> [0..1] DateTime 710
   MinimumSize <MinSz> [0..1] Amount C1, C5 710
   UnitOfMeasure <UnitOfMeasr> [0..1]  711
{Or     Code <Cd> [1..1] CodeSet 711
Or}     Proprietary <Prtry> [1..1] ± 713
   TimeUnit <TmUnit> [0..1]  713
{Or     Code <Cd> [1..1] CodeSet 714
Or}     Proprietary <Prtry> [1..1] ± 714
   AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  714
     AllocationPercentage <AllcnPctg> [0..1] Rate 716
     Quantity <Qty> [0..1]  716
{Or       Unit <Unit> [1..1] Quantity 716
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 716
     SettlementType <SttlmTp> [0..1]  716
{Or       Code <Cd> [1..1] CodeSet 717
Or}       Proprietary <Prtry> [1..1] ± 717
     CashAmount <CshAmt> [0..1] Amount C1, C5 717
     CashType <CshTp> [0..1] Text 718
     Price <Pric> [0..1]  718
       ValueType <ValTp> [0..1] CodeSet 718
       Value <Val> [1..1] ± 719
       PriceType <PricTp> [0..1] CodeSet 719
     DirtyPrice <DrtyPric> [0..1]  720
       ValueType <ValTp> [0..1] CodeSet 720
       Value <Val> [1..1] ± 721
       PriceType <PricTp> [0..1] CodeSet 721
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 707 August 2026
```

