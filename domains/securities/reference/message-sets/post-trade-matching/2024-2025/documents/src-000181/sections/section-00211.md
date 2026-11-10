---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.11 Date Time", "7.1.11.4 SettlementDate16Choice", "7.1.11.4.1 Date <Dt>"]
file_pages: [265]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.11.4.1 Date <Dt>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 265 to 265.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 265

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 265
Or}   Code <Cd> [1..1] ± 265
7.1.11.4.1  Date <Dt>
Presence: [1..1]
Definition: Numeric representation of the day of the month and year.
Date <Dt> contains one of the following elements (see "DateAndDateTime1Choice" on page 263 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 263
Or}   DateTime <DtTm> [1..1] DateTime 263
7.1.11.4.2  Code <Cd>
Presence: [1..1]
Definition: Date and time at which the securities are to be delivered or received.
Code <Cd> contains one of the following elements (see "SettlementDateCode12Choice" on page 266
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 266
Or}   Proprietary <Prtry> [1..1] ± 266
7.1.11.5  DateAndDateTime2Choice
Definition: Choice between a date or a date and time format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 265
Or}   DateTime <DtTm> [1..1] DateTime 265
7.1.11.5.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Datatype: "ISODate" on page 662
7.1.11.5.2  DateTime <DtTm>
Presence: [1..1]
Definition: Specified date and time.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 265 February 2025
```

