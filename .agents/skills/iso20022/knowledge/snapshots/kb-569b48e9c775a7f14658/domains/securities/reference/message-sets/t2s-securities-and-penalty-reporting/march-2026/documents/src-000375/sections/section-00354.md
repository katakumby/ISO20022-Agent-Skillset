---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.21 Postal Address", "7.1.21.1 PostalAddress27", "7.1.21.1.13 TownName <TwnNm>"]
file_pages: [441]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.21.1.13 TownName <TwnNm>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 441 to 441.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 441

```text
7.1.21.1.13  TownName <TwnNm>
Presence: [0..1]
Definition: Name of a built-up area, with defined boundaries, and a local government.
Datatype: "Max140Text" on page 556
7.1.21.1.14  TownLocationName <TwnLctnNm>
Presence: [0..1]
Definition: Specific location name within the town.
Datatype: "Max140Text" on page 556
7.1.21.1.15  DistrictName <DstrctNm>
Presence: [0..1]
Definition: Identifies a subdivision within a country sub-division.
Datatype: "Max140Text" on page 556
7.1.21.1.16  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country such as state, region, county.
Datatype: "Max35Text" on page 557
7.1.21.1.17  Country <Ctry>
Presence: [0..1]
Definition: Nation with its own government.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 501
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.1.21.1.18  AddressLine <AdrLine>
Presence: [0..7]
Definition: Information that locates and identifies a specific address, as defined by postal services,
presented in free format text.
Datatype: "Max70Text" on page 558
7.1.21.2  PostalAddress1
Definition: Information that locates and identifies a specific address, as defined by postal services.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 441 March 2026
```

