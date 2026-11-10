---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.3 Debt <Debt>", "32.4.3.1.1.2.3.77 PriceRange <PricRg>"]
file_pages: [1904, 1905, 1906, 1907]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.3.77 PriceRange <PricRg>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1904 to 1907.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1904

```text
32.4.3.1.1.2.3.77  PriceRange <PricRg>
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
32.4.3.1.1.2.4  Derivative <Deriv>
Presence: [0..1]
Definition: Choice between type of derivatives.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1904 August 2026
```

## File page 1905

```text
Derivative <Deriv> contains the following Derivative4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Future <Futr> [0..1]  1908
     ContractSize <CtrctSz> [0..1] Rate 1910
     ExercisePrice <ExrcPric> [0..1]  1910
       ValueType <ValTp> [0..1] CodeSet 1910
       Value <Val> [1..1] ± 1911
       PriceType <PricTp> [0..1] CodeSet 1911
     FutureDate <FutrDt> [0..1] DateTime 1912
     MinimumSize <MinSz> [0..1] Amount C1, C5 1912
     UnitOfMeasure <UnitOfMeasr> [0..1]  1913
{Or       Code <Cd> [1..1] CodeSet 1913
Or}       Proprietary <Prtry> [1..1] ± 1915
     TimeUnit <TmUnit> [0..1]  1915
{Or       Code <Cd> [1..1] CodeSet 1916
Or}       Proprietary <Prtry> [1..1] ± 1916
     AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1916
       AllocationPercentage <AllcnPctg> [0..1] Rate 1918
       Quantity <Qty> [0..1]  1918
{Or         Unit <Unit> [1..1] Quantity 1918
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1918
       SettlementType <SttlmTp> [0..1]  1918
{Or         Code <Cd> [1..1] CodeSet 1919
Or}         Proprietary <Prtry> [1..1] ± 1919
       CashAmount <CshAmt> [0..1] Amount C1, C5 1919
       CashType <CshTp> [0..1] Text 1920
       Price <Pric> [0..1]  1920
         ValueType <ValTp> [0..1] CodeSet 1920
         Value <Val> [1..1] ± 1921
         PriceType <PricTp> [0..1] CodeSet 1921
       DirtyPrice <DrtyPric> [0..1]  1922
         ValueType <ValTp> [0..1] CodeSet 1922
         Value <Val> [1..1] ± 1923
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1905 August 2026
```

## File page 1906

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 1923
       EndPrice <EndPric> [0..1]  1924
         ValueType <ValTp> [0..1] CodeSet 1924
         Value <Val> [1..1] ± 1925
         PriceType <PricTp> [0..1] CodeSet 1925
       StartValue <StartVal> [0..1] Amount C1, C5 1926
       CurrentValue <CurVal> [0..1] Amount C1, C5 1926
       EndValue <EndVal> [0..1] Amount C1, C5 1927
       AdjustedQuantity <AdjstdQty> [0..1]  1927
{Or         Unit <Unit> [1..1] Quantity 1927
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1928
       ExchangeRate <XchgRate> [0..1] Rate 1928
       CapValue <CapVal> [0..1] Amount C1, C5 1928
   Option <Optn> [0..1]  1928
     OptionSettlementStyle <OptnSttlmStyle> [0..1]  1932
{Or       Code <Cd> [0..*] CodeSet 1932
Or}       Proprietary <Prtry> [1..1] ± 1932
     ConversionDate <ConvsDt> [0..1] DateTime 1932
     StrikePrice <StrkPric> [0..1]  1932
       ValueType <ValTp> [0..1] CodeSet 1933
       Value <Val> [1..1] ± 1933
       PriceType <PricTp> [0..1] CodeSet 1934
     MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 1934
     ConversionPeriod <ConvsPrd> [0..1]  1935
{Or       FromDateTime <FrDtTm> [1..1] DateTime 1935
Or       ToDateTime <ToDtTm> [1..1] DateTime 1935
Or}       DateTimeRange <DtTmRg> [1..1] ± 1935
     OptionStyle <OptnStyle> [0..1]  1936
{Or       Code <Cd> [1..1] CodeSet 1936
Or}       Proprietary <Prtry> [1..1] ± 1936
     OptionType <OptnTp> [0..1] ± 1936
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1906 August 2026
```

## File page 1907

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     StrikeValue <StrkVal> [0..1] Quantity 1937
     StrikeMultiplier <StrkMltplr> [0..1] Quantity 1937
     InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  1937
{Or       Code <Cd> [1..1] CodeSet 1937
Or}       Proprietary <Prtry> [1..1] ± 1937
     VersionNumber <VrsnNb> [0..1] Quantity 1938
     ExpiryLocation <XpryLctn> [0..1] Text 1938
     Standardisation <Stdstn> [0..1]  1938
{Or       Code <Cd> [1..*] CodeSet 1938
Or}       Proprietary <Prtry> [1..1] ± 1939
     TradingPartyRole <TradgPtyRole> [0..1]  1939
{Or       Code <Cd> [1..*] CodeSet 1939
Or}       Proprietary <Prtry> [1..1] ± 1939
     ContractSize <CtrctSz> [0..1] Rate 1940
     AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> [0..*]  1940
       AllocationPercentage <AllcnPctg> [0..1] Rate 1942
       Quantity <Qty> [0..1]  1942
{Or         Unit <Unit> [1..1] Quantity 1942
Or}         FaceAmount <FaceAmt> [1..1] Amount C1, C5 1942
       SettlementType <SttlmTp> [0..1]  1942
{Or         Code <Cd> [1..1] CodeSet 1943
Or}         Proprietary <Prtry> [1..1] ± 1943
       CashAmount <CshAmt> [0..1] Amount C1, C5 1943
       CashType <CshTp> [0..1] Text 1944
       Price <Pric> [0..1]  1944
         ValueType <ValTp> [0..1] CodeSet 1944
         Value <Val> [1..1] ± 1945
         PriceType <PricTp> [0..1] CodeSet 1945
       DirtyPrice <DrtyPric> [0..1]  1946
         ValueType <ValTp> [0..1] CodeSet 1946
         Value <Val> [1..1] ± 1947
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1907 August 2026
```

