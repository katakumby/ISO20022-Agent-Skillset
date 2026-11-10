---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["18 camt.019.001.07 ReturnBusinessDayInformationV07", "18.4 Message Building Blocks", "18.4.2 ReportOrError <RptOrErr>", "18.4.2.1 BusinessReport <BizRpt>", "18.4.2.1.2 BusinessDayOrError <BizDayOrErr>", "18.4.2.1.2.1 BusinessDayInformation <BizDayInf>", "18.4.2.1.2.1.3 SystemInformationPerCurrency <SysInfPerCcy>", "18.4.2.1.2.1.3.2 SessionPeriod <SsnPrd>"]
file_pages: [551]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.019.001.07"]
---

# 18.4.2.1.2.1.3.2 SessionPeriod <SsnPrd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 551 to 551.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 551

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
18.4.2.1.2.1.3.2  SessionPeriod <SsnPrd>
Presence: [0..1]
Definition: Time window of system activity.
SessionPeriod <SsnPrd> contains the following TimePeriod1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromTime <FrTm> [1..1] Time 551
   ToTime <ToTm> [1..1] Time 551
18.4.2.1.2.1.3.2.1  FromTime <FrTm>
Presence: [1..1]
Definition: Time at which the time span starts.
Datatype: "ISOTime" on page 891
18.4.2.1.2.1.3.2.2  ToTime <ToTm>
Presence: [1..1]
Definition: Time at which the time span ends.
Datatype: "ISOTime" on page 891
18.4.2.1.2.1.3.3  Event <Evt>
Presence: [0..*]
Definition: Detailed information about an event occurring on a system, whether planned, such as the
cut-off time for a specific type of eligible transfer, or unplanned (an unsolicited failure), as stipulated in
the specifications of the system.
Event <Evt> contains the following SystemEvent3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  551
{Or     Code <Cd> [1..1] CodeSet 552
Or}     Proprietary <Prtry> [1..1] ± 552
   ScheduledTime <SchdldTm> [1..1] DateTime 552
   EffectiveTime <FctvTm> [0..1] DateTime 552
   StartTime <StartTm> [0..1] DateTime 552
   EndTime <EndTm> [0..1] DateTime 552
18.4.2.1.2.1.3.3.1  Type <Tp>
Presence: [1..1]
Definition: Nature of the event that has occurred.
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 551 February 2025
```

