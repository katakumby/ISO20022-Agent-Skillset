---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.4 Message Building Blocks", "2.4.2 ReportQueryCriteria <RptQryCrit>", "2.4.2.1 NewQueryName <NewQryNm>"]
file_pages: [10, 11]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.4.2.1 NewQueryName <NewQryNm>

Source: [src-000344](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 10 to 11.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 10

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           NotEqualDateTime <NEQDtTm> [1..1] DateTime 21
Or}         Date <Dt> [1..1]  21
{Or           FromDate <FrDt> [1..1] Date 21
Or           ToDate <ToDt> [1..1] Date 21
Or           FromToDate <FrToDt> [1..1] ± 22
Or           EqualDate <EQDt> [1..1] Date 22
Or}           NotEqualDate <NEQDt> [1..1] Date 22
     ReportName <RptNm> [0..1] Text 22
     MessageNameIdentification <MsgNmId> [0..1] Text 22
     PartyIdentification <PtyId> [1..1] ± 22
     ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 23
     DateSearch <DtSch> [0..1]  23
{Or       FromDate <FrDt> [1..1] Date 23
Or       ToDate <ToDt> [1..1] Date 23
Or       FromToDate <FrToDt> [1..1] ± 23
Or       EqualDate <EQDt> [1..1] Date 24
Or}       NotEqualDate <NEQDt> [1..1] Date 24
     ScheduledTime <SchdldTm> [0..1]  24
{Or       FromDateTime <FrDtTm> [1..1] DateTime 24
Or       ToDateTime <ToDtTm> [1..1] DateTime 24
Or}       DateTimeRange <DtTmRg> [1..1] ± 24
     Event <Evt> [0..1]  25
{Or       Code <Cd> [1..1] CodeSet 25
Or}       Proprietary <Prtry> [1..1] Text 25
2.4.2.1  NewQueryName <NewQryNm>
Presence: [0..1]
Definition: Name of the query defined by the search criteria and return criteria.
Datatype: "Max35Text" on page 69
2.4.2.2  SearchCriteria <SchCrit>
Presence: [1..1]
Definition: Defines the criteria to be used to extract the account information.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.005.001.02 ReportQueryRequestV02
Target2-Securities - Administration - Maintenance 2023 -
2024
10 March 2024
```

## File page 11

```text
SearchCriteria <SchCrit> contains the following ReportQuerySearchCriteria3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [0..*]  12
{Or     Equal <EQ> [1..1] ± 13
Or     ContainText <CTTxt> [1..1] Text 13
Or}     NotContainText <NCTTxt> [1..1] Text 13
   Balance <Bal> [0..*]  C3, C4 13
     Type <Tp> [0..*]  15
{Or       Code <Cd> [1..1] CodeSet 15
Or}       Proprietary <Prtry> [1..1] Text 15
     CounterpartyType <CtrPtyTp> [1..1] CodeSet 15
     CounterpartyIdentification <CtrPtyId> [0..*] ± 16
     ValueDate <ValDt> [0..*]  16
{Or       DateTime <DtTm> [1..1]  17
{Or         FromDateTime <FrDtTm> [1..1] DateTime 17
Or         ToDateTime <ToDtTm> [1..1] DateTime 17
Or         FromToDateTime <FrToDtTm> [1..1] ± 18
Or         EqualDateTime <EQDtTm> [1..1] DateTime 18
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 18
Or}       Date <Dt> [1..1]  18
{Or         FromDate <FrDt> [1..1] Date 18
Or         ToDate <ToDt> [1..1] Date 18
Or         FromToDate <FrToDt> [1..1] ± 19
Or         EqualDate <EQDt> [1..1] Date 19
Or}         NotEqualDate <NEQDt> [1..1] Date 19
     ProcessingDate <PrcgDt> [0..1]  19
{Or       DateTime <DtTm> [1..1]  20
{Or         FromDateTime <FrDtTm> [1..1] DateTime 20
Or         ToDateTime <ToDtTm> [1..1] DateTime 20
Or         FromToDateTime <FrToDtTm> [1..1] ± 21
Or         EqualDateTime <EQDtTm> [1..1] DateTime 21
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 21
Or}       Date <Dt> [1..1]  21
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.005.001.02 ReportQueryRequestV02
Target2-Securities - Administration - Maintenance 2023 -
2024
11 March 2024
```

