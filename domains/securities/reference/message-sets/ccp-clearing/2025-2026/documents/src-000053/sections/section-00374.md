---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.18 Structured Postal Address"]
file_pages: [467]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.18 Structured Postal Address

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 467 to 467.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 467

```text
12.1.18 Structured Postal Address
12.1.18.1  PostalAddress2
Definition: Address of a party expressed in a formal structure, usually according to the country's postal
services specifications.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StreetName <StrtNm> [0..1] Text 467
   PostCodeIdentification <PstCdId> [1..1] Text 467
   TownName <TwnNm> [1..1] Text 467
   CountrySubDivision <CtrySubDvsn> [0..1] Text 467
   Country <Ctry> [1..1] CodeSet   'C5 467
12.1.18.1.1  StreetName <StrtNm>
Presence: [0..1]
Definition: Name of a street or thoroughfare.
Datatype: Max70Text on page 493
12.1.18.1.2  PostCodeIdentification <PstCdId>
Presence: [1..1]
Definition: Identifier consisting of a group of letters and/or numbers that is added to a postal address to
assist the sorting of mail.
Datatype: Max16Text on page 492
12.1.18.1.3  TownName <TwnNm>
Presence: [1..1]
Definition: Name of a built-up area, with defined boundaries, and a local government.
Datatype: Max35Text on page 493
12.1.18.1.4  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country for example, state, region, county.
Datatype: Max35Text on page 493
12.1.18.1.5  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government.
Impacted by:   'C5 Country  '
Datatype: CountryCode on page 475
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 467
```

