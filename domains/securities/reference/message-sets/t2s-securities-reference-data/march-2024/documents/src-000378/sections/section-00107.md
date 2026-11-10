---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.2 Derivative4", "13.1.2.2.1 Future <Futr>", "13.1.2.2.1.6 TimeUnit <TmUnit>", "13.1.2.2.1.6.1 Code <Cd>"]
file_pages: [161, 162]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.2.1.6.1 Code <Cd>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 161 to 162.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 161

```text
TimeUnit <TmUnit> contains one of the following TimeUnit3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 161
Or}   Proprietary <Prtry> [1..1] ± 161
13.1.2.2.1.6.1  Code <Cd>
Presence: [1..1]
Definition: Time unit expressed as an ISO 20022 code.
Datatype: "TimeUnit1Code" on page 524
CodeName Name Definition
DAYC CalendarDay Time unit is calendar day.
HOUR Hour Time unit is hour.
MINU Minute Time unit is minute.
MNTH Month Time unit is month.
SECO Second Time unit is second.
WEEK Week Time unit is week.
YEAR Year Time unit is year.
13.1.2.2.1.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Time unit expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.2.2.1.7  AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>
Presence: [0..*]
Definition: Provides more information about the underlying instrument.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 161 March 2024
```

## File page 162

```text
AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> contains the following
UnderlyingAttributes4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AllocationPercentage <AllcnPctg> [0..1] Rate 163
   Quantity <Qty> [0..1]  163
{Or     Unit <Unit> [1..1] Quantity 163
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 163
   SettlementType <SttlmTp> [0..1]  163
{Or     Code <Cd> [1..1] CodeSet 164
Or}     Proprietary <Prtry> [1..1] ± 164
   CashAmount <CshAmt> [0..1] Amount C1, C5 164
   CashType <CshTp> [0..1] Text 165
   Price <Pric> [0..1]  165
     ValueType <ValTp> [0..1] CodeSet 165
     Value <Val> [1..1] ± 166
     PriceType <PricTp> [0..1] CodeSet 166
   DirtyPrice <DrtyPric> [0..1]  167
     ValueType <ValTp> [0..1] CodeSet 167
     Value <Val> [1..1] ± 168
     PriceType <PricTp> [0..1] CodeSet 168
   EndPrice <EndPric> [0..1]  169
     ValueType <ValTp> [0..1] CodeSet 169
     Value <Val> [1..1] ± 170
     PriceType <PricTp> [0..1] CodeSet 170
   StartValue <StartVal> [0..1] Amount C1, C5 171
   CurrentValue <CurVal> [0..1] Amount C1, C5 171
   EndValue <EndVal> [0..1] Amount C1, C5 172
   AdjustedQuantity <AdjstdQty> [0..1]  172
{Or     Unit <Unit> [1..1] Quantity 172
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 173
   ExchangeRate <XchgRate> [0..1] Rate 173
   CapValue <CapVal> [0..1] Amount C1, C5 173
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 162 March 2024
```

