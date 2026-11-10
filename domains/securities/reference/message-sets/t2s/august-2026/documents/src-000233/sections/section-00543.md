---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.4 Derivative <Deriv>", "27.4.2.2.4.1 Future <Futr>", "27.4.2.2.4.1.6 TimeUnit <TmUnit>", "27.4.2.2.4.1.6.1 Code <Cd>"]
file_pages: [714, 715]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.4.1.6.1 Code <Cd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 714 to 715.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 714

```text
TimeUnit <TmUnit> contains one of the following TimeUnit3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 714
Or}   Proprietary <Prtry> [1..1] ± 714
27.4.2.2.4.1.6.1  Code <Cd>
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
27.4.2.2.4.1.6.2  Proprietary <Prtry>
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
27.4.2.2.4.1.7  AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>
Presence: [0..*]
Definition: Provides more information about the underlying instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 714 August 2026
```

## File page 715

```text
AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts> contains the following
UnderlyingAttributes4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AllocationPercentage <AllcnPctg> [0..1] Rate 716
   Quantity <Qty> [0..1]  716
{Or     Unit <Unit> [1..1] Quantity 716
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 716
   SettlementType <SttlmTp> [0..1]  716
{Or     Code <Cd> [1..1] CodeSet 717
Or}     Proprietary <Prtry> [1..1] ± 717
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
   EndPrice <EndPric> [0..1]  722
     ValueType <ValTp> [0..1] CodeSet 722
     Value <Val> [1..1] ± 723
     PriceType <PricTp> [0..1] CodeSet 723
   StartValue <StartVal> [0..1] Amount C1, C5 724
   CurrentValue <CurVal> [0..1] Amount C1, C5 724
   EndValue <EndVal> [0..1] Amount C1, C5 725
   AdjustedQuantity <AdjstdQty> [0..1]  725
{Or     Unit <Unit> [1..1] Quantity 725
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 726
   ExchangeRate <XchgRate> [0..1] Rate 726
   CapValue <CapVal> [0..1] Amount C1, C5 726
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 715 August 2026
```

