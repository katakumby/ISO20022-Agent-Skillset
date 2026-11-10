---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.7 IndividualPerson38", "66.1.32.7.7 BirthDate <BirthDt>"]
file_pages: [5085]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.7.7 BirthDate <BirthDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5085 to 5085.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5085

```text
66.1.32.7.7  BirthDate <BirthDt>
Presence: [0..1]
Definition: Date on which the person was born.
Datatype: "ISODate" on page 5388
66.1.32.7.8  CountryOfBirth <CtryOfBirth>
Presence: [0..1]
Definition: Country where the person was born.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.32.7.9  ProvinceOfBirth <PrvcOfBirth>
Presence: [0..1]
Definition: Province where the person was born.
Datatype: "Max35Text" on page 5403
66.1.32.7.10  CityOfBirth <CityOfBirth>
Presence: [0..1]
Definition: City where the person was born.
Datatype: "Max35Text" on page 5403
66.1.32.7.11  Profession <Prfssn>
Presence: [0..1]
Definition: Name of the occupation or job of the person.
Datatype: "Max35Text" on page 5403
66.1.32.7.12  ModifiedPostalAddress <ModfdPstlAdr>
Presence: [0..*]
Definition: Information related to an address to be inserted, updated or deleted.
ModifiedPostalAddress <ModfdPstlAdr> contains the following ModificationScope34 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 5086
   PostalAddress <PstlAdr> [1..1] ± C23 5086
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5085 May 2026
```

