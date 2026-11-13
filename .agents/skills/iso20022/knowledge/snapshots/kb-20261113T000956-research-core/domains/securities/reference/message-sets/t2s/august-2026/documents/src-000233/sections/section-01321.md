---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.4 Derivative <Deriv>", "32.4.3.1.1.2.4.1 Future <Futr>", "32.4.3.1.1.2.4.1.6 TimeUnit <TmUnit>", "32.4.3.1.1.2.4.1.6.1 Code <Cd>"]
file_pages: [1916, 1917]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.4.1.6.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1916 to 1917.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1916

```text
TimeUnit <TmUnit> contains one of the following TimeUnit3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1916
Or}   Proprietary <Prtry> [1..1] ± 1916
32.4.3.1.1.2.4.1.6.1  Code <Cd>
Presence: [1..1]
Definition: Time unit expressed as an ISO 20022 code.
Datatype: "TimeUnit1Code" on page 3306
CodeName Name Definition
DAYC CalendarDay Time unit is calendar day.
HOUR Hour Time unit is hour.
MINU Minute Time unit is minute.
MNTH Month Time unit is month.
SECO Second Time unit is second.
WEEK Week Time unit is week.
YEAR Year Time unit is year.
32.4.3.1.1.2.4.1.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Time unit expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
32.4.3.1.1.2.4.1.7  AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>
Presence: [0..*]
Definition: Provides more information about the underlying instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1916 August 2026
```

## File page 1917

```text
AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> contains the following
UnderlyingAttributes4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AllocationPercentage <AllcnPctg> [0..1] Rate 1918
   Quantity <Qty> [0..1]  1918
{Or     Unit <Unit> [1..1] Quantity 1918
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1918
   SettlementType <SttlmTp> [0..1]  1918
{Or     Code <Cd> [1..1] CodeSet 1919
Or}     Proprietary <Prtry> [1..1] ± 1919
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
   EndPrice <EndPric> [0..1]  1924
     ValueType <ValTp> [0..1] CodeSet 1924
     Value <Val> [1..1] ± 1925
     PriceType <PricTp> [0..1] CodeSet 1925
   StartValue <StartVal> [0..1] Amount C1, C5 1926
   CurrentValue <CurVal> [0..1] Amount C1, C5 1926
   EndValue <EndVal> [0..1] Amount C1, C5 1927
   AdjustedQuantity <AdjstdQty> [0..1]  1927
{Or     Unit <Unit> [1..1] Quantity 1927
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1928
   ExchangeRate <XchgRate> [0..1] Rate 1928
   CapValue <CapVal> [0..1] Amount C1, C5 1928
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1917 August 2026
```

