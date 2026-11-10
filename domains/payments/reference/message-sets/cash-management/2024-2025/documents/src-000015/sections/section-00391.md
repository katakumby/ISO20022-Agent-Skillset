---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["18 camt.019.001.07 ReturnBusinessDayInformationV07", "18.4 Message Building Blocks", "18.4.1 MessageHeader <MsgHdr>"]
file_pages: [539, 540]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.019.001.07"]
---

# 18.4.1 MessageHeader <MsgHdr>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 539 to 540.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 539

```text
18.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader7" on page 814 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 814
   CreationDateTime <CreDtTm> [0..1] DateTime 814
   RequestType <ReqTp> [0..1]  814
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 814
Or     Enquiry <Enqry> [1..1] CodeSet 815
Or}     Proprietary <Prtry> [1..1] ± 815
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 815
   QueryName <QryNm> [0..1] Text 815
18.4.2 ReportOrError <RptOrErr>
Presence: [1..1]
Definition: Reports on business day information.
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 539 February 2025
```

## File page 540

```text
ReportOrError <RptOrErr> contains one of the following BusinessDayReportOrError9Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BusinessReport <BizRpt> [1..*]  541
     SystemIdentification <SysId> [1..*] ± 543
     BusinessDayOrError <BizDayOrErr> [1..1]  543
{Or       BusinessDayInformation <BizDayInf> [1..1]  545
         SystemDate <SysDt> [0..1] ± 547
         SystemStatus <SysSts> [0..1]  547
           Status <Sts> [1..1]  547
{Or             Code <Cd> [1..1] CodeSet 547
Or}             Proprietary <Prtry> [1..1] ± 548
           ValidityTime <VldtyTm> [0..1]  548
{Or             FromDateTime <FrDtTm> [1..1] DateTime 548
Or             ToDateTime <ToDtTm> [1..1] DateTime 548
Or}             DateTimeRange <DtTmRg> [1..1] ± 549
         SystemInformationPerCurrency <SysInfPerCcy> [0..*]  549
           SystemCurrency <SysCcy> [0..1] CodeSet C1 550
           SessionPeriod <SsnPrd> [0..1]  551
             FromTime <FrTm> [1..1] Time 551
             ToTime <ToTm> [1..1] Time 551
           Event <Evt> [0..*]  551
             Type <Tp> [1..1]  551
{Or               Code <Cd> [1..1] CodeSet 552
Or}               Proprietary <Prtry> [1..1] ± 552
             ScheduledTime <SchdldTm> [1..1] DateTime 552
             EffectiveTime <FctvTm> [0..1] DateTime 552
             StartTime <StartTm> [0..1] DateTime 552
             EndTime <EndTm> [0..1] DateTime 552
           ClosureInformation <ClsrInf> [0..*]  553
             Period <Prd> [0..1]  553
{Or               FromDateTime <FrDtTm> [1..1] DateTime 553
Or               ToDateTime <ToDtTm> [1..1] DateTime 553
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 540 February 2025
```

