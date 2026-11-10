---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["18 camt.019.001.07 ReturnBusinessDayInformationV07", "18.4 Message Building Blocks", "18.4.2 ReportOrError <RptOrErr>", "18.4.2.1 BusinessReport <BizRpt>", "18.4.2.1.2 BusinessDayOrError <BizDayOrErr>", "18.4.2.1.2.1 BusinessDayInformation <BizDayInf>", "18.4.2.1.2.1.2 SystemStatus <SysSts>", "18.4.2.1.2.1.2.1 Status <Sts>", "18.4.2.1.2.1.2.1.2 Proprietary <Prtry>"]
file_pages: [548]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.019.001.07"]
---

# 18.4.2.1.2.1.2.1.2 Proprietary <Prtry>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 548 to 548.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 548

```text
CodeName Name Definition
SUSP Suspended System is suspended, that is, not
operational.
ACTV Active System is functioning normally, that is,
operational.
CLSD Closed System is closed (eg. normal closure of
an RTGS).
CLSG Closing System needs to wait for completion of
intermediate internal activities before
going to a status Closed.
18.4.2.1.2.1.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Status of the system, in a proprietary form.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 809 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 809
   SchemeName <SchmeNm> [0..1] Text 809
   Issuer <Issr> [0..1] Text 809
18.4.2.1.2.1.2.2  ValidityTime <VldtyTm>
Presence: [0..1]
Definition: Period of time during which the status of the system is valid.
ValidityTime <VldtyTm> contains one of the following DateTimePeriod1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 548
Or   ToDateTime <ToDtTm> [1..1] DateTime 548
Or}   DateTimeRange <DtTmRg> [1..1] ± 549
18.4.2.1.2.1.2.2.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODateTime" on page 883
18.4.2.1.2.1.2.2.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the range ends.
Datatype: "ISODateTime" on page 883
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 548 February 2025
```

