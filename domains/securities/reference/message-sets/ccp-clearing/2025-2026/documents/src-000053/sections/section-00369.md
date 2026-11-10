---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.16 Postal Address", "12.1.16.2 PostalAddress1", "12.1.16.2.5 PostCode <PstCd>"]
file_pages: [462]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.16.2.5 PostCode <PstCd>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 462 to 462.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 462

```text
Datatype: Max16Text on page 492
12.1.16.2.5  PostCode <PstCd>
Presence: [0..1]
Definition: Identifier consisting of a group of letters and/or numbers that is added to a postal address to
assist the sorting of mail.
Datatype: Max16Text on page 492
12.1.16.2.6  TownName <TwnNm>
Presence: [0..1]
Definition: Name of a built-up area, with defined boundaries, and a local government.
Datatype: Max35Text on page 493
12.1.16.2.7  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country for example, state, region, county.
Datatype: Max35Text on page 493
12.1.16.2.8  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government.
Impacted by:   'C5 Country  '
Datatype: CountryCode on page 475
Constraints
• Country
(Rule)
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
Error handling:
– Error severity: Fatal
– Error Code: D00004
– Error Text: Invalid Country Code.
12.1.17 Price
12.1.17.1  Price14
Definition: Provides the value and optionaly the type of price.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 462
```

