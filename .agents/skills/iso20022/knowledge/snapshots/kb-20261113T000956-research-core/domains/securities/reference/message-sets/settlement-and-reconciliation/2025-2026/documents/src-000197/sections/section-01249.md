---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.19 Postal Address", "35.1.19.2 PostalAddress1", "35.1.19.2.5 PostCode <PstCd>"]
file_pages: [1706]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.19.2.5 PostCode <PstCd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1706 to 1706.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1706

```text
Datatype: "Max16Text" on page 2191
35.1.19.2.5  PostCode <PstCd>
Presence: [0..1]
Definition: Identifier consisting of a group of letters and/or numbers that is added to a postal address to
assist the sorting of mail.
Datatype: "Max16Text" on page 2191
35.1.19.2.6  TownName <TwnNm>
Presence: [0..1]
Definition: Name of a built-up area, with defined boundaries, and a local government.
Datatype: "Max35Text" on page 2192
35.1.19.2.7  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country for example, state, region, county.
Datatype: "Max35Text" on page 2192
35.1.19.2.8  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government.
Impacted by: C7 "Country"
Datatype: "CountryCode" on page 2057
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
35.1.20 Price
35.1.20.1  PriceInformation30
Definition: Amount of money for which goods or services are offered, sold, or bought.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 1707
   ValueType <ValTp> [1..1] ± 1707
   Value <Val> [1..1] ± 1707
   SourceOfPrice <SrcOfPric> [0..1] ± C35 1707
   QuotationDate <QtnDt> [0..1] ± 1708
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1706 March 2026
```

