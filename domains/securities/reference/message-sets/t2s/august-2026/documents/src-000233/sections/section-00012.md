---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.4 Message Building Blocks", "2.4.2 ReportQueryCriteria <RptQryCrit>", "2.4.2.2 SearchCriteria <SchCrit>", "2.4.2.2.1 AccountIdentification <AcctId>"]
file_pages: [42]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.4.2.2.1 AccountIdentification <AcctId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 42 to 42.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 42

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or         FromDate <FrDt> [1..1] Date 51
Or         ToDate <ToDt> [1..1] Date 51
Or         FromToDate <FrToDt> [1..1] ± 52
Or         EqualDate <EQDt> [1..1] Date 52
Or}         NotEqualDate <NEQDt> [1..1] Date 52
   ReportName <RptNm> [0..1] Text 52
   MessageNameIdentification <MsgNmId> [0..1] Text 52
   PartyIdentification <PtyId> [1..1] ± 52
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 53
   DateSearch <DtSch> [0..1]  53
{Or     FromDate <FrDt> [1..1] Date 53
Or     ToDate <ToDt> [1..1] Date 53
Or     FromToDate <FrToDt> [1..1] ± 53
Or     EqualDate <EQDt> [1..1] Date 54
Or}     NotEqualDate <NEQDt> [1..1] Date 54
   ScheduledTime <SchdldTm> [0..1]  54
{Or     FromDateTime <FrDtTm> [1..1] DateTime 54
Or     ToDateTime <ToDtTm> [1..1] DateTime 54
Or}     DateTimeRange <DtTmRg> [1..1] ± 54
   Event <Evt> [0..1]  55
{Or     Code <Cd> [1..1] CodeSet 55
Or}     Proprietary <Prtry> [1..1] Text 55
2.4.2.2.1  AccountIdentification <AcctId>
Presence: [0..*]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
AccountIdentification <AcctId> contains one of the following
AccountIdentificationSearchCriteria2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Equal <EQ> [1..1] ± 43
Or   ContainText <CTTxt> [1..1] Text 43
Or}   NotContainText <NCTTxt> [1..1] Text 43
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.005.001.02 ReportQueryRequestV02
Target2-Securities 42 August 2026
```

