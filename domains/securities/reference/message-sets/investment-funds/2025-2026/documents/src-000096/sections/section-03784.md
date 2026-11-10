---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.3 IndividualPerson37", "66.1.32.3.18 CivilStatus <CvlSts>", "66.1.32.3.18.2 Proprietary <Prtry>"]
file_pages: [5072]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.3.18.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5072 to 5072.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5072

```text
CodeName Name Definition
DIVO Divorced Person is divorced.
LDIV LegallyDivorced Person is legally divorced.
MARR Married Person is married.
SEPA Separated Person is separated.
SING Single Person is single.
UNIO StableUnion Person is in a stable union.
WIDO Widow Person is a widower.
66.1.32.3.18.2  Proprietary <Prtry>
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
66.1.32.3.19  EducationLevel <EdctnLvl>
Presence: [0..1]
Definition: Highest level of education reached by the individual person.
Datatype: "Max35Text" on page 5403
66.1.32.3.20  FamilyInformation <FmlyInf>
Presence: [0..1]
Definition: Information related to the person.
FamilyInformation <FmlyInf> contains the following PersonalInformation1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NameOfFather <NmOfFthr> [0..1] Text 5072
   MaidenNameOfMother <MdnNmOfMthr> [0..1] Text 5073
   NameOfPartner <NmOfPrtnr> [0..1] Text 5073
66.1.32.3.20.1  NameOfFather <NmOfFthr>
Presence: [0..1]
Definition: Name of the father of the individual person.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5072 May 2026
```

