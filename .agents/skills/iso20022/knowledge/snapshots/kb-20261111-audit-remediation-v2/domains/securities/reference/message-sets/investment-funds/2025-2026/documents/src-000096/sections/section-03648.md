---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.29 Organisation Identification", "66.1.29.5 Organisation39", "66.1.29.5.6 RegistrationCountry <RegnCtry>"]
file_pages: [4898]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.29.5.6 RegistrationCountry <RegnCtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4898 to 4898.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4898

```text
66.1.29.5.6  RegistrationCountry <RegnCtry>
Presence: [0..1]
Definition: Country in which the organisation is registered.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.29.5.7  RegistrationDate <RegnDt>
Presence: [0..1]
Definition: Date and time at which a given organisation was officially registered.
Datatype: "ISODate" on page 5388
66.1.29.5.8  PostalAddress <PstlAdr>
Presence: [0..10]
Definition: Information that locates and identifies a specific address, as defined by postal services.
Impacted by: C23 "MailingIndicatorRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4898 May 2026
```

