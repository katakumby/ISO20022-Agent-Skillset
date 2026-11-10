---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.5 Date Time", "16.1.5.5 DateFormat59Choice"]
file_pages: [847]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.5.5 DateFormat59Choice

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 847 to 847.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 847

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.5.5  DateFormat59Choice
Definition: Choice between an ISODate or ISODateTime format or a date code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 847
Or}   DateCode <DtCd> [1..1]  847
{Or     Code <Cd> [1..1] CodeSet 847
Or}     Proprietary <Prtry> [1..1] ± 848
16.1.5.5.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as a calendar date.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 848 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 848
Or}   DateTime <DtTm> [1..1] DateTime 849
16.1.5.5.2  DateCode <DtCd>
Presence: [1..1]
Definition: Specifies the type of date.
DateCode <DtCd> contains one of the following DateCode33Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 847
Or}   Proprietary <Prtry> [1..1] ± 848
16.1.5.5.2.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the type of date.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 847 February 2026
```

