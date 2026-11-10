---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["3 Message Items Types", "3.1 MessageComponents", "3.1.5 Postal Address", "3.1.5.1 PostalAddress27", "3.1.5.1.13 TownName <TwnNm>"]
file_pages: [49]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.1.5.1.13 TownName <TwnNm>

Source: [src-000011](../../../../../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md). Locator: one-based file pages 49 to 49.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 49

```text
3.1.5.1.13  TownName <TwnNm>
Presence: [0..1]
Definition: Name of a built-up area, with defined boundaries, and a local government.
Datatype: "Max140Text" on page 56
3.1.5.1.14  TownLocationName <TwnLctnNm>
Presence: [0..1]
Definition: Specific location name within the town.
Datatype: "Max140Text" on page 56
3.1.5.1.15  DistrictName <DstrctNm>
Presence: [0..1]
Definition: Identifies a subdivision within a country sub-division.
Datatype: "Max140Text" on page 56
3.1.5.1.16  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country such as state, region, county.
Datatype: "Max35Text" on page 57
3.1.5.1.17  Country <Ctry>
Presence: [0..1]
Definition: Nation with its own government.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 51
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
3.1.5.1.18  AddressLine <AdrLine>
Presence: [0..7]
Definition: Information that locates and identifies a specific address, as defined by postal services,
presented in free format text.
Datatype: "Max70Text" on page 57
3.1.6 System Identification
3.1.6.1  ClearingSystemIdentification2Choice
Definition: Choice of a clearing system identifier.
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Items Types
Business Application Header - Version 4 49 March 2024
```

