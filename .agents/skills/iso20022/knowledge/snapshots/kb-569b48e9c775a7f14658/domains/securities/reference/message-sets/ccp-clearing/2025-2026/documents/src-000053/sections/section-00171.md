---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.16 TradeLegDetails <TradLegDtls>", "5.4.5.16.19 Broker <Brkr>", "5.4.5.16.19.1 Identification <Id>", "5.4.5.16.19.1.3 NameAndAddress <NmAndAdr>", "5.4.5.16.19.1.3.2 Address <Adr>", "5.4.5.16.19.1.3.2.5 PostCode <PstCd>"]
file_pages: [225]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.16.19.1.3.2.5 PostCode <PstCd>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 225 to 225.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 225

```text
Datatype: Max16Text on page 492
5.4.5.16.19.1.3.2.5  PostCode <PstCd>
Presence: [0..1]
Definition: Identifier consisting of a group of letters and/or numbers that is added to a postal address to
assist the sorting of mail.
Datatype: Max16Text on page 492
5.4.5.16.19.1.3.2.6  TownName <TwnNm>
Presence: [0..1]
Definition: Name of a built-up area, with defined boundaries, and a local government.
Datatype: Max35Text on page 493
5.4.5.16.19.1.3.2.7  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country for example, state, region, county.
Datatype: Max35Text on page 493
5.4.5.16.19.1.3.2.8  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government, occupying a particular territory.
Impacted by:   'C4 Country  '
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
5.4.5.16.19.2  AlternateIdentification <AltrnId>
Presence: [0..1]
Definition: Alternate identification for a party.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 225
```

