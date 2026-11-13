---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.5 Date Time", "16.1.5.1 DateFormat30Choice", "16.1.5.1.2 DateCode <DtCd>", "16.1.5.1.2.1 Code <Cd>"]
file_pages: [843]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.5.1.2.1 Code <Cd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 843 to 843.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 843

```text
DateCode <DtCd> contains one of the following DateCode19Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 843
Or}   Proprietary <Prtry> [1..1] ± 843
16.1.5.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the type of date.
Datatype: "DateType8Code" on page 1206
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
ONGO Ongoing Ongoing basis, which indicates that the
date is determined by "ongoing basis"
process, for example "au fil de l'eau".
16.1.5.1.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of date.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.5.2  DateFormat43Choice
Definition: Choice between an ISODate or ISODateTime format or a date code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
16.1.5.2.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as a calendar date.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 843 February 2026
```

