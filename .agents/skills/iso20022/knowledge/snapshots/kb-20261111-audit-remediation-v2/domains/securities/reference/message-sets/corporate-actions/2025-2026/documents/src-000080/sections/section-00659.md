---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.5 Date Time", "16.1.5.7 DateFormat44Choice", "16.1.5.7.2 DateCodeAndTime <DtCdAndTm>", "16.1.5.7.2.1 DateCode <DtCd>"]
file_pages: [850]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.5.7.2.1 DateCode <DtCd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 850 to 850.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 850

```text
DateCodeAndTime <DtCdAndTm> contains the following DateCodeAndTimeFormat3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateCode <DtCd> [1..1]  850
{Or     Code <Cd> [1..1] CodeSet 850
Or}     Proprietary <Prtry> [1..1] ± 850
   Time <Tm> [1..1] Time 850
16.1.5.7.2.1  DateCode <DtCd>
Presence: [1..1]
Definition: Specifies the type of date.
DateCode <DtCd> contains one of the following DateCode21Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 850
Or}   Proprietary <Prtry> [1..1] ± 850
16.1.5.7.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the type of date.
Datatype: "DateType7Code" on page 1205
CodeName Name Definition
ONGO Ongoing Ongoing basis, which indicates that the
date is determined by "ongoing basis"
process, for example "au fil de l'eau".
16.1.5.7.2.1.2  Proprietary <Prtry>
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
16.1.5.7.2.2  Time <Tm>
Presence: [1..1]
Definition: Specifies the time.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 850 February 2026
```

