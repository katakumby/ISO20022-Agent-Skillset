---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.22 Postal Address", "82.1.22.1 PostalAddress27", "82.1.22.1.14 TownLocationName <TwnLctnNm>"]
file_pages: [3091]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.22.1.14 TownLocationName <TwnLctnNm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3091 to 3091.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3091

```text
Datatype: "Max140Text" on page 3326
82.1.22.1.14  TownLocationName <TwnLctnNm>
Presence: [0..1]
Definition: Specific location name within the town.
Datatype: "Max140Text" on page 3326
82.1.22.1.15  DistrictName <DstrctNm>
Presence: [0..1]
Definition: Identifies a subdivision within a country sub-division.
Datatype: "Max140Text" on page 3326
82.1.22.1.16  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country such as state, region, county.
Datatype: "Max35Text" on page 3328
82.1.22.1.17  Country <Ctry>
Presence: [0..1]
Definition: Nation with its own government.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
82.1.22.1.18  AddressLine <AdrLine>
Presence: [0..7]
Definition: Information that locates and identifies a specific address, as defined by postal services,
presented in free format text.
Datatype: "Max70Text" on page 3329
82.1.22.2  PostalAddress1
Definition: Information that locates and identifies a specific address, as defined by postal services.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3091 August 2026
```

