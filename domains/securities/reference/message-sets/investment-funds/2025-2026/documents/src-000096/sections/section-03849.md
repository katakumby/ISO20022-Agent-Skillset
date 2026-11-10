---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.39 Securities Identification"]
file_pages: [5138]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.39 Securities Identification

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5138 to 5138.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5138

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification78" on page 4554 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 4554
   Identification <Id> [0..1] Text 4554
66.1.39 Securities Identification
66.1.39.1  AlternateSecurityIdentification1
Definition: Proprietary or domestic identification scheme that uniquely identifies a security.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 5138
{Or   DomesticIdentificationSource <DmstIdSrc> [1..1] CodeSet C12 5138
Or}   ProprietaryIdentificationSource <PrtryIdSrc> [1..1] Text 5138
66.1.39.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a security.
Datatype: "Max35Text" on page 5403
66.1.39.1.2  DomesticIdentificationSource <DmstIdSrc>
Presence: [1..1]
Warning   Either DomesticIdentificationSource or ProprietaryIdentificationSource must be present,
but not both.
Definition: Country of the proprietary identification scheme.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.39.1.3  ProprietaryIdentificationSource <PrtryIdSrc>
Presence: [1..1]
Warning   Either DomesticIdentificationSource or ProprietaryIdentificationSource must be present,
but not both.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5138 May 2026
```

