---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.4 Message Building Blocks", "2.4.2 ReportQueryCriteria <RptQryCrit>", "2.4.2.2 SearchCriteria <SchCrit>", "2.4.2.2.1 AccountIdentification <AcctId>"]
file_pages: [12]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.4.2.2.1 AccountIdentification <AcctId>

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 12 to 12.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 12

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or         FromDate <FrDt> [1..1] Date 21
Or         ToDate <ToDt> [1..1] Date 21
Or         FromToDate <FrToDt> [1..1] ± 22
Or         EqualDate <EQDt> [1..1] Date 22
Or}         NotEqualDate <NEQDt> [1..1] Date 22
   ReportName <RptNm> [0..1] Text 22
   MessageNameIdentification <MsgNmId> [0..1] Text 22
   PartyIdentification <PtyId> [1..1] ± 22
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 23
   DateSearch <DtSch> [0..1]  23
{Or     FromDate <FrDt> [1..1] Date 23
Or     ToDate <ToDt> [1..1] Date 23
Or     FromToDate <FrToDt> [1..1] ± 23
Or     EqualDate <EQDt> [1..1] Date 24
Or}     NotEqualDate <NEQDt> [1..1] Date 24
   ScheduledTime <SchdldTm> [0..1]  24
{Or     FromDateTime <FrDtTm> [1..1] DateTime 24
Or     ToDateTime <ToDtTm> [1..1] DateTime 24
Or}     DateTimeRange <DtTmRg> [1..1] ± 24
   Event <Evt> [0..1]  25
{Or     Code <Cd> [1..1] CodeSet 25
Or}     Proprietary <Prtry> [1..1] Text 25
2.4.2.2.1  AccountIdentification <AcctId>
Presence: [0..*]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
AccountIdentification <AcctId> contains one of the following
AccountIdentificationSearchCriteria2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Equal <EQ> [1..1] ± 13
Or   ContainText <CTTxt> [1..1] Text 13
Or}   NotContainText <NCTTxt> [1..1] Text 13
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.005.001.02 ReportQueryRequestV02
Target2-Securities - Administration - Maintenance 2023 -
2024
12 March 2024
```

