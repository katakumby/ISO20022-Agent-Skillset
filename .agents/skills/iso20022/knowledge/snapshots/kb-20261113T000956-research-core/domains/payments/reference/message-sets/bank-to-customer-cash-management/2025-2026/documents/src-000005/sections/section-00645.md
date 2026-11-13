---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.19 Postal Address", "6.1.19.1 PostalAddress27", "6.1.19.1.12 PostCode <PstCd>"]
file_pages: [878]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.19.1.12 PostCode <PstCd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 878 to 878.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 878

```text
6.1.19.1.12  PostCode <PstCd>
Presence: [0..1]
Definition: Identifier consisting of a group of letters and/or numbers that is added to a postal address to
assist the sorting of mail.
Datatype: "Max16Text" on page 915
6.1.19.1.13  TownName <TwnNm>
Presence: [0..1]
Definition: Name of a built-up area, with defined boundaries, and a local government.
Datatype: "Max140Text" on page 914
6.1.19.1.14  TownLocationName <TwnLctnNm>
Presence: [0..1]
Definition: Specific location name within the town.
Datatype: "Max140Text" on page 914
6.1.19.1.15  DistrictName <DstrctNm>
Presence: [0..1]
Definition: Identifies a subdivision within a country sub-division.
Datatype: "Max140Text" on page 914
6.1.19.1.16  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country such as state, region, county.
Datatype: "Max35Text" on page 916
6.1.19.1.17  Country <Ctry>
Presence: [0..1]
Definition: Nation with its own government.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 892
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
6.1.19.1.18  AddressLine <AdrLine>
Presence: [0..7]
Definition: Information that locates and identifies a specific address, as defined by postal services,
presented in free format text.
Datatype: "Max70Text" on page 917
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
878 March 2026
```

