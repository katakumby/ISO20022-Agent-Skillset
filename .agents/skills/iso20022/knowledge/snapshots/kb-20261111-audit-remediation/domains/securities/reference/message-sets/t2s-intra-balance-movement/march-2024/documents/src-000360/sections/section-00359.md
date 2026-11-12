---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.15 Postal Address", "17.1.15.2 PostalAddress27", "17.1.15.2.14 TownLocationName <TwnLctnNm>"]
file_pages: [425]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.15.2.14 TownLocationName <TwnLctnNm>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 425 to 425.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 425

```text
Datatype: "Max140Text" on page 496
17.1.15.2.14  TownLocationName <TwnLctnNm>
Presence: [0..1]
Definition: Specific location name within the town.
Datatype: "Max140Text" on page 496
17.1.15.2.15  DistrictName <DstrctNm>
Presence: [0..1]
Definition: Identifies a subdivision within a country sub-division.
Datatype: "Max140Text" on page 496
17.1.15.2.16  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country such as state, region, county.
Datatype: "Max35Text" on page 497
17.1.15.2.17  Country <Ctry>
Presence: [0..1]
Definition: Nation with its own government.
Impacted by: C7 "Country"
Datatype: "CountryCode" on page 478
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
17.1.15.2.18  AddressLine <AdrLine>
Presence: [0..7]
Definition: Information that locates and identifies a specific address, as defined by postal services,
presented in free format text.
Datatype: "Max70Text" on page 498
17.1.15.3  PostalAddress1
Definition: Information that locates and identifies a specific address, as defined by postal services.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
425 March 2024
```

