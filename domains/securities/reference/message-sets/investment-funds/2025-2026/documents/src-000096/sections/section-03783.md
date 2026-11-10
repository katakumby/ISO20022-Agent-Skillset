---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.3 IndividualPerson37", "66.1.32.3.16 PoliticallyExposedPerson <PltclyXpsdPrsn>", "66.1.32.3.16.2 PoliticallyExposedPersonStatus <PltclyXpsdPrsnSts>", "66.1.32.3.16.2.2 Proprietary <Prtry>"]
file_pages: [5071]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.3.16.2.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5071 to 5071.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5071

```text
CodeName Name Definition
PE02 FamilyMember Family member of the politically exposed
person. A family member includes:
(a) the spouse, or a person considered
to be equivalent to a spouse, of the
politically exposed person,
(b) the children and their spouses, or
persons considered to be equivalent to a
spouse, of the politically exposed
person,
(c) the parents of the politically exposed
person.
66.1.32.3.16.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Status of the politically exposed person expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.32.3.17  DeathDate <DthDt>
Presence: [0..1]
Definition: Date of death.
Datatype: "ISODate" on page 5388
66.1.32.3.18  CivilStatus <CvlSts>
Presence: [0..1]
Definition: Civil status of the individual person.
CivilStatus <CvlSts> contains one of the following CivilStatus1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5071
Or}   Proprietary <Prtry> [1..1] ± 5072
66.1.32.3.18.1  Code <Cd>
Presence: [1..1]
Definition: Civil status expressed as a code.
Datatype: "CivilStatus1Code" on page 5284
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5071 May 2026
```

