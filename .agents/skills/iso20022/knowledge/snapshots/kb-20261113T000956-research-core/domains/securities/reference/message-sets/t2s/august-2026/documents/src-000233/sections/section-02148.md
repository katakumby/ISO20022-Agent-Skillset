---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.8 Date Period", "82.1.8.3 DateTimePeriod2"]
file_pages: [2909]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.8.3 DateTimePeriod2

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2909 to 2909.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2909

```text
Definition: End date of the range.
Datatype: "ISODate" on page 3319
82.1.8.3  DateTimePeriod2
Definition: Time span defined by a start date and time, and an end date and time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 2909
   ToDateTime <ToDtTm> [0..1] DateTime 2909
82.1.8.3.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODateTime" on page 3320
82.1.8.3.2  ToDateTime <ToDtTm>
Presence: [0..1]
Definition: Date and time at which the range ends.
Datatype: "ISODateTime" on page 3320
82.1.8.4  Period7Choice
Definition: Choice between date and date-time for the specification of a period.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTimeToDateTime <FrDtTmToDtTm> [1..1] ± 2909
Or}   FromDateToDate <FrDtToDt> [1..1] ± 2909
82.1.8.4.1  FromDateTimeToDateTime <FrDtTmToDtTm>
Presence: [1..1]
Definition: Time span defined by a start date and time, and an end date and time.
FromDateTimeToDateTime <FrDtTmToDtTm> contains the following elements (see
"DateTimePeriod1" on page 2916 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 2916
   ToDateTime <ToDtTm> [1..1] DateTime 2916
82.1.8.4.2  FromDateToDate <FrDtToDt>
Presence: [1..1]
Definition: Time span defined by a start date and time, and an end date and time.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2909 August 2026
```

