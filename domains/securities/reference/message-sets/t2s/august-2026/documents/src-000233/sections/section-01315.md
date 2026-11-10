---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.4 Derivative <Deriv>", "32.4.3.1.1.2.4.1 Future <Futr>"]
file_pages: [1908, 1909]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.4.1 Future <Futr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1908 to 1909.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1908

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 1947
       EndPrice <EndPric> [0..1]  1948
         ValueType <ValTp> [0..1] CodeSet 1948
         Value <Val> [1..1] ± 1949
         PriceType <PricTp> [0..1] CodeSet 1949
       StartValue <StartVal> [0..1] Amount C1, C5 1950
       CurrentValue <CurVal> [0..1] Amount C1, C5 1950
       EndValue <EndVal> [0..1] Amount C1, C5 1951
       AdjustedQuantity <AdjstdQty> [0..1]  1951
{Or         Unit <Unit> [1..1] Quantity 1951
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1952
       ExchangeRate <XchgRate> [0..1] Rate 1952
       CapValue <CapVal> [0..1] Amount C1, C5 1952
32.4.3.1.1.2.4.1  Future <Futr>
Presence: [0..1]
Definition: Parameters for contracts which obligate the buyer to receive and the seller to deliver in the
future the assets specified at an agreed price.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1908 August 2026
```

## File page 1909

```text
Future <Futr> contains the following Future4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ContractSize <CtrctSz> [0..1] Rate 1910
   ExercisePrice <ExrcPric> [0..1]  1910
     ValueType <ValTp> [0..1] CodeSet 1910
     Value <Val> [1..1] ± 1911
     PriceType <PricTp> [0..1] CodeSet 1911
   FutureDate <FutrDt> [0..1] DateTime 1912
   MinimumSize <MinSz> [0..1] Amount C1, C5 1912
   UnitOfMeasure <UnitOfMeasr> [0..1]  1913
{Or     Code <Cd> [1..1] CodeSet 1913
Or}     Proprietary <Prtry> [1..1] ± 1915
   TimeUnit <TmUnit> [0..1]  1915
{Or     Code <Cd> [1..1] CodeSet 1916
Or}     Proprietary <Prtry> [1..1] ± 1916
   AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1916
     AllocationPercentage <AllcnPctg> [0..1] Rate 1918
     Quantity <Qty> [0..1]  1918
{Or       Unit <Unit> [1..1] Quantity 1918
Or}       FaceAmount <FaceAmt> [1..1] Amount C1, C5 1918
     SettlementType <SttlmTp> [0..1]  1918
{Or       Code <Cd> [1..1] CodeSet 1919
Or}       Proprietary <Prtry> [1..1] ± 1919
     CashAmount <CshAmt> [0..1] Amount C1, C5 1919
     CashType <CshTp> [0..1] Text 1920
     Price <Pric> [0..1]  1920
       ValueType <ValTp> [0..1] CodeSet 1920
       Value <Val> [1..1] ± 1921
       PriceType <PricTp> [0..1] CodeSet 1921
     DirtyPrice <DrtyPric> [0..1]  1922
       ValueType <ValTp> [0..1] CodeSet 1922
       Value <Val> [1..1] ± 1923
       PriceType <PricTp> [0..1] CodeSet 1923
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1909 August 2026
```

