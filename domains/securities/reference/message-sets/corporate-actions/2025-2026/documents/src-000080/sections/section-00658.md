---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.5 Date Time", "16.1.5.6 DateAndDateTime2Choice", "16.1.5.6.2 DateTime <DtTm>"]
file_pages: [849]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.5.6.2 DateTime <DtTm>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 849 to 849.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 849

```text
16.1.5.6.2  DateTime <DtTm>
Presence: [1..1]
Definition: Specified date and time.
Datatype: "ISODateTime" on page 1243
16.1.5.7  DateFormat44Choice
Definition: Choice between an ISODate or ISODateTime format or a date code or a date code and a
time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 849
Or   DateCodeAndTime <DtCdAndTm> [1..1]  849
     DateCode <DtCd> [1..1]  850
{Or       Code <Cd> [1..1] CodeSet 850
Or}       Proprietary <Prtry> [1..1] ± 850
     Time <Tm> [1..1] Time 850
Or}   DateCode <DtCd> [1..1]  851
{Or     Code <Cd> [1..1] CodeSet 851
Or}     Proprietary <Prtry> [1..1] ± 851
16.1.5.7.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as a calendar date.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 848 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 848
Or}   DateTime <DtTm> [1..1] DateTime 849
16.1.5.7.2  DateCodeAndTime <DtCdAndTm>
Presence: [1..1]
Definition: Specifies a date code and a time.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 849 February 2026
```

