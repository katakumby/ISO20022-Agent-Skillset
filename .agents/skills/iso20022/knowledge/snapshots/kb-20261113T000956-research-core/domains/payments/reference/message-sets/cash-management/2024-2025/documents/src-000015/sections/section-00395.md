---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["18 camt.019.001.07 ReturnBusinessDayInformationV07", "18.4 Message Building Blocks", "18.4.2 ReportOrError <RptOrErr>", "18.4.2.1 BusinessReport <BizRpt>", "18.4.2.1.2 BusinessDayOrError <BizDayOrErr>", "18.4.2.1.2.1 BusinessDayInformation <BizDayInf>", "18.4.2.1.2.1.1 SystemDate <SysDt>"]
file_pages: [547]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.019.001.07"]
---

# 18.4.2.1.2.1.1 SystemDate <SysDt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 547 to 547.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 547

```text
18.4.2.1.2.1.1  SystemDate <SysDt>
Presence: [0..1]
Definition: Date for which the availability information is provided.
SystemDate <SysDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 801 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 801
Or}   DateTime <DtTm> [1..1] DateTime 801
18.4.2.1.2.1.2  SystemStatus <SysSts>
Presence: [0..1]
Definition: Status of a system and the period of time during which the status is valid.
SystemStatus <SysSts> contains the following SystemStatus3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1]  547
{Or     Code <Cd> [1..1] CodeSet 547
Or}     Proprietary <Prtry> [1..1] ± 548
   ValidityTime <VldtyTm> [0..1]  548
{Or     FromDateTime <FrDtTm> [1..1] DateTime 548
Or     ToDateTime <ToDtTm> [1..1] DateTime 548
Or}     DateTimeRange <DtTmRg> [1..1] ± 549
18.4.2.1.2.1.2.1  Status <Sts>
Presence: [1..1]
Definition: Current status of a system.
Status <Sts> contains one of the following SystemStatus2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 547
Or}   Proprietary <Prtry> [1..1] ± 548
18.4.2.1.2.1.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Status of the system, in a coded form.
Datatype: "SystemStatus2Code" on page 881
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 547 February 2025
```

