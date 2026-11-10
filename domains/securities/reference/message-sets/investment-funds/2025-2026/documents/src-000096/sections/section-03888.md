---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.8 AccountStatus2", "66.1.45.8.8 Other <Othr>"]
file_pages: [5179]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.8.8 Other <Othr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5179 to 5179.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5179

```text
ClosurePending <ClsrPdg> contains one of the following elements (see
"ClosurePendingStatusReason1Choice" on page 5168 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5168
Or}   Reason <Rsn> [1..*]  5169
     Code <Cd> [1..1]  5169
{Or       Code <Cd> [1..1] CodeSet 5169
Or}       Proprietary <Prtry> [1..1] ± 5169
     AdditionalInformation <AddtlInf> [0..1] Text 5170
66.1.45.8.8  Other <Othr>
Presence: [0..*]
Definition: Status is a bilaterally agreed status.
Other <Othr> contains the following elements (see "OtherAccountStatus1" on page 5170 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] ± 5170
   Reason <Rsn> [0..1] ± 5170
66.1.45.9  PendingStatusReason1Choice
Definition: Choice of formats for a pending status reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5179
Or}   Reason <Rsn> [1..*] ± 5179
66.1.45.9.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: There is no reason available or to report for the pending account status.
Datatype: "NoReasonCode" on page 5331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
66.1.45.9.2  Reason <Rsn>
Presence: [1..*]
Definition: Reason for the pending account status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5179 May 2026
```

