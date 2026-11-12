---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.1.1.4 Derivative <Deriv>", "28.4.2.1.1.1.4.1 Future <Futr>", "28.4.2.1.1.1.4.1.6 TimeUnit <TmUnit>", "28.4.2.1.1.1.4.1.6.1 Code <Cd>"]
file_pages: [1074, 1075]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.1.4.1.6.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1074 to 1075.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1074

```text
TimeUnit <TmUnit> contains one of the following TimeUnit3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1074
Or}   Proprietary <Prtry> [1..1] ± 1074
28.4.2.1.1.1.4.1.6.1  Code <Cd>
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
28.4.2.1.1.1.4.1.6.2  Proprietary <Prtry>
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
28.4.2.1.1.1.4.1.7  AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>
Presence: [0..*]
Definition: Provides more information about the underlying instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1074 August 2026
```

## File page 1075

```text
AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> contains the following
UnderlyingAttributes4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AllocationPercentage <AllcnPctg> [0..1] Rate 1076
   Quantity <Qty> [0..1]  1076
{Or     Unit <Unit> [1..1] Quantity 1076
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1076
   SettlementType <SttlmTp> [0..1]  1076
{Or     Code <Cd> [1..1] CodeSet 1077
Or}     Proprietary <Prtry> [1..1] ± 1077
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
   EndPrice <EndPric> [0..1]  1082
     ValueType <ValTp> [0..1] CodeSet 1082
     Value <Val> [1..1] ± 1083
     PriceType <PricTp> [0..1] CodeSet 1083
   StartValue <StartVal> [0..1] Amount C1, C5 1084
   CurrentValue <CurVal> [0..1] Amount C1, C5 1084
   EndValue <EndVal> [0..1] Amount C1, C5 1085
   AdjustedQuantity <AdjstdQty> [0..1]  1085
{Or     Unit <Unit> [1..1] Quantity 1085
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1086
   ExchangeRate <XchgRate> [0..1] Rate 1086
   CapValue <CapVal> [0..1] Amount C1, C5 1086
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1075 August 2026
```

