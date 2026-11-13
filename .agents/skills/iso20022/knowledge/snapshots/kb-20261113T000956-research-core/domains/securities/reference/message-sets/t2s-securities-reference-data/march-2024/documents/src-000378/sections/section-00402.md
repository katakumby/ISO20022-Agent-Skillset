---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.12 Postal Address", "13.1.12.3 PostalAddress1", "13.1.12.3.5 PostCode <PstCd>"]
file_pages: [495]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.12.3.5 PostCode <PstCd>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 495 to 495.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 495

```text
Datatype: "Max16Text" on page 533
13.1.12.3.5  PostCode <PstCd>
Presence: [0..1]
Definition: Identifier consisting of a group of letters and/or numbers that is added to a postal address to
assist the sorting of mail.
Datatype: "Max16Text" on page 533
13.1.12.3.6  TownName <TwnNm>
Presence: [0..1]
Definition: Name of a built-up area, with defined boundaries, and a local government.
Datatype: "Max35Text" on page 534
13.1.12.3.7  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country for example, state, region, county.
Datatype: "Max35Text" on page 534
13.1.12.3.8  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 513
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
13.1.12.4  NameAndAddress5
Definition: Information that locates and identifies a party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 495
   Address <Adr> [0..1] ± 496
13.1.12.4.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 534
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 495 March 2024
```

