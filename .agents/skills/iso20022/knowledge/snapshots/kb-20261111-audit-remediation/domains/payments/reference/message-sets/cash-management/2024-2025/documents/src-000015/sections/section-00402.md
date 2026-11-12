---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["18 camt.019.001.07 ReturnBusinessDayInformationV07", "18.4 Message Building Blocks", "18.4.2 ReportOrError <RptOrErr>", "18.4.2.1 BusinessReport <BizRpt>", "18.4.2.1.2 BusinessDayOrError <BizDayOrErr>", "18.4.2.1.2.1 BusinessDayInformation <BizDayInf>", "18.4.2.1.2.1.3 SystemInformationPerCurrency <SysInfPerCcy>", "18.4.2.1.2.1.3.4 ClosureInformation <ClsrInf>", "18.4.2.1.2.1.3.4.2 Reason <Rsn>"]
file_pages: [554]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.019.001.07"]
---

# 18.4.2.1.2.1.3.4.2 Reason <Rsn>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 554 to 554.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 554

```text
DateTimeRange <DtTmRg> contains the following elements (see "DateTimePeriod1" on page 801 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 802
   ToDateTime <ToDtTm> [1..1] DateTime 802
18.4.2.1.2.1.3.4.2  Reason <Rsn>
Presence: [1..1]
Definition: Reason the system is closed/not operating.
Reason <Rsn> contains one of the following ClosureReason2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 554
Or}   Proprietary <Prtry> [1..1] Text 554
18.4.2.1.2.1.3.4.2.1  Code <Cd>
Presence: [1..1]
Definition: Reason the system is closed/not operating, in a coded form.
Datatype: "SystemClosureReason1Code" on page 879
CodeName Name Definition
BHOL BankingHoliday System is closed due to a bank holiday.
SMTN SystemMaintenance System is closed for maintenance
reasons.
NOOP NoOperation System is not processing any operation.
RCVR Recovery System is not operational during
recovery operations.
ADTW AllowedDowntimeWindow System is not operational during allowed
downtime windows.
18.4.2.1.2.1.3.4.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason the system is closed/not operating, in a bilateral agreed code.
Datatype: "Max35Text" on page 889
18.4.2.1.2.2  BusinessError <BizErr>
Presence: [1..*]
Definition: Reason the requested business information is not given.
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 554 February 2025
```

