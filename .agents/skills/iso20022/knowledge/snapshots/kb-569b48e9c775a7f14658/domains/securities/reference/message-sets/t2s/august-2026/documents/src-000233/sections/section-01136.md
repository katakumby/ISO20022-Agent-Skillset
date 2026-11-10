---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.2.1.4 Derivative <Deriv>", "28.4.2.2.1.4.1 Future <Futr>", "28.4.2.2.1.4.1.6 TimeUnit <TmUnit>", "28.4.2.2.1.4.1.6.1 Code <Cd>"]
file_pages: [1638, 1639]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.1.4.1.6.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1638 to 1639.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1638

```text
TimeUnit <TmUnit> contains one of the following TimeUnit3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1638
Or}   Proprietary <Prtry> [1..1] ± 1638
28.4.2.2.1.4.1.6.1  Code <Cd>
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
28.4.2.2.1.4.1.6.2  Proprietary <Prtry>
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
28.4.2.2.1.4.1.7  AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>
Presence: [0..*]
Definition: Provides more information about the underlying instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1638 August 2026
```

## File page 1639

```text
AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> contains the following
UnderlyingAttributes4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AllocationPercentage <AllcnPctg> [0..1] Rate 1640
   Quantity <Qty> [0..1]  1640
{Or     Unit <Unit> [1..1] Quantity 1640
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1640
   SettlementType <SttlmTp> [0..1]  1640
{Or     Code <Cd> [1..1] CodeSet 1641
Or}     Proprietary <Prtry> [1..1] ± 1641
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
   EndPrice <EndPric> [0..1]  1646
     ValueType <ValTp> [0..1] CodeSet 1646
     Value <Val> [1..1] ± 1647
     PriceType <PricTp> [0..1] CodeSet 1647
   StartValue <StartVal> [0..1] Amount C1, C5 1648
   CurrentValue <CurVal> [0..1] Amount C1, C5 1648
   EndValue <EndVal> [0..1] Amount C1, C5 1649
   AdjustedQuantity <AdjstdQty> [0..1]  1649
{Or     Unit <Unit> [1..1] Quantity 1649
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1650
   ExchangeRate <XchgRate> [0..1] Rate 1650
   CapValue <CapVal> [0..1] Amount C1, C5 1650
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1639 August 2026
```

