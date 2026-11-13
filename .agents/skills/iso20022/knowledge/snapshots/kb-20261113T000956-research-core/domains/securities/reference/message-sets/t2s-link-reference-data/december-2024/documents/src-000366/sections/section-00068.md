---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["8 Message Items Types", "8.1 MessageComponents", "8.1.8 Postal Address", "8.1.8.2 PostalAddress1", "8.1.8.2.5 PostCode <PstCd>"]
file_pages: [72]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 8.1.8.2.5 PostCode <PstCd>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 72 to 72.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 72

```text
Datatype: "Max16Text" on page 78
8.1.8.2.5  PostCode <PstCd>
Presence: [0..1]
Definition: Identifier consisting of a group of letters and/or numbers that is added to a postal address to
assist the sorting of mail.
Datatype: "Max16Text" on page 78
8.1.8.2.6  TownName <TwnNm>
Presence: [0..1]
Definition: Name of a built-up area, with defined boundaries, and a local government.
Datatype: "Max35Text" on page 78
8.1.8.2.7  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country for example, state, region, county.
Datatype: "Max35Text" on page 78
8.1.8.2.8  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government.
Impacted by: C2 "Country"
Datatype: "CountryCode" on page 73
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
8.2 Message Datatypes
8.2.1 CodeSet
8.2.1.1  ActiveOrHistoricCurrencyCode
Definition: A code allocated to a currency by a Maintenance Agency under an international identification
scheme, as described in the latest edition of the international standard ISO 4217 "Codes for the
representation of currencies and funds".
Type: CodeSet
Format
pattern [A-Z]{3,3}
Approved by the Securities SEG on 21 November 2024. Message Items Types
Target2-Securities - Link Reference Data 72 December 2024
```

