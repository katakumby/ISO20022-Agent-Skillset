---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["18 camt.019.001.07 ReturnBusinessDayInformationV07", "18.4 Message Building Blocks", "18.4.2 ReportOrError <RptOrErr>", "18.4.2.1 BusinessReport <BizRpt>", "18.4.2.1.2 BusinessDayOrError <BizDayOrErr>", "18.4.2.1.2.1 BusinessDayInformation <BizDayInf>", "18.4.2.1.2.1.3 SystemInformationPerCurrency <SysInfPerCcy>", "18.4.2.1.2.1.3.4 ClosureInformation <ClsrInf>"]
file_pages: [553]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.019.001.07"]
---

# 18.4.2.1.2.1.3.4 ClosureInformation <ClsrInf>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 553 to 553.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 553

```text
Datatype: "ISODateTime" on page 883
18.4.2.1.2.1.3.4  ClosureInformation <ClsrInf>
Presence: [0..*]
Definition: Information regarding the closure time of a system.
ClosureInformation <ClsrInf> contains the following SystemClosure2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Period <Prd> [0..1]  553
{Or     FromDateTime <FrDtTm> [1..1] DateTime 553
Or     ToDateTime <ToDtTm> [1..1] DateTime 553
Or}     DateTimeRange <DtTmRg> [1..1] ± 553
   Reason <Rsn> [1..1]  554
{Or     Code <Cd> [1..1] CodeSet 554
Or}     Proprietary <Prtry> [1..1] Text 554
18.4.2.1.2.1.3.4.1  Period <Prd>
Presence: [0..1]
Definition: Period of time when the system is closed/not operating.
Period <Prd> contains one of the following DateTimePeriod1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 553
Or   ToDateTime <ToDtTm> [1..1] DateTime 553
Or}   DateTimeRange <DtTmRg> [1..1] ± 553
18.4.2.1.2.1.3.4.1.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODateTime" on page 883
18.4.2.1.2.1.3.4.1.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the range ends.
Datatype: "ISODateTime" on page 883
18.4.2.1.2.1.3.4.1.3  DateTimeRange <DtTmRg>
Presence: [1..1]
Definition: Range of time between a start date and time and an end date and time.
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 553 February 2025
```

