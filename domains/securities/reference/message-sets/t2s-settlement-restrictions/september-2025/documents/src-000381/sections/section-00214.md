---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.16 Postal Address", "9.1.16.2 PostalAddress1", "9.1.16.2.5 PostCode <PstCd>"]
file_pages: [260]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.16.2.5 PostCode <PstCd>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 260 to 260.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 260

```text
Datatype: "Max16Text" on page 344
9.1.16.2.5  PostCode <PstCd>
Presence: [0..1]
Definition: Identifier consisting of a group of letters and/or numbers that is added to a postal address to
assist the sorting of mail.
Datatype: "Max16Text" on page 344
9.1.16.2.6  TownName <TwnNm>
Presence: [0..1]
Definition: Name of a built-up area, with defined boundaries, and a local government.
Datatype: "Max35Text" on page 345
9.1.16.2.7  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country for example, state, region, county.
Datatype: "Max35Text" on page 345
9.1.16.2.8  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government.
Impacted by: C7 "Country"
Datatype: "CountryCode" on page 323
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
9.1.17 Price
9.1.17.1  Price7
Definition: Type and information about a price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 260
   Value <Val> [1..1] ± 261
9.1.17.1.1  Type <Tp>
Presence: [1..1]
Definition: Specification of the price type.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 260 September 2025
```

