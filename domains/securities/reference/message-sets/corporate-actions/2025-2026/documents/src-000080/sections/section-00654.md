---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.5 Date Time", "16.1.5.3 DateFormat57Choice", "16.1.5.3.1 Date <Dt>"]
file_pages: [845]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.5.3.1 Date <Dt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 845 to 845.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 845

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 845
Or}   DateCode <DtCd> [1..1]  845
{Or     Code <Cd> [1..1] CodeSet 845
Or}     Proprietary <Prtry> [1..1] ± 845
16.1.5.3.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as a calendar date.
Datatype: "ISODate" on page 1243
16.1.5.3.2  DateCode <DtCd>
Presence: [1..1]
Definition: Date is expressed using a code.
DateCode <DtCd> contains one of the following DateCode20Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 845
Or}   Proprietary <Prtry> [1..1] ± 845
16.1.5.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to indicate the date is unknown.
Datatype: "DateType1Code" on page 1205
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
16.1.5.3.2.2  Proprietary <Prtry>
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 845 February 2026
```

