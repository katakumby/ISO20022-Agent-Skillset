---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.12 SuspendedStatusReason4Choice", "66.1.45.12.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [5183]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.12.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5183 to 5183.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5183

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5183
Or}   ReasonDetails <RsnDtls> [1..5]  5183
     Reason <Rsn> [1..1]  5183
{Or       Code <Cd> [1..1] CodeSet 5183
Or}       Proprietary <Prtry> [1..1] ± 5184
     AdditionalInformation <AddtlInf> [0..1] Text 5184
66.1.45.12.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: No reason available or to report for the suspended status.
Datatype: "NoReasonCode" on page 5331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
66.1.45.12.2  ReasonDetails <RsnDtls>
Presence: [1..5]
Definition: Reason for the suspended status, expressed as a code.
ReasonDetails <RsnDtls> contains the following SuspendedStatusReason4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  5183
{Or     Code <Cd> [1..1] CodeSet 5183
Or}     Proprietary <Prtry> [1..1] ± 5184
   AdditionalInformation <AddtlInf> [0..1] Text 5184
66.1.45.12.2.1  Reason <Rsn>
Presence: [1..1]
Definition: Reason for the conditionally accepted status expressed as a code.
Reason <Rsn> contains one of the following SuspendedStatusReason5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5183
Or}   Proprietary <Prtry> [1..1] ± 5184
66.1.45.12.2.1.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5183 May 2026
```

