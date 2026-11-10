---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.4 Message Building Blocks", "2.4.2 ReportQueryCriteria <RptQryCrit>", "2.4.2.1 NewQueryName <NewQryNm>"]
file_pages: [40, 41]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.4.2.1 NewQueryName <NewQryNm>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 40 to 41.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 40

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           NotEqualDateTime <NEQDtTm> [1..1] DateTime 51
Or}         Date <Dt> [1..1]  51
{Or           FromDate <FrDt> [1..1] Date 51
Or           ToDate <ToDt> [1..1] Date 51
Or           FromToDate <FrToDt> [1..1] ± 52
Or           EqualDate <EQDt> [1..1] Date 52
Or}           NotEqualDate <NEQDt> [1..1] Date 52
     ReportName <RptNm> [0..1] Text 52
     MessageNameIdentification <MsgNmId> [0..1] Text 52
     PartyIdentification <PtyId> [1..1] ± 52
     ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 53
     DateSearch <DtSch> [0..1]  53
{Or       FromDate <FrDt> [1..1] Date 53
Or       ToDate <ToDt> [1..1] Date 53
Or       FromToDate <FrToDt> [1..1] ± 53
Or       EqualDate <EQDt> [1..1] Date 54
Or}       NotEqualDate <NEQDt> [1..1] Date 54
     ScheduledTime <SchdldTm> [0..1]  54
{Or       FromDateTime <FrDtTm> [1..1] DateTime 54
Or       ToDateTime <ToDtTm> [1..1] DateTime 54
Or}       DateTimeRange <DtTmRg> [1..1] ± 54
     Event <Evt> [0..1]  55
{Or       Code <Cd> [1..1] CodeSet 55
Or}       Proprietary <Prtry> [1..1] Text 55
2.4.2.1  NewQueryName <NewQryNm>
Presence: [0..1]
Definition: Name of the query defined by the search criteria and return criteria.
Datatype: "Max35Text" on page 3328
2.4.2.2  SearchCriteria <SchCrit>
Presence: [1..1]
Definition: Defines the criteria to be used to extract the account information.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.005.001.02 ReportQueryRequestV02
Target2-Securities 40 August 2026
```

## File page 41

```text
SearchCriteria <SchCrit> contains the following ReportQuerySearchCriteria3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [0..*]  42
{Or     Equal <EQ> [1..1] ± 43
Or     ContainText <CTTxt> [1..1] Text 43
Or}     NotContainText <NCTTxt> [1..1] Text 43
   Balance <Bal> [0..*]  C3, C4 43
     Type <Tp> [0..*]  45
{Or       Code <Cd> [1..1] CodeSet 45
Or}       Proprietary <Prtry> [1..1] Text 45
     CounterpartyType <CtrPtyTp> [1..1] CodeSet 45
     CounterpartyIdentification <CtrPtyId> [0..*] ± 46
     ValueDate <ValDt> [0..*]  46
{Or       DateTime <DtTm> [1..1]  47
{Or         FromDateTime <FrDtTm> [1..1] DateTime 47
Or         ToDateTime <ToDtTm> [1..1] DateTime 47
Or         FromToDateTime <FrToDtTm> [1..1] ± 48
Or         EqualDateTime <EQDtTm> [1..1] DateTime 48
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 48
Or}       Date <Dt> [1..1]  48
{Or         FromDate <FrDt> [1..1] Date 48
Or         ToDate <ToDt> [1..1] Date 48
Or         FromToDate <FrToDt> [1..1] ± 49
Or         EqualDate <EQDt> [1..1] Date 49
Or}         NotEqualDate <NEQDt> [1..1] Date 49
     ProcessingDate <PrcgDt> [0..1]  49
{Or       DateTime <DtTm> [1..1]  50
{Or         FromDateTime <FrDtTm> [1..1] DateTime 50
Or         ToDateTime <ToDtTm> [1..1] DateTime 50
Or         FromToDateTime <FrToDtTm> [1..1] ± 51
Or         EqualDateTime <EQDtTm> [1..1] DateTime 51
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 51
Or}       Date <Dt> [1..1]  51
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.005.001.02 ReportQueryRequestV02
Target2-Securities 41 August 2026
```

