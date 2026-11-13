---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.11 Date Time", "7.1.11.7 TradeDate7Choice"]
file_pages: [267]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.11.7 TradeDate7Choice

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 267 to 267.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 267

```text
Definition: Settlement date expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.11.7  TradeDate7Choice
Definition: expressed as a ISO20022 code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 267
Or}   Value <Val> [1..1]  267
{Or     Code <Cd> [1..1] CodeSet 267
Or}     Proprietary <Prtry> [1..1] ± 268
7.1.11.7.1  Date <Dt>
Presence: [1..1]
Definition: Date and time at which the securities are to be traded.
Date <Dt> contains one of the following elements (see "DateAndDateTime1Choice" on page 263 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 263
Or}   DateTime <DtTm> [1..1] DateTime 263
7.1.11.7.2  Value <Val>
Presence: [1..1]
Definition: Date and time at which the securities are to be traded expressed as a ISO20022 code.
Value <Val> contains one of the following TradingDateCode2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 267
Or}   Proprietary <Prtry> [1..1] ± 268
7.1.11.7.2.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 267 February 2025
```

