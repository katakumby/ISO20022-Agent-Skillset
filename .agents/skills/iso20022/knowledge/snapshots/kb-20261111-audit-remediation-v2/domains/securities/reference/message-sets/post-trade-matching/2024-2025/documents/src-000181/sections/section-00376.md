---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.16 PartyIdentification117Choice", "7.1.20.16.3 NameAndAddress <NmAndAdr>", "7.1.20.16.3.2 Address <Adr>", "7.1.20.16.3.2.5 PostCode <PstCd>"]
file_pages: [441]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.16.3.2.5 PostCode <PstCd>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 441 to 441.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 441

```text
Datatype: "Max16Text" on page 668
7.1.20.16.3.2.5  PostCode <PstCd>
Presence: [0..1]
Definition: Identifier consisting of a group of letters and/or numbers that is added to a postal address to
assist the sorting of mail.
Datatype: "Max16Text" on page 668
7.1.20.16.3.2.6  TownName <TwnNm>
Presence: [0..1]
Definition: Name of a built-up area, with defined boundaries, and a local government.
Datatype: "Max35Text" on page 669
7.1.20.16.3.2.7  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country for example, state, region, county.
Datatype: "Max35Text" on page 669
7.1.20.16.3.2.8  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government, occupying a particular territory.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 622
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.1.20.17  PartyTextInformation5
Definition: Provides additional information regarding the party, eg, the contact unit or person
responsible for the transaction identified in the message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 442
   PartyContactDetails <PtyCtctDtls> [0..1] Text 442
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 441 February 2025
```

