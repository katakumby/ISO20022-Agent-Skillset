---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.7 IndividualPerson38", "66.1.32.7.18 CivilStatus <CvlSts>"]
file_pages: [5092]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.7.18 CivilStatus <CvlSts>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5092 to 5092.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5092

```text
66.1.32.7.18  CivilStatus <CvlSts>
Presence: [0..1]
Definition: Civil status of the individual person.
CivilStatus <CvlSts> contains one of the following CivilStatus1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5092
Or}   Proprietary <Prtry> [1..1] ± 5092
66.1.32.7.18.1  Code <Cd>
Presence: [1..1]
Definition: Civil status expressed as a code.
Datatype: "CivilStatus1Code" on page 5284
CodeName Name Definition
DIVO Divorced Person is divorced.
LDIV LegallyDivorced Person is legally divorced.
MARR Married Person is married.
SEPA Separated Person is separated.
SING Single Person is single.
UNIO StableUnion Person is in a stable union.
WIDO Widow Person is a widower.
66.1.32.7.18.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Civil status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.32.7.19  EducationLevel <EdctnLvl>
Presence: [0..1]
Definition: Highest level of education reached by the individual person.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5092 May 2026
```

