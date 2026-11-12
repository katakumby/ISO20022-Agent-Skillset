---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.6 TradeLegDetails <TradLegDtls>", "2.4.6.23 Broker <Brkr>", "2.4.6.23.1 Identification <Id>", "2.4.6.23.1.3 NameAndAddress <NmAndAdr>", "2.4.6.23.1.3.2 Address <Adr>", "2.4.6.23.1.3.2.5 PostCode <PstCd>"]
file_pages: [56]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.6.23.1.3.2.5 PostCode <PstCd>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 56 to 56.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 56

```text
Datatype: Max16Text on page 492
2.4.6.23.1.3.2.5  PostCode <PstCd>
Presence: [0..1]
Definition: Identifier consisting of a group of letters and/or numbers that is added to a postal address to
assist the sorting of mail.
Datatype: Max16Text on page 492
2.4.6.23.1.3.2.6  TownName <TwnNm>
Presence: [0..1]
Definition: Name of a built-up area, with defined boundaries, and a local government.
Datatype: Max35Text on page 493
2.4.6.23.1.3.2.7  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country for example, state, region, county.
Datatype: Max35Text on page 493
2.4.6.23.1.3.2.8  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government, occupying a particular territory.
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
2.4.6.23.2  AlternateIdentification <AltrnId>
Presence: [0..1]
Definition: Alternate identification for a party.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 56
```

