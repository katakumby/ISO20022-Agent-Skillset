---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.4 Message Building Blocks", "2.4.2 ReportQueryCriteria <RptQryCrit>"]
file_pages: [8, 9]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.4.2 ReportQueryCriteria <RptQryCrit>

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 8 to 9.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 8

```text
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader7" on page 49 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 49
   CreationDateTime <CreDtTm> [0..1] DateTime 50
   RequestType <ReqTp> [0..1]  50
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 50
Or     Enquiry <Enqry> [1..1] CodeSet 50
Or}     Proprietary <Prtry> [1..1] ± 50
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 51
   QueryName <QryNm> [0..1] Text 51
2.4.2 ReportQueryCriteria <RptQryCrit>
Presence: [0..*]
Definition: Definition of the report query criteria.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.005.001.02 ReportQueryRequestV02
Target2-Securities - Administration - Maintenance 2023 -
2024
8 March 2024
```

## File page 9

```text
ReportQueryCriteria <RptQryCrit> contains the following ReportQueryCriteria3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NewQueryName <NewQryNm> [0..1] Text 10
   SearchCriteria <SchCrit> [1..1]  10
     AccountIdentification <AcctId> [0..*]  12
{Or       Equal <EQ> [1..1] ± 13
Or       ContainText <CTTxt> [1..1] Text 13
Or}       NotContainText <NCTTxt> [1..1] Text 13
     Balance <Bal> [0..*]  C3, C4 13
       Type <Tp> [0..*]  15
{Or         Code <Cd> [1..1] CodeSet 15
Or}         Proprietary <Prtry> [1..1] Text 15
       CounterpartyType <CtrPtyTp> [1..1] CodeSet 15
       CounterpartyIdentification <CtrPtyId> [0..*] ± 16
       ValueDate <ValDt> [0..*]  16
{Or         DateTime <DtTm> [1..1]  17
{Or           FromDateTime <FrDtTm> [1..1] DateTime 17
Or           ToDateTime <ToDtTm> [1..1] DateTime 17
Or           FromToDateTime <FrToDtTm> [1..1] ± 18
Or           EqualDateTime <EQDtTm> [1..1] DateTime 18
Or}           NotEqualDateTime <NEQDtTm> [1..1] DateTime 18
Or}         Date <Dt> [1..1]  18
{Or           FromDate <FrDt> [1..1] Date 18
Or           ToDate <ToDt> [1..1] Date 18
Or           FromToDate <FrToDt> [1..1] ± 19
Or           EqualDate <EQDt> [1..1] Date 19
Or}           NotEqualDate <NEQDt> [1..1] Date 19
       ProcessingDate <PrcgDt> [0..1]  19
{Or         DateTime <DtTm> [1..1]  20
{Or           FromDateTime <FrDtTm> [1..1] DateTime 20
Or           ToDateTime <ToDtTm> [1..1] DateTime 20
Or           FromToDateTime <FrToDtTm> [1..1] ± 21
Or           EqualDateTime <EQDtTm> [1..1] DateTime 21
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.005.001.02 ReportQueryRequestV02
Target2-Securities - Administration - Maintenance 2023 -
2024
9 March 2024
```

