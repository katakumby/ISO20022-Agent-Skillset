---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.6 Date Time Period", "16.1.6.1 Period18", "16.1.6.1.1 StartDate <StartDt>"]
file_pages: [852]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.6.1.1 StartDate <StartDt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 852 to 852.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 852

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StartDate <StartDt> [1..1]  852
{Or     Date <Dt> [1..1] Date 852
Or}     NotSpecifiedDate <NotSpcfdDt> [1..1] CodeSet 852
   EndDate <EndDt> [1..1]  852
{Or     Date <Dt> [1..1] Date 853
Or}     NotSpecifiedDate <NotSpcfdDt> [1..1] CodeSet 853
16.1.6.1.1  StartDate <StartDt>
Presence: [1..1]
Definition: Date and time at which the range starts.
StartDate <StartDt> contains one of the following DateFormat73Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 852
Or}   NotSpecifiedDate <NotSpcfdDt> [1..1] CodeSet 852
16.1.6.1.1.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as an ISO Date.
Datatype: "ISODate" on page 1243
16.1.6.1.1.2  NotSpecifiedDate <NotSpcfdDt>
Presence: [1..1]
Definition: Date not specified, for example, the date is unknown.
Datatype: "DateType8Code" on page 1206
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
ONGO Ongoing Ongoing basis, which indicates that the
date is determined by "ongoing basis"
process, for example "au fil de l'eau".
16.1.6.1.2  EndDate <EndDt>
Presence: [1..1]
Definition: Date and time at which the range ends.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 852 February 2026
```

