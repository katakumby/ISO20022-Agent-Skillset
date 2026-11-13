---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.25 EnabledStatusReason1Choice", "66.1.45.25.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [5203]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.25.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5203 to 5203.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5203

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5203
Or}   Reason <Rsn> [1..*]  5203
     Code <Cd> [1..1]  5203
{Or       Code <Cd> [1..1] CodeSet 5203
Or}       Proprietary <Prtry> [1..1] ± 5204
     AdditionalInformation <AddtlInf> [0..1] Text 5204
66.1.45.25.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: There is no reason available or to report for the enabled account status.
Datatype: "NoReasonCode" on page 5331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
66.1.45.25.2  Reason <Rsn>
Presence: [1..*]
Definition: Reason for the enabled account status.
Reason <Rsn> contains the following EnabledStatusReason1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  5203
{Or     Code <Cd> [1..1] CodeSet 5203
Or}     Proprietary <Prtry> [1..1] ± 5204
   AdditionalInformation <AddtlInf> [0..1] Text 5204
66.1.45.25.2.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the enabled account status.
Code <Cd> contains one of the following EnabledStatusReason2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5203
Or}   Proprietary <Prtry> [1..1] ± 5204
66.1.45.25.2.1.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5203 May 2026
```

