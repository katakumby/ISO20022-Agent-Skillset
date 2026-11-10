---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.23 Identification Information", "66.1.23.7 GenericIdentification82", "66.1.23.7.3 Issuer <Issr>"]
file_pages: [4543]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.23.7.3 Issuer <Issr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4543 to 4543.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4543

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.23.7.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 5403
66.1.23.7.4  IssueDate <IsseDt>
Presence: [0..1]
Definition: Date at which the identification was issued.
Datatype: "ISODate" on page 5388
66.1.23.7.5  ExpiryDate <XpryDt>
Presence: [0..1]
Definition: Date at which the identification expires.
Datatype: "ISODate" on page 5388
66.1.23.7.6  State <Stat>
Presence: [0..1]
Definition: Name of the state, county or country sub-division that issued the identification document.
Datatype: "Max70Text" on page 5404
66.1.23.7.7  IssuerCountry <IssrCtry>
Presence: [0..1]
Definition: Country that issued the identification document.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.23.8  GenericIdentification81
Definition: Information related to the identification of a party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4543 May 2026
```

