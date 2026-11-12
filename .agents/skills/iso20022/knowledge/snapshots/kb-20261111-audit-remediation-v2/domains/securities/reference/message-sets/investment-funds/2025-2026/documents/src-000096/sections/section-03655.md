---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.29 Organisation Identification", "66.1.29.7 Organisation36", "66.1.29.7.4 TaxationCountry <TaxtnCtry>"]
file_pages: [4905]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.29.7.4 TaxationCountry <TaxtnCtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4905 to 4905.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4905

```text
Definition: Purpose of the organisation, for example, charity.
Datatype: "Max35Text" on page 5403
66.1.29.7.4  TaxationCountry <TaxtnCtry>
Presence: [0..1]
Definition: Country of taxation of the organisation.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.29.7.5  RegistrationCountry <RegnCtry>
Presence: [0..1]
Definition: Country in which the organisation is registered.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.29.7.6  RegistrationDate <RegnDt>
Presence: [0..1]
Definition: Date and time at which the organisation was officially registered.
Datatype: "ISODate" on page 5388
66.1.29.7.7  TaxIdentificationNumber <TaxIdNb>
Presence: [0..1]
Definition: Number assigned by a tax authority to the organisation.
Datatype: "Max35Text" on page 5403
66.1.29.7.8  NationalRegistrationNumber <NtlRegnNb>
Presence: [0..1]
Definition: Number assigned by a national registration authority to the organisation.
Datatype: "Max35Text" on page 5403
66.1.29.7.9  CorporateInvestorAddress <CorpInvstrAdr>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4905 May 2026
```

