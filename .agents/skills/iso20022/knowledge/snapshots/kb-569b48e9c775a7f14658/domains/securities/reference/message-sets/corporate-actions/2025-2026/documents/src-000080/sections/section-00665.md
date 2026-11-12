---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.6 Date Time Period", "16.1.6.5 Period11", "16.1.6.5.1 StartDate <StartDt>", "16.1.6.5.1.1 Date <Dt>"]
file_pages: [856]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.6.5.1.1 Date <Dt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 856 to 856.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 856

```text
StartDate <StartDt> contains one of the following DateFormat45Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 856
Or}   NotSpecifiedDate <NotSpcfdDt> [1..1] CodeSet 856
16.1.6.5.1.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as an ISO Date.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 848 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 848
Or}   DateTime <DtTm> [1..1] DateTime 849
16.1.6.5.1.2  NotSpecifiedDate <NotSpcfdDt>
Presence: [1..1]
Definition: Date not specified, for example, the date is unknown.
Datatype: "DateType8Code" on page 1206
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
ONGO Ongoing Ongoing basis, which indicates that the
date is determined by "ongoing basis"
process, for example "au fil de l'eau".
16.1.6.5.2  EndDate <EndDt>
Presence: [1..1]
Definition: Date and time at which the range ends.
EndDate <EndDt> contains one of the following DateFormat45Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 856
Or}   NotSpecifiedDate <NotSpcfdDt> [1..1] CodeSet 857
16.1.6.5.2.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as an ISO Date.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 856 February 2026
```

