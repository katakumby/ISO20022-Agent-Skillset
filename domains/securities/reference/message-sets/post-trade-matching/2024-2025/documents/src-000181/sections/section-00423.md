---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.31 PartyIdentificationAndAccount220", "7.1.20.31.1 Identification <Id>", "7.1.20.31.1.3 NameAndAddress <NmAndAdr>", "7.1.20.31.1.3.2 Address <Adr>", "7.1.20.31.1.3.2.5 PostCode <PstCd>"]
file_pages: [489]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.31.1.3.2.5 PostCode <PstCd>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 489 to 489.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 489

```text
Datatype: "Max16Text" on page 668
7.1.20.31.1.3.2.5  PostCode <PstCd>
Presence: [0..1]
Definition: Identifier consisting of a group of letters and/or numbers that is added to a postal address to
assist the sorting of mail.
Datatype: "Max16Text" on page 668
7.1.20.31.1.3.2.6  TownName <TwnNm>
Presence: [0..1]
Definition: Name of a built-up area, with defined boundaries, and a local government.
Datatype: "Max35Text" on page 669
7.1.20.31.1.3.2.7  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country for example, state, region, county.
Datatype: "Max35Text" on page 669
7.1.20.31.1.3.2.8  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government, occupying a particular territory.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 622
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.1.20.31.2  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
Datatype: "Max35Text" on page 669
7.1.20.31.3  CashAccount <CshAcct>
Presence: [0..1]
Definition: Account to or from which a cash entry is made.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 489 February 2025
```

