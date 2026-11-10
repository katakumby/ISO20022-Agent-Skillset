---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.3 IndividualPerson37", "66.1.32.3.8 CountryOfBirth <CtryOfBirth>"]
file_pages: [5066]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.3.8 CountryOfBirth <CtryOfBirth>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5066 to 5066.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5066

```text
66.1.32.3.8  CountryOfBirth <CtryOfBirth>
Presence: [0..1]
Definition: Country where the person was born.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.32.3.9  ProvinceOfBirth <PrvcOfBirth>
Presence: [0..1]
Definition: Province where the person was born.
Datatype: "Max35Text" on page 5403
66.1.32.3.10  CityOfBirth <CityOfBirth>
Presence: [0..1]
Definition: City where the person was born.
Datatype: "Max35Text" on page 5403
66.1.32.3.11  Profession <Prfssn>
Presence: [0..1]
Definition: Name of the occupation or job of the person.
Datatype: "Max35Text" on page 5403
66.1.32.3.12  PostalAddress <PstlAdr>
Presence: [1..10]
Definition: Address of the person.
Impacted by: C23 "MailingIndicatorRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5066 May 2026
```

