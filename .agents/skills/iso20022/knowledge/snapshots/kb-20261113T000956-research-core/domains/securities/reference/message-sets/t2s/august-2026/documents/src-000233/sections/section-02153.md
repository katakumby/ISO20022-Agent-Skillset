---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.9 Date Time", "82.1.9.6 DateAndDateTime2Choice"]
file_pages: [2914]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.9.6 DateAndDateTime2Choice

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2914 to 2914.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2914

```text
82.1.9.6  DateAndDateTime2Choice
Definition: Choice between a date or a date and time format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
82.1.9.6.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Datatype: "ISODate" on page 3319
82.1.9.6.2  DateTime <DtTm>
Presence: [1..1]
Definition: Specified date and time.
Datatype: "ISODateTime" on page 3320
82.1.9.7  SettlementDate19Choice
Definition: Choice of format for the settlement date.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 2914
Or}   DateCode <DtCd> [1..1] ± 2914
82.1.9.7.1  Date <Dt>
Presence: [1..1]
Definition: Date in ISO format.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 2914 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
82.1.9.7.2  DateCode <DtCd>
Presence: [1..1]
Definition: Date and time at which the securities are to be delivered or received.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2914 August 2026
```

