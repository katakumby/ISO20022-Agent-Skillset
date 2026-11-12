---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.11 Date Time", "7.1.11.1 TradeDate8Choice", "7.1.11.1.1 Date <Dt>"]
file_pages: [262]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.11.1.1 Date <Dt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 262 to 262.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 262

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 262
Or}   DateCode <DtCd> [1..1]  262
{Or     Code <Cd> [1..1] CodeSet 262
Or}     Proprietary <Prtry> [1..1] ± 262
7.1.11.1.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as an ISO date.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 265 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 265
Or}   DateTime <DtTm> [1..1] DateTime 265
7.1.11.1.2  DateCode <DtCd>
Presence: [1..1]
Definition: Date expressed as a code.
DateCode <DtCd> contains one of the following TradeDateCode3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 262
Or}   Proprietary <Prtry> [1..1] ± 262
7.1.11.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Trade date expressed as an ISO 20022 code.
Datatype: "DateType3Code" on page 623
CodeName Name Definition
VARI Various Partial trades have occurred over a
period of two or more days.
7.1.11.1.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trade date expressed as a proprietary code.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 262 February 2025
```

