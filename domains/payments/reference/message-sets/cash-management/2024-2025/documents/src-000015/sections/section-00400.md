---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["18 camt.019.001.07 ReturnBusinessDayInformationV07", "18.4 Message Building Blocks", "18.4.2 ReportOrError <RptOrErr>", "18.4.2.1 BusinessReport <BizRpt>", "18.4.2.1.2 BusinessDayOrError <BizDayOrErr>", "18.4.2.1.2.1 BusinessDayInformation <BizDayInf>", "18.4.2.1.2.1.3 SystemInformationPerCurrency <SysInfPerCcy>", "18.4.2.1.2.1.3.3 Event <Evt>", "18.4.2.1.2.1.3.3.1 Type <Tp>", "18.4.2.1.2.1.3.3.1.1 Code <Cd>"]
file_pages: [552]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.019.001.07"]
---

# 18.4.2.1.2.1.3.3.1.1 Code <Cd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 552 to 552.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 552

```text
Type <Tp> contains one of the following SystemEventType4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 552
Or}   Proprietary <Prtry> [1..1] ± 552
18.4.2.1.2.1.3.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of system event that has occurred, expressed in a coded form.
Datatype: "ExternalSystemEventType1Code" on page 857
18.4.2.1.2.1.3.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of system event that has occurred, expressed as free text or a bilaterally agreed code.
.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 809 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 809
   SchemeName <SchmeNm> [0..1] Text 809
   Issuer <Issr> [0..1] Text 809
18.4.2.1.2.1.3.3.2  ScheduledTime <SchdldTm>
Presence: [1..1]
Definition: Date and time at which the event is foreseen to occur.
Datatype: "ISODateTime" on page 883
18.4.2.1.2.1.3.3.3  EffectiveTime <FctvTm>
Presence: [0..1]
Definition: Date and time at which the event effectively takes place.
Datatype: "ISODateTime" on page 883
18.4.2.1.2.1.3.3.4  StartTime <StartTm>
Presence: [0..1]
Definition: Time at which the event starts.
Datatype: "ISODateTime" on page 883
18.4.2.1.2.1.3.3.5  EndTime <EndTm>
Presence: [0..1]
Definition: Time at which the event ends.
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 552 February 2025
```

