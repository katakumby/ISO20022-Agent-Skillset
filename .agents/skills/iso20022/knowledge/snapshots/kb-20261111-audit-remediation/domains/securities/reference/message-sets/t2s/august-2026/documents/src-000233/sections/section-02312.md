---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.22 Postal Address", "82.1.22.2 PostalAddress1", "82.1.22.2.5 PostCode <PstCd>"]
file_pages: [3093]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.22.2.5 PostCode <PstCd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3093 to 3093.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3093

```text
Datatype: "Max16Text" on page 3326
82.1.22.2.5  PostCode <PstCd>
Presence: [0..1]
Definition: Identifier consisting of a group of letters and/or numbers that is added to a postal address to
assist the sorting of mail.
Datatype: "Max16Text" on page 3326
82.1.22.2.6  TownName <TwnNm>
Presence: [0..1]
Definition: Name of a built-up area, with defined boundaries, and a local government.
Datatype: "Max35Text" on page 3328
82.1.22.2.7  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country for example, state, region, county.
Datatype: "Max35Text" on page 3328
82.1.22.2.8  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
82.1.22.3  PostalAddress28
Definition: Information that locates and identifies a specific address, as defined by postal services.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3093 August 2026
```

