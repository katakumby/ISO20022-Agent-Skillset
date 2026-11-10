---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["18 camt.019.001.07 ReturnBusinessDayInformationV07", "18.4 Message Building Blocks", "18.4.2 ReportOrError <RptOrErr>", "18.4.2.1 BusinessReport <BizRpt>", "18.4.2.1.1 SystemIdentification <SysId>"]
file_pages: [543, 544]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.019.001.07"]
---

# 18.4.2.1.1 SystemIdentification <SysId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 543 to 544.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 543

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or             Code <Cd> [1..1] CodeSet 554
Or}             Proprietary <Prtry> [1..1] Text 554
Or}     BusinessError <BizErr> [1..*]  554
       Error <Err> [1..1]  555
{Or         Code <Cd> [1..1] CodeSet 555
Or}         Proprietary <Prtry> [1..1] Text 555
       Description <Desc> [0..1] Text 555
18.4.2.1.1  SystemIdentification <SysId>
Presence: [1..*]
Definition: Identification of a particular market infrastructure.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 846
Or}   Country <Ctry> [1..1] CodeSet C3 846
18.4.2.1.2  BusinessDayOrError <BizDayOrErr>
Presence: [1..1]
Definition: Requested information on the system availability for a specific business day or business
error when information has not been found.
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 543 February 2025
```

## File page 544

```text
BusinessDayOrError <BizDayOrErr> contains one of the following
BusinessDayReportOrError10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BusinessDayInformation <BizDayInf> [1..1]  545
     SystemDate <SysDt> [0..1] ± 547
     SystemStatus <SysSts> [0..1]  547
       Status <Sts> [1..1]  547
{Or         Code <Cd> [1..1] CodeSet 547
Or}         Proprietary <Prtry> [1..1] ± 548
       ValidityTime <VldtyTm> [0..1]  548
{Or         FromDateTime <FrDtTm> [1..1] DateTime 548
Or         ToDateTime <ToDtTm> [1..1] DateTime 548
Or}         DateTimeRange <DtTmRg> [1..1] ± 549
     SystemInformationPerCurrency <SysInfPerCcy> [0..*]  549
       SystemCurrency <SysCcy> [0..1] CodeSet C1 550
       SessionPeriod <SsnPrd> [0..1]  551
         FromTime <FrTm> [1..1] Time 551
         ToTime <ToTm> [1..1] Time 551
       Event <Evt> [0..*]  551
         Type <Tp> [1..1]  551
{Or           Code <Cd> [1..1] CodeSet 552
Or}           Proprietary <Prtry> [1..1] ± 552
         ScheduledTime <SchdldTm> [1..1] DateTime 552
         EffectiveTime <FctvTm> [0..1] DateTime 552
         StartTime <StartTm> [0..1] DateTime 552
         EndTime <EndTm> [0..1] DateTime 552
       ClosureInformation <ClsrInf> [0..*]  553
         Period <Prd> [0..1]  553
{Or           FromDateTime <FrDtTm> [1..1] DateTime 553
Or           ToDateTime <ToDtTm> [1..1] DateTime 553
Or}           DateTimeRange <DtTmRg> [1..1] ± 553
         Reason <Rsn> [1..1]  554
{Or           Code <Cd> [1..1] CodeSet 554
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 544 February 2025
```

